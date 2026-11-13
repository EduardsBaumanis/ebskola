# Review · 10 · Instructional & UX Designer

> Improvement plan for learner flow, navigation and visual coherence across the
> four courses.

Severity: `Critical | Major | Minor | Nit`.

## What I reviewed

- Shared layout (`style.css`, `lesson.css`) and nav components: `course-topbar`,
  `sidebar-nav`, breadcrumb, `stundas-navigacija`.
- Course/topic overview pages and the `_redirects` rules that expose link bugs.

## Findings

- **Resolved · broken source links** — `_redirects` previously contained corrective
  rules for doubled/nested paths (`/programmesana1/programmesana1/prog1_6/…` and
  `/programmesana1/programmesana1/prog1_6/datorika9/dat9_3main…`). Verification
  showed all current `prog1_6` links are absolute and correct; the four stale
  redirects were removed. No malformed links remain.
- **Minor · sidebar heading style** — the topic heading differs in casing and
  separator across courses: "1. tēma — …" (Datorika 9) vs "1. Tēma - …"
  (Programmēšana I/Robotika). Standardize.
- **Positive** — breadcrumb, sidebar highlight (`aria-current="page"`) and
  prev/next navigation are present and correct in sampled lessons.
- **Verification item** — run a link crawler over all 148 lessons to find dead or
  wrong extensionless links before the redirects are cleaned up.

## Improvement plan

1. Crawl all internal links; fix the malformed ones in `prog1_6` and any others.
2. Standardize sidebar/breadcrumb heading casing and separator across courses.
3. Verify each `*_main.html` topic page accurately lists and links its 5–6 lessons.
4. Confirm the home page (`index.html`) course/topic index matches the real
   structure (4 courses, 25 topics).
5. Adopt the canonical lesson skeleton from Worker 3 so flow is identical per course.

## Open questions

- Are the nested-path redirects safe to remove immediately after link fixes, or
  should they stay for a grace period (cached URLs)?
