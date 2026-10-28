# Alabama fact check B

Checker B, 2026-10-28. Scope: `state/AL/inserts.md` (all 28 keys, each read in context in the rebuilt `out/AL/Permit_Path_Alabama.md`) and every `bank/AL.json` question with ch other than 1 (AL-043 to AL-147). Ch 1 questions not touched.

Sources: Code of Alabama on law.justia.com (2025 code, cited "J s") and codes.findlaw.com (current to 2024-12-30, cited "FL s"); Alabama Driver Manual, ALEA, November 2024 ("MAN", Drive copy, text in scratchpad); alea.gov pages. alison.legislature.state.al.us and legislature.state.al.us PDFs are blocked (robots); Justia and FindLaw do not serve 32-5A-350.1.

## Insert changes

| Key | Change | Reason and source |
|---|---|---|
| implied_consent | "prior offense in the past **five years**" became "**10 years**" | J 32-5A-304(b) (2025): 90 days with no prior, then 1 year, 3 years, 5 years by prior alcohol or drug enforcement contacts in the "immediately preceding 10 years"; refusals count as priors. https://law.justia.com/codes/alabama/title-32/chapter-5a/article-14/section-32-5a-304/ . Refusal minimum 90 days: 32-5-192(a)(3) (vLex, 2023 code). |
| dui_penalties | Second offense jail: "48 hours or 20 days community service" became "At least 5 days, or 30 days community service; up to 1 year" | J 32-5A-191(f) (2025): "not less than five days or community service for not less than 30 days", not suspendable. MAN p. 33 still prints the old 48 hours / 20 days. https://law.justia.com/codes/alabama/title-32/chapter-5a/article-9/section-32-5a-191/ |
| underage_alcohol | Suspension "90-day to 6-month" became "3 to 6 month" | J 28-3A-25(c) (2025): license surrendered "not less than three months nor more than six months" for (a)(18) (under 21 purchase, consume, possess, transport) and (a)(21) (false ID). Fine $50 to $500 and up to 3 months jail confirmed in (b)(2). Replaces the 2019 University of Alabama summary. https://law.justia.com/codes/alabama/title-28/chapter-3a/section-28-3a-25/ |
| phone_laws | First paragraph rewritten. Old: hands-free law "bars every driver from holding..." and "Police can stop you for this alone." New: holding or supporting a phone, or watching or recording video, is a violation when an officer also sees you cross lanes without a signal, swerve or otherwise drive improperly; voice, Bluetooth, one tap or swipe and emergency calls allowed; "Never text while you drive" (advice). Table (fines, points) unchanged. | 32-5A-350.1(c) as quoted by MAN p. 16 ("a violation ... when a driver is observed crossing in and out of a traffic lane without using a turn signal, swerving or otherwise operating a motor vehicle in an improper manner") and by ALEA via Cullman Tribune, 2024-06-06 (https://cullmantribune.com/?p=108709 , where a police chief calls it a secondary offense). The same (c) text appears as existing law in SB239 (2024, died in committee: https://legiscan.com/AL/bill/SB239/2024). Fines $50/$100/$150 within 24 months: SB239 text (e)(1); points 1/2/3: J 32-5A-351 (2025). Old texting section 32-5A-350 repealed by Act 2023-478 (J 32-5A-350), so MAN p. 32 ($25/$50/$75, 2 points) is obsolete. "Primary offense" claim from news (Wetumpka Herald) not supported by the statute text. |
| turn_on_red | Red arrow sentence. Old: the law allows turns at "any steady red signal, so a red arrow follows the same rule". New: "The law has no separate rule for a red arrow and does not clearly allow a turn on one. When a red arrow is lit, wait for the green." | J 32-5A-32(3) (2025): (a) speaks of a "steady circular red signal alone", (b) lets traffic "facing any steady red signal" turn right (or left one-way to one-way) after stopping; no red arrow provision, no case law or ALEA guidance found; MAN pp. 55 to 56 silent. The old wording stated an inference as law. https://law.justia.com/codes/alabama/title-32/chapter-5a/article-2/section-32-5a-32/ |
| hov | "a yellow X means use it with caution" became "a yellow X means you may use it only with caution, ready to leave it" | MAN p. 56: steady yellow X "permitted to drive in the lane ... using caution. Potentially hazardous conditions exist". Statute J 32-5A-35 covers only green and red. The added "ready to leave it" bridges the core table (see below). |
| speed_limits | Rows "Where posted 65" and "Interstate, where posted 70" became "Highway with four or more lanes 65" and "Interstate 70" | FL 32-5A-171: 65 mph on "any other highway having four or more traffic lanes", 70 mph on interstates, as statutory maximums. MAN p. 60 uses "where posted"; both agree on the numbers. https://codes.findlaw.com/al/title-32-motor-vehicles-and-traffic/al-code-sect-32-5a-171/ |
| supervised_hours | "licensed driving instructor" became "certified driving instructor" | ALEA GDL page: form "signed by a parent, grandparent, legal guardian or certified driving instructor". |

All inserts 90 words or fewer after the changes (largest: school_bus 90, police_stop 89, move_over 88, turn_on_red 86; whitespace count with table pipes removed). No em or en dashes, no years.

## Inserts verified without change

| Key | Checked against |
|---|---|
| school_zone | MAN pp. 44, 60, 65 |
| work_zone | J 32-5A-176.1(a), (c) (2025): any Chapter 5 or 5A violation in a construction zone with workers present and performing work, fine "the greater of $250 or double"; 3 points MAN p. 19 |
| move_over | FL 32-5A-58.2 (current to 2024-12-30) and ALEA Move Over page (lists Act 2024-295): covered vehicles; vacate lane or 15 mph under; two-lane 15 under at 25+, 10 mph at 20 or less; $200 / $250 / $300; third or later at least 90-day suspension |
| emergency_vehicles | MAN pp. 58, 61, 63, 65 (statute 32-5A-115 not fetched) |
| school_bus | FL 32-5A-154: school and church buses; resume when bus moves, driver signals or lights off; divided highway of four or more lanes exception; $150 to $300 first; second $300 to $500, 100 hours service, 30-day suspension. 20 ft and 4 to 6 lane undivided rule: MAN pp. 61 to 62. 5 points MAN p. 19 |
| u_turn | MAN pp. 23, 78 |
| following_distance, parking_rules, bicycle_passing, crash_reporting, police_stop, signal_distance, headlight_dimming, road_test | MAN pages as logged in `sources.md` (parking p. 29, bicycles pp. 23 to 24, SR-31 p. 38, dimming p. 69 re-read) |
| hov (left lane) | FL 32-5A-80(d): interstate leftmost lane, 1.5 miles without completely passing; exceptions incl. traffic, weather, exiting left, tolls, emergency vehicles, road work |
| bac_limits | J 32-5A-191(a), (b), (i) |
| seat_belts | FL 32-5B-4: "each occupant of a passenger car"; non-front-seat violation "shall be a secondary violation" |
| child_restraints | FL 32-5-222(a), (b), (d), (g): stages, vehicles, $25, 1 then 2 points |
| vehicle_rules | MAN p. 68 (25/50/25; $500 / $1,000 and/or six-month license suspension); FL 32-7A-16 now also sets towing and impoundment for repeat violations (not printed) |
| headlight_use | FL 32-5-240(a)(1): half hour after sunset to half hour before sunrise; 500 ft; wipers for rain, sleet or snow, intermittent use excepted |
| driver_record | MAN p. 19 point schedule and suspension table (12 to 14: 60 days ... 24+: 365 days), two years, $100 reinstatement MAN p. 17 |

## Question fixes (bank/AL.json)

No wrong answer keys found apart from AL-125.

| ID | Old | New | Reason |
|---|---|---|---|
| AL-125 | "Can an Alabama officer stop you only for holding your phone while driving?" Key D: "Yes, it is a primary offense" | "Under Alabama's hands-free law, when is holding a phone while driving a violation?" Key D: "When an officer also sees you swerve, cross lanes without a signal or otherwise drive improperly" (distractors: only in a school zone, only under 18, only after dark). src: MAN p. 16; 32-5A-350.1 via Cullman Tribune | Statute makes holding a violation only with observed improper driving; old key not defensible |
| AL-122 | Option A "A suspension of 90 days to 6 months"; exp "90-day to 6-month" | "A suspension of 3 to 6 months"; exp updated; src adds 28-3A-25 | 28-3A-25(c) says 3 to 6 months. Key unchanged (A) |
| AL-130 | exp "Since 2019, all occupants..." | "All occupants must be buckled; a back seat violation is secondary." | No years in book text |

Quiz-flagged state questions: every one (AL-043, 044, 049, 050, 053 to 055, 068, 069, 074 to 076, 084, 085, 088 to 090, 094, 095, 099 to 101, 110 to 112, 127 to 129, 143, 144, 147) is taught in its chapter's box. `check_bank.py`: BANK PASSED. `originality_check.py check state/AL/inserts.md`: PASSED (0.10%). AL build: QA PASSED, ORIGINALITY PASSED, 196 pages.

## Core text vs Alabama law

1. `core/ch03.md` 3.6 lane control table: "Steady yellow X | Leave this lane safely; it is about to close" (MUTCD meaning). The Alabama manual (p. 56) says a steady yellow X lets you drive in the lane with caution, and AL-052 is keyed that way. The hov insert now says "use it only with caution, ready to leave it", but the ch 3 table still reads differently from the AL key. Suggested core fix: hedge the yellow X row ("Prepare to leave this lane; some state manuals say use it with caution") or move it to an insert.
2. `core/ch13.md` 13.6: "Chapter 1 and the box in 13.3 give the waiting period." Neither the AL Chapter 1 nor the road_test insert gives one (ALEA publishes none that we found). Not a legal contradiction; the sentence points to missing text.
3. `core/ch03.md` 3.4: "Whether you may ever turn on a steady red arrow ... the Alabama rule box in Section 3.2 tells you." Consistent with the new turn_on_red wording.
4. No other core sentence near an insert contradicts Alabama law (checked 2.6, 2.7, 3.2 to 3.6, 4.6, 4.7, 5.1, 5.6, 5.8, 5.9, 6.2, 6.3, 6.5, 7.3, 7.9, 8.5, 9.2, 10.1, 10.8, 10.9, 11.2 to 11.4, 11.7, 12.3, 12.5 to 12.10, 13.3 to 13.6, driving log).

## Unresolved

- 32-5A-350.1 full official text not fetched (Justia, FindLaw and the legislature site all failed). Wording rests on the ALEA manual and the statute quote in news and SB239. Whether texting has a separate ban without the swerving element is not confirmed, so the insert only advises against texting.
- MAN p. 33 (48 hours / 20 days) and p. 32 (old texting fines) are out of date versus statute. A test question drawn from the manual could use the old figures; the book follows the statute.
- Child restraint age: statute and MAN list say seat belt "until 15 years of age"; MAN intro says "through age 15". Insert table says "Until age 15"; seat_belts box and AL-133 say "through age 15". Left as the manual teaches; flag to owner if a single phrasing is wanted.
- Open container fine (32-5A-330) and crash reporting not re-fetched beyond the writer's FindLaw and MAN logs.
