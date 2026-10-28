# California fact check A (Chapter 1 and ch 1 bank questions)

Checked 2026-10-28. Scope: `state/CA/ch01.md` and the 47 ch 1 questions in `bank/CA.json`. Sources: dmv.ca.gov pages (fetched today), California Driver's Handbook DL 600 (Drive copy, Sections 2 and 3), Vehicle Code on california.public.law, 13 CCR 15.02 (Justia).

## Wrong answer keys
None. All 47 ch 1 keys are correct against the sources below.

## Chapter changes

| Where | Old | New | Reason and source |
|---|---|---|---|
| 1.4 table, Questions | Multiple choice; DMV does not publish the count | Multiple choice; current DMV pages give no count | DMV has published counts, only not on current pages (see Question count below). |
| 1.4 table, To pass | 80 percent correct | 80 percent; under 18, miss no more than 8 | DMV Fast Facts FFDL 19 (rev. 7/2019, live on dmv.ca.gov): "To pass the knowledge test, you may miss no more than 8 questions." https://www.dmv.ca.gov/portal/file/ffdl_19-pdf/ |
| 1.4 mock paragraph | Because DMV does not publish its question count | Because current DMV pages give no question count | Same as above. |
| 1.8 What the Examiner Scores | backing (including parallel parking) | backing straight along a curb for about three car lengths | Error. The DPE backing criterion is "Parallel (B)": back in a straight line for 3 vehicle lengths within 3 feet of the curb, no more than 1 correction. It is not parallel parking. https://www.dmv.ca.gov/portal/handbook/driving-test-criteria/driving-performance-evaluation-dpe-scoring-criteria/ |
| 1.10 Moving from another state | DMV's steps for a valid out-of-state license do not list a drive test. | DMV may waive the drive test once it checks your out-of-state record and finds no suspension or hold. | 13 CCR 15.02(c): DMV may waive the behind-the-wheel test for an applicant presenting an expired or unexpired license from another state, territory or possession after a Problem Driver Pointer System check shows no holds, stops or other impediments. https://regulations.justia.com/states/california/title-13/division-1/chapter-1/article-2/section-15-02 . Assembly Transportation analysis of AB 639 (2023) says the same. HB Section 2: only applicants without a license from California or another state must get a permit before the drive test. |
| 1.3 Fees | Driving schools set their own prices for driver education and training. | Driving schools set their own prices. | Trim to keep the chapter under 2,300 words (now 2,298 by `wc -w`). |

## Question fixes

| ID | Old | New | Reason |
|---|---|---|---|
| CA-027 (stem) | Under the passenger limit, which person may ride with a provisional driver who is carrying a 17-year-old friend? | A provisional driver in the first 12 months wants to drive a 17-year-old friend. Who must also be in the car to make the trip legal? | "May ride with" was ambiguous (a 21-year-old may legally ride along; they just do not lift the limit). Key A unchanged. VC 12814.6(b)(1); HB Section 2. |

## Knowledge test question count: verdict

**Official DMV source exists, but dated; not stated on any current DMV page.**

- DMV research report CAL-DMV-RSS-06-221, *Evaluation of the Class C Driver License Written Knowledge Tests* (December 2006), hosted on dmv.ca.gov: the minors' original test (DL 5T) "has five forms, each with 46 questions" with "eight errors" allowed (38 to pass); adult originals "complete all 36 questions" with "six errors" allowed (30 to pass); renewals take the first 18 (3 errors). https://www.dmv.ca.gov/portal/file/evaluation-of-the-class-c-driver-license-written-knowledge-tests/
- DMV Fast Facts FFDL 19, Provisional Licensing (rev. 7/2019), live on dmv.ca.gov: minors "may miss no more than 8 questions". No count given, but consistent with 46/38. https://www.dmv.ca.gov/portal/file/ffdl_19-pdf/
- Current pages (Instruction Permits, Driver's Licenses, Teen Drivers, Online Learning, all modified 2026) and HB Section 3 give no count; the permits page gives "a passing score is 80%". DMV press release of 2023-12-28 gives no count.
- Note: 38 of 46 is 82.6 percent and 30 of 36 is 83.3 percent, so the 80 percent figure and the error allowances do not match exactly.
- Recommendation for mock sizing: 46 questions (38 to pass) for the teen audience is defensible as DMV-documented; it is not confirmed current. Owner decision. The chapter now says current DMV pages give no count and states the 8-miss allowance; if mocks move to 46, update the mock paragraph in 1.4 and `state/CA/mocks.json`.

## Other checks (confirmed, no change)

- Out-of-state license holders: vision and knowledge test required (DL page: "Pass a vision exam", "Pass the knowledge test(s)", three attempts). CA-010 key correct.
- Foreign license: knowledge and drive tests, insurance proof, accompanying driver to and from the drive test (DL page; PERMIT FAQ). No reciprocity: AB 639 analysis: foreign nationals "regardless of their country of origin" take both. CA-035, CA-036 correct.
- AB 60: DMV AB60 page (modified 2026-08-07): for people unable to prove legal presence, proof of identity and residency, knowledge test in more than 40 languages, drive test, driver education at 15 to 17 1/2. VC 12801.9: not evidence of citizenship or immigration status; anti-discrimination for businesses, employers and government entities. Card notice: VC 12801.9's own notice was replaced from the 2023 card revision by the VC 12800.5(b)(2) notice for all non-REAL ID licenses, which still says "not acceptable for official federal purposes", so the chapter text and CA-038 stay correct. The AB60 page says a holder "may be able to upgrade to a REAL ID" if they qualify (i.e., after gaining status); the chapter's "it cannot be a REAL ID" refers to the AB 60 card itself and is correct.
- Provisional rules: VC 12814.6(a)(2) 6 months, (a)(3)(B) 30 classroom hours and 6 behind the wheel, (a)(4) 50 hours with 10 after dark and parent certification, (b)(1) 11 p.m. to 5 a.m. and passengers under 20 for 12 months, (b)(2) medical, school, work and family exceptions with signed notes. HB Section 2 matches. Two and three at-fault actions per HB Section 7 (statute (g)(2) counts points; the book follows the handbook wording).
- Fees (FEES, modified 2026-08-07): $46 original, $9 drive retest, $37 replacement. The DL page still says $7 retest; the fees page wins.
- Retest waits: HB Section 3, 7 days (knowledge) and 14 days (drive) not counting the failure day; TEEN page says 8 and 15 days (same rule counted inclusively).
- Online testing: Online Learning page (modified 2026-10-13): eLearning only for eligible noncommercial Class C renewals; "Original driver license applicants" do not qualify. DMV release 2023-12-28 confirms the earlier at-home knowledge test (adults from 2022, minors from September 2023). The book's statement that first-time applicants test in an office is correct; the book gives no end date (no year in the book).
- Vision: VISION page 20/40 both eyes or 20/40 and 20/70; DL 62; 20/200 or worse "may not be scheduled for a drive test".
- Drive test: HB Section 3 (pre-drive items, donut tire, rescheduled if the car fails, only examiner, ADAS off, backup camera with visual checks, rental contract, two instructions). DPE critical errors list matches the chapter.
- VC 12505(c) 10 days for new residents; VC 12502(a)(1) nonresident over 18 with a home-jurisdiction license.

## Unresolved
- Question count: only dated official sources (2006 report, 2019 fast fact). Owner to decide mock size (25 now).
- "No separate sign section" (1.4): no DMV source describes a sign section; none states its absence either. Low risk, left as is.
- End date of at-home permit testing (passrates.uk cites an archived DMV page, 2025-01-03): web.archive.org is blocked here, not verified; not in the book.
- Statute (12814.6(g)) triggers the 30-day restriction and suspension by violation points; the handbook (and book) says "at-fault collisions or convictions". Wording kept to the handbook.
