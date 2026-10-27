"""Automatic QA for a built edition. Usage: check_book.py BOOK.pdf BOOK.epub N_CHAPTERS [--preview]
Fails (exit 1) on anything that would ship a broken book."""
import sys, subprocess, zipfile, re, json, pathlib
from xml.dom import minidom

pdf, epub, n_ch = sys.argv[1], sys.argv[2], int(sys.argv[3])
preview = "--preview" in sys.argv
cfg = json.loads((pathlib.Path(__file__).resolve().parent.parent / "layout" / "config.json").read_text())
errors = []
txt = subprocess.run(["pdftotext", pdf, "-"], capture_output=True, text=True).stdout
pages = txt.split("\f")
BAD = [("{{", "unfilled placeholder"), ("APP-LINK", "unresolved app link"), ("@@", "build marker"), ("—", "em dash"), ("–", "en dash"),
       ("Inkwise", "company name"), ("Daniel Hart", "other series author"), ("Driving School", "other brand"), ("[FIGURE", "figure placeholder")]
for bad, label in BAD:
    hits = [i + 1 for i, p in enumerate(pages) if bad in re.sub(r"@@TOC:k\d+@@", "", p)]
    if hits:
        errors.append(f"PDF: {label} on pages {hits[:5]}")
if re.search(r"\b20[2-3]\d\b", txt.split("Contents")[0] if "Contents" in txt else ""):
    errors.append("PDF: a year appears on the title or copyright page")
cards = len(re.findall(r"Keep practicing Chapter \d+", txt))
if cards != n_ch:
    errors.append(f"PDF: {cards} chapter practice cards, expected {n_ch}")
info = subprocess.run(["pdfinfo", pdf], capture_output=True, text=True).stdout
npages = int(re.search(r"Pages:\s+(\d+)", info).group(1))
if "432 x 648" not in info:
    errors.append("PDF: trim size is not 6 x 9 in")
if not preview and not cfg.get("app_url_final"):
    errors.append("config: app_url_final is false (set the final app URL before shipping)")

z = zipfile.ZipFile(epub)
xh = [n for n in z.namelist() if n.endswith(".xhtml")]
for n in xh:
    try:
        minidom.parseString(z.read(n))
    except Exception as e:
        errors.append(f"EPUB: {n} invalid XHTML ({e})")
et = "".join(z.read(n).decode("utf-8", "ignore") for n in xh)
for bad, label in [("{{", "placeholder"), ("—", "em dash"), ("Inkwise", "company name"), ("@@", "build marker")]:
    if bad in et:
        errors.append(f"EPUB: {label} found")
links = len(re.findall(r'href="' + re.escape(cfg["app_base"]) + r'/ch/\d+"', et))
if links != n_ch:
    errors.append(f"EPUB: {links} chapter links, expected {n_ch}")

print(f"QA: {npages} pages, {cards} chapter cards, {len(xh)} EPUB files, {links} EPUB chapter links")
if errors:
    print("QA FAILED:\n- " + "\n- ".join(errors))
    sys.exit(1)
print("QA PASSED")
