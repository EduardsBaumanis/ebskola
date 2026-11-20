/* Atkārtojuma testi: novērtē atbildes lapā un nosūta rezultātu uz /api/tests
   (functions/api/tests.js), kas to ieraksta skolotāja Google Sheets tabulā. */
"use strict";

(function () {
  const form = document.querySelector(".test-form");
  if (!form) return;

  const questions = Array.from(form.querySelectorAll(".test-question"));
  const nameInput = form.elements.vards;
  // Lapa, kas vēl nav atjaunota, var saturēt tikai vienu lauku "Vārds, uzvārds".
  const surnameInput = form.elements.uzvards || null;
  const classSelect = form.elements.klase;
  const button = form.querySelector(".test-submit");
  const status = form.querySelector(".test-status");
  const scoreLine = form.querySelector(".test-score");
  let result = null; // Atbildes vērtē vienreiz; vēlāk poga tikai atkārto sūtīšanu.
  let sending = false;

  function chosen(question) {
    return question.querySelector("input[type=radio]:checked");
  }

  function say(text, state) {
    status.textContent = text;
    status.className = "test-status" + (state ? " " + state : "");
  }

  function clean(text) {
    return text.replace(/\s+/g, " ").trim();
  }

  // Vārds un uzvārds atsevišķi; vecajā vienlauka formā pirmais vārds ir vārds, pārējais — uzvārds.
  function person() {
    if (surnameInput) return { vards: clean(nameInput.value), uzvards: clean(surnameInput.value) };
    const parts = clean(nameInput.value).split(" ");
    return { vards: parts[0], uzvards: parts.slice(1).join(" ") };
  }

  function firstProblem() {
    if (surnameInput) {
      if (clean(nameInput.value).length < 2) return { field: nameInput, text: "Ieraksti savu vārdu." };
      if (clean(surnameInput.value).length < 2) return { field: surnameInput, text: "Ieraksti savu uzvārdu." };
    } else if (clean(nameInput.value).length < 2) {
      return { field: nameInput, text: "Ieraksti savu vārdu un uzvārdu." };
    }
    if (!classSelect.value) return { field: classSelect, text: "Izvēlies savu klasi." };
    const index = questions.findIndex(function (question) { return !chosen(question); });
    if (index >= 0) {
      return { field: questions[index].querySelector("input"), text: "Izvēlies atbildi " + (index + 1) + ". jautājumam." };
    }
    return null;
  }

  function mark(label, className, text) {
    label.classList.add(className);
    const note = document.createElement("span");
    note.className = "test-mark";
    note.textContent = text;
    label.append(note);
  }

  function grade() {
    const answers = questions.map(function (question) {
      const pick = chosen(question);
      const ok = pick.value === question.dataset.correct;
      question.classList.add(ok ? "is-correct" : "is-wrong");
      question.querySelectorAll("input[type=radio]").forEach(function (input) {
        const label = input.closest("label");
        if (input.value === question.dataset.correct) mark(label, "is-answer", ok ? "✓ Pareizi" : "✓ Pareizā atbilde");
        else if (input === pick) mark(label, "is-mistake", "✗ Tava atbilde");
        input.disabled = true;
      });
      const explanation = question.querySelector(".test-explain");
      if (explanation) explanation.hidden = false;
      return { a: pick.value.toUpperCase(), ok: ok };
    });
    const who = person();
    result = {
      test: form.dataset.test,
      vards: who.vards,
      uzvards: who.uzvards,
      klase: classSelect.value,
      answers: answers,
    };
    nameInput.readOnly = true;
    if (surnameInput) surnameInput.readOnly = true;
    classSelect.disabled = true;

    const score = answers.filter(function (answer) { return answer.ok; }).length;
    scoreLine.textContent = "Tavs rezultāts: " + score + " no " + answers.length +
      ". Pie katra jautājuma tagad redzi pareizo atbildi un īsu skaidrojumu.";
    scoreLine.hidden = false;
  }

  async function send() {
    sending = true;
    button.disabled = true;
    say("Sūta rezultātu skolotājam…");
    try {
      const response = await fetch("/api/tests", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify(result),
        signal: AbortSignal.timeout(20000),
      });
      const reply = await response.json().catch(function () { return {}; });
      if (!response.ok || !reply.ok) throw new Error(reply.detail || reply.error || "HTTP " + response.status);
      say("Rezultāts nosūtīts skolotājam.", "is-sent");
      button.hidden = true;
    } catch (error) {
      console.error("Testa rezultāts nav nosūtīts:", error);
      say("Rezultātu neizdevās nosūtīt. Pārbaudi interneta savienojumu un nospied “Sūtīt vēlreiz”. " +
        "Ja neizdodas arī tad, parādi šo lapu skolotājam.", "is-failed");
      button.textContent = "Sūtīt vēlreiz";
      button.disabled = false;
    }
    sending = false;
  }

  form.addEventListener("submit", function (event) {
    event.preventDefault();
    if (sending) return;
    if (!result) {
      const problem = firstProblem();
      if (problem) {
        say(problem.text, "is-failed");
        problem.field.focus();
        return;
      }
      grade();
    }
    send();
  });
})();
