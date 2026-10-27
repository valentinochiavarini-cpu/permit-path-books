"""Build a Permit Path state edition: 6 x 9 B&W paperback PDF and EPUB.

Usage (from the repo root):
  python3 layout/build_book.py --state Pennsylvania --code PA     # -> out/PA/
  python3 layout/build_book.py --core-only                        # core preview with sample inserts -> out/core/
"""
import sys, pathlib, subprocess, re, argparse, json, random
sys.path.insert(0, str(pathlib.Path(__file__).parent))
from build import md_to_html, HERE, CFG
ROOT = HERE.parent

ap = argparse.ArgumentParser()
ap.add_argument("--state")
ap.add_argument("--code")
ap.add_argument("--core-only", action="store_true")
args = ap.parse_args()
if args.core_only:
    state, code, sdir = "Sample State", None, ROOT / "core" / "sample"
else:
    if not (args.state and args.code):
        sys.exit("--state and --code are required unless --core-only")
    state, code, sdir = args.state, args.code.upper(), ROOT / "state" / args.code.upper()
OUT = ROOT / "out" / (code or "core"); OUT.mkdir(parents=True, exist_ok=True)
stem = f"Permit_Path_{state.replace(' ', '_')}" if code else "Core_preview"
BASE, SHORT = CFG["app_base"], CFG["app_short"]
errors = []

# ---------- QR codes ----------
try:
    import segno
except ImportError:
    subprocess.run([sys.executable, "-m", "pip", "install", "-q", "--break-system-packages", "segno"], check=True); import segno
qr = HERE / "qr"; qr.mkdir(exist_ok=True)
for name, url in [("home", BASE)] + [(f"ch{n}", f"{BASE}/ch/{n}") for n in range(1, 14)]:
    segno.make(url, error="m").save(str(qr / f"{name}.svg"), scale=4, border=2)

# ---------- question bank ----------
def load(p):
    return json.loads(p.read_text()) if p.exists() else []
bank = load(ROOT / "bank" / "core.json") + (load(ROOT / "bank" / f"{code}.json") if code else load(sdir / "bank.json"))
byid = {r["id"]: r for r in bank}

def q_md(n, r):
    return f"**{n}. {r['q']}**\n\nA) {r['a']}  \nB) {r['b']}  \nC) {r['c']}  \nD) {r['d']}\n"

def a_md(n, r):
    return f"**{n}. {r['correct']}.** {r['exp'].strip()}\n"

def quiz(ch):
    rows = [r for r in bank if r["ch"] == ch and r.get("quiz")]
    if len(rows) != 10:
        errors.append(f"Chapter {ch}: {len(rows)} quiz questions in the bank, expected 10")
    qs = "\n".join(q_md(i + 1, r) for i, r in enumerate(rows))
    ans = "\n".join(a_md(i + 1, r) for i, r in enumerate(rows))
    return f"{qs}\n### Chapter {ch} Quiz Answers\n\n{ans}"

# ---------- inserts ----------
ins_text = (sdir / "inserts.md").read_text() if (sdir / "inserts.md").exists() else ""
inserts = {m.group(1).strip(): m.group(2).strip() for m in re.finditer(r"(?ms)^## ([a-z_]+)\s*\n(.*?)(?=^## |\Z)", ins_text)}
for k in CFG["insert_keys"]:
    if k not in inserts:
        errors.append(f"inserts.md: missing key {k}")

def fill_inserts(t):
    def rep(m):
        k = m.group(1)
        body = inserts.get(k)
        if body is None:
            errors.append(f"insert {k} used in text but missing"); return ""
        if body.strip() == "OMIT":
            return ""
        lines = [f"**{state} rule:**", ""] + body.splitlines()
        return "\n".join("> " + l if l.strip() else ">" for l in lines)
    return re.sub(r"(?m)^\{\{INSERT:([a-z_]+)\}\}\s*$", rep, t)

# ---------- mocks ----------
mock_cfg = load(sdir / "mocks.json") if (sdir / "mocks.json").exists() else {}
def mocks_md():
    size = mock_cfg.get("size", CFG["default_mock_size"])
    sets = []
    if mock_cfg:
        sets = [[byid[i] for i in mock_cfg["mock1"]], [byid[i] for i in mock_cfg["mock2"]]]
    else:  # preview only: deterministic sample of non-quiz questions
        pool = [r for r in bank if not r.get("quiz")]
        random.Random(7).shuffle(pool)
        sets = [pool[:size], pool[size:2 * size]]
    intro = (ROOT / "core" / "90_mocks.md").read_text().replace("{{MOCK_SIZE}}", str(size)).replace("{{MOCK_PASS}}", mock_cfg.get("pass", "80 percent"))
    out = [intro]
    for k, s in enumerate(sets, 1):
        if mock_cfg and len(s) != size:
            errors.append(f"Mock {k}: {len(s)} questions, expected {size}")
        out.append(f"# Mock Exam {k}\n\n" + "\n".join(q_md(i + 1, r) for i, r in enumerate(s)))
    out.append("# Mock Exam Answer Key\n\n" + "\n\n".join(
        f"## Mock Exam {k}\n\n" + "\n".join(a_md(i + 1, r).rstrip() + f" (Chapter {r['ch']})\n" for i, r in enumerate(s)) for k, s in enumerate(sets, 1)))
    used_quiz = [r["id"] for s in sets for r in s if r.get("quiz")]
    if mock_cfg and used_quiz:
        errors.append(f"mocks reuse chapter quiz questions: {used_quiz[:5]}")
    return "\n\n".join(out)

# ---------- assemble ----------
ch01 = sdir / "ch01.md"
parts = [ROOT / "core" / "00_front.md"] + ([ch01] if ch01.exists() else [])
parts += [ROOT / "core" / f"ch{n:02d}.md" for n in CFG["core_chapters"] if (ROOT / "core" / f"ch{n:02d}.md").exists()]
missing = [n for n in CFG["core_chapters"] if not (ROOT / "core" / f"ch{n:02d}.md").exists()]
if code and (missing or not ch01.exists()):
    errors.append(f"missing chapters: {missing + ([] if ch01.exists() else [1])}")
mds = []
for p in parts:
    t = p.read_text()
    m = re.search(r"(?m)^# Chapter (\d+):", t)
    if "{{QUIZ}}" in t and m:
        t = t.replace("{{QUIZ}}", quiz(int(m.group(1))))
    mds.append(t)
mds.append(mocks_md())
mds.append((ROOT / "core" / "95_driving_log.md").read_text())
full = "\n\n".join(mds)
full = fill_inserts(full).replace("{{STATE}}", state)
full = re.sub(r"\[APP-LINK:(\d+)\]", rf"{SHORT}/ch/\1", full)
(OUT / f"{stem}.md").write_text(full)

APP_BOX = (f'<div class="app-box"><img src="qr/home.svg"><div><div class="app-kicker">Free with this book</div>'
           f'<div class="app-head">Permit Path online practice</div><ul class="app-list">'
           f'<li>500+ {state} practice questions with explanations</li><li>Full-color road sign flashcards</li>'
           f'<li>Timed practice tests built like the real one</li><li>A free ebook copy to study on your phone</li></ul>'
           f'<div class="app-foot">Scan the code or go to <span class="url">{SHORT}</span></div></div></div>')
APP_MD = (f"**Free with this book: Permit Path online practice**\n\n- 500+ {state} practice questions with explanations\n"
          f"- Full-color road sign flashcards\n- Timed practice tests built like the real one\n- A free ebook copy to study on your phone\n\n"
          f"Go to [{SHORT}]({BASE}).")

TITLE_HTML = (f'<section class="titlepage"><div class="tp-brand">Permit Path</div><div class="tp-main">'
              f'<div class="tp-state">{state}</div><div class="tp-title">Drivers Ed Book</div>'
              f'<div class="tp-sub">Driver\'s License Handbook and Permit Practice Test Book for Teens and First-Time Drivers</div>'
              f'<div class="tp-tag">Chapter quizzes, two full mock exams and 500+ free online practice questions, plus full-color road sign flashcards and a free ebook download.</div></div>'
              f'<div class="tp-foot"><span>Permit Path</span><span>{SHORT}</span></div></section>')

def split_chunks(t):
    return [c for c in re.split(r"(?m)^(?=# )", t) if c.strip()]

chunks = split_chunks(full)
entries, html_parts = [], []
PART = {1: f"Part 1: Your {state} License", 2: "Part 2: Rules of the Road", 13: "Part 3: Test Day"}
cur_part = "Getting Started"
for i, c in enumerate(chunks):
    first = c.strip().splitlines()[0].lstrip("# ").strip()
    h = md_to_html(c.replace("{{APP_BOX}}", "XXAPPBOXXX")).replace("<p>XXAPPBOXXX</p>", APP_BOX)
    key = f"k{i}"
    m = re.match(r"Chapter (\d+):\s*(.+)", first)
    if m:
        n = int(m.group(1)); cur_part = PART.get(n, cur_part)
        entries.append((key, cur_part, str(n), m.group(2).strip()))
    elif first != "Copyright":
        if first.startswith("Mock") or first.startswith("Supervised"):
            cur_part = PART[13]
        entries.append((key, cur_part, "", first))
    else:
        html_parts.append(h.replace('<section class="part">', '<section class="part copyright">', 1)); continue
    html_parts.append(h.replace("</h1>", f'<span class="tocm">@@TOC:{key}@@</span></h1>', 1))

def toc_html(pages):
    out, last = ['<section class="toc"><h1>Contents</h1>'], None
    for key, part, n, title in entries:
        if part != last:
            out.append(f'<div class="toc-part">{part}</div>'); last = part
        out.append(f'<div class="toc-row"><span class="n">{n}</span><span class="t">{title}</span><span class="dots"></span><span class="p">{pages.get(key, "00")}</span></div>')
    return "".join(out) + "</section>"

def assemble(pages):
    body = "".join(html_parts)
    i = body.find('<h1 id="how-to-use-this-book"')
    i = body.rfind('<section', 0, i)
    body = body[:i] + toc_html(pages) + body[i:]
    body = body.replace('<section class="part"><h1 id="supervised', '<section class="part log"><h1 id="supervised')
    return TITLE_HTML + body

def render(body):
    (HERE / f"{stem}.html").write_text(f'<!doctype html><html><head><meta charset="utf-8"><link rel="stylesheet" href="book.css"></head><body>{body}</body></html>')
    js = f"""const {{ chromium }} = require('playwright');
(async () => {{ const b = await chromium.launch({{ executablePath: '/opt/pw-browsers/chromium' }});
const p = await b.newPage(); await p.goto('file://{HERE}/{stem}.html'); await p.evaluate(() => document.fonts.ready);
await p.pdf({{ path: '{OUT}/{stem}.pdf', preferCSSPageSize: true, printBackground: true }}); await b.close(); }})();"""
    subprocess.run(["node", "-e", js], check=True, cwd=HERE)
    txt = subprocess.run(["pdftotext", str(OUT / f"{stem}.pdf"), "-"], capture_output=True, text=True).stdout.split("\f")
    pages = {}
    for i, pg in enumerate(txt):
        for k in re.findall(r"@@TOC:(k\d+)@@", pg):
            pages.setdefault(k, i + 1)
    return pages

pages = render(assemble({}))
pages2 = render(assemble(pages))
if pages != pages2:
    errors.append("contents page numbers shifted between passes")

# ---------- EPUB ----------
emd = full.replace("{{APP_BOX}}", APP_MD)
emd = re.sub(r"\*\*Practice this chapter online:\*\* scan the code or go to (\S+/ch/\d+)", rf"**Practice this chapter online:** go to [\1](https://\1)", emd)
emd = emd.replace(f"https://{SHORT}", BASE)
assert "<div" not in emd and "<img" not in emd, "raw HTML left in ebook source"
(OUT / f"{stem}_ebook.md").write_text(emd)
meta = ["--metadata", f"title={state} Drivers Ed Book", "--metadata", "subtitle=Driver's License Handbook and Permit Practice Test Book for Teens and First-Time Drivers",
        "--metadata", "author=Permit Path", "--metadata", "publisher=Permit Path", "--metadata", "lang=en-US"]
subprocess.run(["pandoc", str(OUT / f"{stem}_ebook.md"), "-o", str(OUT / f"{stem}.epub"), "--css", str(HERE / "epub.css"), "--toc", "--toc-depth=1", "--split-level=1"] + meta, check=True)
(HERE / f"{stem}.html").unlink(missing_ok=True)
print("built", OUT / f"{stem}.pdf", "| words", len(full.split()))

if errors:
    print("BUILD ERRORS:\n- " + "\n- ".join(errors))
n_ch = len([e for e in entries if e[2]])
qa = subprocess.run([sys.executable, str(ROOT / "tools" / "check_book.py"), str(OUT / f"{stem}.pdf"), str(OUT / f"{stem}.epub"), str(n_ch)] + (["--preview"] if args.core_only else []))
orig = subprocess.run([sys.executable, str(ROOT / "tools" / "originality_check.py"), "check", str(OUT / f"{stem}.md")])
if errors or qa.returncode or orig.returncode:
    sys.exit(1)
