# Texas fact check B: inserts and chapter 2 to 13 questions

Checked 2026-10-28. Scope: `state/TX/inserts.md` (all 23 keys) and every `bank/TX.json` question with `ch` other than 1 (TX-043 to TX-144, 102 questions). Each insert was read in place in `core/chNN.md` (and `core/95_driving_log.md`) around its marker. The ch 1 questions were not touched; the bank was re-read right before the write and only the IDs below were changed.

Sources:
- **DL-7**: Texas Driver Handbook DL-7, rev. Jan 2026, Drive copy 1QFLw84NB77SFOD1HjAsHI5no5CaC8h40 (manual page numbers)
- **TC n**: Texas Transportation Code section n, read on texas.public.law (`https://texas.public.law/statutes/tex._transp._code_section_n`) or law.justia.com (`https://law.justia.com/codes/texas/transportation-code/...`): 541.302(13), 544.007, 545.066, 545.102, 545.156, 545.157, 545.412, 545.413, 545.414, 545.425, 545.4251, 545.4252
- **PC n**: Texas Penal Code section n on texas.public.law: 49.04, 49.031
- **CRASH**: https://www.txdot.gov/driver/laws/crash-reports.html
- **BEXAR**: https://www.dps.texas.gov/section/vehicle-inspection/faq/bexar-county-emission-inspections
- **15.54**: 37 TAC 15.54, https://www.law.cornell.edu/regulations/texas/37-Tex-Admin-Code-SS-15-54
- **MUTCD**: FHWA MUTCD 2009, Section 4D.04 (the base of the Texas MUTCD), https://mutcd.fhwa.dot.gov/htm/2009/part4/part4d.htm

## Changes to inserts.md

| Key | Change | Reason | Source |
|---|---|---|---|
| move_over | "On a road with two or more lanes your way, leave the lane next to them. Otherwise slow to 20 mph below..." to "You must either leave the lane next to them (on a road with two or more lanes your way) or slow to 20 mph below the limit..." | Legal error: the statute gives the driver a choice (vacate the lane **or** slow down); the old text made changing lanes the duty and slowing the fallback | TC 545.157(b); DL-7 pp. 23, 46 |
| turn_on_red | "Texas law grants these turns only on a steady red light, not on a red arrow" to "The law that grants these turns speaks only of a steady red light and says nothing about a red arrow. Treat a red arrow as no turn..." | 544.007(d) is silent on red arrows; the old line claimed more than the statute says. The no-turn advice stands: under the MUTCD a steady red arrow means do not enter for that movement unless a sign permits the turn, and DL-7 p. 25 gives turns on red only for a steady red light | TC 544.007(d), (f); MUTCD 4D.04 para. 3; DL-7 p. 25 |
| u_turn | "could not see you in time" to "cannot see your car from **500 feet** away" | Statute now read: the visibility distance is 500 feet | TC 545.102 |
| crash_reporting | Added "TxDOT keeps no driver reports; keep your own." Light trims to stay at 89 words ("show your license if asked" kept) | Core ch10 step 6 says to report to "your state agency when the law requires it"; Texas has no driver report any more (SB 312, 85R, eff. 2017-09-01; TxDOT destroys CR-2s), so the box now says so instead of leaving the reader to look for a form | CRASH |
| phone_laws | "Texting is allowed only while stopped or to report an emergency" to "The ban does not apply while you are stopped, and hands-free (voice) use, navigation and emergency calls are allowed"; bus line now "unless stopped" | The old "only" was wrong: hands-free use, navigation, music and emergency use are statutory defenses. The bus rule applies only while the bus is not stopped | TC 545.4251(b), (c); TC 545.425(c) |
| vehicle_rules | "17 counties ... with Bexar County (San Antonio) being added" to "18 counties around Houston, Dallas and Fort Worth, Austin, El Paso and San Antonio" | Bexar emissions testing starts 2026-11-01, before the book is on sale; "being added" would be stale at once (no year allowed in the book) | BEXAR |
| road_test | Added "Only you and the examiner (plus an interpreter if needed) ride in the car." Trimmed wording to stay at 89 words | Core ch13 line 53 says "the box below says who may ride in yours"; the insert did not | 15.54(2)(D) |

## Inserts verified without change

| Key | Verified against |
|---|---|
| school_zone | Speed while lights flash or posted hours: DL-7 p. 31. Handheld ban in a school crossing zone unless stopped or hands-free; zone exists only "during the time the reduced speed limit applies"; emergency call defense: TC 545.425(b), (d); TC 541.302(13); TC 545.4252 |
| work_zone | DL-7 pp. 36 to 38 |
| school_bus | Either direction, stop before reaching, three release conditions, separate roadways incl. left turn lane exclusion, no distance in feet, $500 to $1,250, repeat in 5 years $1,000 to $2,000, suspension up to 6 months on a repeat: TC 545.066 |
| speed_limits | DL-7 p. 46 |
| following_distance | DL-7 pp. 45, 52 |
| hov | DL-7 p. 30 |
| parking_rules | DL-7 pp. 42 to 44 |
| bicycle_passing | DL-7 pp. 53, 62; no statewide distance found in Chapter 545 or 551 |
| bac_limits | DL-7 pp. 55 to 58 |
| implied_consent | DL-7 pp. 57 to 58 (180 days, 730 days; 90 days, 365 days) |
| dui_penalties | DL-7 Table 31 p. 58; PC 49.04(a), (b) (72 hours; 6 days with open container); PC 49.031 (Class C, so fine up to $500) |
| seat_belts | TC 545.413(a), (b), (d); TC 545.414; DL-7 p. 64 |
| child_restraints | TC 545.412(a), (b) |
| supervised_hours, signal_distance, headlight_dimming | DL-7 pp. 1 to 3, 38 to 39, 47 |

## Question fixes

| ID | Field | Old | New | Reason |
|---|---|---|---|---|
| TX-085 | a (key A) | Leave the lane next to it, if you can do so safely | Leave the lane next to it, or slow to 20 mph below the limit | Stem asks what the law **requires**; the law requires either move, so the key named only one of two lawful options. Key stays A |
| TX-085 | exp, src | "you must vacate the lane closest..." | "you must either vacate the lane closest to the stopped vehicle or slow to 20 mph below the limit"; src adds TC 545.157(b) | Same legal error as the insert |
| TX-133 | q | ...a 15-year-old passenger... | ...a 14-year-old passenger... | Two defensible answers: a passenger 15 or older can be fined $25 to $50 personally (TC 545.413(a)), so "the driver" was not the whole answer for a 15-year-old. At 14 only the driver is fined. Key stays A |
| TX-133 | exp | ...assessed to the driver. | ...assessed to the driver; passengers are fined themselves only from age 15. | Explains the age line |
| TX-083 | exp | "Texas law allows turns after a stop only on a steady red light, not on a red arrow." | "The Texas turn on red law covers only a steady red light; a red arrow means do not make that turn." | Do not claim more than 544.007 says. Key C stands (MUTCD 4D.04; core ch03 table) |
| TX-078 | q | a driver over 18 | a driver 18 or older | An 18-year-old falls under the adult rule; "over 18" left them out |

All other keys checked correct with one defensible answer. `python3 tools/check_bank.py bank/core.json bank/TX.json`: BANK PASSED (TX 144 questions, A 36, B 36, C 36, D 36). `python3 tools/originality_check.py check state/TX/inserts.md`: ORIGINALITY PASSED (0.30 percent, no 12-word runs). All inserts 89 words or fewer; no em or en dashes.

## Core text vs Texas law

1. **ch04 line 95 (emergency vehicles):** "You must also stop for an emergency vehicle on the other side of a two way road, unless a median or barrier separates you." TC 545.156 and DL-7 p. 22 say only to pull to the right edge and stop on the approach of an emergency vehicle; neither addresses opposite direction traffic or medians. Not a direct contradiction, but the claim has no Texas source. Core owner to soften to "many states" or leave.
2. **ch10 step 6 (crash reporting):** "Report the crash ... to your state agency when the law requires it." Texas drivers no longer file a report (CRASH). Covered by the new sentence in the insert; no core change needed.
3. **ch13 line 53:** the box now says who may ride (fixed in the insert).
4. **ch03 red arrow:** core says treat a red arrow as a firm no unless the state box says otherwise; the Texas box agrees. No conflict.

## Open items

1. **DL-7 is out of date on inspection.** DL-7 Ch. 2 p. 15 (rev. Jan 2026) still says every Texas vehicle must be inspected each year. The insert and TX-138 follow the law (safety inspection ended for non-commercial vehicles 2025-01-01). If DPS exam items follow the handbook, a student may meet the old rule on the test. Owner decision; the book is right on the law.
2. **Tire tread 2/32 inch (TX-141, vehicle_rules)** is from DL-7 p. 15, which sits in the outdated inspection chapter. It is still printed in the current handbook, so it is kept.
3. **Minor DWI license suspension.** DL-7 Table 30 gives a minor's first DWI a 365-day suspension (90 days with interlock), versus 90 to 365 days for adults. The insert's adult table range still covers it; not added (word limit).
4. **Weakly taught app-only questions (quiz false):** TX-076 (mileposts every mile; core ch02 mentions mile markers but not their spacing), TX-065 (ramp meter advance sign with flashing yellow lights; core ch03 covers ramp meters but not this sign), TX-057 (far left lane of a double left turn must turn left; core ch05 says lane signs show which lanes may turn), TX-056 (two way left turn lane, tagged ch 2 but taught in ch 3). Keys are correct per DL-7 pp. 29 to 34; left for the owner to retag or keep.
5. **Statutes site** statutes.capitol.texas.gov still blocked; sections were read on texas.public.law and law.justia.com, which note they may lag the official text.
