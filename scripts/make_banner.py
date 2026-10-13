"""Draw the trial homepage banner as SVG: forested ridges, an Earth-observing
satellite, and an old-style Earth-system "wiring diagram" in the sky.

Writes images/banner-<palette>.svg. Output is deterministic (fixed random seed).

Note: images/banner-earth.svg (the banner in use) was hand-edited in Inkscape and
is the master copy. This script reproduces its layout closely, but don't rerun it
over that file; to change the diagram, splice diagram_svg() output into group g17.

The page shows the banner at full height and crops it left and right (css/style.css),
so the satellite and diagram sit near the horizontal middle, which stays visible on
phones.

Usage: python3 scripts/make_banner.py [output_dir]   (default: images/)
"""
import math
import os
import random
import sys

from config import IMAGES_DIR

WIDTH, HEIGHT = 3200, 320
SCALE_X = WIDTH / 1600          # ridge wave frequencies were tuned on a 1600-wide drawing
FONT = "Helvetica, Arial, sans-serif"

# Per palette: sky gradient (top, bottom), sun, back-to-front ridge colors,
# diagram ink, box fill, and satellite body / panel / imaging-beam colors.
PALETTES = {
    "boreal": {
        "sky": ("#e3efe9", "#f8f5ec"),
        "sun": "#f1e2b3",
        "ridges": ["#c9ded5", "#9cc5b7", "#649f92", "#346f66", "#16413e"],
        "ink": "#2f5f58", "text": "#1d433e", "box": "#f4f7f2",
        "sat_body": "#16413e", "sat_panel": "#649f92", "beam": "#f1e2b3",
    },
    "earth": {
        "sky": ("#f6e9dc", "#fbf6f0"),
        "sun": "#f3c995",
        "ridges": ["#efc9a1", "#e07a5f", "#8f2d3c", "#3d6f7d", "#12343b"],
        "ink": "#3d6f7d", "text": "#24515c", "box": "#fbf4ec",
        "sat_body": "#12343b", "sat_panel": "#3d6f7d", "beam": "#f3c995",
    },
}


# ---------- Ridges and trees ----------

def ridge_points(rng, base, amplitude, step=8):
    """Return (x, y) points of one ridge line.

    The ridge height is a sum of three sine waves with random phases:
    y(x) = base - sum_k a_k * sin(2*pi*f_k*x/W + phi_k)
    """
    waves = [(amplitude * w, f * SCALE_X, rng.uniform(0, 2 * math.pi))
             for w, f in ((0.6, rng.uniform(1.0, 1.8)),
                          (0.3, rng.uniform(3.0, 5.0)),
                          (0.1, rng.uniform(9.0, 14.0)))]
    pts = []
    for x in range(0, WIDTH + step, step):
        y = base - sum(a * math.sin(2 * math.pi * f * x / WIDTH + phi) for a, f, phi in waves)
        pts.append((x, y))
    return pts


def ridge_y(pts, x):
    """Linearly interpolate the ridge height at horizontal position x."""
    step = pts[1][0] - pts[0][0]
    i = min(int(x // step), len(pts) - 2)
    (x0, y0), (x1, y1) = pts[i], pts[i + 1]
    return y0 + (y1 - y0) * (x - x0) / (x1 - x0)


def conifer_path(x, y, h):
    """Return SVG path data for a three-tier conifer of height h standing at (x, y)."""
    w = h * 0.42
    d = []
    for top, bottom, width in ((0.0, 0.45, 0.55), (0.25, 0.75, 0.8), (0.5, 1.0, 1.0)):
        ty, by, half = y - h + top * h, y - h + bottom * h, w * width / 2
        d.append(f"M{x:.1f},{ty:.1f}L{x - half:.1f},{by:.1f}L{x + half:.1f},{by:.1f}Z")
    t = w * 0.06
    d.append(f"M{x - t:.1f},{y:.1f}L{x - t:.1f},{y - h * 0.05:.1f}L{x + t:.1f},{y - h * 0.05:.1f}L{x + t:.1f},{y:.1f}Z")
    return "".join(d)


def ridges_svg(rng, colors):
    """Return SVG for the layered ridges, with conifers on the three front ridges.

    Also returns the points of the middle forested ridge, where the satellite beam lands.
    """
    out, n, landing = [], len(colors), None
    for i, color in enumerate(colors):
        # Back ridges sit higher with bigger relief; front ridges are lower and gentler.
        base = 165 + i * 34
        amplitude = 50 - i * 8
        pts = ridge_points(rng, base, amplitude)
        path = f"M0,{HEIGHT} " + " ".join(f"L{x},{y:.1f}" for x, y in pts) + f" L{WIDTH},{HEIGHT} Z"
        out.append(f'<path d="{path}" fill="{color}"/>')
        if i >= n - 3:
            depth = i - (n - 3)                 # 0, 1, 2 from back to front
            trees, x = [], rng.uniform(0, 12)
            while x < WIDTH:
                h = rng.uniform(14, 26) * (1 + 0.7 * depth)
                trees.append(conifer_path(x, ridge_y(pts, x) + 2, h))
                x += rng.uniform(6, 22) * (1 + 0.5 * depth)
            out.append(f'<path d="{"".join(trees)}" fill="{color}"/>')
        if i == n - 3:
            landing = pts
    return "\n".join(out), landing


# ---------- Earth-system wiring diagram ----------

def wire(points, ink, start_arrow=False, end_arrow=True):
    """Return an SVG polyline through points, with optional arrowheads."""
    pts = " ".join(f"{x},{y}" for x, y in points)
    marks = (' marker-start="url(#arrow-rev)"' if start_arrow else "") + (' marker-end="url(#arrow)"' if end_arrow else "")
    return f'<polyline points="{pts}" fill="none" stroke="{ink}" stroke-width="1.5"{marks}/>'


def box(x, y, w, h, label, ink, text, fill):
    """Return an SVG pool box with a centered, bold uppercase label."""
    return (f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="3" fill="{fill}" fill-opacity="0.95" '
            f'stroke="{ink}" stroke-width="1.5"/>'
            f'<text x="{x + w / 2}" y="{y + h / 2 + 5.5}" text-anchor="middle" font-family="{FONT}" '
            f'font-size="16" font-weight="600" letter-spacing="1.2" fill="{text}">{label}</text>')


def flux_label(x, y, label, text, anchor="middle", bg=None, width=0):
    """Return an upright label for a flux wire; with bg, it sits on the wire over a gap."""
    gap = (f'<rect x="{x - width / 2}" y="{y - 12}" width="{width}" height="16" fill="{bg}"/>' if bg else "")
    return (gap + f'<text x="{x}" y="{y}" text-anchor="{anchor}" font-family="{FONT}" font-size="14" '
            f'fill="{text}">{label}</text>')


def frame(x, y, w, h, name, models, ink, text, fill, sky, anchor="start", label_w=0):
    """Return a dashed model frame with a legend such as "ESM · CESM / E3SM" sitting on its top edge."""
    lx = x + 12 if anchor == "start" else x + w - 12
    gx = lx - 4 if anchor == "start" else lx - label_w + 4
    return (f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="6" fill="{fill}" fill-opacity="0.35" '
            f'stroke="{ink}" stroke-width="1.3" stroke-dasharray="6 4"/>'
            f'<rect x="{gx}" y="{y - 9}" width="{label_w}" height="17" fill="{sky}"/>'
            f'<text x="{lx}" y="{y + 5}" text-anchor="{anchor}" font-family="{FONT}" font-size="14" '
            f'letter-spacing="1" fill="{text}"><tspan font-weight="700">{name}</tspan> · {models}</text>')


def diagram_svg(ink, text, fill, sky, x0, y0=0):
    """Return SVG for a small Earth-system diagram drawn like an electrical schematic.

    Boxes are pools (atmosphere, vegetation, soil, ocean, human systems). Dashed
    frames group them into the two model types that get coupled: an Earth system
    model (ESM) and an integrated assessment model (IAM). Wires are fluxes, drawn
    with circuit conventions: right-angle wires, junction dots and arrowheads, the
    sun as the power source, a resistor on the litter flux, and an electrical
    ground symbol for the respiration sink under the soil.
    (x0, y0) is the top-left corner; the diagram is about 740 x 115 units.
    """
    g = [f'<g transform="translate({x0},{y0})">']
    # Model frames, drawn first so wires and boxes sit on top
    g.append(frame(70, 16, 420, 90, "ESM", "CESM / E3SM", ink, text, fill, sky, anchor="end", label_w=178))
    g.append(frame(530, 16, 210, 90, "IAM", "GCAM", ink, text, fill, sky, label_w=104))
    # Pools
    g += [box(88, 26, 156, 28, "ATMOSPHERE", ink, text, fill),
          box(88, 70, 156, 28, "VEGETATION", ink, text, fill),
          box(330, 26, 140, 28, "OCEAN", ink, text, fill),
          box(330, 70, 140, 28, "SOIL", ink, text, fill),
          box(545, 48, 180, 28, "HUMAN SYSTEMS", ink, text, fill)]
    # Sun as the source, outside the models, feeding atmosphere and vegetation through a junction
    g.append(f'<circle cx="20" cy="62" r="17" fill="{fill}" stroke="{ink}" stroke-width="1.5"/>'
             f'<text x="20" y="66.5" text-anchor="middle" font-family="{FONT}" font-size="12" '
             f'font-weight="600" letter-spacing="0.5" fill="{text}">SUN</text>')
    g.append(wire([(37, 62), (54, 62), (54, 40), (88, 40)], ink))
    g.append(wire([(54, 62), (54, 84), (88, 84)], ink))
    # Atmosphere <-> vegetation carbon exchange
    g.append(wire([(166, 54), (166, 70)], ink, start_arrow=True))
    g.append(flux_label(176, 67, "CO₂", text, anchor="start"))
    # Atmosphere -> ocean heat
    g.append(wire([(244, 40), (330, 40)], ink))
    g.append(flux_label(287, 35, "heat", text))
    # Vegetation -> soil litter, through a resistor (decomposition)
    zig = [(244, 84), (274, 84), (277, 78), (282, 90), (287, 78), (292, 90), (297, 78), (300, 84), (330, 84)]
    g.append(wire(zig, ink))
    g.append(flux_label(287, 74, "litter", text))
    # ESM -> IAM coupling: ocean and soil feed human systems (food, water)
    g.append(wire([(470, 40), (510, 40), (510, 62), (545, 62)], ink))
    g.append(wire([(470, 84), (510, 84), (510, 62)], ink, end_arrow=False))
    g.append(flux_label(547, 42, "food, water", text, anchor="start"))
    # IAM -> ESM coupling: emissions back to the atmosphere, over the top of both frames
    g.append(wire([(710, 48), (710, 6), (225, 6), (225, 26)], ink))
    g.append(flux_label(262, 11, "emissions", text, bg=sky, width=70))   # left end, clear of the ESM legend
    # Junction dots
    for x, y in ((54, 62), (510, 62)):
        g.append(f'<circle cx="{x}" cy="{y}" r="2.8" fill="{ink}"/>')
    # Ground symbol under the soil: the respiration / heat sink
    g.append(f'<path d="M400,98 V106 M387,106 H413 M392,110.5 H408 M397,115 H403" '
             f'stroke="{ink}" stroke-width="1.5" fill="none"/>')
    g.append("</g>")
    return "".join(g)


# ---------- Satellite ----------

def satellite_svg(cx, cy, angle, p, landing):
    """Return SVG for a small Earth-observing satellite at (cx, cy), tilted by `angle`
    degrees, with its imaging swath falling onto the forest (the `landing` ridge)."""
    # The sensor tip sits 16 units below the body centre, rotated with the satellite:
    # (sx, sy) = (cx - 16*sin(a), cy + 16*cos(a))
    a = math.radians(angle)
    sx, sy = cx - 16 * math.sin(a), cy + 16 * math.cos(a)
    left, right = sx - 95, sx + 95
    gy_l, gy_r = ridge_y(landing, left), ridge_y(landing, right)
    out = [
        # Imaging swath from the sensor down to the forest
        f'<polygon points="{sx:.1f},{sy:.1f} {left:.1f},{gy_l:.1f} {right:.1f},{gy_r:.1f}" fill="{p["beam"]}" opacity="0.45"/>',
        f'<polyline points="{left:.1f},{gy_l:.1f} {sx:.1f},{sy:.1f} {right:.1f},{gy_r:.1f}" fill="none" '
        f'stroke="{p["sat_body"]}" stroke-width="1" stroke-dasharray="3 4" opacity="0.55"/>',
        # The satellite: body, solar panels on an arm, sensor and antenna
        f'<g transform="translate({cx},{cy}) rotate({angle})">',
        f'<line x1="-46" y1="0" x2="46" y2="0" stroke="{p["sat_body"]}" stroke-width="2.2"/>',
    ]
    for px in (-80, 46):
        out.append(f'<rect x="{px}" y="-10" width="34" height="20" fill="{p["sat_panel"]}" '
                   f'stroke="{p["sat_body"]}" stroke-width="1"/>')
        out.append(f'<path d="M{px + 11.3},-10 V10 M{px + 22.7},-10 V10 M{px},0 H{px + 34}" '
                   f'stroke="{p["sky"][1]}" stroke-width="0.9" opacity="0.8"/>')
    out += [
        f'<rect x="-13" y="-12" width="26" height="24" rx="2.5" fill="{p["sat_body"]}"/>',
        f'<polygon points="-6,12 6,12 3.5,18 -3.5,18" fill="{p["sat_body"]}"/>',
        f'<line x1="0" y1="-12" x2="0" y2="-20" stroke="{p["sat_body"]}" stroke-width="1.6"/>',
        f'<circle cx="0" cy="-22" r="3" fill="{p["sat_body"]}"/>',
        "</g>",
    ]
    return "\n".join(out)


# ---------- Whole banner ----------

def banner_svg(p, seed=7):
    """Return the full SVG document for one palette."""
    rng = random.Random(seed)
    top, bottom = p["sky"]
    ink = p["ink"]
    sat_x, sat_y, sat_angle = 2286, 28, 25.7   # where the user placed it in Inkscape
    out = [
        f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {WIDTH} {HEIGHT}">',
        "<defs>",
        f'<linearGradient id="sky" x1="0.478" y1="0.646" x2="-0.478" y2="0.354"><stop offset="0" stop-color="{top}"/>'
        f'<stop offset="1" stop-color="{bottom}"/></linearGradient>',
        f'<marker id="arrow" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="5" markerHeight="5" orient="auto">'
        f'<path d="M0,0 L10,5 L0,10 z" fill="{ink}"/></marker>',
        f'<marker id="arrow-rev" viewBox="0 0 10 10" refX="1" refY="5" markerWidth="5" markerHeight="5" orient="auto">'
        f'<path d="M10,0 L0,5 L10,10 z" fill="{ink}"/></marker>',
        "</defs>",
        f'<rect width="{WIDTH}" height="{HEIGHT}" fill="url(#sky)"/>',
        f'<circle cx="1353" cy="46" r="46" fill="{p["sun"]}" opacity="0.85"/>',
        # Dashed orbit; the quadratic curve passes near the satellite at its midpoint:
        # B(0.5) = 0.25*P0 + 0.5*P1 + 0.25*P2
        f'<path d="M1300,150 Q1850,-39 2600,120" fill="none" stroke="{ink}" stroke-width="1.2" '
        f'stroke-dasharray="2 6" opacity="0.5"/>',
        diagram_svg(ink, p["text"], p["box"], p["sky"][1], x0=1435, y0=28),
    ]
    ridges, landing = ridges_svg(rng, p["ridges"])
    out.append(ridges)
    out.append(satellite_svg(sat_x, sat_y, sat_angle, p, landing))
    out.append("</svg>")
    return "\n".join(out)


def main(out_dir):
    """Write banner-<palette>.svg for every palette into out_dir (atomic write per file)."""
    for name, palette in PALETTES.items():
        path = os.path.join(out_dir, f"banner-{name}.svg")
        tmp = path + ".tmp"
        with open(tmp, "w", encoding="utf-8") as f:
            f.write(banner_svg(palette))
        os.replace(tmp, path)
        print(f"wrote {path} ({os.path.getsize(path) // 1024} KB)")


if __name__ == "__main__":
    main(sys.argv[1] if len(sys.argv) > 1 else str(IMAGES_DIR))
