# California fact check C (state upgrade since cb15098)

Scope: 5 new inserts (emergency_vehicles, headlight_use, police_stop, underage_alcohol, driver_record), rewrite of all inserts (meaning vs cb15098), new questions CA-149 to CA-164, quiz flags and changed questions (CA-047, 050, 062, 074, 079, 083, 085, 110, 113, 115, 126, 134: options reshuffled or moved, keys checked). Built text read in out/CA/Permit_Path_California.md; rebuilt after fixes (QA passed; only the expected "mocks print app_only" error remains).

Sources: CA Driver's Handbook (Drive 1qT23zBRVYqr3VH6228kwmf7OSUMlBWCF), california.public.law (VC 21806, 12810, 12810.5, 23224, 13202.5, 24400; B&P 25661, 25662).

## Changes

| Key | Old | New | Reason | Source |
|---|---|---|---|---|
| police_stop | "The officer must tell you why you were stopped before asking questions." | "Except in an emergency, the officer must ..." | Handbook (Law Enforcement Stops) allows withholding the reason to protect life or property from an imminent threat; CA-156 keys that exception. | Handbook Section 6, p. 29 |
| underage_alcohol | "up to $1,000 and 6 months in jail" | "up to $1,000, 6 months in jail, or both" | VC 23224(d): fine, jail, or both. | https://california.public.law/codes/vehicle_code_section_23224 |
| underage_alcohol | "a DUI conviction, even on a bicycle, means a one-year license suspension or delay" | "a DUI conviction means a one-year ... delay. A bicycle DUI can bring the same." | VC 13202.5 (mandatory one year) does not list bicycle DUI (21200.5); the handbook says a bicycle DUI at 13 to 20 "may" bring a one-year suspension or delay. sources.md cited 13202.5 for bicycles. | https://california.public.law/codes/vehicle_code_section_13202.5; Handbook Section 9 |
| underage_alcohol | "an adult the parent named" | "parent-approved adult" | Trim to 89 words (was 98 after fixes); same meaning (23224(a) designated adult). | VC 23224(a) |

No question changes needed.

## Verified (no change)

- emergency_vehicles: siren and red lamp; right-hand edge or curb, clear of intersection, stop; leave an exclusive or preferential lane as soon as reasonably safe (VC 21806(a)); no one-way rule. 300 ft and arrest for driving to a scene (Handbook Section 7).
- headlight_use: VC 24400(b), (c) (darkness, 1,000 ft, wipers in continuous use for rain, mist, snow, fog); statute says headlamps, handbook says low beams; parking lights only illegal, mountain roads, tunnels, signs (Handbook Section 5).
- police_stop: right shoulder even from HOV lane, well-lit, window down, hands in view, license plus insurance plus registration, may decline a search but not resist (Handbook Section 6, pp. 29 to 30).
- underage_alcohol: B&P 25662 (public possession, first offense $250 or 24 to 32 h), B&P 25661 (false ID, at least $250, 24 to 32 h, or both); 23224(c) impound 1 to 30 days of a car registered to the minor.
- driver_record: 2 points for hit-and-run, DUI, reckless driving; 1 point other moving convictions and at-fault crashes (VC 12810). Negligent operator presumption 4/12, 6/24, 8/36 (VC 12810.5(a)). Record 36 months or longer, traffic violator school once in 18 months, not reported to insurer (Handbook Section 7). Insurance 30/60/15.
- All 23 rewritten inserts compared with cb15098: no other change of meaning (300 ft moved to emergency_vehicles; insurance and headlights moved out of vehicle_rules; "in writing" dropped from crash_reporting, an omission).
- New questions CA-149 to CA-164: one defensible answer each, keys correct. Quiz-flagged questions (ch 2 to 13) are all taught in that chapter's state box in the built book (CA-134 now in ch 10 headlight_use).

## Open
- ch01 line 126 says alcohol or drug conviction "between ages 15 and 20"; VC 13202.5 runs from 13. Not wrong for drivers, not changed (outside the diff).
- u_turn (92) and dui_penalties (92) exceed 90 words counting list markup; left for the lead.
