# Missouri fact check B (inserts and non-Chapter 1 bank)

Checked 2026-10-28. Scope: `state/MO/inserts.md` (all 28 keys, read in context in the built `out/MO/Permit_Path_Missouri.md`) and every `bank/MO.json` question with ch 2 to 13 (MO-041 to MO-160). Chapter 1 IDs were not touched.

Sources used: Missouri Driver Guide, rev. Aug 2026 (Drive file 1T7sMnlclbbPk2DSH86ljtDJGG9QepGoz); revisor.mo.gov (only RSMo 302.525 was readable: every section URL returned 302.525; one PageSelect URL was blocked by an unanswered permission request); law.justia.com (2025 Revised Statutes: 304.022, 304.281, 307.178, 307.179, 303.040, 577.010, 558.002 read; 304.822, 304.050, 304.010 and 577.060 failed at Justia); FindLaw copy of 304.822; Missouri House bill text HCS HB 2742 and bill summary; dor.mo.gov DWI page; modot.org Move Over page; NHTSA open container document.

## Insert changes

| Key | Old | New | Reason and source |
|---|---|---|---|
| school_bus | "Passing illegally: 5 points, a fine up to $1,000 and a 90-day suspension." | "Passing illegally: 5 points, a fine of $500 to $1,000 and a possible suspension. Repeats within five years: a 90-day, then 180-day, suspension." | Legal error. The law effective Aug. 28, 2026 (HB 2742, signed as SB 1421 per KCTV5) sets a first-offense fine of $500 to $1,000 and leaves a first-offense suspension to the court; 90 days is the second offense within 5 years, 180 days the third. 5 points under 302.302. Sources: HCS HB 2742 text, sections 304.070.2 and .4 and 302.302 (https://documents.house.mo.gov/billtracking/bills261/hlrbillspdf/6086H.03C.pdf); bill summary (https://documents.house.mo.gov/billtracking/bills261/sumpdf/HB2742C.pdf); KSHB, Aug. 28, 2026 (https://www.kshb.com/news/local-news/missouri/platte-county/missouri-school-bus-stop-arm-fines-increase-to-500-starting-today); KFVS, Aug. 26, 2026. The Guide (p. 24) says "First offense: Court ordered suspension, 90 days, or as designated by the court", which matches "possible suspension". |
| work_zone | "in a work zone can cost up to $500" | "in a work zone with workers present can cost up to $500" | 304.822.6(5) applies the $500 maximum in a work zone only when workers are present (FindLaw, https://codes.findlaw.com/mo/title-xix-motor-vehicles-watercraft-and-aviation/mo-rev-st-304-822/). |
| dui_penalties | Fines: up to $500 / $1,000 / $5,000 | Up to $1,000 / $2,000 / $10,000 | Legal error. 577.010: first offense class B misdemeanor, prior offender class A misdemeanor, persistent offender class E felony (https://law.justia.com/codes/missouri/title-xxxviii/chapter-577/section-577-010/). 558.002 maximum fines: class B misdemeanor $1,000, class A $2,000, class E felony $10,000 (https://law.justia.com/codes/missouri/title-xxxviii/chapter-558/section-558-002/). The Guide p. 68 still prints the pre-2017 figures ($500, $1,000, $5,000). Jail terms (6 months, 1 year, 4 years) unchanged and correct. |
| road_test | "You also park on a hill, back up and turn." | "You also park on a hill, back up, and make at least two right and two left turns." | MO-157 is a Chapter 13 quiz question and was not taught in the Chapter 13 box (only in Chapter 1). Guide p. 20. |

All inserts are 90 words or fewer, no em or en dashes, no years.

## Coordinator item: RSMo 302.525 (effective Aug. 28, 2026)

302.525.2(1) (revisor.mo.gov, https://revisor.mo.gov/main/OneSection.aspx?section=302.525): the administrative first action is a 30-day suspension then a 60-day restricted privilege, or no suspension and a 90-day restricted privilege with an ignition interlock. No insert change needed: dui_penalties' "90-day suspension" is the court conviction action, which the DOR DWI page still states as "a 90-day suspension" with possible RDP (https://dor.mo.gov/driver-license/revocation-reinstatement/dwi.html), and underage_alcohol only says a minor at 0.02 is treated like an adult at 0.08 (no day count). MO-131 ("90-day suspension" for a first DWI or BAC conviction) stays correct.

## Question fixes

| ID | Old | New | Reason |
|---|---|---|---|
| MO-087 | D: "5 points, a fine up to $1,000 and a 90-day suspension"; exp and src cited Missourinet | D: "5 points, a fine of $500 to $1,000 and a possible license suspension"; exp and src updated to HB 2742 / 304.070 | Keyed answer stated the second-offense suspension as the first-offense penalty (see school_bus). |
| MO-061 | "an arrow bending sharply right, then sharply left" | "an arrow bending sharply left, then sharply right" | `layout/fig/sq_reverse_turn.svg` shows the arrow rising, turning left, then right (W1-3L). Stem contradicted the picture. |
| MO-077 | "A yellow diamond shows a person holding a flag or paddle" | "An orange diamond ..." | `sq_flagger_ahead.svg` is an orange work zone sign (Guide p. 53, MUTCD W20-7). |

All other ch 2 to 13 questions checked: key correct, one defensible answer, consistent with the box and the Guide or statute. Every quiz-flagged state question (MO-041 to 043, 078 to 080, 082 to 084, 092 to 094, 098 to 100, 106 to 108, 110, 111, 113 to 115, 124 to 126, 141 to 143, 155 to 157) is now taught in its chapter's box. Sign pictures for all 15 `img` questions were rendered and match their stems.

## Items confirmed (no change)

- phone_laws: 304.822 covers all drivers; bans holding or supporting, texting, video; single touch or swipe allowed; lawfully stopped or parked and emergency exceptions; fines up to $150, $250, $500 within 24 months; "No person shall be stopped, inspected, or detained solely" for it (FindLaw copy). Correct.
- move_over: 304.022.2 (Justia 2025) and MoDOT: stationary vehicle with red, red and blue, amber, or amber and white lights; lane not adjacent on 4+ lanes with 2 in your direction; else slow to a safe speed; class A misdemeanor (304.022.7). emergency_vehicles: 304.022.1 "as far as possible to the right". Correct.
- open container: no statewide ban confirmed (Missouri is not among the 39 states plus DC complying with 23 U.S.C. 154, NHTSA, https://nhtsa.gov/document/open-container-laws; no statute found). Local bans: secondary source only.
- bac_limits / underage_alcohol: 0.08, 0.04 commercial, 0.02 under 21 (Guide p. 67; DOR). MIP 30/90 days/1 year (DOR). Abuse and Lose 90 days (Guide p. 69).
- seat_belts: 307.178 (Justia): driver and front seat; under 18 in a truck; $10 max, no court costs, no points; no stop solely for it; under 16 governed by 307.179 (driver responsible). Intermediate and permit drivers: all passengers belted (Guide p. 55). The box makes no primary or secondary claim for under 16, so nothing to fix.
- child_restraints: 307.179 tiers and $50 plus court costs, dismissal on proof (Justia). Correct.
- speed_limits: Guide p. 50; 304.010 as amended effective Aug. 28, 2026 lets MoDOT post 75 mph on rural interstates and freeways; MoDOT announced the first 75 mph segments (I-29, I-35, I-49, I-55) on Oct. 21, 2026, signs going up this fall (KY3, https://www.ky3.com/2026/10/21/see-list-modot-announces-locations-increased-interstate-speed-limits/; KCUR, Aug. 23, 2026). "70 mph, or 75 mph where posted" is correct in practice.
- driver_record: 8 in 18 months; 30/60/90 days; 12/12, 18/24, 24/36 revocation; reduction to 4 points; one-third, half, zero (Guide pp. 73 to 74).
- vehicle_rules: 25/50/25 (303.190 per writer; 302.302 4 points). Not re-read this pass.
- crash_reporting: 303.040.1 (Justia): report to the director within 30 days for a crash with an uninsured motorist where someone is killed or injured or property damage exceeds $500, and any uninsured owner or operator must report. Matches the box; leaving the scene 12 points (Guide p. 73).
- turn_on_red: 304.281.1(3)(b) authorizes only a right turn on red; the statute is silent on left on red, so "Missouri law allows only that right turn" is defensible. Red arrow rule from Guide p. 44.
- hov: OMIT kept (no Missouri HOV lanes found).
- headlight_use, headlight_dimming, signal_distance, following_distance, u_turn, parking_rules, police_stop, supervised_hours: match the Guide pages cited in sources.md.

## Core sentences that do not fit Missouri (not edited; outside scope)

1. core/ch08.md, 8.5: "The box below gives the exact distances." The Missouri box gives none: the Guide (p. 35) lists no-parking places without distances (only "blocking a fire hydrant"). Suggest a `[[generic]]` wording or "the box below gives your state's list".
2. core/ch04.md, 4.6: "The box below gives your state's details, such as how far back to stay." Missouri has no following distance in 304.022, so the box gives none. Soft mismatch, not a legal contradiction.
3. core/ch04.md, Move Over: "Slow down well below the speed limit". Missouri law says reduce to "a safe speed for road conditions"; no fixed amount. Not a contradiction, but "well below" is stronger than the statute.

No core sentence found that states a rule contrary to Missouri law.

## Open items

- Official text of 304.070, 304.050 and 304.010 as amended Aug. 28, 2026 not read on revisor.mo.gov (WebFetch returns 302.525 for every section; curl blocked by the proxy). Penalties above rest on the House committee substitute text and four news reports; the truly agreed bill summary (HB2742T.pdf) was blocked by an unanswered permission request. KSMU (Aug. 20, 2026) reports a first-offense 90-day suspension "or as the court determines", the others "possible suspension": the box wording covers both.
- DWI fines now follow the statute, not the Guide (Guide p. 68 shows $500 / $1,000 / $5,000). No bank question asks the fine. Owner may prefer to drop the fine column instead.
- 304.822 read on FindLaw (Justia failed); revisor not readable.
- 577.060 (leaving the scene) not read; 12 points from the Guide and 302.302.
- MO-087's correct option is now longer than its distractors; consider lengthening a distractor in a later pass.
