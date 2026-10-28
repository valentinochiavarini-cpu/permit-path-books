# North Carolina fact check B: inserts and chapter 2 to 13 questions

Checked 2026-10-28. Scope: `state/NC/inserts.md` (all 28 keys, each read in place in the rebuilt `out/NC/Permit_Path_North_Carolina.md`) and every `bank/NC.json` question with `ch` other than 1 (NC-041 to NC-160, 120 questions). Chapter 1 questions were not touched.

Sources:
- **GS n**: https://www.ncleg.gov/EnactedLegislation/Statutes/HTML/BySection/Chapter_20/GS_n.html (read: 20-4.01, 20-11, 20-16, 20-16.1, 20-16.2, 20-129, 20-131, 20-135.2A, 20-135.2B, 20-137.1, 20-137.3, 20-137.4A, 20-138.3, 20-138.7, 20-140.3, 20-141, 20-141.1, 20-149, 20-150, 20-154, 20-157, 20-158, 20-160.1, 20-162, 20-179, 20-181, 20-217, 20-279.1)
- **SL2025-47**: https://www.ncleg.gov/EnactedLegislation/SessionLaws/HTML/2025-2026/SL2025-47.html (s. 13 school zone cameras; s. 22(d) tinted window at stops)
- **SL2026-46**: https://www.ncleg.gov/EnactedLegislation/SessionLaws/HTML/2025-2026/SL2026-46.html (s. 17 unpaved road limit, effective December 1, 2026)
- **SOG**: https://nccriminallaw.sog.unc.edu/2025/08/06/summer-2025-motor-vehicle-law-changes/
- **HB**: NC Driver Handbook, rev. May 2025, Drive file 1xsHtFARBh7SuBf0V7-TNRynnxLqu0gRf
- **L2**: https://www.ncdot.gov/dmv/license-id/driver-licenses/new-drivers/Pages/level2.aspx
- **TESTS**: https://www.ncdot.gov/dmv/license-id/driver-licenses/new-drivers/Pages/driver-license-tests.aspx
- **I77**: https://www.fhwa.dot.gov/ipd/project_profiles/nc_i77_express_lanes.aspx
- **MUTCD**: FHWA MUTCD 11th edition (sign descriptions; colors Sec. 2A.06, Table 2A-2; incident pink Sec. 6H.01)

## Changes to inserts.md

| Key | Change | Reason | Source |
|---|---|---|---|
| school_bus | "Passing a stopped bus: 5 points and at least $500" to "5 points, at least $500" | Insert was 91 words built (limit 90); now 90 | Word limit |
| speed_limits | "At a speed above 55, going more than 15 over also costs your license..." to "Either one, at a speed above 55, also costs your license for at least 30 days" | The 30-day suspension also applies to any conviction for driving over 80 mph, which the old sentence left out | GS 20-16.1(a); HB Ch. 3 |
| dui_penalties | "no one may hold or drink from" to "no one may keep or drink from" an open container | G.S. 20-138.7(a1) bans possessing an open container in the passenger area (glove box included), not only holding one | GS 20-138.7(a1), (f) |
| road_test | Added "(stopping as fast as you safely can when told)" after quick stop; "with its registration card" to "its registration" | NC-157 (quiz, ch 13) asks what a quick stop is; neither the insert nor core Chapter 13 defined it. L2 now accepts a printed or downloaded registration copy | HB Ch. 1 Skills Observed; TESTS; L2 |
| supervised_hours | "you hand in a printed copy" to "NCDMV takes a printed or digital copy" | L2: "Driving log showing at least 60 hours of driving (digital and printed copies accepted)". Log must still be signed by the supervisor (GS 20-11(d)(5)). Requested by the coordinator; agreed after checking. `sources.md` driving log row updated to match | L2; GS 20-11(d)(5) |

All 28 inserts are 90 words or fewer as built, with no dashes and no years.

## Inserts verified without change

| Key | Verified against |
|---|---|
| school_zone | Not below 20 mph, school days, posted hours or flasher, $250: GS 20-141.1. 3 points: GS 20-16(c). Cameras: any city or county may use them, warning signs within 1,000 feet, $250 civil penalty, no license or insurance points, effective October 1, 2025: SL2025-47 s. 13 |
| work_zone | $250 extra only where signs at start and end post it: GS 20-141(j2). Failure to yield with serious bodily injury (work zone is one listed case): Class 2 misdemeanor, $500, 90-day revocation: GS 20-160.1; HB Ch. 3 |
| turn_on_red | Right on red after complete stop unless sign; yield to traffic and pedestrians; $100 to $500: GS 20-158(b)(2). Statute authorizes only right turns on red. Red arrow: HB Ch. 5 |
| move_over | 12 feet, covered vehicles (wrecker, utility, refuse, highway maintenance), lane not nearest, else slow and be prepared to stop, $250, up to six months for serious injury or death: GS 20-157(f), (g), (i); HB Ch. 4 |
| emergency_vehicles | Right edge and stop; exception for opposite direction on a four-lane limited access highway with a median: GS 20-157(a). One block / 400 feet, fire hose, 100 feet at crash: GS 20-157(b) to (e). Class 2 misdemeanor; failure to stop for siren 3 points: GS 20-16(c) |
| school_bus | Table matches GS 20-217(c) (divided by a space or barrier, including a center left turn lane on a road of at least four lanes) and HB Ch. 4 table. No distance in feet; stop until signal withdrawn, lights off and bus moving: GS 20-217(a). Class 1 misdemeanor, at least $500: (e); second within 3 years, one year: (g1); 5 points: GS 20-16(c) |
| u_turn | GS 20-140.3; HB Ch. 4 (Interstates, roundabouts), Ch. 5 (green arrow U-turn yields to opposing right turn) |
| speed_limits | 35 / 55: GS 20-141(b). 70 max: GS 20-141(d)(2). 25 unpaved or no center line: SL2026-46 s. 17(a), (b). Over 55: 3 points; other moving violations 2: GS 20-16(c). Class 3 misdemeanor for more than 15 over or over 80: GS 20-141(j1) |
| following_distance | Two-second rule, 5 to 10 mph slower and twice the gap when wet, three times stopping distance on snow and ice: HB Ch. 4. Following too closely 4 points: GS 20-16(c) |
| hov | HOV lanes converted to express toll lanes; HOV3+ free; declare in the NC Quick Pass app or website up to 15 minutes before entry, or with a Flex transponder switch: I77 |
| parking_rules | 15 feet hydrant or fire station; 25 feet curb lines, 15 feet without curb; driveway: GS 20-162(a). Crosswalk, sidewalk, bridge, travel lane, shoulder 200 feet, fire 1 block / 400 feet, Interstate: HB Ch. 4 Parking |
| bicycle_passing | 2 feet: GS 20-149(a). No-passing zone exception (bicycle or moped, same direction, 4 feet or full lane change, not turning left): GS 20-150(e). At least $200: GS 20-154(a1) |
| crash_reporting | Death, injury or $1,000 total damage: GS 20-4.01(33b). 3 points: GS 20-16(c). Move drivable cars: HB Ch. 4 |
| bac_limits | 0.08, 0.04 commercial, any alcohol under 21: GS 20-138.3; HB Ch. 2 |
| implied_consent | Immediate revocation at least 30 days, 12-month DMV revocation, refusal admissible, limited privilege after six months, 30-minute limit for lawyer or witness: GS 20-16.2(a), (d), (e1) |
| dui_penalties | Level Five 24 hours to 60 days, $200; Level Three 72 hours to 6 months, $1,000; Level One 30 days to 24 months, $4,000; judge sets level: GS 20-179. First conviction one year, interlock at 0.15: HB Ch. 2. For-hire passengers exempt: GS 20-138.7(a2) |
| underage_alcohol | Class 2 misdemeanor: GS 20-138.3. One-year revocations: HB Ch. 2, Alcohol and the Young Driver |
| phone_laws | All drivers: no manual texting or reading email or text; $100 plus costs; no points; parked, voice and GPS exceptions: GS 20-137.4A. Under 18: any phone use while moving, hands-free included; parent, guardian, spouse or emergency only; $25: GS 20-137.3. School bus: GS 20-137.4A |
| seat_belts | All occupants; $25.50 plus costs front; $10 rear, no costs; no points; rear alone not a reason to stop: GS 20-135.2A. Under 16 in open bed: GS 20-135.2B |
| child_restraints | GS 20-137.1(a), (a1), (c), (d): under 16 restrained; under 8 and under 80 lb; under 5 and under 40 lb rear seat with active airbag; lap belt exception 40 to 80 lb; up to $25; 2 points |
| vehicle_rules | Inspection within 90 days before expiration: HB Ch. 7. Insurance 50/100/50: GS 20-279.1(11). Address and name 60 days, plate covers: HB Ch. 7. Tint 35 percent still law (tint no longer checked at inspection under SL2025-47, not a contradiction) |
| police_stop | HB Ch. 4, What Motorists Should Do When Stopped. Lowering tinted window on the officer's side: GS 20-127(g), SL2025-47 s. 22(d), effective December 1, 2025 |
| headlight_use | GS 20-129(a): sunset to sunrise, 400 feet, 500 feet, wipers due to smoke, fog, rain, sleet or snow, intermittent misting exception, $5, no points. Low beams in fog and city: HB Ch. 4 |
| driver_record | 7 points clinic, $83.50, minus 3 once in five years; 12 points in 3 years; 8 after reinstatement; up to 60 days, 6 months, one year: GS 20-16(a)(5), (c); HB Ch. 3 |
| road_test | Quick stops, backing, three-point turnabouts; retest after seven calendar days: TESTS. Own car, pre-trip inspection, parent or guardian present, NCDMV office or certified driver education school, printed insurance: L2 |
| supervised_hours | 60, 10 night, 10 per week, signed by supervisor: GS 20-11(d)(5). Supervisor licensed 5 years: GS 20-11(k); seated beside: GS 20-11(c)(2), (e)(3). Nine months: L2 |
| signal_distance | 100 feet before stopping or turning; 200 feet before turning at 45 mph or more: GS 20-154(b) |
| headlight_dimming | 500 feet: GS 20-131(a) (no glare to persons within 500 feet when meeting); 200 feet following, except when passing: GS 20-181 |

## Question fixes (bank/NC.json, ch 2 to 13)

| ID | Old | New | Reason |
|---|---|---|---|
| NC-046 | quiz: true | quiz: false | Duplicated core Chapter 2 quiz question 1 (both ask about the red octagon) in the same printed quiz |
| NC-072 | quiz: false | quiz: true | Replaces NC-046 in the Chapter 2 quiz (still 3 state questions); EXCEPT RIGHT TURN is taught in the Section 2.4 table |
| NC-057 | src "MUTCD 11th ed., Sec. 2A.10" | "MUTCD 11th ed., Sec. 2A.06, Table 2A-2" | Wrong section number for sign colors in the 11th edition (core logs use 2A.06) |
| NC-058 | src "MUTCD 11th ed., Sec. 2A.10" | "MUTCD 11th ed., Sec. 2A.06, Table 2A-2; Sec. 6H.01" | Same; pink incident signs are in 6H.01 |
| NC-105 | "The license is revoked for at least:"; src handbook only | "The license is taken for at least:"; src adds G.S. 20-16.1(a) | Statute calls it a suspension, the handbook a revocation; neutral wording, statute cited. Key unchanged (30 days) |
| NC-106 | src "S.L. 2026-46, s. 17; G.S. 20-141(b)(3)" | "S.L. 2026-46, s. 17 (amends G.S. 20-141(b), effective December 1, 2026)" | The subdivision number could not be confirmed (the online G.S. 20-141 text does not yet show the amendment) |

All other 114 questions verified: one defensible answer, key correct, taught in the chapter's core text or NC box, no conflict with the chapter text. All 33 quiz-flagged state questions in Chapters 2 to 13 are taught in their chapter (NC-157 after the road_test fix). Sign questions NC-046 to NC-079 checked against the MUTCD shapes, colors and symbols (R1-1, R1-2, S1-1, W14-3, W10-1, R15-1, R5-1, R5-1a, W8-5, W4-1, W6-3, W6-2, W20-7, W13-1P, W1-1/W1-2, W2-5, W2-2, W2-6, W5-3, W8-9, W14-2, R1-10P, EXIT ONLY panel, R3-9 series, W1-13, W3-3, R6-3, R1-2aP); NC route marker diamond: HB Ch. 5.

Checks: `python3 tools/check_bank.py bank/core.json bank/NC.json`: BANK PASSED. `python3 tools/originality_check.py check state/NC/inserts.md`: PASSED (0.09 percent). NC rebuild: QA PASSED, 196 pages.

## Core sentences that conflict with North Carolina (not edited, outside scope)

1. **core/ch07.md, Section 7.3 and quiz C07-031**: "Do not pass within 100 feet of an intersection or a railroad crossing ... bridge, viaduct or tunnel", quiz keyed 100 feet with 500 feet as a distractor. North Carolina has no 100-foot rule: G.S. 20-150 bans passing at intersections and rail crossings, and on curves or hills where you cannot see 500 feet ahead (HB Ch. 4 lists 500 feet). An NC reader learns a number the NC test does not use, and 500 feet is a wrong answer in the book. Suggest a `passing` insert or `[[generic]]` hedge.
2. **core/ch04.md, Section 4.6**: "The box below gives the rule for one way streets and how far back to stay." The NC box has no one-way street rule because G.S. 20-157(a) has none. Promise not kept for NC.
3. **core/ch10.md, Section 10.2**: hydroplaning "can start at speeds as low as about 35 mph"; the NC handbook says 30 mph (HB Ch. 4, Hydroplaning). Risk if the NC test asks the number.
4. **core C04-022** (ch 4 quiz): keyed "When the red lights stop flashing and the stop arm folds in". NC law also requires the bus to start moving (G.S. 20-217(a)); the NC box says so. Still the best of the four options, so no conflict in the key, but the core sentence in 4.7 omits the third condition.
5. Minor: core ch10.4 "slow to about half your normal speed" on packed snow vs HB "reduce speed by more than half". Core ch6.2 "For a new driver, one ticket can also bring a suspension": NC provisional suspensions start at the second moving violation in 12 months (G.S. 20-13), though some single offenses suspend any driver.

## Open items

- The 25 mph unpaved road limit (speed_limits insert, NC-106 app_only) takes effect December 1, 2026. If the book goes on sale before then, it states a rule not yet in force. Owner decision already logged in `sources.md`; flagging again.
- Knowledge test question count is still unpublished (not in scope here; affects mock sizing).
