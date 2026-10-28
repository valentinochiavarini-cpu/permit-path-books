"""Re-draw a state's mocks with the same format already stored in state/XX/mocks.json
(size, pass text, parts, size note). Use after bank changes, for example when questions become app_only.
Usage: python3 tools/regen_mocks.py XX [XX ...]
A part whose name contains "Sign" draws from chapter 2; other parts draw from every other chapter."""
import json, sys, subprocess, pathlib
ROOT = pathlib.Path(__file__).resolve().parent.parent
for code in [c.upper() for c in sys.argv[1:]]:
    m = json.loads((ROOT / f"state/{code}/mocks.json").read_text())
    cmd = [sys.executable, str(ROOT / "tools/make_mocks.py"), code]
    if m.get("parts"):
        for p in m["parts"]:
            ch = "2" if "sign" in p["name"].lower() else ""
            cmd += ["--part", f"{p['name']}|{p['size']}|{p['pass']}|{ch}"]
        cmd += ["--pass", m["pass"]]
    else:
        cmd += [str(m["size"]), m["pass"]]
    if m.get("size_note"):
        cmd += ["--size-note", m["size_note"]]
    print(code, subprocess.run(cmd, capture_output=True, text=True).stdout.strip().replace("\n", " | "))
