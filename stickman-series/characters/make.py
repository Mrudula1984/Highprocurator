import random, math, os, sys
OUT = sys.argv[1]
W = 1024

def scribble(clip_id, x0, y0, x1, y1, color, seed, sw=30, gap=30):
    r = random.Random(seed)
    pts = []
    # diagonal zigzag strokes across bbox
    y = y0 - 40
    y1 = y1 + 260
    out = []
    while y < y1 + 80:
        d = f"M{x0-40},{y+r.uniform(-6,6):.0f}"
        x = x0 - 40
        up = True
        while x < x1 + 40:
            x += r.uniform(34, 58)
            yy = y + (-gap*2.0 if up else 0) + r.uniform(-12, 12) - (x-x0)*0.35
            d += f" L{x:.0f},{yy:.0f}"
            up = not up
        out.append(f'<path d="{d}" fill="none" stroke="{color}" stroke-width="{sw}" stroke-linecap="round" stroke-linejoin="round" opacity="0.92"/>')
        y += gap*1.55 + r.uniform(0, 22)
    return f'<g clip-path="url(#{clip_id})">' + "".join(out) + "</g>"

def mitten(x, y, ang, fill, stroke, sw, s=1.0):
    return (f'<g transform="translate({x},{y}) rotate({ang}) scale({s})">'
            f'<ellipse cx="2" cy="-30" rx="11" ry="19" transform="rotate(-25 2 -30)" fill="{fill}" stroke="{stroke}" stroke-width="{sw}"/>'
            f'<ellipse cx="18" cy="0" rx="34" ry="27" fill="{fill}" stroke="{stroke}" stroke-width="{sw}"/>'
            f'<ellipse cx="2" cy="-30" rx="8" ry="15" transform="rotate(-25 2 -30)" fill="{fill}"/></g>')

def ang(a, b):
    return math.degrees(math.atan2(b[1]-a[1], b[0]-a[0]))

def arm(pts, sw, color="#111"):
    d = "M" + " L".join(f"{x},{y}" for x, y in pts)
    return f'<path d="{d}" fill="none" stroke="{color}" stroke-width="{sw}" stroke-linecap="round" stroke-linejoin="round"/>'

def svg(body, bg=True):
    b = '<rect width="1024" height="1024" fill="#ffffff"/>' if bg else ""
    return f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{W}" viewBox="0 0 {W} {W}">{b}{body}</svg>'

# ---------------- BLU ----------------
BLU_POSES = {
  "wave":    dict(L=[(432,525),(320,470),(280,320)], La=-80, R=[(592,525),(680,600),(610,690)], Ra=200, mouth="smile", eyes=(0,0)),
  "think":   dict(L=[(432,525),(320,600),(400,470)], La=-40, R=[(592,525),(660,640),(640,720)], Ra=90, mouth="o", eyes=(10,-10)),
  "explain": dict(L=[(432,525),(360,620),(370,720)], La=90, R=[(592,525),(700,470),(800,400)], Ra=-35, mouth="smile", eyes=(8,0)),
}
def blu(pose, bg=True):
    p = BLU_POSES[pose]
    s = ['<defs><clipPath id="bh"><circle cx="512" cy="300" r="168"/></clipPath>'
         '<clipPath id="bt"><rect x="424" y="492" width="176" height="206" rx="34"/></clipPath></defs>']
    # legs + feet
    s.append(arm([(472,690),(462,900)], 30)); s.append(arm([(552,690),(566,900)], 30))
    s.append('<ellipse cx="430" cy="912" rx="62" ry="32" fill="#111"/><ellipse cx="600" cy="912" rx="62" ry="32" fill="#111"/>')
    # torso
    s.append('<rect x="424" y="492" width="176" height="206" rx="34" fill="#fff"/>')
    s.append(scribble("bt", 424, 492, 600, 698, "#7FB2E0", 7))
    s.append('<rect x="424" y="492" width="176" height="206" rx="34" fill="none" stroke="#111" stroke-width="20"/>')
    # head
    s.append('<circle cx="512" cy="300" r="168" fill="#fff"/>')
    s.append(scribble("bh", 344, 132, 680, 468, "#F9C784", 3))
    s.append('<circle cx="512" cy="300" r="168" fill="none" stroke="#111" stroke-width="20"/>')
    ex, ey = p["eyes"]
    s.append(f'<ellipse cx="{458+ex}" cy="{262+ey}" rx="22" ry="32" fill="#1a120b"/><ellipse cx="{566+ex}" cy="{262+ey}" rx="22" ry="32" fill="#1a120b"/>')
    if p["mouth"] == "smile":
        s.append(f'<path d="M{440+ex},{350} Q{512+ex},{420} {584+ex},{350}" fill="none" stroke="#111" stroke-width="10" stroke-linecap="round"/>')
    else:
        s.append(f'<ellipse cx="{530+ex}" cy="370" rx="18" ry="22" fill="none" stroke="#111" stroke-width="9"/>')
    s.append(arm(p["L"], 30)); s.append(arm(p["R"], 30))
    s.append(mitten(*p["L"][-1], p["La"], "#111", "#111", 0, 1.6))
    s.append(mitten(*p["R"][-1], p["Ra"], "#111", "#111", 0, 1.6))
    return svg("".join(s), bg)

# ---------------- SUNNY ----------------
SUNNY_POSES = {
  "present": dict(L=[(496,500),(400,640),(330,560)], La=-120, R=[(528,500),(624,640),(694,560)], Ra=-60, mouth="open"),
  "point":   dict(L=[(496,500),(420,640),(430,720)], La=100, R=[(528,500),(660,440),(790,380)], Ra=-30, mouth="open"),
  "wave":    dict(L=[(496,500),(400,640),(400,730)], La=95, R=[(528,500),(670,470),(740,330)], Ra=-70, mouth="smile"),
}
def sunny(pose, bg=True):
    p = SUNNY_POSES[pose]
    s = ['<defs><radialGradient id="sh" cx="0.45" cy="0.38" r="0.7"><stop offset="0" stop-color="#FFF07A"/>'
         '<stop offset="0.7" stop-color="#FFE04D"/><stop offset="1" stop-color="#F4B81F"/></radialGradient>'
         '<linearGradient id="sb" x1="0" x2="1"><stop offset="0" stop-color="#FFE04D"/><stop offset="0.7" stop-color="#FFE04D"/>'
         '<stop offset="1" stop-color="#F2B320"/></linearGradient></defs>']
    # legs
    s.append(arm([(490,760),(458,935)], 9)); s.append(arm([(536,760),(568,935)], 9))
    s.append('<ellipse cx="440" cy="945" rx="48" ry="20" fill="#FFE04D" stroke="#111" stroke-width="8"/>')
    s.append('<ellipse cx="588" cy="945" rx="48" ry="20" fill="#FFE04D" stroke="#111" stroke-width="8"/>')
    # arms
    s.append(arm(p["L"], 9)); s.append(arm(p["R"], 9))
    s.append(mitten(*p["L"][-1], p["La"], "#FFE04D", "#111", 7, 1.25))
    s.append(mitten(*p["R"][-1], p["Ra"], "#FFE04D", "#111", 7, 1.25))
    # torso teardrop
    s.append('<path d="M492,470 C486,520 440,640 446,720 C450,775 576,775 580,720 C586,640 540,520 534,470 Z" fill="url(#sb)" stroke="#111" stroke-width="9"/>')
    s.append('<path d="M470,700 C480,740 540,745 560,720" fill="none" stroke="#F2B320" stroke-width="10" opacity="0.6"/>')
    # head
    s.append('<circle cx="512" cy="290" r="168" fill="url(#sh)" stroke="#111" stroke-width="9"/>')
    s.append('<path d="M370,350 A150,150 0 0 0 654,350 A168,140 0 0 1 370,350 Z" fill="#F2B320" opacity="0.55"/>')
    s.append('<ellipse cx="600" cy="168" rx="20" ry="13" fill="#fff" transform="rotate(25 600 168)"/><circle cx="636" cy="205" r="8" fill="#fff"/>')
    s.append('<ellipse cx="460" cy="250" rx="18" ry="38" fill="#111"/><ellipse cx="564" cy="250" rx="18" ry="38" fill="#111"/>')
    if p["mouth"] == "open":
        s.append('<path d="M430,320 L594,320 Q590,410 512,410 Q434,410 430,320 Z" fill="#111"/>')
        s.append('<path d="M478,392 Q512,365 546,392 Q512,412 478,392 Z" fill="#E8262B"/>')
    else:
        s.append('<path d="M440,330 Q512,400 584,330" fill="none" stroke="#111" stroke-width="12" stroke-linecap="round"/>')
    return svg("".join(s), bg)

os.makedirs(OUT, exist_ok=True)
for k in BLU_POSES:
    open(f"{OUT}/blu_{k}.svg","w").write(blu(k)); open(f"{OUT}/blu_{k}_transparent.svg","w").write(blu(k,False))
for k in SUNNY_POSES:
    open(f"{OUT}/sunny_{k}.svg","w").write(sunny(k)); open(f"{OUT}/sunny_{k}_transparent.svg","w").write(sunny(k,False))
print("done")
