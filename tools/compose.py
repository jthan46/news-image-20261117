#!/usr/bin/env python3
"""Compose the news-image-20261117 front page: one image summing up the world
news of Tuesday 17 November 2026.

Lays out a 1024x1024 newspaper-style front page with PIL: a masthead, a large
date banner, and six story panels (AI-generated editorial illustrations in
../assets) each with a kicker, a short factual headline and a one-line sub.
The result is written to ../entry.png as JPEG bytes (the gate accepts PNG or
JPEG by first bytes; the filename stays entry.png).
"""
from pathlib import Path
from PIL import Image, ImageDraw, ImageFont

ROOT = Path(__file__).resolve().parent.parent
ASSETS = ROOT / "assets"
OUT = ROOT / "entry.png"

W = H = 1024
PAPER = (246, 241, 231)
INK = (18, 28, 40)
RED = (176, 48, 40)
GOLD = (216, 164, 65)
GREY = (84, 90, 98)
WHITE = (250, 248, 243)

SERIF_B = "/usr/share/fonts/truetype/dejavu/DejaVuSerif-Bold.ttf"
SANS_B = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"
SANS = "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"


def font(path, size):
    return ImageFont.truetype(path, size)


def text_w(draw, s, f):
    return draw.textlength(s, font=f)


def draw_tracked(draw, xy, s, f, fill, tracking=3):
    """Draw text with simple letter tracking, left-aligned at xy."""
    x, y = xy
    for ch in s:
        draw.text((x, y), ch, font=f, fill=fill)
        x += text_w(draw, ch, f) + tracking
    return x - tracking


def tracked_w(draw, s, f, tracking=3):
    return sum(text_w(draw, ch, f) for ch in s) + tracking * (len(s) - 1)


def draw_centered(draw, cx, y, s, f, fill):
    draw.text((cx - text_w(draw, s, f) / 2, y), s, font=f, fill=fill)


def wrap(draw, s, f, max_w):
    words, lines, cur = s.split(), [], ""
    for wd in words:
        trial = f"{cur} {wd}".strip()
        if text_w(draw, trial, f) <= max_w:
            cur = trial
        else:
            lines.append(cur)
            cur = wd
    if cur:
        lines.append(cur)
    return lines


def cover_crop(img, box_w, box_h, focus_y=0.5):
    """Resize/crop img to exactly box_w x box_h (cover), focus_y 0=top..1=bottom."""
    sw, sh = img.size
    scale = max(box_w / sw, box_h / sh)
    nw, nh = round(sw * scale), round(sh * scale)
    img = img.resize((nw, nh), Image.LANCZOS)
    x = (nw - box_w) // 2
    y = int((nh - box_h) * focus_y)
    return img.crop((x, y, x + box_w, y + box_h))


# kicker, headline, sub, asset file, crop focus_y
PANELS = [
    ("UKRAINE · WAR",
     "Kerch Bridge to Crimea partly collapses in Ukraine strike",
     "Zelenskyy hails the 'unprecedented' attack",
     "panel-bridge.webp", 0.45),
    ("THE GULF · IRAN",
     "Iran strikes US base in Bahrain for third time in days",
     "US confirms a retaliatory strike on Qeshm Island",
     "panel-gulf.webp", 0.35),
    ("ASIA · SUMMIT DIPLOMACY",
     "Trump in Asia ahead of talks with Xi and Putin",
     "Three leaders set to meet at APEC in Shenzhen",
     "panel-summit.webp", 0.40),
    ("UNITED STATES · HEALTH",
     "US loses measles-free status after 26 years",
     "Over 5,400 cases this year — a 40-year high",
     "panel-measles.webp", 0.28),
    ("FRANCE · STRIKES",
     "146,000 march as France strikes over cost of living",
     "Second nationwide walkout called by the unions",
     "panel-france.webp", 0.55),
    ("GAZA · AID",
     "Four nations urge Israel to open Gaza aid crossings",
     "Joint call as agencies warn of a winter emergency",
     "panel-gaza.webp", 0.55),
]


def main():
    img = Image.new("RGB", (W, H), PAPER)
    d = ImageDraw.Draw(img)

    # outer frame
    d.rectangle([10, 10, W - 11, H - 11], outline=INK, width=3)
    d.rectangle([18, 18, W - 19, H - 19], outline=INK, width=1)

    M = 30  # inner margin

    # --- masthead ---
    tag_f = font(SANS_B, 15)
    tag = "THE WORLD'S NEWS · ONE DAY · ONE IMAGE"
    draw_tracked(d, ((W - tracked_w(d, tag, tag_f)) / 2, 30), tag, tag_f, RED)
    title_f = font(SERIF_B, 57)
    draw_centered(d, W / 2, 54, "THE WORLD IN ONE IMAGE", title_f, INK)
    d.line([M, 126, W - M, 126], fill=INK, width=3)
    d.line([M, 131, W - M, 131], fill=INK, width=1)

    # --- date banner ---
    band_y0, band_y1 = 142, 206
    d.rectangle([M, band_y0, W - M, band_y1], fill=INK)
    date_f = font(SANS_B, 41)
    draw_centered(d, W / 2, band_y0 + 11, "TUESDAY · 17 NOVEMBER 2026", date_f, GOLD)

    # --- panels: 2 cols x 3 rows ---
    grid_top = 216
    col_gap = 14
    col_w = (W - 2 * M - col_gap) // 2          # 475
    img_h = 136
    row_pitch = 250                              # image + caption + gap
    kick_f = font(SANS_B, 15)
    head_f = font(SANS_B, 25)
    sub_f = font(SANS, 17)

    for i, (kicker, head, sub, fname, fy) in enumerate(PANELS):
        col, row = i % 2, i // 2
        x = M + col * (col_w + col_gap)
        y = grid_top + row * row_pitch

        art = Image.open(ASSETS / fname).convert("RGB")
        img.paste(cover_crop(art, col_w, img_h, fy), (x, y))
        d.rectangle([x, y, x + col_w - 1, y + img_h - 1], outline=INK, width=2)

        cy = y + img_h + 5
        draw_tracked(d, (x + 1, cy), kicker, kick_f, RED, tracking=2)
        cy += 22
        for line in wrap(d, head, head_f, col_w - 2)[:2]:
            d.text((x + 1, cy), line, font=head_f, fill=INK)
            cy += 29
        d.text((x + 1, cy + 2), sub, font=sub_f, fill=GREY)

    # --- footer ---
    foot_f = font(SANS, 15)
    d.line([M, 974, W - M, 974], fill=INK, width=1)
    draw_centered(d, W / 2, 984,
                  "As reported 17 Nov 2026 · BBC · PBS NewsHour · Daily Baku · Asas Press",
                  foot_f, GREY)

    img.save(OUT, format="JPEG", quality=90)
    print(f"wrote {OUT} ({OUT.stat().st_size} bytes)")


if __name__ == "__main__":
    main()
