# Missouri fact check A: Chapter 1 and ch 1 bank questions

Checked 2026-10-28. Scope: `state/MO/ch01.md`, `bank/MO.json` IDs MO-001 to MO-040 (ch 1). Guide = Missouri Driver Guide, rev. August 2026 (Drive 1T7sMnlclbbPk2DSH86ljtDJGG9QepGoz).

## Sources used
- Guide pp. 2, 3 to 8, 15 to 21 (text read in full for Chapter 1 and 2 topics).
- MSHP Driver Examination FAQs: https://apps.mshp.dps.mo.gov/MSHPWeb/PatrolDivisions/DVSD/DE/faqs.html
- MSHP Driver Examination home: https://apps.mshp.dps.mo.gov/MSHPWeb/PatrolDivisions/DVSD/DE/index.html
- MSHP, Modernized Testing System DOR-FUSION: https://statepatrol.dps.mo.gov/divisions/driver-and-vehicle-safety-division/modernized-testing-system-dor-fusion
- DOR, Driver License and Nondriver ID (fees): https://dor.mo.gov/driver-license/resources/license.html
- DOR, Driver License General FAQs: https://dor.mo.gov/faq/driver-license/general.html
- 12 CSR 10-24.452 (sign test, 6 signs, 4 to pass): https://regulations.justia.com/states/missouri/title-12/division-10/chapter-24/section-12-csr-10-24-452
- 12 CSR 10-24.090 (vision restrictions): https://law.cornell.edu/regulations/missouri/12-CSR-10-24-090
- RSMo 302.178 and 302.173 (Justia, 2025 statutes): https://law.justia.com/codes/missouri/title-xix/chapter-302/section-302-178/ , https://law.justia.com/codes/missouri/title-xix/chapter-302/section-302-173/
- revisor.mo.gov: every section URL fetched returned RSMo 302.525 instead of the requested section, so Justia was used as the fallback for 302.178 and 302.173. 302.130 could not be read on either site; permit supervisor rules rest on Guide p. 15.

## Confirmed (no change)
- Written test 25 questions, 20 to pass (Guide pp. 2, 18; DOR FAQ "80% (20 questions out of 25)"). Up to two written tests a day (MSHP FAQ). Formats: touch screen, paper, oral by computer or examiner (MSHP FAQ). Tests free for non-CDL (MSHP FAQ). No appointment for non-CDL tests (MSHP FAQ and DE home).
- Road sign test: six signs, four to pass (12 CSR 10-24.452(2)). All applicants, including transfers, take sign and vision tests (DOR FAQ).
- Vision: 20/40 either or both eyes; 55 degrees each eye or 85 in one; 20/160 and 70 degrees cutoffs; eye form (Guide pp. 18 to 19). Daylight-only and lens restrictions confirmed (12 CSR 10-24.090(6)).
- Permit supervisors: under 16 list incl. 25+ licensed 3 years with written permission, disabled parent may name two; 16+ licensed 21+; front seat; all belted (Guide p. 15).
- 182 days from day after issuance; 40 hours incl. 10 at night; no alcohol conviction 12 months, no traffic conviction 6 months (Guide p. 16; RSMo 302.178.1(3) to (6) has six months, 40 hours, 12 and 6 month record; the 10 night hours are Guide only).
- Intermediate: passengers under 19 not immediate family, 1 then 3; farm work exception; 1 a.m. to 5 a.m. with school, job, emergency exceptions and licensed 21+ companion (Guide p. 16; RSMo 302.178.2 and .3).
- Full license at 18: valid intermediate, not suspended, no alcohol offense or traffic conviction 12 months; vision and road sign tests (Guide p. 17; DOR FAQ). Note: RSMo 302.178.6 says "without further examination, other than a vision test"; the Guide and DOR FAQ add the road sign test, which 12 CSR 10-24.452(1) requires of every new or renewal applicant. Book follows the Guide.
- New residents: valid or expired no more than 184 days, vision and sign tests only, surrender old license (Guide pp. 6, 18; DOR FAQ "from another U.S. state"; DOR license page).
- Fees: permit $10, intermediate $14, full $16.50 (3 yr) / $33 (6 yr); card convenience fee 2.0% + $0.25; cash, checks, money orders, cards (DOR license page; Guide p. 8).
- Driving test: car need not be yours but registered and insured (MSHP FAQ); equipment, only examiner rides, 25 x 7 ft space, 18 in, two minutes, 2 right and 2 left turns, hill park, over 30 points fails, automatic fails, result form not a license, one test a day, three failures need training and DOR approval (Guide pp. 19 to 21). Parallel parking only a few points (MSHP FAQ). Fraud, up to one year (Guide p. 21).

## Changes to ch01.md
1. Section 1.4 table, Languages: "20 languages, plus a sign language video version" changed to "20 languages, including a sign language video version". The FUSION page says "a total of 20 languages, which includes a newly created sign language video version". The old text implied 21.
2. Section 1.8: "some stations let you book the driving test online, and the Patrol recommends it where offered" changed to "Tests are given as examiners are free, and you can also book a driving test online." No MSHP page recommends booking; MSHP says appointments are not needed for non-CDL skills tests, tests are given "based upon personnel availability and volume of test applicants", and links to "Schedule a Driver Skills Test" (DE home page above).

Word count before the quiz: 2,223 (in range). No em or en dashes, no years.

## Question fixes (bank/MO.json)
| ID | Old | New | Reason |
|---|---|---|---|
| MO-037 | b: "20, plus a sign language video version" | b: "20, including a sign language video version" | Keyed answer counted 21 languages; FUSION says the 20 include the sign language video. Key (B) unchanged. |

All other ch 1 keys (MO-001 to MO-040) checked against the sources above: one defensible answer each, correct key, taught in the chapter, no contradiction with the text.

## Checks run
- `python3 tools/check_bank.py bank/core.json bank/MO.json`: BANK PASSED.
- `python3 tools/originality_check.py check state/MO/ch01.md`: 0 shared sequences, PASSED.

## Unresolved
- Foreign licenses: RSMo 302.173 lets the director waive the knowledge and driving tests for a license from a country with a reciprocal agreement under 302.172. No DOR page lists any such country, and the DOR FAQ limits the waiver to licenses "from another U.S. state". The book's "expect the full four-part exam" stands; re-check if DOR publishes a reciprocity list. MO-039 (Brazil) unaffected unless Brazil is added.
- RSMo 302.130 (permit supervisors) not read on revisor.mo.gov or Justia (both failed); Guide p. 15 used.
- revisor.mo.gov returned 302.525 (effective Aug. 28, 2026, administrative alcohol suspension) for every section request. That section changed in 2026: a 30-day suspension plus 60-day restricted privilege, or 90 days with an interlock. Outside ch 1 scope, but the checker for the alcohol inserts should verify the book's "first 90-day suspension" wording against it.
- The "On the test" box lists "Points, alcohol limits for drivers under 21, and how a license is lost", which Chapter 1 does not teach (covered in core chapters via inserts). Not a factual error; left as is.
- License office processing fee amount still unverified (book gives no amount).
