// Cloudflare Pages Function: /api/tests
//
// POST saves one test result (sent by /test.js) as a new row in the Google Sheet.
// GET  checks the setup and answers {"ok": true} when the sheet can be reached, with
//      "header": "empty" | "old" | "current" (old = no separate "Uzvārds" column yet).
//
// Columns: Laiks, Tests, Klase, Vārds, Uzvārds, Punkti, No, then one per question.
// A sheet started earlier has no "Uzvārds" column; its rows keep the full name in "Vārds"
// until a column "Uzvārds" is inserted left of "Punkti" (column E). Then rows split by themselves.
//
// Setup, done once:
//   1. Google Cloud, project "ebskolasheet": enable "Google Sheets API".
//   2. Service account "ebapi" -> Keys -> Add key -> Create new key -> JSON.
//   3. Share the Google Sheet with the service account's email as Editor.
//   4. Cloudflare Pages -> Settings -> Variables and Secrets -> add the secret
//      GOOGLE_SERVICE_ACCOUNT_JSON = the whole content of the downloaded JSON file.
//      Then redeploy. Never commit the JSON file to this repository.

const SHEET_ID = "1w5BbnJJ1YUyZqJHmi3LzQEWp6iySepI_ksfUdXYGHNw";
const SHEET_API = "https://sheets.googleapis.com/v4/spreadsheets/" + SHEET_ID + "/values/";
const TOKEN_URL = "https://oauth2.googleapis.com/token";
// A range without a tab name means the first tab, whatever it is called.
const FIRST_CELL = "A1";

const CLASSES = ["9.a", "9.b", "9.c"];
const MAX_QUESTIONS = 10;
const HEADER = ["Laiks", "Tests", "Klase", "Vārds", "Uzvārds", "Punkti", "No"];
// Header row of sheets started before surnames got their own column: E1 is "Punkti".
// Rows for such a sheet keep the full name in "Vārds" until the teacher inserts the column.
const HEADER_ROW = "A1:G1";
const MAX_NAME = 40;

// Reused while the same worker instance stays alive.
let cachedToken = null;
// Set once the sheet has the current header. A sheet never goes back to the old layout,
// so only this state is cached; an empty or old-layout sheet is checked again on each result.
let headerCurrent = false;

class SetupError extends Error {
  constructor(code, detail) {
    super(detail);
    this.code = code;
  }
}

function json(body, status) {
  return new Response(JSON.stringify(body), {
    status: status || 200,
    headers: { "Content-Type": "application/json; charset=utf-8", "Cache-Control": "no-store" },
  });
}

function base64url(input) {
  const bytes = typeof input === "string" ? new TextEncoder().encode(input) : new Uint8Array(input);
  let binary = "";
  for (const byte of bytes) binary += String.fromCharCode(byte);
  return btoa(binary).replace(/\+/g, "-").replace(/\//g, "_").replace(/=+$/, "");
}

async function accessToken(env) {
  const now = Math.floor(Date.now() / 1000);
  if (cachedToken && cachedToken.expires > now + 60) return cachedToken.value;

  let account;
  try {
    account = JSON.parse(env.GOOGLE_SERVICE_ACCOUNT_JSON);
  } catch (_) {
    throw new SetupError("config", "Secret GOOGLE_SERVICE_ACCOUNT_JSON is missing or is not the JSON key file.");
  }
  if (!account || !account.client_email || !account.private_key) {
    throw new SetupError("config", "GOOGLE_SERVICE_ACCOUNT_JSON has no client_email or private_key.");
  }

  const claims = {
    iss: account.client_email,
    scope: "https://www.googleapis.com/auth/spreadsheets",
    aud: TOKEN_URL,
    iat: now,
    exp: now + 3600,
  };
  const unsigned = base64url(JSON.stringify({ alg: "RS256", typ: "JWT" })) + "." + base64url(JSON.stringify(claims));
  let signature;
  try {
    const pem = account.private_key.replace(/-----[^-]+-----/g, "").replace(/\s+/g, "");
    const der = Uint8Array.from(atob(pem), function (char) { return char.charCodeAt(0); });
    const key = await crypto.subtle.importKey("pkcs8", der, { name: "RSASSA-PKCS1-v1_5", hash: "SHA-256" }, false, ["sign"]);
    signature = await crypto.subtle.sign("RSASSA-PKCS1-v1_5", key, new TextEncoder().encode(unsigned));
  } catch (_) {
    throw new SetupError("config", "The private_key in GOOGLE_SERVICE_ACCOUNT_JSON cannot be read.");
  }

  const response = await fetch(TOKEN_URL, {
    method: "POST",
    headers: { "Content-Type": "application/x-www-form-urlencoded" },
    body: new URLSearchParams({
      grant_type: "urn:ietf:params:oauth:grant-type:jwt-bearer",
      assertion: unsigned + "." + base64url(signature),
    }),
  });
  const data = await response.json().catch(function () { return {}; });
  if (!response.ok || !data.access_token) {
    throw new SetupError("auth", data.error_description || data.error || "Google refused the service account key.");
  }
  cachedToken = { value: data.access_token, expires: now + (data.expires_in || 3600) };
  return cachedToken.value;
}

async function sheets(env, path, options) {
  const token = await accessToken(env);
  const request = Object.assign({}, options);
  request.headers = Object.assign({ Authorization: "Bearer " + token }, request.headers);
  const response = await fetch(SHEET_API + path, request);
  const data = await response.json().catch(function () { return {}; });
  if (!response.ok) {
    throw new SetupError("sheet", (data.error && data.error.message) || "Google Sheets answered " + response.status + ".");
  }
  return data;
}

// "empty" (nothing written yet), "old" (no Uzvārds column) or "current".
async function headerLayout(env) {
  const data = await sheets(env, HEADER_ROW);
  const row = (data.values && data.values[0]) || [];
  if (!row.some(function (cell) { return String(cell).trim(); })) return "empty";
  return String(row[4] || "").trim() === "Punkti" ? "old" : "current";
}

function fail(error) {
  if (error instanceof SetupError) {
    console.error("tests:", error.code, error.message);
    return json({ ok: false, error: error.code, detail: error.message }, 502);
  }
  console.error("tests:", error);
  return json({ ok: false, error: "server" }, 500);
}

// The result comes from a public page, so nothing in it is trusted.
function readResult(body) {
  if (!body || typeof body !== "object") return null;
  const test = typeof body.test === "string" ? body.test : "";
  let vards = clean(body.vards);
  let uzvards = clean(body.uzvards);
  if (!vards && !uzvards) {
    // Pages opened before the name was split send one "name": first word is the given name.
    const full = clean(body.name);
    if (full.length > 60) return null;
    const space = full.indexOf(" ");
    vards = space < 0 ? full : full.slice(0, space);
    uzvards = space < 0 ? "" : full.slice(space + 1);
  }
  const answers = body.answers;
  if (!/^[a-z0-9_]{3,40}$/.test(test)) return null;
  if (!vards || vards.length > MAX_NAME || uzvards.length > MAX_NAME) return null;
  if ((vards + uzvards).length < 2) return null;
  if (!CLASSES.includes(body.klase)) return null;
  if (!Array.isArray(answers) || answers.length < 1 || answers.length > MAX_QUESTIONS) return null;
  for (const answer of answers) {
    if (!answer || typeof answer.a !== "string" || !/^[A-D]$/.test(answer.a) || typeof answer.ok !== "boolean") return null;
  }
  return { test: test, vards: vards, uzvards: uzvards, klase: body.klase, answers: answers };
}

function clean(value) {
  return typeof value === "string" ? value.replace(/\s+/g, " ").trim() : "";
}

export async function onRequestPost(context) {
  const request = context.request;
  const origin = request.headers.get("Origin");
  if (origin && origin !== new URL(request.url).origin) return json({ ok: false, error: "origin" }, 403);

  const text = await request.text();
  if (text.length > 4000) return json({ ok: false, error: "too-large" }, 413);
  let body;
  try {
    body = JSON.parse(text);
  } catch (_) {
    return json({ ok: false, error: "invalid" }, 400);
  }
  const result = readResult(body);
  if (!result) return json({ ok: false, error: "invalid" }, 400);

  const time = new Date().toLocaleString("sv-SE", { timeZone: "Europe/Riga" });
  const score = result.answers.filter(function (answer) { return answer.ok; }).length;
  const marks = result.answers.map(function (answer) { return answer.a + (answer.ok ? " ✓" : " ✗"); });

  try {
    const layout = headerCurrent ? "current" : await headerLayout(context.env);
    const name = layout === "old"
      ? [(result.vards + " " + result.uzvards).trim()]
      : [result.vards, result.uzvards];
    const rows = [[time, result.test, result.klase].concat(name, [score, result.answers.length], marks)];
    if (layout === "empty") {
      rows.unshift(HEADER.concat(result.answers.map(function (_, index) { return (index + 1) + ". jautājums"; })));
    }
    // RAW stores the name as plain text, so it can never run as a formula.
    await sheets(context.env, FIRST_CELL + ":append?valueInputOption=RAW&insertDataOption=INSERT_ROWS", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ values: rows }),
    });
    if (layout !== "old") headerCurrent = true;
  } catch (error) {
    return fail(error);
  }
  return json({ ok: true });
}

export async function onRequestGet(context) {
  let layout;
  try {
    layout = await headerLayout(context.env);
  } catch (error) {
    return fail(error);
  }
  const reply = { ok: true, sheet: "connected", header: layout };
  if (layout === "old") {
    reply.hint = "Insert a column \"Uzvārds\" left of \"Punkti\" (column E) to store surnames separately.";
  }
  return json(reply);
}
