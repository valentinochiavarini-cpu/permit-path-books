"""Pick the two mock exams for a state. Usage: make_mocks.py XX SIZE "PASS TEXT" [seed]
About 60 percent core, 40 percent state questions; never a chapter-quiz question; no repeats; spread across chapters.
Writes state/XX/mocks.json."""
import json, sys, random, pathlib, collections
ROOT = pathlib.Path(__file__).resolve().parent.parent
code, size, pass_text = sys.argv[1].upper(), int(sys.argv[2]), sys.argv[3]
rng = random.Random(int(sys.argv[4]) if len(sys.argv) > 4 else 2027)
core = [r for r in json.loads((ROOT / "bank/core.json").read_text()) if not r.get("quiz")]
st = [r for r in json.loads((ROOT / f"bank/{code}.json").read_text()) if not r.get("quiz")]

def spread(pool, n):
    by = collections.defaultdict(list)
    for r in pool:
        by[r["ch"]].append(r)
    for v in by.values():
        rng.shuffle(v)
    out, chs = [], sorted(by)
    while len(out) < n and any(by.values()):
        for c in chs:
            if by[c] and len(out) < n:
                out.append(by[c].pop())
    return out

n_state = round(size * 0.4)
picks = []
for _ in range(2):
    s = spread([r for r in st if r not in picks], n_state) + spread([r for r in core if r not in picks], size - n_state)
    rng.shuffle(s)
    picks += s
m1, m2 = picks[:size], picks[size:2 * size]
out = {"size": size, "pass": pass_text, "mock1": [r["id"] for r in m1], "mock2": [r["id"] for r in m2]}
(ROOT / f"state/{code}/mocks.json").write_text(json.dumps(out, indent=1))
for k, m in (("mock1", m1), ("mock2", m2)):
    print(k, len(m), "letters", dict(collections.Counter(r["correct"] for r in m)))
