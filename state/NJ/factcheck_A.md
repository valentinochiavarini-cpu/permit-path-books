# New Jersey fact check A (Chapter 1 and ch 1 bank questions)

Checked 2026-10-28. Scope: `state/NJ/ch01.md`, `bank/NJ.json` IDs with `ch: 1` (NJ-001 to NJ-043, NJ-136).

## Manual access
Not read. The Drive copy (1zlPerWLh90UZoFruJ2eQzN38t0jSkKoB) again returned empty text through `read_file_content`; a direct download of nj.gov/mvc/pdf/license/drivermanual.pdf is blocked by the network proxy (403). Facts were verified on MVC web pages and statutes instead. An old 2015 edition (third-party copy) was used only as a lead.

## Verified (no change needed)
| Claim | Source |
|---|---|
| Knowledge test 50 questions, 80 percent (40 of 50) | https://www.nj.gov/mvc/license/sample_knowledge_test.htm |
| Written test in 13 languages (English, Arabic, Chinese, French, Spanish, Korean, Polish, Portuguese, Russian, Japanese, Hindi, Albanian, Turkish); oral in English and Spanish; interpreter appointments 4 to 6 weeks | https://www.nj.gov/mvc/license/knowledgetest.htm |
| Knowledge retest after 7 days; road retest after 14 days; 2 years to finish steps or buy a new permit | https://www.nj.gov/mvc/license/firstlic.htm; https://www.nj.gov/mvc/license/roadtest.htm |
| Special learner permit at 16 in a behind-the-wheel course; 6 hours in a dual-control car with a licensed instructor | https://www.nj.gov/mvc/license/youngadult.htm |
| Examination permit at 17 ("over 17 years of age"); supervisor NJ licensed, 21+, 3 years licensed, front seat; 6 months supervised, 3 months at 21+ | N.J.S.A. 39:3-13(a), (c) (law.justia.com, 2025 text) |
| 50 hours, 10 in darkness, certified by parent, guardian or supervisor; fraud = 6-month suspension; only form BA-CSD accepted; applies by age at permit | N.J.S.A. 39:3-13(o), 39:3-13.4(a)(5); firstlic.htm; youngadult.htm |
| Under 21: no driving 11:01 p.m. to 5 a.m. (employment or religion exemption); one extra passenger unless parent or guardian; dependents excluded; seat belts for all occupants | N.J.S.A. 39:3-13(c), 39:3-13.4(b), (c); https://www.nj.gov/mvc/about/gdlsafety.htm |
| Device ban (hand-held and hands-free) for all probationary holders, any age | N.J.S.A. 39:3-13.4(c) |
| Decals: upper left of front and rear plates, $4 a pair, under 21; GDL violation $100 | gdlsafety.htm; N.J.S.A. 39:3-13.8 |
| Basic license after 1 year unsupervised and at 18, online; renew in person if not upgraded in 3.5 years | firstlic.htm; youngadult.htm |
| Fees: permit $10 (GDL permits valid 2 years, non-GDL 90 days); auto license $24 initial and renewal; REAL ID $11; duplicate $11 | https://www.nj.gov/mvc/license/licfees.htm |
| Road test: 6 or 3 months; bring 6 Points, permit, qualified driver, registered, inspected, insured car, decals; denial reasons; 10 to 15 minutes; 9 skills; non-GDL 20 days; examiner endorses permit | roadtest.htm |
| Only the examiner rides on the road test; expired out-of-state license over 1 year = start over; IDP visitors up to 1 year; standard license "regardless of immigration status"; affidavit if no SSN or ITIN | https://www.nj.gov/mvc/pdf/license/FAQ_firsttime.pdf |
| New residents: 60 days or before expiry, whichever first; knowledge and road tests waived with valid non-provisional license; reciprocity only with Taiwan and South Korea, 18+, Class D | https://www.nj.gov/mvc/drivertopics/movetonj.htm |
| No other reciprocity country in force: Ireland bill A1003 only introduced (Jan 2026) | https://app.azure.legiplex.com/nj/legislature/2026/2026-r/bills/a1003 |

## Changes to ch01.md
1. Section 1.4: "When you pass, your permit is **validated** for practice driving." changed to "Passing **validates** an examination permit for practice driving." Reason: on the special learner path, the permit is validated only after the 6 instructor hours (as Section 1.6 says), not on passing the test. Source: youngadult.htm.
2. Section 1.7: "The only exceptions are for work or religious activities," changed to "Exceptions are made for work or religious activities,". Reason: N.J.S.A. 39:3-13.4(b) also allows an emergency waiver, so "only" overstated the law.

Word count after edits: 2,293 (wc). No em or en dashes, no years in book text.

## Question fixes
| ID | Old | New | Reason |
|---|---|---|---|
| NJ-032 (exp) | "The only exemptions are for bona fide employment..." | "The exemptions are for bona fide employment..." | Same as change 2; key (B) unchanged and correct |

All other ch 1 keys checked against the sources above: correct, one defensible answer each, taught in the chapter.

## Checks
- `python3 tools/check_bank.py bank/core.json bank/NJ.json`: BANK PASSED.
- `python3 tools/originality_check.py check state/NJ/ch01.md`: 0 shared sequences, PASSED.

## Unresolved
- Manual not read; confirm against the current edition (translations dated 9-21-26) when a readable copy is available.
- Section 1.10, foreign licenses (other countries): the 90-day non-GDL permit and 20-day practice are on MVC pages, but the rule that experienced foreign drivers use that track (and full GDL otherwise) rests on a secondary source (Rutgers). An older manual and Montclair State say a road test waiver for foreign licenses "cannot be guaranteed", which hints the road test is sometimes waived. Text kept; confirm in the manual.
- Probationary, knowledge and road test fees are not on the MVC fee page; the chapter does not state them.
