# 10. tēma — Komandas projekts: no pasūtījuma līdz laidienam (plāns)

> **Status:** plan only. No lesson pages exist yet. Write the lessons in the
> Programmēšana II format: Teorija, three tasks, "Ko sagatavo" (what goes in
> the GitHub repository and `README.md`, and how to hand in), "Ja kaut kas
> nestrādā".

## Why this topic exists

Every Programmēšana II project is built alone, from a brief the course
gives. At the higher level, MK Nr. 416 requires the whole software process
in a group. Five of its results are not covered at all:

- **2.4.1:** formulating a work task as a client.
- **2.4.2:** comparing development models and choosing one.
- **2.4.3:** developing in a group by the chosen model's stages.
- **2.4.4:** a requirements specification.
- **2.4.8:** a code style agreed by the whole group.

Others are only touched lightly:

- **2.4.5:** design, including the task split in the group.
- **2.4.6:** unit, integration and acceptance testing.
- **2.4.7:** deployment and maintenance plans.
- **2.4.9:** project tools for collaboration.
- **3.1.4:** comparing and choosing licences.

This topic is a team project that covers all of them. Two teams act as each
other's clients.

**Place in the course:** the last topic. It needs everything
before it, and it ends the course with one larger product built together.

**Prerequisites:** topics 1–9. Topics 6, 7 and 9 let the teams choose to
build with a database, ML or networking.

## Results covered (MK Nr. 416, 7. pielikums, augstākais līmenis)

| Kods | Sasniedzamais rezultāts | Stundas |
|---|---|---|
| 2.4.1. | Analizē dažādus ikdienas darba procesus, saskata tajos vai to daļās automatizācijas iespējas un kā pasūtītājs formulē darba uzdevumu programmatūras izstrādātājam. | 10.1 |
| 2.4.2. | Salīdzina un izvēlas piemērotāko programmatūras izstrādes modeli konkrētā uzdevuma atrisināšanai, pamato izvēli. | 10.1, 10.2 |
| 2.4.4. | Sastāda vienkāršotu programmatūras prasību specifikāciju atbilstoši konkrētajam uzdevumam, izvērtējot mērķauditorijas specifiku un vajadzības. | 10.2 |
| 2.4.5. | Veic vienkāršotu programmatūras projektēšanu (t. sk. lietotāju saskarnes un vienkāršotu datu modeļa izveidi) atbilstoši programmatūras prasību specifikācijā izvirzītajām funkcionālajām un nefunkcionālajām prasībām. Veic vienkāršotu programmatūras izstrādes plānošanu (bez darbietilpības novērtējuma) un darba pienākumu sadali grupā. | 10.2 |
| 2.4.9. | Lieto projektu un versiju pārvaldības rīkus sadarbībai ar citiem programmatūras izstrādes procesā un tā vadībā. | 10.3 |
| 2.4.3. | Izstrādā programmatūru grupā, ievērojot izvēlētā programmatūras izstrādes modeļa posmus, veic katra posma vienkāršotu dokumentēšanu. | 10.3–10.6 |
| 2.4.8. | Veido programmu, ievērojot labās prakses pieredzi tās pieraksta strukturēšanā un komentāru veidošanā, vienojoties par vienotu stilu ar visiem grupas dalībniekiem. | 10.4 |
| 2.4.6. | Veic programmatūras vienību izstrādi un vienībtestēšanu, izstrādājamās programmatūras vienību apvienošanu, integrācijas un akcepttestēšanu atbilstoši izstrādātajai programmatūras prasību specifikācijai un projektējuma aprakstam. | 10.5, 10.6 |
| 2.4.7. | Izstrādā un prezentē izveidotās programmatūras vienkāršotu izvēršanas (t. sk. ieviešanas) plānu, lietotāja ceļvedi un uzturēšanas plānu, ievērojot tās lietotāju mērķauditorijas specifiku. | 10.6 |
| 3.1.4. | Salīdzina atvērto kodu licences un to atšķirības, izmanto un piemēro atbilstošāko no licencēm savam programmatūras projektam. | 10.6 |

Cite them in `.lesson-meta` in the current format, linking to
`/sasnRez#prog2-a-…`.

## Tools

- GitHub: an organisation or a shared repository per team, branches, pull
  requests with required review, Issues, Projects (board), milestones and
  releases. GitHub Desktop or git commands, whichever the students used in
  the earlier topics.
- `.editorconfig` and `dotnet format` for the shared C# style. Build
  warnings from the .NET analysers.
- xUnit in a separate test project (`dotnet new xunit`) for game logic that
  does not depend on Godot nodes. The topic 8 puzzle already separates its
  data model from the UI (8.6), which is the pattern to follow.
- Optional: GitHub Actions to run `dotnet test` and `dotnet format
  --verify-no-changes` on every pull request.

## Lessons

Teams of 3–4. Each team is a **developer** team for one brief and the
**client** for another team's brief. All work goes in the team repository
`komanda-N`. Documents go in `docs/`, one file per stage.

### 10.1 Pasūtījums un izstrādes modeļa izvēle

- **File:** `prog2_101.html`
- **Goal:** Kā pasūtītājs uzraksti darba uzdevumu citai komandai par reālu
  skolas procesu, ko var automatizēt vai padarīt par spēli, un kā izstrādātājs
  izvēlies izstrādes modeli savam pasūtījumam.
- **SR:** 2.4.1., 2.4.2.
- **Theory:** how a good brief is written: the problem, who uses it, what
  "done" means, limits (time, platforms). Waterfall, V-model, incremental and
  iterative/Scrum compared, with the criteria from Programmēšana I topic 9
  (requirements stability, risk, client availability).
- **Task 1:** observe one school process (a cloakroom queue, a library
  return, learning vocabulary) and list the steps that software or a game
  could help with.
- **Task 2:** write `docs/pasutijums.md` for the other team: the
  problem, users, three must-haves, two nice-to-haves, deadline, and how
  you will accept the work.
- **Task 3:** as developers, read the brief you received and ask the
  client three clarifying questions (in a GitHub Issue). Choose a
  development model and justify it in `docs/modelis.md`.

### 10.2 Prasību specifikācija un projektējums

- **File:** `prog2_102.html`
- **Goal:** Sastādi prasību specifikāciju, kuru pasūtītājs apstiprina, un
  projektējumu ar saskarnes skicēm, datu modeli, darba plānu un pienākumu
  sadali.
- **SR:** 2.4.4., 2.4.5., 2.4.2.
- **Theory:** functional and non-functional requirements (performance,
  platforms, accessibility). User stories with acceptance criteria. From
  requirements to design: screen flow, a class diagram or data model, and
  modules that can be developed separately. Splitting work by module, not
  by person's favourite task.
- **Task 1:** `docs/prasibas.md` with at least six user stories and three
  non-functional requirements, each with acceptance criteria.
- **Task 2:** `docs/projektejums.md` with screen sketches (photo or
  wireframe), the class or data model, the module list, and who owns which
  module.
- **Task 3:** the client team reviews the specification in a pull request,
  with at least two change requests. Update the documents and get the
  client's approval in the PR.

### 10.3 Sadarbība ar Git: zari, pull request un dēlis

- **File:** `prog2_103.html`
- **Goal:** Iestati komandas krātuvi tā, ka neviens neraksta tieši `main`,
  katra izmaiņa iet caur pull request ar pārskatu un viss darbs ir redzams
  projekta dēlī.
- **SR:** 2.4.9., 2.4.3.
- **Theory:** feature branches, pull requests and code review. Branch
  protection on `main`. Merge conflicts and how to resolve them. Issues
  linked to PRs ("Closes #12"). Board columns and milestones per iteration.
- **Task 1:** one person creates the repository, protects `main` (one
  review required) and adds the team. Everyone clones it.
- **Task 2:** turn every user story into an Issue on a Projects board.
  Each member opens a branch and a PR for their first small task.
- **Task 3:** two members change the same line on purpose. Resolve the
  conflict in the PR, and record in `docs/procesi.md` how the team will
  avoid it.

### 10.4 Vienots koda stils

- **File:** `prog2_104.html`
- **Goal:** Vienojieties par komandas C# koda stilu, ielieciet to
  `.editorconfig` failā un pārbaudiet, ka rīks automātiski atrod un labo
  novirzes.
- **SR:** 2.4.8.
- **Theory:** why a shared style matters more than which style. C# naming
  conventions (PascalCase, `_camelCase` fields), file layout, and XML doc
  comments (`///`) for public methods. Comments that say *why*, not *what*.
  `.editorconfig` rules and severities, and `dotnet format`.
- **Task 1:** each member brings one of their own scripts from earlier topics. Find
  the five biggest style differences and vote on each.
- **Task 2:** write `.editorconfig` with those rules plus the .NET defaults.
  Run `dotnet format` and commit the result in one separate PR.
- **Task 3:** break three rules in a branch. Check that the build warns and
  that `dotnet format --verify-no-changes` fails. Add the check to the PR
  checklist, or to GitHub Actions.

### 10.5 Vienībtesti, integrācija un akcepttests

- **File:** `prog2_105.html`
- **Goal:** Uzraksti vienībtestus sava moduļa loģikai, apvieno moduļus
  integrācijas pārbaudē un vadi akcepttestu, kurā pasūtītājs pārbauda
  prasības.
- **SR:** 2.4.6., 2.4.3.
- **Theory:** a unit test, an integration test and an acceptance test, and
  who writes each one. Keeping logic in plain C# classes so it can be
  tested without Godot. xUnit: `[Fact]`, `[Theory]` and `Assert`. Turning
  acceptance criteria into a test protocol.
- **Task 1:** `dotnet new xunit` in `Tests/` and reference the logic
  project. Write five tests for your module, including one edge case.
- **Task 2:** merge all modules and run an integration checklist (every
  screen, every data path). Log the failures as Issues.
- **Task 3:** the client team runs the acceptance test from
  `docs/prasibas.md`, and records pass or fail per criterion in
  `docs/akcepttests.md`. Fix at least the failed must-haves.

### 10.6 Noslēguma projekts: Laidiens, ceļvedis un prezentācija

- **File:** `prog2_106.html`
- **Goal:** Izlaidiet pasūtīto programmatūru kā GitHub laidienu ar licenci,
  lietotāja ceļvedi, izvēršanas un uzturēšanas plānu un prezentējiet to
  pasūtītājam.
- **SR:** 2.4.7., 3.1.4., 2.4.3., 2.4.6.
- **Step 1:** compare MIT, GPL-3.0 and Apache-2.0 (and CC licences for the
  art). Choose one for the project, with the client's wishes in mind, and
  add `LICENSE` plus third-party credits.
- **Step 2:** an export (topic 8) attached to a GitHub release `v1.0`, with
  `docs/celvedis.md` (user guide), `docs/izversana.md` (how it is installed
  or put into use at school) and `docs/uzturesana.md` (who fixes bugs, how
  bugs are reported, and what goes into v1.1).
- **Step 3:** a ten-minute presentation to the client team: the brief, the
  model and why, a demo, the test results, and what the team would do
  differently. Each member reviews their own part of the process in the
  README.
- **Assessment (SLA):** every stage has its document; the commit and PR
  history shows work by every member; the style check passes; the
  acceptance test is recorded; and the licence choice is justified.

## Open questions for the author

1. **Team size and grading.** How much of the grade is individual? The PR
   and review history gives evidence per person. Should it count?
2. **GitHub organisation.** One school organisation with a repository per
   team makes branch protection and grading easier. Does the school have
   one?
3. **Briefs.** Should the class invent the briefs (10.1 as written), or
   should the teacher keep a list of real requests from school staff as a
   fallback?
