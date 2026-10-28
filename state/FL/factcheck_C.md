# Florida fact check C (state upgrade since cb15098)

Scope: 5 new inserts (emergency_vehicles, headlight_use, police_stop, underage_alcohol, driver_record), the 23 rewritten inserts (meaning vs cb15098), newly quiz-flagged state questions, new questions FL-143 to FL-158. Date: 2026-10-28.

## Verified (no change needed)

| Item | Source |
|---|---|
| Points: 3 (15 or less over, other moving), 4 (16+ over, signal violation, school bus, reckless), 6 (speed causing crash; school bus with serious injury); 12/12 up to 30 days, 18/18 up to 3 months, 24/36 up to 1 year | https://www.flsenate.gov/Laws/Statutes/2025/322.27 (3)(a) to (d) |
| Under 21 possession: 2nd-degree misdemeanor, repeat 1st-degree; no license sanction in 562.111 | https://www.flsenate.gov/Laws/Statutes/2025/562.111 |
| Misrepresenting age: 2nd-degree misdemeanor; up to 40 hours public service if a Florida license or ID card was used | https://www.flsenate.gov/Laws/Statutes/2025/562.11 (2)(a), (c) |
| 322.056 covers only ch. 893 drug offenses (no alcohol license sanction) | https://www.flsenate.gov/Laws/Statutes/2025/322.056 |
| Fake license: 3rd-degree felony | https://www.flsenate.gov/Laws/Statutes/2025/322.212 (1)(a), (6) |
| Fleeing or refusing to stop: 3rd-degree felony; revocation 1 to 5 years | https://www.flsenate.gov/Laws/Statutes/2025/316.1935 (1), (5) |
| License in possession, digital license allowed, printed card if not verifiable | https://www.flsenate.gov/Laws/Statutes/2025/322.15 (1) |
| Emergency vehicle: parallel to closest edge, clear of intersection, stop until passed unless officer directs | https://www.flsenate.gov/Laws/Statutes/2025/316.126 (1)(a) |
| Headlamps sunset to sunrise incl. twilight, rain, smoke, fog | https://m.flsenate.gov/Statutes/316.217 (1) |
| Flashing lights: exceptions incl. stopped/disabled and extremely low visibility on 55+ mph roads | https://m.flsenate.gov/Statutes/316.2397 (7) |
| Work zone: doubled fines, civil penalties up to $1,000; police may stop you at any time for an equipment inspection; BDI election limits | FL handbook (Drive 1bDRChO0h4R1B1OfBvwqpp-wG5eRvamPX) pp. 17, 30 (Penalties), 38 (Equipment Standards) |
| Third-party random retest covers written and driving skills portions | https://www.flsenate.gov/Laws/Statutes/2025/322.56 (3)(e) |
| Rewritten inserts: meaning unchanged except school_zone (below) | diff vs cb15098 |
| All 32 quiz-flagged state questions (ch 2 to 13) are taught in their chapter's state box, except FL-140 (fixed below) | out/FL/Permit_Path_Florida.md |

## Changes

| Where | Old | New | Reason |
|---|---|---|---|
| inserts school_zone | "the court may also send you to a driving course" | "you may also have to take a driving course" | Rewrite added "the court"; handbook says only "you can be required to complete a driving course"; s. 318.18(3)(c) has no course requirement. Restores the original meaning. |
| FL-140 (ch 13, quiz) stem | "You passed the Florida knowledge exam with a third-party administrator" | "You passed the Florida driving skills test with a third-party administrator" | Ch 13 box teaches the random retest for the skills test, not the knowledge exam; s. 322.56(3)(e) covers both, so the key stays A. src now cites 322.56(3)(e). |

## Open items
- Texting in a school zone: s. 322.27(3)(d) adds 2 points; handbook p. 30 table says +3. Not printed in any box (already logged in sources.md).
- Core Chapter 11 says under-21 alcohol and fake ID offenses "can cost you your driver's license"; no Florida statute read provides that (562.111, 562.11, 322.212, 322.056). Core owner item.
- Build: FL passed QA and originality.
