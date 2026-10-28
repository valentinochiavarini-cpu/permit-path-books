# Virginia fact check B (inserts and state questions, ch 2 to 13)

Checker B, 2026-10-28. Scope: `state/VA/inserts.md` (all 28 keys, read in context in the rebuilt `out/VA/Permit_Path_Virginia.md`) and every `bank/VA.json` question with ch 2 to 13 (VA-041 to VA-158). Chapter 1 and its questions belong to checker A and were not touched.

Rebuild before the check: `python3 layout/build_book.py --state Virginia --code VA` passed QA (194 pages) and originality.

## Sources read
- Code of Virginia (law.lis.virginia.gov/vacode/...): 46.2-818.2 (history ends 2026 c. 518; first offense $125, later $250, work zone mandatory $250, holding ban only), 46.2-818.3 (2026 c. 1047: up to $500, then 30 and 90-day suspensions, secondary enforcement), 46.2-829, 46.2-835, 46.2-836, 46.2-839, 46.2-845, 46.2-849, 46.2-861.1 (4+ lanes, 2 going your way; A reckless, B infraction; not in work zones), 46.2-862 (20 or more over, or over 85), 46.2-870, 46.2-873, 46.2-878.1, 46.2-878.3 (extra $100 above 80 and below 86 in a 65 zone), 46.2-882.1, 46.2-896, 46.2-1030, 46.2-1034, 46.2-1094 (18+ every seat, $25, no points, secondary; history ends 2026 c. 93), 46.2-1095, 46.2-1098, 46.2-1157, 46.2-1158 (every 12 months), 46.2-472 ($50,000 / $100,000 / $25,000 from 2025 policies), 18.2-266.1 (0.02 to under 0.08, 1 year, $500 or 50 hours), 18.2-268.3, 18.2-270, 18.2-271, 18.2-323.1, 33.2-501.
- vacode.org 2026 text mirror for 46.2-859 (school bus; any direction, highway, private road, school driveway; divided highway, access road or driveway separated by barrier or unpaved area; no distance; reckless driving) and 46.2-818.2 / 46.2-861.1 / 18.2-266.1 wording checks.
- dmv.virginia.gov/licenses-ids/improvement/points/system and /points/over-18.
- Virginia Driver's Manual DMV 39 (Apr. 2026), Drive file 140cORhpylUEb5NgAbIfxkpA_TNE1g82Q: signs (pp. 6 to 10), bike boxes and HOV (p. 13), speed (p. 14), school bus and flashing lights (pp. 15 to 16), turning and signals (p. 18), following distance (p. 19), parking (p. 22), crashes (p. 25), police stops (p. 26), belts and child seats (p. 27), alcohol under 21 and fake ID (pp. 30 to 31).
- Sign pictures: every `img` file used by VA questions exists in `layout/fig/`; lane_ends, merge, two_way_traffic, divided_highway_ends, y_intersection, slippery, horse_drawn, low_shoulder, rr_advance, crossbuck, no_passing_zone, signal_ahead, flagger_ahead, wrong_way, one_way, no_u_turn and left_turn_yield_green were rendered and compared with the MUTCD designs and the question wording.

## Inserts
All 28 keys checked against the sources above. No legal or numeric error found; no edit made. All are 90 words or fewer (longest: phone_laws 89), with no em or en dashes and no years.

Points confirmed in the statutes (the hard checks):
- move_over: blue, red or amber; lane change on 4+ lanes with 2 going your way, else caution; reckless driving; hazard lights, flares, caution signs an infraction (46.2-861.1).
- school_bus: any direction; highway, private road, school driveway; divided highway exception; no stopping distance in the law; reckless driving (46.2-859). "Stop even if the lights are off" is the manual (p. 15).
- turn_on_red: right after stop; left only one-way to one-way (46.2-836); red arrow hold unless a sign permits (46.2-835, 46.2-836); bike box ban (manual p. 13).
- dui_penalties, implied_consent, bac_limits, underage_alcohol: match 18.2-266.1, 18.2-268.3, 18.2-270(A), (D), 18.2-271, 18.2-323.1 (Class 4 misdemeanor).
- phone_laws: match 46.2-818.2 as amended 2026 (the 2026 amendment did not change the ban or fines) and 46.2-818.3.
- seat_belts: 18+ in every seat, $25, no points, secondary (46.2-1094 as of 2026). child_restraints: 46.2-1095, 46.2-1098.
- speed_limits: 46.2-862 thresholds, 46.2-870 (70 only where posted), 46.2-878.3.
- driver_record: 2-year points, 1 safe driving point per clean year up to 5, clinic 5; 12/12 or 18/24 clinic; 18/12 or 24/24 90-day suspension (DMV points pages).
- vehicle_rules: annual inspection (46.2-1158); 50/100/25 (46.2-472).
- headlight_use: 46.2-1030 (500 feet, wipers, intermittent mist exception, no points, secondary). headlight_dimming: 46.2-1034. signal_distance: 46.2-849.
- crash_reporting: manual p. 25; 24-hour police report for unattended property (46.2-896).
- hov: 33.2-501 ($100; Planning District 8 $125, $250, $500, $1,000; 3 points from the second offense; motorcycles exempt).

## Core sentences read against Virginia law
No core sentence contradicts Virginia law. Notes (no change needed, outside scope):
- 4.6 says an emergency vehicle uses "a siren, flashing lights or both". 46.2-829 requires both for the duty to yield, but the VA manual (p. 16) uses the same "or both" wording, so the text matches the test.
- 4.7 says stay stopped "until the red lights stop flashing and the stop arm is folded, or until the moment your state's box below allows"; the VA box (until everyone is clear and the bus moves) governs. Not a contradiction.
- 4.6 Move Over says slow "well below the speed limit" if you cannot move over; Virginia only requires due caution and a safe speed. Advice, not a legal claim; consistent with the box.
- 11.3 says implied consent covers breath, blood or urine; the VA box mentions breath only (the misdemeanor second refusal applies to breath only, 18.2-268.3(A), so the box wording is kept).

## Question fixes
| ID | Old | New | Reason |
|---|---|---|---|
| VA-058 | "A white sign at a signal reads LEFT TURN YIELD ON GREEN with a green circle." | "A white sign at a signal reads LEFT TURN YIELD ON, followed by a green circle." | The MUTCD R10-12 sign and `sq_left_turn_yield_green.svg` read LEFT TURN YIELD ON with a green ball; the word GREEN is not on the sign (core 3.2 already says "LEFT TURN YIELD ON sign with a green ball"). |
| VA-157 | "An adult with no driver education takes the road skills test..." | "An adult 21 or older with no driver education takes the road skills test..." | Applicants 18 to 20 will need driver education (HB 1224, Code 46.2-324.1, applied by DMV from January 1, 2027), so the stem now names the group for whom the CSMA 19 route stays valid. |

All other ch 2 to 13 questions (VA-041 to VA-158) have one defensible answer, a correct key, and are taught in their chapter. Every quiz-flagged question (VA-068 to 070, 072 to 074, 077, 080, 085, 088, 089, 091, 094, 097, 100, 103, 106 to 108, 112, 113, 115, 117, 118, 126, 128, 131, 144, 148, 149, 155 to 157) is taught in its chapter's Virginia box. Sign pictures match their descriptions.

Checks: `python3 tools/check_bank.py bank/core.json bank/VA.json` BANK PASSED; `python3 tools/originality_check.py check state/VA/inserts.md` ORIGINALITY PASSED (0.05 percent shared, no 12-word runs).

## Open items
- law.lis.virginia.gov/vacode/46.2-859/ was blocked in this session (permission request timed out); the 2026 text was read on vacode.org instead.
- road_test: "Failing to wear your belt or to stop fully at a stop sign ends it" rests on the old Road Skills Testing Guide (closed course retired 2024); DMV publishes no current on-road scoring sheet (already logged in sources.md).
- 18.2-266.1 and 18.2-268.3 carry 2026 amendments (c. 1112; cc. 686, 687, 1112) whose content could not be read; the current code text still gives the penalties used in the book.
- VA-104 (motorcycles in HOV) is `app_only` although the hov box now teaches it; it could be printed. Left as is.
