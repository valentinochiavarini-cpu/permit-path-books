# Core upgrade, Chapters 2 and 3 (tag signs, 2026-10-28)

Brief: `briefs/UPGRADE_BRIEF.md`, figures per `briefs/FIGURES_BRIEF.md` (details in `figures_signs2.md`, third pass). Sources: QA reports `coverage_PA.md` and `review_PA.md`. Not committed by this agent.

## Words (wc, before the quiz marker included)
| Chapter | Before | After | Change |
|---|---|---|---|
| Ch 2 Road Signs | 2,461 | 3,376 | +915 (owner asked for about 900 on signs) |
| Ch 3 Signals and Markings | 2,117 | 2,137 | +20 (wrapped generic text still counted) |

Ch 2 cut: the three-digit Interstate sentence, the "most states" exit sentence (rewritten), the two-sentence 50-state opening (rewritten). Most added words are three tables (28 signs, name, shape and color, meaning).

## Added, with national sources
### Chapter 2
- 2.4 "Crossings, Plaques and Exit Lanes": Divided Highway Crossing R6-3 (2B.50) with the crossing rule (first roadway traffic from your left, right turn there; left turn onto the second roadway; Uniform Vehicle Code 11-311, divided highways), EXIT ONLY panel (2E, E11-1), LEFT TURN YIELD ON green ball R10-12 (2B.59), EXCEPT RIGHT TURN R1-10P (2B.04), TO ONCOMING TRAFFIC R1-2aP (2B.18), two way left turn only R3-9b (2B.32).
- 2.4 Stop: creep forward slowly after the stop if the view is still blocked (UVC 11-403 and state manuals; PUB 95 review Q54).
- 2.5 "Road Shape and Intersections": turn vs curve sign (Chapter 2C: turn sign where the advisory speed is 30 mph or less), Large Arrow W1-6 (2C.10), Two-Direction Large Arrow W1-7 (2C.43), Reverse Curve W1-4, Reverse Turn W1-3, Side Road W2-2 and Y W2-5 (2C.41), Circular Intersection W2-6, Truck Rollover W1-13 (2C.11).
- 2.5 "Narrow Roads, Shoulders and Dead Ends": Road Narrows W5-1 (2C.17), Narrow Bridge W5-2 (2C.18), One Lane Bridge W5-3 (2C.19), Low Shoulder W8-9 (3 in or less, 2C.29), Shoulder Drop-Off W8-17 with W8-17P (more than 3 in), Horse-Drawn Vehicle W11-14 (2C.54), DEAD END W14-1, NO OUTLET W14-2; pointer to Ch 10 for recovering from a drop-off.
- 2.7 work zone rules (bullets, before the work_zone insert): yield to workers, flaggers and work vehicles; stay in your lane where a solid white line separates lanes (MUTCD Chapter 3A meaning of solid lane lines); do not pass a moving work operation unless a flagger or sign directs you (Part 6 mobile operations); fines are often doubled (state detail stays in the insert).
- 2.7 "Warning signs ahead of the work": Flagger W20-7, Workers W21-1, RIGHT LANE CLOSED AHEAD W20-5, DETOUR W20-2 / M4-9, END ROAD WORK G20-2 (Part 6).
- Not added: SHARE THE ROAD plaque, because the 11th edition no longer has it (W16-1P is now IN ROAD). `core/ch09.md` line 120 still teaches it: run leader should decide.

### Chapter 3
- 3.2 Steady green: LEFT TURN YIELD ON (green ball) sign as the reminder for unprotected left turns (2B.59, R10-12). Coverage report item "LEFT TURN YIELD ON GREEN" now taught in Ch 2 (sign) and Ch 3 (rule).
- 3.4 Test trap: oncoming drivers have a green at the same time as the flashing yellow arrow.
- 3.4 red arrow: the table row now says "Stop for that turn" and the text sends the reader to the state box, because PA, FL and IL allow turns on a steady red arrow after a stop while CA, NY and TX do not. The old row "Do not make that turn" and the old figure label contradicted the PA box. Figure label fixed (`ch03_arrow_signals.svg`).
- Signal content checked against the coverage report section 1B: all items covered except the white one-way left-turn lane control arrow (minor, not added).

## Hedges (unwrapped sentences a state edition still prints)
| Chapter | Before | After | What was done |
|---|---|---|---|
| Ch 2 | 4 | 1 | Opening "Almost every state tests signs ... Every state follows ..." rewritten as national facts; "In most states, exit numbers match" rewritten "On most freeways"; kept: school figure caption "(your state sets the number)", which points at the state box. |
| Ch 3 | 6 | 0 | "In most places you may turn right on red" rewritten as the national rule; "Most states also permit a left turn on red ... Some cities and states ... a few cities ban it" wrapped `[[generic]]` (the turn_on_red insert gives the state rule); "States differ on ... red arrow ... unless your state box" rewritten to point at the {{STATE}} rule box; "(some states only)" dropped from the flashing yellow X row (a national MUTCD lane-use indication); "Some states also allow a left turn across it for a U-turn ... and some let you cross it to pass a bicycle" wrapped `[[generic]]`. |

## Quiz changes (bank/core.json)
### Chapter 2 (70 questions, was 30; letters A 18, B 18, C 17, D 17)
New quiz order: C02-001, C02-002, C02-031 (picture, large arrow), C02-015, C02-032 (picture, divided highway crossing), C02-006, C02-004 (now with picture) | expendable last 3: C02-033 (picture, EXIT ONLY), C02-024, C02-026. Four quiz questions carry a picture (the maximum).
- Left the quiz: C02-010 (regulatory definition), C02-013 (Wrong Way, now a picture question), C02-020 (WHEN FLASHING school limit; the school_zone state questions cover the zone).
- Weak distractors replaced: C02-001 D, C02-002 B, C02-024 B, C02-026 A.
- New C02-031 to C02-070: 34 picture questions (stems describe the sign in words: shape, color, symbol or legend) and 6 text questions (divided highway left turn, solid white line in a work zone, moving work operation, creep forward at a blocked stop, yield to workers, drop-off size).
- Pictures added to C02-004, C02-005, C02-013, C02-018, C02-029 (stems of C02-005 and C02-029 now describe the sign). 39 Ch 2 questions use an `sq_` image in total.
### Chapter 3 (32 questions, was 30; letters 8 each)
New quiz order: C03-004, C03-002, C03-001, C03-009, C03-021, C03-027, C03-016 | expendable last 3: C03-025, C03-019, C03-007 (right on red last, because the state turn_on_red questions cover it).
- Throwaway distractors replaced: C03-001 A, B, C ("stop in the middle of the intersection" gone), C03-002 B, C03-004 D, C03-009 B, C (no "honk and drive through"), C03-016 B (no "honk to tell the person to hurry"), C03-021 B, C03-025 A.
- New: C03-031 LEFT TURN YIELD ON green ball, C03-032 flashing yellow X center lane.

## app_only
- C02-028 (even Interstate numbers run east and west): trivia per the review; stays online, never prints. Text keeps one sentence on odd and even numbers.

## Checks
- `tools/check_bank.py bank/core.json`: BANK PASSED (448 questions incl. other agents' chapters).
- `tools/originality_check.py check`: ch02 0.15 percent, ch03 0.34 percent, 0 copied runs: passed.
- `layout/build_book.py --core-only`: QA PASSED, 176 pages, originality passed. Picture questions render in the Ch 2 quiz (page 23 to 24) and in the mocks (pages 156, 160, 162).
- No em or en dashes, years or state names in the new text, figures or questions.

## Notes for the run leader
- Chapter 2 now has 13 figures in about 3,400 words, above the 1 per 400 words guide; the owner asked for the signs. The three tables add about 2 to 3 printed pages.
- `bank/core.json` uses indent 1 in the file; kept as found (the brief says indent 2).
- Another session committed this work in progress (commits e2ed336 and 622ba2b) while it was running; this agent made no commit.
