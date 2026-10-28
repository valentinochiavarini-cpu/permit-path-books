# Upgrade notes: Chapters 4 to 8 (tag ch4to8)

Done 2026-10-28 under `briefs/UPGRADE_BRIEF.md`. Not committed.

## Words (before the quiz; core preview / state edition with generic text dropped)

| Ch | Before | After (core) | After (state edition) |
|---|---|---|---|
| 4 | 1,683 | 1,764 | 1,732 |
| 5 | 1,809 | 2,106 | 2,071 |
| 6 | 1,841 | 2,056 | 2,056 |
| 7 | 1,899 | 2,061 | 2,043 |
| 8 | 1,877 | 1,835 | 1,768 |

## Topics added, with national sources

### Chapter 4
- 4.2 "Judging a Gap": about 6 s to cross, 8 s to turn right, 9 s to turn left where traffic moves about 30 mph; more for faster traffic, wet roads, slow cars. General guidance. Sources: PennDOT PUB 95 Chapter 3 (6/8/9 s, per the QA coverage audit); Montana OPI Driver Education "Gaps" fact sheet (6 to 7 s crossing, 7 to 9 s right, 9 s left).
- 4.6 emergency vehicles rewritten: pull to the right edge and stop, never stop in an intersection (drive through first), slow and be ready if you cannot locate the siren, do not follow. `{{INSERT:emergency_vehicles}}` placed after the national rule (one way streets and following distance go in the insert: CA 300 ft, FL and PA 500 ft for fire apparatus). Source: Uniform Vehicle Code 11-405 (right-hand edge, clear of any intersection) and 11-1107 (following fire apparatus); CA and NY manuals.
- 4.7 school bus intro reworded (yellow lights while getting ready to stop, red once stopped). Removed "or in some states the bus driver" and replaced with "unless a police officer or, where the box below allows it, the bus driver signals you to go": NY, TX and IL inserts allow the bus driver's signal, PA's says a wave is not enough, so the core now defers to the box and contradicts none of them.

### Chapter 5
- 5.2 off-tracking: rear wheels follow a shorter path inside the front wheels; trucks off-track far more. Sources: state CDL manuals (off-tracking), CA Driver Handbook.
- 5.8 renamed "Talking to Other Drivers": signal well before every turn/lane change/pull out and cancel after; tap the brake pedal a few times before an unexpected slowdown (PUB 95 Ch 3); hazard flashers when stopped on or beside the road or disabled and creeping to a safe place; horn: light tap to warn, long blast only in danger, never in anger, not near cyclists, horses or blind pedestrians (PUB 95 Ch 3, CA handbook); eye contact. Hand signals kept as a subsection.
- Hazard flasher wording is deliberately "stopped or disabled", not "moving slowly": Florida restricts flashers while moving (s. 316.2397), PA allows them below 40 mph on limited access roads. The moving case is left to state material.

### Chapter 6
- Look-ahead fixed to 12 to 15 seconds (6.7, Quick Review, C06-022). Source: PennDOT PUB 95 Managing Space.
- 6.1 "Curves": run-off-road crashes, often on curves, are among the most common for new teen drivers (PUB 95 Ch 3; NHTSA teen data); slow before the curve, center of the lane, look through it.
- 6.1 "Steep Downgrades": lower gear, do not ride the brakes (fade), brake firmly then ease off. Source: CA Driver Handbook, NY Driver's Manual Ch 8.
- 6.5 more space: driver behind wants to pass; stopped behind a car on an upgrade (it may roll back). Motorcycles and large trucks were already listed. Source: PUB 95 Managing Space.

### Chapter 7
- 7.3 passing in numbers: about 10 mph faster than the other car, 10 to 20 seconds, about a quarter mile of clear road at 45 mph; finish quickly. Sources: PennDOT online manual Ch 3 (10 mph faster, quarter mile at 45 mph); Montana OPI "Estimate Passing Gap" fact sheet (13 to 19 s at 40 to 60 mph). Return rule (both headlights in the inside mirror) was already taught.
- 7.3 no passing within 100 feet of an intersection, railroad crossing, bridge, viaduct or tunnel; replaced "Many states set a fixed distance, often 100 feet". Source: UVC 11-306; PennDOT manual Ch 3; NY manual Ch 6. Note: UVC and some states (NY, CA) limit the bridge/tunnel ban to an obstructed view, and NY's page lists railroad crossings but not intersections; the core states the stricter, safe version, which no state insert contradicts.
- 7.6 never use the acceleration lane to pass (PennDOT manual Ch 3).
- 7.7 "Weave Lanes": one lane for entering and exiting traffic; entering drivers yield to traffic already on the freeway, including drivers moving over to exit; both take turns. Consistent with the 7.6 merge rule. Sources: CA handbook, PUB 95.
- 7.7 "Truck Escape Ramps": yellow RUNAWAY TRUCK RAMP sign (MUTCD 11th ed., Chapter 2C, W7-4 series); never stop or park in it or at its entrance.

### Chapter 8
- 8.6 no backing in a travel lane except to parallel park; drive on and turn around. Source: UVC 11-1102 (backing only when safe and without interfering with traffic; never on a controlled-access highway); CA handbook.
- Restructured: old 8.5 "Curb Colors" + 8.6 "Where You May Not Park" became 8.5 "Where You May Not Park" with the list first, then `{{INSERT:parking_rules}}` ("The box below gives the exact distances."), then disability parking and No Parking / No Standing / No Stopping. The curb color table is now a one-paragraph `[[generic]]` block (CA's insert carries California's colors). Backing became 8.6, pulling away 8.7. No other file referenced these section numbers.

## Hedges (patterns: most/many/some states, your state may/sets/lets/requires, states differ/vary, every state)

| Ch | Before | Deleted | Wrapped `[[generic]]` | Rewritten as national rule / pointer to box | Left in state edition |
|---|---|---|---|---|---|
| 4 | 14 | 4 (one way edge, opposite direction, States differ, Many states extend) | 2 (transit bus yield, funeral procession) | 8 (Move Over, white cane, school bus x4, opening, Every state) | 0 |
| 5 | 4 | 2 (States add, "the distance most states use") | 1 (bike lane broken line) | 1 (hand signals) | 0 |
| 6 | 6 | 1 ("most state manuals" in Test trap) | 0 | 5 (basic speed law, statutory limits, points, too slow, count in the box x2) | 0 |
| 7 | 5 | 1 (100 ft "many states") | 1 (left lane ticket) | 3 (keep right, being passed is illegal, signal distance) plus "in many places motorcycles" made national (23 USC 166) | 0 |
| 8 | 7 | 3 (alley full stop, "differ by state", "almost every state") | 2 (curb distance 12 or 18 in, curb color block) | 2 (hydrant and crosswalk distances moved to the box) | 0 |

## Quiz changes (bank/core.json; first 7 print in a state edition)

- Ch 4 quiz order: C04-016, 022, 001, 003, 019, 006, 009 | 017, 021, 012. C04-027 (funeral) left the quiz, C04-017 (in an intersection when a siren comes) joined. Joke or weak distractors replaced in 001, 003, 009, 016, 019, 021, 022, 027. Rewritten non-quiz: 020 (now which situation Move Over covers), 023, 028, 029 (now: do not follow an ambulance; the old "nearest edge where your state allows it" answer is gone). New: C04-031 to 034 (gap size, bigger gap, siren you cannot locate, never stop in an intersection).
- Ch 5 quiz order: C05-001, 027, 026, 016, 017, 006, 005 | 031, 019, 023. C05-003 left the quiz; new C05-031 (brake tap) joined. C05-026 reworded to "closest you may stop" (5/10/25/15 ft) so only 15 is defensible. Distractors fixed in 001, 005, 006, 016, 017, 019, 023. New: C05-031 to 036 (brake tap, horn tap, horn blast, hazard flashers, eye contact, off-tracking).
- Ch 6 quiz order: C06-001, 007, 011, 022, 016, 031, 013 | 026, 005, 002. C06-019 left the quiz; new C06-031 (slow before the curve) joined. C06-011 now offers "one car length per 10 mph"; C06-022 now 12 to 15 s with near-miss options. New: C06-031 to 037 (curve speed, downgrade gear, brake fade, run-off-road, upgrade stop, driver wants to pass, curve lane position).
- Ch 7 quiz order: C07-007, 031, 008, 015, 018, 013, 023 | 003, 029, 022. Left the quiz: C07-001, C07-026 (HOV diamond, still in the bank as a normal question). Joined: C07-031 (100 ft), C07-008 (both headlights). New: C07-031 to 036 (100 ft, quarter mile, acceleration lane, weave lane, escape ramp, why passing needs a long stretch).
- Ch 8 quiz order: C08-002, 001, 003, 011, 015, 028, 023 | 031, 017, 021. C08-006 (red curb) left the quiz; new C08-031 (missed driveway, do not back in the lane) joined. New: C08-031, 032.
- Answer letters per chapter (all / quiz): Ch4 A9 B10 C8 D7 / A2 B2 C3 D3; Ch5 A10 B9 C9 D8 / A3 B3 C1 D3; Ch6 A10 B9 C9 D9; Ch7 A9 B9 C10 D8; Ch8 A8 B8 C8 D8. Totals: Ch4 34, Ch5 36, Ch6 37, Ch7 36, Ch8 32.

## app_only (quiz false)
C06-027 (blind spot warning lights), C07-027 (HOV 2+), C07-028 (entering a barrier-separated HOV lane), C08-006 to C08-010 (curb colors; taught only in the generic block), C08-026 (backup camera).

## Open issue for the run leader
State mocks already list core IDs that are now app_only: C06-027 (CA, IL, NY, PA), C08-026 (CA, NY, PA), C08-009 (CA), C08-008 (NY, TX), C07-028 (NY), C07-027 (PA). `tools/make_mocks.py` filters app_only only from the state bank, not from core (line 17). Suggested fix: add `and not r.get("app_only")` to the core filter, then regenerate those mocks. No state mock uses any ID that is now flagged quiz.

## Checks
- `python3 tools/originality_check.py check core/ch04.md` to `ch08.md`: all PASSED (0.00 to 0.26 percent shared, no 12-word runs).
- `python3 tools/check_bank.py bank/core.json`: BANK PASSED.
- `python3 layout/build_book.py --core-only`: QA PASSED (170 pages). A first run failed on "6 chapter practice cards", a race with another agent's concurrent build; the rerun passed.
- No em or en dashes, no years, no state names in Ch 4 to 8.
- bank/core.json kept in its existing indent-1 format (the brief says indent 2, but the file in git uses indent 1).
