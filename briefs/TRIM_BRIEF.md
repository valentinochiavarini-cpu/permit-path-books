# Trim brief: shorter Permit Path chapters

The owner wants the book around 160 to 170 printed pages (it was 259). Page count drives print cost and therefore profit. The market leader runs about 110 pages. Permit Path must stay friendlier, clearer and more complete than the official manual, but without padding.

## Targets
- Core chapters 2 to 12: 1,700 to 2,000 words each before the quiz (they are about 2,500 to 3,400 now). Chapter 13: 1,500 words.
- State Chapter 1: 2,000 to 2,300 words. State inserts: 90 words or fewer each, figures and rules only.
- Callouts: at most 5 per chapter. Quick Review: 5 bullets, one line each.

## What to cut
- Sentences that repeat a rule already stated, restate the heading, or explain the obvious.
- Long scene-setting openings: keep the opening to 2 or 3 short sentences.
- Background that is not tested and does not change what a new driver does.
- Tables and bullet lists that say the same thing as the paragraph next to them: keep the clearer one.
- Hedged asides ("Some drivers find that..."). Keep the rule.

## What must stay
- Every fact any question in `bank/core.json` (or `bank/XX.json` for state files) tests for that chapter. Before you finish, read each of the chapter's 30 questions and confirm the text still teaches the keyed answer. List any you had to keep text for.
- Every `{{INSERT:key}}` line, the `{{QUIZ}}` line, the practice line, every figure line `![...](fig/...)` with a lead-in sentence, and every "most states", "many states" hedge the fact checkers added (they exist because the rule is not national).
- The voice (calm instructor, second person, short sentences) and colors named in words.

## Rules
- Cut and tighten only. Do not add facts, change rules, or reword a rule in a way that changes its meaning. If two sentences merge, the merged one must say exactly what both said.
- No em or en dashes. Run `python3 tools/originality_check.py check` on every file you edit; it must pass.
- Report per chapter: words before and after, anything you were unsure about cutting.
