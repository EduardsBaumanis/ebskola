# 6. tēma — Biroja lietotnes: spēles dokumentācija (plāns)

> **Status:** plan only. No lesson pages, tests or starter files exist yet.
> Write the lessons in the format of the existing Datorika 9 lessons: theory
> with examples, "Sākuma kods un darba vieta", three tasks with "Vide:",
> "Izmanto teoriju:" and "Gatavs, kad:", and "Iesniedz 3. uzdevuma rezultātu".

## Why this topic exists

After the 2026-11-23 law check (`datorika9/law-analysis-plan.md`), nine
results that this course counts as datorika have no lesson. They cover
office applications and research and citations, and topics 1–5 never open
a word processor, a spreadsheet or a presentation app:

- **2.4.1–2.4.4:** large structured text documents, spreadsheets, data
  display, presentations.
- **2.4.8, 2.4.9, 2.4.11:** app settings for productivity and security,
  moving content between documents with one-way sync, help systems and
  communities.
- **1.2.3:** researching existing similar solutions and judging how your own
  compares.
- **3.3.6:** intellectual property, personal data and correct citations in
  documents.

**The thread:** students document and present the game they published in
topic 5. They write a player's manual, collect playtest results in a
spreadsheet, chart them, link the chart into the manual, and pitch the game
in a presentation. Every file is about their own game, so the office skills
have a real purpose.

**Place in the course:** after topic 5. It needs a finished game to
document. The author decided on 2026-11-25 (D5) to keep the order: topics
1–5 stay as they are, and this is topic 6.

**Prerequisites:** topics 1–5, in particular the published game and README
(5.6), files and folders and saving (2.3–2.5), and the image and sound files
(2.3, 2.4).

## Results covered (MK Nr. 747, 7. pielikums, beidzot 9. klasi)

| Kods | Sasniedzamais rezultāts | Nodarbības |
|---|---|---|
| 2.4.1. | Veido lielus strukturētus dokumentus, izvēloties piemērotākos lappuses iestatījumus, rediģējot galveni un kājeni, pievienojot vēri, automātisko satura rādītāju, vairāklīmeņu sarakstus. Formatē teksta dokumentu atbilstoši normatīvajām prasībām. | 6.1, 6.2, 6.6 |
| 2.4.2. | Strukturē datus, izvēloties to piemērotāko attēlošanas veidu un racionālākos paņēmienus, izmantojot izklājlapu (rēķintabulu) lietotni. Veic datu apstrādi un analīzi, izmantojot datu kārtošanu un atlasi, aprēķinus. Veic darbības ar darbgrāmatas lapām. Importē un eksportē datus. | 6.3, 6.6 |
| 2.4.3. | Pārzina dažādus datu attēlošanas veidus (to skaitā tiešsaistē) un tos lieto atbilstoši savu mērķu sasniegšanai. | 6.4, 6.6 |
| 2.4.4. | Prezentācijas sagatavošanai un demonstrēšanai efektīvi izmanto prezentāciju lietotnes rīkus un tehniskas ierīces. Plāno, izveido un demonstrē prezentācijas saturu, ievērojot mērķauditoriju. Sagatavo izdales materiālus. | 6.5, 6.6 |
| 2.4.8. | Patstāvīgi pielāgo lietotnes iestatījumus atbilstoši lietotāja vajadzībām, lai paaugstinātu darba produktivitāti un drošību, ievērojot un izvērtējot veicamā uzdevuma specifiku. | 6.2 |
| 2.4.9. | Risinājuma radīšanā dublē dažāda veida saturu starp dažādu tipu dokumentiem, nepieciešamības gadījumā nodrošinot vienvirziena informācijas sinhronizāciju starp avota un mērķa dokumentu. | 6.4, 6.6 |
| 2.4.11. | Izmanto lietotņu palīdzības un atbalsta sistēmas, tiešsaistes kopienas, tai skaitā meklējot risinājumus nestandarta situāciju un nepazīstamu kļūdu paziņojumu izvades gadījumos. | 6.2, 6.3 |
| 1.2.3. | Atrod, apkopo un pēta pieejamo informāciju par konkrētās problēmas risināšanas iespējām un jau esošiem līdzīgiem risinājumiem. Novērtē sava risinājuma konkurētspēju ar esošajiem risinājumiem. | 6.5 |
| 3.3.6. | Ievēro intelektuālā īpašuma un personas datu aizsardzības noteikumus un izvērtē šo noteikumu neievērošanas sekas. Veidojot dokumentus, kuros ir citēta vai apkopota citos resursos atrastā informācija, veido korektas atsauces uz tās avotu. | 6.1, 6.5, 6.6 |

The lessons also revisit 2.4.7 (choosing apps), 2.4.10 (saving in a chosen
format and folder) and 1.5.1 (presenting the solution).

When the lessons are written, cite these in `.lesson-meta` in the current
format: `<a href="/sasnRez#dat9-2-4-1" title="{law text}">SR 2.4.1. {label}</a>`,
with 1–4 citations per lesson.

## Tools (Windows 11)

- **Word, Excel and PowerPoint from Microsoft 365.** The author decided this
  on 2026-11-25. The lessons use the desktop apps. The web versions lack
  Paste Link (6.4), Restrict Editing (6.2) and handout export (6.5). See
  open question 1.
- File Explorer and the topic folder `Desktop/datorika9-tema6`, as in
  topics 1–5.
- The student's published game from 5.6, and its GitHub Pages link.
- Free-licence image sources for 6.5: Wikimedia Commons, Pixabay, Openverse.

## Starter files

Topics 1–5 start from `sakuma-kodi/TS.html`. This topic starts from a
download kit, like `25.zip` and `26.zip`: `sakuma-kodi/6S.zip` holds the
office files. Each kit uses the course's sample game "Zvaigžņu mednieks", so
a student who has no finished game can still do every task.

**Phase 5 note:** the renaming regex must cover
`sakuma-kodi/(\d+)\.(html|zip)`, not just `.html`.

## Lessons

All student files go in `Desktop/datorika9-tema6`. Each lesson hands in the
task 3 file, as in topics 1–5. Office files are handed in as the original
file plus a PDF where the task says so.

### 6.1 Spēles rokasgrāmata: stili, saraksti un satura rādītājs

- **File:** `dat9_61.html`
- **Starter:** `sakuma-kodi/61.zip` holds `rokasgramata_61.docx`, an
  unformatted three-page manual for "Zvaigžņu mednieks" (plain paragraphs,
  manual bold for headings, a typed-in list of controls), and two
  screenshots.
- **Goal:** Šajā nodarbībā tu pārvērtīsi neformatētu tekstu par sakārtotu
  spēles rokasgrāmatu ar virsrakstu stiliem, vairāklīmeņu sarakstu, galveni,
  kājeni un automātisku satura rādītāju.
- **SR:** 2.4.1., 3.3.6.
- **Theory:**
  - Styles vs manual formatting: why "Heading 1" beats bold 16 pt.
  - The Navigation Pane.
  - Multilevel lists.
  - Page setup: margins, orientation, size.
  - Header and footer with page numbers.
  - A footnote (vēre) for a source.
  - An automatic table of contents, and why it needs updating.
- **Task 1 (try):** apply Heading 1 and 2 to the manual's sections and open
  the Navigation Pane. Change the Heading 1 style once and watch every
  heading change.
- **Task 2 (build):**
  - Rewrite the controls and rules as a multilevel list.
  - Add a header with the game's name and a footer with the page number.
  - Add a footnote that cites the source of one screenshot.
  - Insert an automatic table of contents on page 1.
- **Task 3 (break and test):**
  - Add a new section "Biežākās kļūdas" at the end and check that the table
    of contents is now out of date. Update it.
  - Then apply bold by hand to one heading instead of a style, and explain
    why it is missing from the table of contents. Fix it.
  - Hand in the `.docx` file.
- **Watch out:** the table of contents title and the heading style names
  differ between Latvian and English Word ("Virsraksts 1" / "Heading 1").
  Show both.

### 6.2 Iesniegums pēc noteikumiem un lietotnes iestatījumi

- **File:** `dat9_62.html`
- **Starter:** `sakuma-kodi/62.zip` holds `iesniegums_62.docx`. It is a
  request to the school director to use the computer lab for a class game
  tournament, with every requisite present but in the wrong place, and a
  one-page summary of the requisite rules.
- **Goal:** Šajā nodarbībā tu noformēsi iesniegumu atbilstoši dokumentu
  noformēšanas prasībām, pielāgosi Word iestatījumus drošākam un ātrākam
  darbam un atradīsi atbildi palīdzības sistēmā.
- **SR:** 2.4.1., 2.4.8., 2.4.11.
- **Theory:**
  - **Normatīvās prasības:** the requisites of an official document under
    MK 2018. gada 4. septembra noteikumi Nr. 558 "Dokumentu izstrādāšanas un
    noformēšanas kārtība"
    (<https://likumi.lv/ta/id/301436>): author, addressee, document type,
    date, title, text, signature. Its general requirements apply to
    documents by any person, so they cover a student's iesniegums. Dates
    are written day, month, four-digit year. Margins and fonts follow the
    school's requirements.
  - **Settings that matter:** AutoSave and AutoRecover interval, the
    default save folder, proofing language (latviešu), showing formatting
    marks, and units.
  - **Security:** Restrict Editing, Mark as Final, and Inspect Document,
    which removes the author name and comments, that is, personal data.
  - **Help:** Help and the "Tell me / Meklēt" box, Microsoft Support pages,
    and community forums. How to search for an unknown error message.
- **Task 1 (try):**
  - Turn on formatting marks and find the stray spaces and empty lines in
    the starter.
  - Set the proofing language of the whole document to Latvian and check
    that the spelling marks change.
- **Task 2 (build):**
  - Move the requisites to the right places using the summary.
  - Set the margins.
  - Save as `iesniegums_62.docx` and as a PDF.
- **Task 3 (break and test):**
  - The teacher's file `kluda_62.docx` opens as "Protected View" or
    read-only. Find out why with the help system and write the steps in two
    sentences.
  - Then run Inspect Document on your own file and remove the personal
    data.
  - Protect the file against editing.
  - Hand in the PDF and the protected `.docx`.
- **Open:** see open question 2 about which normative text to use.

### 6.3 Spēles testu rezultāti izklājlapā

- **File:** `dat9_63.html`
- **Starter:** `sakuma-kodi/63.zip` holds `speles_63.csv`: 60 playtest rows
  (spēlētājs, datums, līmenis, punkti, laiks_s, dzīvības_zaudētas). It uses
  `;` as the separator and `,` as the decimal mark, as a Latvian Excel
  exports.
- **Goal:** Šajā nodarbībā tu importēsi spēles testu datus izklājlapā,
  sakārtosi, atlasīsi un aprēķināsi, cik grūta ir katra spēles līmeņa
  spēle.
- **SR:** 2.4.2., 2.4.11.
- **Theory:**
  - Importing CSV with Data → From Text/CSV: separator, decimal mark,
    encoding (UTF-8 for ā, č, ņ).
  - Tables, sort and filter.
  - Formulas: `SUM`, `AVERAGE`, `MAX`, `COUNTIF`, `AVERAGEIF`.
  - Relative and absolute references (`$B$2`).
  - Worksheet operations: rename, copy, move, colour.
  - Exporting as CSV and PDF.
  - Using the function help (`fx`) to learn a function you don't know.
- **Task 1 (try):**
  - Import the CSV.
  - Sort by points and filter one level.
  - Find the best result for each level with the filter and `MAX`.
- **Task 2 (build):** a sheet "Kopsavilkums" with one row per level:
  number of games (`COUNTIF`), average points (`AVERAGEIF`) and average
  time. Add one column the student defines, for example points per second.
- **Task 3 (break and test):**
  - Open the same CSV by double-clicking it and see the broken numbers and
    letters. Explain what went wrong and fix the import.
  - Find `AVERAGEIFS` in the help system and use it for "level 2, only
    games over 60 s".
  - Hand in `testi_63.xlsx`.
- **Watch out:** Latvian Excel uses `;` between function arguments. Show
  formulas the way the students' Excel shows them.

### 6.4 Diagrammas un saistīta diagramma rokasgrāmatā

- **File:** `dat9_64.html`
- **Starter:** `sakuma-kodi/64.zip` holds the finished `testi_63.xlsx` (for
  students who missed 6.3) and the formatted `rokasgramata_61.docx`.
- **Goal:** Šajā nodarbībā tu izvēlēsies piemērotāko diagrammas veidu savam
  jautājumam, izveidosi to un ievietosi rokasgrāmatā tā, lai tā atjaunotos,
  mainoties datiem.
- **SR:** 2.4.3., 2.4.9.
- **Theory:**
  - Which chart answers which question: column to compare levels, line for
    change over time, pie for parts of a whole (rarely), scatter for "is
    time related to points?".
  - Axis titles, the y-axis starting at 0, and misleading charts.
  - Sharing data online: a live chart in Excel for the web or Google
    Sheets.
  - Paste vs Paste Link, one-way sync from source to target, Update Links,
    and what happens when the source file moves.
- **Task 1 (try):** make three charts of the same summary (column, pie,
  line) and say which one answers "Kurš līmenis ir visgrūtākais?" and why
  the others don't.
- **Task 2 (build):** a finished column chart with a title, axis titles and
  data labels. Paste it into the manual with **Paste Link** in a new
  section "Testu rezultāti".
- **Task 3 (break and test):**
  - Add five new games to the spreadsheet and check that the chart in the
    manual updates.
  - Then move the `.xlsx` to another folder, reopen the manual, and fix the
    broken link with Edit Links.
  - Hand in both files, zipped as `tema6_64.zip`.

### 6.5 Spēles prezentācija un līdzīgu spēļu izpēte

- **File:** `dat9_65.html`
- **Starter:** `sakuma-kodi/65.zip` holds `prezentacija_65.pptx`. It has
  six slides with too much text, mixed fonts, an image without a source,
  and no speaker notes.
- **Goal:** Šajā nodarbībā tu izpētīsi līdzīgas spēles, salīdzināsi ar tām
  savu un izveidosi īsu prezentāciju ar runātāja piezīmēm un izdales
  materiālu konkrētai auditorijai.
- **SR:** 2.4.4., 1.2.3., 3.3.6.
- **Theory:**
  - Audience first: classmates vs parents vs a jury.
  - One idea per slide, the slide master and the theme.
  - Speaker notes and Presenter View.
  - Embedding the game link and a short screen recording.
  - Handouts: three slides per page, exported to PDF.
  - Researching similar games: what to compare (goal, controls,
    difficulty, look) and how to say what is better or worse in yours.
  - Licences (CC BY, CC0, "all rights reserved"), the attribution line,
    and why a screenshot of someone else's game needs a source.
- **Task 1 (try):** fix the starter deck with the slide master (one font,
  one colour scheme) and cut two text-heavy slides to one idea each.
- **Task 2 (build):**
  - Find two similar browser games.
  - Make a comparison slide: three criteria and your game against the two.
  - Add a sources slide with correct attributions.
  - Write speaker notes for every slide.
- **Task 3 (break and test):**
  - Rehearse with Presenter View and a 3-minute timer, and cut what does
    not fit.
  - Export handouts (three per page) to PDF.
  - Hand in `prezentacija_65.pptx` and the handout PDF.

### 6.6 Noslēguma darbs: spēles dokumentācijas komplekts

- **File:** `dat9_66.html`
- **Starter:** `sakuma-kodi/66.zip` holds a checklist (`parbaude_66.docx`)
  and the sample game's finished set for reference.
- **Goal:** Šajā noslēguma darbā tu izveidosi savas spēles dokumentācijas
  komplektu — rokasgrāmatu, testu izklājlapu un prezentāciju — un to
  prezentēsi klasei.
- **SR:** 2.4.1., 2.4.2., 2.4.3., 2.4.4. (also 2.4.9., 3.3.6., 1.5.1.)
- **Step 1:** the manual for **your own** game: styles, a multilevel list,
  a header, a footer and a table of contents, a linked results chart, and
  footnoted sources.
- **Step 2:** a playtest spreadsheet with at least 15 games played by
  classmates: summary formulas and one chart.
- **Step 3:** a 3-minute presentation with a comparison slide, sources and
  speaker notes, given to the class. Hand in all three files and a PDF of
  each.
- **Assessment (SLA):**
  - The table of contents is automatic and up to date.
  - The formulas give correct results on the teacher's check row.
  - The chart type fits the question, and the linked chart updates.
  - The presentation fits the time and the audience.
  - Every image and screenshot has a source.
  - The files contain no personal data in their properties.

## Open questions for the author

1. **Desktop apps in the licence.** Microsoft 365 is decided. Check that
   the school's licence installs the desktop Word, Excel and PowerPoint on
   the classroom computers, not only the web apps.
2. **Which "normatīvās prasības" in 6.2.** MK Nr. 558 covers the
   requisites. Read its current consolidated text before writing the
   lesson to see whether it also sets fonts or margins. If it does not,
   use the school's own rules for written work for those.
3. **Office files in GitHub?** Topics 1–5 hand in a GitHub link at the end
   of each topic. `.docx`, `.xlsx` and `.pptx` are binary files: Git stores
   them, but diffs are useless. Hand them in directly instead, or keep the
   GitHub link only for the PDFs.
4. **Real playtest data.** 6.6 needs 15 games played by classmates. Either
   plan 10 minutes of cross-play in 6.5, or let the game log its own
   results. A "Lejupielādēt rezultātus (CSV)" button could be a topic 5
   extra task.
