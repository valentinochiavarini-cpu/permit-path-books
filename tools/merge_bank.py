"""Merge per-chapter bank files (bank/_chNN.json) into bank/core.json, replacing that chapter's questions.
Usage: python3 tools/merge_bank.py            # merges every bank/_ch*.json, then deletes them"""
import json, pathlib
ROOT = pathlib.Path(__file__).resolve().parent.parent
core_p = ROOT / "bank/core.json"
core = json.loads(core_p.read_text()) if core_p.exists() else []
for f in sorted((ROOT / "bank").glob("_ch*.json")):
    rows = json.loads(f.read_text())
    chs = {r["ch"] for r in rows}
    core = [r for r in core if r["ch"] not in chs] + rows
    print(f"merged {f.name}: {len(rows)} questions, chapters {sorted(chs)}")
    f.unlink()
core.sort(key=lambda r: (r["ch"], r["id"]))
core_p.write_text(json.dumps(core, indent=1, ensure_ascii=False) + "\n")
print(f"bank/core.json: {len(core)} questions")
