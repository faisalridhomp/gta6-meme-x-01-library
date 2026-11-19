#!/usr/bin/env python3
"""Build the GTA 6 meme for make.fun bounty gta6-meme-x-01.

A Leonida Public Library overdue notice, composited with PIL so every word
is spelled correctly and stays readable at 480 px (the size the judge sees).
The make.fun ghost is the REAL press-kit mark (mark-1024.png), placed as a
round magenta wax seal overlapping the notice's bottom-right edge, like a
library seal stamped on the document -- in the scene, not a flat corner
sticker. Background is an AI-generated warm library desk (no text in it).
"""
import math
from PIL import Image, ImageDraw, ImageFont, ImageFilter

BASE = "/home/hatch/workspace/makefun/gta6-meme-x-01"
BG_PATH = f"{BASE}/assets/media-generation-gta6-meme-library-desk-0-9e32e45d-d251-4d9b-855d-627928d97e1b.png"
MARK_PATH = f"{BASE}/assets/mark-1024.png"
OUT_PATH = f"{BASE}/meme.png"
PREVIEW_PATH = f"{BASE}/meme-480.png"

SERIF_B = "/usr/share/fonts/truetype/liberation/LiberationSerif-Bold.ttf"
SANS_B = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"
MONO = "/usr/share/fonts/truetype/liberation/LiberationMono-Regular.ttf"
MONO_B = "/usr/share/fonts/truetype/liberation/LiberationMono-Bold.ttf"

CANVAS = 1024
INK = (32, 28, 24)          # near-black warm ink
RED = (178, 24, 24)         # stamp red
PAPER = (247, 241, 222)     # cream paper
PAPER_EDGE = (214, 200, 164)

def font(path, size):
    return ImageFont.truetype(path, size)

def tracked(draw, xy, text, fnt, fill, tracking=4):
    """Draw text with letter tracking; returns width used."""
    x, y = xy
    for ch in text:
        draw.text((x, y), ch, font=fnt, fill=fill)
        x += draw.textlength(ch, font=fnt) + tracking
    return x

def center(draw, y, text, fnt, fill, cx, tracking=0):
    w = sum(draw.textlength(c, font=fnt) + tracking for c in text) - tracking
    x = cx - w / 2
    if tracking:
        tracked(draw, (x, y), text, fnt, fill, tracking)
    else:
        draw.text((x, y), text, font=fnt, fill=fill)
    return w

def main():
    bg = Image.open(BG_PATH).convert("RGB")
    # center-crop to square, then to canvas size
    w, h = bg.size
    side = min(w, h)
    bg = bg.crop(((w - side) // 2, (h - side) // 2,
                  (w + side) // 2, (h + side) // 2)).resize((CANVAS, CANVAS), Image.LANCZOS)
    # slightly darken edges so the paper pops
    overlay = Image.new("RGB", (CANVAS, CANVAS), (0, 0, 0))
    mask = Image.new("L", (CANVAS, CANVAS), 0)
    md = ImageDraw.Draw(mask)
    md.rectangle([0, 0, CANVAS, CANVAS], fill=0)
    bg = Image.composite(Image.blend(bg, overlay, 0.08), bg, mask)

    # ---- paper layer (drawn flat, then rotated as one sheet) ----
    PW, PH = 800, 940
    paper = Image.new("RGBA", (PW + 80, PH + 80), (0, 0, 0, 0))
    d = ImageDraw.Draw(paper)
    OX, OY = 40, 40  # paper origin inside the layer
    d.rounded_rectangle([OX, OY, OX + PW, OY + PH], radius=6,
                        fill=PAPER + (255,), outline=PAPER_EDGE + (255,), width=2)
    # faint inner border
    d.rounded_rectangle([OX + 18, OY + 18, OX + PW - 18, OY + PH - 18], radius=4,
                        outline=(190, 175, 140, 255), width=1)

    cx = OX + PW // 2
    y = OY + 42
    center(d, y, "LEONIDA PUBLIC LIBRARY", font(SERIF_B, 34), INK, cx, tracking=5)
    y += 52
    center(d, y, "OVERDUE NOTICE", font(SANS_B, 66), RED, cx)
    y += 88
    d.line([(OX + 60, y), (OX + PW - 60, y)], fill=INK + (255,), width=3)
    y += 34
    center(d, y, "ITEM", font(MONO, 26), (110, 100, 88), cx)
    y += 34
    center(d, y, "GRAND THEFT AUTO VI", font(SANS_B, 50), INK, cx)
    y += 78
    center(d, y, "RESERVED: 17 SEP 2013", font(MONO, 34), INK, cx)
    y += 48
    center(d, y, "DAYS OVERDUE: 4,811", font(MONO_B, 40), INK, cx)
    y += 66
    fines = [
        ("WAITING", "13 YEARS"),
        ("TRAILER REWATCHES", "1,337"),
        ("DELAYS SURVIVED", "2"),
    ]
    for label, value in fines:
        lx = OX + 90
        d.text((lx, y), label, font=font(MONO, 30), fill=INK)
        vw = d.textlength(value, font=font(MONO_B, 30))
        d.text((OX + PW - 90 - vw, y), value, font=font(MONO_B, 30), fill=INK)
        # dotted leader between label and value
        lx_end = lx + d.textlength(label, font=font(MONO, 30)) + 12
        rx = OX + PW - 90 - vw - 12
        x = lx_end
        while x < rx - 6:
            d.ellipse([x, y + 22, x + 3, y + 25], fill=(140, 130, 115, 255))
            x += 10
        y += 44
    y += 12
    d.line([(OX + 60, y), (OX + PW - 60, y)], fill=INK + (255,), width=3)
    y += 26
    center(d, y, "TOTAL DUE: $70.00", font(SANS_B, 54), INK, cx)

    # ---- red PAID stamp, rotated, stamped across the lower paper ----
    stamp = Image.new("RGBA", (500, 130), (0, 0, 0, 0))
    sd = ImageDraw.Draw(stamp)
    sd.rounded_rectangle([6, 6, 494, 124], radius=10,
                         outline=RED + (235,), width=6)
    sd.rounded_rectangle([16, 16, 484, 114], radius=8,
                         outline=RED + (235,), width=2)
    sd.text((250, 32), "PAID IN FULL", font=font(SANS_B, 54),
            fill=RED + (235,), anchor="ma")
    stamp = stamp.rotate(-9, expand=True, resample=Image.BICUBIC)
    paper.alpha_composite(stamp, (OX + (PW - stamp.width) // 2, OY + 648))

    # paid-by line under the stamp
    center(d, OY + 880, "Paid by my AI agent earning on make.fun",
           font(SANS_B, 24), RED, cx - 30)

    # rotate the whole sheet slightly and paste with a soft shadow
    paper_rot = paper.rotate(-1.5, expand=True, resample=Image.BICUBIC)
    shadow = Image.new("RGBA", (CANVAS, CANVAS), (0, 0, 0, 0))
    sh = Image.new("RGBA", paper_rot.size, (0, 0, 0, 0))
    shd = ImageDraw.Draw(sh)
    shd.rounded_rectangle([10, 14, paper_rot.width - 4, paper_rot.height - 4],
                          radius=8, fill=(0, 0, 0, 110))
    sh = sh.filter(ImageFilter.GaussianBlur(14))
    px = (CANVAS - paper_rot.width) // 2
    py = (CANVAS - paper_rot.height) // 2 - 8
    shadow.alpha_composite(sh, (px, py))
    out = bg.convert("RGBA")
    out.alpha_composite(shadow)
    out.alpha_composite(paper_rot, (px, py))

    # ---- make.fun mark as a wax seal on the notice's bottom-right edge ----
    mark = Image.open(MARK_PATH).convert("RGBA")
    mark = mark.resize((200, 200), Image.LANCZOS)
    mark = mark.rotate(10, expand=True, resample=Image.BICUBIC)
    mshadow = Image.new("RGBA", (mark.width + 30, mark.height + 30), (0, 0, 0, 0))
    md2 = ImageDraw.Draw(mshadow)
    md2.ellipse([18, 20, mark.width + 12, mark.height + 12], fill=(0, 0, 0, 110))
    mshadow = mshadow.filter(ImageFilter.GaussianBlur(8))
    mx, my = 790, 800  # overlaps the paper's bottom-right corner onto the desk
    out.alpha_composite(mshadow, (mx - 8, my - 6))
    out.alpha_composite(mark, (mx, my))

    out.convert("RGB").save(OUT_PATH, "PNG")
    out.convert("RGB").resize((480, 480), Image.LANCZOS).save(PREVIEW_PATH, "PNG")
    print("saved", OUT_PATH, "and", PREVIEW_PATH)

if __name__ == "__main__":
    main()
