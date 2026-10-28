"""Pick the two mock exams for a state.

One-part test:  make_mocks.py XX SIZE "PASS TEXT" [--seed N]
Split test:     make_mocks.py XX --part "Road Signs|10|all 10 correct|2" --part "Rules of the Road|30|24 of 30 correct" [--seed N]
  A part is NAME|SIZE|PASS TEXT|CHAPTERS. CHAPTERS (comma list) limits the pool, e.g. 2 for road signs;
  leave it out for "any chapter except the restricted ones of other parts".
About 60 percent core, 40 percent state questions (a part limited to chapters uses whatever the pool holds,
state first); never a chapter-quiz question; no repeats; spread across chapters. Writes state/XX/mocks.json."""
import json, sys, random, pathlib, collections, argparse, re
ROOT = pathlib.Path(__file__).resolve().parent.parent
ap = argparse.ArgumentParser()
ap.add_argument("code"); ap.add_argument("size", nargs="?", type=int); ap.add_argument("pass_text", nargs="?")
ap.add_argument("--part", action="append", default=[]); ap.add_argument("--pass", dest="overall", default=""); ap.add_argument("--seed", type=int, default=2027)
a = ap.parse_args()
code = a.code.upper()
rng = random.Random(a.seed)
core = [r for r in json.loads((ROOT / "bank/core.json").read_text()) if not r.get("quiz")]
st = [r for r in json.loads((ROOT / f"bank/{code}.json").read_text()) if not r.get("quiz") and not r.get("app_only")]

parts = []
for p in a.part:
    f = p.split("|")
    parts.append({"name": f[0], "size": int(f[1]), "pass": f[2], "chapters": [int(x) for x in f[3].split(",")] if len(f) > 3 and f[3] else []})
if not parts:
    parts = [{"name": "", "size": a.size, "pass": a.pass_text, "chapters": []}]
restricted = {c for p in parts for c in p["chapters"]}

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

def build():
    used, mocks = set(), [[], []]
    for p in parts:
        ok = (lambda r: r["ch"] in p["chapters"]) if p["chapters"] else (lambda r: r["ch"] not in restricted)
        for k in range(2):
            sp = [r for r in st if ok(r) and r["id"] not in used]
            cp = [r for r in core if ok(r) and r["id"] not in used]
            n_state = round(p["size"] * 0.4)
            if p["chapters"]:  # small core pool: use state questions only for what the core cannot cover
                n_state = min(max(n_state, p["size"] - len(cp) // (2 - k)), len(sp), p["size"])
            s = spread(sp, n_state)
            s += spread(cp, p["size"] - len(s))
            if len(s) < p["size"]:
                s += spread([r for r in sp if r not in s], p["size"] - len(s))
            if len(s) < p["size"]:
                sys.exit(f"Not enough questions for part '{p['name']}' mock {k + 1}: {len(s)} of {p['size']}. Add state questions in chapters {p['chapters']}.")
            rng.shuffle(s)
            used.update(r["id"] for r in s)
            mocks[k] += s
    return mocks

def balanced(ms):
    # every answer letter at least 15 percent of each mock
    return all(min(collections.Counter(r['correct'] for r in m).get(L, 0) for L in 'ABCD') >= 0.15 * len(m) for m in ms)

for tries in range(500):
    rng = random.Random(a.seed + tries)
    mocks = build()
    if balanced(mocks):
        break
print('seed', a.seed + tries, '(balanced)' if balanced(mocks) else '(no balanced seed found)')

total = sum(p["size"] for p in parts)
out = {"size": total, "pass": a.overall or parts[0]["pass"] if len(parts) == 1 else a.overall or "; ".join(f"for {p['name']}, {p['pass']}" for p in parts),
       "mock1": [r["id"] for r in mocks[0]], "mock2": [r["id"] for r in mocks[1]]}
if len(parts) > 1:
    out["parts"] = [{"name": p["name"], "size": p["size"], "pass": p["pass"]} for p in parts]
(ROOT / f"state/{code}/mocks.json").write_text(json.dumps(out, indent=1))
for k, m in enumerate(mocks, 1):
    print(f"mock{k}", len(m), "state", sum(not re.match(r"C\d", r["id"]) for r in m), "letters", dict(collections.Counter(r["correct"] for r in m)))
