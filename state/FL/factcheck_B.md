# Florida fact check B

Checker B, 2026-10-28. Scope: `state/FL/inserts.md` (all 23 keys, each read in context in `core/chNN.md` and `core/95_driving_log.md`) and every `bank/FL.json` question with ch other than 1 (FL-043 to FL-142). Ch 1 questions not touched.

Sources: Florida Statutes, 2026 edition, read on m.flsenate.gov/Statutes/<section> (cited below as "FS n"); Official Florida Driver License Handbook rev. 08/2023 (Drive copy, "HB"); FLHSMV pages. Bash access to statute sites is blocked by the proxy here; statutes were read with WebFetch.

## Insert changes

| Key | Change | Reason and source |
|---|---|---|
| hov | Rewritten. Old text taught HOV lanes for 2+ occupants and hybrid decals (form 83027). New text: no HOV lane rules any more, FLHSMV no longer issues HOV decals, former HOV lanes run as tolled express lanes, enter and leave only at marked openings. 83 words. | SB 1662 (2025) repealed FS 316.0741 effective 2025-07-01; FLHSMV stopped issuing, renewing and replacing HOV decals: https://www.flhsmv.gov/pdf/bulletins/2025/info25-010.pdf . Lanes now express lanes with dynamic tolls: https://www.wlrn.org/business/2025-07-03/hov-express-lanes-traffic-i95 ; https://www.wusf.org/politics-issues/2025-07-04/florida-hits-the-brakes-on-hov-lanes ; https://www.mysuncoast.com/2025/07/05/hov-lane-rules-changing-florida-interstates . Federal hybrid exemption also expired 2025-09-30: https://afdc.energy.gov/laws/5733 . FS 316.0741 no longer loads on m.flsenate.gov. |
| implied_consent | Added: a first refusal "is a second-degree misdemeanor". | Trenton's Law (HB 687, ch. 2025-121, effective 2025-10-01). FS 316.1939(1) (2026): "a misdemeanor of the second degree for a first refusal", first degree for second or later. https://m.flsenate.gov/Statutes/316.1939 |
| work_zone | "In a construction zone" became "In a construction zone with workers present" before "speeding fines are doubled". | FS 318.18(3)(e) (2026): doubled "only if construction personnel are present or operating equipment". https://m.flsenate.gov/Statutes/318.18 |

All inserts are 90 words or fewer (largest: school_bus and dui_penalties, 86). No em or en dashes.

## Inserts verified without change

| Key | Checked against |
|---|---|
| school_zone | FS 316.1895 limit max 20 mph; FS 318.18(3)(c) doubled; FS 316.306 handheld ban, moving, 3 points; HB pp. 28 to 29 (course, $1,000) |
| turn_on_red | FS 316.075(1)(c)1 (right on red, left one-way to one-way; the statute does not address red arrows); red arrow rule from HB p. 52 |
| move_over | FS 316.126(1)(b) (2026): covered vehicles incl. disabled vehicles (HB 425, 2023); vacate lane or slow; two-lane: 20 under when limit 25+, 5 mph when 20 or less |
| school_bus | FS 316.172(1), (2) (2026): both directions stop, wait until signal withdrawn; divided highway exception (unpaved 5 ft, raised median, barrier); no stopping distance. Penalties: FS 318.18(5) minimum civil penalty $200 / $400 plus $65 added under (5)(c) = $265 / $465 (matches HB p. 27 "minimum fine"); 4 points HB p. 30 |
| u_turn | HB pp. 63, 70 |
| speed_limits | FS 316.183(2) (30 / 55; minimum 40 on interstates, 50 when posted 70); HB p. 68 table (20 / 30 / 55 / 70); FS 316.1922 (50+ over or 100+ dangerously; first: up to 30 days, $500); points HB p. 30 |
| following_distance | HB p. 61 (four seconds), HB p. 62 (fire truck 500 ft); EXAM page "minimum following distance of four seconds" |
| parking_rules | FS 316.1945(1)(b), (1)(c)1 (15 / 20 / 20 / 30 / 50 ft); HB p. 65 (12 inches, keys) |
| bicycle_passing | FS 316.083(2), (3) (2026); HB p. 70 line rules ("may ... pass a bicyclist" across double solid yellow; brief left of center) |
| crash_reporting | FS 316.065(1) (2026): "apparent amount of at least $2,000" (SB 488 in force); FS 316.061(1), (2) |
| bac_limits | HB pp. 25 to 26; FS 322.2616 |
| dui_penalties | FS 316.193(2)(a), (4), (5), (6)(a) (2026): $500 to $1,000, 6 months; 0.15+ or minor: $1,000 to $2,000, 9 months; 50 hours; probation up to 1 year; DUI school. 180-day revocation and 75 years: HB pp. 26, 35. Open container: FS 316.1936 |
| phone_laws | FS 316.305 (2026; last amended 2022): texting while operating, first offense nonmoving, second within 5 years moving; stationary vehicle not operated; navigation allowed. FS 316.306: handheld ban in school crossing, school zone, work zone with workers present, 3 points. 2026 hands-free bill (SB 1152) did not become law (not in 2026 statutes) |
| seat_belts | FS 316.614(4), (5) (2026) |
| child_restraints | FS 316.613(1)(a) (2026; no change since 2020): 3 and younger carrier or integrated seat; 4 and 5 adds booster; belt exception for non-family favor, medical emergency, medical condition |
| vehicle_rules | PIP $10,000 and PDL $10,000 still required: 2026 repeal bills SB 522 and HB 769 died (https://www.vilesandbeckman.com/blog/did-florida-repeal-no-fault-insurance-the-pip-myths-and-the-facts-for-2026/ ; https://www.insurancejournal.com/news/southeast/2026/05/05/868507.htm). Rest HB pp. 12, 23, 37, 71 to 72 |
| road_test | EXAM page (maneuvers, four seconds, 100 ft, no passengers unless an interpreter is needed, random no-fee retest applies to knowledge and skills tests from third parties); FEES ($20) |
| supervised_hours | TEEN, FAQ, FS 322.1615(2) as logged in `sources.md` |
| signal_distance | FS 316.155(2), (4) (2026) |
| headlight_dimming | FS 316.238(1)(a), (b) (2026): 500 ft and 300 ft |

## Question fixes (bank/FL.json)

No wrong answer keys found in FL-043 to FL-142.

| ID | Old | New | Reason |
|---|---|---|---|
| FL-086 | "In Florida, which vehicles may use an HOV lane?" Key: 2+ occupants or decaled hybrids | "What happened to Florida's HOV lanes?" Key A: now express lanes with a toll that can change with traffic | HOV law repealed (SB 1662, 2025); old key is no longer the law |
| FL-087 | "Where may you enter or leave a Florida HOV lane?" Key: only at designated points | "Can a Florida driver still get an HOV decal for a hybrid car?" Key D: no, FLHSMV no longer issues HOV decals | Same; FLHSMV INFO 25-010 |
| FL-088 | "How is a Florida HOV lane usually marked?" Key: signs, diamonds, striped buffer | "Where may you enter or leave a Florida express lane?" Key B: only at marked openings | Same; taught in the new hov insert |
| FL-108 | Distractor C "Hazard lights while moving" | "Interior dome light only" | FS 316.2397(7) (2026) now allows flashing lights "during periods of extremely low visibility on roadways with a posted speed limit of 55 miles per hour or higher", so C was partly defensible |
| FL-113 | Explanation: one-year suspension only | Adds that a first refusal after a lawful DUI arrest is a second-degree misdemeanor; src adds FS 316.1939(1) | Trenton's Law (ch. 2025-121). Key unchanged |

All three HOV questions keep `quiz: false`; ch 7 still has 3 FL questions.

## Core text vs Florida law

No core sentence near an insert marker states something Florida law forbids. Points worth knowing:

1. `core/ch07.md` 7.9 describes HOV lanes generally ("most" framing, diamonds, HOV 2+). Florida no longer has them; the new hov insert says so right below. No core change needed.
2. `core/ch04.md` 4.7: "Stay stopped until the red lights go off, the stop arm folds in and the bus starts to move". FS 316.172(1)(a) only requires waiting "until the signal has been withdrawn". The core is stricter, not contrary; the insert and FL-065 give the legal rule. No change.
3. `core/ch11.md` 11.7: "most states ban all phone use, even hands-free, for new or teen drivers". Florida has no teen-specific phone ban (FS 316.305, 316.306). The phone_laws insert states Florida's rule (hands-free allowed), so a Florida reader gets the right answer. No change.

## Open items

- `state/FL/sources.md` still logs the old hov claim (HB p. 69, form 83027). Not edited here; checker A or the owner should replace that row with the SB 1662 sources above.
- The 08/2023 handbook (HB pp. 25, 26, 69) is out of date on HOV lanes and on the refusal crime. If a newer FLHSMV handbook is posted, recheck.
- Skills test following distance: HB p. 20 says "three to four seconds"; the current FLHSMV EXAM page says "minimum following distance of four seconds". Book uses four (newer source).
- EXAM page still allows "a language interpreter" during the skills test, while exams are now English only (ENG sources). road_test insert says "No passengers ride along"; left as is.
- Express lane entry and leaving "only at marked openings" rests on HB p. 69 (HOV buffer rule) and news reports; no current FDOT express lane rule page was read.
- Move Over penalties and the 316.193 amendment by ch. 2026-14 (content not described on the statute page) were not checked further; the first-offense DUI figures in the 2026 text match the insert.
