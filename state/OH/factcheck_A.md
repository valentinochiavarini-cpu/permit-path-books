# Ohio fact check A: Chapter 1 and bank chapter 1 questions

Checker A, 2026-10-28. Scope: `state/OH/ch01.md` and the 42 `ch: 1` questions in `bank/OH.json` (OH-001 to OH-042). Other chapters' questions not touched.

Sources read:
- MAN: Ohio Driver Manual HSY 7607 10/25 (Drive 16-Z3HYqpZnD0mmZ_MLkdbnQ3Hf06YGyr), Sections 1, 6 (p. 26), 11, 12, 13 read in full.
- GDL: https://ohiobmv.gov/dl-gdl.aspx
- NEW: https://ohiobmv.gov/new-to-ohio.aspx
- FEES: https://www.ohiobmv.gov/doc-fees.aspx (last updated 9/30/2025)
- ORC 4507.05 (eff. 2026-03-20, HB 184), 4507.21 (eff. 2026-03-20, HB 184 and HB 434), 4507.071 (eff. 2015-07-01), 4507.10 (eff. 2000-06-01), 4507.101 (eff. 2000-09-01), 4510.31 (eff. 2025-04-09), 4510.02, 4511.205 (eff. 2018-10-29): https://codes.ohio.gov/ohio-revised-code/section-<number>
- OAC 4501:1-1-10 and 4501:1-1-20 (both eff. 2016-04-10): https://codes.ohio.gov/ohio-administrative-code/rule-<number>
- Ohio University ISSS, https://www.ohio.edu/international-student-scholar-services/resources/practical/driving (secondary, reciprocity list)

## Result

No wrong answer keys. No legal errors of substance. Three small text fixes and one stem fix.

## Verified (no change)

- Knowledge test: 40 multiple choice, 75 percent; online two attempts in six months, webcam computer, supervising adult for 15.5 to under 19; in person unlimited, one per day; wait one day (GDL says 24 hours). MAN p. 1; GDL.
- Languages list (10 incl. ASL), own interpreter at Driver Exam Station only. MAN p. 1.
- TIPIC: from 15 years 6 months; valid one year (ORC 4507.05(A), (C)); buy within 60 days (MAN p. 2).
- Supervisors: under 16 eligible adult (parent, guardian, custodian, instructor, 21+ in loco parentis) per ORC 4507.05(H)(1); 16+ licensed driver 21+; midnight to 6 a.m. under 18: licensed parent, guardian or custodian (ORC 4507.05(F)(2)) or a licensed 21+ driver named on notarized BMV 2438 (GDL; the statute has no form, the BMV page grants it). Kept as printed.
- Driver ed 24 + 8 and 50 hours (10 night) for every applicant under 21: ORC 4507.21(B) as amended eff. 2026-03-20 opens "each person under twenty-one years of age". Six-month TIPIC hold under 18 only: ORC 4507.071(A).
- 21+: no driver ed or affidavit (except initial limited term license holders); abbreviated adult course after failing road or maneuverability test unless a driver training course was completed in the prior 12 months: ORC 4507.21(C); 4 hour class or online plus 4 hours school driving or 24 hours with licensed 21+, max 4 hours a day, BMV 5789: MAN p. 44; GDL.
- Maneuverability: five markers, 9 x 20 ft, forward then reverse, deductions, instant fail items: MAN pp. 42 to 43. Pass unless "a minus score in excess of twenty-five points in either part": OAC 4501:1-1-10. Book's "lose up to 25 points and still pass" is correct.
- Under 21 retest wait two days: MAN p. 43; GDL.
- Probationary limits by months held, not age (ORC 4507.071(B)): first 12 months midnight to 6 a.m. and max 1 non-family passenger without parent, guardian (or custodian); after 12 months 1 a.m. to 5 a.m.; exceptions with BMV 2825 and 2826 (MAN p. 47). Ride-along order if licensed before 17 and violation within six months of issuance: ORC 4507.071(D).
- Under-18 device ban incl. hands-free; exceptions emergency, stopped outside lane, hands-free navigation; $150 + 60 days, then $300 + one year: ORC 4511.205.
- Under 18: two violations class E (3 months), three class C (1 year), OVI class D (6 months); reinstatement needs TIPIC, juvenile driver improvement program, driving test: ORC 4510.31(A), (E); ORC 4510.02(B); MAN p. 26.
- Vision: 20/40 unrestricted, to 20/70 daytime only, worse denied; 30 days to return: OAC 4501:1-1-20.
- Fees: TIPIC $26.50; first license 16 $28.75, 17 $27.50, 21+ 4 year $27.50, DR fee included: FEES.
- New residents: 30 days, residency triggers (NEW; MAN p. 50); out-of-state license valid or expired no more than six months, examination may be waived (ORC 4507.10(B)); vision screening required (NEW).
- Reciprocity: Canada, France, Germany, Japan, South Korea, Taiwan (MAN p. 3; Ohio University ISSS); ORC 4507.101 authorizes the waiver but lists no countries.
- Temporary resident 21+: driver ed, 50 hours, 14 days on TIPIC: MAN p. 3; ORC 4507.21(B)(1), (3).
- Pending bills not printed: SB 419 (136th GA) exists only "As Passed by the Senate"; Sub. HB 463 still in committee. Chapter 1 prints neither. Correct.

## Changes to `state/OH/ch01.md`

1. Section 1.3 fee table: "First license at 16 (four years)" changed to "First license at 16". A license issued under 21 expires on the 21st birthday (MAN p. 47), so a license bought at 16 runs about five years; the "4 year" label on FEES is the fee column, not the real term. The table also contradicted the sentence below it.
2. Section 1.4: "You have three choices:" changed to "You have these choices:". Only two bullets follow (manual lists three venues, the book merges two of them).
3. Section 1.6: "The adult who supervised you signs the Fifty-Hour Affidavit" changed to "Your parent, guardian or another eligible adult signs". ORC 4507.21(B)(2) requires the affidavit of an "eligible adult" as defined in (I) (parent, guardian, custodian, or certain 21+ adults), not any supervising driver.

Word count before the quiz: 2,294 (in range). No dashes, no years.

## Question fixes (`bank/OH.json`)

| ID | Old | New | Reason |
|---|---|---|---|
| OH-013 | Stem: "Which form does your supervising adult sign to certify your 50 practice hours?" | "Which form does your parent or guardian sign to certify your 50 practice hours?" | Same signer error as change 3 (ORC 4507.21(B)(2), (I)). Key B unchanged. Source line now adds ORC 4507.21. |

All other ch 1 keys checked against the sources above: one defensible answer each, taught in the chapter, no contradiction with the text.

## Checks run

- `python3 tools/check_bank.py bank/core.json bank/OH.json`: BANK PASSED.
- `python3 tools/originality_check.py check state/OH/ch01.md`: 0.05 percent shared, 0 runs of 12+, PASSED.

## Open items (not changed)

- ORC 4507.21(B)(4) also exempts from driver ed and the affidavit certain visa holders (military or Department of Defense work, hospital or health system work, agricultural guest workers). Section 1.10 names only the reciprocity exemption. Too narrow to teach; owner may add a half sentence.
- ORC 4507.21(B)(4) grants the reciprocity exemption from driver ed to applicants "21 or older". The book's reciprocity bullet does not mention age, so an 18 to 20 year old reciprocity holder could read it as a full exemption. Edge case; left as is.
- NEW says an expired out-of-state license means testing, without a grace period; ORC 4507.10(B) allows a waiver up to six months after expiry. Book follows the statute with "may waive". Left.
- Midnight to 6 a.m. BMV 2438 designee comes only from GDL (not in ORC 4507.05 or the manual). Kept because the BMV states it; recheck at each manual edition.
- Watch SB 419 and HB 463: if enacted, Chapter 1 sections 1.1, 1.2, 1.6, 1.9 and questions OH-001, OH-008, OH-035, OH-036 need updating.
