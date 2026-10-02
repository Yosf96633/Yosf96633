"""Generate the Linux desktop's self-contained SVGs and native GIF animation.

Only the small activity ribbon uses Pillow. The generated hero is independent
artwork, currently stored in assets/desktop/hero-ubuntu-v3.png.
"""

from html import escape
from math import cos, pi, sin
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont


OUT = Path(__file__).resolve().parents[1] / "assets" / "desktop"
BG = "#0d0b16"
FG = "#f5f0e9"
MUTED = "#b8afc9"
VIOLET = "#b66aff"
CYAN = "#54dcf1"
ORANGE = "#ffa15a"
MONO = "DejaVu Sans Mono, monospace"
SANS = "DejaVu Sans, Arial, sans-serif"

PROJECTS = [
    ("myshell", "myShell", "Unix processes. A shell from scratch.", "SYSTEMS", ORANGE),
    ("autohunt", "AutoHunt", "From CV to a reviewed job application.", "AGENTIC AI", CYAN),
    ("docsai", "DocsAI", "Document answers you can trace.", "RETRIEVAL", VIOLET),
    ("vidspire", "Vidspire / Vidly", "Understand the conversation around a video.", "SENTIMENT", ORANGE),
    ("better-auth", "Better Auth Starter", "OAuth, sessions, and two-factor authentication.", "AUTHENTICATION", VIOLET),
]


def text(x, y, value, size=20, color=FG, bold=False, mono=False, extra=""):
    return (f'<text x="{x}" y="{y}" fill="{color}" font-size="{size}" '
            f'font-family="{MONO if mono else SANS}" '
            f'font-weight="{700 if bold else 400}" {extra}>{escape(value)}</text>')


def line(x1, y1, x2, y2, color=VIOLET, width=2, extra=""):
    return (f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" '
            f'stroke="{color}" stroke-width="{width}" {extra}/>')


def rect(x, y, w, h, fill="#161021", stroke="#443254", radius=12, extra=""):
    return (f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{radius}" '
            f'fill="{fill}" stroke="{stroke}" {extra}/>')


def circle(x, y, r, color, extra=""):
    return f'<circle cx="{x}" cy="{y}" r="{r}" fill="{color}" {extra}/>'


def window(x, y, w, h, title, accent):
    s = rect(x, y, w, h, "url(#glass)", accent)
    s += line(x, y + 28, x + w, y + 28, "#40314f", 1)
    for i, c in enumerate((ORANGE, VIOLET, CYAN)):
        s += circle(x + 14 + i * 13, y + 14, 3, c)
    s += text(x + 57, y + 19, title, 11, MUTED, mono=True)
    return s


def node(x, y, label, accent, width=80):
    return rect(x, y, width, 35, "#171225", accent, 8) + text(x + width / 2, y + 23, label, 12, FG, mono=True, extra='text-anchor="middle"')


def svg(body, width, height, title, description, accent=VIOLET):
    return f'''<svg xmlns="http://www.w3.org/2000/svg" width="{width}" height="{height}" viewBox="0 0 {width} {height}" role="img" aria-labelledby="title description">
<title id="title">{escape(title)}</title><desc id="description">{escape(description)}</desc>
<defs>
 <linearGradient id="base" x2="1" y2="1"><stop stop-color="#151020"/><stop offset=".6" stop-color="#0d0c16"/><stop offset="1" stop-color="#1d102b"/></linearGradient>
 <linearGradient id="glass" x2=".7" y2="1"><stop stop-color="#291e3b" stop-opacity=".95"/><stop offset="1" stop-color="#100e1b" stop-opacity=".98"/></linearGradient>
 <radialGradient id="halo"><stop stop-color="{accent}" stop-opacity=".18"/><stop offset="1" stop-color="{accent}" stop-opacity="0"/></radialGradient>
 <pattern id="grid" width="32" height="32" patternUnits="userSpaceOnUse"><path d="M32 0H0V32" fill="none" stroke="#b66aff" stroke-opacity=".07"/></pattern>
 <filter id="glow" x="-100%" y="-100%" width="300%" height="300%"><feGaussianBlur stdDeviation="4"/></filter>
</defs>
{body}
</svg>'''


def diagram(slug, accent):
    """All diagrams are illustrations of features, never live data."""
    s = '<ellipse cx="270" cy="140" rx="295" ry="190" fill="url(#halo)"/>'
    s += '<path d="M0 290 240 172 550 248M20 270 270 150 550 222M80 300 310 183 540 266" stroke="#483059" stroke-width="1" fill="none"/>'
    # Tilted glass planes behind the diagram give the desktop illustration
    # depth while keeping labels on the front plane crisp and readable.
    s += '<g transform="rotate(-5 270 154)" opacity=".4">' + rect(46, 23, 454, 252, "url(#glass)", VIOLET, 12) + '</g>'
    s += '<g transform="rotate(4 270 154)" opacity=".25">' + rect(74, 33, 430, 245, "url(#glass)", CYAN, 12) + '</g>'
    s += window(60, 38, 430, 240, "~/" + slug, accent)
    if slug == "myshell":
        s += text(84, 98, "$ parse → execute", 16, accent, mono=True)
        s += node(230, 120, "process", accent)
        for x, label in ((90, "fork()"), (230, "exec()"), (370, "wait()")):
            s += f'<path d="M270 155V174H{x + 40}V188" fill="none" stroke="{accent}" stroke-opacity=".6"/>'
            s += node(x, 188, label, accent)
        s += text(86, 253, "pipes / signals / job control", 13, MUTED, mono=True)
    elif slug == "autohunt":
        labels = ["CV", "MATCH", "DRAFT", "REVIEW", "APPLY"]
        points = [(120, 128), (270, 104), (415, 128), (360, 221), (170, 221)]
        for i, (x, y) in enumerate(points):
            nx, ny = points[(i + 1) % len(points)]
            s += line(x, y, nx, ny, accent, 2, 'opacity=".5"')
        for (x, y), label in zip(points, labels):
            color = ORANGE if label == "REVIEW" else accent
            s += circle(x, y, 31, "#171226", f'stroke="{color}" stroke-width="2"')
            s += text(x, y + 4, label, 11, FG, bold=True, mono=True, extra='text-anchor="middle"')
        s += rect(223, 148, 94, 30, "#2b1c3e", VIOLET, 15)
        s += text(270, 168, "STATE", 12, VIOLET, bold=True, mono=True, extra='text-anchor="middle"')
    elif slug == "docsai":
        for offset in (16, 8, 0):
            s += rect(91 + offset, 102 - offset, 80, 120, "#21192f", accent, 6)
        for y in range(127, 192, 16):
            s += line(104, y, 157, y, "#9683b2", 3)
        s += line(186, 158, 221, 158, CYAN, 2)
        s += '<path d="M237 120V200C237 220 315 220 315 200V120" fill="#21192f" stroke="#54dcf1" stroke-width="2"/>'
        s += '<ellipse cx="276" cy="120" rx="39" ry="13" fill="#24203b" stroke="#54dcf1" stroke-width="2"/>'
        s += '<path d="M237 157C237 176 315 176 315 157M237 183C237 202 315 202 315 183" fill="none" stroke="#54dcf1"/>'
        s += line(331, 158, 363, 158, CYAN, 2)
        s += rect(378, 102, 86, 120, "#21192f", accent, 6)
        for y, w in ((125, 58), (146, 39), (167, 58), (188, 48)):
            s += rect(391, y, w, 7, accent if y == 146 else "#7e7290", "none", 2)
        s += text(120, 252, "PDF → retrieve → rerank → cite", 12, MUTED, mono=True)
    elif slug == "vidspire":
        s += rect(86, 92, 179, 119, "#21182e", accent, 8)
        s += '<path d="M157 120 157 179 207 149Z" fill="#ffa15a"/>'
        for y, width, c in ((111, 134, CYAN), (155, 91, VIOLET), (199, 56, ORANGE)):
            s += rect(299, y, 148, 13, "#281d35", "none", 5)
            s += rect(299, y, width, 13, c, "none", 5)
        s += text(106, 250, "video / comments / sentiment", 13, MUTED, mono=True)
    else:
        s += '<path d="M277 92 339 115V166C339 205 309 230 277 246 245 230 215 205 215 166V115Z" fill="#2d1b44" stroke="#b66aff" stroke-width="2"/>'
        s += rect(252, 160, 50, 40, "#b66aff", "none", 6)
        s += '<path d="M260 161V144A17 17 0 0 1 294 144V161" fill="none" stroke="#f5f0e9" stroke-width="4"/>'
        s += circle(277, 177, 4, BG)
        s += line(277, 179, 277, 188, BG, 3)
        s += node(80, 119, "OAuth", CYAN, 95)
        s += node(366, 119, "TOTP", ORANGE, 95)
        s += line(175, 137, 215, 137, CYAN)
        s += line(339, 137, 366, 137, ORANGE)
        for x in range(86, 168, 16):
            s += circle(x, 200, 4, CYAN)
        s += text(359, 209, "sessions", 12, MUTED, mono=True)
    return s


def project_cards():
    for index, (slug, name, caption, category, accent) in enumerate(PROJECTS, 1):
        for mobile in (False, True):
            width, height = (640, 520) if mobile else (1200, 332)
            body = rect(1, 1, width - 2, height - 2, "url(#base)", "#4d3865", 18)
            body += rect(1, 1, width - 2, height - 2, "url(#grid)", "none", 18)
            body += text(34, 54, f"{index:02d} / {category}", 14, accent, mono=True, extra='letter-spacing="2"')
            body += text(34, 117 if mobile else 128, name, 38 if len(name) > 12 else 52, FG, bold=True)
            if mobile:
                body += text(35, 159, caption, 17, MUTED)
                body += f'<g transform="translate(43,182)">{diagram(slug, accent)}</g>'
            else:
                body += text(36, 179, caption, 18, MUTED)
                body += line(36, 210, 440, 210, "#483159", 1)
                body += text(36, 249, "~/projects/" + slug, 16, accent, mono=True)
                body += f'<g transform="translate(596,0)">{diagram(slug, accent)}</g>'
            body += circle(width - 29, 29, 4, accent)
            suffix = "-mobile" if mobile else ""
            (OUT / f"project-{slug}{suffix}-static.svg").write_text(svg(body, width, height, name, caption, accent))
            # A few moving light points trace the illustrated system. Native
            # SVG animation works as an image and requires no JavaScript.
            dx, dy = (43, 182) if mobile else (596, 0)
            route = {
                "myshell": "M270 156 V174 H130 V188",
                "autohunt": "M120 128 L270 104 L415 128 L360 221 L170 221 Z",
                "docsai": "M173 158 H235 M316 158 H376",
                "vidspire": "M298 111 H445 M298 155 H390 M298 199 H355",
                "better-auth": "M176 137 H214 M340 137 H365",
            }[slug]
            motion = f'<g transform="translate({dx},{dy})">'
            for i in range(2):
                motion += (f'<circle r="3" fill="{accent}"><animateMotion path="{route}" '
                           f'dur="6s" begin="-{i * 3}s" repeatCount="indefinite"/></circle>')
            motion += '</g>'
            (OUT / f"project-{slug}{suffix}.svg").write_text(svg(body + motion, width, height, name, caption, accent))


def section_headers():
    headings = [
        ("about", "ABOUT", "ME", "01 / ~/profile"),
        ("projects", "SELECTED", "BUILDS", "02 / ~/projects"),
        ("stack", "TECH", "STACK", "03 / ~/.config/stack"),
        ("experience", "WORK", "EXPERIENCE", "04 / ~/experience"),
        ("education", "EDUCATION", "", "05 / ~/education"),
        ("notes", "ENGINEERING", "NOTES", "06 / ~/notes"),
        ("activity", "OPEN", "SOURCE", "07 / ~/activity"),
        ("contact", "LET'S", "CONNECT", "08 / ~/contact"),
    ]
    for slug, first, second, path in headings:
        body = rect(0, 0, 1200, 130, BG, "none", 12)
        body += text(24, 34, path, 14, MUTED, mono=True, extra='letter-spacing="2"')
        body += text(21, 97, first, 51, FG, bold=True)
        # Font metrics make long titles fit without estimating character widths.
        font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", 51)
        end = 21 + font.getlength(first) + 20
        if second:
            body += text(round(end), 97, second, 51, VIOLET, bold=True)
            end += font.getlength(second)
        body += line(round(end + 28), 81, 1106, 81, "#554268", 1)
        for i, c in enumerate((ORANGE, CYAN, VIOLET)):
            body += rect(1125 + 21 * i, 75, 9, 9, c, "none", 1)
        (OUT / f"section-{slug}.svg").write_text(svg(body, 1200, 130, f"{first} {second}".strip(), path))


def group_headers():
    groups = [
        ("languages", "LANGUAGES", "01"),
        ("frontend", "FRONTEND & INTERFACES", "02"),
        ("backend", "BACKEND & AUTHENTICATION", "03"),
        ("data", "DATABASES & ORMS", "04"),
        ("ai", "AGENTIC AI & AUTOMATION", "05"),
        ("linux", "LINUX & SECURITY", "06"),
        ("tooling", "DEPLOYMENT & TOOLING", "07"),
    ]
    for slug, label, index in groups:
        body = rect(1, 1, 1198, 58, "url(#base)", "#34263f", 8)
        body += text(21, 37, index, 16, VIOLET, mono=True)
        body += line(63, 16, 63, 43, "#50375e", 1)
        body += text(82, 37, label, 18, FG, bold=True, extra='letter-spacing="2"')
        body += line(700, 30, 1174, 30, "#41304e", 1)
        (OUT / f"stack-{slug}.svg").write_text(svg(body, 1200, 60, label, "Technology icons follow this heading."))
        mobile = rect(1, 1, 638, 58, "url(#base)", "#34263f", 8)
        mobile += text(20, 37, index, 16, VIOLET, mono=True)
        mobile += line(57, 17, 57, 43, "#50375e", 1)
        mobile += text(75, 37, label, 18, FG, bold=True, extra='letter-spacing="1"')
        mobile += circle(616, 30, 3, VIOLET)
        (OUT / f"stack-{slug}-mobile.svg").write_text(svg(mobile, 640, 60, label, "Technology icons follow this heading."))


def experience_cards():
    items = [
        ("independent", "2026-05 → PRESENT", "Self-Employed", "Independent", VIOLET, "Systems / agents / full-stack"),
        ("mozzine", "2025-10 → 2026-04", "Frontend Developer", "Mozzine Technologies", CYAN, "B2B SaaS / responsive interfaces"),
        ("code-expert", "2025-07 → 2025-09", "Full Stack Intern", "Code Expert", ORANGE, "E-commerce / APIs / authentication"),
        ("hiba-logics", "2025-05 → 2025-06", "PHP Laravel Intern", "Hiba Logics", VIOLET, "Laravel / MVC / MySQL"),
    ]
    for slug, date, role, company, accent, focus in items:
        body = rect(1, 1, 1198, 177, "url(#base)", "#493455", 14)
        body += circle(39, 44, 5, accent)
        body += text(57, 50, date, 18, accent, mono=True)
        body += text(30, 109, role, 35, FG, bold=True)
        body += text(32, 147, company, 20, MUTED)
        body += line(644, 34, 644, 144, "#493455", 1)
        body += text(683, 72, "~/experience/" + slug, 17, accent, mono=True)
        body += text(683, 117, focus, 18, MUTED)
        (OUT / f"experience-{slug}.svg").write_text(svg(body, 1200, 179, f"{role} at {company}", date, accent))
        mobile = rect(1, 1, 638, 218, "url(#base)", "#493455", 14)
        mobile += circle(29, 36, 4, accent)
        mobile += text(47, 42, date, 18, accent, mono=True)
        mobile += text(24, 103, role, 34, FG, bold=True)
        mobile += text(26, 144, company, 22, MUTED)
        mobile += line(26, 165, 610, 165, "#493455", 1)
        mobile += text(26, 197, focus, 17, accent, mono=True)
        (OUT / f"experience-{slug}-mobile.svg").write_text(svg(mobile, 640, 220, f"{role} at {company}", date, accent))


def footer_cards():
    for slug, title, subtitle, accent in (
        ("portfolio", "Portfolio ↗", "Explore the work", ORANGE),
        ("linkedin", "LinkedIn ↗", "Connect with me", CYAN),
        ("email", "Email ↗", "Let's build something useful", VIOLET),
    ):
        body = rect(1, 1, 378, 113, "url(#base)", "#50385f", 12)
        body += rect(22, 25, 3, 65, accent, "none", 1)
        body += text(44, 51, title, 25, FG, bold=True)
        body += text(45, 81, subtitle, 15, MUTED)
        (OUT / f"contact-{slug}.svg").write_text(svg(body, 380, 115, title, subtitle, accent))


def ribbon():
    """Draw an original UI animation; never transform the AI-created hero."""
    fonts = {
        "mono": ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSansMono.ttf", 18),
        "small": ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSansMono.ttf", 14),
        "bold": ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", 19),
    }
    frames = []
    width, height = 1200, 86
    for frame in range(48):
        im = Image.new("RGB", (width, height), BG)
        d = ImageDraw.Draw(im)
        d.rounded_rectangle((1, 1, 1198, 84), 12, fill="#151021", outline="#503a64", width=1)
        d.text((24, 16), "~/building", font=fonts["small"], fill=VIOLET)
        d.text((24, 42), "Systems that think. Interfaces that work.", font=fonts["bold"], fill=FG)
        for i in range(48):
            phase = 2 * pi * (i / 16 - frame / 48)
            amplitude = (sin(phase) + 1) / 2
            h = round(7 + amplitude * 25)
            x = 714 + i * 7
            d.rounded_rectangle((x, 45 - h // 2, x + 3, 45 + h // 2), 1,
                                fill=CYAN if i % 3 else VIOLET)
        d.text((1080, 34), "CREATE", font=fonts["small"], fill=ORANGE)
        frames.append(im)
    still = frames[0]
    still.save(OUT / "building-static.png")
    # A single palette keeps the animation steady, with no color flicker.
    palette = still.quantize(colors=128)
    indexed = [im.quantize(palette=palette, dither=Image.Dither.NONE) for im in frames]
    indexed[0].save(OUT / "building.gif", save_all=True, append_images=indexed[1:],
                    duration=80, loop=0, optimize=True, disposal=1)
    mobile_frames = []
    for frame in range(48):
        im = Image.new("RGB", (640, 122), BG)
        d = ImageDraw.Draw(im)
        d.rounded_rectangle((1, 1, 638, 120), 12, fill="#151021", outline="#503a64", width=1)
        d.text((22, 12), "~/building", font=fonts["small"], fill=VIOLET)
        d.text((22, 37), "Systems that think. Interfaces that work.", font=fonts["bold"], fill=FG)
        for i in range(48):
            amplitude = (sin(2 * pi * (i / 16 - frame / 48)) + 1) / 2
            h = round(7 + amplitude * 22)
            x = 23 + i * 12
            d.rounded_rectangle((x, 93 - h // 2, x + 4, 93 + h // 2), 1,
                                fill=CYAN if i % 3 else VIOLET)
        mobile_frames.append(im)
    mobile_frames[0].save(OUT / "building-mobile-static.png")
    palette = mobile_frames[0].quantize(colors=128)
    indexed = [im.quantize(palette=palette, dither=Image.Dither.NONE) for im in mobile_frames]
    indexed[0].save(OUT / "building-mobile.gif", save_all=True, append_images=indexed[1:],
                    duration=80, loop=0, optimize=True, disposal=1)


def main():
    OUT.mkdir(parents=True, exist_ok=True)
    project_cards()
    section_headers()
    group_headers()
    experience_cards()
    footer_cards()
    ribbon()
    print("Generated animated/static project banners for desktop/mobile, section and stack headers, 4 experience banners, contact cards, and an animated ribbon.")


if __name__ == "__main__":
    main()
