# Ohio fact check B: inserts and chapter 2 to 13 questions

Checked 2026-10-28. Scope: `state/OH/inserts.md` (all 28 keys, each read in place in the built `out/OH/Permit_Path_Ohio.md`) and every `bank/OH.json` question with `ch` other than 1 (OH-043 to OH-155, 113 questions). Chapter 1 questions were not touched.

Sources:
- **MAN**: Ohio Driver Manual HSY 7607 10/25, Drive file 16-Z3HYqpZnD0mmZ_MLkdbnQ3Hf06YGyr, read in full (page numbers are the printed ones)
- **ORC s**: https://codes.ohio.gov/ohio-revised-code/section-s (read: 4511.204 eff. 2025-06-30, 4511.213 eff. 2018-10-29, 4511.75 eff. 2025-09-30, 4513.263 eff. 2025-04-09, 4511.81 eff. 2025-03-20, 4513.03, 4513.15, 4511.68 eff. 2025-06-30, 4511.19 eff. 2025-04-09, 4510.036 eff. 2024-10-24, 4510.037, 4511.21 eff. 2025-06-30, 4511.13 eff. 2025-06-30, 4511.37, 4511.45, 4511.72, 4301.99)
- **OAC 4501:1-1-10**: https://codes.ohio.gov/ohio-administrative-code/rule-4501:1-1-10 (25 points per part)
- **FEES**: https://www.ohiobmv.gov/doc-fees.aspx (ALS and OVI reinstatement $315 for suspensions added or convictions on or after 4/9/25)
- **ABC6**: https://abc6onyourside.com/news/local/smartlane-opens-wednesday-on-670-east; **WOSU**: https://wosu.org/news/2023-05-08/odot-hopes-new-smartlane-will-ease-traffic-on-i-71-in-downtown-columbus

## Changes to inserts.md

| Key | Change | Reason | Source |
|---|---|---|---|
| phone_laws | Added that holding the phone to your ear for a call is legal if one tap or swipe starts and ends it | Legal error: the insert said drivers 18+ "may not hold" a phone, with no exception; the statute and manual allow holding it to the ear for a call | ORC 4511.204(B); MAN p. 8 |
| phone_laws | Added the first-offense distracted driving course option | OH-131 (ch 11) was not taught in Chapter 11 | ORC 4511.204(D)(2); MAN p. 8 |
| driver_record | "file proof of high-risk insurance (an SR-22)" to "file an SR-22, a form (not insurance) proving your coverage meets the minimum" | Old wording read as if an SR-22 were a kind of insurance, which is the wrong answer (A) of OH-139 | MAN p. 26 |
| road_test | Rewritten: schedule online or at a Driver Exam Station; front doors must open inside and out; stop with rear bumper even with the center marker, then back until the front bumper is even with the two rear markers; retest rules now pointed to Chapter 1 | "Stop beside the center marker" was imprecise; OH-152, OH-153, OH-154, OH-155 (ch 13) were not taught in Chapter 13. Retest waits remain in Chapter 1 (ch01.md, test failure section) | MAN pp. 42 to 43; OAC 4501:1-1-10 |
| move_over | "slow down and pass with caution" to "slow to a safe speed and pass with caution; the law sets no number" | Core ch04 promises the box gives "how much to slow down"; Ohio sets no figure | ORC 4511.213(A)(2); MAN p. 38 |
| school_bus | Trimmed to 90 words (no change of meaning) | Over the 90-word limit | |
| turn_on_red, dui_penalties, underage_alcohol | Trimmed to 90 words or fewer; OVUAC range now "from 0.02 to under 0.08" (statute wording); "minors" now "anyone under 21" | Word limit; precision | ORC 4511.19(B); ORC 4301.99 |

All 28 keys are now 90 words or fewer, with no em or en dashes and no years.

## Inserts verified without change

| Key | Verified against |
|---|---|
| school_zone | 20 mph at recess, arrival and dismissal or posted: ORC 4511.21(B)(1)(a); over 35 mph is a fourth degree misdemeanor: ORC 4511.21(P)(2); crossing guards: MAN p. 34 |
| work_zone | Speeding fine doubled in posted construction zone: ORC 4511.21(P)(3); phone fines doubled: ORC 4511.204(D)(1)(d); slow down with no workers: MAN p. 29 |
| turn_on_red | Right on red after stop, left on red one-way to one-way from far left lane, red arrow only with a permitting sign: ORC 4511.13(C)(1)(b), (C)(2); MAN p. 17 |
| move_over | Vehicle list (public safety, emergency, road service, waste collection, PUCO, highway maintenance), non-adjacent lane on 2+ same-direction lanes, doubled fine: ORC 4511.213(A), (D)(2); MAN p. 38 |
| emergency_vehicles | Right edge or curb, clear of intersection, stop: ORC 4511.45(A); opposite direction on divided highway need not stop: MAN p. 15; 500 ft and fire block: ORC 4511.72 |
| school_bus | 10 ft, until bus moves or driver signals: ORC 4511.75(A); "four or more lanes" exception: ORC 4511.75(C) ("divided into four or more traffic lanes", which the manual renders as a road with four or more lanes, not a median-divided highway); $500, in-person court appearance, class seven suspension (up to one year): ORC 4511.75; MAN p. 22 |
| u_turn | Curve or crest, 500 ft visibility: ORC 4511.37(A); median openings: MAN p. 19 |
| speed_limits | 15, 20, 25, 35, 55, 70: ORC 4511.21(B)(7), (1)(a), (2), (3), (5), (14); points 2, 2, 4: ORC 4510.036(C)(11), (12) |
| following_distance | Four seconds or one length per 10 mph, increase cases, motorcycle 4 s: MAN pp. 31, 34 |
| hov | SmartLane eastbound I-670, left shoulder, green arrow open to all, red X closed: ABC6; still operating in May 2023: WOSU (see open items) |
| parking_rules | 10, 20 (crosswalk at intersection), 20 (fire station driveway), 30, 50 ft, 1 ft: ORC 4511.68(A); 12 inches, either curb on one-way: MAN p. 23 |
| bicycle_passing | 3 ft: MAN p. 35; ORC 4511.27; half the posted limit rule: MAN p. 38 |
| crash_reporting | 911, OSHP, sheriff or police; unattended vehicle; BMV 3303 within six months: MAN p. 41; proof of insurance over $400: MAN p. 24 |
| bac_limits | 0.08, 0.04, 0.02: MAN p. 25; 0.17 high test: ORC 4511.19(A)(1)(f) |
| implied_consent | Two hours, refusal 1, 2, 3, 5 years, stands if acquitted, 90 days first test over: MAN p. 25; $315: FEES |
| dui_penalties | 3 days or 3-day program; high test both; $565 to $1,075; 1 to 3 years: ORC 4511.19(G)(1)(a); open container: ORC 4301.62 |
| underage_alcohol | OVUAC class six (3 months to 2 years): ORC 4511.19(H), MAN p. 25; under 18 in a vehicle 6 months to 1 year; false ID $250 to $1,000; furnishing $500 to $1,000: ORC 4301.99 |
| phone_laws | Fines $150, $250, $500 and 90-day suspension: ORC 4511.204(D)(1); points 2, 3, 4: ORC 4510.036(C)(13) |
| seat_belts | Driver and front seat only; secondary enforcement; $30 and $20: ORC 4513.263(B), (D), (G); under 18 driver rule: MAN p. 6 |
| child_restraints | Under 4 or under 40 lb seat; under 8 and under 4 ft 9 in booster; 8 through 15 belt or seat; $25 to $75: ORC 4511.81(A), (C), (D), (L); 12 and under in back, airbag: MAN p. 27 |
| vehicle_rules | 1/16 in, studs Nov 1 to Apr 15, tint 70 and 50 plus or minus 3: MAN pp. 4 to 5; 25/50/25: MAN p. 24 |
| police_stop | MAN p. 28 |
| headlight_use | Sunset to sunrise, 1,000 ft, wipers for precipitation: ORC 4513.03(A); bad weather: MAN p. 28; fog low beams: MAN p. 29 |
| driver_record | 6-point letter, 12 points class D (6 months): ORC 4510.037(A), (B); 2-point credit for 2 to 11 points, once in three years: ORC 4510.037(C); reinstatement: MAN p. 26; point values: ORC 4510.036 |
| supervised_hours | 50 hours, 10 night, BMV 5791, driver ed 24 + 8, six months TIPIC: MAN p. 3 |
| signal_distance | 100 ft, hand signals: MAN p. 17; four or more lanes: MAN p. 18 |
| headlight_dimming | No distance in feet: ORC 4513.15(A)(1); dim for approaching traffic: MAN p. 28 |

## Question fixes

| ID | Old | New | Reason |
|---|---|---|---|
| OH-056 | "You are driving toward a stopped school bus with red lights flashing on a road with four lanes." | "A school bus is stopped with red lights flashing on a four-lane road, and you are coming toward it from the opposite direction." | "Driving toward" also fits a driver coming up behind the bus, who must stop; the keyed answer is right only for opposite-direction traffic (ORC 4511.75(C); MAN p. 22) |

All other 112 questions (OH-043 to OH-155) verified: one defensible answer, correct key, taught in their chapter (Chapter 13 questions OH-152 to OH-155 after the road_test change, Chapter 11 OH-131 after the phone_laws change). Every quiz-flagged question is taught in its chapter's box. No keys changed.

Notes on questions checked and kept:
- OH-075 (four seconds): MAN p. 15 says "Allow 3-4 second following distance", but p. 31 states the minimum as four seconds; the stem asks for the minimum, so the key stands.
- OH-085, OH-086 (SmartLane) are app_only; sources are news reports, not ODOT pages.

## Core sentences that conflict with Ohio (not edited; core is out of scope)

- core/ch04.md 4.7 and its Quick Review: "Stay stopped until the red lights stop flashing and the stop arm is folded." Ohio: stay stopped until the bus resumes motion or the bus driver signals you to go (ORC 4511.75(A)). The Ohio box states the Ohio rule right below, so a reader sees both. Low risk; a core hedge such as "or as your state's rule allows" would remove it.
- core/ch06.md 6.5 Test trap ("choose the seconds answer" over "one car length for every 10 mph"): the Ohio manual teaches both as equal minimums (MAN p. 31). No Ohio question conflicts (OH-082 asks for the method besides four seconds), but the trap is wrong for Ohio if a test item offers both.
- core/ch10.md 10.7 brake failure ("Pump the brake pedal" first): MAN p. 40 says use the parking brake first, then turn off the engine. Not a legal rule; no Ohio question depends on it.

## Open items

- I-670 SmartLane: the last source confirming it operates is from May 2023 (WOSU); no ODOT page found. The questions are app_only. Recheck before release, or drop the SmartLane sentence from the hov box.
- The road_test box no longer states the under-21 two-day wait or the adult course; Chapter 1 teaches both and core 13.6 points to Chapter 1.
