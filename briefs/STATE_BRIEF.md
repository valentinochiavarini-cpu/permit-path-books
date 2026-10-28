# State brief: Permit Path state edition

You are writing the state-specific parts of one Permit Path state edition. Read first: `docs/decisions.md`, `briefs/CORE_SPEC.md`, `briefs/CORE_WRITER_BRIEF.md` (voice, style, originality; the state-neutral rule does not apply to you) and `core/ch02.md` (model formatting). Today is October 2026.

## Sources
1. The official state driver manual. Read it with the Google Drive connector (load `mcp__Google_Drive__read_file_content` with ToolSearch; the file ID is in `docs/states.md`), or `state/XX/handbook.txt` if the run leader saved it. Never download it as base64. Check the agency website for a newer edition; if one exists, use it and say so.
2. The state agency website (permits, licensing, fees, testing, GDL, new residents, foreign licenses).
3. State statutes for numbers the manual leaves vague (fines, BAC, implied consent, phone laws). Cite the section.
Never paraphrase the manual's sentences; teach the facts in Permit Path's own words. Never invent a figure, form name or deadline. If you cannot verify something, leave it out and log it.

## Output
1. `state/XX/ch01.md`: `# Chapter 1: Your Path to a {{STATE}} License` (2,000 to 2,300 words; the book must stay near 175 pages, see `briefs/TRIM_BRIEF.md`). Cover in this order:
   - Who needs what: learner's permit, junior or provisional license, full license; minimum ages.
   - What to bring: identity, residency, Social Security number, parent or guardian consent for minors; REAL ID choice.
   - Fees (as of the current fee schedule, with source).
   - The knowledge test: number of questions, pass mark, sign section if any, languages, retake waits, where to take it, online testing if offered. Must match `docs/states.md`; report any difference.
   - Vision test.
   - Graduated license rules: permit holding period, supervised hours (day and night), passenger limits, curfew, phone ban for teens, how the restrictions lift.
   - The road test: how to schedule, what car and documents to bring, what is scored, automatic fails.
   - Adults getting their first license (18+): what changes.
   - Foreign license holders and, only where a test applies, new residents. Use the facts in `docs/states.md`.
   - Where to find the official manual and agency.
   Then `## Quick Review`, `## Chapter 1 Quiz` with `{{QUIZ}}`, and the practice line with `[APP-LINK:1]`.
2. `state/XX/inserts.md`: every key listed in `CORE_SPEC.md`, each 90 words or fewer (figures and rules only, no background), exact state figures with the rule stated plainly. Use `OMIT` only when the state truly has no rule beyond the national one. `supervised_hours`: total, night, and any other category. `dui_penalties` must also state the open container rule (core Chapter 11 points there). `turn_on_red` must cover right on red, turning on a red arrow, and left on red from one-way to one-way. `school_bus` must cover divided highways and the minimum stopping distance.
3. `bank/XX.json`: 130 to 160 questions, IDs `XX-001` upward. About 40 on Chapter 1 topics (`ch: 1`, exactly 10 with `quiz: true`), the rest on insert topics, tagged with the core chapter number where the insert appears (`quiz: false`). Format and rules in `CORE_SPEC.md`. If the state's test has a separate road sign part (for example GA, VA, NC; see `docs/states.md`), also write at least 25 state questions with `ch: 2` on signs, so both mocks can fill their sign part. Run `python3 tools/check_bank.py bank/XX.json`: it also runs the originality check on every question as printed, and must print BANK PASSED.
4. `state/XX/sources.md`: table of claim, source (URL or manual page), date checked, for every number, fee, deadline and rule.

Run `python3 tools/originality_check.py check state/XX/ch01.md state/XX/inserts.md` and fix any failure.

Figures: all 35 figures live in the core (`layout/fig/`). Do not add figures or image lines. Where Chapter 1 needs a picture of a sign, refer to the core chapter that shows it.

Reply with: word count, the knowledge test format you verified (and any mismatch with docs/states.md), the 5 facts most likely to change soon, and anything unverified.
