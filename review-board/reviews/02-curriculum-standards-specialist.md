# Review · 2 · Curriculum & Standards Specialist

> Improvement plan for alignment with MK noteikumi Nr. 416/747 and the
> sasniedzamie rezultāti (SR) tracked in `sasnRez.html`.

Severity: `Critical | Major | Minor | Nit`.

## What I reviewed

- `sasnRez.html` (authoritative SR list) and its `#datorika9` anchor.
- SR references in sampled lessons: `datorika9/dat9_11.html` (pills +
  `teacher-meta` caveat), `programmesana1/prog1_1/prog1_11.html` (full-text
  `.lesson-meta`), `robotika/rbtk7_11.html` (plain-text `D.7.1.1., D.7.2.1.`).
- The coverage policy documented in `datorika9/SKOLOTAJAM.md` and `README.md`.

## Findings

- **Resolved** — SR references standardized to the Programmēšana II pattern in all
  four courses: visible `.lesson-meta` with `SR {code}. {Title}` links to
  `/sasnRez`, titles verbatim from `sasnRez.html`, Robotika using `SR D.7.x.x.`.
- **Resolved** — `macibu-satura-audits.md` recreated at the repo root with the
  per-lesson SR coverage table; the `SKOLOTAJAM.md` link now resolves.

## Improvement plan

1. (Resolved) One citation format is applied: `SR {code}. {Title}` → `/sasnRez`
   everywhere (P2 pattern); Robotika uses `SR D.7.x.x.`.
2. (Resolved) `macibu-satura-audits.md` restored for Datorika 9; per-course
   equivalents remain future work.
3. Audit each course's 148 lessons for SR links that are missing, wrong-numbered
   or overclaimed (a task must actually exercise the cited part).
4. Verify every cited SR code exists in `sasnRez.html`; flag any link to a code
   the standard list does not contain.
5. Confirm grade-level labels (9. klase / 10.–12. / 7.–9.) on every course page
   and `LearningResource` JSON-LD block.

## Open questions

- (Resolved) `SR {code}. {Title}` is authoritative; `D.7.x.x` codes carry the
  `SR ` prefix too, per the applied standard.
