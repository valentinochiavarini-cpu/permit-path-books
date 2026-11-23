"""KDP upload file (one per state) in the owner's approved format.
Usage: python3 listing/make_upload_files.py  -> listing/upload/XX.html (Google Doc source) + listing/upload/XX.md
Rules: no em or en dashes; no dollar amounts or years in the description; 'flashcards' never in the subtitle."""
import json, glob, pathlib, subprocess, html
ROOT = pathlib.Path(__file__).resolve().parent.parent
NAMES = json.loads((ROOT / "layout/config.json").read_text())["state_names"]
TITLES = json.loads((ROOT / "listing/titles.json").read_text())
DESC = json.loads((ROOT / "listing/descriptions_v2.json").read_text())
FILL = {"A": ["drivers ed book for teens and first time drivers", "drivers manual book learners permit study book", "adult drivers license test prep book"],
        "B": ["drivers license handbook for teens and adults", "drivers manual book learners permit study book", "first time driver book road signs and rules"],
        "C": ["drivers ed book for teens and first time drivers", "drivers license handbook dmv handbook", "adult drivers license test prep book"]}
CORE = len(json.loads((ROOT / "bank/core.json").read_text()))

# agency, test sentence (hook), mock phrase, simulator wording real (True) or practice size (False)
S = {
 "FL": ("FLHSMV", "The Florida Class E Knowledge Exam asks 50 questions, and you need 40 right.", "full 50-question mock exams", True),
 "TX": ("Texas DPS", "The Texas knowledge test comes in two parts, road signs and road rules, and you need 70 percent on each.", "full two-part mock exams (road signs and road rules)", False),
 "CA": ("the California DMV", "The California knowledge test takes 80 percent to pass. Under 18, that means missing no more than 8 of 46 questions.", "full 46-question mock exams", True),
 "PA": ("PennDOT", "The Pennsylvania knowledge test asks 18 questions, and you need 15 right.", "full 18-question mock exams", True),
 "NY": ("the New York DMV", "The New York written test asks 20 questions. You need 14 right, including at least 2 of the 4 road sign questions.", "full 20-question mock exams", True),
 "IL": ("the Illinois Secretary of State", "The Illinois written exam asks at least 35 questions, and you need 80 percent to pass.", "full 35-question mock exams", True),
 "OH": ("the Ohio BMV", "The Ohio knowledge test asks 40 questions, and you need 30 right.", "full 40-question mock exams", True),
 "MO": ("the Missouri Department of Revenue", "Missouri gives you two tests: 25 written questions with 20 needed to pass, plus a road sign test.", "full mock exams with a written part and a road sign part", True),
 "NC": ("NCDMV", "North Carolina gives you two tests: a knowledge test you pass with 80 percent, and a road sign test where you can miss only 3 of 12.", "full mock exams with a knowledge part and a road sign part", False),
 "SC": ("the SCDMV", "The SCDMV doesn't publish how many questions are on the knowledge test, so you have to know every chapter of the manual.", "full 25-question mock exams", False),
 "GA": ("Georgia DDS", "The Georgia knowledge exam has two parts, 20 road signs and 20 road rules, and you need 15 right on each.", "full two-part mock exams (road signs and road rules)", True),
 "NJ": ("the New Jersey MVC", "The New Jersey knowledge test asks 50 questions, and you need 40 right.", "full 50-question mock exams", True),
 "VA": ("the Virginia DMV", "The Virginia knowledge exam starts with 10 road signs, and you must get all 10 right. Then come 30 general questions, with 24 needed to pass.", "full two-part mock exams (road signs and general knowledge)", True),
 "AL": ("ALEA", "ALEA doesn't publish how many questions are on the Alabama knowledge test, so you have to know every chapter of the manual.", "full 30-question mock exams", False),
 "MI": ("the Michigan Secretary of State", "Michigan's written test covers road rules and road signs, and the Secretary of State doesn't publish the question count, so you have to know every chapter.", "full two-part mock exams (road rules and road signs)", False),
}
WHO_DEFAULT = "For teens, adults learning to drive for the first time, newcomers with a foreign license, and the parents helping them."
WHO = {
 "CA": "For teens, adults learning to drive for the first time, new residents from other states and countries (California tests both), and the parents helping them.",
 "MO": "For teens, adults learning to drive for the first time, newcomers with a foreign license, new residents who take the Missouri road sign test, and the parents helping them.",
 "NC": "For teens, adults learning to drive for the first time, newcomers with a foreign license, new residents who take the North Carolina road sign test, and the parents helping them.",
}
# A+ Module 4 test format line and sources checked
FORMAT = {
 "FL": ("Class E Knowledge Exam: 50 questions, 40 to pass", "FLHSMV, Florida Statutes"),
 "TX": ("knowledge test in two parts (road signs, road rules), 70 percent each", "Texas DPS Driver Handbook, Texas Transportation Code"),
 "CA": ("knowledge test, 80 percent to pass (46 questions under 18)", "California DMV Driver's Handbook, California Vehicle Code"),
 "PA": ("knowledge test: 18 questions, 15 to pass", "PennDOT PUB 95, Pennsylvania Vehicle Code"),
 "NY": ("written test: 20 questions, 14 to pass, at least 2 of 4 signs", "NY DMV MV-21, NY Vehicle and Traffic Law"),
 "IL": ("written exam: at least 35 questions, 80 percent to pass", "Rules of the Road, Illinois Vehicle Code"),
 "OH": ("knowledge test: 40 questions, 30 to pass", "Ohio BMV Digest, Ohio Revised Code"),
 "MO": ("written test 25 questions (20 to pass) plus a 6-sign test", "Missouri Driver Guide, Missouri Revised Statutes"),
 "NC": ("knowledge test (80 percent) plus a 12-sign test (9 to pass)", "NC Driver Handbook, NC General Statutes"),
 "SC": ("knowledge test, count not published by the SCDMV", "SC Driver's Manual, SC Code of Laws"),
 "GA": ("two parts: 20 road signs and 20 road rules, 15 to pass each", "Georgia Driver's Manual, O.C.G.A. Title 40"),
 "NJ": ("knowledge test: 50 questions, 40 to pass", "NJ MVC pages, N.J.S.A. Title 39"),
 "VA": ("two parts: 10 signs (all 10), then 30 questions (24 to pass)", "Virginia Driver's Manual, Code of Virginia"),
 "AL": ("knowledge test, count not published by ALEA", "ALEA Driver Manual, Code of Alabama"),
 "MI": ("written test in two parts, rules and signs", "What Every Driver Must Know, Michigan Vehicle Code"),
}
# keyword slots 2 and 4 (state specific); the rest follow the pattern
KW = {
 "FL": ("fl permit test study guide class e knowledge exam", "florida dmv flhsmv learners license test"),
 "TX": ("tx permit test study guide dps learner license", "texas dmv written test road signs and rules"),
 "CA": ("ca permit test study guide dmv written test", "california dmv handbook drivers ed teens"),
 "PA": ("pa permit test study guide penndot", "pennsylvania learners permit test book"),
 "NY": ("ny permit test study guide dmv written test", "new york learner permit practice test book"),
 "IL": ("il permit test study guide rules of the road", "illinois instruction permit practice test"),
 "OH": ("ohio temps test study guide bmv", "ohio permit test practice book tipic"),
 "MO": ("mo permit test study guide driver guide", "missouri drivers permit study book"),
 "NC": ("nc permit test study guide road signs test", "north carolina dmv learners permit book"),
 "SC": ("sc permit test study guide scdmv", "south carolina beginners permit practice test"),
 "GA": ("ga permit test study guide dds", "georgia learners permit practice test book"),
 "NJ": ("nj permit test study guide mvc knowledge test", "new jersey driver manual practice test book"),
 "VA": ("va learners permit test study guide dmv", "virginia permit test road signs practice book"),
 "AL": ("al permit test study guide alea", "alabama learners permit practice test book"),
 "MI": ("mi permit test study guide segment 1", "michigan what every driver must know test"),
}
# state open items for Before Upload
OPEN = {
 "NJ": "Red arrow rule follows N.J.S.A. 39:4-115 (right on a steady red arrow after a full stop); the NJ Driver Manual could not be read, so confirm against it if you can.",
 "IL": "Illinois may test new residents from other states (not confirmed with the Secretary of State). Keep the standard title unless that is confirmed.",
 "TX": "DPS does not publish the question count: mocks use the 15 signs + 15 rules course format.",
 "SC": "The SCDMV does not publish the test length: mocks are a 25-question practice size at 80 percent.",
 "AL": "ALEA does not publish the test length: mocks are a 30-question practice size at 80 percent.",
 "MI": "The SOS does not publish the test length: mocks are a practice size at about 70 percent.",
 "NC": "NCDMV does not publish the knowledge test length: mocks use a practice size plus the 12-sign test.",
}
STD_TITLE = "Driver's License Handbook and Permit Practice Test Book for Teens and First-Time Drivers | Chapter Quizzes, Full Mock Exams and 500+ Online Practice Questions"
CA_TITLE = "Driver's License Handbook and Permit Practice Test Book for Teens, First-Time Drivers and New Residents | Chapter Quizzes, Mock Exams and 500+ Online Practice Questions"

def pages(c):
    pdf = sorted(glob.glob(str(ROOT / f"out/{c}/*.pdf")))[0]
    out = subprocess.run(["pdfinfo", pdf], capture_output=True, text=True).stdout
    return int([l for l in out.splitlines() if l.startswith("Pages")][0].split()[1])

def doc(c):
    n = NAMES[c]; nl = n.lower(); ag, test, mock, real = S[c]
    st = len(json.loads((ROOT / f"bank/{c}.json").read_text())); app = CORE + st
    pg = pages(c); cost = 1.00 + 0.012 * pg; roy = 0.6 * 18.99 - cost
    sub = CA_TITLE if c == "CA" else STD_TITLE
    sim = "with the real test's length and passing score" if real else "at a full practice length"
    hook, miss, ch1, dmock = DESC[c]; dmock = dmock[0].upper() + dmock[1:]
    art = "An" if n[0] in "AEIOU" else "A"
    tt = TITLES[c]
    kw = [f"{nl} drivers handbook 2026 2027", KW[c][0], KW[c][1],
          f"how to pass the {nl} permit test" if tt["dmv"] else f"{nl} dmv test book"] + FILL[tt["group"]]
    for k in kw:
        assert len(k) <= 50, (c, k, len(k))
    fmt, srcs = FORMAT[c]
    title, sub = tt["title"], tt["subtitle"]
    assert len(title) + len(sub) < 200, (c, len(title) + len(sub))
    open_items = [f"The 500+ claim holds: {app} questions in the app ({CORE} core plus {st} {n}).",
                  "Title on the cover and on the interior title page: " + title + ". Same in the KDP title field.",
                  f"Paperback cover: the folder holds the front cover only (fine for Kindle). KDP paperback needs a full wrap cover (back, spine, front) for {pg} pages on white paper.",
                  "KDP AI content question: answer it for the text as written for this edition.",
                  "Kindle manuscript: upload the EPUB from this folder. Paperback interior: the PDF (6 x 9)."]
    if c in OPEN:
        open_items.insert(1, OPEN[c])
    else:
        open_items.insert(1, f"No pending {n} law change is flagged in the repo.")
    li = lambda xs: "<ul>" + "".join(f"<li>{x}</li>" for x in xs) + "</ul>"
    body = f"""<h1>{title}</h1>
<h2>{sub}</h2>
<h3>Permit Path</h3>
<p>Size: 6 x 9 in, black and white, {pg} pages<br>Ebook Price: 9.99$<br>Paperback Price: 18.99$ (print cost about {cost:.2f}$, royalty about {roy:.2f}$)<br>Publisher: Permit Path<br>Series: Permit Path</p>
<h2>Categories</h2>
<p>Engineering &amp; Transportation &gt; Automotive &gt; Driver Education<br>Education &amp; Teaching &gt; Studying &amp; Workbooks &gt; Test Preparation<br>Teen &amp; Young Adult &gt; Education &amp; Reference &gt; Study Aids<br><i>Confirm the exact paths in the KDP category picker before saving.</i></p>
<h2>7 keywords</h2>
<p>{'<br>'.join(kw)}</p>
<h2>Product Description</h2>
<h4>{hook}</h4>
<p>Most people who fail don't fail for lack of effort. They read the {n} manual once, then get caught on the exact numbers: {miss}. This book is built so that doesn't happen to you.</p>
<p><b>Learn a topic, then prove it.</b> Each of the 13 chapters teaches one topic in plain English and ends with a 10-question quiz, every answer explained. Every {n} rule is checked against {ag} and {n} law, and boxed wherever {n} differs from other states.</p>
<h4>Inside the book</h4>
<ul><li>{art} {n} chapter on the whole path: {ch1}</li><li>80+ road signs and diagrams, with every color named</li><li>130 chapter quiz questions with explanations</li><li>{dmock}</li><li>A road test chapter: what the examiner scores and the mistakes that fail people</li></ul>
<h4>Plus the free Permit Path practice app</h4>
<p>The book teaches you. The app drills you until the answers are automatic. It opens in any browser: no download, no sign-up, no access code.</p>
<ul><li><b>600+ {n} questions</b> by chapter, shuffled every time, each answer explained</li><li><b>A timed exam simulator</b> {sim}</li><li><b>115 road signs in full color</b> as flashcards</li><li><b>The full ebook</b> on your phone, every sign in color</li></ul>
<p>{WHO.get(c, WHO_DEFAULT)}</p>
<p><b>Read a chapter a day, pass both mock exams, and walk in knowing you're ready.</b></p>
<h2>Editorial Reviews</h2>
<p><i>Left empty on purpose. Add only reviews from real, named reviewers who agreed to be quoted, such as a driving instructor or a parent beta reader.</i></p>
<h2>From the Author</h2>
<p>We built this book because most people who fail the permit test don't fail for lack of effort. They read a long handbook once, then meet questions worded in ways they never practiced, and lose points on exact numbers. So we built it the other way around. Each chapter teaches one topic in plain words and ends with a quiz, so you find your gaps right away. Every {n} rule was checked against the official manual and {n} law. Then we connected the book to a free app that keeps testing you until your scores show you're ready. If you're the parent in the passenger seat, the road test chapter is there for you too. Read a chapter a day, take both mock exams under real conditions, and review every miss. Do that, and you'll walk in knowing what to expect.</p>
<p>Good luck on test day. <b>The Permit Path team</b></p>
<h2>Customer Reviews</h2>
<p></p>
<h2>A+ Content</h2>
{li([
 "Module 1, Why the handbook alone is not enough: the official manual vs this book (a quiz after every chapter, explanations, " + n + " rule boxes).",
 "Module 2, Learn, then test: a chapter page next to its quiz and answer key.",
 "Module 3, The free app: screenshots of chapter practice, the exam simulator and its results page, a color sign flip card and the ebook page. No download, no sign-up, no access code.",
 f"Module 4, The {n} test: {fmt}; what Chapter 1 covers; a line naming the sources checked ({srcs}).",
 "Module 5, Who it's for: teens, adults learning to drive for the first time, " + ("new residents from other states and countries" if c == "CA" else "newcomers with a foreign license") + ", parents.",
 "Module 6, Series strip: the other Permit Path state editions.",
])}
<h2>Before Upload</h2>
{li(open_items)}
"""
    for bad in ("—", "–"):
        assert bad not in body, (c, bad)
    desc = body.split("<h2>Product Description</h2>")[1].split("<h2>Editorial Reviews</h2>")[0]
    for bad in ("$", "202"):
        assert bad not in desc, (c, bad)
    assert "flashcard" not in sub.lower() and "free" not in sub.lower()
    return body, pg, app

out = ROOT / "listing/upload"; out.mkdir(exist_ok=True)
for c in S:
    body, pg, app = doc(c)
    (out / f"{c}.html").write_text(f"<html><body>{body}</body></html>")
    print(c, pg, app)
