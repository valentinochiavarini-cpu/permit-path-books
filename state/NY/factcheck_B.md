# New York fact check B (inserts + bank questions ch 2 to 13)

Checked 2026-10-28 by an independent checker. Scope: `state/NY/inserts.md` (all 23 keys, read in context of their `{{INSERT:key}}` markers in `core/`) and the 113 questions in `bank/NY.json` with ch 2 to 13 (including the 26 ch 2 sign questions). Ch 1 questions were not touched.

Sources: NY Driver's Manual MV-21 (Drive file 1ltO6DCUT3mMDRSa7gG2yLBbuOIvKKNkD; same 230,663-character text as the writer's copy), NY VTL on nysenate.gov (1144-a, 1174, 1180, 1122-a), dmv.ny.gov via WebFetch (point system page, Feb 16, 2026 point values news release, road test page, road test scoring summary), FHWA MUTCD 11th edition table of contents (https://mutcd-dr.fhwa.dot.gov/pdfs/11th_Edition/11thcovtoc.pdf), Chapter 2D (https://mutcd.fhwa.dot.gov/pdfs/11th_Edition/Chapter2d.pdf) and Part 7B text (https://www.mutcd.fyi/11r1/part-7b-signs/). The direct MUTCD PDF could not be downloaded (proxy 403).

## Result

No wrong answer keys and no legal errors found in the inserts or the ch 2 to 13 questions. Every focus item checked out:

| Topic | Book says | Verified against |
|---|---|---|
| Turn on red | Right on red after stop; left on red one-way to one-way; none on a red arrow; none in NYC unless a sign allows | MAN Ch. 4, Traffic Lights |
| School bus | Both directions, all roads, opposite side of divided highway, school lots; at least 20 ft (manual advice); 8 points; $250 to $400 first, up to $1,500 third in 3 years; revocation 6+ months after 3 in 3 years | VTL 1174(a), (c) (third: $750 to $1,500); MAN Ch. 6 and Ch. 2; POINTS. Note: the manual's "$1,000 maximum" is outdated; the statute says $1,500. |
| Move over | Due care and slow down on all roads; lane change on parkways and controlled-access highways; any stopped vehicle there; moving violation | VTL 1144-a(a) to (d); MAN Ch. 5, Move Over Law |
| DWI / DWAI / zero tolerance | 0.05 / 0.08 / 0.18; 0.02 to 0.07 under 21; 6-month suspension, $125 + $100; first offense table; interlock 12 months; Leandra's Law felony | MAN Ch. 9 table and text; Ch. 2 |
| Refusal | Suspended at arraignment; revoked after DMV hearing; 1 year + $500; 18 months + $750; under 21 second | MAN Ch. 9, Chemical Tests; Ch. 2 |
| Open container | Driver or passenger may not drink, hold open alcohol or use cannabis; limousine passenger exemption | MAN Ch. 9, Open Container Law |
| Phone | Hand-held and device ban; hands-free allowed; 5 points; $200 / $250 / $450 within 18 months; junior and probationary 120 days | MAN Ch. 8; POINTS |
| Seat belts | Primary; driver and all 16+ any seat, up to $50; driver liable for under 16, $25 to $100 and 3 points | MAN Ch. 8; POINTS |
| Child restraints | Under 4 seat; rear-facing to 2; 4 to 7 booster with lap and shoulder belt; 4 ft 9 in or 100 lb exception | MAN Ch. 8 |
| Speed | 55 unposted; NYC 25; up to 65 posted on some rural expressways; points 3/4/6/8/11; 11 points in 24 months | MAN Ch. 8, Ch. 10; POINTS; news release (effective Feb 16, 2026, look-back 18 to 24 months) |
| Work zone | 25 mph minimum posted limit; minimum fines double ($90/$180/$360), no workers needed; 8 points | VTL 1180(f), (h)(3); MAN Ch. 4, Ch. 8; POINTS |
| Headlights | Low beams 500 ft oncoming, 200 ft following; half hour rule, 1,000 ft, wipers | MAN Ch. 10 |
| Signal | 100 ft before turn, lane change, exit ramp | MAN Ch. 5, Ch. 6, Ch. 10 |
| Crash report | MV-104 within 10 days, injury, death or $1,000 to one person's property; misdemeanor | MAN Ch. 12; VTL 600 |
| HOV | Diamond; occupancy rule during posted times; broken line lets drivers enter to turn right | MAN Ch. 4 |
| U-turns | Left part of lane nearest center line; 500 ft; NYC business districts; limited access expressway; school zone; green arrow | MAN Ch. 5 |
| Bicycle passing | Safe distance on the left, no fixed footage | VTL 1122-a (last revised 2014-09-22; no 3-foot law enacted) |
| Road test | Scored groups, ADAS limits, only accompanying driver, results after 6 p.m., 14 days, fees after 2 fails | ROAD; SCORE; MAN Ch. 13 |

## Insert changes

| Key | Old | New | Reason / source |
|---|---|---|---|
| school_zone | "during the posted hours, generally 7 a.m. to 6 p.m." | "at the times on the sign, which fall between 7 a.m. and 6 p.m." | VTL 1180(c): times are those on the sign and must fall within 7 a.m. to 6 p.m.; "generally" implied a default window. https://www.nysenate.gov/legislation/laws/VAT/1180 |
| dui_penalties | (first offense table only, adult penalties) | Added: "Under 21, any alcohol or drug driving conviction revokes your license for at least one year." | The table showed DWAI 90 days and DWI 6 months, which are wrong for the book's teen readers. MAN Ch. 2, Drivers Under Age 21 ("minimum one-year revocation"); MAN Ch. 9 table note "License actions for those under age 21 are different." Insert now 88 words. |

All 23 inserts are 90 words or fewer, with no em or en dashes and no years.

## Question fixes (bank/NY.json)

| ID | Field | Old | New | Reason |
|---|---|---|---|---|
| NY-054 | src | MUTCD Sec. 2A.11 | MUTCD Sections 2A.05 and 2B.04 | 2A.05 is Shapes, 2B.04 is the STOP sign (11th ed. TOC). |
| NY-055 | src | MUTCD Sec. 2C.50 | MUTCD Sections 2A.05, 7B.01 and 7B.02 | School signs are in Part 7B (7B.01 color, 7B.02 S1-1 uses). |
| NY-055 | exp | "The five-sided pentagon is reserved for school signs." | "Among warning signs, the five-sided pentagon in fluorescent yellow-green means a school zone or school crossing." | MUTCD 2A.05 also uses the pentagon for the County Route sign, so "reserved for school signs" was not exact. |
| NY-057 | src | MUTCD Sec. 2C.45 | MUTCD Sec. 2C.53 | No Passing Zone sign (W14-3) is 2C.53 in the 11th ed. |
| NY-059 | src | MUTCD Sec. 2D.10 | MUTCD Sec. 2D.11 | Design of Route Signs (incl. Interstate M1-1) is 2D.11. |
| NY-060 | src | MUTCD Sec. 2A.10 | MUTCD Section 2A.06 and Table 2A-2 | Colors are 2A.06. |
| NY-061 | src | MUTCD Sec. 7B.12 | MUTCD Sections 7B.02 and 7B.03 | School Crossing assembly with W16-7P plaque is 7B.02/7B.03. |
| NY-062 | src | (manual only) | added MUTCD Sec. 2B.28 | Mandatory movement lane-use signs (ONLY). |
| NY-063 | exp | "generally 7 a.m. to 6 p.m." | "at the times on the sign, which fall between 7 a.m. and 6 p.m." | Matches VTL 1180(c) and the corrected insert. |
| NY-101 | b (key) | "Only when the signs show the restriction is not in effect" | "When the signs show the restriction is not in effect" | "Only" made the keyed answer false: on city streets a non-HOV car may enter at a broken line to turn right (MAN Ch. 4, Diamond Symbol; NY-102). Key unchanged. |
| NY-133 | a (key) | "No driver or passenger, except in vehicles such as licensed limousines" | "No driver, and no passenger except in vehicles such as licensed limousines" | The limousine exemption covers passengers only (MAN Ch. 9, Open Container Law). Key unchanged. |

All 26 ch 2 sign descriptions were checked against MUTCD 11th ed. and MAN Ch. 4: colors and shapes are correct (yield: red and white with red letters; regulation white rectangles; warning yellow diamonds; orange work; green destination; blue services; brown recreation 2A.06; octagon STOP only; pentagon school in fluorescent yellow-green 7B.01; pennant on the left for no passing; round yellow RR advance sign; yellow and black advisory speed plaque 2C.59; Interstate red and blue shield 2D.11 / Standard Highway Signs).

## Core text vs New York law (not edited: outside scope)

1. **core/ch03.md, Turning on Red**: "Every state lets you turn right on a steady red light after a complete stop, unless a sign says NO TURN ON RED." In New York City no turn on red is allowed unless a sign permits it (MAN Ch. 4, Traffic Lights). The core's "Some cities and states add limits" and the NY insert cover it, but the first sentence reads as absolute. Suggest "Almost everywhere you may turn right..." or "Every state, outside a few cities, lets you...".
2. **core/ch04.md, Move Over**: the core says you must move over or, if you cannot, slow down. In New York the lane change is required only on parkways, interstates and other controlled-access highways; on other roads the duty is due care and reduced speed (VTL 1144-a; MAN Ch. 5). The NY insert states this correctly, so no reader harm; the core wording is the general rule and does not need a change unless the core checker wants "where your state requires it".
3. **core/ch09.md**: "Most states set a minimum of at least 3 feet" is true nationally; New York has no fixed distance (VTL 1122-a), stated in the insert. No conflict.
4. **core/ch11.md**: "most states ban all phone use, even hands-free, for new or teen drivers." New York does not; the manual says a driver can use a hands-free phone at any time. The insert says hands-free calling is allowed. No conflict.

## Open items

1. **NY-071** (school bus with students may not turn right on any red) and **NY-117** (passenger or owner may file the MV-104 for an injured driver) are correct per MAN (Ch. 4 Traffic Lights; Ch. 12 Reports to DMV) but neither fact is taught in core Ch. 3 / Ch. 10 or the NY inserts. Fine for the app; do not use them in printed quizzes or mocks unless the text is extended.
2. The MV-21 copy predates the Feb 16, 2026 point changes and still prints a $1,000 maximum school bus fine; the book follows VTL 1174(c) ($1,500) and the current DMV point table.
3. NYC Sammy's Law lets the city post lower limits in some areas; the unposted NYC limit stays 25 mph. Not mentioned in the book (correctly).
