# Review · 6 · Godot / C# Expert

> Improvement plan for the Godot 4 .NET / C# content in Programmēšana II
> (6 topics: Pong, Platformer, RPG, Top-down Shooter, Roguelike, Puzzle).

Severity: `Critical | Major | Minor | Nit`.

## What I reviewed

- Repo layout: `programmesana2/prog2_1/{kods/1_3,1_4, parbaudes, pong, pong.zip}`,
  `prog2_2/{kods/2_1..2_3, parbaudes, platformer, platformer.zip}`.
- `programmesana2/prog2_1/parbaudes/check.py` and `prog2_2/parbaudes/check.py`.
- `README.md` verification instructions (`--godot`, `--dotnet` flags).

## Findings

- **Nit · repo hygiene** — `.godot/` build/cache directories exist on disk under
  `prog2_1/pong` and `prog2_2/platformer`, but each project's `.gitignore`
  (`.godot/`, `bin/`, `obj/`, `*.tmp`) already ignores them; nothing is committed.
  No action needed.
- **Positive** — `check.py` scripts and full sample projects (`pong`, `platformer`)
  exist, and `pong.zip` / `platformer.zip` are present, matching the README.
- **Verification item** — confirm `check.py`'s actual CLI matches the README's
  `--godot <path> --dotnet <path>` form, and that `SmokeTest.cs` asserts the exact
  outcomes each lesson claims.

## Improvement plan

1. (Resolved) `.godot/` is already ignored per-project; no cleanup required.
2. Audit each topic's milestone lessons (x.1–x.6) against the `kods/` intermediate
   scripts and the full project: do node paths, exported properties and signal
   connections in the text match the actual C# files?
3. Verify `SmokeTest.cs` + `check.py` genuinely exercise the lesson's stated
   outcomes; document what each check does and does not cover.
4. Confirm the six project stages produce the promised behavior (e.g., Pong
   paddle/ball, Platformer movement, RPG turn logic).
5. Check version specificity: Godot 4 .NET minor version and .NET SDK assumptions
   should be stated consistently in README and lessons.

## Open questions

- Which exact Godot 4.x and .NET SDK versions are the tests validated against?
