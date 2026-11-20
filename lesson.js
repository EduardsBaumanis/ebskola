/* Optional reading aids. All instructions and downloads work without JavaScript. */
"use strict";

document.querySelectorAll("[data-copy]").forEach(function (button) {
  button.addEventListener("click", async function () {
    const source = document.getElementById(button.dataset.copy);
    const status = button.closest("section").querySelector(".copy-status");
    if (!source || !status) return;
    try {
      await navigator.clipboard.writeText(source.textContent);
      status.textContent = "Kods nokopēts. VS Code ielīmē ar Ctrl+V.";
    } catch (_) {
      const details = source.closest("details");
      if (details) details.open = true;
      const range = document.createRange();
      range.selectNodeContents(source);
      const selection = window.getSelection();
      selection.removeAllRanges();
      selection.addRange(range);
      status.textContent = "Kods ir iezīmēts. Nospied Ctrl+C, pēc tam VS Code — Ctrl+V.";
    }
  });
});

const taskSteps = Array.from(document.querySelectorAll(".lesson-task > .step-list > li"));
if (taskSteps.length) {
  // Keep existing Datorika 9 marks when moving to the shared script.
  const datorika = document.body.classList.contains("datorika-kurss");
  const path = location.pathname.replace(/\/$/, "").replace(/\.html$/, "");
  // Datorika 9 lessons moved from /datorika9/dat9_11 into /datorika9/dat9_1/nodarbibas/dat9_11;
  // the key keeps the old flat path so marks saved before the move still load.
  const key = datorika
    ? "datorika9-2026-09-soļi:/datorika9/" + path.split("/").pop()
    : "ebskola-soļi-v1:" + path;
  let saved = [];
  try {
    const value = JSON.parse(localStorage.getItem(key) || "[]");
    if (Array.isArray(value)) saved = value;
  } catch (_) { /* Step markers also work when storage is unavailable. */ }

  const panel = document.createElement("div");
  panel.className = "step-progress";
  const status = document.createElement("span");
  status.setAttribute("role", "status");
  const reset = document.createElement("button");
  reset.type = "button";
  reset.textContent = "Noņemt soļu atzīmes";
  panel.append(status, reset);
  document.querySelector("#uzdevums-1").before(panel);

  const boxes = taskSteps.map(function (step, index) {
    const box = document.createElement("input");
    box.type = "checkbox";
    box.className = "step-check";
    const task = step.closest(".lesson-task");
    const number = Array.from(step.parentElement.children).indexOf(step) + 1;
    const label = task.querySelector(".task-number").textContent.trim().replace(/\s*[-–—:]$/, "").split(" · ")[0];
    box.setAttribute("aria-label", label + ": atzīmēt " + number + ". soli kā paveiktu");
    box.checked = saved[index] === true;
    step.prepend(box);
    return box;
  });
  function update() {
    status.textContent = "Atzīmēti " + boxes.filter(function (box) { return box.checked; }).length + " no " + boxes.length + " soļiem.";
    try { localStorage.setItem(key, JSON.stringify(boxes.map(function (box) { return box.checked; }))); } catch (_) { /* Optional. */ }
  }
  boxes.forEach(function (box) { box.addEventListener("change", update); });
  reset.addEventListener("click", function () {
    boxes.forEach(function (box) { box.checked = false; });
    update();
  });
  update();
}
