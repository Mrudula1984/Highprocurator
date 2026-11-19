# Builds scene.html: an SVG animation of EP01, driven by window.render(t)
import json, re, runpy, sys, tempfile, os
HERE = os.path.dirname(os.path.abspath(__file__))
CHAR = os.path.join(HERE, "..", "..", "characters", "make.py")
tmp = tempfile.mkdtemp()
sys.argv = ["make.py", tmp]
m = runpy.run_path(CHAR)
def inner(svg):
    return re.sub(r"^<svg[^>]*>|</svg>$", "", svg)
chars = {}
for p in ["wave", "think", "explain"]:
    chars["blu_" + p] = inner(m["blu"](p, False))
for p in ["present", "point", "wave"]:
    chars["sunny_" + p] = inner(m["sunny"](p, False))
words = json.load(open(os.path.join(HERE, "words.json")))
html = open(os.path.join(HERE, "scene_template.html")).read()
html = html.replace("/*CHARS*/", "const CHARS=" + json.dumps(chars) + ";")
html = html.replace("/*WORDS*/", "const WORDS=" + json.dumps(words) + ";")
open(os.path.join(HERE, "scene.html"), "w").write(html)
print("built")
