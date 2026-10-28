"""Lint the question bank. Usage: python3 tools/check_bank.py bank/core.json [bank/PA.json ...]
Checks schema, unique IDs, quiz counts, answer-letter balance, banned wording and dashes. Exit 1 on errors."""
import json, sys, re, collections

KEYS = {"id", "ch", "quiz", "q", "a", "b", "c", "d", "correct", "exp", "src"}
BANNED = [r"\ball of the above\b", r"\bnone of the above\b", r"\bboth [abcd] and [abcd]\b", "—", "–", r"\bInkwise\b", r"\bDaniel Hart\b"]
errors, warns = [], []
for path in sys.argv[1:]:
    rows = json.load(open(path))
    core = path.endswith("core.json")
    ids = collections.Counter(r.get("id") for r in rows)
    for i, n in ids.items():
        if n > 1:
            errors.append(f"{path}: duplicate id {i}")
    per_ch = collections.defaultdict(list)
    for r in rows:
        rid = r.get("id", "?")
        missing = KEYS - set(r)
        if missing:
            errors.append(f"{rid}: missing {sorted(missing)}")
            continue
        if r["correct"] not in "ABCD" or len(r["correct"]) != 1:
            errors.append(f"{rid}: correct must be A, B, C or D")
        opts = [r[k].strip().lower() for k in "abcd"]
        if len(set(opts)) < 4:
            errors.append(f"{rid}: duplicate options")
        text = " ".join(str(r[k]) for k in ("q", "a", "b", "c", "d", "exp"))
        for b in BANNED:
            if re.search(b, text, re.I):
                errors.append(f"{rid}: banned text {b!r}")
        if not r["exp"].strip() or not r["src"].strip():
            errors.append(f"{rid}: empty explanation or source")
        per_ch[r["ch"]].append(r)
    for ch, rs in sorted(per_ch.items()):
        q = sum(1 for r in rs if r["quiz"])
        if core and (len(rs) < 30 or q != 10):
            errors.append(f"{path} ch{ch}: {len(rs)} questions, {q} quiz (need 30+ and exactly 10 quiz)")
        letters = collections.Counter(r["correct"] for r in rs)
        top = max(letters.values()) / len(rs)
        if len(rs) >= 20 and top > 0.35:
            warns.append(f"{path} ch{ch}: answer letters unbalanced {dict(letters)}")
    letters = collections.Counter(r["correct"] for r in rows)
    print(f"{path}: {len(rows)} questions, chapters {sorted(per_ch)}, letters {dict(sorted(letters.items()))}")
# Originality: every bank question can be printed in some state's mocks, so check each one as the book prints it.
import subprocess, tempfile, pathlib as _pl
_root = _pl.Path(__file__).resolve().parent.parent
for path in sys.argv[1:]:
    md = "\n\n".join(f"**1. {r['q']}**\n\nA) {r['a']}  \nB) {r['b']}  \nC) {r['c']}  \nD) {r['d']}\n\n**1. {r['correct']}.** {r['exp']}\n\n<!-- {r['id']} -->"
                     for r in json.load(open(path)))
    with tempfile.NamedTemporaryFile("w", suffix=".md", delete=False) as f:
        f.write(md)
    res = subprocess.run([sys.executable, str(_root / "tools/originality_check.py"), "check", f.name], capture_output=True, text=True)
    if res.returncode:
        errors.append(f"{path}: originality check failed\n" + res.stdout.strip()[-1500:])
for w in warns:
    print("WARN", w)
if errors:
    print("BANK FAILED:\n- " + "\n- ".join(errors[:50]))
    sys.exit(1)
print("BANK PASSED")
