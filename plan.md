# Programmēšana I — plan for clearer lesson tasks

Goal: a student with weak technical skills can finish every task in
`programmesana1/` alone, by doing exactly what the steps say, and can tell
whether the result is right.

Based on a read of the course page, all 12 `prog1_Nmain.html` topic pages and
all 72 lesson pages (2026-11-16, commit `18596e1`).

> **Renumbered on 2026-11-20.** Four planned topics were added and the course
> now has 16 topics. Every topic and lesson number in this file uses the new
> numbers: old 7 → 8, 8 → 10, 9 → 11, 10 → 13, 11 → 14, 12 → 16. Topics 7, 9,
> 12 and 15 are planned only (`prog1_N/prog1_Nplan.md`).

---

## 1. The course as it is now

| # | Topic | Lessons use | Final project (x.6) |
|---|---|---|---|
| 1 | Darba vide un versiju kontrole | VS Code, GitHub Desktop, `.gitignore`, Markdown | `pd1/` mini-project on GitHub |
| 2 | Python pamati un ievade/izvade | `input`, `int`/`float`, operators, f-strings, PEP 8 | Skaitļu duelītis |
| 3 | Vadības struktūras un validācija | `if`, `and/or/not`, `while`, `try/except`, lists + `for` | Akmens-šķēres-papīrs |
| 4 | Funkcijas un modularitāte | `def`, `return`, `import`, scope, dict, flowcharts | Skaitļu minētājs |
| 5 | Kolekcijas un datu analīze | list, dict, `for`, survey → Python data | Atmiņu kāršu spēle |
| 6 | Datu pastāvība | text files, CSV from Google Sheets, JSON | Quiz ar highscore |
| 7 | *Lietotņu automatizācija un digitālā sadarbība* | planned: `prog1_7/prog1_7plan.md` | Klases pasākuma plānotājs |
| 8 | Algoritmi un efektivitāte | linear/binary search, bubble sort, Big O, `set` | Koda lauzējs |
| 9 | *Izstrādes modeļi, dizains un IT profesijas* | planned: `prog1_9/prog1_9plan.md` | Prototips iterācijās |
| 10 | Projektēšana un plānošana | problem statement, user stories, ER/UI, pitch, plan | Projektējuma aizstāvēšana |
| 11 | Web integrācija un bibliotēkas | `venv`, `pip`, `requests`, licences, **Streamlit** | Krustiņi un nullītes (Streamlit) |
| 12 | *Mākslīgais intelekts un atvērtie dati* | planned: `prog1_12/prog1_12plan.md` | MI palīgs pārlūkā |
| 13 | Datubāzes un PostgreSQL | `CREATE TABLE`, CRUD, FK, `JOIN`, `psycopg2` | Highscore datubāze |
| 14 | OOP | classes, `__init__`, methods, inheritance, dunder | Klases turnīra simulators |
| 15 | *Datortīkli, ierīces un droša darba vide* | planned: `prog1_15/prog1_15plan.md` | Datorklases tehniskais pārskats |
| 16 | Pilnvērtīga izstrāde un deploy | HTTP, Flask, REST, `fetch`, Render | Daudzspēlētāju krustiņi |

Every lesson has the same skeleton, and it is a good one:

1. `<h1>`, `.lesson-goal`, SR links (`.lesson-meta`)
2. Theory in a `.logic-box` with a short code sample; topics 1–6 also have one collapsed self-check question
3. Three tasks (`#uzdevums-1..3`): one sentence "Beigās…", 5–7 numbered steps, `Gatavs, kad:`
4. One collapsed extra task
5. "Biežākās kļūdas" and a full "Koda piemērs" with its output
6. x.6 lessons add a rubric (SLA) and a self-check list

In numbers: 72 lessons, 216 tasks, about 1,400 steps. Lessons average 725–930
words. There are no screenshots, no starter code and no copy buttons anywhere
in the course. No task contains a code block; all code sits inline inside a
step sentence.

What already works and should stay: the three-task rhythm (try → build →
break and test), the `Gatavs, kad:` criterion on every task, the "salauz kodu
un izlasi kļūdu" tasks, and the Latvian glosses on English buttons in topic 1.

---

## 2. What stops a weak student

### 2.1 Blockers: following the steps literally fails

All seven were fixed on 2026-11-16. The table records what was wrong and what
the lesson says now. The edits are in the working tree, not yet committed.

| Where | Was | Now |
|---|---|---|
| 4.3, 4.6, topic 4 page | `import 43_punkti` and `from 46_spele import …` were a `SyntaxError`: a module name cannot start with a digit. Tasks 2 and 3 of 4.3 could not be done. | Modules are named number-last (`punkti_43.py`, `spele_46.py`). 4.3 explains the rule in the theory and under "Biežākās kļūdas". All 4.3 steps were run and give the errors the lesson names. |
| 5.6, 6.6 "Darba uzdevuma gaita" | Same trap with `56_engine.py`, `56_data.py`, `66_data.py`, `66_spele.py`, `66_highscore.py`. | Renamed to `engine_56.py`, `data_56.py`, `data_66.py`, `spele_66.py`, `highscore_66.py`. |
| 1.1 task 1 | No step installed Python itself; the topic 1 cheatsheet described a different installer ("Add Python to PATH"). | Step 3 installs Python from Microsoft Store before VS Code is opened. Goal, title, error list and cheatsheet agree. |
| 11.3 | `streamlit run 113.py` with no install step. | Task 1 starts with activating `venv` and `pip install streamlit`; the run step covers the first-launch email prompt. |
| 13.1 | First step was "Atver pgAdmin vai izpildi `psql -U postgres`": no install, no password. | New "Pirms sāc: uzstādi PostgreSQL (Windows)" section: installer, `postgres` password, first login in SQL Shell (psql). Task 1 starts from there. |
| 13.5, 16.2 | `pip install psycopg2-binary` and `pip install flask` only in a theory sentence. | First two steps of task 1 install the library and check it. |
| 16.5 | `.env` was created but never loaded, so `os.environ.get(...)` returned `None` locally. | Task 1 installs `python-dotenv`, adds `load_dotenv()`, shows the `.env` format and has a check that prints `True`. |

Not verified here (Windows-only, and this machine has no `pip`): the Microsoft
Store Python package, the PostgreSQL installer, the `pip install` steps and
`python-dotenv`. Run each once on a school computer.

### 2.2 Patterns that repeat in almost every lesson

1. **The student is not told where they are.** Steps start with "Ieraksti failā
   `21.py`…" without saying to create the file, in which folder, or which
   program to be in. Topics 5, 6, 10, 11, 13, 14 and 16 never say where files go. Topic 1
   puts `11.py` and `12.py` in a desktop folder, then moves to the cloned
   repository without moving them. Topics 8 and 10 create new folders outside
   the repository with PowerShell (`mkdir`, `ni`, `code .`), which is a third
   way of working.
2. **Steps get vaguer as the course gets harder.** Topic 2 gives the exact
   line to type. From topic 5 on, many steps are a whole sub-problem in one
   line: "Uzraksti `while True:` ciklu ar izvēlni" (5.1), "Pārbīdi `apaksa`
   vai `augsa` atkarībā no salīdzinājuma" (8.1), "Atrodi vai izveido spēlētāju
   un atgriez viņa `id`" (13.6), "Uzraksti metodi `uzvaretajs(self)`" (16.6).
   There is no hint and no fallback if the student cannot do it.
3. **Expected output is rarely shown.** A step says "Palaid un pārbaudi", but
   the student does not see what a correct terminal looks like until the final
   code sample below all the tasks.
4. **"Pieraksti…" has no destination.** 147 of 159 "Pieraksti" steps do not say
   where to write (notebook, comment, file). The answer is also not something
   the teacher can see on GitHub. (Decided: the student's `README.md`, D3.)
5. **Tasks continue from each other without saying so.** "Ieliec šo rindu `try:`
   blokā" (3.4) or "Pievieno failā `143.py` klasē…" (14.3) assume code from an
   earlier task or lesson is already in the file. A student who was absent, or
   who started a new file, has nothing to add to.
6. **English term first, Latvian second.** "Type casting (Datu tipu
   konvertācija)", "Exponentiation (Kāpināšana)", "Read-Modify-Write". Lesson
   goals use teacher verbs ("Diferencēt mainīgo tvērumu", "Identificēt…").
7. **The worked example comes last.** "Koda piemērs" is close to the finished
   solution but sits after the tasks, so it works as an answer key, not as a
   model to learn from.
8. **Final projects have two sets of instructions.** 4.6, 5.6 and 6.6 contain
   a "Darba uzdevuma gaita" (three levels) and then three tasks that describe
   a different route to the same program (5.6: a 4×4 board with 8 pairs in
   one, 2 pairs in the other; 6.6: 10 questions in one, 5 in the other). Rubrics grade things the tasks never
   ask for (2.6: README, ergonomics note, "vismaz trīs operatori").
9. **Leftovers and duplicates.** 2.1 and 2.2 teach the same thing twice. 8.4
   and 8.5 have nearly the same goal. 2.3 "Biežākās kļūdas" talks about
   "spēlētāju skaits" in a task about bags. 5.4 creates `54.py` in task 1 and
   again in task 3. 1.4 shows the shortcut as `Ctrl+`` with broken formatting.

### 2.3 Topic pages that describe a different lesson

The student reads the topic page first, so a wrong promise costs trust.

| Page | Says | Lessons actually do |
|---|---|---|
| Topic 11 cards, hero, CTA; course page | Flask, Jinja2 templates, `fetch`, REST | Streamlit throughout (Flask starts in 16.2) |
| Topic 10 hero and 10.6 card; course page | `unittest`, "skolēnu vērtēšanas sistēma", GitHub Issues | Design documents for Krustiņi un nullītes, no tests |
| 8.4, 8.5 cards | `timeit`; `map`, `filter`, `reduce` | `time.time()`; `sorted` vs bubble sort, list vs `set` |
| 6.4 card | highscore table in CSV | highscore in JSON |
| 5.4, 5.5 cards | CSV export, `Counter` | answers typed by hand into lists |
| 16.2 card | Blueprints, Flask-SQLAlchemy | plain Flask routes with a list |
| 2.5 card; 2.6 on course page | "skaitļu minēšanas spēle ar plūsmas shēmu"; "Interaktīvs kalkulators" | pseudocode for the duel; Skaitļu duelītis |
| 11 hero | RPG cīnītāji, `Maģis` | `Dalibnieks`, `Kapteinis`, `Prezentetajs` |

Which side changes: for topic 11 the pages change to match the lessons (D4).
For topic 10 the lessons change to match the page: `unittest` is added (D5).
Everywhere else the topic page follows the lesson.

---

## 3. Decisions

Decided by the author on 2026-11-16. Every rewritten lesson follows these.

| # | Decision | What it means in the lessons |
|---|---|---|
| D1 | **GitHub Desktop is the way in.** The student starts in GitHub Desktop and opens VS Code from there. | From 1.3 on, every lesson starts: GitHub Desktop → repository `programmesana-pamatkurss` → **Fetch origin** → **Open in Visual Studio Code**. Every lesson ends: save → GitHub Desktop → **Summary** → **Commit to main** → **Push origin**. VS Code therefore always has the repository root open. No "File → Open Folder" after 1.2, and no PowerShell folder setup (topics 8 and 10). 1.1 and 1.2 come before the repository is cloned; 1.3 moves `11.py` and `12.py` into it. |
| D2 | **Lesson number goes last** in file names, in all lessons. | Any file that is imported: `punkti_43.py`, `spele_46.py`, `test_104.py`. A file that is only run stays `43.py`. Applies to every new file the rewrites introduce. |
| D3 | **`README.md` is the student's notebook.** | Every "Pieraksti" step says: open `README.md`, go to this lesson's heading, finish this sentence. No answers in code comments or loose files. The teacher reads the notebook on GitHub. |
| D4 | **Topic 11 stays Streamlit.** | Lessons keep their content. Rewrite what describes them wrongly: topic 11 page (hero, six cards, closing strip, `<head>` description), topic 11 row and project card on the course page, and the Programmēšana I line in the repository `README.md`. |
| D5 | **Topic 10 gets `unittest`.** | The lessons change to match the topic page, not the other way round. See 3.1 for where it goes. |
| D6 | **Help fades; "Biežākās kļūdas" goes.** | Task 1 gives exact lines, task 2 a skeleton with gaps, task 3 tests and breaks it. The "Biežākās kļūdas" section is removed from every lesson (60 lessons have one). Each task gets one collapsed "Iestrēgi?" block directly under it, holding the hints for that task's harder steps and the errors a student meets there. |
| D7 | **2.1/2.2 and 8.4/8.5 stay, each with its own job.** | 2.1 = data types and `type()`; 2.2 = `input` and conversion. 8.4 = built-in functions vs own loop; 8.5 = choosing the data structure. |
| D8 | **Windows only.** | Remove every macOS/Linux mention, including in troubleshooting and on topic pages. Found so far: 1.1, topic 1 page, 11.1 (`source venv/bin/activate`, `pip3`), topic 11 page. |

### 3.1 Follow-ups to those answers

All four proposals were accepted by the author on 2026-11-16 and count as
decisions.

| # | Question | Decided |
|---|---|---|
| F1 | **Folders inside the repository.** With D1, VS Code opens the repository root, so the Run button most likely runs programs from the root. A lesson file in a subfolder that opens `61_dati.txt` would then not find a file sitting next to it. (Imports such as `import punkti_43` are not affected.) | One folder per topic, `tema01` … `tema16`. In 1.4 the student adds `.vscode/settings.json` with `"python.terminal.executeInFileDir": true`; it is committed, so it follows the repository to any computer. Test this on a school computer in the pilot. If it does not hold, fall back to keeping all lesson files in the repository root. |
| F2 | **README as project page and notebook at once.** 1.5 currently tells the student to delete the README content and write a project description; 1.6 has its own `pd1/README.md`. | Top of `README.md` = project description (1.5). Below it a section `## Piezīmes` with one heading per lesson (`### 2.1 Ievade un datu tipi`). The notebook starts in 1.3, the first lesson with the cloned repository; "Pieraksti" steps in 1.1–1.2 become things to check on screen. After 1.3 the README is edited only in VS Code, never on github.com, to avoid merge conflicts. |
| F3 | **Where `unittest` goes in topic 10.** All six lessons are taken. | 10.4 becomes "Testēšana ar unittest": the acceptance criteria from 10.2 turn into tests for one small function (`spele_104.py`, `test_104.py`). The pitch from 10.4 moves into 10.6, which already ends with a three-minute presentation. 10.5 adds "all tests pass" to the Definition of Done; 10.6 shows the tests running. This changes the title of 10.4 everywhere it appears. |
| F4 | **Does D2 also cover data files?** | No: `61_dati.txt`, `66_jautajumi.json` keep their names, since they are never imported. |

---

## 4. The standard: what a clear task looks like

A lesson is done when every rule holds. Programmēšana II steps are the model
for step wording ("**what:** where to click and what to type").

**Lesson level**

- L1. A "Pirms sāc" box before task 1 with the same routine in every lesson:
  open GitHub Desktop, check **Current repository**, **Fetch origin** (and
  **Pull origin** if it appears), then **Repository → Open in Visual Studio
  Code**. Use the menu path, not the button on the start screen: the button
  disappears as soon as there are uncommitted changes. Then: which file to create or continue, in which
  folder, what must be installed, and which earlier file is needed (with a
  link to that lesson).
- L2. The goal is one plain sentence about what the student will have at the
  end ("Šajā stundā tu uzrakstīsi programmu, kas…"), not a list of teacher verbs.
- L3. Latvian term first, English in brackets once: "datu tipu pārveidošana
  (*type casting*)". After that, only the Latvian term.
- L4. A short worked example sits before the tasks. The full "Koda piemērs"
  moves into a collapsed "Parādīt pilnu risinājumu" at the end.
- L5. Every tool is installed by a step, in the lesson where it is first used.
- L6. A "Stundas beigās" block after task 3: save, GitHub Desktop, a given
  **Summary** text, **Commit to main**, **Push origin**, check the file on
  github.com. Today only the x.6 lessons do this.
- L7. No "Biežākās kļūdas" section. Its useful entries move into the
  "Iestrēgi?" block of the task where the error happens (S5).
- L8. Windows only. No macOS or Linux commands, paths or notes anywhere.

**Step level**

- S1. One action per step. If a step has "un", check whether it is two steps.
- S2. The step says where: program, file, and place in the file ("faila
  beigās", "zem rindas `while True:`, ar atkāpi").
- S3. Code longer than one short line goes in a code block inside the step,
  not inline in the sentence. Indentation is visible.
- S4. After every "Palaid", show what the terminal should print, and name the
  test input ("ievadi `Lācis`, `10`, `1.5`").
- S5. Each task ends with one collapsed "Iestrēgi?" block
  (`details.course-help`, inside the task section, after `Gatavs, kad:`). It
  holds, by step number, the code for every step that did not give it, and the
  errors typical for this task with the fix. A step may ask the student to
  write code on their own only if the answer is in this block.
- S6. English interface labels are bold and glossed the same way everywhere:
  **Push origin** (nosūtīt uz GitHub).
- S7. "Pieraksti" always goes to the notebook and gives a sentence starter:
  "Atver `README.md` un zem virsraksta `### 3.3` pabeidz teikumu:
  *break atšķiras no continue ar to, ka …*".
- S8. A task that builds on earlier code starts with "Turpini failā `33.py`.
  Tajā jau jābūt šim kodam:" and shows that code.

**Task level**

- T1. `Gatavs, kad:` is something the student can see on screen, not something
  they "can explain".
- T2. 5–8 steps. A longer task is split, not compressed.
- T3. In x.6 lessons there is one set of instructions, and each rubric row
  points to a step that asks for it.
- T4. Help fades across the lesson: task 1 gives the exact lines, task 2 gives
  a skeleton with `___` gaps, task 3 has the student test and break the code.

**Technical**

- X1. Every code block was run. The printed output in the lesson is the real
  output, including the exact error name in "break it" steps.
- X2. Keep the page structure: `section.lesson-task#uzdevums-1..3`,
  `.task-number`, `ol.step-list > li`, `.done-when`, `details.course-help`.
  `lesson.js` attaches the step checkboxes to `.lesson-task > .step-list > li`.
  The fixed blocks are `section.lesson-prep#pirms-sac` and
  `section.lesson-wrapup#stundas-beigas` (styled in `lesson.css`). Expected
  terminal output is a `<pre><code class="language-none">` inside the step.
  Lesson 1.3 is the reference page for all of this.
- X3. Do not touch `<head>` metadata unless the lesson title changes.
- X4. A file that is imported never starts with a digit; the lesson number
  goes last (`punkti_43.py`).

**Example: the two fixed blocks (L1, L6), here for 2.1**

> **Pirms sāc**
> 1. Atver **GitHub Desktop** un pārbaudi, vai augšā kreisajā stūrī pie
>    **Current repository** ir `programmesana-pamatkurss`.
> 2. Nospied **Fetch origin**. Ja poga pārvēršas par **Pull origin**, nospied
>    arī to.
> 3. Izvēlies **Repository → Open in Visual Studio Code**.
> 4. VS Code kreisajā pusē mapē `tema02` izveido jaunu failu `21.py`.

> **Stundas beigās**
> 1. Saglabā visus failus ar `Ctrl+S`.
> 2. Pārslēdzies uz **GitHub Desktop**. Kreisajā pusē jābūt `21.py` un `README.md`.
> 3. Laukā **Summary** ieraksti `Pievieno 21.py un piezīmes`.
> 4. Nospied **Commit to main**, pēc tam **Push origin**.

**Example: one step (2.1, task 1)**

Now:

> Ieraksti failā `21.py` rindu `a = "5"` un zem tā `b = 5`.

After:

> 1. **Ieraksti failā `21.py` šīs trīs rindas:**
>    ```python
>    a = "5"
>    b = 5
>    c = 5.5
>    ```
> 2. **Pievieno izdruku** zem tām:
>    ```python
>    print(type(a))
>    print(type(b))
>    print(type(c))
>    ```
> 3. **Palaid** ar zaļo **Run** pogu. Terminālī jāparādās:
>    ```
>    <class 'str'>
>    <class 'int'>
>    <class 'float'>
>    ```

**Example: a vague step and its "Iestrēgi?" block (8.1, task 2)**

Now:

> Pārbīdi `apaksa` vai `augsa` atkarībā no salīdzinājuma.

After, in the step list:

> 6. **Salīdzini vidējo elementu ar meklēto.** Cikla iekšpusē, zem rindas
>    `vidus = …`, pabeidz šo kodu:
>    ```python
>    if saraksts[vidus] == mekletais:
>        return vidus
>    elif saraksts[vidus] < mekletais:
>        apaksa = ___      # meklētais ir pa labi no vidus
>    else:
>        augsa = ___       # meklētais ir pa kreisi no vidus
>    ```

After, under the task:

> **Gatavs, kad:** abas funkcijas atrod vienu un to pašu skaitli.
>
> ▸ **Iestrēgi?**
> - **6. solis:** `apaksa = vidus + 1` un `augsa = vidus - 1`.
> - **Programma neapstājas:** trūkst `+ 1` vai `- 1`. Apturi ar `Ctrl+C`.
> - **Vienmēr atgriež -1:** saraksts nav sakārtots. Pirms meklēšanas izsauc
>   `saraksts.sort()`.

**Example: a notebook step (3.3, task 3)**

Now:

> Pieraksti vienu secinājumu: ar ko `break` atšķiras no `continue`.

After:

> 7. **Pieraksti secinājumu.** Atver `README.md` un zem virsraksta `### 3.3`
>    pabeidz teikumu: *`break` atšķiras no `continue` ar to, ka …*

---

## 5. Order of work

**Phase 0 — decisions.** Done (section 3, including the follow-ups in 3.1).

**Phase 1 — blockers.** Done (section 2.1). Open: one run-through of the
install steps on a school computer.

**Phase 2 — pilot (3 lessons).** Rewrite 1.3, 2.1 and 5.1 to the full
standard. 1.3 is rewritten (2026-11-16) and waits for the author's review;
2.1 and 5.1 follow after that review.

- 1.3 is where the GitHub Desktop routine and the README notebook begin; every
  later "Pirms sāc" and "Stundas beigās" copies it.
- 2.1 is the first ordinary code lesson and becomes the template.
- 5.1 is where steps first turn vague, so it tests the "Iestrēgi?" block.

During the pilot, also settle these once:

- the look of "Pirms sāc", "Iestrēgi?", "Stundas beigās" and the
  expected-output block in `lesson.css`;
- on a school computer: that **Open in Visual Studio Code** works with VS Code
  installed from Microsoft Store, and that the working-directory setting (F1)
  behaves as expected;
- the lesson skeleton text in the repository `README.md` and
  `review-board/README.md`, which still list a "Biežākās kļūdas" section.

Review the three lessons in the browser, adjust this standard and the prompts,
and only then continue.

**Phase 3 — lesson by lesson, topic by topic.** Order: 1 → 2 → 3 → 4 → 5 → 6,
then 11 → 13 → 16 (most setup risk), then 8 → 14 → 10. One lesson per commit.
After the sixth lesson of a topic, do the topic wrap-up. Topic 10 is last
because it is the only one whose content changes (D5).

**Phase 4 — topic wrap-up (after each topic).** Sync the six cards, hero and
cheatsheet on `prog1_Nmain.html`, and the topic's row and project card on
`programmesana1.html`, with what the lessons now say. Remove macOS/Linux lines
from the topic page. Check that files named in one lesson exist where the next
lesson expects them, and that the student's README has a heading for each
lesson of the topic.

**Phase 5 — real-student check.** Give one rewritten lesson per topic to a
student who struggles, without help, and watch where they stop. Each stop is a
missing step. This is the only test that proves the goal.

---

## 6. Prompts

Run these per lesson, in order. Replace `T.S` and the path. Each prompt is
written to work in a fresh session.

### Prompt A — review (no edits)

```text
Read plan.md sections 3 and 4, then read programmesana1/prog1_T/prog1_TS.html
and the lesson before it.

Act as the reviewers in review-board/12-student-perspective.md and
review-board/13-lesson-clarity-reviewer.md. The reader is a 10th-12th grade
student with weak technical skills, on a Windows school computer, who starts
in GitHub Desktop and does exactly what each step says and nothing more.

Walk through the lesson step by step as that student. For every step where
they would stop, guess, or get a different result than the lesson claims,
report: the step quoted, which rule from plan.md section 4 it breaks, and what
the student would actually see. Also list anything the lesson needs that an
earlier lesson did not provide (a file, a tool, a concept).

Run every Python/SQL/shell snippet you can run and report real output where it
differs from the lesson. Do not edit any file. Finish with the five changes
that would help this student most, in order.
```

### Prompt B — rewrite

```text
Apply the review findings to programmesana1/prog1_T/prog1_TS.html so the
lesson follows the decisions in plan.md section 3 and meets every rule in
section 4. In particular:
- "Pirms sāc" starts in GitHub Desktop and opens VS Code from there;
- each task ends with a collapsed "Iestrēgi?" block, and the "Biežākās
  kļūdas" section is gone, with its useful entries moved into those blocks;
- every "Pieraksti" step goes to README.md under this lesson's heading;
- the lesson ends with "Stundas beigās" (commit and push);
- Windows only; imported files have the lesson number last.

Keep: the lesson topic, the three tasks and their purpose (try, build, break
and test), the SR links, the <head>, all ids and class names, and the
difficulty of what the student builds. Change only how it is explained. Write
in plain Latvian, "tu" form, short sentences. Do not add new concepts.

Before writing, build the finished student files for this lesson in the
scratchpad by following your own steps literally, and run them. Every output
block in the lesson must be copied from a real run.

When done, list what changed per task, and anything you could not verify
(installs, GUI steps, accounts) so I can test it on a school computer.
```

### Prompt C — verify

```text
You are a student who has only done lessons up to T.(S-1). Open
programmesana1/prog1_T/prog1_TS.html and follow it from "Pirms sāc" to
"Stundas beigās", typing exactly what the steps say into new files in the
scratchpad. Do not use knowledge the lesson does not give. Open "Iestrēgi?"
only when a step cannot be done without it, and say which steps needed it.

Report every point where a step was ambiguous, where your output differed from
the lesson, or where "Gatavs, kad" could not be checked on screen. Then check
the page itself: three tasks with ids uzdevums-1..3, steps are direct <li>
children of ol.step-list, each task has one "Iestrēgi?" block, no "Biežākās
kļūdas" section, no macOS/Linux text, code blocks have language-* classes,
prev/next links are right. Report only; do not fix.
```

### Prompt D — topic wrap-up

```text
All six lessons of topic T are rewritten. Read them, then update
programmesana1/prog1_T/prog1_Tmain.html (hero, six lesson cards, cheatsheet)
and topic T's entries on programmesana1/programmesana1.html so every title,
description, file name and code sample matches the lessons. Run the cheatsheet
code. Remove any macOS/Linux lines. Then check continuity: every file a lesson
says "turpini failā …" or "nokopē no …" was created by an earlier lesson under
the same name and folder, and every "Pieraksti" step names a README heading.
List what you changed and any mismatch you left for me to decide.
```

Tips for prompting:

- One lesson per session keeps the review honest; a session that just wrote
  the lesson is a poor judge of it. Run Prompt C in a new session.
- When a rewrite is not what you wanted, say what the student would
  experience ("a student who missed 3.3 cannot start task 2"), not only
  "make it clearer".
- If the same correction comes up three lessons in a row, add it as a rule in
  section 4 instead of repeating it in prompts.

---

## 7. Notes per topic

- **Topic 1.** This topic builds the routine every later lesson relies on.
  1.1 and 1.2 run before there is a cloned repository. 1.3 clones it, moves
  `11.py` and `12.py` in, starts the README notebook and teaches "open VS Code
  from GitHub Desktop". 1.4 sets up the folder layout (F1). 1.5 must stop
  telling the student to delete the README content (F2). 1.2 uses an f-string
  a full topic before 2.3 teaches it: give the line as-is and say it is
  explained later. Remove the macOS/Linux lines in 1.1 and on the topic page.
  GUI-heavy lessons are where screenshots would help most.
- **Topic 2.** Separate 2.1 and 2.2 (D7). 2.1, 2.3 ask for notes as code
  comments; move them to the README (D3). 2.5 never says which game is being
  planned; state it. It also asks for a Markdown table, which 1.5 did not
  teach. Align the 2.6 rubric with the tasks.
- **Topic 3.** Clearest topic for code. Main gap is continuity: 3.3 and 3.4
  tasks 2–3 extend task 1 without showing the starting code.
- **Topic 4.** Module names are fixed. 4.6: merge "Darba uzdevuma gaita" and
  the three tasks into one route. 4.5: say where the flowchart is drawn and
  how it gets into the repository.
- **Topic 5.** First topic with large vague steps (5.1 task 2, 5.5 task 1,
  5.6 task 2). 5.4: name the tool (Google Forms) and give click-by-click steps;
  fix the double creation of `54.py`. 5.6: one set of instructions.
- **Topic 6.** File location matters most here (F1). 6.2: the downloaded CSV
  has a long name and lands in Downloads; spell out rename and move into the
  repository folder. 6.5 task 1 depends on a file from 6.4. 6.6: one set of
  instructions.
- **Topic 8.** Replace the PowerShell "Vides sagatavošana" with the standard
  "Pirms sāc" (D1). Give skeletons with gaps for binary search and bubble
  sort. 8.3–8.5 describe the timing pattern in words ("izmēri ar `time.time()`
  pirms un pēc"); show it once as a code block. Separate 8.4 and 8.5 (D7).
- **Topic 10.** Add `unittest` (D5, F3). Replace the PowerShell setup (D1).
  No code in most lessons, so "Gatavs, kad" must point at what is in the file.
  Say where diagrams are drawn (paper + photo, or a named tool) before 10.6
  asks to add them to the repository. Give one filled-in example per document.
  Pick the SR for the testing lesson from `sasnRez.html`.
- **Topic 11.** Stays Streamlit (D4); rewrite the topic page and course page.
  11.1: one `venv` in the repository root, so `venv\Scripts\activate` works in
  the terminal VS Code opens; remove `source venv/bin/activate` and the `pip3`
  note (D8). 11.3 task 3 "nokopē savu skaitļu minētāju no 4.6" must name the
  file and folder. 11.4 needs HTML/CSS this course has not taught: give the CSS
  in full. 11.6 task 2 is five sub-problems in seven lines.
- **Topic 13.** Install and first login are in place (13.1). Still to do: say
  how a `.sql` file is run from SQL Shell, and keep every step on SQL Shell
  rather than mixing in pgAdmin. 13.5: step-by-step connection with the
  password kept out of the file.
- **Topic 14.** 14.3–14.5 extend the class from the previous lesson; each
  needs a "Pirms sāc" with the class to copy. Otherwise close to the standard.
- **Topic 16.** `curl` with single quotes does not work the same in Windows
  PowerShell; give a tested command or a small Python client. 16.4 needs
  HTML/JS given in full. 16.5: `165.py` is never created, the code example
  uses `sslmode="require"` which a local database refuses, and the Render
  click path is missing. Check whether `gunicorn 125:app` should become
  `app_165.py` under D2. 16.6 steps are whole features; split and add
  skeletons.

---

## 8. Progress

Mark a lesson ☑ when prompts A–C are done and the page was checked in a
browser. ◐ means rewritten and waiting for the author's review. Mark "wrap-up"
when Prompt D is done for the topic.

| Topic | .1 | .2 | .3 | .4 | .5 | .6 | wrap-up |
|---|---|---|---|---|---|---|---|
| 1 | ☐ | ☐ | ◐ | ☐ | ☐ | ☐ | ☐ |
| 2 | ☐ | ☐ | ☐ | ☐ | ☐ | ☐ | ☐ |
| 3 | ☐ | ☐ | ☐ | ☐ | ☐ | ☐ | ☐ |
| 4 | ☐ | ☐ | ☐ | ☐ | ☐ | ☐ | ☐ |
| 5 | ☐ | ☐ | ☐ | ☐ | ☐ | ☐ | ☐ |
| 6 | ☐ | ☐ | ☐ | ☐ | ☐ | ☐ | ☐ |
| 7 | ☐ | ☐ | ☐ | ☐ | ☐ | ☐ | ☐ |
| 8 | ☐ | ☐ | ☐ | ◐ | ☐ | ☐ | ☐ |
| 9 | ☐ | ☐ | ☐ | ☐ | ☐ | ☐ | ☐ |
| 10 | ☐ | ☐ | ☐ | ☐ | ☐ | ☐ | ☐ |
| 11 | ☐ | ☐ | ☐ | ☐ | ☐ | ☐ | ☐ |
| 12 | ☐ | ☐ | ☐ | ☐ | ☐ | ☐ | ☐ |

Before the pilot:

- ☑ Decisions D1–D8 (2026-11-16)
- ☑ Blockers in section 2.1 fixed in the working tree (2026-11-16)
- ☑ Follow-ups F1–F4 confirmed (2026-11-16)
- ☐ 1.3 on a school computer: GitHub Desktop menu and button names match the
  lesson, **Open in Visual Studio Code** works with VS Code from Microsoft
  Store, and the default **Local path** is writable for students
- ☐ Install steps run once on a school computer: Microsoft Store Python (1.1),
  PostgreSQL installer and SQL Shell (13.1), `pip install` for Streamlit,
  psycopg2 and Flask (11.3, 13.5, 16.2), `python-dotenv` (16.5)
- ☐ Blocker fixes committed
