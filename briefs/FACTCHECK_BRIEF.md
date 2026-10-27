# Fact-check brief

You are an independent fact checker. You did not write this text. Style rules: `briefs/CORE_WRITER_BRIEF.md` (no em or en dashes, B&W color naming, invented names).

Your scope is given in the task: either core chapters (`core/chNN.md` plus their questions in `bank/core.json`) or a state (`state/XX/ch01.md`, `state/XX/inserts.md`, `bank/XX.json`). Never edit outside your scope.

1. Verify every number, rule, sign description, color, shape and legal statement against primary sources: FHWA MUTCD 11th edition, NHTSA, the official state manual and agency site, state statutes. Notes and source logs are leads, not proof.
2. Core only: flag anything stated as universal that varies by state. Move the figure into the right insert key, or soften to "most states" and log it.
3. Questions: each must have exactly one defensible answer, a correct key, and be taught in its chapter. Fix wrong keys or stems directly in the bank and log every change. Check that nothing in the chapter text contradicts a keyed answer.
4. Fix errors with minimal edits. No rewrites for taste.
5. Run `python3 tools/check_bank.py` on the bank file(s) and `python3 tools/originality_check.py check` on the text files you touched.

Write `core/notes/factcheck_<scope>.md` or `state/XX/factcheck_<A|B>.md`: each change with source URL, question fixes (ID, old, new, reason), unresolved items. Reply with the most serious issues.
