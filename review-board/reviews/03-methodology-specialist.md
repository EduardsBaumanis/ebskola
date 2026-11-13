# Review · 3 · Methodology & Didactics Specialist

> Improvement plan for lesson structure, scaffolding, tasks and assessment.

Severity: `Critical | Major | Minor | Nit`.

## What I reviewed

- The shared lesson skeleton and its conventions from `README.md`.
- Sampled lessons: `datorika9/dat9_11.html`, `programmesana1/prog1_1/prog1_11.html`,
  `robotika/rbtk7_11.html`.
- `lesson.js` (step checkboxes, progress, localStorage) and the grading rules in
  `datorika9/SKOLOTAJAM.md`.

## Findings

- **Positive** — The 3-task model (task 1 → 2 → 3 build toward one submitted
  result), `.done-when` criteria, expandable self-checks and optional extra tasks
  are consistent and well-designed across all sampled lessons.
- **Minor · all courses** — the skeleton diverges between courses. Datorika 9 has
  self-check, "Ja kaut kas neizdodas" and `teacher-meta`; Programmēšana I and
  Robotika put a `70 min plāns` info box directly on the student page. Pick one
  rule: student-visible short plan everywhere, detailed timing teacher-only.
- **Minor · `lesson.js`** — checkboxes are added only to `.lesson-task > .step-list
  > li`, so extra-task steps are never checkable. Decide whether extra tasks should
  also track progress (they are optional), and document the choice.
- **Nit · `lesson.js`** — the Datorika 9 migration key
  `datorika9-2026-09-soļi:` is a hardcoded dated string; fine now, but note it
  when the next migration happens.
- **Verification item** — confirm every topic-closing lesson (x.6) that is a graded
  project actually includes the `.assessment-rubric` SLA table; `dat9_16.html` is
  referenced by SKOLOTAJAM as the example.

## Improvement plan

1. Codify the canonical lesson skeleton in one place (extend `README.md` or add
   `review-board/templates/lesson-skeleton.md`) so all four courses match.
2. Unify time-plan visibility per the decision in the PM report.
3. Decide and document extra-task progress tracking; if wanted, extend the
   `lesson.js` selector to include `.extra-task .step-list > li`.
4. Audit all 148 lessons for: measurable `.lesson-goal`, progressive 3 tasks,
   objective `.done-when`, theory example from the lesson's own code, and a
   self-check question in the theory.
5. Spot-check SLA rubrics in all project-closing lessons for 4 clearly separated
   performance levels.

## Open questions

- Should extra tasks get checkboxes too, or stay deliberately un-tracked?
- Should the `70 min plāns` box remain on student pages for all courses?
