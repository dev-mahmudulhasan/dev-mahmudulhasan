import textwrap, os
from xml.sax.saxutils import escape as E

OUT = "assets"
FONT = "'Segoe UI', -apple-system, BlinkMacSystemFont, Helvetica, Arial, sans-serif"
BG1, BG2 = "#0B1220", "#0F1E36"
CARD, LINE = "#0F1A2E", "#1E2A44"
ACC, ACC2 = "#13B9FD", "#02569B"
TXT, MUT, DIM = "#F1F5F9", "#94A3B8", "#64748B"

def save(name, w, h, body, style=""):
    svg = f'''<svg xmlns="http://www.w3.org/2000/svg" width="{w}" height="{h}" viewBox="0 0 {w} {h}" font-family="{FONT}">
<style>{style}</style>
{body}
</svg>'''
    open(os.path.join(OUT, name), "w").write(svg)

def tw(s, size, bold=False):  # rough text width
    return sum(0.7 if c.isupper() else 0.55 for c in s) * size * (1.07 if bold else 1)

def chip(x, y, label, fill="#13233D", stroke="#24406A", color=TXT, size=13, dot=None):
    w = tw(label, size) + 26 + (14 if dot else 0)
    h = size + 15
    s = f'<rect x="{x}" y="{y}" width="{w:.0f}" height="{h}" rx="{h/2}" fill="{fill}" stroke="{stroke}"/>'
    tx = x + 13
    if dot:
        s += f'<circle cx="{x+15}" cy="{y+h/2}" r="4" fill="{dot}"/>'
        tx += 12
    s += f'<text x="{tx:.0f}" y="{y+h/2+size*0.36:.1f}" font-size="{size}" fill="{color}">{E(label)}</text>'
    return s, w

GRAD = f'''<defs>
<linearGradient id="bg" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="{BG1}"/><stop offset="1" stop-color="{BG2}"/></linearGradient>
<linearGradient id="acc" x1="0" y1="0" x2="1" y2="0"><stop offset="0" stop-color="{ACC}"/><stop offset="1" stop-color="{ACC2}"/></linearGradient>
<radialGradient id="glow"><stop offset="0" stop-color="{ACC}" stop-opacity=".35"/><stop offset="1" stop-color="{ACC}" stop-opacity="0"/></radialGradient>
<pattern id="dots" width="22" height="22" patternUnits="userSpaceOnUse"><circle cx="2" cy="2" r="1" fill="#1C2A44"/></pattern>
</defs>'''

# ---------- HEADER ----------
def header():
    W, H = 840, 280
    b = GRAD
    b += f'<rect width="{W}" height="{H}" rx="18" fill="url(#bg)"/>'
    b += f'<rect width="{W}" height="{H}" rx="18" fill="url(#dots)"/>'
    b += f'<circle class="pulse" cx="700" cy="120" r="170" fill="url(#glow)"/>'
    b += f'<rect x="0.5" y="0.5" width="{W-1}" height="{H-1}" rx="18" fill="none" stroke="{LINE}"/>'
    b += f'<text x="48" y="70" font-size="13" font-weight="600" letter-spacing="2.5" fill="{ACC}">SOFTWARE ENGINEER · MOBILE</text>'
    b += f'<text x="46" y="122" font-size="44" font-weight="700" fill="{TXT}">Md Mahmudul Hasan</text>'
    b += f'<rect x="48" y="138" width="64" height="4" rx="2" fill="url(#acc)"/>'
    b += f'<text x="48" y="174" font-size="17" fill="{MUT}">Flutter engineer shipping production apps</text>'
    b += f'<text x="48" y="198" font-size="17" fill="{MUT}">for Android &amp; iOS since 2022.</text>'
    x = 48
    for lab in ["4+ years", "8 production apps", "6 live on stores", "Dhaka, BD"]:
        s, w = chip(x, 222, lab, size=12.5)
        b += s; x += w + 8
    # phone mockup
    px, py = 640, 34
    b += f'<g transform="translate({px},{py})">'
    b += f'<rect width="128" height="214" rx="20" fill="#0A1426" stroke="#2A3B5C" stroke-width="2"/>'
    b += f'<rect x="48" y="9" width="32" height="5" rx="2.5" fill="#2A3B5C"/>'
    b += f'<rect x="12" y="26" width="104" height="44" rx="9" fill="url(#acc)" opacity=".9"/>'
    b += f'<rect x="22" y="38" width="46" height="6" rx="3" fill="#fff" opacity=".9"/><rect x="22" y="51" width="70" height="5" rx="2.5" fill="#fff" opacity=".55"/>'
    for i in range(4):
        y = 82 + i * 30
        b += f'<g class="row r{i}"><rect x="12" y="{y}" width="22" height="22" rx="6" fill="#16304F"/>'
        b += f'<rect x="42" y="{y+4}" width="{60 - i*6}" height="5" rx="2.5" fill="#3B5378"/>'
        b += f'<rect x="42" y="{y+14}" width="{44 + i*5}" height="4" rx="2" fill="#24385A"/></g>'
    b += f'<rect x="44" y="200" width="40" height="4" rx="2" fill="#2A3B5C"/>'
    b += '</g>'
    # flutter-ish chevrons
    for cx, cy, r, o in [(585, 70, 4, .7), (600, 210, 3, .5), (800, 245, 5, .4), (560, 150, 2.5, .6)]:
        b += f'<circle cx="{cx}" cy="{cy}" r="{r}" fill="{ACC}" opacity="{o}"/>'
    style = ".pulse{animation:p 6s ease-in-out infinite;transform-origin:700px 120px}@keyframes p{50%{opacity:.55;transform:scale(1.08)}}" \
            ".row{opacity:1;animation:f 4s ease-in-out infinite}.r1{animation-delay:.4s}.r2{animation-delay:.8s}.r3{animation-delay:1.2s}@keyframes f{0%,100%{opacity:1}50%{opacity:.45}}"
    save("header.svg", W, H, b, style)

# ---------- EXPERIENCE ----------
def experience():
    W, H = 840, 340
    b = GRAD + f'<rect width="{W}" height="{H}" rx="18" fill="url(#bg)"/><rect x=".5" y=".5" width="{W-1}" height="{H-1}" rx="18" fill="none" stroke="{LINE}"/>'
    b += f'<text x="40" y="50" font-size="13" font-weight="600" letter-spacing="2.5" fill="{ACC}">EXPERIENCE</text>'
    b += f'<line x1="52" y1="88" x2="52" y2="232" stroke="#24406A" stroke-width="2" stroke-dasharray="4 5"/>'
    items = [
        ("Software Engineer (Mobile)", "Analyzen Bangladesh Limited", "Dec 2024 — Present", True,
         ["Building Creed, a Muslim commerce platform & global business",
          "directory, live on Google Play and the App Store."]),
        ("Mobile Application Developer", "Limerick Resources Limited", "Apr 2022 — Nov 2024", False,
         ["Built end-to-end sales & distribution apps (DSR MDO, Distributor)",
          "that replaced paper and phone-based field workflows."]),
    ]
    y = 88
    for role, co, date, cur, lines in items:
        if cur:
            b += f'<circle class="ring" cx="52" cy="{y}" r="12" fill="{ACC}" opacity=".25"/>'
        b += f'<circle cx="52" cy="{y}" r="6.5" fill="{ACC if cur else "#3B5378"}" stroke="{BG1}" stroke-width="3"/>'
        b += f'<text x="80" y="{y+6}" font-size="19" font-weight="700" fill="{TXT}">{E(role)}</text>'
        b += f'<text x="800" y="{y+5}" font-size="13" text-anchor="end" fill="{ACC if cur else MUT}" font-weight="600">{date}</text>'
        b += f'<text x="80" y="{y+30}" font-size="14.5" fill="{ACC if cur else MUT}">{E(co)}</text>'
        for i, l in enumerate(lines):
            b += f'<text x="80" y="{y+56+i*21}" font-size="14" fill="{MUT}">{E(l)}</text>'
        y += 144
    style = ".ring{animation:r 2.4s ease-out infinite;transform-origin:52px 88px}@keyframes r{0%{transform:scale(.6);opacity:.5}100%{transform:scale(1.8);opacity:0}}"
    save("experience.svg", W, H, b, style)

# ---------- PROJECT CARDS ----------
PROJECTS = [
    ("creed", "Creed", "COMMERCE", "Muslim commerce platform and global business directory.", ["Android", "iOS"], ("#13B9FD", "#02569B")),
    ("nafs-cart", "Nafs Cart", "E-COMMERCE", "Shopping app with catalogue, cart and checkout.", ["iOS"], ("#F59E0B", "#B45309")),
    ("orderwala", "OrderWala", "RETAIL OPS", "Order management system for retailers.", ["Android"], ("#22C55E", "#15803D")),
    ("dsr-mdo", "DSR MDO", "SALES FORCE", "Daily sales representative and market development app.", ["Android"], ("#A78BFA", "#6D28D9")),
    ("distributor", "Distributor", "SUPPLY CHAIN", "Distributor onboarding and stock tracking.", ["Android"], ("#F472B6", "#BE185D")),
    ("bddoctor", "BDDoctor", "HEALTHCARE", "Doctor and hospital finder with geo-search.", ["Android"], ("#2DD4BF", "#0F766E")),
    ("boichitro", "Boichitro", "DIGITAL BOOKS", "Digital bookstore and e-reading experience.", ["Private"], ("#FB923C", "#C2410C")),
    ("hrm", "HRM", "HR &amp; PAYROLL", "Human resource and payroll management.", ["Internal"], ("#60A5FA", "#1D4ED8")),
]
PILL = {"Android": "#3DDC84", "iOS": "#E2E8F0", "Private": DIM, "Internal": DIM}

def card(slug, name, cat, desc, plats, cols):
    W, H = 410, 178
    c1, c2 = cols
    b = f'''<defs><linearGradient id="ic" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="{c1}"/><stop offset="1" stop-color="{c2}"/></linearGradient>
<linearGradient id="bg" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="{BG1}"/><stop offset="1" stop-color="{BG2}"/></linearGradient></defs>'''
    b += f'<rect width="{W}" height="{H}" rx="16" fill="url(#bg)"/><rect x=".5" y=".5" width="{W-1}" height="{H-1}" rx="16" fill="none" stroke="{LINE}"/>'
    b += f'<rect x="22" y="0" width="{W-44}" height="3" rx="1.5" fill="url(#ic)" opacity=".9"/>'
    b += f'<rect x="22" y="24" width="50" height="50" rx="13" fill="url(#ic)"/>'
    initials = {"Creed":"C","Nafs Cart":"NC","OrderWala":"OW","DSR MDO":"DM","Distributor":"D","BDDoctor":"BD","Boichitro":"Bo","HRM":"HR"}[name]
    b += f'<text x="47" y="56" font-size="19" font-weight="700" fill="#fff" text-anchor="middle">{E(initials)}</text>'
    b += f'<text x="86" y="45" font-size="20" font-weight="700" fill="{TXT}">{E(name)}</text>'
    b += f'<text x="86" y="67" font-size="11" font-weight="600" letter-spacing="1.8" fill="{c1}">{cat}</text>'
    for i, l in enumerate(textwrap.wrap(desc, 46)[:2]):
        b += f'<text x="22" y="{100+i*19}" font-size="14" fill="{MUT}">{E(l)}</text>'
    x = 22
    for p in plats:
        s, w = chip(x, 138, p, fill="#111D33", stroke="#24364F", color=TXT if p in ("Android", "iOS") else MUT, size=12, dot=PILL[p])
        b += s; x += w + 8
    if plats[0] in ("Android", "iOS"):
        b += f'<text x="388" y="157" font-size="12.5" text-anchor="end" fill="{DIM}">View ↗</text>'
    save(f"project-{slug}.svg", W, H, b)

# ---------- STACK ----------
def stack():
    rows = [
        ("Mobile", ["Flutter", "Dart", "Bloc", "GetX", "Clean Architecture"]),
        ("Backend", ["Firebase Auth", "Firestore", "Cloud Functions", "Laravel", "MySQL"]),
        ("Web / Admin", ["React"]),
        ("Integrations", ["bKash", "SSLCOMMERZ", "Stripe", "Agora", "Google Maps", "Facebook SDK"]),
        ("Release", ["Play Console", "App Store Connect"]),
        ("Workflow", ["Git", "GitHub", "GitLab", "Jira", "ClickUp", "Figma"]),
    ]
    W = 840; top = 76; rh = 46; H = top + rh * len(rows) + 24
    b = GRAD + f'<rect width="{W}" height="{H}" rx="18" fill="url(#bg)"/><rect x=".5" y=".5" width="{W-1}" height="{H-1}" rx="18" fill="none" stroke="{LINE}"/>'
    b += f'<text x="40" y="50" font-size="13" font-weight="600" letter-spacing="2.5" fill="{ACC}">TECH STACK</text>'
    for i, (lab, items) in enumerate(rows):
        y = top + i * rh
        if i: b += f'<line x1="40" y1="{y-8}" x2="800" y2="{y-8}" stroke="#16233A"/>'
        b += f'<text x="40" y="{y+19}" font-size="14" font-weight="600" fill="{TXT}">{lab}</text>'
        x = 180
        for j, it in enumerate(items):
            hl = (i == 0 and j < 3)
            s, w = chip(x, y, it, fill="#0E2A47" if hl else "#111D33", stroke=ACC if hl else "#24364F", color=TXT, size=12.5)
            b += s; x += w + 8
    save("stack.svg", W, H, b)

def footer():
    W, H = 840, 70
    b = GRAD + f'<rect x="0" y="20" width="{W}" height="2" fill="url(#acc)" opacity=".6"/>'
    b += f'<text x="{W/2}" y="54" font-size="13" text-anchor="middle" fill="{DIM}">Building reliable mobile products from Dhaka, Bangladesh</text>'
    save("footer.svg", W, H, b)

header(); experience(); stack(); footer()
for p in PROJECTS: card(*p)
print("done", len(os.listdir(OUT)))
