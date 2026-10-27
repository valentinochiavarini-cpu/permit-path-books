# State brief: Permit Path state edition

You are writing the state-specific parts of one Permit Path state edition. Read first: `docs/decisions.md`, `briefs/CORE_SPEC.md`, `briefs/CORE_WRITER_BRIEF.md` (voice, style, originality; the state-neutral rule does not apply to you) and `core/ch02.md` (model formatting). Today is October 2026.

## Sources
1. The official state driver manual. Read it with the Google Drive connector (load `mcp__Google_Drive__read_file_content` with ToolSearch; the file ID is in `docs/states.md`), or `state/XX/handbook.txt` if the run leader saved it. Never download it as base64. Check the agency website for a newer edition; if one exists, use it and say so.
2. The state agency website (permits, licensing, fees, testing, GDL, new residents, foreign licenses).
3. State statutes for numbers the manual leaves vague (fines, BAC, implied consent, phone laws). Cite the section.
Never paraphrase the manual's sentences; teach the facts in Permit Path's own words. Never invent a figure, form name or deadline. If you cannot verify something, leave it out and log it.

## Output
1. `state/XX/ch01.md`: `# Chapter 1: Your Path to a {{STATE}} License` (2,500 to 3,500 words). Cover in this order:
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
2. `state/XX/inserts.md`: every key listed in `CORE_SPEC.md`, each 30 to 150 words, exact state figures with the rule stated plainly. Use `OMIT` only when the state truly has no rule beyond the national one. `supervised_hours`: total, night, and any other category. `dui_penalties` must also state the open container rule (core Chapter 11 points there).
3. `bank/XX.json`: 130 to 160 questions, IDs `XX-001` upward. About 40 on Chapter 1 topics (`ch: 1`, exactly 10 with `quiz: true`), the rest on insert topics, tagged with the core chapter number where the insert appears (`quiz: false`). Format and rules in `CORE_SPEC.md`. Run `python3 tools/check_bank.py bank/XX.json`.
4. `state/XX/sources.md`: table of claim, source (URL or manual page), date checked, for every number, fee, deadline and rule.

Run `python3 tools/originality_check.py check state/XX/ch01.md state/XX/inserts.md` and fix any failure.

Reply with: word count, the knowledge test format you verified (and any mismatch with docs/states.md), the 5 facts most likely to change soon, and anything unverified.
