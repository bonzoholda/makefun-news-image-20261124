#!/usr/bin/env python3
"""Draw the front page for the make.fun news-image-20261124 entry.

One image, 1024x1024 PNG, summing up Tuesday 24 November 2026 in the
style of a newspaper front page: masthead, one lead story (COP31) with a
large drawn visual, and four secondary stories with small drawn icons.
All five stories and every fact below were verified against news sources
on 25 Nov 2026 (see ../cuan-team/research/news-image-20261124-story-lock.md).

Deterministic: no randomness, no timestamps, no network. Running this
script twice produces byte-identical output.
"""

import os
from PIL import Image, ImageDraw, ImageFont

W, H = 1024, 1024
PAPER = (250, 246, 236)      # warm newsprint
INK = (17, 17, 17)
RED = (179, 38, 30)
GRAY = (90, 90, 90)
BLUE = (28, 68, 110)
TEAL = (31, 120, 110)
GREEN = (27, 120, 60)
GOLD = (176, 132, 30)
LIGHT = (238, 232, 218)

FONT_DIR = "/usr/share/fonts/truetype/dejavu"
SERIF = os.path.join(FONT_DIR, "DejaVuSerif.ttf")
SERIF_B = os.path.join(FONT_DIR, "DejaVuSerif-Bold.ttf")
SANS = os.path.join(FONT_DIR, "DejaVuSans.ttf")
SANS_B = os.path.join(FONT_DIR, "DejaVuSans-Bold.ttf")


def font(path, size):
    return ImageFont.truetype(path, size)


def wrap(draw, text, fnt, max_w):
    """Greedy word wrap; returns list of lines that fit max_w."""
    words = text.split()
    lines, cur = [], ""
    for w in words:
        trial = (cur + " " + w).strip()
        if draw.textlength(trial, font=fnt) <= max_w:
            cur = trial
        else:
            if cur:
                lines.append(cur)
            cur = w
    if cur:
        lines.append(cur)
    return lines


def draw_lines(draw, lines, x, y, fnt, fill=INK, leading=None):
    if leading is None:
        leading = int(fnt.size * 1.28)
    for line in lines:
        draw.text((x, y), line, font=fnt, fill=fill)
        y += leading
    return y


def rule(draw, x0, y, x1, width=2, fill=INK):
    draw.line([(x0, y), (x1, y)], fill=fill, width=width)


def draw_globe(draw, cx, cy, r):
    """Earth with a jagged crack: the lead visual for COP31."""
    draw.ellipse([cx - r, cy - r, cx + r, cy + r], fill=BLUE, outline=INK, width=3)
    # latitude lines
    for dy, w in ((-r * 0.55, 0.82), (-r * 0.2, 0.97), (r * 0.2, 0.97), (r * 0.55, 0.82)):
        half = int(r * w)
        draw.arc([cx - half, cy + dy - r * 0.28, cx + half, cy + dy + r * 0.28],
                 200, 340, fill=(120, 170, 210), width=2)
    # simple continents (abstract blobs)
    draw.ellipse([cx - r * 0.62, cy - r * 0.55, cx - r * 0.05, cy - r * 0.05],
                 fill=TEAL)
    draw.ellipse([cx + r * 0.05, cy + r * 0.15, cx + r * 0.60, cy + r * 0.62],
                 fill=TEAL)
    # jagged crack across the globe, in paper colour with dark edge
    crack = [(cx - r * 0.75, cy - r * 0.62), (cx - r * 0.45, cy - r * 0.30),
             (cx - r * 0.55, cy - r * 0.05), (cx - r * 0.15, cy + r * 0.12),
             (cx - r * 0.30, cy + r * 0.38), (cx + r * 0.05, cy + r * 0.55),
             (cx - r * 0.05, cy + r * 0.78), (cx + r * 0.35, cy + r * 0.95)]
    draw.line(crack, fill=PAPER, width=7, joint="curve")
    draw.line(crack, fill=INK, width=1, joint="curve")


def icon_ship(draw, x, y, s):
    """Corvette on waves with a small drone above."""
    # drone (enlarged so it reads at a glance)
    draw.ellipse([x + s * 0.60, y + s * 0.04, x + s * 0.76, y + s * 0.20], fill=INK)
    for dx in (0.48, 0.82):
        draw.line([(x + s * dx, y + s * 0.12), (x + s * dx + s * 0.14, y + s * 0.12)],
                  fill=INK, width=4)
    # hull
    draw.polygon([(x + s * 0.08, y + s * 0.52), (x + s * 0.92, y + s * 0.52),
                  (x + s * 0.78, y + s * 0.72), (x + s * 0.22, y + s * 0.72)],
                 fill=INK)
    draw.rectangle([x + s * 0.38, y + s * 0.36, x + s * 0.56, y + s * 0.52], fill=INK)
    # waves
    for wy in (0.80, 0.90):
        draw.arc([x + s * 0.05, y + s * wy, x + s * 0.48, y + s * (wy + 0.14)],
                 180, 360, fill=BLUE, width=3)
        draw.arc([x + s * 0.52, y + s * wy, x + s * 0.95, y + s * (wy + 0.14)],
                 180, 360, fill=BLUE, width=3)


def icon_chip(draw, x, y, s):
    """Microchip with a rising arrow and +30%."""
    draw.rectangle([x + s * 0.24, y + s * 0.30, x + s * 0.66, y + s * 0.72],
                   fill=GREEN, outline=INK, width=2)
    draw.rectangle([x + s * 0.38, y + s * 0.44, x + s * 0.52, y + s * 0.58],
                   fill=PAPER)
    for px in (0.30, 0.45, 0.60):
        draw.line([(x + s * px, y + s * 0.18), (x + s * px, y + s * 0.30)],
                  fill=INK, width=3)
        draw.line([(x + s * px, y + s * 0.72), (x + s * px, y + s * 0.84)],
                  fill=INK, width=3)
    # rising arrow
    draw.line([(x + s * 0.68, y + s * 0.52), (x + s * 0.88, y + s * 0.28)],
              fill=RED, width=5)
    draw.polygon([(x + s * 0.88, y + s * 0.28), (x + s * 0.76, y + s * 0.26),
                  (x + s * 0.88, y + s * 0.40)], fill=RED)
    f = font(SANS_B, int(s * 0.20))
    draw.text((x + s * 0.06, y + s * 0.02), "+30%", font=f, fill=RED)


def icon_kyiv(draw, x, y, s):
    """City skyline with a burst above it."""
    heights = [0.42, 0.60, 0.50, 0.68, 0.46]
    bw = s * 0.18
    for i, hh in enumerate(heights):
        bx = x + s * 0.03 + i * bw
        draw.rectangle([bx, y + s * (0.92 - hh), bx + bw * 0.9, y + s * 0.92],
                       fill=INK)
    # burst
    cx, cy = x + s * 0.72, y + s * 0.24
    for ang in range(0, 360, 30):
        import math
        r1, r2 = s * 0.08, s * 0.20
        a = math.radians(ang)
        draw.line([(cx + r1 * math.cos(a), cy + r1 * math.sin(a)),
                   (cx + r2 * math.cos(a), cy + r2 * math.sin(a))],
                  fill=RED, width=4)
    draw.ellipse([cx - s * 0.07, cy - s * 0.07, cx + s * 0.07, cy + s * 0.07],
                 fill=RED)


def icon_capitol(draw, x, y, s):
    """US Capitol dome with a 259-seat badge."""
    # dome
    draw.pieslice([x + s * 0.28, y + s * 0.10, x + s * 0.72, y + s * 0.62],
                  180, 360, fill=INK)
    draw.rectangle([x + s * 0.46, y + s * 0.02, x + s * 0.54, y + s * 0.14], fill=INK)
    # base + columns
    draw.rectangle([x + s * 0.14, y + s * 0.60, x + s * 0.86, y + s * 0.68], fill=INK)
    for cx in (0.22, 0.38, 0.54, 0.70):
        draw.rectangle([x + s * cx, y + s * 0.68, x + s * (cx + 0.06), y + s * 0.86],
                       fill=INK)
    draw.rectangle([x + s * 0.10, y + s * 0.86, x + s * 0.90, y + s * 0.92], fill=INK)
    # badge
    draw.ellipse([x + s * 0.66, y + s * 0.06, x + s * 0.98, y + s * 0.38],
                 fill=RED, outline=PAPER, width=2)
    f = font(SANS_B, int(s * 0.13))
    tw = draw.textlength("259", font=f)
    draw.text((x + s * 0.82 - tw / 2, y + s * 0.15), "259", font=f, fill=(255, 255, 255))


def secondary(draw, x, y, w, icon, kicker, headline, deck):
    """One secondary story cell: icon left, text right."""
    s = 120
    icon(draw, x, y + 8, s)
    tx = x + s + 16
    tw = w - s - 16
    f_kick = font(SANS_B, 17)
    draw.text((tx, y + 4), kicker, font=f_kick, fill=RED)
    f_head = font(SERIF_B, 26)
    lines = wrap(draw, headline, f_head, tw)
    y2 = draw_lines(draw, lines[:2], tx, y + 28, f_head, leading=31)
    f_deck = font(SANS, 17)
    lines = wrap(draw, deck, f_deck, tw)
    draw_lines(draw, lines[:2], tx, y2 + 4, f_deck, fill=GRAY, leading=22)


def main():
    img = Image.new("RGB", (W, H), PAPER)
    d = ImageDraw.Draw(img)
    MX = 40  # margin
    RX = W - MX

    # ---- masthead ----
    rule(d, MX, 26, RX, 3)
    f_mast = font(SERIF_B, 82)
    title = "THE WORLD TODAY"
    tw = d.textlength(title, font=f_mast)
    d.text(((W - tw) / 2, 36), title, font=f_mast, fill=INK)
    rule(d, MX, 138, RX, 5)
    rule(d, MX, 146, RX, 1)
    f_date = font(SANS_B, 20)
    d.text((MX, 158), "TUESDAY, 24 NOVEMBER 2026", font=f_date, fill=INK)
    right = "WORLD NEWS  ·  ONE PAGE"
    tw = d.textlength(right, font=f_date)
    d.text((RX - tw, 158), right, font=f_date, fill=INK)

    # ---- lead story: COP31 ----
    y = 196
    f_kick = font(SANS_B, 20)
    d.text((MX, y), "CLIMATE  —  ANTALYA, TURKEY", font=f_kick, fill=RED)
    y += 30
    f_head = font(SERIF_B, 60)
    d.text((MX, y), "COP31 COLLAPSES", font=f_head, fill=INK)
    y += 68
    d.text((MX, y), "WITHOUT A DEAL", font=f_head, fill=INK)
    y += 78
    # left column: deck + body; right column: globe visual
    text_w = 560
    f_deck = font(SERIF, 25)
    deck = ("More than 90 nations reject a draft that never names "
            "fossil fuels — the first climate summit to end with "
            "no deal since 2009.")
    y2 = draw_lines(d, wrap(d, deck, f_deck, text_w), MX, y, f_deck, leading=32)
    f_body = font(SERIF, 19)
    body = ("Talks ran nearly 50 hours into overtime before delegates "
            "walked away from the Antalya Pact. The EU called the "
            "outcome “terrible”.")
    draw_lines(d, wrap(d, body, f_body, text_w), MX, y2 + 14, f_body,
               fill=GRAY, leading=25)
    draw_globe(d, 800, y + 112, 112)

    # ---- divider ----
    rule(d, MX, 600, RX, 3)

    # ---- secondary stories, 2 x 2 ----
    cell_w = (W - 2 * MX - 24) // 2
    cell_h = 158
    gx, gy = MX, 624
    secondary(d, gx, gy, cell_w, icon_ship,
              "CONFLICT — BENGHAZI, LIBYA",
              "Ukraine sinks Russian corvette off Libya",
              "Seven sea drones sank the Merkury and hit the cargo ship Angara; Italy voices concern.")
    secondary(d, gx + cell_w + 24, gy, cell_w, icon_chip,
              "MARKETS — SANTA CLARA",
              "Nvidia brings back Huang as CEO",
              "Board reinstates the founder 11 days after his exit; shares jump 30%.")
    secondary(d, gx, gy + cell_h + 14, cell_w, icon_kyiv,
              "WAR — KYIV",
              "Russia hits Kyiv as peace talks go on",
              "Missile and drone strikes kill at least two, ending a three-day pause.")
    secondary(d, gx + cell_w + 24, gy + cell_h + 14, cell_w, icon_capitol,
              "POLITICS — WASHINGTON",
              "Democrats clinch historic House majority",
              "At least 259 seats — the largest since 1992 — as voters sweep Congress.")

    # ---- footer ----
    rule(d, MX, 972, RX, 1)
    f_foot = font(SANS, 15)
    foot = "THE WORLD TODAY  ·  ALL FIVE STORIES FROM TUESDAY 24 NOVEMBER 2026  ·  DRAWN ENTIRELY IN CODE"
    tw = d.textlength(foot, font=f_foot)
    d.text(((W - tw) / 2, 982), foot, font=f_foot, fill=GRAY)

    out = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "entry.png")
    img.save(out, format="PNG", optimize=True)
    print("wrote", out, os.path.getsize(out), "bytes")


if __name__ == "__main__":
    main()
