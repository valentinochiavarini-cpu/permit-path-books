# Florida fact check A: Chapter 1 and ch 1 bank questions

Checker A, 2026-10-28. Scope: `state/FL/ch01.md` and the 42 ch 1 questions (FL-001 to FL-042) in `bank/FL.json`. Every claim in the chapter and every key was checked against the sources below. Handbook (HB) = Official Florida Driver License Handbook rev. 08/2023, Drive file 1bDRChO0h4R1B1OfBvwqpp-wG5eRvamPX.

## Sources read
- Fla. Stat. 322.1615 (2026), https://m.flsenate.gov/Statutes/322.1615 (history: s. 2, ch. 2025-104)
- Fla. Stat. 322.095 (2026), https://m.flsenate.gov/Statutes/322.095 (subs. (1) and (9))
- SB 994 (2025), ch. 2025-104, https://www.flsenate.gov/Session/Bill/2025/994/BillText/e2/HTML (effective July 1, 2025)
- FLHSMV Class E Knowledge Exam and Driving Skills Test: https://flhsmv.gov/driver-licenses-id-cards/licensing-requirements-teens-graduated-driver-license-laws-driving-curfews/class-e-knowledge-exam-driving-skills-test/
- FLHSMV teen GDL page: https://www.flhsmv.gov/driver-licenses-id-cards/licensing-requirements-teens-graduated-driver-license-laws-driving-curfews/
- FLHSMV teen FAQ: https://flhsmv.gov/driver-licenses-id-cards/licensing-requirements-teens-graduated-driver-license-laws-driving-curfews/frequently-asked-questions
- FLHSMV fees: https://www.flhsmv.gov/fees/
- English-only policy (effective 2026-02-06): https://www.hillstaxfl.gov/news/statewide-policy-change-all-florida-driver-license-exams-to-be-administered-in-english-only-beginning-february-6/ ; https://helpcenter.taxcollector.com/hc/en-us/articles/43175411104013-Driver-License-Exams-Administered-in-English-Only ("This includes written exams, oral exams and driving skills tests." "Language translation services for testing will no longer be permitted.")
- HB pp. 3 to 4 (residents, reciprocity), 8 to 9 (teen requirements, consent), 10 (code B), 19 (vision), 29 to 30 (points)

## Points checked hard (all confirmed)
| Point | Result |
|---|---|
| TLSAE only for 18+ | Confirmed: s. 322.095(1) (2026) "18 years of age or older", exemption if licensed in another jurisdiction or DOE driver ed; minimum 4 hours, s. 322.095(9). Amended by ch. 2025-104, effective July 1, 2025. |
| Teen driver education course | Confirmed: s. 322.1615(1)(c) as amended by SB 994 requires a department-approved driver education course meeting or exceeding DOE course 1900300; the TLSAE reference was struck. Chapter wording ("It replaced the old requirement...") is correct. |
| English-only exams | Confirmed, effective Feb 6, 2026, statewide incl. third parties; covers knowledge AND skills tests. Note: the FLHSMV exam page still lists six languages and an interpreter exception; it is out of date. |
| 50 questions, 40 to pass | Confirmed (EXAM page). |
| Online testing under 18 only, Parent Proctoring Form, random no-fee retest | Confirmed (EXAM page, FAQ). |
| Learner: 15, supervisor 21+ licensed in front passenger seat, daylight 3 months then until 10 p.m., violation = moving violation penalty | Confirmed s. 322.1615(1) to (4) (2026); TEEN. |
| 12 months or 18; no convictions 12 months (one if adjudication withheld); delay 1 year from conviction date | Confirmed TEEN, FAQ, HB p. 8. |
| 50 hours, 10 at night; parent, guardian or responsible adult 21+ | Confirmed TEEN, HB p. 8. |
| Curfews 16: 11 p.m. to 6 a.m.; 17: 1 a.m. to 5 a.m.; work or 21+ licensed driver exceptions; 3 points | Confirmed TEEN, FAQ, HB p. 30. |
| 6+ points under 18: Business Purposes Only 1 year | Confirmed HB p. 29. |
| Fees $48 (incl. learner's), $10, $20, $25, $6.25; learner to Class E free without name or address change | Confirmed FEES, FAQ. |
| Vision standards, 130 degrees, no telescopic lenses, code B | Confirmed HB pp. 10, 19. |
| Parental consent, stepparent only if adopted, signer may cancel | Confirmed HB pp. 8 to 9, FAQ. |
| Reciprocity list incl. Germany skills only, Canada if surrendered; vision still required; 30 days | Confirmed HB pp. 3 to 4. |

## Changes made

### Chapter (`state/FL/ch01.md`, 1.8 The Car Check)
- Old: "No passengers ride along, unless an interpreter is needed."
- New: "No passengers ride along, and interpreters and translation devices are no longer allowed."
- Reason: since Feb 6, 2026 the English-only policy covers driving skills tests and bans translation services for testing (sources above). The interpreter exception on the FLHSMV exam page predates the policy.

### Bank (`bank/FL.json`)
| ID | Old | New | Reason |
|---|---|---|---|
| FL-036 | b: "No one but the examiner, unless an interpreter is needed"; exp cited interpreter exception | b: "No one but the examiner"; exp: no other passengers, exams English only, translation services and devices not allowed; src adds English-only policy | Keyed answer stated a superseded rule (interpreter exception removed by the English-only policy). Key stays B. |

No other ch 1 question needed a change: all 42 keys verified correct with one defensible answer, each taught in Chapter 1, and no chapter text contradicts a key.

## Checks
- Word count after edit: 2,166 (target 2,000 to 2,300). No em or en dashes. No year in the chapter.
- `python3 tools/check_bank.py bank/core.json bank/FL.json`: BANK PASSED.
- `python3 tools/originality_check.py check state/FL/ch01.md`: 0 shared sequences, ORIGINALITY PASSED.

## Open items
- FLHSMV's own exam page still shows the old language list and interpreter exception; the English-only rule rests on the Jan 30, 2026 FLHSMV release as published by county tax collectors and news. Recheck flhsmv.gov before publishing.
- Driver education course length for teens is not set in statute (left out of the book, as the writer did). County pages and the FLHSMV FAQ still describe TLSAE for teens; the statute governs.
- Whether a TLSAE certificate completed before July 1, 2025 still satisfies the learner requirement is not stated on any primary source; the chapter tells readers to ask the service center. Fine as is.
- Newer handbook edition (post 08/2023) still not confirmed.
