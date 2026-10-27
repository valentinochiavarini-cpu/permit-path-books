"""Write SQL files that load bank questions into the Permit Path app (Lovable Cloud table `questions`).

Usage:
  python3 tools/export_app_sql.py --core OUT_DIR            # core questions (state = null)
  python3 tools/export_app_sql.py --state PA OUT_DIR        # one state's questions (state = 'PA')

Each file holds up to 100 rows and is run as-is with the Lovable query tool. Category = "Chapter N: Title",
which the app's /ch/:n route uses. To reload, first delete that scope:
  delete from questions where state is null;      or      delete from questions where state = 'PA';
"""
import json, re, sys, pathlib, argparse
ROOT = pathlib.Path(__file__).resolve().parent.parent
ap = argparse.ArgumentParser()
g = ap.add_mutually_exclusive_group(required=True)
g.add_argument("--core", action="store_true")
g.add_argument("--state")
ap.add_argument("out")
a = ap.parse_args()
out = pathlib.Path(a.out); out.mkdir(parents=True, exist_ok=True)

titles = {}
for n in range(2, 14):
    titles[n] = re.search(r"(?m)^# Chapter \d+: (.+)$", (ROOT / f"core/ch{n:02d}.md").read_text()).group(1).strip()
if a.state:
    code = a.state.upper()
    name = json.loads((ROOT / "layout/config.json").read_text()).get("state_names", {}).get(code)
    ch1 = re.search(r"(?m)^# Chapter 1: (.+)$", (ROOT / f"state/{code}/ch01.md").read_text()).group(1)
    if "{{STATE}}" in ch1:
        if not name:
            sys.exit("add the state name to layout/config.json state_names")
        ch1 = ch1.replace("{{STATE}}", name)
    titles[1] = ch1.strip()
    src, st = ROOT / f"bank/{code}.json", code
else:
    src, st = ROOT / "bank/core.json", None

rows = [{"question_text": r["q"], "answers": {"A": r["a"], "B": r["b"], "C": r["c"], "D": r["d"]},
         "correct_answer": r["correct"], "explanation": r["exp"], "category": f"Chapter {r['ch']}: {titles[r['ch']]}",
         "state": st} for r in json.loads(src.read_text())]
tag = st or "core"
for i in range(0, len(rows), 100):
    body = json.dumps(rows[i:i + 100], ensure_ascii=False, separators=(",", ":"))
    assert "$j$" not in body
    sql = ("insert into questions (question_text,answers,correct_answer,explanation,category,state) "
           "select question_text,answers,correct_answer,explanation,category,state from jsonb_to_recordset($j$" + body +
           "$j$::jsonb) as x(question_text text,answers jsonb,correct_answer text,explanation text,category text,state text) returning 1")
    (out / f"{tag}_{i // 100}.sql").write_text(sql)
print(f"{len(rows)} {tag} questions -> {out}")
