# Core polish after the PA v2 coverage audit (2026-10-28)

Input: `qa/coverage_PA_v2.md` (sections 4 to 7). Scope: core/*.md, bank/core.json, layout/fig/. No state files touched.

## 1. Core sentences that clashed with state boxes

| Where | Change |
|---|---|
| 4.7 | "Stay stopped until the red lights stop flashing and the stop arm is folded." The police officer and bus driver wave is now a `[[generic]]` sentence that points to the box. |
| Ch 4 Quick Review | Dropped "and the bus moves". |
| 11.4 | "These offenses carry penalties even when no car is involved; the box below gives your state's penalties." License loss is now a `[[generic]]` sentence only. |
| Ch 11 Quick Review | "Underage alcohol offenses are penalized even off the road; the penalties are in the box." |
| 10.2 | Rain: "add at least 2 seconds to your following distance (more in heavy rain)", which fits a 4-second base with 5 or 6 seconds in rain. |
| 13.6 | Temporary paper license is now a `[[generic]]` sentence. A state edition reads "If you pass, you are licensed. Teens move on to ..." |
| 13.4 | "The test may include maneuvers such as parallel parking, parking on a hill, a three-point turn or pulling over to the curb (Chapters 5 and 8)"; "hitting the cones or poles". |
| 12.9 | Minimum insurance: "(see your state's boxes in this chapter)" in place of "(see 12.10)". |
| 2.7 | "Work zone fines are often doubled" became "Expect higher fines in a work zone. The box below gives the rule." (audit section 5) |
| 6.1 | **Not changed.** National driver ed guidance does not agree with the PA wording. The ADTSEA-based state curriculum (Montana OPI, Module 4.2) puts a right curve near the center line (lane position 2) and a left curve near the right edge. PUB 95 says slightly right of center on right curves. "Keep to the center of your lane" stays as the neutral rule. If a state wants its own wording, it can go in a state box. |

## 2. Facts added (national level, own words)

| Fact | Where | Source |
|---|---|---|
| Flash your high beams once, quickly, then look down and right | 10.1 | PennDOT PUB 95 Ch 3; NY Driver's Manual Ch 9 |
| Signal about 3 to 4 seconds before a turn (guide), plus the box minimum | 5.1 step 2 | PennDOT PUB 95 Ch 3 |
| Long horn blast when you have lost control of your car | 5.8 | PennDOT PUB 95 Ch 3; UVC 12-401 |
| Left turn with a blocked view: wait until you can see every lane you must cross | 4.2 Turning Left | PennDOT PUB 95 Ch 3 |
| Smoking added to the distraction list; no headphones or earbuds | 11.7 | NHTSA distracted driving; PUB 95 Ch 3 |
| BAC 0.02 to 0.05 (about 0.04): about 2 to 3 times the fatal crash risk, highest for young drivers | 11.1 | Zador, Krawchuk and Voas (2000), NHTSA DOT HS 809 050, Tables 6.1 to 6.6 (RR 1.7 to 4.6 at BAC 0.020 to 0.049) |
| Phone use: about 4 times the crash risk, and hands-free is no safer | 11.7 | McEvoy et al., BMJ 331:428 (2005), IIHS |
| Warm up the engine so the defroster works; on packed snow, about half your normal speed | 10.4 | PennDOT PUB 95 Ch 3 (winter driving) |

PUB 95 gives "2 to 7 times" for 0.04. The book uses the range from the NHTSA study instead, because that range has a citable source.

## 3. Signs

New panel `layout/fig/signs_markers_plates.svg` (460 x 290), placed in 2.8 under a new subsection "Markers, Plates and Left Exits" with an 8-row table:
- Object marker OM3-R: yellow and black stripes slope down toward the side you pass on (MUTCD 11th ed., object markers).
- End of roadway marker OM4-1: red diamond.
- No Bicycles R5-6 and No Pedestrian Crossing R9-3: black symbol, red circle and slash, white square.
- Road Entering Curve (W1-10 family, combination curve and intersection): yellow diamond.
- JCT plate M2-1 over a U.S. route marker; WEST cardinal direction plate M3-4 with an M6 arrow plate.
- Left exit: exit number tab on the left edge with a yellow LEFT panel (E1-5bP).

Single-sign picture files for the app: `sq_object_marker`, `sq_end_of_road`, `sq_no_bicycles`, `sq_left_exit`.

Ch 2 grew by 248 words, under the 250 limit. That count includes the table and the caption, and the 2.7 change saved a few words. The grayscale preview and the built page (Core_preview p. 22 to 23) were checked: no clipping, and every sign has its shape and color in a label.

## 4. Bank (bank/core.json)

- 150 records had their distractors replaced: every core quiz question the audit flagged, plus core questions in any `state/*/mocks.json` that had throwaway or twin options. IDs, correct letters and correct answer text did not change. Twin options were removed: the C08-001/002/003 "Straight ahead, as long as ..." options, C05-006 C/D and C05-017 A/D. Fake options were removed: C02-070 "Exactly 1 foot", C02-057 "A rest room", C02-009 "A toll plaza", C07-020 A to C and the like. "WORKERS AHEAD SOMETIMES" was not a core option. It belonged to PA-047, and the state agent has already replaced it in `state/PA/polish.md`.
- Duplicate Move Over in the Ch 4 quiz: C04-019 is now a different testable point, what to do after an emergency vehicle passes (check for a second one, then pull out and stay well back). The state quiz question PA-055 now covers Move Over alone. Move Over is still taught and drilled in the non-quiz bank.
- New non-quiz questions (16): C02-071 to C02-074 (picture questions), C02-075 (JCT), C04-035 (blocked left turn view), C05-037 (signal 3 to 4 s), C05-038 (horn, lost control), C10-040 (flash high beams), C10-041 (rain +2 s), C10-042 (winter warm-up and clearing), C10-043 (packed snow half speed), C11-035 (BAC 0.04 risk), C11-036 (phone 4x), C11-037 (eating and smoking), C11-038 (headphones).
- Letters overall: A 120, B 121, C 111, D 112. Result: BANK PASSED.

## 5. Words per chapter (before / after)

ch02 3204 / 3452; ch04 1934 / 1959; ch05 2363 / 2387; ch10 2343 / 2391; ch11 1989 / 2071; ch12 2159 / 2164; ch13 1219 / 1237.

## Checks

- `python3 tools/check_bank.py bank/core.json`: BANK PASSED.
- `originality_check.py` on ch02, ch04, ch05, ch10, ch11, ch12 and ch13: all passed.
- `python3 layout/build_book.py --core-only`: QA PASSED (179 pages), ORIGINALITY PASSED.
- No em or en dashes in the edited files or the new SVGs.
