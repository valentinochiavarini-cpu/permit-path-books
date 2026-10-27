# Permit Path books

Source, briefs and build pipeline for the **Permit Path** state drivers ed books (KDP, 6 x 9 B&W paperback + EPUB). Read `docs/decisions.md` before changing anything: it records what the owner approved. `docs/states.md` holds per-state test facts and status.

## Layout of this repo
- `core/`: universal core shared by every state: `00_front.md`, `ch02.md` to `ch13.md`, `90_mocks.md`, `95_driving_log.md`. `core/notes/` holds writing and fact-check logs.
- `state/XX/`: per state: `ch01.md` (state chapter), `inserts.md` (state values for the core's `{{INSERT:key}}` markers), `mocks.json` (mock exam question IDs), `sources.md`, fact-check logs. `handbook.pdf` is gitignored.
- `bank/`: question bank, the single source of truth for every printed and app question (`core.json`, `XX.json`).
- `layout/`: build pipeline (`build_book.py`, `build.py`, CSS, `config.json` with the app URL).
- `tools/`: `check_book.py` (QA, run by the build), `originality_check.py` (vs Daniel Hart, run by the build), `check_bank.py` (bank lint).
- `ref/`: hashed 8-word sequences of the Daniel Hart texts (no raw text).
- `briefs/`: `CORE_SPEC.md` (chapter plan, inserts, bank format) and agent briefs.
- `out/XX/`: deliverables (PDF, EPUB).

## Build
```bash
cd layout && npm install --silent && cd ..
python3 layout/build_book.py --state Pennsylvania --code PA
python3 layout/build_book.py --core-only        # core preview with sample inserts
```
Chromium is at `/opt/pw-browsers/chromium` (never run `playwright install`). Needs pandoc and poppler. The build fails on: unfilled placeholders or inserts, em or en dashes, company or pen names, wrong trim size, contents page numbers that shift, invalid EPUB, quiz count mismatch, originality check failure.

## Markdown conventions
See `briefs/CORE_SPEC.md`. Callouts: `> **On the test**`, `> **Test trap:**`, `> **Road tip:**`, `> **Remember it:**`. `{{STATE}}` becomes the state name; `{{INSERT:key}}` the state's insert; `{{QUIZ}}` the chapter quiz from the bank; `[APP-LINK:N]` the chapter's practice URL.

## Session rules
- No em or en dashes anywhere. Brand only: never "Inkwise", "Daniel Hart", "Driving School" or a year in the book.
- Verify facts on primary sources; log them in `core/notes/` or `state/XX/sources.md`.
- Commit with the session attribution lines; fetch before pushing.
