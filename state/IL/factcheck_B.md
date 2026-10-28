# Illinois fact check B (inserts + bank questions outside Chapter 1)

Checked 2026-10-28. Scope: `state/IL/inserts.md` (all 23 keys, each read in context in `core/chNN.md` and `core/95_driving_log.md`) and the 101 questions in `bank/IL.json` with ch 2 to 13 (IL-042 to IL-142). Chapter 1 questions were not touched.

Sources:
- **RR**: Illinois Rules of the Road 2026 (Drive file 1LeXtD-Oamm4hMi150EIXYUXOTtLaNo8H; text ends at RR p. 77)
- **ILCS**: 625 ILCS 5. ilga.gov returned robots or proxy blocks for most sections this session, so: 11-1414 and 11-907 read on https://www.ilga.gov/Documents/legislation/ilcs/documents/062500050K11-1414.htm and ...K11-907.htm; 11-306 read in P.A. 98-798 (https://witnessslips.ilga.gov/ftp/Public%20Acts/98/098-0798.htm); 11-605.1, 12-610.2, 11-501, 6-208, 6-208.1, 11-703 read on codes.findlaw.com (current as of 2025-01-01); 11-406 read on law.onecle.com/illinois/625ilcs5/11-406.html
- **AC**: 92 Ill. Adm. Code 1030.85, https://www.law.cornell.edu/regulations/illinois/Ill-Admin-Code-tit-92-SS-1030.85
- **ISBE**: https://www.isbe.net/Documents/bus_safety_motorist.pdf
- **MOTORIST**: Village of South Barrington, Illinois Motorist Report, https://southbarrington.org/traffic-safety/ (report to IDOT within 10 days; filed at motoristreport.illinois.gov)

## Insert changes

| Key | Change | Reason and source |
|---|---|---|
| crash_reporting | Added: "Within 10 days, also send a written crash report to the Illinois Department of Transportation." Trimmed two phrases to stay under 90 words ("stop safely"; "Not reporting: up to $2,500 and one year in jail"). | Omission of a legal duty: 11-406(a) requires the driver to file a written report with the Administrator (IDOT) within 10 days for death, injury or damage over $1,500 ($500 uninsured). ILCS 11-406 (onecle); MOTORIST. |
| school_bus | "(two each way)" became "(two each way, divided or not)". | STATE_BRIEF requires the divided highway rule. 11-1414(e) exempts oncoming traffic on any highway with 4 or more lanes and at least 2 each way; it does not depend on a median. A two-lane divided road gets no exemption. ILCS 11-1414(e). |
| dui_penalties | "is a Class A misdemeanor, and the conviction revokes" became "is a Class A misdemeanor and revokes". | Was 92 words (limit 90). No change of meaning. |
| road_test | "You may lose up to 36 points." became "You can lose up to 36 points and still pass." | Ambiguous (could read as the maximum deduction). AC 1030.85(g): 36 points allowed for Class D. |

Verified unchanged (source):
- school_zone: 20 mph, school days 6:30 a.m. to 4 p.m., children present; phone, crosswalk, full stop near school zone crosswalk; no passing (RR pp. 24 to 29).
- work_zone: posted limit 24/7 regardless of workers, lower when present; no passing; 2nd violation within 2 years with workers present: 90-day suspension (RR pp. 25, 29; 11-605.1(a), (a-5), (g)). Fines, not printed in the insert: minimum $250 first, $750 second (11-605.1(d)).
- turn_on_red: right on red, left one-way to one-way, and the same after a full stop on a steady red arrow ((c)(2) is "except as provided in paragraph 3"; (c)(3) covers any steady red) (11-306(c), P.A. 98-798; RR pp. 26, 77).
- move_over: lights blue, red, amber, white, green; non-adjacent lane on 4+ lanes with 2+ your way, else slow; $250 to $10,000 first; property damage suspension 90 days to 1 year, injury 180 days to 2 years, death 2 years (11-907(c), (d) to (g), current source notes P.A. 103-711, 104-131, 104-400, 104-417). Disabled vehicle with hazards on a four-lane highway: RR p. 45 (not in the 11-907 text read; RR says "Illinois law requires").
- school_bus: either direction, any road, private road, school property; may go when the bus moves, the driver signals or the lights stop; 3-month suspension, $300 fine (11-1414(a), (f), source note P.A. 102-859); no statutory distance; ISBE "at least 20 feet".
- speed_limits 70/65/55/30/15/20 (RR p. 24). signal_distance 100/200 ft, courtesy signal illegal (RR pp. 28, 30). headlight_dimming 500/300 ft (12-210). u_turn 500 ft (RR p. 32). parking_rules 15/20/30/50 ft, 12 inches (RR pp. 35 to 36). bicycle_passing 3 ft from the mirror; no-passing-zone conditions (RR p. 43; 11-703(d), (d-5)). following_distance (11-710; RR p. 42).
- bac_limits, implied_consent: 0.08, any trace under 21 (3 months), THC 5 ng/mL; 6 months fail, 12 months refuse, non-first offender 1 year and 3 years (6-208.1(a)(1) to (4); RR pp. 48 to 52).
- dui_penalties: Class A (11-501(c)(1)); 1 year, under 21 2 years, 2nd within 20 years 5 years (6-208(b); RR pp. 50, 52); 0.16+: $500 and 100 hours; child under 16: extra $1,000 minimum (11-501(c)). Note: `sources.md` labels these (c)(3) and (c)(4) the wrong way round; the 0.16 rule is (c)(4) and the child rule (c)(3).
- phone_laws: handheld, video, video conferencing, social media banned; hands-free or voice, single-sided headset; emergency, shoulder, stopped traffic in neutral or park; fines $75 to $150 (12-610.2(b) to (d); RR pp. 22, 25). Under 19 total ban: RR pp. 18 to 19.
- seat_belts, child_restraints: 8+ all seats; under 8 restraint; booster with lap and shoulder belt; 40 lb lap belt exception; rear-facing under 2 unless over 40 lb or 40 in (RR pp. 23 to 24).
- vehicle_rules: 25/50/20; 3-month suspension; headlights; 75 ft sound; 10-day address change (RR pp. 6, 21, 36, 55; 12-201(b)).
- road_test, supervised_hours: RR pp. 14 to 16; AC 1030.85(g), (h).

## Core text vs Illinois law

No core sentence contradicts Illinois law. Two soft points, left for the core owner:
- core/ch09.md 9.2: "many states let or require you to enter it [the bike lane] just before a right turn". RR p. 43: in Illinois, vehicles may not drive, park, idle or drop off in a bike lane even when no cyclist is present. The core hedges with "many states" and the IL insert says "Never drive, park or stop in a bike lane", so the reader gets the IL rule. Watch for a core quiz question keyed to entering the bike lane.
- core/ch04.md 4.7: "Stay stopped until the red lights go off, the stop arm folds in and the bus starts to move". Illinois (11-1414(a)) lets you go when any one of these happens: the bus moves, the driver signals, or the lights stop. The core is stricter, not unsafe, and the insert states the IL rule.

## Bank changes (non-ch-1 only)

| ID | Field | Old | New | Reason |
|---|---|---|---|---|
| IL-060 | src | core Chapter 2; FHWA MUTCD 11th ed. 2D; core Chapter 2 | core Chapter 2; FHWA MUTCD 11th ed. 2D | Duplicate citation |
| IL-093 | src | Illinois DOT Kennedy Expressway project news (timeout.com, 2024-12-17) | IDOT, reported by WTTW News, 2024-12-17 and 2025-01-09 (news.wttw.com) | Old source was a Time Out blog credited to IDOT; WTTW quotes IDOT on reversible lane operation |

No wrong answer keys. Every ch 2 to 13 question has one defensible answer that matches RR, statute or MUTCD. Sign descriptions IL-042 to IL-060 match the MUTCD and RR Chapter 9 (octagon stop; red-bordered downward triangle yield; round yellow RR advance warning; pennant on the left; pentagon school; orange work zone; fluorescent pink incident; yellow diamond warning; blue services; brown recreation; white rectangle regulatory; red WRONG WAY; square yellow advisory plaque; Lane Ends; Divided Highway Ends; SLOW paddle; arrow board; barricade stripes slope down toward the side to pass; odd Interstates north and south).

## Checks

- `python3 tools/check_bank.py bank/core.json bank/IL.json`: BANK PASSED (IL 142 questions).
- `python3 tools/originality_check.py check state/IL/inserts.md`: ORIGINALITY PASSED (0.18 percent, no 12-word runs).
- Inserts: all 90 words or fewer (largest: school_bus 89, dui_penalties 89); no em or en dashes; no years.

## Open items

- RR pp. 78 to 106 not in the Drive text: the RR general following distance advice (p. 83) was not read. The insert gives only the statute (no fixed seconds) and the motorcycle figure.
- Current official text of 11-605.1, 12-610.2, 11-501, 6-208 and 11-406 was read on FindLaw or Onecle (ilga.gov blocked). FindLaw is current to 2025-01-01. A 2025 or 2026 amendment would not show there.
- 11-406: the Onecle copy may be older. MOTORIST confirms the 10-day IDOT report is still in use, but whether it is still required when police already took a report was not confirmed. The insert does not claim an exception.
- Disabled vehicle Move Over duty (RR p. 45): the statute section that carries it was not found in the 11-907 text read.
