# Decisions log (owner-approved)

Everything here was agreed with the owner. Change it only with the owner's approval and record the change with a date.

## Brand and account
- Brand: **Permit Path**. The brand is the author name on Amazon and the only name in the book. No pen name, no company name, no year in the book.
- Publishing account: the owner's LTD KDP account. Must not resemble the Daniel Hart DMV series (same niche, same owner). The core text is written from scratch; `tools/originality_check.py` enforces it (see Originality).
- Copyright line: "© Permit Path. All rights reserved."
- Scope: car (Class C/D/E) permit and license only. English only for now (Spanish is the largest unexploited pocket in the market data; parked).

## Product
- Format: 6 x 9 in, black and white paperback, plus EPUB (Kindle). No hardcover for now.
- Structure: state chapter (Ch 1, fully state-specific) + universal core (Ch 2 to 13) with state inserts + 2 full mock exams sized to the state's real test + answer key + supervised driving log appendix.
- Every content chapter ends with a 10-question chapter quiz (questions in context, the top complaint about the market leader). Quiz answers with explanations follow the quiz.
- Book teaches, app drills: about 150 questions in the book (quizzes + mocks), 500+ per state online. Color sign flashcards and a downloadable ebook live online to compensate for B&W print. Say so on the title page, in How to Use This Book and in every chapter practice card.
- Every printed question comes from the question bank in `bank/`, verbatim. The bank is the source of truth; the app imports it. Never edit a question only in the book.

## Title (KDP)
Standard (max 200 characters; the longest state name gives 192):
`[State] Drivers Ed Book: Driver's License Handbook and Permit Practice Test Book for Teens and First-Time Drivers | Chapter Quizzes, 2 Full Mock Exams and 500+ Online Practice Questions`

California only (new residents must take the knowledge test there):
`California Drivers Ed Book: Driver's License Handbook and Permit Practice Test Book for Teens, First-Time Drivers and New Residents | Chapter Quizzes, 2 Mock Exams and 500+ Online Practice Questions`

- Do not put "flashcards" in the subtitle (KDP issues in the past).
- Year phrases ("[state] drivers handbook 2026") go only in the 7 backend keyword slots; refresh every January.
- Price: $17.99 to $18.99 paperback (market leader Easy Route Test Prep: $18.99).

## Positioning (from market research, 2026-10-27)
- Audience: teens (about 50 percent of knowledge test takers) and first-time adult drivers (about 30 percent). Lead all copy with these two.
- Do not target seniors (no age-based knowledge retest in the 15 states) or new residents (14 of 15 states waive the test for a valid out-of-state license; California is the exception; Missouri and North Carolina give new residents a road sign test).
- Foreign license holders must test in every state: strongest angle in CA, NY, IL, NJ, VA (licenses regardless of immigration status).
- Beat the market leader on: coverage (chapter quizzes + mocks + 500+ online), questions in context, accuracy (two-pass fact check, every question cited to the official manual), readable type (11 pt body minimum), teen focus, supervised driving log.

## Target states (15) and pilot
Florida, Texas, California, Pennsylvania, New York, Illinois, Ohio, Missouri, North Carolina, South Carolina, Georgia, New Jersey, Virginia, Alabama, Michigan. Spares with handbooks on file: Maryland, Tennessee. Pilot: **Pennsylvania**.

Skipped on purpose (Daniel Hart already leads, a new brand would cannibalize it): WA, IN, MS, KY, OK, LA, OR, CO.

## Writing rules
- No em or en dashes anywhere (book, app text, listings, messages).
- Voice: a calm, direct driving instructor talking to a teen or a nervous first-time adult. Second person, short sentences, plain words, no hype, no jokes at the reader's expense.
- Colors are always named in words next to the sign or marking ("a red octagon"), because the print is B&W.
- Core chapters are state-neutral. Where states differ, use an insert marker (`{{INSERT:key}}`) and fill it per state, or state the common national rule and say "your state may differ; see the box below".
- Verify every legal or numeric fact on primary sources (state manual, statute, state agency site, FHWA MUTCD 11th edition, NHTSA). Invented names in examples.

## Originality
- `tools/originality_check.py` compares the book text with hashed 8-word sequences of the Daniel Hart master template and the Daniel Hart Pennsylvania edition (`ref/*.hashes`; raw text is not stored in the repo). The build fails if any 12-word run matches or overall 8-word overlap exceeds 1 percent. Shared legal facts are fine; shared sentences are not.

## Length and figures (2026-10-28)
- Page target 160 to 175 for a state edition (180 to 195 accepted where the real test is long: owner kept Florida's two 50-question mocks, 193 pages, 2026-10-28) (print cost about $3.00 to $3.10 per copy on KDP US). PA: 177 pages.
- Word targets: core chapters about 2,000 words, Chapter 13 about 1,500, state Chapter 1 about 2,300, inserts 90 words max (`briefs/TRIM_BRIEF.md`).
- 35 original figures in the core (about 80 signs) (`layout/fig/`, rules in `briefs/FIGURES_BRIEF.md`): full MUTCD colors in PDF and EPUB, Amazon prints them in B&W, every meaningful color named in a label or caption. State runs add no figures.
- Chapter quiz answers live in one two-column Answer Key at the back.

## Layout (paperback)
- Trim 6 x 9 in, B&W, no bleed. Body Literata 10.5 pt, headings and tables Inter.
- Margins: inside 0.75 in, outside 0.5 in, top 0.6 in, bottom 0.65 in (KDP minimum inside 0.375 in up to 150 pages, 0.5 in for 151 to 300).
- Chapter practice card at the end of every chapter: QR + short URL to that chapter's online practice.
- EPUB: same text, links instead of QR codes, must parse cleanly.

## App
- Lovable project `5aba30bf-4b8e-4041-b0c3-080168980b32` ("Permit Path"), remixed 2026-10-27 from The Driving School (`c427a0c1-...`, never write to it). Free, no login.
- Data goes in through SQL (no Lovable credits): `questions` (core rows have state null; category "Chapter N: Title"), `states` (only states with a Permit Path book), `flashcards` (115, descriptions rewritten, see `app/flashcards.json`; images still load from the old project's storage, so keep that project).
- Routes: `/ch/:n` (chapter practice, the book QR codes), `/chapters`, `/ebook` (EPUB from public bucket `ebooks/XX.epub`, uploaded by the owner), `/flashcards`, the timed exam and practice mode.
- App URL (final, set 2026-10-27): https://permit-path-practice.lovable.app (`layout/config.json`, `app_url_final: true`). Published from the Lovable project with slug `permit-path-practice`. Every QR code and link in the books points here.

## Quality upgrade (2026-10-28, owner approved all five changes)
- Independent QA of PA found sign gaps, untaught manual topics, multi-state hedging and weak quizzes. Fixed: about 37 more signs (75 of the PA manual's 95 as figures), 5 new insert keys (emergency_vehicles, headlight_use, police_stop, underage_alcohol, driver_record), hedges as `[[generic]]` (dropped in state editions), chapter quizzes = 7 core + 3 state questions, sign-picture questions (`img`), believable wrong answers only, test-irrelevant trivia `app_only`.
- Re-audit (PA): 98 percent of Daniel Hart's PA questions and 94 percent of PUB 95 review questions answerable from the book (was 91 and 84).
- Page counts after the upgrade: PA 190, FL 203, TX 196, CA 202, NY 190, IL 199 (about 13 pages more each).

## All 15 states built (2026-10-28)
- Page counts: PA 190, NY 190, SC 194, MI 195, TX 196, MO 198, IL 199, AL 199, CA 202, NC 202, VA 202, FL 203, GA 204, OH 204, NJ 207.
- Mocks follow the real test format where published; where a state publishes no count (TX, CA, NC rules part, AL, MI, SC) the mock intro says so (`size_note` in mocks.json). `tools/regen_mocks.py XX` redraws mocks in the stored format after bank changes.

## Open items for the owner
- REMINDER when all state editions are finished: upload every EPUB (`out/XX/Permit_Path_NAME.epub` saved as `XX.epub`) to the app's public `ebooks` storage bucket. The /ebook page shows "coming soon" until then.
- Next Lovable batch (small, not urgent): sitemap.xml still uses the preview host instead of permit-path-practice.lovable.app; the page title contains an em dash.
- Spot-check flashcard images whose names look mislabeled (Railroad Crossing, Roundabout, Right Turn, duplicate pairs).
- Cover design.

- 2026-10-29: Bank pass 2 done on all 16 banks (believable distractors, correct answer longest in 23 percent of 2,833 questions). All 15 books rebuilt (189 to 207 pp), app reloaded from the same bank (counts verified), states table mock sizes and pass scores aligned. 16 core and most state sign questions carry app images; the other sign questions describe the sign in words, so they work without one. EPUBs handed to the owner for the ebooks bucket.
