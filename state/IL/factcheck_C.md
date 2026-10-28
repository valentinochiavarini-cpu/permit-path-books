# Illinois fact check C (state upgrade, diff since cb15098)

Scope: `state/IL/inserts.md` (5 new keys, 23 rewritten), `bank/IL.json` (newly quiz-flagged questions, edited distractors, IL-143 to IL-161). Checked 2026-10-28.

Sources: Illinois Rules of the Road 2026 (Drive file 1LeXtD-Oamm4hMi150EIXYUXOTtLaNo8H, text copy); 625 ILCS 5 and 235 ILCS 5 via witnessslips.ilga.gov / lig.ilga.gov mirrors; 92 Ill. Adm. Code 1040.20 and 1040.30 via ilga.gov JCAR (https://ilga.gov/ftp/JCAR/AdminCode/092/092010400000200R.html, ...0300R.html).

## Changes made

| Where | Old | New | Reason and source |
|---|---|---|---|
| driver_record | "15 to 44 points means 2 months" | "... 2 months with no suspension in seven years" | 1040.30: 2 months is column (a), no prior suspension in 7 years; column (b) is 4 months |
| driver_record | under-21 sentence | "Under 21, two convictions in 24 months bring a suspension (Chapter 1)." | Trimmed to stay at 90 words; same meaning (RR p. 52, 6-206(a)(36)) |
| IL-160 stem | "no recent suspensions" | "no suspension in the past seven years" | Makes the 2-month key exact under 1040.30(a) |
| emergency_vehicles | "Never drive over a fire hose." | "... unless a fire official allows it." | RR p. 25: prohibited "unless permitted by a fire official in command"; matches IL-146 key |
| hov | "You may never drive or pass on the shoulder." | "Never use the shoulder as a travel lane or to pass." | Rewrite overstated the rule and contradicted the police_stop and Chapter 10 advice to pull onto the shoulder |
| bicycle_passing | "Open your door with your right hand (the Dutch Reach)." | "... with your right hand to turn and check for bikes (the Dutch Reach)." | IL-104 (quiz) keys the reason (turn to check for bikes), which the box did not teach. RR pp. 30, 43 |

No wrong keys found.

## Verified (no change)

- **Points.** 1040.20: 5 (1 to 10 over), 15 (11 to 14), 20 (15 to 25), 50 (26 to 34 and 35+), 20 for red light (11-306) and stop sign (11-904). 1040.30: three or more convictions in 12 months; 110+ revocation in every column. 6-206(a)(2).
- **Underage alcohol.** 235 ILCS 5/6-20(a), (c), (d), (e), (f): purchase, accept, possess, consume, and use of a false or another person's ID are Class A misdemeanors. 625 ILCS 5/6-206(a)(43): supervision while an occupant of a motor vehicle, 3 months; (a)(38) conviction while an occupant; RR p. 19: at least 6 months. Zero tolerance at least 3 months and under-21 DUI revocation at least 2 years: RR p. 52. Adults furnishing alcohol: fines, jail, suspension (RR p. 52).
- **Scott's Law.** 11-907(d), P.A. 103-711: $250 to $10,000 first; suspensions for damage (90 days to 1 year), injury, death. 11-907(a): right-hand edge or curb, clear of any intersection, no one-way rule.
- **Fire apparatus.** 625 ILCS 5/11-1411: no following within 500 feet, no stopping within 500 feet (lig.ilga.gov).
- **headlight_use.** 625 ILCS 5/12-201(b): sunset to sunrise, wipers for rain, snow, fog or other conditions, 1,000 feet.
- **police_stop.** RR pp. 21 to 22: no stopping on bridges, curves, by guardrails or walls; tell officer about glove box or phone; unmarked car options; signing a ticket is not an admission of guilt.
- **vehicle_rules.** RR, Mandatory Insurance section: insurance violation, at least 3 months and $100 reinstatement fee.
- All other rewritten keys keep the old meaning. Every quiz-flagged state question is taught in its chapter's box; build QA passed (only the known "mocks print app_only" error).

## Open items

- **Manual conflict on underage off-road suspension.** RR p. 52 says anyone under 21 convicted or under supervision for possession or consumption "will lose their driving privileges regardless of whether or not they are operating a motor vehicle". RR p. 19, the RR suspension list (Chapter 7) and 6-206(a)(38) and (a)(43) tie the suspension to being an occupant of a motor vehicle. The box follows the statute and does not claim no suspension off the road. Owner may want to keep the wording as is.
