# Upgrade brief: core quality pass (owner approved, 2026-10-28)

An independent QA of the Pennsylvania edition found: missing signs, missing testable topics, about 120 "most states / your state may" hedges that make a state edition read like a 50-state book (some contradict the state box next to them), and chapter quizzes that are too easy and too generic. You fix this in the universal core, for your chapters only. The full QA reports are in
`/tmp/claude-0/-home-claude/9d4de182-a7b0-5f49-bd9e-983574378387/scratchpad/qa/coverage_PA.md` and `.../qa/review_PA.md`. Read both first (they cite Pennsylvania facts; the core must stay state-neutral, so turn a PA fact into either a national rule or an insert).

Read also: `CLAUDE.md`, `docs/decisions.md`, `briefs/CORE_SPEC.md`, `briefs/CORE_WRITER_BRIEF.md` (voice, originality), `briefs/TRIM_BRIEF.md` (length discipline).

## 1. Add the missing topics (your chapter list is in your task)
- Teach each in Permit Path's own words, calm instructor voice, short sentences, colors named in words.
- National facts only in core text: the Uniform Vehicle Code / MUTCD / NHTSA level (cite in `core/notes/upgrade_<tag>.md`). Anything that varies by state goes in an insert.
- Budget: at most about 350 added words per chapter (Chapter 2 may add more for signs). Cut padding elsewhere to stay close.

## 2. New insert keys (already in `layout/config.json`)
Place each marker on its own line where the topic is taught, after the national rule:
- `{{INSERT:emergency_vehicles}}` in Ch 4 (yielding to emergency vehicles: which edge on one-way streets, distance to stay behind, intersections).
- `{{INSERT:headlight_use}}` in Ch 10 night section (when headlights are required, visibility distance, wipers-on rule, daytime running lights).
- `{{INSERT:police_stop}}` in Ch 10 (new short section: what to do when police signal you to stop).
- `{{INSERT:underage_alcohol}}` in Ch 11 (under-21 penalties, including non-driving offenses: possession, false ID).
- `{{INSERT:driver_record}}` in Ch 12 (new section on points, suspensions, point removal, required insurance). Rename Chapter 12 to `# Chapter 12: Your Car, Passengers and Your Record`.
Write the national framing around each marker (2 to 5 sentences), then add a sample body for every new key to `core/sample/inserts.md` (Chapter 9 to 13 agent does all five).

## 3. Remove the 50-state feel
Every "most states", "many states", "some states", "your state may", "check your state" sentence: decide one of
- **Delete** it if the insert below gives the rule, or if it adds nothing.
- **Keep it for the core preview only** by wrapping it: `[[generic]]Some states let you use the nearest edge.[[/generic]]`. A state edition drops the wrapped text at build time. Wrap whole sentences only (with their final period), inside one paragraph. For a whole block (paragraph, list item, table row) put `[[generic]]` and `[[/generic]]` each on its own line around it.
- **Rewrite** as a plain national rule if it is true everywhere.
Never leave a sentence that could contradict a state box (for example "in some states the bus driver may wave you on"). Text a state edition keeps must read naturally without the wrapped text: check the sentence before and after.
Goal: a state edition has at most about 1 hedge per chapter.

## 4. Rework your chapter quizzes (bank/core.json, your chapters only)
- Each chapter keeps exactly 10 core questions with `"quiz": true`, in bank order. A state edition shows the first 7 core quiz questions plus 3 state questions about that chapter's state boxes, so put your 7 most important quiz questions first and the 3 most expendable last (reorder records in the file; IDs stay).
- Every quiz question must test something a test writer would actually ask, with 3 believable wrong answers (common misconceptions, near-miss numbers). No joke options, no "whichever driver honks first", no study-tactics questions in Ch 13's quiz (test-day rules and road test skills instead).
- Rewrite weak questions in place (same ID) or replace them; add new non-quiz questions for every new topic (IDs continue the chapter's numbering, e.g. C06-031). Each chapter keeps 30+ questions.
- Mark questions about trivia the state tests do not ask (HOV details, Interstate numbering, backup cameras, work zone camera warnings and the like) with `"app_only": true` and `"quiz": false`: they stay online, never print.
- Every question must be taught in your chapter's text. Correct letters about 25 percent each.
- `python3 tools/check_bank.py bank/core.json` must print BANK PASSED (it also runs the originality check on every question).
- Another agent edits other chapters of bank/core.json at the same time: re-read the file right before each write, change only your chapters' records, keep its formatting (indent 2, ensure_ascii False, trailing newline).

## 5. Checks before you finish
- `python3 tools/originality_check.py check core/chNN.md` for each chapter you touched: must pass. Never look at or reuse Daniel Hart text.
- `python3 layout/build_book.py --core-only` must finish with QA PASSED (another agent may be mid-edit; if a failure is clearly in someone else's chapter, note it and move on).
- No em or en dashes, no years, no state names in core text.
- Write `core/notes/upgrade_<tag>.md`: what you added (with national sources), hedges deleted/wrapped/rewritten per chapter, quiz changes, app_only list, words before and after per chapter.
- Do not commit.

Reply briefly: per chapter words before and after, topics added, hedge count before and after (unwrapped hedges a state edition still prints), quiz changes, anything unsure.
