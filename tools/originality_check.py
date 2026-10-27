"""Originality check against the Daniel Hart DMV texts.

The reference is stored only as hashed 8-word sequences (ref/*.hashes), never as raw text.

Usage:
  python3 tools/originality_check.py build-ref NAME SOURCE.txt     # create ref/NAME.hashes from a text file
  python3 tools/originality_check.py check FILE.md [FILE.md ...]    # check text; exit 1 on failure

Fails when any run of 12+ consecutive words matches a reference text, or when more than
1 percent of the 8-word sequences in the checked text appear in a reference.
"""
import sys, re, hashlib, pathlib

ROOT = pathlib.Path(__file__).resolve().parent.parent
REF = ROOT / "ref"
N = 8            # shingle size
RUN = 12         # words in a row that count as a copied sentence
MAX_OVERLAP = 0.01


def tokens(text):
    text = re.sub(r"<!--.*?-->", " ", text, flags=re.S)
    text = re.sub(r"\{\{[^}]*\}\}|\[APP-LINK[^\]]*\]", " ", text)
    return re.findall(r"[a-z0-9]+", text.lower().replace("’", "'").replace("'", ""))


def h(words):
    return hashlib.blake2b(" ".join(words).encode(), digest_size=6).hexdigest()


def shingles(tok):
    return [h(tok[i:i + N]) for i in range(len(tok) - N + 1)]


def load_ref():
    ref = set()
    for f in sorted(REF.glob("*.hashes")):
        ref.update(f.read_text().split())
    if not ref:
        sys.exit("no reference hashes in ref/")
    return ref


def check(paths):
    ref = load_ref()
    total = hit = 0
    failures = []
    for p in paths:
        tok = tokens(pathlib.Path(p).read_text())
        sh = shingles(tok)
        marks = [s in ref for s in sh]
        total += len(sh)
        hit += sum(marks)
        i = 0
        while i < len(marks):
            if marks[i]:
                j = i
                while j < len(marks) and marks[j]:
                    j += 1
                run_words = (j - i) + N - 1
                if run_words >= RUN:
                    failures.append(f"{p}: {run_words} words copied: \"{' '.join(tok[i:i + min(run_words, 25)])}...\"")
                i = j
            else:
                i += 1
    rate = hit / total if total else 0
    print(f"Originality: {total} sequences checked, {hit} shared ({rate:.2%}), {len(failures)} copied runs of {RUN}+ words")
    for f in failures[:30]:
        print("  -", f)
    if failures or rate > MAX_OVERLAP:
        print("ORIGINALITY FAILED")
        return 1
    print("ORIGINALITY PASSED")
    return 0


if __name__ == "__main__":
    if len(sys.argv) >= 4 and sys.argv[1] == "build-ref":
        REF.mkdir(exist_ok=True)
        hs = sorted(set(shingles(tokens(pathlib.Path(sys.argv[3]).read_text()))))
        (REF / f"{sys.argv[2]}.hashes").write_text("\n".join(hs) + "\n")
        print(f"ref/{sys.argv[2]}.hashes: {len(hs)} sequences")
    elif len(sys.argv) >= 3 and sys.argv[1] == "check":
        sys.exit(check(sys.argv[2:]))
    else:
        sys.exit(__doc__)
