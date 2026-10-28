# New York fact check A: Chapter 1 and ch 1 bank questions

Checker A, 2026-10-28. Scope: `state/NY/ch01.md` and the 40 ch 1 questions in `bank/NY.json` (NY-001 to NY-040). Sources read: dmv.ny.gov pages via WebFetch, the NY Driver's Manual MV-21 (Drive copy 1ltO6DCUT3mMDRSa7gG2yLBbuOIvKKNkD, undated), VTL 501 and 501-b on nysenate.gov, NYSED driver education forms page. Short names as in `sources.md`.

## Result

No wrong answer keys. No legal errors in the quiz questions. One outdated legal statement in the chapter text fixed (proof of employment). One wording alignment (Green Light law). All 40 ch 1 questions have one defensible answer, a correct key, and are taught in Chapter 1; nothing in the chapter contradicts a key.

## Changes to state/NY/ch01.md

| Section | Old | New | Reason and source |
|---|---|---|---|
| 1.8 | "Driving to work alone needs proof: upstate, a dated letter from your employer, or on Long Island the **Certificate of Employment (MV-58A)**." | "Driving to work alone needs proof: carry a **Certificate of Employment (MV-58A)** filled out by your employer." | The current GDL page requires a filled-out MV-58A in both the upstate and the Long Island sections ("Driver must also have in their possession a filled-out Certificate of Employment (MV-58A)"). Only the older, undated manual allows an upstate employer letter. VTL 501(3)(e) requires signed documentation in a form set by the commissioner. Following the newer source. https://dmv.ny.gov/node/9371 ; https://www.nysenate.gov/legislation/laws/VAT/501 |
| 1.2 | "regardless of citizenship or immigration status" | "regardless of citizenship or lawful status" | Matches the DMV wording exactly and stays neutral. https://dmv.ny.gov/driver-license/driver-licenses-and-green-light-law |

Word count after edits: 2,281 (target 2,000 to 2,300). No em or en dashes. No years.

## Question fixes (bank/NY.json)

| ID | Old | New | Reason |
|---|---|---|---|
| NY-038 | stem "...regardless of citizenship or immigration status?" | "...regardless of citizenship or lawful status?" | Match the chapter and the DMV wording. Key B unchanged. |

No other ch 1 IDs touched. The bank file was re-read immediately before the write; only NY-038 changed (the writer also added a final newline).

## Verified as printed (no change)

- Permit test: 20 questions, 14 to pass, at least 2 of 4 sign questions (MAN Ch. 1, Vision and Knowledge Tests). 20 languages (PERMIT lists them). Online test: 80 percent overall and 50 percent of sign questions, webcam, retry after 6 hours, office visit to finish, parent or guardian supervises minors (ONLINE). Three business days of review (PERMIT). OKTA from 15 years 11 months (MAN Ch. 1).
- Vision 20/40 in at least one eye, with or without lenses (MAN).
- Junior permit chart (MV-500H 11/21): upstate any supervisor 21+ by day, parent/guardian/driver ed teacher/instructor at night; Long Island those people by day, no driving at night; NYC those people in a dual-control car by day, no driving at night. One passenger under 21 not family (unless supervisor is parent, guardian, teacher or instructor). Only supervisor in front. Restricted roads list correct.
- Junior license chart (GDL page): upstate alone by day, at night only home to work or a school course, otherwise supervised by parent, guardian, teacher or instructor; Long Island day and night exception lists (night list drops employment, keeps farm work); NYC no driving under any circumstances; 60-day suspension for one serious (3+ point) or two other violations; 120 days for phone or texting; senior license at 17 with driver education (MV-285); advice to wait until 18 for NYC.
- 50 hours, 15 after sunset, parent or guardian signs MV-262, driver ed hours count (MV-262 rev. 3/25). 10 hours in moderate to heavy traffic is a manual recommendation, printed as such.
- 5-hour course: no driving; classroom and live virtual at 16+, self-paced online at 18+; MV-278 valid one year; online course reported electronically (PLC). Driver education replaces it; student certificate is MV-285 (GDL; MAN).
- MV-283: per NYSED, the MV-283 is a card issued to driver education teachers, not a student certificate. The chapter correctly does not mention it. https://nysed.gov/career-technical-education/driver-and-traffic-safety-education-forms
- Six months on the junior permit, suspended time excluded (MAN Ch. 2; ROAD).
- Road test: booking 1-518-402-2100, 3 to 5 weeks; MV-278 original, MV-262 each test; accompanying driver over 21 if the applicant drives there; only that driver in the car; 14-day wait; extra fees after two failed tests; results after 6 p.m.; interim license; photo license in about 2 weeks (ROAD).
- Probation 6 months for drivers licensed at 18+; 60 days for DWAI (alcohol), speeding, reckless driving, following too closely, speed contest or any two violations; 120 days for phone (MAN Ch. 2).
- New residents: 30 days; 90 days of residence presumptive; exchange for U.S. state, territory, federal district or Canadian province license issued at least 6 months ago and valid or expired less than 24 months; vision test; surrender (XCH). Newer XCH 24-month window beats the manual's one year.
- Foreign licenses (non-Canadian): written test, 5-hour course, road test, vision; license handed to the examiner (DINY; MAN). IDP optional but helpful (DINY).
- Fees (FEES, node/941): 16 to 16.5 $80.00 / $90.00; 17 to 17.5 $92.50 / $102.50; 21+ $64.25 to $67.50 / $73.25 to $77.50; Enhanced $30 extra; MCTD = five boroughs plus seven counties.
- Points changes effective Feb 16, 2026 (school bus 8, work zone speeding 8, alcohol or drug 11, due care 5, speed contest 5, look-back 24 months; phone stays 5). Chapter 1 cites no point values other than the "3 or more points" junior rule, which is unchanged. https://dmv.ny.gov/news/dmv-reminds-new-yorkers-of-updated-point-values-for-driving-violations

## Open items

1. **Online permit test eligibility.** PERMIT says the online option is for applicants under 18; ONLINE describes an MV-264 attestation for applicants 18+. The chapter does not state an age limit, so it is safe either way.
2. **Long Island junior permit supervisors.** The older manual chart also lists a person designated in writing by the parent; MV-500H (11/21) does not. The chapter follows MV-500H. The GDL page lists such a designee for Long Island junior license supervision; the chapter's "otherwise supervised" covers it without naming who.
3. **Upstate employer letter.** If the owner wants to keep the manual's upstate letter option, it needs a current DMV source; none found.
