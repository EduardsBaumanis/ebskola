# Review · 5 · Python Expert

> Improvement plan for the Python / Flask / SQL / PostgreSQL content in
> Programmēšana I (12 topics, 72 lessons).

Severity: `Critical | Major | Minor | Nit`.

## What I reviewed

- `programmesana1/prog1_1/prog1_11.html` (first lesson) in detail.
- Course scope from `README.md`: Python basics → control flow → functions →
  collections → JSON/CSV → algorithms → software design → Flask → PostgreSQL/SQL
  → OOP → deployment.
- Shared conventions: Prism.js highlighting, `language-python` / `language-bash`
  code blocks, `70 min plāns` info box.

## Findings

- **Positive** — `prog1_11.html` is correct and well-scaffolded: valid Python,
  an accurate `print("Sveika, pasaule!")` example, correct Windows/VS Code steps,
  and a motivating "break the code and read the error" third task.
- **Verification item** — ensure every code block that contains Python or shell
  actually carries `class="language-python"` / `class="language-bash"` (Prism.js
  depends on it). Early lessons may have plain blocks without the class.
- **Priority audit** — the Flask and PostgreSQL topics (the `prog1_7`–`prog1_9`
  range per the README's topic list) carry the highest risk: route/import
  mismatches, connection strings, and deployment instructions must be checked
  for internal consistency.
- **Minor** — the course uses the exact version the VS Code flow installs
  (`python --version` → e.g. `3.12.x`); any snippet relying on newer syntax or a
  different platform must be flagged.

## Improvement plan

1. Add `language-*` classes to all code blocks (or run a scripted check).
2. Audit all 72 lessons in topic order, verifying: syntax/indentation/imports;
   example outputs match real `print` results; every API used in a task was
   taught earlier or is explicitly given as a ready helper (the course's rule).
3. Trace the Flask + PostgreSQL lessons end-to-end (routes, templates, SQL) for
   consistency, and confirm deployment steps match the documented commands.
4. Confirm bash snippets work on the documented Windows + VS Code setup.
5. Recommend a lint/compile pass (e.g., `py_compile`) as part of Worker 11's QA
   for any Python embedded in lesson pages.

## Open questions

- Is there a canonical Python version pinned for the course, or should snippets
  remain version-agnostic?
