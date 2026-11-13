# Review · 11 · Technical QA & Consistency Reviewer

> Improvement plan for links, code blocks, starter-code sync, file naming, SEO/
> Schema.org metadata, and the redirects/sitemap rules.

Severity: `Critical | Major | Minor | Nit`.

## What I reviewed

- Full repo inventory (343 files excl. `.git`): 67 Datorika 9, 85 P1, 43 P2,
  13 Robotika HTML files; MD/PY file list; `.gitignore` absence.
- `_redirects` (238 lines), `_headers` (22), `sitemap.xml` (727 lines / 181 URLs),
  `lesson.js`, `style.css` tokens.

## Findings

- **Resolved · missing files** — `macibu-satura-audits.md` created at the repo root;
  the stale `programmesana2/img/` references removed from `README.md`.
- **Nit · `.godot/` on disk but already ignored** — `.godot/` directories exist
  under `prog2_1/pong` and `prog2_2/platformer`, but each project's own
  `.gitignore` (`.godot/`, `bin/`, `obj/`, `*.tmp`) already ignores them, and
  `git ls-files` confirms nothing is tracked. No `git rm` is needed.
  Fix: none required; a root `.gitignore` for general noise was added.
- **Resolved · corrective redirects** — the nested-path rules
  (`/programmesana1/programmesana1/prog1_6/…`,
  `/programmesana1/programmesana1/prog1_6/datorika9/dat9_3main…`) were stale:
  every current `prog1_6` link is already absolute and correct. The four rules
  were removed from `_redirects`.
- **Nit · legacy redirects** — `/par` and `/par.html` → `/` remain from a removed
  page. Clean up or document.
- **Nit · sitemap** — complete (181 URLs exactly match index + paligm + sasnRez +
  4 course + 25 topic mains + 148 lessons + git), but every `lastmod` is `2026-10-26`.
  Set real per-page dates on next change.
- **Verification item · `_headers`** — confirm Cloudflare Pages `_headers`
  wildcards (`/*/SKOLOTAJAM.md`, `/*/*/SKOLOTAJAM.md`) match across path segments;
  if not, teacher notes could be indexed.
- **Verification item · starter-code sync** — enforce the two-copy rule for
  Datorika 9 (in-page `#pilnais-kods` vs `sakuma-kodi/NN.html`) manually on edit.

## Improvement plan

1. (Resolved) `.godot/` is already ignored per-project; added a root `.gitignore`
   for OS/Python noise. No build artifacts were tracked, so no `git rm` was needed.
2. (Resolved) `macibu-satura-audits.md` created; `programmesana2/img/` references removed.
3. (Resolved) Crawled `prog1_6` links — all absolute and correct; removed the 4
   stale corrective redirects from `_redirects`.
4. (Resolved) SR-reference markup standardized across all four courses (with Worker 2).
5. (Resolved) No check script is kept in the repo; starter-code sync is verified manually.
6. Refresh `sitemap.xml` `lastmod` values.

## Open questions

- (Resolved) The `programmesana2/img/` references were removed.
 