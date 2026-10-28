# State upgrade brief: bring a finished state up to the upgraded core

The core was upgraded (see `briefs/UPGRADE_BRIEF.md`): new topics, 5 new insert keys, hedges removed from state editions, and chapter quizzes that now end with up to 3 state questions. You bring one finished state (XX) up to it. Read `CLAUDE.md`, `docs/decisions.md`, `briefs/CORE_SPEC.md`, `briefs/STATE_BRIEF.md` (voice, sources, rules) and the QA reports in `/tmp/claude-0/-home-claude/9d4de182-a7b0-5f49-bd9e-983574378387/scratchpad/qa/` first. Then build the current book once (`python3 layout/build_book.py --state "NAME" --code XX`; it fails until the new inserts exist, that is expected) and read `out/XX/*.md` around every state box.

## 1. Five new inserts in state/XX/inserts.md (90 words or fewer each, verified on primary sources, logged in sources.md)
- `emergency_vehicles`: which edge to pull to (including one-way streets), how far to stay behind a responding emergency vehicle, anything else the state manual says.
- `headlight_use`: when headlights are required (times, visibility distance, wipers rule), daytime running lights, any fine.
- `police_stop`: what the state manual tells drivers to do when stopped by police (if the manual is silent, give the state's documents to show: license, registration, insurance; never invent).
- `underage_alcohol`: zero tolerance limit and penalties for under-21 drivers, plus non-driving offenses (possession, purchase, false ID) and license consequences.
- `driver_record`: point system (how many points trigger what), point removal, required insurance minimums and proof, any teen-specific rules not already in Chapter 1.

## 2. Rewrite every existing insert as clear teen prose
One idea per sentence, plain words, numbers in bold where they are the testable fact. Tables only where they truly help; every column header must match its contents (for example do not put probation under "Jail"; keep fines in their own column). Read each box in context: it must follow naturally from the core text above it, never repeat it, never contradict it. Keep all verified facts; do not add unverified ones. 90 words or fewer each.

## 3. State questions in chapter quizzes (bank/XX.json)
- For each chapter 2 to 13, flag up to **3** state questions with `"quiz": true`: the most testable facts from that chapter's state boxes (numbers, distances, limits, penalties). Each must be taught in that chapter's box. Prefer existing questions; write new ones where a chapter has none (IDs continue after the highest XX- number). Chapter 1 keeps exactly 10 quiz questions.
- Add 2 to 4 non-quiz questions for each of the 5 new inserts.
- Mark state trivia that the state test does not ask (for example a single highway's HOV rule) `"app_only": true` and `"quiz": false`.
- Believable wrong answers only. Correct letters about 25 percent each per chapter.
- `python3 tools/check_bank.py bank/core.json bank/XX.json` must print BANK PASSED.

## 4. Chapter 1
Remove anything Chapter 13 now covers generically only if Chapter 1 repeats it word for word in spirit; keep every state fact. Fix any contradiction with the new core. Stay 2,000 to 2,300 words.

## 5. Build and check
- `python3 tools/originality_check.py check state/XX/ch01.md state/XX/inserts.md` must pass.
- `python3 layout/build_book.py --state "NAME" --code XX` must print QA PASSED and ORIGINALITY PASSED. Read the rebuilt `out/XX/*.md` around every state box once more.
- Do not run make_mocks or touch mocks.json, core files, figures or other states. Do not commit.

Reply briefly: the 5 new inserts' key facts with sources, inserts rewritten, quiz questions flagged per chapter (IDs), new question IDs, app_only IDs, anything unverified, page count.
