---
name: permit-path-state-edition
description: Build one or more Permit Path state editions (KDP DMV drivers ed series on the LTD account) from the permit-path-books repo: state chapter, inserts, question bank, fact check, mocks, app load, build PDF/EPUB.
---

# Permit Path: build a state edition

Use when the owner asks to build, rebuild or update a Permit Path state edition ("build Florida", "do TX, NY and OH", "update PA for the new manual"). Each edition = state Chapter 1 + the universal core (Ch 2 to 13) filled with that state's 23 inserts + 10-question chapter quizzes + 2 mock exams sized to the real test + supervised driving log, built to a 6 x 9 B&W paperback PDF and an EPUB. About 87 percent of each book is the shared core, including all 35 color figures (state runs add none). Target 160 to 180 pages. The core is written once; a state run never edits core chapters unless a fact check proves a core error.

## 0. Setup (every session)
1. `add_repo` owner `valentinochiavarini-cpu`, repo `permit-path-books`, access `push`; clone to `/home/claude/permit-path-books` (long timeout); `register_repo_root`.
2. Read `CLAUDE.md`, `docs/decisions.md`, `docs/states.md`, `briefs/CORE_SPEC.md`. They are binding: brand only (Permit Path), no pen or company name, no year, no em or en dashes, never reuse Daniel Hart text.
3. `cd layout && npm install --silent`. Chromium is at `/opt/pw-browsers/chromium`; never run `playwright install`.
4. Task list per state: write, fact check A (Ch 1), fact check B (inserts), merge and mocks, build and QA, app load, commit, report.

## 1. Inputs (per state XX)
- Official manual: Google Drive folder `1FyAFV4MCSnyVvLuPMnjzK6xHIr6k5VIA` (file IDs in `docs/states.md`). Agents read it with `mcp__Google_Drive__read_file_content`; never download as base64. Long manuals get cut off: agents must fill gaps from the agency's online manual.
- Test format, new-resident rule and status column in `docs/states.md` are leads; the writer verifies them.
- Add the state name to `layout/config.json` `state_names` if missing.

## 2. Write (one agent per state)
Launch a general-purpose agent: "Read `briefs/STATE_BRIEF.md` and follow it exactly. State: NAME (XX). Manual Drive file ID: ID. Write only state/XX/ch01.md, state/XX/inserts.md, state/XX/sources.md and bank/XX.json. Keep your own scripts under unique names in the scratchpad. Do not commit." For 3+ states run up to 3 writers in parallel; files never overlap.

## 3. Fact check (two agents per state, in parallel, after the writer)
- A: "Read `briefs/FACTCHECK_BRIEF.md`. Scope: state/XX/ch01.md and the ch 1 questions in bank/XX.json. Write state/XX/factcheck_A.md."
- B: "Read `briefs/FACTCHECK_BRIEF.md`. Scope: state/XX/inserts.md (all keys, read each in context around its marker in core/chNN.md) and the non-ch-1 questions in bank/XX.json. Write state/XX/factcheck_B.md."
Tell both: re-read bank/XX.json right before each write and change only their IDs. Give them statute access tips that worked (for example PA: palegis.us view-statute URLs through WebFetch). Then resolve their open items yourself: delete questions that contradict the core, retag questions to the chapter that teaches them, and fix any core contradiction in core/chNN.md only with a source (it affects every state).

## 4. Mocks
`python3 tools/make_mocks.py XX SIZE "PASS TEXT"` where SIZE is the real test's question count (25 if the state publishes none). It never reuses quiz questions and draws about 40 percent state, 60 percent core.
Split tests (a separate road sign part, for example GA, VA, NC): `python3 tools/make_mocks.py XX --part "Road Signs|10|all 10 correct|2" --part "Rules of the Road|30|24 of 30 correct"` (NAME|SIZE|PASS|CHAPTERS; chapter 2 is road signs). The book then prints each mock in parts with their own pass marks. The core has 20 non-quiz sign questions, so a sign part of more than 10 per mock needs state `ch: 2` questions (the writer adds 25+). If a mock's answer letters are lopsided (any letter under 15 percent), rerun with another `--seed`.

## 5. Build and QA
First `python3 tools/check_bank.py bank/core.json bank/XX.json` (schema plus originality of every question; must print BANK PASSED). Then `python3 layout/build_book.py --state "NAME" --code XX`. It must print QA PASSED and ORIGINALITY PASSED. It runs the originality check on the whole book: fix any 12-word run it reports (usually stock phrases in question explanations) by rewording in the bank or text, then rebuild. Render and look at 4 pages (contents, Ch 1 opener, a page with a state rule box, a quiz page). Check the page count: target 160 to 180 (KDP margins are set for 151 to 300 pages). Over 180, trim Chapter 1 and the inserts first, never the core.

## 6. App load (no Lovable credits)
Permit Path app: Lovable project `5aba30bf-4b8e-4041-b0c3-080168980b32` (never the old The Driving School project `c427a0c1-...`, which is read-only for us).
1. If the state is not in the `states` table, insert it (code, name, mock_exam_question_count = SIZE, mock_exam_time_limit, pass_score from the verified test).
2. `python3 tools/export_app_sql.py --state XX OUT_DIR`, then delegate to an agent: run `delete from questions where state = 'XX'` (only on a rebuild) and each SQL file verbatim with `mcp__Lovable__query_database`, then verify counts by state and category.
3. If core questions changed during the run, reload the core the same way (`--core`, after `delete from questions where state is null`). If you reword a few questions already in the app (for example to pass the originality check), update those rows in place with `update questions set ... where state = 'XX' and question_text = '...'` and check they match the bank.
4. Ebook: the EPUB upload is batched at the end of all states (see App URL and owner reminders); the upload host is blocked from this workspace, so the owner does it.
No code changes are needed per state; only send a Lovable message for real app bugs or features, batched, with the owner's OK.

## 7. Commit and report
1. Commit on `main` with the session attribution lines, fetch, push. Never commit a file an agent is still editing.
2. Update the state's row in `docs/states.md` (verified test format, status Done).
3. Send the PDF and EPUB from `out/XX/` with SendUserFile.
4. Report briefly: page count; verified test format and any mismatch; wrong keys or legal errors the fact check fixed; facts most likely to change; open items for the owner.

## Owner preferences
Concise and direct; no em or en dashes anywhere; verify on the web; report only issues that affect product quality; do not lecture about risks already addressed. Use as few Lovable credits as possible: data goes in through SQL.

## App URL and owner reminders
- The app URL is final: https://permit-path-practice.lovable.app (`app_url_final: true`). Every build must pass QA with no exceptions. Never change the URL without rebuilding every finished state.
- When the last of the owner's planned state editions is done, remind the owner to upload all EPUBs to the app's `ebooks` bucket (`XX.epub`), listing every EPUB with its target file name. Do not raise it in earlier state reports.
