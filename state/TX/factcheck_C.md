# Texas fact check C (state upgrade since cb15098)

Scope: 5 new inserts (emergency_vehicles, headlight_use, police_stop, underage_alcohol, driver_record), rewrite of all inserts (meaning vs cb15098), new questions TX-145 to TX-163, quiz flags and changed questions (TX-082, 089, 112, 113, 118, 129, 133, 143: options reshuffled, keys checked). Built text read in out/TX/Permit_Path_Texas.md; rebuilt after fixes (QA passed; only the expected "mocks print app_only" error remains).

Sources: DL-7 handbook (Drive 1QFLw84NB77SFOD1HjAsHI5no5CaC8h40), texas.public.law (Transp. Code 545.156, 545.157, 545.407, 521.292, 542.401, 547.004; Alco. Bev. Code 106.071), dps.texas.gov DRP repeal FAQ.

## Changes

| Key | Old | New | Reason | Source |
|---|---|---|---|---|
| move_over | "leave the lane next to them. If you cannot, slow to 20 mph below the limit" | "You may leave the lane next to them, on a road with two or more lanes your way, or slow to 20 mph below the limit" | Rewrite turned the statute's either/or into a fallback. 545.157(b) and DL-7 p. 46 give two options joined by "or". | https://texas.public.law/statutes/tex._transp._code_section_545.157 |
| phone_laws | "reading, writing or sending text messages" | "reading, writing or sending electronic messages, such as texts," | Rewrite narrowed the ban to texts; 545.4251 covers any electronic message (TX-129 keys "electronic messages"). | Tex. Transp. Code 545.4251 |

No question changes needed.

## Verified (no change)

- emergency_vehicles: right-hand edge or curb, clear of intersection, stop (545.156(a-1)); no one-way rule in statute; "if you cannot pull right, slow down and leave a clear path" and "siren or lights" are DL-7 Ch. 4 p. 22 wording (statute: audible and visual, police either). 500 ft behind fire apparatus answering an alarm or ambulance with red lights; no driving into or parking in the block where it stopped (545.407(a), (b)).
- headlight_use: 30 min after sunset to 30 min before sunrise, 1,000 ft (547.302, 541.401; DL-7 p. 47); no wipers clause; parking lights or low beams when parked on an unlighted highway (DL-7 p. 47). Fine up to $200: 547.004 makes equipment and lighting violations a misdemeanor without a penalty, so the 542.401 general penalty ($1 to $200) applies.
- headlight_dimming: lighted roads, fog, heavy rain, sleet, snow, dust (DL-7 p. 47).
- police_stop: DL-7 Ch. 14 pp. 65 to 66 (right shoulder or well-lighted side street, parking brake, hazards, tell officer of any weapon, license must be displayed on request, hazards plus slow driving plus 911 if unsure).
- underage_alcohol: Table 26 (1st: Class C up to $500, 8 to 12 h, course, 30 days; 2nd: 60 days) matches Alco. Bev. Code 106.071(d) (8 to 12 h, 30/60/180 days; covers 106.02, 106.025, 106.04, 106.05, 106.07 misrepresentation of age). DUI by a Minor 1st: up to $500, 20 to 40 h, course (Table 29).
- driver_record: no point system: DPS FAQ says DRP points are no longer assessed and earlier points were removed; no other Texas point system exists. Habitual violator 4+ in 12 months or 7+ in 24 months, moving violations, separate transactions, seat belt excluded (521.292(b)); suspension follows a hearing or 90 days if none requested (521.293 to 521.295). Under 18: 2+ moving violations in 12 months (521.292(a)(8)), taught in ch01 line 135. Insurance 30/60/25 and Table 13 fines (DL-7 p. 18).
- All 23 rewritten inserts compared with cb15098: no other change of meaning (dropped items are omissions or moved to new keys; bodily injury clause dropped from move_over, suspension dropped from school_bus repeat: omissions only).
- New questions TX-145 to TX-163: one defensible answer each, keys correct. Quiz-flagged questions (ch 2 to 13) are all taught in that chapter's state box in the built book (TX-139 insurance now in driver_record, ch 12).

## Open
- parking_rules (102 words) and dui_penalties (106 words) exceed 90 words counting table markup; unchanged in substance, left for the lead.
