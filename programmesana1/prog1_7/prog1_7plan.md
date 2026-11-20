# 7. tēma — Lietotņu automatizācija un digitālā sadarbība (plāns)

> **Status:** plan only. No lesson pages exist yet. Write the lessons with
> `plan.md` section 4 (the task standard) and decisions D1–D8, F1–F4.

## Why this topic exists

Course goals 2 and 3 of Programmēšana I are about everyday applications,
information systems and online tools. The course so far uses Google Forms
(5.4) and Google Sheets (6.2), but never teaches:

- scripting inside an application;
- sharing documents with different permissions;
- formatting a large structured document;
- choosing tools for communication and planning.

This topic covers those four results and the general-level "find what can be
automated" (2.4.1). Topic 10 already covers the optimal-level 2.4.1.

**Place in the course:** after topic 6 (files and data). Topic 10 later uses the GitHub Issues board and the structured
document from this topic for its project documentation.

**Prerequisites:** topics 1–6. 7.5 reuses the survey answers from 5.4 and
the spreadsheet from 6.2.

## Results covered (MK Nr. 416, 7. pielikums)

| Kods | Līmenis | Sasniedzamais rezultāts | Stundas |
|---|---|---|---|
| 2.3.2. | optimālais | Izmanto dažādās lietotnēs pieejamās programmēšanas iespējas, izstrādājot vienkāršas programmas (skriptus), piedāvāto datu apstrādes iespēju papildināšanai un lietotāja darba produktivitātes paaugstināšanai. | 7.5, 7.6 |
| 2.3.2. | vispārīgais | Izmanto dažādu lietotņu piedāvātās dokumentu koplietošanas iespējas, nosakot atšķirīgiem lietotājiem atšķirīgas piekļuves, rediģēšanas un komentēšanas tiesības un iespējas. | 7.2, 7.6 |
| 2.3.3. | vispārīgais | Sagatavo, rediģē un formatē lielus strukturētus dokumentus, iekļaujot dažādus objektus (t. sk. attēlus, tabulas, vēres, mijnorādes, galvenes, kājenes, automātiskos satura, attēlu, priekšmetu (alfabētiskos) rādītājus, kā arī literatūras (avotu) sarakstu un atsauces uz tiem) un izmantojot lietotnēs iebūvētos darba efektivitātes un automatizācijas rīkus. | 7.3, 7.6 |
| 2.3.8. | vispārīgais | Izvēlas, pielāgo un lieto piemērotākos saziņas, informācijas ieguves un apmaiņas rīkus un citus interneta pakalpojumus, kā arī laika plānošanas rīkus, veicinot sava ikdienas un mācību darba produktivitāti un efektivitāti. | 7.4 |
| 2.4.1. | vispārīgais | Analizē vienkāršus ikdienas darba procesus, atpazīst automatizācijai piemērotas daļas un raksturo automatizācijas iespējas. | 7.1, 7.6 |

When the lessons are written, cite these in `.lesson-meta` in the current
format: short label, the law's text in `title`, and a link to
`/sasnRez#prog1-o-…` or `/sasnRez#prog1-v-…`.

## Tools (Windows)

- Google Workspace (Docs, Sheets, Drive, Apps Script) with the school Google
  account that 5.4 already uses. See the open questions for a Microsoft 365
  alternative.
- GitHub: repository collaborators, Issues and Projects (board view).
- Python standard library: `pathlib`, `shutil`, `datetime`.

## Lessons

All student files go in `tema07/` in the `programmesana-pamatkurss`
repository. Notes go in `README.md` under `### 14.x …` (D3). Apps Script
code is also copied into the repository as `.js` files, so it has a history.

### 7.1 Ko var automatizēt? Ikdienas darba procesi

- **File:** `prog1_71.html`
- **Goal:** Šajā stundā tu aprakstīsi vienu savu ikdienas darbu soli pa
  solim, atradīsi tajā atkārtojošās daļas un uzrakstīsi programmu, kas vienu
  no tām izdara tavā vietā.
- **SR:** 2.4.1. (vispārīgais)
- **Theory:** a process as steps with an input and an output. Signs a step
  can be automated: it repeats, follows a rule, and uses data that is
  already digital. Signs it cannot: it needs judgement or talking to people.
- **Task 1 (try):** list the steps of one routine (for example handing in
  homework or sorting phone photos). Mark each step A (automatable), D
  (partly) or N (no), with a reason.
- **Task 2 (build):** `kartot_71.py` sorts the files in a given folder into
  subfolders by extension with `pathlib` and `shutil.move`. Use a practice
  folder the program creates itself.
- **Task 3 (test):** run it twice, which should change nothing. Then try a
  file with no extension and a file name that already exists in the target
  folder. Add a "dry run" mode that only prints what it would do.
- **Watch out:** the program must never run on the student's real Documents
  folder. The practice folder is created by the program in `tema07/`.

### 7.2 Koplietošana un piekļuves tiesības

- **File:** `prog1_72.html`
- **Goal:** Šajā stundā tu koplietosi dokumentu un savu GitHub krātuvi trim
  cilvēkiem ar atšķirīgām tiesībām un pārbaudīsi, ka katrs var tieši to, kas
  atļauts.
- **SR:** 2.3.2. (vispārīgais)
- **Theory:** viewer, commenter, editor and owner. Link sharing vs named
  people. The principle of least privilege. Version history. GitHub roles
  (read, triage, write) and why the teacher gets read access.
- **Task 1 (try):** share one Google Doc with a classmate as commenter, and
  check what they can and cannot do.
- **Task 2 (build):** set up a project folder on Drive with three
  permission levels for a given brief: teacher can comment, teammate can
  edit, everyone with the link can view the final PDF only. Add the teacher
  as a collaborator on the GitHub repository.
- **Task 3 (test):** a classmate tries to edit, comment and download as each
  role. Record a table of expected vs actual results in the README. Fix any
  wrong setting.
- **Notebook:** when "anyone with the link" is a risk, with one example.

### 7.3 Liels strukturēts dokuments: projekta apraksts

- **File:** `prog1_73.html`
- **Goal:** Šajā stundā tu pārvērtīsi sava projekta piezīmes par noformētu
  dokumentu ar automātisku saturu, attēlu numerāciju, atsaucēm un avotu
  sarakstu.
- **SR:** 2.3.3. (vispārīgais)
- **Theory:** why styles beat manual formatting. Heading levels, automatic
  table of contents, captions and a list of figures, cross-references,
  footnotes, header and footer with page numbers, and a citation style.
- **Task 1 (try):** in a given unformatted text (a template doc), apply
  heading styles and insert the automatic table of contents.
- **Task 2 (build):** write a 5+ page description of an earlier project (for
  example the topic 6 quiz game). It needs captioned screenshots, one table,
  a cross-reference, a header/footer, and a source list with three sources.
- **Task 3 (test):** move one chapter to a new position and add one figure.
  Update the table of contents and the numbering, and check that nothing
  is numbered by hand. Export to PDF and commit the PDF to `tema07/`.
- **Watch out:** Google Docs has no automatic list of figures or index, and
  Word does. Say which features each program has (see open questions).

### 7.4 Saziņas un laika plānošanas rīki

- **File:** `prog1_74.html`
- **Goal:** Šajā stundā tu saplānosi divu nedēļu darbu GitHub dēlī un
  uzrakstīsi programmu, kas termiņus ieliek tavā kalendārā.
- **SR:** 2.3.8. (vispārīgais)
- **Theory:** comparing tools: chat, e-mail, forum and issue tracker;
  calendar, to-do list and kanban board. Choosing by the task:
  synchronous vs asynchronous, who needs to see what, and notifications vs
  focus.
- **Task 1 (try):** create three GitHub Issues for your next project and put
  them on a Projects board with the columns To do / Doing / Done.
- **Task 2 (build):** `kalendars_74.py` reads the deadlines from
  `termini_74.csv` and writes an `.ics` file by hand (plain text lines
  `BEGIN:VEVENT` …). Import it into Google or Outlook Calendar.
- **Task 3 (test):** a wrong date format and a deadline in the past. The
  program reports both and skips them. Re-import and check that the events
  are right.
- **Notebook:** a table of three tools you would choose for a group project,
  and why.

### 7.5 Skripti izklājlapā: Google Apps Script

- **File:** `prog1_75.html`
- **Goal:** Šajā stundā tu uzrakstīsi savu funkciju izklājlapai un izvēlnes
  pogu, kas vienā klikšķī sakārto aptaujas atbildes.
- **SR:** 2.3.2. (optimālais)
- **Theory:** applications that can be programmed (Sheets and Docs with
  Apps Script, Excel with VBA or Office Scripts, LibreOffice with Basic or
  Python). JavaScript only as far as needed: `function`, `let`, `for` and
  arrays, explained next to the Python the student already knows.
- **Task 1 (try):** a custom function `=PUNKTI(A2)` in Apps Script that
  returns a value. Use it in a cell.
- **Task 2 (build):** a script that reads the answers sheet from the 5.4
  survey, counts the answers per option, and writes a summary to a new sheet.
  `onOpen` adds the menu item "ebSkola → Apkopot".
- **Task 3 (test):** empty rows, an unexpected answer and a re-run that must
  not duplicate the summary. Copy the final code into `tema07/apkopot_75.js`
  and commit it.
- **Watch out:** this is the first JavaScript in Programmēšana I (topic 16
  uses it again for `fetch`). Show a side-by-side Python ↔ JS table once.

### 7.6 Noslēguma projekts: Klases pasākuma plānotājs

- **File:** `prog1_76.html`
- **Goal:** Šajā projektā tu izveidosi koplietotu pasākuma plānotāju:
  izklājlapu ar skriptu, kas sagatavo uzdevumu sarakstu un atgādinājumus,
  pareizas piekļuves tiesības un noformētu lietošanas instrukciju.
- **SR:** 2.3.2. (optimālais), 2.3.2., 2.3.3., 2.4.1. (vispārīgais)
- **Step 1:** process analysis in the README. Describe how the class plans
  an event today and mark the steps to automate (from 7.1).
- **Step 2:** a Sheets planner (tasks, people, deadlines). An Apps Script
  menu marks overdue tasks and builds a per-person task list in a new sheet.
  Optionally it e-mails each person their list.
- **Step 3:** sharing (organisers edit, class comments, the teacher views),
  plus a 2–3 page user guide document with styles, a table of contents and
  captioned screenshots.
- **Assessment (SLA):** the script runs on new data without errors and does
  not duplicate output; the permissions match the brief and are tested; the
  guide uses automatic structure; and the process analysis gives reasons for
  what was and was not automated.

## Open questions for the author

1. **Google or Microsoft?** Topics 5–6 already use Google Forms and Sheets,
   so Apps Script is the natural choice. If the school is on Microsoft 365,
   the same lessons work with Word, Excel and Office Scripts, but 7.5 and
   7.6 would need to be rewritten in TypeScript.
2. **Index in 7.3.** The law lists "priekšmetu (alfabētiskos) rādītājus" and
   lists of figures. Google Docs cannot make these automatically, and Word
   can. Is Word available, or is that part covered with a note?
3. **E-mail in 7.6.** `MailApp` needs extra authorisation and can hit the
   school's sending limits. Keep it optional?
