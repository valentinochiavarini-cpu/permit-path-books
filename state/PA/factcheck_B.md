# Pennsylvania fact check B: inserts and chapter 2 to 13 questions

Checked 2026-10-27. Scope: `state/PA/inserts.md` (all 21 keys) and every `bank/PA.json` question with `ch` other than 1 (PA-042 to PA-139, 98 questions). Each insert was also read in place in `core/chNN.md` around its marker.

Sources:
- **STAT n**: 75 Pa.C.S. section n on palegis.us, `https://www.palegis.us/statutes/consolidated/view-statute?txtType=PDF&ttl=75&div=00.&chpt=0NN.&sctn=0NN.&subsctn=000.` (read: 1535, 3112, 3303, 3307, 3316, 3316.1, 3326, 3327, 3332, 3345, 3353, 3362, 3369, 3805, 4302, 4581, 1786; 3809 is in Title 75 chapter 38)
- **PUB 95**: PA Driver's Manual PUB 95 (4-21), Drive copy 1MZi7_SLlRizXTi9Fzi_KXhzv4dk9RkyU
- **ONLINE-4**: https://www.pa.gov/agencies/dmv/driver-services/pennsylvania-drivers-manual/online-drivers-manual/pennsylvanias-point-system
- **ONLINE-5**: https://www.pa.gov/agencies/dmv/driver-services/pennsylvania-drivers-manual/online-drivers-manual/chapter-5-laws-and-related-issues
- **ONLINE-3SC**: https://www.pa.gov/agencies/dmv/driver-services/pennsylvania-drivers-manual/online-drivers-manual/special-circumstances-and-emergencies
- **ONLINE-2SIG**: https://www.pa.gov/agencies/dmv/driver-services/pennsylvania-drivers-manual/online-drivers-manual/signals
- **ACT81**: https://www.pa.gov/agencies/dmv/resources/laws-and-regulations/act-81-of-2011

## Changes to inserts.md

| Key | Change | Reason | Source |
|---|---|---|---|
| work_zone | "Injuring a worker" to "Seriously injuring a worker" | The 6-month suspension is for serious bodily injury only | STAT 3326(c.3) |
| move_over | "Injuring or killing someone" to "Seriously injuring or killing someone" | Suspensions in (b.1) are for serious bodily injury or death; plain bodily injury carries only a fine up to $1,000 | STAT 3327(b.1), (b.2) |
| school_bus | Added: "A wave from the bus driver does not let you go while the red lights still flash." | Core ch04 line 128 says you may go when "the bus driver or a police officer signals you to go"; in PA you stay stopped until the red lights stop flashing (and PA-063 keys the driver's wave as wrong). The insert now states the PA rule in context | STAT 3345(a); PUB 95 p. 58 |
| speed_limits | Added the speeding point schedule (2, 3, 4, 5 points) | PA-074 (ch 6) was not taught in Chapter 6 | STAT 1535(a) |
| parking_rules | Added disability space fine $50 to $200 and towing | PA-090 (ch 8) was not taught in Chapter 8 (core only says "Fines are high") | ONLINE-5 |
| vehicle_rules | "and so is the license of anyone who drove it" to "and so is your license if you drove the car or let someone else drive it" | Statute suspends the owner or registrant who operated or permitted operation, not any driver | STAT 1786(d)(1); ONLINE-4 |
| road_test | Fail list now "touching a pole, crossing the line or going up onto the curb"; added examiner as only passenger, self-parking off, license the same day at a PennDOT center | Core ch13 line 91 promises "the box below says who may ride in yours" and the insert did not; PA-134, PA-135, PA-136 (ch 13) were not taught in Chapter 13 | PUB 95 pp. 5 to 6 |

## Inserts verified without change

| Key | Verified against |
|---|---|
| school_zone | 15 mph flashing or posted times, 3 points: PUB 95 p. 9; STAT 1535(a) (3365(b)) |
| work_zone | Headlights in all posted work zones, DRL not enough: PUB 95 pp. 18, 54; ONLINE-3SC. Doubled fines in posted active zone: STAT 3326(c), (c.1). 15 days at 11+ over: STAT 1535(e). Cameras 11+ over, warning, $75, $150, no points, only when active: STAT 3369(c), (e) (sunset deleted) |
| turn_on_red | Right on red and one-way to one-way left on red: STAT 3112(a)(3)(ii); PUB 95 p. 45. Red arrow: see open items |
| move_over | Nonadjacent lane or at least 20 mph under limit; disabled vehicle with 2 of hazard lamps, flares, signs: STAT 3327(a), (a.1), (c)(2), (f). Fines $500, $1,000, $2,000: STAT 3327(b); PUB 95 p. 59. 2 points: STAT 1535(a); PUB 95 p. 59. Up to $10,000 for death: STAT 3327(b.2), (b.3). Responder list incl. tow and road crews: PUB 95 p. 59 |
| school_bus | 10 feet, behind, oncoming, intersection: STAT 3345(a); divided highway: 3345(g); amber: 3345(b); $250: 3345(j); 5 points and 60 days: STAT 1535(a) |
| u_turn | Safe and no interference, 500 ft visibility on curves and crests: STAT 3332; PUB 95 p. 45 |
| speed_limits | 35, 25 (local, non-numbered, residence), 55, 65 or 70: STAT 3362(a); 70 max: PUB 95 p. 39 |
| following_distance | 4 s dry, 5 to 10 mph slower and 5 or 6 s wet, double in work zones, 4 s trucks and motorcycles: PUB 95 pp. 35, 41, 54, 56, 57; ONLINE-3SC |
| hov | Reversible, Downtown to North Hills, inbound mornings, outbound evenings: en.wikipedia.org/wiki/Interstate_279; otmapgh.org (PennDOT notice, 2011). See open items |
| parking_rules | 15, 20, 20, 30, 50 ft: STAT 3353(a)(2), (a)(3); PUB 95 p. 53. 12 inches: PUB 95 p. 53 |
| bicycle_passing | 4 ft: STAT 3303(a)(3); crossing a no-passing line to pass a bicycle allowed: STAT 3307(b.1); ONLINE-5 |
| crash_reporting | ONLINE-4 (Crashes), all points match |
| bac_limits | 0.08, 0.04 commercial, 0.02 under 21 and school bus; underage rules: ONLINE-4 |
| implied_consent | 1 year, 18 months, highest tier, $653: ONLINE-4; interlock on restoration: STAT 3805(a) (exemption in (a.2) for a first offender who certifies they will not drive; not worth printing) |
| dui_penalties | ONLINE-4 tables; open container: STAT 3809 |
| phone_laws | STAT 3316 ($50, in motion, emergency); STAT 3316.1 ($50, includes temporarily stationary at traffic or signal, emergency) |
| seat_belts | STAT 4581(a)(2), (a)(3), (b); ACT81 (under 18 is a primary offense) |
| child_restraints | STAT 4581(a)(1), (1.1), (b) ($75) |
| vehicle_rules | 12 months, 90 days early, 15 days: ONLINE-5; wipers: STAT 4302(a)(3); PUB 95 p. 43 |
| supervised_hours | PUB 95 pp. 1 to 3, 5; STAT 1505 |

## Question fixes

None. All 98 keys are correct and each has one defensible answer against the sources above. `python3 tools/check_bank.py bank/PA.json`: BANK PASSED (139 questions, A 35, B 35, C 35, D 34). The bank was not written to.

## Writer's open items

1. **Move Over fines.** Statute 3327(b) (current text on palegis.us) and PUB 95 p. 59 both say up to $500, $1,000, $2,000. ONLINE-3SC says $250, $500, $1,000 and is outdated. Insert and PA-057 follow the statute. Resolved.
2. **Seat belt under 18.** Resolved: ACT81 (PennDOT) states a belt violation by a driver or passenger under 18 is a primary offense. 4581(b) limits the "other violation" condition to (a)(2)(ii), which excludes children under 18.
3. **I-279 HOV occupancy.** Not resolved. TribLive (2023) reports PennDOT lifted HOV 2+ outbound only temporarily, with inbound still HOV 2+; the 2011 PennDOT notice gives HOV 2+ weekdays 6 to 9 a.m. and 3 to 7 p.m., outbound open to all on weekends. PennDOT's own HOV page did not render, and a long-term closure of the southbound crossovers began June 2025 for pier repairs. Keeping the insert free of an occupancy figure is correct; it does not contradict core ch07 (which describes HOV 2+ generically).
4. **Red arrow turns.** STAT 3112 is silent on red arrows. Both PennDOT sources (PUB 95 p. 7 and ONLINE-2SIG, current) say "The same turns-on-red that are allowed for a steady red signal are allowed for a steady red arrow." Insert and PA-052 follow the manual, which is what the test draws on. Fits core ch03 line 82, which defers to the state box. Accept.

## Unresolved, for the writer or the core checker

- **Core ch04 line 128 (core scope, not edited).** "or until the bus driver or a police officer signals you to go" contradicts PA law and PA-063 option D. The PA insert now says so, but the core sentence should drop "the bus driver" or say "a police officer". Flag to the core checker.
- **PA-094 (ch 9, open-bed truck 35 mph).** Not taught in Chapter 9 or any insert, and core ch12 line 111 says never let a passenger ride in the cargo area of a pickup. Suggest deleting the question or moving the fact into an insert.
- **PA-099 (ch 10, headlights with wipers).** The PA rule is taught in the ch12 vehicle_rules insert, not in Chapter 10 (core ch10 says "many states"). Suggest changing `ch` to 12.
- **PA-137, PA-138, PA-139 (ch 13).** Road test documents, 3-year restart and 6-month booking are taught in state ch01, not Chapter 13. PA-137 is covered by core ch13 (registration and insurance). For PA-138 and PA-139, either change `ch` to 1 or accept them as review questions.
- **PA-109.** ONLINE-4 lists Alcohol Highway Safety School for first or second offense; the "every level" wording is the writer's reading of the tables. Low risk.
- Blocked URL: lehighvalleypublicmedia.org Road Scholar article on red arrows (permission not answered); not needed.

## Checks run

- `python3 tools/originality_check.py check state/PA/inserts.md`: ORIGINALITY PASSED (1 shared sequence of 1993, 0 copied runs)
- `python3 tools/check_bank.py bank/PA.json`: BANK PASSED
- No em or en dashes in inserts.md or this file.
