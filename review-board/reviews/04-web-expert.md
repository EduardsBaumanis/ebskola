# Review · 4 · Web Technologies Expert

> Improvement plan for the HTML / CSS / JavaScript content in Datorika 9.

Severity: `Critical | Major | Minor | Nit`.

## What I reviewed

- `datorika9/dat9_11.html` in full (theory, starter code, tasks, diagnostics).
- The course's two-copy starter-code rule (in-page `#pilnais-kods` + `sakuma-kodi/`).
- `datorika9/sakuma-kodi/` inventory (11–56 present; `25.zip`, `26.zip` present).

## Findings

- **Positive** — `dat9_11.html` is technically correct: tags nest properly, the
  in-page starter code is HTML-entity-encoded (`&lt;`, `&gt;`, `&amp;`), and the
  three tasks name exact change points in the starter code.
- **Verification item** — the hard requirement is byte-level sync between the
  encoded `#pilnais-kods` block and `sakuma-kodi/NN.html` for all 30 lessons.
  This is the most likely place for drift (an edit made in one copy only).
  Verify manually on each edit — no automated check script is kept in the repo.
- **Priority audit** — theme 5 (lessons 51–56, the game-logic build: score, lives,
  win/lose) carries the most JavaScript risk; audit those lessons first for
  behavior-vs-text mismatches.

## Improvement plan

1. Manually diff every `#pilnais-kods` block against `sakuma-kodi/NN.html`, and
   validate the ZIP contents (`25.zip`, `26.zip`) match their lessons.
2. Audit all 30 lessons: valid HTML nesting; correct entity encoding in the
   in-page block; CSS that does what the text claims; JS that matches the
   described score/lives/win/lose behavior.
3. Verify each task's "change this specific spot" instruction points at code that
   actually exists in the starter file.
4. Check the `[hidden]` + `button`/`input` starter CSS is consistently included
   so every student page behaves the same before customization.

## Open questions

- (Resolved) No check script is kept in the repo; starter-code sync is verified manually.