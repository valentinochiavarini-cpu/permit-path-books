# Texas fact check A (Chapter 1 and ch 1 bank questions)

Checked 2026-10-28. Scope: `state/TX/ch01.md` and `bank/TX.json` IDs TX-001 to TX-042 (ch: 1). Sources: Texas Driver Handbook DL-7 rev. Jan 2026 (Drive 1QFLw84NB77SFOD1HjAsHI5no5CaC8h40, text to p. 74), DPS and TDLR pages, Texas Administrative Code (Cornell LII, Justia). Short names as in `sources.md`.

## Changes to ch01.md

| Where | Old | New | Reason and source |
|---|---|---|---|
| 1.7, The Practice Requirement | "Course rules allow no more than two hours of driving instruction a day, so spread the practice out." | "Course rules credit no more than two hours of behind-the-wheel instruction a day, so spread your lessons out." | The two hour cap applies to behind-the-wheel instruction, not to the 30 hours of supervised practice. 16 TAC 84.50(d): "not more than two hours of behind-the-wheel instruction per day"; no daily cap on supervised practice. https://law.cornell.edu/regulations/texas/16-Tex-Admin-Code-SS-84-50 ; TDLR-BTW |
| 1.11, From another state | Under 18: "skip the knowledge test, still take the road test, and receive the matching learner or provisional license" | Permit becomes a learner license; license becomes a provisional license once you pass the road test | A learner license never needs a driving exam (DL-7 p. 8, Part 3: "the driving exam is not required for anyone applying for a learner license"); out-of-state license holders 16 to 17 get a provisional license after the driving exam (DL-7 p. 3, Out-of-State License Holders). MOVE |
| 1.11, From another country | "Holders of a valid license from France, Germany..." | "Adult holders of..." | MOVE: all applicants under 18 must take the skills exam; reciprocity waives only the knowledge exam for minors. https://www.dps.texas.gov/section/service/moving-texas |
| 1.9, after temporary license | (none) | "If you move later, report your new address to DPS within 30 days." | Quiz bank TX-042 tested a fact the chapter never taught. DL-7 p. 9: "A change of address must be reported to DPS within 30 days." |

Word count after edits: 2,242 (wc -w on the Markdown). No em or en dashes.

## Bank (TX-001 to TX-042)

No wrong keys, no stems with two defensible answers. Every keyed answer matches DL-7, the DPS pages or the TAC. TX-042 was not taught in the chapter; fixed in the text (above), not in the bank. No bank edits, so no other IDs were touched.

## Verified (no change needed)

- **Knowledge test format.** DL-7 p. 7: Class C knowledge exam, 70 percent or better on any knowledge exam. 37 TAC 15.52: 70 percent on each test; written and oral exams in English and Spanish only. 37 TAC 15.64: driver education schools and parent-taught providers may give two exams, Class C Road Signs and Class C Road Rules, 70 percent on each; exams supplied by DPS or TDLR; not before the 15th birthday; no review before the exam; result on the driver education certificate. DPS "Testing in Other Languages": English or Spanish only, translators not allowed during the test. Nothing official gives a question count (see below).
- **ITTD / ITAD.** ITD page: ITTD for ages 15 to 17 (2 hour video), ITAD for 18 to 24 in adult driver ed and 25+ (1 hour); taken after behind-the-wheel requirements, before the skills test; certificate valid 90 days; printed copy. ITTD-FAQ: free, eight modules, last step before the skills exam, restart if expired, paper copy only.
- **Learner holding period.** DL-7 p. 2: six months on a learner, hardship or combination; extended by suspension days. TEEN.
- **30 hours, 10 at night; 7 + 7.** PROV; 16 TAC 84.50(k); TDLR-BTW (supervisor 21+, licensed a year; parent or guardian certifies).
- **Provisional restrictions.** DL-7 p. 3: one passenger under 21 not family; midnight to 5 a.m. except work, school-related activity, medical emergency; no wireless device under 18, even hands-free, except emergency; expires on 18th birthday. PROV.
- **Adult driver ed 18 to 24.** ADULT: six-hour adult course for 18 through 24, waived for new residents 18+ surrendering a valid license; none at 25+; ITD certificate within 90 days of the skills test. DL-7 p. 1: adults wanting to practice get a Class C with learner restrictions.
- **Fees.** FEES (page dated 2020-09-29) and DL-7 Tables 1 and 4: learner $16, Class C under 18 $16, Class C 18 to 84 $33 for eight years, replacement or change $11, $1 admin fee once per visit, fee before exams.
- **New residents.** MOVE: 90 days; valid or not expired over two years; no knowledge or skills exam; vehicles registered in Texas first; foreign licenses not in English or Spanish translated.
- **Exchange countries.** MOVE: France, Germany, South Korea, United Arab Emirates and Taiwan (exact list, matches the chapter).
- No 2025 to 2026 legislation found changing Chapter 1 facts (TDLR news: SB 1366 adds work zone content to courses from 2026-09-01; no licensing changes).

## Knowledge test question count (for mock sizing)

- **Official sources: no count.** Checked DL-7 (Ch. 1 p. 7), 37 TAC 15.52 and 15.64, 16 TAC 84.50, DPS pages (teen, provisional, adult, other languages, "Section 23: Request Knowledge Tests by Driver Education Schools", which says only that DPS emails the Class C exams to schools as PDFs), TDLR POI for teen and adult driver ed (May 2026, TexReg April 24, 2026; the adult POI names a "Texas Department of Public Safety Highway Sign and Traffic Law Examination" with 70 percent mastery, no count).
- **Providers (only source of a count):**
  - I Drive Safely, TDLR-approved adult course: "30 questions, with 15 pertaining to road signs and 15 covering road rules", 70 percent, 3 attempts. https://www.idrivesafely.com/drivers-ed/texas/adult-driver-education/
  - Adult Drivers Ed Texas (provider): 30 questions, 15 road rules and 15 road signs. https://www.adultdriversedtexas.com/question-answers.html
  - Aceable (provider): "30 multiple-choice questions about road rules and traffic signs", 21 correct to pass. https://www.aceable.com/drivers-ed/texas/knowledge-test-prep-course/
  - Jerry (not a provider): Highway Signs 15 + Traffic Laws 15.
  - Outliers: easydriversed.com says 40; driving-tests.org gives no count.
- **Verdict.** Most reliable figure: 30 questions, 15 Road Signs + 15 Road Rules, each part scored at 70 percent (11 of 15, per 15.64), published only by approved providers, never by DPS or TDLR. No source gives a separate count for the test at a DPS office. The chapter keeps "DPS does not publish a count", which is accurate.

## Open items

1. **Mock sizing (owner decision).** `docs/states.md` says use 25 when the state publishes no count. Provider evidence points to 30 (15 signs + 15 rules, 70 percent on each part). Suggest two 30-question mocks split 15/15 and scored per part, with the book saying the count comes from course providers, not DPS. Update `docs/states.md` if approved.
2. 37 TAC 15.52 says exams in English and Spanish "only"; the chapter matches. No change.
3. Parent Taught Program Guide: PTDE calls the $20 an application fee; the chapter's "$20 per student" for the guide matches TDLR usage. No change.
4. DL-7 Appendices B to E (fees, restriction codes) are missing from the Drive text; fees taken from the DPS fee page (dated 2020, still current per DL-7 Tables 1 and 4).
