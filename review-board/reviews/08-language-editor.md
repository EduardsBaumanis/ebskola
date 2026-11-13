# Review · 8 · Latvian Language & Terminology Editor

> Improvement plan for grammar, style and terminology consistency across the
> Latvian-language material, anchored to the EN→LV glossary in `paligm.html`.

Severity: `Critical | Major | Minor | Nit`.

## What I reviewed

- Sampled lessons: `datorika9/dat9_11.html`, `programmesana1/prog1_1/prog1_11.html`,
  `robotika/rbtk7_11.html`, plus `README.md`.
- The terminology conventions in `README.md` (terms, EN→LV glossary pointer).

## Findings

- **Positive** — sampled Datorika 9 text is high-quality, imperative and clear
  ("Atver…", "Saglabā…", "Pārbaudi…"), with English UI labels kept in parentheses.
- **Minor · terminology writing** — the repo mixes "sākuma kods" (text) with the
  folder name `sakuma-kodi` and other hyphenated slug forms; confirm a single
  written form for every core term and apply it everywhere ("sākuma kods" vs
  possible "sākumkods").
- **Minor · UI-label convention** — English UI strings (Start, New → Folder,
  Install, Open, Sign in, Get) are handled slightly differently across courses
  (some bolded, some parenthesized, some with translations). Standardize one
  convention (e.g., bold English label + Latvian gloss in parentheses).
- **Verification item** — cross-check every technical term against `paligm.html`'s
  glossary and flag any term used in lessons that the glossary does not define
  (or defines differently).

## Improvement plan

1. Produce a short terminology style guide (core terms, EN-label convention,
   imperative-step voice) and add it near `review-board/`.
2. Run a full grammar/spelling pass over all 148 lesson pages and the overviews.
3. Diff lesson terminology against `paligm.html`; add missing glossary entries.
4. Standardize the formatting of English UI labels and the writing of core terms.

## Open questions

- Is "sākuma kods" (two words) the canonical written form, or "sākumkods"?
- May I add new EN→LV entries to `paligm.html`, or should they be proposed first?
