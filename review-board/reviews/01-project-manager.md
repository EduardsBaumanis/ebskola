# Review · 1 · Project Manager — Consolidated Report

> Board-wide review of the ebSkola repository. Scope: the whole repo — all four
> courses, shared assets, tooling and documentation — with all 12 workers active.

**Date:** 2026-11-13 · **Reviewed by:** the review board (Workers 1–12)

Severity legend used throughout: `Critical` (blocks students/teachers), `Major`
(wrong or untrustworthy), `Minor` (inconsistent/rough), `Nit` (polish).

## 1. Scope

Reviewed: repo structure, `README.md`, `datorika9/` (incl. `SKOLOTAJAM.md`,
`sakuma-kodi/`), `programmesana1/`, `programmesana2/` (incl. `kods/`, `parbaudes/`,
full projects), `robotika/`, `style.css`, `lesson.css`, `lesson.js`, `_redirects`,
`_headers`, `sitemap.xml`, `paligm.html`, `sasnRez.html`.

Workers ran: 1 Project Manager, 2 Standards, 3 Methodology, 4 Web, 5 Python,
6 Godot/C#, 7 Robotics, 8 Language, 9 Accessibility, 10 UX, 11 QA, 12 Student.

## 2. Decision log

| # | Item | Positions | Decision |
|---|------|-----------|----------|
| 1 | SR-reference format differs per course (pills vs full-text vs `D.x.x.x`) | Worker 2: standardize on `sasnRez` anchors. Worker 11: make labels uniform. Author: apply the Programmēšana II example. | Applied the P2 pattern everywhere (112 lessons): visible `.lesson-meta`, `SR {code}. {Title}` (verbatim from `sasnRez.html`), link to `/sasnRez`; Robotika uses `SR D.7.x.x.`. Done. |
| 2 | Missing files referenced by docs (`programmesana2/img/`, `macibu-satura-audits.md`) | Worker 11: remove stale references. Worker 2: recreate the coverage audit doc. | Resolved: `macibu-satura-audits.md` created; `img/` references dropped. |
| 3 | Time plans visible on student pages in P1/Robotika but teacher-only in Datorika 9 | Worker 3: unify. Worker 10: keep visible, it helps students plan. | Keep a short plan on student pages everywhere, move the detailed 10/15/20/25 split to teacher docs only. |
| 4 | `.godot/` build artifacts | Worker 6/11 initially flagged as committed; verified they are already ignored per-project. | No `git rm` needed — `.godot/` is untracked and ignored. Added a root `.gitignore` for OS/Python noise. |
| 5 | Buggy nested-path redirects in `_redirects` | Worker 11: delete redirects once source links are fixed. Worker 10: fix the links first. | Fix the source links in HTML first, keep redirects temporarily, then remove after a crawl confirms clean. |

## 3. Findings (consolidated, grouped by area)

### A. Repository hygiene & tooling
- **Severity: Nit · Worker: 11** — `.godot/` build directories exist on disk under
  `programmesana2/prog2_1/pong/.godot` and `prog2_2/platformer/.godot`, but they
  are already ignored by each project's own `.gitignore` (`.godot/`, `bin/`,
  `obj/`, `*.tmp`) and are not tracked by git. No `git rm` is needed.
  Fix: none required; a root `.gitignore` was added for OS/Python noise.
- **Resolved · Worker: 11** — missing-file references reconciled: `macibu-satura-audits.md`
  created at the repo root; the stale `programmesana2/img/` references removed
  from `README.md`.

### B. Links & redirects
- **Resolved · Workers: 10, 11** — the `prog1_6` source links were already absolute
  and correct; the four nested-path corrective redirects in `_redirects` were stale
  leftovers and have been removed.
- **Severity: Nit · Worker: 11** — legacy `/par` and `/par.html` redirects to `/`
  remain after the "about" page was removed. Fix: drop or keep deliberately.

### C. Standards & lesson structure
- **Resolved · Workers: 2, 11** — SR references standardized to the Programmēšana II
  pattern across all four courses (112 lessons): visible `.lesson-meta`, links
  `SR {code}. {Title}` with verbatim titles from `sasnRez.html`, target `/sasnRez`;
  Robotika uses `SR D.7.x.x.`. The Datorika 9 `teacher-meta` block keeps its caveat.
- **Severity: Minor · Worker: 3** — lesson skeleton diverges: Datorika 9 has
  self-check, "Ja kaut kas neizdodas" and `teacher-meta`; P1/Robotika use a
  `70 min plāns` info box on the student page. Fix: unify per §2 #3.

### D. Content accuracy
- **Workers 4–7** found no Critical errors in sampled lessons (`dat9_11`,
  `prog1_11`, `rbtk7_11` are clean and well-scaffolded). Remaining risk is in
  un-sampled lessons — see each worker's audit plan for the specific lessons to
  prioritize (game-logic lessons 5x, Flask/PostgreSQL topics, Godot milestones,
  Arduino topic).

### E. SEO & metadata
- **Severity: Nit · Worker: 11** — `sitemap.xml` is complete (181 URLs match the
  page inventory exactly), but every `lastmod` is the single date `2026-10-26`.
  Fix: set per-page `lastmod` on actual change.

## 4. Recommended order of work

1. **Repo hygiene** — confirmed `.godot/` already ignored; added a root `.gitignore` for OS/Python noise. *(QA)*
2. ~~Fix broken links in `prog1_6` area; clean corrective redirects.~~ Done — links already correct; 4 stale redirects removed. *(QA + UX)*
3. ~~Reconcile missing files.~~ Done — `macibu-satura-audits.md` created; `img/` refs dropped. *(QA + Standards)*
4. ~~Standardize SR references across all four courses.~~ Done — P2 pattern applied everywhere. *(Standards + QA)*
5. **Unify the lesson skeleton** and time-plan visibility. *(Methodology + UX)*
6. **Run per-course technical audits** (Web → Python → Godot → Robotics). *(Workers 4–7)*
7. **Language, accessibility and UX polish** on shared CSS and nav. *(Workers 8–10)*
8. **SEO polish** — `lastmod` values. *(QA)*

## 5. Open questions for the author

- ~~check script~~ Resolved: the helper-scripts folder and its references were
  removed; no check scripts are kept in the repo.
- `programmesana2/img/README.md` and `SOURCES.md` are documented but absent — create
  ~~`programmesana2/img/README.md` / `SOURCES.md`~~ Resolved: references removed.(verbatim titles) is the standard;
  Robotika's `D.7.x.x` codes also carry the `SR ` prefix.
- Are the nested-path `_redirects` rules serving live traffic yet, or can the source
  links be fixed and the rules removed immediately?

*See each worker's file under `review-board/reviews/` for the full area plan.*
