# Review · 9 · Accessibility & Inclusion Specialist

> Improvement plan for readability, cognitive load and technical accessibility,
> with explicit attention to UDHS/ADHD and reading difficulties.

Severity: `Critical | Major | Minor | Nit`.

## What I reviewed

- `style.css` design tokens (color system) and `lesson.css` layout constants.
- Shared affordances: skip link, `role="status"`, `aria-live`, `aria-label`,
  `role="region"`, native checkboxes/copy button.
- Sampled lessons `dat9_11.html`, `prog1_11.html`, `rbtk7_11.html`.

## Findings

- **Positive** — strong baseline: skip links, semantic `main`/`nav`/`aside`,
  `aria-label` on sidebars and tables, `aria-live` copy status, and the
  short-step / visible-goal / expandable-code design for UDHS students.
- **Verification item · contrast** — `--accent: #A89C88` and `--muted: #C8BCA4`
  are used on dark surfaces (`--bg: #222831`, `--surface: #2A2F34`). Verify these
  meet WCAG AA (≥ 4.5:1) for small text; `--muted`/`--accent` are borderline on a
  dark background. Confirm `--line`/`--line-soft` are never used for body text.
- **Verification item · focus states** — confirm a visible `:focus-visible` style
  exists for links, buttons and checkboxes; dark themes often omit it.
- **Minor · goal placement** — success criteria (`.done-when`) sit at the *end* of
  each task. For UDHS students, state the success criterion at the *start* of the
  task too, so the goal is visible before the steps.
- **Nit** — `lesson.js`'s reset button label ("Noņemt soļu atzīmes") appears even
  when nothing is checked; harmless but could be clearer.

## Improvement plan

1. Audit color contrast for all text tokens against their backgrounds; adjust
   `--muted`/`--accent` if below AA.
2. Add/verify `:focus-visible` styling for all interactive elements.
3. Move or duplicate the success criterion to the top of each task.
4. Verify heading order (h1 → h2 → h3) and landmark structure on every lesson.
5. Confirm keyboard-only completion of a full lesson (copy button, checkboxes,
   navigation, details/summary).

## Open questions

- Is a WCAG AA target acceptable, or should the project aim for AAA where feasible?
