"""Build sign figures from the official FHWA Standard Highway Signs artwork (public domain).

Source files: layout/signs_fhwa/CODE.svg, taken from the FHWA 2024 Standard Highway Signs release as
repackaged (CC0) at github.com/whizy76/mutcd-svg. Output: layout/fig_official/NAME.svg, which the
build uses in place of layout/fig/NAME.svg when it exists (color edition).

Three quiz pictures (center lane, exit only, lane closed) keep the old drawing because the question text
describes that drawing. A few items have no file in that set (Interstate shield, brown recreation symbols, pink incident sign,
striped object marker, JCT and direction plates, left exit tab). Those keep the drawing from the old figure.

Usage: python3 tools/make_official_figs.py            # writes every figure in SPEC and SQ
"""
import re, json, pathlib, subprocess, sys
ROOT = pathlib.Path(__file__).resolve().parent.parent
LIB, OLD, OUT = ROOT / "layout" / "signs_fhwa", ROOT / "layout" / "fig", ROOT / "layout" / "fig_official"
W = 460
ART_H = {3: 108, 4: 88, 5: 70}          # art box height by number of columns
LBL = re.compile(r'<text class="\w*(?:lbl|sub)"[^>]*>.*?</text>', re.S)

# figure -> (columns, [(art pieces stacked top to bottom, label, [sub labels])])
# a piece is "CODE", "CODE@relative width", "CODE~" (mirrored) or "old:N" (the Nth drawing of the old figure, "old:N[x,y,w,h]" to give its visible box)
SPEC = {
 "signs_shapes": (5, [
   (["R01-01"], "Octagon", ["Stop", "Red"]), (["R01-02"], "Triangle", ["Yield", "Red and white"]),
   (["W10-01"], "Circle", ["Railroad ahead", "Yellow"]), (["W14-03"], "Pennant", ["No passing zone", "Yellow"]),
   (["S01-01"], "Pentagon", ["School", "Yellow-green"]), (["R15-01"], "Crossbuck", ["Railroad crossing", "White"]),
   (["W01-02"], "Diamond", ["Warning", "Yellow"]), (["R02-01"], "Vertical rectangle", ["Regulatory", "White"]),
   (["D01-01"], "Horizontal rectangle", ["Mostly guide", "Green"])]),
 "signs_colors": (5, [
   (["R01-01"], "Red", ["Stop, yield,", "not allowed"]), (["R02-01"], "White", ["Rules", "(regulatory)"]),
   (["W01-02"], "Yellow", ["General", "warning"]), (["S01-01"], "Yellow-green", ["Fluorescent: school,", "walkers, bikes"]),
   (["W20-01"], "Orange", ["Work zone"]), (["D01-01"], "Green", ["Direction, guide"]),
   (["D09-02"], "Blue", ["Motorist", "services"]), (["old:8"], "Brown", ["Recreation,", "parks"]),
   (["old:9"], "Fluorescent pink", ["Incident ahead"]), (["R06-01"], "Black", ["One Way signs"])]),
 "signs_regulatory_core": (3, [
   (["R01-01"], "Stop", ["Red octagon"]), (["R01-02"], "Yield", ["Red and white triangle, point down"]),
   (["R02-01"], "Speed Limit", ["White rectangle, black letters"]), (["R05-01"], "Do Not Enter", ["Red circle, white bar"]),
   (["R05-01A"], "Wrong Way", ["Red rectangle, white letters"]), (["R06-01"], "One Way", ["Black rectangle, white arrow"])]),
 "signs_regulatory_more": (3, [
   (["R03-02"], "No Left Turn", ["Red circle and slash"]), (["R03-04"], "No U-Turn", ["Red circle and slash"]),
   (["R04-07"], "Keep Right", ["White rectangle, pass right"]), (["R03-05"], "Right Turn Only", ["White rectangle, black arrow"]),
   (["R04-01"], "Do Not Pass", ["White rectangle, right side"]), (["W14-03"], "No Passing Zone", ["Yellow pennant, left side"])]),
 "signs_regulatory_extra": (3, [
   (["R08-03"], "No Parking", ["Red circle and slash"]), (["R03-01"], "No Right Turn", ["Red circle and slash"]),
   (["R10-11"], "No Turn on Red", ["White rectangle"]), (["R04-03"], "Slower Traffic Keep Right", ["White rectangle"]),
   (["R01-01", "R01-03P@0.62"], "All Way Stop", ["Red ALL WAY plaque"]),
   (["R07-08"], "Accessible Parking", ["White rectangle, symbol on blue,", "green letters"])]),
 "signs_regulatory_lanes": (3, [
   (["R06-03"], "Divided Highway Crossing", ["White rectangle", "Two roadways to cross"]),
   (["old:2"], "EXIT ONLY Lane", ["Yellow panel, green sign", "This lane must exit"]),
   (["R10-12"], "Left Turn Yield on Green", ["White rectangle", "Green ball: yield"]),
   (["R01-01", "R01-10P@0.8"], "Except Right Turn", ["Red octagon, white plaque", "Right turn need not stop"]),
   (["R01-02", "R01-02AP@0.86"], "To Oncoming Traffic", ["Red triangle, white plaque", "Yield to oncoming"]),
   (["R03-09B"], "Center Lane Left Only", ["White rectangle", "Left turns, both ways"])]),
 "signs_warning": (4, [
   (["W01-02", "W13-01P@0.46"], "Curve, 35 MPH", ["Plaque is advice"]), (["W01-08"], "Chevron", ["Outside of a curve"]),
   (["W04-01"], "Merge", ["Traffic joins you"]), (["W04-02"], "Lane Ends", ["Road loses a lane"]),
   (["W06-01"], "Divided Highway", ["Median begins"]), (["W06-02"], "Divided Hwy. Ends", ["Median ends"]),
   (["W06-03"], "Two Way Traffic", ["Oncoming ahead"]), (["W08-05"], "Slippery When Wet", ["Car, wavy skid marks"]),
   (["W02-01"], "Crossroad", ["Plus sign"]), (["W02-04"], "T Intersection", ["Your road ends"]),
   (["W03-01"], "Stop Ahead", ["Red octagon symbol"]), (["W03-03"], "Signal Ahead", ["Traffic light symbol"])]),
 "signs_warning_more": (5, [
   (["W11-02"], "Pedestrians", ["Yellow-green", "or yellow"]), (["W11-01"], "Bicycles", ["Yellow or", "yellow-green"]),
   (["W11-03"], "Deer Crossing", ["Yellow diamond", "Deer may cross"]), (["W01-05"], "Winding Road", ["Yellow diamond", "Series of curves"]),
   (["W01-01"], "Sharp Turn", ["Yellow diamond", "Slow way down"]), (["W07-01"], "Steep Hill", ["Yellow diamond", "Steep downgrade"]),
   (["W04-03"], "Added Lane", ["Yellow diamond", "No merge needed"]), (["W12-02"], "Low Clearance", ["Yellow diamond", "12 ft 6 in clearance"]),
   (["W03-02"], "Yield Ahead", ["Red and white", "triangle symbol"]), (["W13-02"], "Exit Speed", ["Yellow rectangle", "Advice for the ramp"])]),
 "signs_warning_extra": (4, [
   (["W01-06~"], "Large Arrow", ["Yellow rectangle", "Road turns sharply"]), (["W01-07"], "Double Arrow", ["Yellow rectangle", "Turn left or right"]),
   (["W01-04"], "Reverse Curve", ["Yellow diamond", "One way, then the other"]), (["W01-03"], "Reverse Turn", ["Yellow diamond", "Two sharp turns"]),
   (["W02-02"], "Side Road", ["Yellow diamond", "Road joins from side"]), (["W02-05"], "Y Intersection", ["Yellow diamond", "Road splits in two"]),
   (["W02-06"], "Circular Intersection", ["Yellow diamond", "Roundabout ahead"]), (["W01-13"], "Truck Rollover", ["Yellow diamond", "Trucks: slow for curve"])]),
 "signs_warning_road": (4, [
   (["W05-01"], "Road Narrows", ["Yellow diamond", "Road gets narrower"]), (["W05-02"], "Narrow Bridge", ["Yellow diamond", "Bridge narrower"]),
   (["W05-03"], "One Lane Bridge", ["Yellow diamond", "Take turns crossing"]), (["W08-09"], "Low Shoulder", ["Yellow diamond", "Shoulder sits lower"]),
   (["W08-17", "W08-17P@0.8"], "Shoulder Drop-Off", ["Yellow diamond", "and yellow plaque"]), (["W11-14"], "Horse-Drawn Vehicle", ["Yellow diamond", "Slow buggies ahead"]),
   (["W14-01"], "Dead End", ["Yellow diamond", "No way through"]), (["W14-02"], "No Outlet", ["Yellow diamond", "Area has no exit"])]),
 "signs_school": (4, [
   (["S01-01"], "School Zone", ["Yellow-green"]), (["S01-01", "W16-07P@0.7"], "School Crossing", ["Down arrow plaque"]),
   (["S05-01"], "School Speed Limit", ["White, with plaques"]), (["S05-02"], "End School Zone", ["White rectangle"])]),
 "signs_work_zone_more": (3, [
   (["W20-07"], "Flagger Ahead", ["Orange diamond", "Be ready to stop"]), (["W21-01"], "Workers", ["Orange diamond", "People in the road"]),
   (["W20-05"], "Lane Closed Ahead", ["Orange diamond", "Merge early"]), (["W20-02"], "Detour Ahead", ["Orange diamond", "Route changes ahead"]),
   (["M04-09"], "Detour", ["Orange rectangle", "Follow the arrow"]), (["G20-02"], "End Road Work", ["Orange rectangle", "Work zone ends"])]),
 "signs_guide": (5, [
   (["old:1"], "Interstate", ["Red and blue shield"]), (["M01-04"], "U.S. Route", ["White shield,", "black number"]),
   (["M01-05"], "State Route", ["Design varies", "by state"]), (["D10-01"], "Mile Marker", ["Green, on the", "shoulder"]),
   (["old:5"], "Exit Sign", ["Green, exit number", "on the top tab"]),
   (["D09-02"], "Hospital", ["Blue service sign"]), (["D09-07"], "Gas", ["Blue service sign"]), (["D09-08"], "Food", ["Blue service sign"]),
   (["D09-09"], "Lodging", ["Blue service sign"]), (["old:7"], "Recreation", ["Brown: camping,", "picnic area"])]),
 "signs_markers_plates": (4, [
   (["old:1[50,14,24,68]"], "Object Marker", ["Yellow and black stripes;", "pass on the low side"]), (["OM04-01"], "End of Road", ["Red diamond:", "stop or turn"]),
   (["R05-06"], "No Bicycles", ["Red circle and slash"]), (["R09-03"], "No Pedestrians", ["Red circle and slash"]),
   (["W01-10"], "Road Entering Curve", ["Yellow diamond"]), (["old:6"], "Junction Plate", ["White JCT plate", "over a route marker"]),
   (["old:7"], "Direction Plates", ["White WEST and", "arrow plates"]), (["old:8"], "Left Exit", ["Green, exit tab on the", "left with yellow LEFT"])]),
}

# single signs shown inside quiz and mock questions
SQ = {"circular_intersection": ["W02-06"], "crossbuck": ["R15-01"], "dead_end": ["W14-01"],
 "detour_ahead": ["W20-02"], "detour_arrow": ["M04-09"], "divided_highway_crossing": ["R06-03"], "divided_highway_ends": ["W06-02"],
 "do_not_enter": ["R05-01"], "end_of_road": ["OM04-01"], "end_road_work": ["G20-02"], "flagger_ahead": ["W20-07"],
 "horse_drawn": ["W11-14"], "lane_ends": ["W04-02"], "large_arrow": ["W01-06~"],
 "left_turn_yield_green": ["R10-12"], "low_shoulder": ["W08-09"], "merge": ["W04-01"], "narrow_bridge": ["W05-02"], "no_bicycles": ["R05-06"],
 "no_outlet": ["W14-02"], "no_passing_zone": ["W14-03"], "no_u_turn": ["R03-04"], "one_lane_bridge": ["W05-03"], "one_way": ["R06-01"],
 "reverse_curve": ["W01-04"], "reverse_turn": ["W01-03"], "road_narrows": ["W05-01"], "road_work_ahead": ["W20-01"], "rr_advance": ["W10-01"],
 "school": ["S01-01"], "shoulder_drop_off": ["W08-17", "W08-17P@0.8"], "side_road": ["W02-02"], "signal_ahead": ["W03-03"], "slippery": ["W08-05"],
 "stop": ["R01-01"], "stop_except_right": ["R01-01", "R01-10P@0.8"], "truck_rollover": ["W01-13"], "two_direction_arrow": ["W01-07"],
 "two_way_traffic": ["W06-03"], "workers": ["W21-01"], "wrong_way": ["R05-01A"], "y_intersection": ["W02-05"], "yield": ["R01-02"],
 "yield_to_oncoming": ["R01-02", "R01-02AP@0.86"]}

_n = [0]
def lib_piece(code):
    """Return (inner svg markup with unique class and id names, viewBox w, h)."""
    t = (LIB / f"{code}.svg").read_text()
    t = re.sub(r"<\?xml.*?\?>|<!--.*?-->|<!DOCTYPE.*?>", "", t, flags=re.S)
    vb = [float(v) for v in re.search(r'viewBox="([^"]+)"', t).group(1).replace(",", " ").split()]
    inner = t[t.find(">", t.find("<svg")) + 1:t.rfind("</svg>")]
    _n[0] += 1; p = f"f{_n[0]}"
    inner = re.sub(r'class="([^"]+)"', lambda m: 'class="' + " ".join(f"{p}{c}" for c in m.group(1).split()) + '"', inner)
    inner = re.sub(r"(<style[^>]*>)(.*?)(</style>)", lambda m: m.group(1) + re.sub(r"\.([A-Za-z_][\w-]*)", lambda n: f".{p}{n.group(1)}", m.group(2)) + m.group(3), inner, flags=re.S)
    for i in set(re.findall(r'\bid="([^"]+)"', inner)):
        inner = inner.replace(f'id="{i}"', f'id="{p}{i}"').replace(f"url(#{i})", f"url(#{p}{i})").replace(f'href="#{i}"', f'href="#{p}{i}"')
    return inner, vb

_old = {}
def old_chunks(fig):
    """Drawings of the old hand-made figure, one per comment, with the bounding box of each (measured in Chromium)."""
    if fig in _old:
        return _old[fig]
    t = (OLD / f"{fig}.svg").read_text()
    head = re.search(r"<svg[^>]*>", t).group(0)
    extra = "".join(re.findall(r"<style>.*?</style>|<defs>.*?</defs>", t, flags=re.S))
    body = re.sub(r"<style>.*?</style>|<defs>.*?</defs>", "", t[t.find(">", t.find("<svg")) + 1:t.rfind("</svg>")], flags=re.S)
    parts = re.split(r"<!--.*?-->", body, flags=re.S)
    arts = [LBL.sub("", p).strip() for p in parts[1:]]
    html = ROOT / "layout" / f"_old_{fig}.html"
    html.write_text('<html><body style="margin:0">' + head + extra + "".join(f'<g id="c{i}">{a}</g>' for i, a in enumerate(arts)) + "</svg></body></html>")
    js = ("const { chromium } = require('playwright'); (async () => { const b = await chromium.launch({ executablePath: '/opt/pw-browsers/chromium' });"
          f" const p = await b.newPage(); await p.goto('file://{html}');"
          " const r = await p.evaluate(() => [...document.querySelectorAll('svg > g[id^=c]')].map(g => { const r = g.getBBox(); return [r.x, r.y, r.width, r.height]; }));"
          " console.log(JSON.stringify(r)); await b.close(); })();")
    boxes = json.loads(subprocess.run(["node", "-e", js], cwd=ROOT / "layout", capture_output=True, text=True, check=True).stdout)
    html.unlink()
    _old[fig] = (arts, boxes, "".join(re.findall(r"<defs>.*?</defs>", t, flags=re.S)))
    return _old[fig]

def piece(fig, spec):
    code, _, wt = spec.partition("@")
    wt = float(wt) if wt else 1.0
    if code.endswith("~"):             # mirrored left to right (arrows only, never a sign with words)
        inner, vb = lib_piece(code[:-1])
        return f'<g transform="translate({2 * vb[0] + vb[2]:.2f},0) scale(-1,1)">{inner}</g>', vb, wt
    if code.startswith("old:"):
        arts, boxes, _defs = old_chunks(fig)
        num, _, box = code[4:].partition("[")
        i = int(num)                   # drawing 0 is the empty space after the figure title comment
        x, y, w, h = [float(v) for v in box.rstrip("]").split(",")] if box else boxes[i]   # [x,y,w,h]: visible box when the drawing is clipped
        return arts[i], [x - 1, y - 1, w + 2, h + 2], wt
    inner, vb = lib_piece(code)
    return inner, vb, wt

def stack(fig, pieces, cx, top, box_w, box_h, gap=4, valign="center"):
    """Place pieces top to bottom, centered on cx, as large as fits in box_w x box_h."""
    ps = [piece(fig, s) for s in pieces]
    # width of piece i = base * weight; height follows its aspect
    tall = sum(wt * vb[3] / vb[2] for _, vb, wt in ps)
    base = min(box_w / max(wt for *_, wt in ps), (box_h - gap * (len(ps) - 1)) / tall)
    tot = base * tall + gap * (len(ps) - 1)
    y = top + ((box_h - tot) / 2 if valign == "center" else 0)
    out = []
    for inner, vb, wt in ps:
        w = base * wt; h = w * vb[3] / vb[2]
        out.append(f'<svg x="{cx - w / 2:.2f}" y="{y:.2f}" width="{w:.2f}" height="{h:.2f}" viewBox="{vb[0]:.2f} {vb[1]:.2f} {vb[2]:.2f} {vb[3]:.2f}">{inner}</svg>')
        y += h + gap
    return "".join(out), base, tot

def figure(name, cols, items):
    cw = W / cols; ah = ART_H[cols]
    rows = [items[i:i + cols] for i in range(0, len(items), cols)]
    y, out = 6, []
    for row in rows:
        subs = max(len(s) for _, _, s in row)
        cw = W / len(row) if len(row) < cols else W / cols      # a short last row spreads out
        x0 = 0
        for k, (pieces, label, sub) in enumerate(row):
            cx = x0 + cw * (k + 0.5)
            art, _, _ = stack(name, pieces, cx, y, cw - 16, ah)
            out.append(art)
            out.append(f'<text class="lbl" x="{cx:.1f}" y="{y + ah + 15}">{label}</text>')
            for j, s in enumerate(sub):
                out.append(f'<text class="sub" x="{cx:.1f}" y="{y + ah + 27 + 11.5 * j:.1f}">{s}</text>')
        y += ah + 15 + 11.5 * subs + 16
    H = y - 8
    return (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H:.0f}" font-family="Inter, Arial, sans-serif">\n'
            f'<!-- Built by tools/make_official_figs.py from FHWA Standard Highway Signs artwork (public domain) -->\n'
            '<style>.lbl { font-size: 10.5px; font-weight: 700; fill: #1c1c1c; text-anchor: middle; } .sub { font-size: 8.6px; font-weight: 500; fill: #555; text-anchor: middle; }</style>\n'
            + (_old[name][2] if name in _old else "") + "\n".join(out) + "\n</svg>\n")

def single(name, pieces):
    ps = [piece(name, s) for s in pieces]
    maxw = 100
    art, base, tot = stack(name, pieces, maxw / 2, 0, maxw, 10 ** 6, valign="top")
    return f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {maxw} {tot:.1f}">\n<!-- FHWA Standard Highway Signs artwork (public domain) -->\n{art}\n</svg>\n'

if __name__ == "__main__":
    OUT.mkdir(exist_ok=True)
    used = set()
    for name, (cols, items) in SPEC.items():
        (OUT / f"{name}.svg").write_text(figure(name, cols, items))
        used |= {p.partition("@")[0].rstrip("~") for it in items for p in it[0] if not p.startswith("old:")}
    for name, pieces in SQ.items():
        (OUT / f"sq_{name}.svg").write_text(single(name, pieces))
        used |= {p.partition("@")[0].rstrip("~") for p in pieces}
    print(len(SPEC), "figures,", len(SQ), "single signs,", len(used), "FHWA files used")
    extra = sorted(p.stem for p in LIB.glob("*.svg") if p.stem not in used)
    if extra:
        print("unused files in signs_fhwa:", " ".join(extra))
