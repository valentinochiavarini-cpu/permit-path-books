# Pennsylvania fact check C (state upgrade, diff since cb15098)

Scope: `state/PA/inserts.md` (5 new keys, 23 rewritten), `state/PA/ch01.md` (2 small edits), `bank/PA.json` (newly quiz-flagged questions, edited distractors, PA-144 to PA-164). Checked 2026-10-28.

Sources: PUB 95 (4-21), text of the Drive copy (file 1MZi7_SLlRizXTi9Fzi_KXhzv4dk9RkyU); palegis.us view-statute PDFs; pa.gov online manual, Pennsylvania's Point System page (https://www.pa.gov/agencies/dmv/driver-services/pennsylvania-drivers-manual/online-drivers-manual/pennsylvanias-point-system).

## Changes made

| Where | Old | New | Reason and source |
|---|---|---|---|
| move_over | "Injuring or killing someone brings a suspension of 90 days to one year" | "Seriously injuring or killing someone ..." | The rewrite dropped "seriously". Suspension applies only to serious bodily injury or death. PUB 95 p. 59; 75 Pa.C.S. 3327 |
| vehicle_rules | "your license too if you drove the car" | "your license too if you drove it or let someone else drive it" | The rewrite dropped the "permitted operation" half. 75 Pa.C.S. 1786(d) (palegis.us): owner who "operated or permitted the operation"; online manual, Driving Without Insurance |
| vehicle_rules | 96 words | 89 words | Over the 90-word cap; trimmed wording only ("Minimum insurance:", "Report a name or address change ...") |
| PA-161 src | 75 Pa.C.S. 1545 | 75 Pa.C.S. 1537(a) | 1545 is restoration (record restarts at 5 points). Removal of 3 points per 12 clean months is 1537(a) (palegis.us) |
| PA-141 exp | "Above 35 mph" | "At 35 mph or more" | 75 Pa.C.S. 3334(b) threshold is 35 mph or more; matches the box |

No wrong keys found.

## Verified (no change)

- **Underage, non-driving offenses.** 18 Pa.C.S. 6310.4 shows "(Repealed)": "repealed October 24, 2018, P.L.659, No.95, effective in 180 days" (April 22, 2019) (palegis.us). gambonelaw.com/?p=3363 confirms the mandatory suspensions for 6308 and 6310.3 were repealed. The online manual's Underage Drinking section mentions no suspension. Box claim "None of these brings an automatic license suspension" is correct. 6308 fines up to $500 then $1,000; furnishing to minors at least $1,000 then $2,500 (online manual).
- **DUI table vs 75 Pa.C.S. 3804.** (a)(1): 6 months probation, $300, AHSS; (b)(1): 48 hours minimum, $500 to $5,000, covers 3802(e) minors; (c)(1): 72 hours minimum, $1,000 to $5,000, covers refusal and 3802(c); (e)(2): no suspension for first (a) offense, 12 months for ungraded first offenses under (b) and (c). Table and underage_alcohol box (middle tier, 12 months) match.
- **Point system.** 1535(a): 2/3/4/5 points for 6 to 10, 11 to 15, 16 to 25, 26+ over; school bus 5 points and 60 days. 1535(e)(2): 15-day suspension for 11+ mph over in an active work zone (PA-046). 1537(a): 3 points off per 12 consecutive months with no suspension or points. 1538(a): first 6 points, school (removes 4) or special exam (removes 2), person's choice; 1538(b): second time, hearing plus school, examiner may recommend up to 15 days. 1539: 11 points, 5 days per point first suspension.
- **Fleeing.** 75 Pa.C.S. 3733: M2, additional $500 fine; one-year suspension per the online manual.
- **police_stop.** Online manual: window down, passengers' hands in view, tell officer about a firearm, not the wallet, blue lights alone are not police.
- **emergency_vehicles.** PUB 95 p. 59 to 60: siren or flashing red, or red and blue, lights from any direction; one-way street, nearest roadside; obey fire police; check for a second vehicle; keep at least 500 feet away.
- **headlight_use.** PUB 95 p. 40 and 43: list, 1,000 feet, wipers, taillights, $25 fine approaching $100.
- **work_zone.** PUB 95 p. 18: extra $25 without headlights. **parking_rules** additions: PUB 95 p. 52 (flashers, 500 feet both ways, direction of traffic).
- All other rewritten keys keep the old meaning.
- Every quiz-flagged state question (PA-042 to PA-160 set) is taught in its chapter's box; build QA passed (only the known "mocks print app_only" error).

## Open items

- **Early inspection.** "Either may be done up to 90 days early": 67 Pa. Code 175.41(f)(1) caps a sticker at 15 months from the inspection month, which implies a 3-month early window, but no PennDOT page stating "90 days" for safety inspections could be read (online manual Chapter 5 fetch timed out). Low risk; not changed.
- **Fleeing one-year suspension** rests on the online manual; the suspension section in 75 Pa.C.S. 1532 was not opened.
