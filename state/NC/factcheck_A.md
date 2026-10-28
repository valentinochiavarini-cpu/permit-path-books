# North Carolina fact check A: Chapter 1

Scope: `state/NC/ch01.md` and the 40 Chapter 1 questions in `bank/NC.json` (NC-001 to NC-040). Checked 2026-10-28 against primary sources. Questions outside Chapter 1 and `inserts.md` were not touched.

## Sources used

- GS 20-11: https://www.ncleg.gov/EnactedLegislation/Statutes/HTML/BySection/Chapter_20/GS_20-11.html (online text not yet updated for S.L. 2026-46; still lists the Driving Eligibility Certificate)
- GS 20-13: https://www.ncleg.gov/EnactedLegislation/Statutes/HTML/BySection/Chapter_20/GS_20-13.html
- GS 20-137.3: https://www.ncleg.gov/EnactedLegislation/Statutes/HTML/BySection/Chapter_20/GS_20-137.3.html
- GS 20-8: https://www.ncleg.gov/EnactedLegislation/Statutes/HTML/BySection/Chapter_20/GS_20-8.html
- GS 20-279.1: https://www.ncleg.gov/EnactedLegislation/Statutes/HTML/BySection/Chapter_20/GS_20-279.1.html
- SL2023-13: https://www.ncleg.gov/EnactedLegislation/SessionLaws/HTML/2023-2024/SL2023-13.html
- SL2025-91: https://ncleg.gov/EnactedLegislation/SessionLaws/HTML/2025-2026/SL2025-91.html
- SL2026-46: https://www.ncleg.gov/EnactedLegislation/SessionLaws/HTML/2025-2026/SL2026-46.html
- RULE: 19A NCAC 03B .0201, http://reports.oah.state.nc.us/ncac/title%2019a%20-%20transportation/chapter%2003%20-%20division%20of%20motor%20vehicles/subchapter%20b/19a%20ncac%2003b%20.0201.pdf
- L1: https://www.ncdot.gov/dmv/license-id/driver-licenses/new-drivers/Pages/level1.aspx (stamp 10/1/2026)
- L2: https://www.ncdot.gov/dmv/license-id/driver-licenses/new-drivers/Pages/level2.aspx
- L3: https://www.ncdot.gov/dmv/license-id/driver-licenses/new-drivers/Pages/level3.aspx
- TEEN: https://www.ncdot.gov/dmv/license-id/driver-licenses/new-drivers/Pages/teen-drivers.aspx
- TESTS: https://www.ncdot.gov/dmv/license-id/driver-licenses/new-drivers/Pages/driver-license-tests.aspx
- NEWDRV: https://www.ncdot.gov/dmv/license-id/driver-licenses/new-drivers/Pages/default.aspx
- NEWRES: https://www.ncdot.gov/dmv/help/moving/Pages/new-residents.aspx
- REALID: https://www.ncdot.gov/dmv/license-id/nc-real-id/Pages/requirements.aspx and https://www.ncdot.gov/dmv/license-id/nc-real-id/Pages/default.aspx
- HB: NC Driver Handbook, revised May 2025 (Drive file 1xsHtFARBh7SuBf0V7-TNRynnxLqu0gRf)
- PED: DPI/DMV Knowledge Testing Review, report to the General Assembly, March 1, 2014, https://webservices.ncleg.gov/ViewDocSiteFile/16697

## Changes to ch01.md

| Section | Old | New | Reason and source |
|---|---|---|---|
| 1.3, 1.7, 1.10 | Driving log must be a "printed" copy | Log turned in "printed or digital" | L2 now says the log may be digital or printed. Printed is required only for insurance proof. |
| 1.10 | Bring list had no certificate | Added: if you tested at a driving school, bring the certificate showing you passed | L2 |
| 1.5 | "check in by phone and wait for a text that the office has room" | "walk in, check in with your phone at the office and wait for a text that it is your turn" | NEWDRV: you check in with your cell phone at the office, and a text calls you in. "By phone" read as a phone call. |
| 1.5 table | "If you fail: Retake after seven calendar days" (in a row covering both the knowledge and sign tests) | "Retake the knowledge test after seven calendar days" | TESTS gives the 7-day wait for the knowledge test and the driving test only. No retest rule is published for the sign test. |

The chapter is 2,239 words of prose (2,311 by raw `wc` including Markdown). No em or en dashes, no years.

## Recent law changes (writer's claims), all confirmed

| Claim | Result | Source |
|---|---|---|
| Permit hold 9 months (was 12) | Confirmed. S.L. 2023-13 s. 2(a), effective January 1, 2024 for applications on or after that date. The student passenger exception also comes from this law (s. 3, effective August 1, 2023). | SL2023-13; GS 20-11(d)(1); L1; L2 |
| Level 3 driving log repealed | Confirmed. S.L. 2025-91 s. 2 repealed G.S. 20-11(f)(4) (12 hours, 6 at night) and allows remote issuance under G.S. 20-7(f)(6). Effective when it became law (approved September 30, 2025). L3 lists no log. HB still shows the 12-hour log. | SL2025-91; GS 20-11(f); L3 |
| Driving Eligibility Certificate eliminated October 1, 2026 | Confirmed. S.L. 2026-46 s. 9 (heading "Eliminate Driving Eligibility Certificate Requirement") amends G.S. 20-11 and repeals G.S. 20-9(b1), 20-13.2(c1) and 115C-288(k). s. 9(e) makes it effective October 1, 2026. L1 and TEEN carry the notice. | SL2026-46; L1; TEEN |
| Insurance 50/100/50 | Confirmed: $50,000 / $100,000 / $50,000 (S.L. 2023-133 s. 12(a)). Not stated in ch01, and NC-029 only tests the printed proof. The insert is outside this scope. | GS 20-279.1(11) |
| Knowledge test 80 percent; sign test 9 of 12 | Confirmed: computer test, audio option, 80 percent to pass; Class C must identify 9 of 12 signs. | RULE; PED |
| New residents: signs plus vision | Confirmed. The rule gives the signs and vision tests for an out-of-state license that is valid or expired less than 2 years, and the full exam if expired more than 2 years. NEWRES: written and road tests "may be waived". HB: the examiner may require the driving test. 60 days confirmed (NEWRES; HB). | RULE; NEWRES; HB |
| Foreign licenses: full exam | Supported. The rule's reduced test set covers only licenses from other states. NEWRES: "North Carolina law enforcement authorities do not recognize international driver licenses." University ISS pages list all four tests for international students. G.S. 20-8(3): a nonresident 16 or older may drive on a valid license from their home state or country. No foreign reciprocity found. | RULE; NEWRES; GS 20-8 |
| Fees | Confirmed. Level 1 and Level 2 $25.50 (L1, L2, HB). Class C $6.50 per year (HB; L3 shows $32.50 at 16 and $26 at 17, consistent). Duplicate $16.75 (HB; REALID). REAL ID no extra fee (REALID). $52.00 for 8 years is correct. G.S. 20-11(j) still prints $21.50, so DMV is applying the 2024 inflation-adjusted fees. | L1; L2; L3; HB; REALID |

## Other claims verified (no change)

The following match the statute, rule or agency page:

- Level ages (15, 16, 16 and a half) and expiry on the 18th birthday: GS 20-11(b), (d), (f), (j).
- Level 1 hours: 5 a.m. to 9 p.m. for 6 months, then any hour with a supervisor. No one else in the front seat; seat belts for everyone: GS 20-11(c).
- 60-hour log (10 at night, 10 per week maximum, signed); a falsified log means a new log and a 6-month bar: GS 20-11(d)(5).
- Six months violation-free before Level 2 and before Level 3: GS 20-11(d)(2), (f).
- Level 2 hours, the work and volunteer emergency service exceptions, and the passenger rules. The book's wording follows L2 and HB: GS 20-11(e).
- Supervisor: parent, grandparent, guardian or approved adult, licensed 5 years: GS 20-11(k); L1.
- Driver education 30 + 6 hours; enroll at 14 and a half: L1; HB.
- Documents: 1 identity, SSN, 1 residency for a standard card and 2 for REAL ID; insurance not needed for a permit: L1; NEWDRV; REALID. Note: HB Tables 3 and 4 say two residency proofs (one for REAL ID). That is the reverse of the current site, so the book follows the site.
- Parent or guardian present, or written consent: L1; L2.
- Printed insurance proof; phone images refused: HB; L2.
- REAL ID star, "Not for Federal Identification", in person for the first card: HB; REALID.
- 8-year license for ages 18 to 65: NEWDRV.
- Vision 20/40; lens restriction; driving without lenses counts as no license: RULE; TESTS; HB.
- Signs identified by color and shape with an explanation; languages; oral tests: TESTS; HB.
- Under-18 phone ban, its exceptions, $25 fine, no points or costs: GS 20-137.3.
- Provisional licensee suspensions for 2nd, 3rd and 4th moving violations (30 days, 90 days, 6 months, within 12 months of the first): GS 20-13(b).
- Any alcohol or drugs: one-year revocation: HB.
- Road test items (quick stop, three-point turnabout, etc.), own car, pre-trip inspection, certified school option: HB; RULE; L2.
- Adult learner permit with a licensed person seated beside the driver: HB; NEWDRV.

## Knowledge test question count

Still no official count. NCDMV (TESTS, sample test page, TEEN), 19A NCAC 03B .0201 and the handbook give the 80 percent pass mark but no number of questions. The closest official document, the 2014 DPI/DMV report to the General Assembly (PED), gives 80 percent, 8 languages and an average of 24 minutes, but no count. Its "more than 25 test questions" refers to the driver education course exam. The "25 questions, 20 correct" figure appears only on third-party sites. The chapter's wording ("The NCDMV does not publish a fixed number of knowledge questions") stays. Mock exam sizing should not assume an official 25.

## Question fixes

None. All 40 Chapter 1 keys are correct, each question has one defensible answer, and each is taught in the chapter. Nothing in the edited text contradicts a keyed answer. `bank/NC.json` was not written.

## Checks

- `python3 tools/check_bank.py bank/core.json bank/NC.json`: BANK PASSED.
- `python3 tools/originality_check.py check state/NC/ch01.md`: 0.04 percent shared, 0 runs of 12+ words, ORIGINALITY PASSED.

## Open items

- The `supervised_hours` insert (inserts.md line 269) still says "you hand in a printed copy" of the log. L2 accepts printed or digital, so it should read "printed or digital". The sources.md rows for the log say "printed" too. Both files are out of this scope and are left for checker B or the writer.
- The online G.S. 20-11 text still shows the Driving Eligibility Certificate in (b), (d), (f) and (h) because the codifier has not caught up. The book follows S.L. 2026-46, which is correct.
- The passenger rule: the statute places the student exception inside the household sentence. The book follows the NCDMV wording (L2, HB), which is the reading examiners use.
- Sign test retest wait: not published.
