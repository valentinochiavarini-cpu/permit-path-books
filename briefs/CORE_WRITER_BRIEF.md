# Core writer brief: Permit Path drivers ed books

You are writing one or more chapters of the universal core of **Permit Path**, a series of state drivers ed books (one book per US state) for teens and first-time adult drivers studying for the written knowledge test and the road test. The same core is printed in every state edition, so it must be true in every state. Today is October 2026.

Read first:
- `/home/claude/permit-path-books/docs/decisions.md` (binding rules)
- `/home/claude/permit-path-books/briefs/CORE_SPEC.md` (your chapter's topics, insert keys, template, bank format)
- If a model chapter exists in `core/` (ch02.md), match its voice, depth and formatting exactly.

## Originality (hard rule)
The owner already publishes another DMV series. This book must not read like it or like any other book. Write every sentence fresh from the official sources below. Do not search for or read other DMV prep books, practice-test sites or their sample questions. After writing, run:
`python3 tools/originality_check.py check core/chNN.md`
It must pass (no 12-word run shared with the other series, under 1 percent shared 8-word sequences). If it fails, rewrite the flagged passages in different words and structure.

## Sources (verify facts here)
- FHWA Manual on Uniform Traffic Control Devices, 11th Edition (December 2023): sign shapes, colors, markings, signals. mutcd.fhwa.dot.gov
- NHTSA (nhtsa.gov), IIHS (iihs.org), GHSA (ghsa.org) for seat belts, child seats, BAC, distraction, state law summaries.
- Official state driver manuals (for example PennDOT, Florida, Texas, California, New York) to confirm a rule is national and to see how states phrase the test topics. Use them as fact sources, never as text to paraphrase.
If a rule varies by state, do not state one state's number as universal: give the common pattern ("most states") and put an insert marker where the state figure belongs.

## Voice
A calm, direct driving instructor talking to a 15 to 17 year old or a nervous first-time adult. Second person ("you"), short sentences, concrete situations ("You are waiting to turn left and the light turns yellow"). Explain the reason behind a rule in one line when it helps memory. No hype, no fluff, no "In this chapter we will", no "It is important to note". Define each term in bold the first time. The print is black and white: always name colors in words ("a yellow diamond", "a solid white line").

## Style rules
- No em dashes or en dashes anywhere. Use commas, colons, periods, parentheses. Write ranges as "15 to 20".
- Tables: max 3 columns, short cells (6 x 9 page).
- Invented names and places in examples. No real brand names.
- No figures that change by state outside an `{{INSERT:key}}` marker.

## Questions (bank/core.json)
For each chapter, write 30 questions into `bank/core.json` (create it as a JSON array if missing; if other writers are adding chapters at the same time, write your chapter to `bank/_chNN.json` instead and the run leader will merge). Format and rules in `CORE_SPEC.md`. Exactly 10 per chapter get `"quiz": true`: pick the 10 that best cover the chapter, mixing easy and hard. Every question must be taught in the chapter text. Spread correct letters evenly (about 7 or 8 each of A, B, C, D per chapter). Explanations 1 to 2 sentences, plain, no dashes. `src`: the MUTCD section, NHTSA page or manual section that proves the answer.
Run `python3 tools/check_bank.py bank/_chNN.json` (or bank/core.json) and fix all errors.

## Output per chapter
1. `core/chNN.md` (template in CORE_SPEC.md).
2. Questions as above.
3. `core/notes/chNN_notes.md`: facts verified with source URLs, rules you found that vary by state (and which insert key covers them), anything uncertain.

Reply with: files written, word count, originality result, bank check result, and any rule you were unsure was national.
