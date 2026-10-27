# Fact check C: core chapters 3, 4 and 5

Checked 2026-10-27. Scope: `core/ch03.md`, `core/ch04.md`, `core/ch05.md` and bank IDs C03-*, C04-*, C05-* in `bank/core.json`.

Access note: direct downloads from mutcd.fhwa.dot.gov were blocked by the proxy, so the 11th Edition PDFs were read through the web fetch tool, which returns only part of each PDF. Where a federal section was not reached, the California MUTCD 2026 Edition was used. It is FHWA's 2023 (11th) Edition as amended for California and keeps the federal section numbers; none of the cited paragraphs are marked as California changes. eCFR and govinfo pages for 49 CFR could not be opened (permission timeout); Cornell LII was used for 49 CFR 392.10.

## Open items from the chapter notes: resolved

| Item | Finding | Source |
|---|---|---|
| Lane control signal meanings, 11th Edition section | Chapter 4T, Section 4T.02: steady downward green arrow = lane open; steady yellow X = lane about to close, followed by red X; steady red X = lane closed; white two way left turn arrow = left turns from either direction only. Signal faces are rectangular (4T.03). No flashing yellow X exists in the federal MUTCD (2003 4J.02, 2009 4M.02 or 11th 4T.02). Its "left turn only" meaning comes from state manuals (New York). | https://dot.ca.gov/-/media/dot-media/programs/safety-programs/documents/ca-mutcd/2026/2026-camutcd-2026-4t-a11y.pdf ; https://mutcd.fhwa.dot.gov/htm/2009/part4/part4m.htm ; https://dmv.ny.gov/new-york-state-drivers-manual-practice-tests/chapter-4-traffic-control |
| Signal light order | Confirmed. Vertical: red on top, yellow above green (4E.04). Horizontal: red on the left (4E.05). | https://mutcd.fhwa.dot.gov/pdfs/11th_Edition/part4.pdf |
| Pedestrian signal colors | Confirmed. WALKING PERSON white, UPRAISED HAND Portland orange (4I.02). Countdown shows seconds left in the pedestrian change interval, only while the hand flashes (4I.04). | https://dot.ca.gov/-/media/dot-media/programs/safety-programs/documents/ca-mutcd/2026/2026-camutcd-2026-4i-a11y.pdf |
| Ramp meters | Chapter 4P. Two section (red, green) or three section (red, yellow, green) faces; may be dark when not in use; signs state "XX VEHICLE(S) PER GREEN". PA manual: one car per green on single lane ramps. Text is correct. | https://dot.ca.gov/-/media/dot-media/programs/safety-programs/documents/ca-mutcd/2026/2026-camutcd-2026-4p-a11y.pdf ; PA Driver's Manual PUB 95, Chapter 2 |
| Hand signals | Confirmed: left arm straight out = left; bent up = right; bent down = slow or stop. | https://dmv.ny.gov/new-york-state-drivers-manual-practice-tests/chapter-5-intersections-and-turns ; PA PUB 95, Chapter 3 |
| Railroad stop distance | 49 CFR 392.10: within 50 feet, not closer than 15 feet. MUTCD 8C.03: stop line no closer than 15 feet from nearest rail. "Most states" wording kept; not checked against all 15 target state statutes. | https://www.law.cornell.edu/cfr/text/49/392.10 ; https://mutcd.fhwa.dot.gov/pdfs/11th_Edition/part8.pdf |
| 49 CFR 392.10 vehicles | Applies to commercial motor vehicles: every bus carrying passengers, placarded hazmat, chlorine, cargo tanks (loaded or empty) and others. Does not name school buses (school bus stops come from state law). Exceptions exist (officer or flagger, green traffic signal, exempt and abandoned crossings, streetcar tracks in business districts). Also bars shifting gears on the tracks. Text changed from "every crossing" to "almost every crossing". | https://www.law.cornell.edu/cfr/text/49/392.10 |
| Train overhang | "Trains can overhang the tracks by three feet on either side" (Genesee and Wyoming, Operation Lifesaver partner page). Text kept. | https://www.gwrr.com/about/community-involvement/operation-lifesaver |
| Roundabout truck aprons | Confirmed: raised concrete around the central island for large vehicles' rear wheels; trucks may straddle both lanes; give them room, avoid driving beside them. | https://dot.state.mn.us/roundabouts/oversize.html ; https://wisconsindot.gov/Documents/dmv/shared/rab-brochure.pdf ; FHWA-SA-14-098 https://highways.dot.gov/sites/fhwa.dot.gov/files/2022-06/fhwasa14098.pdf |
| Emergency vehicles in roundabouts | Confirmed: if inside, continue to your exit, leave, then pull over; if not yet entered, pull over; never stop inside. | Wisconsin DOT brochure (above); PA PUB 95, Chapter 3 (circular intersections) |
| Other notes items | Dark signal = all way stop (NY Ch 4, CA handbook, PA). Officer overrides signals (NY Ch 4). Turn on red default and left on red one way to one way (MUTCD 4A.03). Flashing red arrow = stop then turn (4A.04). Steady red arrow: CA forbids turning, PA allows the same turns on red as a red ball, so "states differ" is correct. Line colors and patterns (3A.03, 3A.04, 3B.01, 3B.04, 3B.05, 3B.06, 3B.09, 3B.19). Freight train at 55 mph a mile or more; 45 degree angle; ENS sign blue with white legend, phone number and USDOT crossing number (8B.27); flashing lights two red lights alternating (8D.02); gates red and white striped (8D.03). Move Over all 50 states, 19 states plus DC for any hazard lights (NHTSA). School bus lights and resume conditions (NHTSA). | URLs in the chapter notes; https://www.nhtsa.gov/move-over-its-law ; https://www.nhtsa.gov/road-safety/school-bus-safety |

## Text changes

| File | Old | New | Reason and source |
|---|---|---|---|
| ch03.md 3.6 | "They are square lights" | "They are rectangular signals" | MUTCD 11th 4T.03: rectangular signal faces. |
| ch03.md 3.6 table | "Flashing yellow X: Use this lane only to turn left" | Added row "White two way left turn arrow"; flashing yellow X row now "(some states only)" | Flashing yellow X is not in the MUTCD (4T.02); white two way left turn arrow is. |
| ch03.md 3.9 | "You may cross it only to turn left into or out of a driveway..." | "You may cross it to turn left ...; ... and some let you cross it to pass a bicycle when the way is clear." | "Only" was too absolute. PA 75 Pa.C.S. 3307(b.1) allows passing a pedalcycle in a no-passing zone with due care (PennDOT PUB 380, https://www.bikemap.pitt.edu/sites/default/files/pub_380.pdf). |
| ch03.md 3.10 | "white arrows ... are painted on the pavement" | "... are usually painted on the pavement" | MUTCD 3B.05: the two way left turn arrows are Guidance ("should"), not a Standard. |
| ch04.md 4.3 | "a plaque ... that reads ALL WAY or 4-WAY" | "reads ALL WAY (older signs may say 4-WAY)" | MUTCD 2B.05: ALL WAY plaque required; 2-WAY, 3-WAY, 4-WAY plaques "shall not be used" (https://mutcd.fhwa.dot.gov/htm/2009/part2/part2b.htm). |
| ch04.md 4.6 | "On a one way street, pull to the nearest edge." | "pull to the right edge unless your state lets you use the nearest edge, as some states do." | Varies: New York VTL 1144 allows either edge only on one way roads of 3 or more lanes (https://www.nysenate.gov/legislation/laws/VAT/1144); Minnesota 169.20 says closest edge (https://www.revisor.mn.gov/bills/80/1997/0/HF/225/versions/latest). |
| ch04.md 4.7 | "or until the bus driver or a police officer signals you to go" | "or until a police officer, or in some states the bus driver, signals you to go" | NHTSA gives only lights off, arm in, bus moving. Driver wave-on is state law, not universal. |
| ch04.md Quick Review | "...until it moves or the driver signals." | "...until the lights go off, the arm folds in and the bus moves." | Same reason. |
| ch05.md 5.2 | "many states let you, or even require you to, move into the bike lane" | "some states let you..." | Only California's 200 foot rule verified; "many" not supported. |
| ch05.md 5.9 | "must stop at every crossing" | "must stop at almost every crossing" | 49 CFR 392.10 exceptions (officer, green signal, exempt and abandoned crossings). |

## Question fixes (bank/core.json)

| ID | Field | Old | New | Reason |
|---|---|---|---|---|
| C03-023 | d | "To pass a bicycle on a hill" | "To pass a line of cars on a hill" | Some states allow crossing a double yellow to pass a bicycle; the distractor could be argued correct. |
| C04-022 | c (key) | "When the red lights stop, the arm folds in and the bus moves, or the driver signals you on" | "When the red lights stop, the arm folds in and the bus starts moving" | Driver wave-on is not a national rule (NHTSA). |
| C04-022 | exp | mentions driver or officer | "Stay stopped until the red lights stop flashing, the stop arm is drawn back and the bus begins moving. A police officer may also wave you on." | Matches NHTSA wording. |
| C04-029 | q, d (key), exp, src | Keyed "To the nearest edge of the street", cited generic manuals | Stem reworded; key "To the right edge, or to the nearest edge where your state allows it"; exp and src cite NY VTL 1144 and MN 169.20 | Old key was wrong in states such as New York (right edge unless 3 or more lanes). |
| C03-009 | src | "California Driver Handbook, Traffic Control" | "...Laws and Rules of the Road (traffic signals)" | Correct section name. |
| C03-012, C03-013, C03-014 | src | MUTCD 2009 4M.02 | adds MUTCD 11th ed. 4T.02 | Current edition citation. |
| C03-015 | src | MUTCD 11th 4A.01 | MUTCD 11th Chapter 4P | Correct chapter. |
| C03-018 | src | CA handbook only | adds MUTCD 11th 4I.04 | Primary source. |
| C04-024 | src | NHTSA only | adds 49 CFR 571.131 (FMVSS 131) | NHTSA page does not describe the arm shape or side. |
| C05-010 | src | MUTCD 3B.23 only | adds PA PUB 95 (dual left turn lanes) | 3B.23 covers arrows, not the stay-in-lane rule. |
| C05-022 | src | "Official state driver manuals" | MnDOT, WisDOT, FHWA-SA-14-098 | Specific sources. |
| C05-023, C05-024, C05-025 | src | "Official state driver manuals" | NY Ch 5 and PA PUB 95 | Specific sources. |
| C05-026 | src | adds 49 CFR 392.10 | | 15 to 50 foot rule. |
| C05-029 | src | 8B.27 and 8C.03 | 8B.27 | 8C.03 is the stop line section, not ENS. |
| C05-030 | src | Operation Lifesaver only | adds PA PUB 95 (railroad crossings) | The OLI page does not cover the second train rule. |

All other C03, C04 and C05 keys checked: one defensible answer each, taught in the chapter, no contradiction with the text.

`python3 tools/check_bank.py bank/core.json`: BANK PASSED. `python3 tools/originality_check.py check` on ch03, ch04, ch05: PASSED (0.18 percent, no 12 word runs).

## Unresolved

- FMVSS 131 (49 CFR 571.131) text for the stop arm (red octagon, left side) could not be opened (eCFR and govinfo blocked). It is standard equipment and stated in every state manual; confirm on eCFR when reachable.
- Railroad 15 to 50 feet not checked against each of the 15 target state statutes; text says "most states".
- Funeral procession and transit bus yield rules remain "many states" and "some states" without a state count.
- Flashing yellow X: kept as "some states only". If no target state manual uses it, consider removing the row; no question tests it.
- Signal distance before turns (100 feet in NY and PA under 35 mph, 300 feet at 35 mph or more in PA) still has no insert key; the text gives no number, which is safe.
