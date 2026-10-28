# Upgrade log: Chapters 9 to 13 (tag ch9to13)

Brief: `briefs/UPGRADE_BRIEF.md`. QA input: coverage_PA.md and review_PA.md (scratchpad). Not committed.

## Words before quiz (state edition, after [[generic]] removal)

| Ch | Before | After | Note |
|---|---|---|---|
| 9 | 1,994 | 2,048 | preview 2,093 |
| 10 | 1,921 | 2,267 | +346, within the 350 budget; wind folded into 10.3, crash test trap cut |
| 11 | 1,851 | 1,847 | preview 1,921 |
| 12 | 1,888 | 2,003 | new 12.10 driver record |
| 13 | 1,412 | 1,130 | rebuilt as checklist + skills + mistakes |

## Topics added (national sources)

**Ch 9**
- SHARE THE ROAD plaque under bicycle, tractor or buggy warning signs (MUTCD 11th ed., Chapter 2C, W16-1P).
- Horse-drawn vehicles: buggy warning sign, orange triangle and dim lights, no horn or lights flashing, pass wide and return when the horse shows in the mirror, buggies can roll back on hills (PennDOT PUB 95 sharing the road; state manuals).
- Never pass a vehicle stopped for a pedestrian (Uniform Vehicle Code 11-504(d)).
- Bicycle gap now points to the `bicycle_passing` box ("at least the gap the law requires").

**Ch 10**
- 10.1 Headlights: sunset to sunrise and any time visibility is poor; daytime running lights are not enough (UVC 12-201; state manuals). `{{INSERT:headlight_use}}` placed after the national rule.
- 10.4 Winter: clear the roof, gentle inputs, ease off if wheels spin, lower gear on hills, no cruise control on wet or icy roads, winter kit. Ice spacing changed from "8 to 10 seconds" to "up to about ten times the distance to stop", matching PennDOT PUB 95 and not conflicting with manuals that give larger gaps.
- 10.5 Skids: braking skid (ease off the brake so the wheels roll).
- 10.6 Emergency stops and swerves: hands at 9 and 3 or 8 and 4 (PennDOT PUB 95 Ch 3; NHTSA "Using Efficient Steering Techniques"); ABS press and hold; threshold braking without ABS, noting that some manuals call it pumping (PennDOT PUB 95 says press and release repeatedly); steering around a hazard is often better above about 25 mph (PennDOT PUB 95 Ch 3); car coming at you in your lane: horn, slow, steer right, keep braking if a crash is unavoidable (PennDOT PUB 95 Ch 3).
- Breakdowns: off the road, flashers, raise the hood only without stepping into traffic, wait buckled in or well away (consistent with Ch 7.10).
- 10.9 If Police Signal You to Stop: signal and pull right when safe, stay in the car, engine and radio off, interior light at night, hands on the wheel, belt on, reach for documents only when asked, stay calm, contest in court (state manuals, e.g. PennDOT PUB 95, NY DMV Driver's Manual). `{{INSERT:police_stop}}`.

**Ch 11**
- Order fixed: Legal Limit, then Zero Tolerance (0.02 or lower, 23 U.S.C. 161), then `{{INSERT:bac_limits}}`. No "box above" left. Utah appears once, wrapped as generic (state editions print no Utah).
- Open container text moved before `{{INSERT:dui_penalties}}` (every state's dui_penalties insert covers open containers).
- New "Under 21: Alcohol Can Cost You Your License": buying under 21 illegal and fake ID a crime (23 U.S.C. 158), license loss possible without a car, zero tolerance behind the wheel. `{{INSERT:underage_alcohol}}`.
- Fatigue numbers: about 18 hours awake like 0.05 BAC, 24 hours like 0.10 (CDC "Drowsy Driving: Asleep at the Wheel"; CDC NIOSH "Driver Fatigue on the Job" gives 17 hours for 0.05, so "about 18" is safe); teens need 8 or more hours (CDC "About Sleep": ages 13 to 18, 8 to 10 hours).
- DUI table concerns from the QA report (column headed "Jail" holding "6 months probation", "All tiers: $300 to $5,000 fines") are in `state/PA/inserts.md` (`dui_penalties`), not in the core. **For the owner / PA state run:** fix the PA insert (e.g. column "Penalty", and give first-offense fines per tier).

**Ch 12**
- Renamed `# Chapter 12: Your Car, Passengers and Your Record`.
- New 12.10 Your Driving Record: what the record holds, violations counted (usually in points, more for serious ones), steps as they add up (warning, exam/course/hearing, suspension), points coming off with time or a course, required liability insurance and proof, driving while suspended. `{{INSERT:driver_record}}`. Wording avoids saying every state uses points (Texas, for example, does not), so a state box can give the exact system. Sources: state manuals (PennDOT PUB 95 Ch 5), Insurance Information Institute.

**Ch 13**
- Rebuilt: 13.1 Test-Day Checklist (table), 13.2 The Knowledge Test (short tactics), 13.3 How the Road Test Works (with `{{INSERT:road_test}}`, vehicle and controls checks), 13.4 Road Test Skills, 13.5 Common Mistakes and Automatic Fails, 13.6 After the Test. Removed the last-week study table, numbers sheet, the generic "your state may test parallel parking" and every "most/many/some states" line. State facts (retest waits, who may ride, maneuvers) are left to Chapter 1 and the road_test box.

**Sample inserts** (`core/sample/inserts.md`): emergency_vehicles, headlight_use, police_stop, underage_alcohol, driver_record, each labeled "Sample text with invented values, not any real state's rule", under 90 words.

## Hedges (unwrapped lines a state edition prints)

| Ch | Before | After | Action |
|---|---|---|---|
| 9 | 4 | 0 | crosswalk "illegal in most states" deleted; bike lane right turn, 3 feet, transit bus yield wrapped; "every state" rewritten as plain rules |
| 10 | 3 | 0 | headlight "most/many states" wrapped; crash "many states require" wrapped; "your state agency" and "as your state requires" rewritten |
| 11 | 6 | 0 | refusal and jail lines rewritten; open container and phone laws wrapped; Utah wrapped; young passengers pointed to Chapter 1 |
| 12 | 4 | 0 | equipment and New Hampshire lines wrapped; primary/secondary rewritten as definitions; proof on phone "where the law allows"; "each state sets its own minimum" removed |
| 13 | 14 | 0 | all rewritten or deleted in the rebuild |

Remaining soft words (not "states" hedges): "usually counted in points" (12.10), "often face action sooner" (12.10), "Friends and family usually cannot ride along" (13.3).

## Quiz changes (bank/core.json)

Quiz order (first 7 print in a state edition, last 3 give way to state questions):
- Ch 9: C09-001, 002, 003, 009, 015, 019, 021 | 026, 029, 027. C09-008 left the quiz, C09-027 (buggy) joined. C09-009 explanation no longer says "most states require 3 feet"; it says "at least the distance your state requires (see the box in 9.2)".
- Ch 10: C10-001, 021, 020, 008, 025, 031 (new, police stop), 028 | 007, 013, 024. C10-011 left the quiz.
- Ch 11: C11-002, 004, 009, 010, 025, 001, 016 | 006, 020, 031 (new, 18 hours awake). C11-022 left the quiz. C11-004 no longer mentions Utah.
- Ch 12: C12-001, 003, 005, 028, 031 (new, points), 013, 002 | 007, 010, 016. C12-026 left the quiz.
- Ch 13: C13-017, 025, 021, 016, 010, 012, 027 | 026, 028, 022. Study tactic questions C13-001 and C13-004 left the quiz; the quiz is now test-day rules and road test skills only.
- Joke or throwaway distractors replaced with near misses in every quiz question listed above, plus C09-004, C09-020, C09-025.
- Rewritten in place (same ID): C10-005 (daytime running lights not enough), C10-019 (ice: up to ten times the stopping distance; used in the CA mock, still valid), C11-005 (was the Utah question; now the federal 0.04 commercial limit; used in CA and FL mocks, same correct letter), C13-001 (stop behind the line), C13-002 (ask the examiner to repeat), C13-003 (driving far too slowly), C13-009/010/026/029 (removed "most/nearly every/many states" from stems).
- Hedges removed from explanations: C09-009, C09-025, C10-028, C11-004, C11-011, C11-015, C13-012, C13-020, C13-029, C13-030.
- New non-quiz questions: C09-031 to 033, C10-032 to 039, C11-032 to 034, C12-032 to 035. New quiz: C10-031, C11-031, C12-031.
- Counts: Ch 9: 33, Ch 10: 39, Ch 11: 34, Ch 12: 35, Ch 13: 30, each with exactly 10 quiz. No quiz question is used in any state mock. `check_bank.py`: BANK PASSED.

## app_only (stay online, never print)

C13-004, C13-005, C13-006, C13-007, C13-009 (knowledge test tactics), C13-029, C13-030 (what happens after the test). None of them is in a state mock. C13-008 (skip and return) is a tactic too but sits in the CA mock, so it was left printable.

Note for the run leader: `tools/make_mocks.py` filters `app_only` only for state banks, not for core questions. If core app_only questions must never print, add the filter on line 17.

## Checks

- `originality_check.py check` passed for ch09 to ch13 (shared 0.00 to 0.30 percent).
- `build_book.py --core-only`: QA PASSED, 170 pages.
- No em or en dashes, no years, no state names in kept core text (Utah and New Hampshire appear only inside [[generic]]).

## Unsure

- "These offenses can cost you your driver's license even when no car is involved" (11.4) is true in most states (use and lose laws) but not proven for all 50; each state's `underage_alcohol` box must state the actual rule.
- "Turn on your headlights from sunset to sunrise" is the Uniform Vehicle Code baseline; some states phrase it as 30 minutes after sunset. The `headlight_use` box gives the exact rule.
