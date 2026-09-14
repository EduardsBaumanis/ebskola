/* Optional reading aids. All instructions and downloads work without JavaScript. */
"use strict";

document.querySelectorAll("[data-copy]").forEach(function (button) {
  button.addEventListener("click", async function () {
    const source = document.getElementById(button.dataset.copy);
    const status = button.closest("section").querySelector(".copy-status");
    try {
      await navigator.clipboard.writeText(source.textContent);
      status.textContent = "Kods nokopēts. VS Code ielīmē ar Ctrl+V.";
    } catch (_) {
      source.closest("details").open = true;
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
  const key = "datorika9-2026-09-soļi:" + location.pathname.replace(/\.html$/, "");
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
    box.setAttribute("aria-label", task.querySelector(".task-number").textContent.split(" · ")[0] + ": atzīmēt " + number + ". soli kā paveiktu");
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
