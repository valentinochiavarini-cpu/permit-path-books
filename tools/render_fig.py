"""Preview figures as they will print: renders layout/fig/NAME.svg to a grayscale PNG at print width.
Usage: python3 tools/render_fig.py NAME [NAME ...] OUT_DIR
Each PNG is 4.6 in wide at 150 dpi, converted to grayscale so you see the B&W result."""
import sys, subprocess, pathlib
ROOT = pathlib.Path(__file__).resolve().parent.parent
HERE = ROOT / "layout"
*names, out = sys.argv[1:]
out = pathlib.Path(out); out.mkdir(parents=True, exist_ok=True)
for n in names:
    svg = (HERE / "fig" / f"{n}.svg").read_text()
    (HERE / f"_prev_{n}.html").write_text(f'<!doctype html><html><head><meta charset="utf-8"><link rel="stylesheet" href="book.css">'
        f'<style>body{{margin:0;background:#fff;filter:grayscale(1)}} .w{{width:4.6in}} .w svg{{width:100%;height:auto;display:block}}</style></head>'
        f'<body><div class="w">{svg}</div></body></html>')
shots = "".join(f"await p.goto('file://{HERE}/_prev_{n}.html'); await p.evaluate(() => document.fonts.ready); await p.locator('.w').screenshot({{ path: '{out}/{n}.png' }});" for n in names)
js = f"""const {{ chromium }} = require('playwright');
(async () => {{ const b = await chromium.launch({{ executablePath: '/opt/pw-browsers/chromium' }});
const p = await b.newPage({{ deviceScaleFactor: 1.5625 }}); {shots} await b.close(); }})();"""
subprocess.run(["node", "-e", js], check=True, cwd=HERE)
for n in names:
    (HERE / f"_prev_{n}.html").unlink(missing_ok=True)
    print(out / f"{n}.png")
