"""Markdown chunk -> styled HTML for the Permit Path print interior."""
import re, subprocess, pathlib, html, json

HERE = pathlib.Path(__file__).parent
CFG = json.loads((HERE / "config.json").read_text())
LABELS = {"on the test": "tests", "test trap": "trap", "road tip": "tip", "remember it": "memory"}


def md_to_html(md):
    out = subprocess.run(["pandoc", "-f", "markdown", "-t", "html5", "--wrap=none"], input=md,
                         capture_output=True, text=True, check=True).stdout

    def callout(m):
        inner = m.group(1)
        lm = re.match(r'\s*<p><strong>([^<]+?):?</strong>:?\s*', inner)
        if not lm:
            return m.group(0)
        label = lm.group(1).strip().rstrip(":")
        name = label.lower()
        cls = LABELS.get(name, "state" if name.endswith(" rule") else "tip")
        inner = inner[lm.end():]
        inner = inner.strip()[4:] if inner.strip().startswith("</p>") else "<p>" + inner
        return f'<div class="callout {cls}"><span class="label">{html.escape(label)}</span>{inner}</div>'

    out = re.sub(r"<blockquote>(.*?)</blockquote>", callout, out, flags=re.S)

    def fig(m):
        return f'<div class="fig">{(HERE / "fig" / m.group(1)).read_text()}</div>'
    out = re.sub(r'<p>\s*<img src="fig/([a-z0-9_]+\.svg)"[^>]*>\s*</p>', fig, out)

    hm = re.search(r'<h1 id="[^"]*">\s*Chapter\s+(\d+):', out)
    book_n = hm.group(1) if hm else "?"

    def card(m):
        link = re.search(r"/(ch)/(\d+)", m.group(1))
        k = link.group(2) if link else book_n
        return (f'<div class="practice-card"><div class="pc-band">Practice online<span>Chapter {book_n}</span></div>'
                f'<div class="pc-main"><div class="pc-qr"><img src="qr/ch{k}.svg"><span>Scan</span></div>'
                f'<div class="pc-text"><div class="pc-head">Keep practicing Chapter {book_n}</div>'
                f'<ul class="pc-list"><li>New questions with instant explanations</li><li>Full-color road sign flashcards</li><li>Your weak spots, tracked</li></ul>'
                f'<div class="pc-url"><span class="url">{CFG["app_short"]}/ch/{k}</span></div></div></div></div>')
    out = re.sub(r'<p><strong>Practice this chapter online:</strong>(.*?)</p>', card, out, flags=re.S)

    m = re.search(r'<h1 id="[^"]*">\s*Chapter\s+(\d+):\s*(.*?)</h1>', out, flags=re.S)
    if not m:
        return f'<section class="part">{out}</section>'
    num, title = m.group(1), " ".join(m.group(2).split())
    head = f'<div class="chapter-head"><div class="num">Chapter {int(num)}</div><h1>{title}</h1></div>'
    out = out[:m.start()] + head + out[m.end():]
    css = (f'@page ch{num}:right {{ @top-right {{ content: "{title}"; }} }}'
           f'@page ch{num}:first {{ @top-left {{ content: none; }} @top-right {{ content: none; }} }}')
    return f'<style>{css}</style><section class="chapter" style="page: ch{num}">{out}</section>'
