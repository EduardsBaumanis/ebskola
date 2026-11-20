# 6. tēma — Datubāzes spēlēm: inventārs un statistika (plāns)

> **Status:** plan only. No lesson pages exist yet. Write the lessons in the
> Programmēšana II format: Teorija, three tasks, "Ko sagatavo" (what goes in
> the GitHub repository and `README.md`, and how to hand in), "Ja kaut kas
> nestrādā".

## Why this topic exists

Programmēšana II saves data only to files (topic 5: `FileAccess`, JSON).
MK Nr. 416 requires two higher-level results this course never reaches:

- **2.3.2:** planning a database with an ER model.
- **2.4.17:** a data-processing system on the student's own database with
  several tables.

Programmēšana I topic 13 used PostgreSQL from Python. This topic moves to a
database embedded in a C# program and to designing the schema properly.

**Place in the course:** right after topic 5 (saving and loading).
The student then compares three ways to store the same game data: JSON file,
Godot `Resource`, and a database. Topic 9 (networking) can reuse this
database for an online leaderboard.

**Prerequisites:** topics 1–5 (C# classes, `List<T>`, `Dictionary`,
interfaces, `SaveManager`). Programmēšana I topic 13 (SQL basics) helps but
is not required: 6.2 and 6.3 teach the SQL that is needed.

## Results covered (MK Nr. 416, 7. pielikums, augstākais līmenis)

| Kods | Sasniedzamais rezultāts | Stundas |
|---|---|---|
| 2.3.2. | Plāno datubāzi, t. sk. izveido ER modeli konkrētā uzdevuma datu apstrādes risinājumam. | 6.1, 6.3, 6.6 |
| 2.4.17. | Izveido vienkāršu datu apstrādes programmatūru (sistēmu), datu uzglabāšanai izmantojot paša veidotu datubāzi ar vairākām tabulām. | 6.2–6.6 |
| 2.4.11. | Meklē un pievieno atvērtā koda bibliotēkas un lieto API (programmsaskarni) specializētu funkciju veikšanai sava programmēšanas projekta īstenošanai. | 6.2 |
| 2.4.16. | Veic izstrādātajā programmatūrā izmantoto algoritmu sarežģītības novērtēšanu pēc laika un izmantotās atmiņas un, ja nepieciešams, veic algoritmu optimizāciju. | 6.5 |

2.3.2 and 2.4.17 are the gaps. The other two are already covered elsewhere,
and this topic gives more practice. Cite them in `.lesson-meta` in the
current format: short label, the law's text in `title`, and a link to
`/sasnRez#prog2-a-…`.

## Tools

- Godot 4 .NET and .NET 8, as in the other topics.
- SQLite through the NuGet package `Microsoft.Data.Sqlite`, added to the
  project's `.csproj` with `dotnet add package`. It is open source (MIT), and
  there is no server to install.
- DB Browser for SQLite (free) to look inside the database file.
- ER diagrams: paper and a photo, or draw.io / diagrams.net.

## Lessons

One new Godot .NET project and GitHub repository for the topic
(`Inventars`), as in the other topics. Database code lives in `Scripts/Data/`. The
database file is created in `user://` and is never committed (`.gitignore`).

### 6.1 Datu modelis: būtības, atribūti un saites

- **File:** `prog2_61.html`
- **Goal:** Izveido ER modeli spēlei ar spēlētājiem, priekšmetiem, inventāru
  un spēļu rezultātiem un pārbaudi, ka tas atbild uz pieciem dotajiem
  jautājumiem.
- **SR:** 2.3.2.
- **Theory:** entity, attribute and primary key. One-to-many and
  many-to-many relationships and the junction table. Why the topic 5 JSON
  save repeats data (redundancy), and what goes wrong when it is updated.
  Normalisation up to "one fact in one place".
- **Task 1:** take the topic 5 save file and list every repeated value.
  Name the entities hidden in it.
- **Task 2:** draw the ER diagram: `Player`, `Item`, `InventoryItem`
  (quantity), `Match`. Mark the keys and the cardinality.
- **Task 3:** check the model against five questions ("Kuri spēlētāji
  glabā zobenu?", "Labākie 5 rezultāti šonedēļ?" …). Add whatever is
  missing, and write down which questions the model cannot answer and why.
- **Ko sagatavo:** `docs/er_71.png` and the table descriptions in the
  README.

### 6.2 SQLite C# projektā

- **File:** `prog2_62.html`
- **Goal:** Pievieno SQLite bibliotēku Godot projektam, izveido pirmo tabulu
  un ieraksti un nolasi spēlētājus ar parametrizētiem vaicājumiem.
- **SR:** 2.4.17., 2.4.11.
- **Theory:** an embedded database vs a database server. Adding a NuGet
  package and what changes in the `.csproj`. `SqliteConnection`,
  `SqliteCommand` and `ExecuteNonQuery` / `ExecuteReader`. Parameters
  (`$name`) and why string concatenation is an SQL injection.
- **Task 1:** `dotnet add package Microsoft.Data.Sqlite`, build, and open
  the connection to `user://game.db` (`ProjectSettings.GlobalizePath`).
- **Task 2:** `Scripts/Data/Database.cs` creates the `Player` table if it
  does not exist and has `AddPlayer(name)` and `GetPlayers()`.
- **Task 3:** insert a name with an apostrophe (`O'Brien`) and a duplicate
  name. Make the first work with parameters and the second fail with a
  clear message (`UNIQUE`).
- **Ja kaut kas nestrādā:** `DllNotFoundException e_sqlite3` (the package
  version, a clean rebuild), a locked database file (missing `using`).

### 6.3 Vairākas tabulas, ārējās atslēgas un JOIN

- **File:** `prog2_63.html`
- **Goal:** Izveido visas ER modeļa tabulas ar ārējām atslēgām un uzraksti
  vaicājumu, kas parāda spēlētāja inventāru ar priekšmetu nosaukumiem.
- **SR:** 2.4.17., 2.3.2.
- **Theory:** `FOREIGN KEY` and `PRAGMA foreign_keys = ON` (off by default
  in SQLite). `INNER JOIN` vs `LEFT JOIN`. `ON DELETE CASCADE` vs
  `RESTRICT`. A schema version table for later changes.
- **Task 1:** a `schema_73.sql` resource with all four tables. `Database.cs`
  runs it once and stores the schema version.
- **Task 2:** `GetInventory(playerId)` with a `JOIN`, returning
  `List<InventoryRow>`. Print it in Output.
- **Task 3:** try to add an item to a player who does not exist, and to
  delete an item that someone holds. Check that the foreign keys stop both,
  and choose `CASCADE` or `RESTRICT` with a reason.

### 6.4 Datu piekļuves slānis un transakcijas

- **File:** `prog2_64.html`
- **Goal:** Nošķir datubāzes kodu no spēles koda ar repozitorija klasēm un
  nodrošini, ka priekšmeta maiņa starp spēlētājiem notiek pilnībā vai nemaz.
- **SR:** 2.4.17.
- **Theory:** the repository pattern (`IPlayerRepository`), linked to the
  topic 5 `ISaveable` interface. Transactions: `BeginTransaction`, `Commit`,
  `Rollback`. Mapping rows to C# records.
- **Task 1:** `PlayerRepository` and `ItemRepository` behind interfaces.
  The game scene uses only the interfaces.
- **Task 2:** `TradeItem(from, to, itemId)` in one transaction (remove,
  add, log in a `Trade` table).
- **Task 3:** throw an exception between the two steps on purpose. Check
  that nothing changed in the database, then remove the exception.

### 6.5 Ātrdarbība: indeksi un mērījumi

- **File:** `prog2_65.html`
- **Goal:** Ieraksti 100 000 rezultātu, izmēri vaicājuma laiku pirms un pēc
  indeksa un salīdzini datubāzes un JSON faila izmēru un ātrumu.
- **SR:** 2.4.16., 2.4.17.
- **Theory:** why a search without an index is O(n) and with an index
  O(log n), linked to binary search in topic 5. `EXPLAIN QUERY PLAN`.
  Writing many rows inside one transaction. The memory cost of an index.
- **Task 1:** generate 100 000 `Match` rows (with and without one
  transaction) and time both with `Stopwatch`.
- **Task 2:** time "top 10 for one player" before and after `CREATE INDEX`,
  and read `EXPLAIN QUERY PLAN`.
- **Task 3:** fill a table in the README: file size and query time for the
  database vs the same data as JSON loaded into a `List`. When is JSON
  still the better choice?

### 6.6 Noslēguma projekts: Spēles inventāra un statistikas sistēma

- **File:** `prog2_66.html`
- **Goal:** Izveido Godot lietotni ar paša projektētu datubāzi: spēlētāju
  profili, inventārs, mači un statistikas ekrāns, kas viss nolasīts ar
  vaicājumiem.
- **SR:** 2.3.2., 2.4.17.
- **Step 1:** extend the ER model with one entity of your own choice (for
  example `Achievement`, or quests). Update the diagram and the schema
  version.
- **Step 2:** a simple Control-node UI from given scenes (topic 8 teaches
  UI in depth later): choose a player, see and change their inventory, and record a
  match.
- **Step 3:** a statistics screen with three queries (`GROUP BY`, `JOIN`,
  and a date filter). The README lists each query and the question it
  answers.
- **Assessment (SLA):** the ER model matches the schema; there are at least
  four tables with working foreign keys; all queries use parameters; the
  trade uses a transaction; and the database file is not in Git.

## Open questions for the author

1. **SQLite in exported builds.** `Microsoft.Data.Sqlite` brings a native
   `e_sqlite3` library. Check that a Windows export from Godot 4.7 .NET
   includes it before 6.2 is written. If not, keep this topic to the editor
   and note it.
2. **Overlap with Programmēšana I topic 13.** Students who took Prog I have
   seen SQL. Should 6.2–6.3 offer a short path for them?
