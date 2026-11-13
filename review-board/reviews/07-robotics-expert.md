# Review · 7 · Robotics & Electronics Expert

> Improvement plan for the LEGO SPIKE Prime and Arduino (C++) content in
> Robotika (2 topics, 10 lessons, grades 7–9).

Severity: `Critical | Major | Minor | Nit`.

## What I reviewed

- `robotika/rbtk7_11.html` (LEGO SPIKE topic, first lesson) in detail.
- Course scope from `README.md`: LEGO SPIKE Prime movement/sensors/manipulators
  (5 lessons) + Arduino introduction (5 lessons).

## Findings

- **Positive** — `rbtk7_11.html` is physically correct and well-calibrated: it
  fixes port A = left motor, B = right; explains the pink "Movement" vs blue
  "Motor" block distinction; and honestly teaches that motor degrees ≠ robot turn
  angle (suggesting 175–190° tuning). This is the right way to teach SPIKE.
- **Verification item** — port/block naming must stay identical across all five
  SPIKE lessons. A single "set movement motors to A and B" in one lesson and
  "A and C" in another would break every build. Audit all five.
- **Priority audit** — the Arduino topic (lessons 21–25) is where wiring vs code
  mismatches are most likely: verify each sketch's pin numbers match the wiring
  text and that the C++ compiles.

## Improvement plan

1. Build a course-wide block/port glossary (e.g., `set movement motors to [A] and
   [B]`, `move [forward] for [20] [cm]`, `repeat [4] times`) and check all five
   SPIKE lessons against it.
2. Audit Arduino lessons for pin/wiring/code agreement and compile-ability.
3. Consider shipping Arduino sketches as `.ino` files (mirroring Datorika 9's
   `sakuma-kodi/`) so students can download instead of retyping.
4. Verify "done-when" tolerances are physically achievable (e.g., ≤3 cm from the
   start line, square sides within 10 cm).

## Open questions

- Should Arduino starter sketches be added as downloadable `.ino` files?
