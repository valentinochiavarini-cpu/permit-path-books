# New Jersey fact check B

Scope: `state/NJ/inserts.md` (all 28 keys, read in context in the built `out/NJ/Permit_Path_New_Jersey.md`) and every `bank/NJ.json` question with ch 2 to 13 (NJ-044 to NJ-135). Checked 2026-10-28.

**Manual access:** the NJ Driver Manual still could not be read. nj.gov PDFs (English, Tagalog, Portuguese) fail through WebFetch and nj.gov is blocked for direct download in this environment; state.nj.us was not permitted. Everything below rests on statutes (law.justia.com, 2025 N.J. Revised Statutes), nj.gov/mvc, nj.gov/oag and nj.gov/dobi pages.

## Insert changes

| Key | Old | New | Reason and source |
|---|---|---|---|
| turn_on_red | "A **steady red arrow** means stop and stay stopped for that turn until the signal changes." (and "Wait for the green." after the left on red line) | "A **steady red arrow** is a stop signal too: after a full stop you may turn right on it unless a sign forbids it. Never turn left on one." ("Wait for the green." cut for length) | N.J.S.A. 39:4-115(b) lets a driver, after a full stop, turn right "upon a 'stop' or 'caution' signal" unless an official sign prohibits it. The statute makes no exception for arrows, so the national default (no turn on a red arrow) is not NJ law as written. https://law.justia.com/codes/new-jersey/title-39/section-39-4-115/ . Secondary support: shmoop NJ drivers ed page (right on red arrow after full stop). See open item 1. |
| road_test | No supervising driver, no examiner-only rule, no endorsement | Added: bring an NJ licensed driver at least 21 with three years of driving experience; only the examiner rides along; on a pass the examiner endorses your permit. Shortened "on the test car" to "on the car", "to retest" cut. | Quiz question NJ-131 (and NJ-134, NJ-135) were not taught in the Chapter 13 box. https://www.nj.gov/mvc/license/roadtest.htm ; https://www.nj.gov/mvc/license/youngadult.htm ; nj.gov/mvc/pdf/license/FAQ_firsttime.pdf (examiner only, per sources.md). 88 words. |

All other 26 keys verified, no change:

| Key | Verified against |
|---|---|
| school_zone, speed_limits | N.J.S.A. 39:4-98 (25 school zone with the three conditions; 25 business/residential; 35 suburban; 50 other; 65 MPH act exception). Points 2/4/5: nj.gov/mvc/license/points-schedule.htm |
| work_zone | N.J.S.A. 39:4-203.5 (double fines in posted construction zones and safe corridors; missing or stolen sign no defense; no worker presence requirement) |
| move_over | N.J.S.A. 39:4-92.2 (a: red or blue emergency; b: amber tow, yellow/amber/red maintenance, amber sanitation; c: disabled vehicles with hazards, flares, triangles; non-adjacent lane or below limit and ready to stop; $100 to $500). Not in the insert: 2 points for a third violation in 12 months (left out, minor). |
| emergency_vehicles | N.J.S.A. 39:4-92 (right-hand curb, clear of intersection; 300 feet; 200 feet from fire apparatus) |
| school_bus | N.J.S.A. 39:4-128.1 (25 feet; divided highway with safety island or barrier: 10 mph until past bus and children; first offense at least $100, up to 15 days jail or 15 days community service); 5 points: points schedule |
| u_turn | N.J.S.A. 39:4-125 |
| signal_distance | N.J.S.A. 39:4-126 (per sources.md; consistent with MVC points schedule wording) |
| following_distance | nj.gov/oag/hts/downloads/Tailgating_Palm_Card.pdf (2 seconds; 4 or 5 in poor conditions; $140 or more and 5 points) |
| parking_rules | N.J.S.A. 39:4-138 (10 hydrant; 25 crosswalk or side line, 10 with curb extension; 50 stop sign; 50 rail; 20 fire station driveway, 75 opposite side when signposted); 39:4-135 (6 inches) per sources.md |
| bicycle_passing | N.J.S.A. 39:4-92.4 (non-adjacent lane; 4 feet; 25 mph or posted limit if lower; $100, or $500 and 2 points with injury) |
| crash_reporting | N.J.S.A. 39:4-130 (injury, death or damage over $500, quickest means; MVC report in 10 days unless officer reports; $30 to $100; MVC may suspend) |
| headlight_use | N.J.S.A. 39:3-46 (half hour after sunset to half hour before sunrise; 500 feet; wipers) |
| headlight_dimming | N.J.S.A. 39:3-60 (500 feet oncoming). Following rule has no statutory figure; insert gives none. |
| bac_limits | N.J.S.A. 39:4-50; 39:4-50.14; nj.gov/mvc/license/suspension.htm (0.08). Commercial 0.04 per 39:3-10.13 (sources.md). |
| implied_consent | N.J.S.A. 39:4-50.4a (first refusal $300 to $500, IDRC, forfeiture until interlock); 39:4-50.17 (9 to 15 months after license returned); surcharge $1,000 x 3: nj.gov/mvc/license/surcharge.htm |
| dui_penalties | N.J.S.A. 39:4-50(a)(1) (fines $250 to $400 and $300 to $500; up to 30 days; IDRC 12 to 48 hours; 0.15+: 3 months forfeiture following interlock installation); 39:4-50.17 (3 months; 7 to 12 months; 12 to 15 months); 39:4-51b (open container, all occupants, $200 first) |
| underage_alcohol | N.J.S.A. 39:4-50.14 (30 to 90 days; 15 to 30 days community service; IDRC or alcohol education; starts at eligibility or conviction, whichever later); 2C:33-15 (written warnings, no fine); 33:1-81 (disorderly persons, at least $500) |
| phone_laws | N.J.S.A. 39:4-97.3 (hands-free only; emergency reporting exception; $200 to $400, $400 to $600, $600 to $800; 3 points and possible 90 days on third); 39:3-13(c) and 39:3-13.4(c) (permit and probationary holders, any age: no hand-held or hands-free device) |
| seat_belts | N.J.S.A. 39:3-76.2f (driver, front, rear 18+, 8 to 17 with driver responsible); 39:3-76.2j ($20, no points); GDL $100: nj.gov/mvc/about/gdlsafety.htm, 39:3-13.4(c) |
| child_restraints | N.J.S.A. 39:3-76.2a (three tiers, rear seat, no rear-facing seat at an active airbag) |
| vehicle_rules | nj.gov/mvc/inspection/aboutinsp.htm (every 2 years; new 5 years; up to 2 months early); N.J.S.A. 39:3-36 (one week, up to $25) |
| police_stop | nj.gov/oag/safestopnj/tips.html; N.J.S.A. 39:3-29 ($150) |
| driver_record | nj.gov/mvc/license/suspension.htm (12 points; minus 3 per clean year; defensive driving 2 points once in 5 years); surcharge.htm ($150 plus $25 per point over 6, 3 years); nj.gov/dobi standard policy chart (35,000 / 70,000 / 25,000; PIP 15,000) |
| supervised_hours | nj.gov/mvc/license/youngadult.htm (50 hours, 10 in darkness, BA-CSD, 6 months, supervisor 21+ with 3 years, front seat) |
| hov | OMIT kept, see open item 2 |

Word counts: every insert 90 words or fewer (turn_on_red 83, road_test 88). No em or en dashes. No years.

## Question fixes

None needed. All 92 questions with ch 2 to 13 have one defensible answer and a correct key, and match the sources above. Every quiz-flagged question (3 or fewer per chapter) is now taught in its chapter's box; NJ-131 was not, fixed through the road_test insert, not the bank. `bank/NJ.json` was not written.

## Core sentences checked against NJ law (not edited, outside scope)

1. Ch 11, 11.3: "you agree in advance to take a chemical test (breath, blood or urine)". NJ implied consent (N.J.S.A. 39:4-50.2) covers breath samples; blood generally needs a warrant or consent. Not wrong as a national statement, but loose for NJ. The NJ box correctly says "breath test".
2. Ch 13, 13.6: "If you pass, you are licensed." In NJ the examiner endorses the permit and you get the probationary license at an MVC licensing center (roadtest.htm). The road_test box now says this.
3. Ch 3, 3.4 table "Steady red arrow: Stop for that turn" is fine with the new box. Line 734 defers to the box, which now answers it.
4. Ch 7, 7.3: "Most states set the limit at 100 feet" (no passing near intersections and rail crossings) is printed in the NJ edition as a hedge. Not checked against NJ (39:4-85 ff.) in this pass.
No other core sentence contradicts NJ law: right on red, left turns, U-turns, emergency vehicles, Move Over, school buses, following distance, headlights, parking, crash steps, BAC, phones, seat belts, child seats, documents and points all agree with the NJ boxes.

## Open items

1. **Red arrow:** confirm against the current NJ Driver Manual. The new wording follows N.J.S.A. 39:4-115 as written (right turn allowed on a "stop" signal, no arrow exception). If the manual says no turn on a red arrow, swap the sentence back and log the conflict.
2. **HOV:** NJ is not free of HOV lanes. Wikipedia (New Jersey Turnpike) and NJ 101.5 (July 2015) report weekday peak HOV 3+ lanes on the Turnpike outer roadway between interchanges 11 and 14. I-80 and I-287 HOV lanes ended in 1998. No NJTA primary page found, so OMIT stays: the core 7.9 text (diamond, HOV 2+/3+, signs) already covers them. Optional insert if NJTA confirms: "The New Jersey Turnpike has HOV lanes between Interchanges 11 and 14 on weekday rush hours, for vehicles with 3 or more people."
3. Move Over points (2 points for a third violation in 12 months, 39:4-92.2) not in the insert or bank; low test value.
4. Child restraint fine, wiper rule fine and turn signal statute text (39:4-126, 39:4-135) were taken from sources.md and not re-read.
