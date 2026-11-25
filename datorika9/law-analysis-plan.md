# Datorika 9 — law analysis plan (MK Nr. 747)

How to check Datorika 9 against the basic-education standard, and fix what is
wrong. This repeats the method used for Programmēšana I and II in November
2026: the law against `sasnRez.html`, then the lessons, then the missing
results, then the topic order. Run the phases in order. Each phase ends with
a check, and phases 1 and 4 stop for the author's decisions.

---

## 1. The law

**MK 2018. gada 27. novembra noteikumi Nr. 747** "Noteikumi par valsts
pamatizglītības standartu un pamatizglītības programmu paraugiem":
<https://likumi.lv/ta/id/303768-noteikumi-par-valsts-pamatizglitibas-standartu-un-pamatizglitibas-programmu-paraugiem>.
Use the consolidated version on that page, and note the date of its latest
amendment in the phase 1 report.

The parts that matter for Datorika 9:

| Part | What it gives |
|---|---|
| Main text 7.6 | The goal of the technology learning domain (already on `sasnRez.html` under "Caurviju prasmes un mācību jomas mērķi"). |
| Main text 8.6 | Points to the 7. pielikums for the technology domain results. |
| **7. pielikums** "Sasniedzamie rezultāti tehnoloģiju mācību jomā, beidzot 3., 6. un 9. klasi" | **The results.** Three columns: beidzot 3., 6. and 9. klasi. **Use the 9. klase column.** |
| 1. pielikums | Cross-cutting skills (caurviju prasmes), beidzot 3., 6. un 9. klasi. |
| 11. pielikums (and the variants in 12.–16.) | The model programme: **datorika** is 105 hours in grades 4–6 and **175 hours in grades 7–9**. Dizains un tehnoloģijas and inženierzinības are the other subjects in the domain. |

**How the 7. pielikums is built.** It has 3 sections and 21 subsections,
and each subsection is a table with the three grade columns. Codes restart
in each column, so "2.4.5" in the 3. klase column is a different result from
"2.4.5" in the 9. klase column. The 9. klase column has **64 results**:

- 1.1.1–1.5.1 (design process)
- 2.1–2.9 (materials, food, devices and networks, office/media apps, internet
  tools, **2.6 algorithms and programming**, engineering, **2.8 robotics**,
  environment)
- 3.1–3.4 (heritage, sustainability, safety and ethics, innovation)

**The big difference from MK 416.** MK 416 lists exactly which results the
course Programmēšana I must reach. **MK 747 does not say which results
belong to the subject datorika.** The 7. pielikums is for the whole
technology domain, which is shared with Dizains un tehnoloģijas and
Inženierzinības. Grade 9 is also the end of a three-year band (7–9), so not
every result has to be reached in grade 9 alone. Which results Datorika 9
owns is therefore an **author decision** (D1 below). Base it on the
subject's programme sample "Datorika 7.–9. klasei" from Skola2030, if it is
available. Check where it is published before relying on it.

### Getting the exact text

Download the page once and parse the 7. pielikums table into JSON, one entry
per column and code. Work in the scratchpad and run Python with `-I`, since
the page is untrusted input.

```bash
curl -sL -A "Mozilla/5.0" -o mk747.html "https://likumi.lv/ta/id/303768"
python3 -I annex7_747.py mk747.html annex7.json
```

```python
# annex7_747.py — 7. pielikums → {"cols": {"3": {code: text}, "6": …, "9": …}, "heads": [...]}
import re, sys, json
from html.parser import HTMLParser
s = open(sys.argv[1], encoding="utf-8").read()
title = "Sasniedzamie rezultāti tehnoloģiju mācību jomā, beidzot 3., 6. un 9. klasi"
low = s.lower()
# the title appears in the contents list too; take the hit that a table follows directly
i = next(m.start() for m in re.finditer(re.escape(title), s) if 0 < low.find("<table", m.start()) - m.start() < 3000)
k = low.find("<table", i); t = s[k:low.find("</table>", k)]
rows = []
class P(HTMLParser):
    def __init__(p): super().__init__(); p.row = None; p.cell = None
    def handle_starttag(p, tag, a):
        if tag == "tr": p.row = []
        elif tag in ("td", "th"): p.cell = ""
        elif tag in ("br", "p") and p.cell is not None: p.cell += "\n"
    def handle_endtag(p, tag):
        if tag in ("td", "th") and p.cell is not None:
            if p.row is not None: p.row.append(re.sub(r"\s+", " ", p.cell).strip())
            p.cell = None
        elif tag == "tr" and p.row is not None: rows.append(p.row); p.row = None
    def handle_data(p, d):
        if p.cell is not None: p.cell += d
P().feed(t)
out = {"3": {}, "6": {}, "9": {}}; heads = []
for r in rows:
    if len(r) == 3:                                   # a results row: one cell per grade column
        for col, cell in zip(["3", "6", "9"], r):
            for m in re.finditer(r"(\d\.\d\.\d+)\.\s*(.*?)(?=(?:\s\d\.\d\.\d+\.\s)|$)", cell):
                out[col][m.group(1)] = m.group(2)
    elif len(r) == 1:                                 # a section or subsection heading
        heads.append(r[0])
json.dump({"cols": out, "heads": heads}, open(sys.argv[2], "w"), ensure_ascii=False, indent=1)
print({k: len(v) for k, v in out.items()}, "headings", len(heads))
```

Expected output: `{'3': 54, '6': 61, '9': 64} headings 21`. If the counts
differ, the law has changed: read the amendment note before going on.

---

## 2. First look (automated, 2026-11-23, confirm in phase 1)

The Datorika 9 section of `sasnRez.html` (`#datorika9`) is **much closer to
the law** than the Programmēšana sections were.

- **37 rows. 34 are verbatim** from the 9. klase column.
- **2.4.5 has the wrong text.** The site says "Apstrādā attēlus, izmantojot
  rastra un vektoru grafikas reda…". The law says "Izveido zīmējumu vai veic
  digitālā attēla apstrādi, lietojot piemērotus rīkus, grafikas veidu un
  lietotnes, nosaka digitāla attēla galvenos raksturlielumus".
- **2.4.8 has the wrong text.** The site says "Apvieno teksta, attēlu, audio un
  video saturu vienotā multim…". The law says "Patstāvīgi pielāgo lietotnes
  iestatījumus atbilstoši lietotāja vajadzībām, lai paaugstinātu darba
  produktivitāti un drošību, ievērojot un izvērtējot veicamā uzdevuma
  specifiku".
- **2.6.3 does not exist** in the 9. klase column, which has only 2.6.1 and
  2.6.2. Its text ("Pārvalda programmējamas ierīces…") reads like section
  2.8, robotics (2.8.1, 2.8.2).
- **28 results of the 9. klase column are not on the page:** 2.1.1–2.1.3,
  2.2.1–2.2.4, 2.7.1–2.7.3, 2.8.1, 2.8.2, 2.9.1–2.9.3, 3.1.1, 3.1.2,
  3.2.1, 3.2.2, 3.3.1–3.3.7, 3.4.1, 3.4.2. Many are clearly Dizains un
  tehnoloģijas (food, materials). Others, such as 2.8 robotics, 3.3 safety
  and ethics, and 3.4 innovation, may belong to datorika (D1).
- **The "Datorika 7. klasei – robotikas konteksts (MK 747)" table uses codes
  `D.7.1.1`–`D.7.6.1`, which do not exist in MK 747.** They are an invented
  scheme for the Robotika course. Out of scope for Datorika 9, but the same
  law applies: see D4.
- **Lessons:** 30 lesson files cite SR in `.lesson-meta`, in the old format
  `<a href="/sasnRez">SR 2.6.1. Algoritmu pieraksts un izpilde</a>`, with a
  short label and no anchor. Codes used: 1.1.1–1.5.1, 2.3.1, 2.3.3, 2.4.5–2.4.8,
  2.4.10, 2.5.2, 2.5.3, 2.6.1 (21 times) and 2.6.2 (11 times).
  `macibu-satura-audits.md` (repository root) holds the per-lesson table.
  Any lesson citing 2.4.5 or 2.4.8 was mapped by the wrong text.

---

## 3. Course facts the phases need

- **Structure:** 5 topics × 6 lessons.
  - Topic pages: `datorika9/dat9_T/dat9_Tmain.html`.
  - Lessons: `datorika9/dat9_T/nodarbibas/dat9_TS.html`.
  - Tests: `datorika9/dat9_T/testi/dat9_TS_test.html`, which start at S = 2
    and repeat the previous lesson.
  - Course page: `datorika9/datorika9.html`. Shared Git guide:
    `datorika9/git.html`.
- **Starter code** for every lesson is in `datorika9/sakuma-kodi/TS.html`
  (`11.html` … `56.html`, plus `atteli/`, `skanas/` and media). Lessons link
  to it relatively: `href="../../sakuma-kodi/15.html"`. **Any new lesson
  needs a starter file, and any renumbering must rename these too.**
- **Tests** report to Google Sheets with the id `dat9_TS_test`
  (`functions/api/tests.js`: prefix `dat9_`, classes 9.a–9.c).
- **Elsewhere:** `index.html` lists 5 Datorika 9 topics; `README.md`;
  `sitemap.xml` (35 entries); `_redirects` (146 `dat9_` lines, including
  `.html` → extensionless rules).
- **The project:** a browser game in HTML, CSS and JavaScript, published on
  GitHub Pages, built in VS Code with GitHub. Grade 9 students, so new
  topics must stay at that level.

---

## 4. Phases

### Phase 1 — Compare (no edits)

Produce a report, and stop for the author's decisions.

1. Parse the law (section 1). Record the amendment date and the counts.
2. For every row of `#datorika9` on `sasnRez.html`: code, site text, law
   text (9. klase), and a verdict (verbatim / wrong text / code not in the
   column).
3. List the 9. klase results that are not on the page, grouped by
   subsection. For each, give a first guess of the owning subject
   (datorika, dizains un tehnoloģijas, inženierzinības), with a one-line
   reason.
4. Check the caurviju prasmes and the domain-goal texts on the page against
   the 1. pielikums and main text 7.6.
5. List the lesson citations whose code or label no longer matches the law
   text (start with 2.4.5, 2.4.8 and 2.6.3).

**Stop.** The author decides D1–D5 (section 6).

### Phase 2 — Rewrite the Datorika 9 section of `sasnRez.html`

- Keep the section id `datorika9` (many links use `/sasnRez#datorika9`).
- An intro paragraph: MK Nr. 747, 7. pielikums, column "beidzot 9. klasi";
  datorika is 175 hours in grades 7–9 in the model programme; and the D1
  scope statement (which results this course owns, and which are left to
  the other subjects or grades 7–8).
- One table per subsection (or per section), with the law's heading text as
  a `<th colspan="2">` group row, and **verbatim** 9. klase text for every
  result in scope.
- An anchor on every row: `id="dat9-2-6-1"`. The page already has the
  script that opens the right `<details>` for a `#…` link, and the
  `tr:target` highlight.
- The robotics table: per D4.
- **Check:** every row's text equals the JSON. There are no codes outside
  the column. The HTML is balanced, and the page looks right in a browser.

### Phase 3 — Re-map the lessons

- Read each lesson (title, goal, task headings, starter file) and choose
  the results it actually practises. A citation means the lesson practises
  part of the result: don't claim the whole of a broad result, and don't
  cite a result the lesson does not touch.
- The citation format matches Programmēšana I and II:
  `<a href="/sasnRez#dat9-2-6-1" title="{law text, verbatim}">SR 2.6.1. {short label}</a>`.
  Use 1–4 per lesson.
- Update `macibu-satura-audits.md` to the new mapping. Keep its "Pārklājuma
  robežas" section honest.
- **Check:** every `href` anchor exists on `sasnRez.html`, every `title`
  equals the row text, and you have a list of in-scope results with zero
  lessons.

### Phase 4 — Missing results → planned topics

- From the in-scope results with zero lessons, group them into topics of 6
  lessons. Use as many topics as needed: Programmēšana I needed 4,
  Programmēšana II needed 4.
- Create `datorika9/dat9_N/dat9_Nplan.md` (N = 6, 7, …) with the same
  structure as `programmesana1/prog1_7/prog1_7plan.md`:
  - a status line, why the topic exists, its place in the course and its
    prerequisites;
  - a results table with **verbatim** text;
  - the tools;
  - six lessons with a file name, a goal ("Šajā stundā tu…"), results,
    theory, three tasks (try, build, break and test) and what to hand in;
  - **a starter-code note per lesson** (`sakuma-kodi/NS.html`);
  - a final project (N.6) with assessment criteria;
  - open questions.
- Keep the grade-9 level and the browser-game thread where it fits.
- **Check:** a script confirms that every in-scope gap appears in some
  plan's results table.

**Stop.** The author decides whether to reorder (D5).

### Phase 5 — Reorder and renumber (only if the author asks)

Map old → new numbers, then:

1. `git mv` topic folders through temporary names (folder numbers get
   reused), then rename the files inside: `dat9_TS.html`, `dat9_Tmain.html`,
   `testi/dat9_TS_test.html` and plan files. Plan files that are not tracked
   are moved with plain `mv`.
2. **Rename starter files** `sakuma-kodi/TS.html` to match, through
   temporary names. They are referenced relatively, so the regex must cover
   `sakuma-kodi/(\d+)\.html`.
3. Rewrite in **one regex pass per file**, so no number is mapped twice:
   - `dat9_(\d+)` path tokens: folder if followed by `/`, `main` or `plan`;
     otherwise a file, with T = all digits but the last;
   - lesson numbers `T.S`;
   - topic numbers "T. tēma" / "T. Tēma";
   - starter-file names;
   - test ids.

   Scan for false positives first. Decimal numbers in CSS or JS such as
   `1.5`, `0.3s` and `2.5rem` look like lesson numbers. List every match
   outside titles, sidebars and breadcrumbs, and exclude the false ones.
4. By hand:
   - `datorika9/datorika9.html`: topic cards, project cards, counts. Planned
     topics get dashed cards with "tēma tiek izstrādāta", no link, and the
     existing `.topic-card.planned` and `.planned-badge` styles.
   - `index.html` file tree: planned entries use
     `<span class="planned">…<span>title <em>(tiek izstrādāta)</em></span></span>`.
   - Counts in the `index.html` description and JSON-LD, `README.md` rows and
     folder notes, and the topic pages' ← / → buttons, which should skip
     planned topics.
5. `_redirects`: point the legacy flat-URL targets at the new folders.
   Redirect **only old paths that no topic uses any more**. Point those
   folders' `.html` → extensionless rules straight at the new pages, to
   avoid two redirects in a row, and add a comment saying to undo them when
   the planned topic is built.
6. Update `plan.md`-style references in the plans, and the memory notes.

### Phase 6 — Verify

- Link check: every `/datorika9/…` link in all HTML and in `sitemap.xml`
  resolves to a file (`p + ".html"` or `p` exists). Every `_redirects`
  target exists.
- Every lesson's SR anchors and titles match `sasnRez.html`.
- Screenshots in headless Chrome of `sasnRez.html#dat9-…` (the section
  opens and scrolls), the course page and the index list. Smooth scrolling
  needs `behavior: "instant"` in headless runs. For long pages, take a tall
  window and crop it.
- Report what changed, what the author must decide, and the side effects
  (bookmarks, test ids in Sheets, the first test after an inserted topic).

---

## 5. Pitfalls from the Programmēšana runs

- **The page text was not the law.** Most Programmēšana descriptions were
  invented paraphrases that gave codes the wrong meaning (2.4.18 is machine
  learning, not OOP). Never trust a label: compare with the parsed JSON.
- **Codes repeat across columns.** The level or column must be visible next
  to every citation and anchor.
- **Single-pass replacement.** Sequential regexes turned 8.4 → 10.4 → 13.4.
  Use one combined regex with a replacement function.
- **Numbers that only look like lessons.** "Ievadi likmi: 10.5" was the one
  false hit in Prog I. In Datorika, CSS and JS values are the risk.
- **Lists in prose.** "Topics 7 and 8" became "Topics 8 and 8", because only
  the number right after "topic" was mapped. Grep for lists and ranges after
  the pass, and fix them by hand.
- **Folder reuse.** After renumbering, an old URL may serve a different
  lesson, and no redirect is possible there. Say so in the report.
- **Untracked plan files** cannot be moved with `git mv`.
- **The first test of a lesson after an inserted topic** still repeats the
  lesson before the gap, until the new topic exists.

---

## 6. Decisions for the author

| # | Question | Default if no answer |
|---|---|---|
| D1 | Which 9. klase results does Datorika 9 own? Datorika vs Dizains un tehnoloģijas vs Inženierzinības, and grade 9 vs grades 7–8. | Sections 2.3–2.6 and 2.8, plus the 1.x design process and 3.3–3.4 as far as a software project touches them. Everything else is listed as "citi mācību priekšmeti". |
| D2 | Do results reached in grades 7–8 (for example in the Robotika course) count for Datorika 9? | Yes for coverage, but Datorika 9 still cites only what its own lessons practise. |
| D3 | Citation label: short label plus the law text in `title` (as in Programmēšana), or full law text? | Short label plus `title`. |
| D4 | The `D.7.x.x` Robotika table: replace it with real MK 747 codes (mostly 2.8.x, 2.6.x and 2.3.x in the 9. or 6. klase column), or keep it as a separate, clearly labelled course scheme? | Replace it with real codes in a separate task for the Robotika course. |
| D5 | Renumber topics after the planned topics are added? | Ask after phase 4. |

**Decided:**

- **D1 (2026-11-25).** The default, minus the borderline results 1.1.2,
  1.1.3, 1.3.4, 2.8.1, 2.8.2, 3.4.3 and 3.4.4. That leaves 36 results in
  scope: 1.1.1, 1.2.x, 1.3.1–1.3.3, 1.4.x, 1.5.1, 2.3–2.6, 3.3.1 and
  3.3.3–3.3.6.
- **D2.** Robotika covers 2.8.
- **D4 (2026-11-23).** The Robotika lessons cite real 9. klase codes through
  `sasnRez.html#robotika`.
- **Phase 4 (2026-11-25).** The 16 gaps are planned in
  `dat9_6/dat9_6plan.md` (Biroja lietotnes) and `dat9_7/dat9_7plan.md`
  (Tīkli, internets un drošība).
- **D5 (2026-11-25).** Keep the order. Topics 1–5 stay as they are, and the
  new topics are 6 and 7. No renumbering, so phase 5 steps 1–3 and 5 are not
  needed. Step 4 (planned cards) was done on 2026-11-25:
  - `datorika9.html`: two dashed cards for topics 6 and 7, and the scope
    fact "7 tēmas · 42 nodarbības";
  - `index.html`: the file tree shows 7 topics. The index card still counts
    only the built 5 / 30, as for Programmēšana;
  - `README.md`: the course row and the folder notes.
- **Lesson 1.1 (2026-11-25).** It now tells students to register GitHub with
  their personal email, not the school one.
- **Other answers (2026-11-25):**
  - Microsoft 365 for topic 6.
  - Students use their personal email for website accounts, because the
    school email is blocked for registration on most sites.
  - `ping` and `tracert` are allowed.
- **`macibu-satura-audits.md`** was deleted by the author on 2026-11-23. Don't
  recreate it.

---

## 7. Prompts

Paste one per session, in order.

**Phase 1.**
> Read `datorika9/law-analysis-plan.md` sections 1–3. Download MK Nr. 747,
> parse the 7. pielikums with the script in section 1, and do phase 1. No
> edits. Report the comparison table, the missing results with your
> suggested owning subject, and the citations that need re-mapping. Then
> ask me D1–D4.

**Phase 2.**
> Do phase 2 of `datorika9/law-analysis-plan.md` with my D1, D3 and D4
> answers. Rewrite only the `#datorika9` section of `sasnRez.html`, with
> verbatim 9. klase text and `dat9-…` anchors, and run the phase 2 checks.

**Phase 3.**
> Do phase 3 of `datorika9/law-analysis-plan.md`. Re-map every Datorika 9
> lesson's `.lesson-meta` by what the lesson actually practises, update
> `macibu-satura-audits.md`, run the checks, and list the in-scope results
> with no lesson.

**Phase 4.**
> Do phase 4 of `datorika9/law-analysis-plan.md`. Create the
> `dat9_N/dat9_Nplan.md` topic plans for the uncovered results. Six lessons
> each, with starter-code notes, in the structure of
> `programmesana1/prog1_7/prog1_7plan.md`. Then ask me about D5.

**Phase 5–6.**
> Do phases 5 and 6 of `datorika9/law-analysis-plan.md` with this order:
> {order}. Rename the folders, starter files and tests, rewrite the
> numbers in one pass, update `datorika9.html`, `index.html`, `README.md`,
> `_redirects` and `sitemap.xml`, and verify.
