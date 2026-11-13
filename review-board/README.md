# Review Board — ebSkola

A set of 12 reusable AI "worker" personas for reviewing and improving the
[ebSkola](https://ebskola.lv/) project: free, open-source, Latvian-language
teaching materials for computer science, programming and robotics (grades 7–12).

Each persona is a self-contained prompt. To use one, copy the whole file and
paste it into a chat as the system/role prompt, then give it a concrete task
(e.g., "Review `datorika9/dat9_11.html`.").

## The board

| # | Persona | File | Primary focus |
|---|---------|------|---------------|
| 1 | Project Manager | `01-project-manager.md` | Coordinates reviews, prioritizes and consolidates findings |
| 2 | Curriculum & Standards Specialist | `02-curriculum-standards-specialist.md` | Alignment with MK noteikumi Nr. 416/747 and sasniedzamie rezultāti (SR) |
| 3 | Methodology & Didactics Specialist | `03-methodology-specialist.md` | Lesson structure, task scaffolding, assessment, SLA rubrics |
| 4 | Web Technologies Expert | `04-web-expert.md` | HTML / CSS / JavaScript accuracy (Datorika 9) |
| 5 | Python Expert | `05-python-expert.md` | Python / Flask / SQL / PostgreSQL accuracy (Programmēšana I) |
| 6 | Godot / C# Expert | `06-godot-csharp-expert.md` | Godot 4 .NET / C# accuracy (Programmēšana II) |
| 7 | Robotics & Electronics Expert | `07-robotics-expert.md` | LEGO SPIKE Prime / Arduino accuracy (Robotika) |
| 8 | Latvian Language & Terminology Editor | `08-language-editor.md` | Grammar, style, terminology and EN→LV glossary consistency |
| 9 | Accessibility & Inclusion Specialist | `09-accessibility-specialist.md` | Readability, UDHS/ADHD-friendly design, plain language |
| 10 | Instructional & UX Designer | `10-instructional-designer.md` | Learner flow, navigation, visual and course-page coherence |
| 11 | Technical QA & Consistency Reviewer | `11-qa-consistency.md` | Links, code blocks, starter-code sync, SEO/Schema.org, conventions |
| 12 | Student Perspective Reviewer | `12-student-perspective.md` | Beginner empathy: difficulty, motivation, clarity |

## Suggested workflow

1. **Scope** — give the Project Manager (1) the lesson(s) or course(s) to review.
2. **Parallel expert review** — run the relevant subject experts (4–7) on the
   same material, plus the cross-cutting reviewers (2, 3, 8, 9, 10, 12) when
   appropriate.
3. **Consolidation** — feed all findings back to the Project Manager (1) to
   deduplicate, resolve conflicts and produce one prioritized, actionable report.
4. **Apply & verify** — apply accepted fixes, then run the Technical QA (11) to
   confirm links, code blocks, starter-code sync and metadata are intact.

## Conventions shared by all personas

- **Project**: static HTML/CSS/JS site, no build step; MIT licensed; author Eduards Baumanis.
- **Language**: content is Latvian, aimed at students in grades 7–12 and their teachers.
- **Courses**: Datorika 9 (HTML/CSS/JS/VS Code/Git/GitHub Pages), Programmēšana I
  (Python, Flask, PostgreSQL), Programmēšana II (Godot 4 .NET + C#), Robotika
  (LEGO SPIKE Prime, Arduino/C++).
- **Standards**: Latvian MK noteikumi Nr. 416 and Nr. 747; sasniedzamie rezultāti
  (SR) are tracked in `sasnRez.html`.
- **Lesson skeleton** (shared by all courses): course topbar → topic sidebar →
  `<h1>{Topic}.{Lesson} {Title}</h1>` + `.lesson-goal` + `.lesson-meta` →
  theory in `.logic-box` → starter code (`data-copy` + `sakuma-kodi/NN.html`) →
  three tasks `#uzdevums-1..3` (`.step-list` steps + `.done-when` criterion) →
  optional `.extra-task` → troubleshooting → `teacher-meta` → prev/next navigation.
- **Naming**: `dat9_TS.html`, `prog1_TS.html`, `prog2_TS.html`, `rbtk7_TS.html`;
  topic pages `*_main.html`; extensionless URLs via `_redirects`.
