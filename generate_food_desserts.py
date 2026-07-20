import os
import numpy as np
from PIL import Image, ImageDraw

OUTPUT_DIR = "images/food_desserts"
os.makedirs(OUTPUT_DIR, exist_ok=True)

def save_sprite(name, draw_fn):
    """Draw, outline, quantize, and save a 50x50 sprite."""
    img = Image.new("RGBA", (50, 50), (0, 0, 0, 0))
    d   = ImageDraw.Draw(img)
    draw_fn(d)
    
    # Apply automatic thick outlines and quantize
    img = _apply_outline_and_quantize(img)
    
    path = os.path.join(OUTPUT_DIR, f"{name}_50x50.png")
    img.save(path)
    
    # Print color count to verify
    arr = np.array(img)
    colors = len({tuple(arr[y, x]) for y in range(50) for x in range(50) if arr[y, x, 3] > 0})
    print(f"  Saved: {path} [{colors} colors]")

def _apply_outline_and_quantize(img: Image.Image) -> Image.Image:
    """Flatten → bevel shade → auto-outline (1px black border) → quantize to max 10 colors."""
    arr   = np.array(img.convert("RGBA"))
    alpha = arr[:, :, 3]
    mask  = alpha > 128

    h, w = mask.shape
    
    # 1. Bevel/Cell Shading for realistic detail on all flat shapes
    rgb = arr[:, :, :3].astype(float)
    shaded_rgb = rgb.copy()
    for y in range(h):
        for x in range(w):
            if not mask[y, x]: continue
            color = rgb[y, x]
            # Check neighborhood edges for highlighting and shadows
            top_diff = (y == 0) or np.any(rgb[y-1, x] != color)
            left_diff = (x == 0) or np.any(rgb[y, x-1] != color)
            bottom_diff = (y == h-1) or np.any(rgb[y+1, x] != color)
            right_diff = (x == w-1) or np.any(rgb[y, x+1] != color)
            
            base = color.copy()
            if top_diff and left_diff:
                base += 60 # Strong highlight
            elif top_diff or left_diff:
                base += 30 # Mild highlight
            elif bottom_diff and right_diff:
                base -= 60 # Strong shadow
            elif bottom_diff or right_diff:
                base -= 30 # Mild shadow
                
            shaded_rgb[y, x] = np.clip(base, 0, 255)

    # 2. Outline: any transparent pixel next to an opaque pixel gets black/charcoal
    outline = np.zeros((h, w), bool)
    for dy, dx in [(-1,0),(1,0),(0,-1),(0,1)]:
        shifted = np.roll(np.roll(mask, dy, 0), dx, 1)
        if dy ==  1: shifted[0,  :] = False
        if dy == -1: shifted[-1, :] = False
        if dx ==  1: shifted[:,  0] = False
        if dx == -1: shifted[:, -1] = False
        outline |= (~mask) & shifted

    shaded_rgb[outline] = [25, 25, 30] # Dark charcoal outline

    new_alpha = alpha.copy()
    new_alpha[outline] = 255

    # Paste onto a white background to clean it up
    flat = Image.new("RGB", (50, 50), (255, 255, 255))
    composed = Image.fromarray(
        np.dstack((shaded_rgb, new_alpha)).astype(np.uint8), "RGBA"
    )
    flat.paste(composed, mask=Image.fromarray(new_alpha, "L"))

    # Quantize to 9 colors (so total colors including transparent background is <= 10)
    q = flat.quantize(colors=9, method=Image.MEDIANCUT, dither=0)
    final = q.convert("RGBA")
    
    # Restore transparency
    final_arr = np.array(final)
    final_arr[new_alpha < 128] = [0, 0, 0, 0]
    
    return Image.fromarray(final_arr, "RGBA")

# Palettes
BK = (25, 25, 30, 255)
WH = (245, 245, 245, 255)
WHITE = WH
RED = (220, 45, 45, 255)
DRED = (150, 30, 30, 255)
YEL = (250, 215, 40, 255)
DYEL = (200, 160, 20, 255)
GRN = (50, 180, 65, 255)
DGRN = (30, 110, 40, 255)
BRN = (145, 90, 45, 255)
BROWN = BRN
DBRN = (85, 50, 25, 255)
LBRN = (215, 170, 115, 255)
CREAM = (245, 222, 179, 255)
ORNG = (240, 135, 25, 255)
PNK = (255, 150, 185, 255)
DPNK = (220, 100, 140, 255)
BLU = (40, 135, 225, 255)
LBLU = (165, 215, 250, 255)
PURP = (140, 80, 195, 255)
DGY = (100, 100, 100, 255)
SHD = (0, 0, 0, 80)

# 1-50: Existing Detailed Food Sprite Drawing Functions
def draw_pizza(d):
    d.polygon([(10, 12), (40, 12), (25, 44)], fill=YEL)
    d.polygon([(9, 11), (41, 11), (25, 45)], outline=DBRN, fill=BRN)
    d.rectangle([8, 8, 42, 12], fill=BRN)
    d.rectangle([12, 12, 38, 13], fill=DBRN)
    for cx, cy in [(18, 18), (32, 18), (25, 28), (20, 34), (30, 34)]:
        d.ellipse([cx-3, cy-3, cx+3, cy+3], fill=DRED)
        d.ellipse([cx-2, cy-2, cx+1, cy+1], fill=RED)
    d.line([(14,24), (17,27)], fill=GRN, width=2)
    d.line([(31,25), (34,28)], fill=GRN, width=2)
    d.line([(23,36), (26,38)], fill=GRN, width=2)

def draw_burger(d):
    d.ellipse([10, 31, 40, 43], fill=BRN)
    d.rectangle([10, 26, 40, 31], fill=DBRN)
    d.polygon([(10,26), (40,26), (36,29), (28,26), (20,29), (12,26)], fill=YEL)
    d.ellipse([9, 21, 41, 26], fill=GRN)
    for lx in range(12, 38, 5):
         d.rectangle([lx, 21, lx+3, 23], fill=DGRN)
    d.rectangle([11, 18, 39, 21], fill=RED)
    d.ellipse([10, 10, 40, 20], fill=BRN)
    d.rectangle([10, 15, 40, 20], fill=BRN)
    for sx, sy in [(15, 13), (25, 12), (35, 14), (20, 16), (30, 16)]:
        d.rectangle([sx, sy, sx+1, sy+1], fill=WH)

def draw_hotdog(d):
    d.ellipse([8, 16, 42, 36], fill=LBRN)
    d.ellipse([8, 20, 42, 22], fill=BRN)
    d.ellipse([6, 21, 44, 29], fill=RED)
    d.ellipse([6, 22, 9, 28], fill=DRED)
    d.ellipse([41, 22, 44, 28], fill=DRED)
    points = [(12,24), (16,28), (20,24), (24,28), (28,24), (32,28), (36,24), (40,27)]
    d.line(points, fill=YEL, width=2)

def draw_taco(d):
    d.ellipse([10, 15, 40, 39], fill=YEL)
    d.rectangle([10, 27, 40, 39], fill=(0,0,0,0))
    d.ellipse([10, 15, 40, 39], outline=DYEL, width=2)
    d.rectangle([13, 22, 20, 27], fill=DBRN)
    d.rectangle([28, 21, 35, 27], fill=DBRN)
    for gx in [15, 22, 29, 34]:
        d.ellipse([gx, 18, gx+4, 24], fill=GRN)
    d.rectangle([18, 17, 21, 20], fill=RED)
    d.rectangle([28, 17, 31, 20], fill=RED)
    d.line([(14,20),(16,23)], fill=YEL, width=1)
    d.line([(24,19),(26,22)], fill=YEL, width=1)
    d.line([(32,20),(34,23)], fill=YEL, width=1)

def draw_sushi(d):
    d.ellipse([12, 12, 38, 38], fill=BK)
    d.ellipse([14, 14, 36, 36], fill=WH)
    d.ellipse([16, 17, 18, 20], fill=LBLU)
    d.ellipse([32, 28, 34, 31], fill=LBLU)
    d.ellipse([18, 31, 20, 33], fill=LBLU)
    d.ellipse([19, 19, 31, 31], fill=ORNG)
    d.line([(21,21), (29,29)], fill=WH, width=1)
    d.rectangle([20, 24, 24, 28], fill=GRN)
    d.rectangle([21, 25, 23, 27], fill=DGRN)

def draw_fries(d):
    d.polygon([(13, 22), (37, 22), (32, 42), (18, 42)], fill=RED)
    d.polygon([(13, 22), (25, 26), (37, 22), (32, 42), (18, 42)], outline=DRED)
    d.polygon([(25,28), (23,34), (28,31), (22,31), (27,34)], fill=YEL)
    fries_coords = [
        (15, 10, 18, 26), (19, 8, 22, 26), (23, 11, 26, 26),
        (27, 7, 30, 26), (31, 9, 34, 26), (17, 14, 20, 26),
        (21, 13, 24, 26), (25, 14, 28, 26), (29, 12, 32, 26)
    ]
    for x0, y0, x1, y1 in fries_coords:
        d.rectangle([x0, y0, x1, y1], fill=YEL)
        d.rectangle([x0, y0, x0+1, y1], fill=DYEL)

def draw_cupcake(d):
    d.polygon([(14, 28), (36, 28), (31, 43), (19, 43)], fill=PNK)
    for x in range(16, 36, 4):
        d.line([(x, 28), (x - 2 + (x-25)//5, 43)], fill=DPNK, width=1)
    d.ellipse([11, 14, 39, 29], fill=WH)
    d.ellipse([14, 10, 36, 22], fill=WH)
    d.arc([14, 12, 36, 26], 45, 180, fill=DPNK, width=2)
    sprinkles = [(17, 17, RED), (31, 18, BLU), (22, 13, GRN), (28, 12, ORNG), (25, 20, YEL)]
    for sx, sy, col in sprinkles:
        d.rectangle([sx, sy, sx+1, sy+1], fill=col)
    d.ellipse([22, 4, 28, 10], fill=RED)
    d.line([(25, 4), (28, 0)], fill=BK, width=1)

def draw_icecream(d):
    d.polygon([(17, 26), (33, 26), (25, 46)], fill=LBRN)
    for i in range(18, 32, 3):
        d.line([(i, 26), (25 + (i-25)*0.5, 46)], fill=BRN)
    d.ellipse([13, 16, 37, 28], fill=DBRN)
    d.ellipse([15, 8, 35, 20], fill=PNK)
    d.ellipse([21, 12, 29, 18], fill=DBRN)
    d.ellipse([22, 2, 28, 8], fill=RED)

def draw_donut(d):
    d.ellipse([10, 10, 40, 40], fill=LBRN)
    d.ellipse([11, 11, 39, 39], fill=PNK)
    for cx, cy in [(14, 32), (25, 36), (34, 31), (36, 20), (13, 22)]:
        d.ellipse([cx-2, cy-2, cx+2, cy+2], fill=PNK)
    d.ellipse([19, 19, 31, 31], fill=(0,0,0,0))
    for sx, sy in [(15, 17), (32, 18), (25, 13), (29, 31), (18, 30), (14, 24), (35, 24)]:
        d.line([(sx, sy), (sx+2, sy+1)], fill=BLU, width=1)
        d.line([(sx-1, sy+3), (sx+1, sy+4)], fill=YEL, width=1)

def draw_cookie(d):
    d.ellipse([10, 10, 40, 40], fill=LBRN)
    d.arc([12, 12, 38, 38], 45, 135, fill=BRN, width=1)
    d.arc([15, 15, 35, 35], 220, 310, fill=BRN, width=1)
    chunks = [(16, 16), (28, 14), (24, 24), (15, 27), (33, 26), (24, 33)]
    for cx, cy in chunks:
        d.ellipse([cx-2, cy-2, cx+2, cy+2], fill=DBRN)
        d.point((cx-1, cy-1), fill=BRN)

def draw_pancakes(d):
    pancake_y = [29, 23, 17]
    for y in pancake_y:
        d.ellipse([11, y, 39, y+9], fill=LBRN)
        d.ellipse([11, y, 39, y+8], fill=CREAM)
        d.arc([11, y, 39, y+8], 0, 180, fill=BRN, width=1)
    d.polygon([(22, 17), (25, 38), (28, 17)], fill=BRN)
    d.polygon([(14, 23), (16, 32), (18, 23)], fill=BRN)
    d.rectangle([21, 13, 29, 19], fill=YEL)
    d.rectangle([21, 13, 23, 19], fill=WH)

def draw_waffle(d):
    d.rectangle([11, 11, 39, 39], fill=LBRN)
    d.rectangle([13, 13, 37, 37], fill=LBRN)
    for x in range(15, 38, 6):
        d.line([(x, 12), (x, 38)], fill=DBRN, width=1)
        d.line([(12, x), (38, x)], fill=DBRN, width=1)
    d.ellipse([16, 16, 22, 22], fill=CREAM)
    d.ellipse([18, 18, 20, 20], fill=YEL)
    d.polygon([(28, 14), (34, 14), (31, 22)], fill=RED)
    d.polygon([(29, 15), (33, 15), (31, 20)], fill=PNK)
    d.ellipse([21, 21, 29, 29], fill=WH)
    d.ellipse([23, 23, 27, 27], fill=LBLU)

def draw_cake(d):
    d.polygon([(10, 36), (40, 36), (25, 14)], fill=WHITE)
    d.polygon([(12, 34), (38, 34), (25, 16)], fill=DBRN)
    d.polygon([(14, 30), (36, 30), (25, 18)], fill=WH)
    d.polygon([(16, 27), (34, 27), (25, 20)], fill=RED)
    d.polygon([(18, 24), (32, 24), (25, 22)], fill=DBRN)
    d.ellipse([21, 6, 29, 14], fill=RED)
    d.line([(25, 6), (23, 4)], fill=GRN, width=2)
    d.line([(25, 6), (27, 4)], fill=GRN, width=2)

def draw_pie(d):
    d.ellipse([10, 16, 40, 38], fill=BRN)
    for angle in range(0, 360, 30):
        rad = np.deg2rad(angle)
        cx = int(25 + 15 * np.cos(rad))
        cy = int(27 + 11 * np.sin(rad))
        d.ellipse([cx-2, cy-2, cx+2, cy+2], fill=BRN)
    d.ellipse([13, 19, 37, 35], fill=RED)
    d.line([(17, 20), (31, 34)], fill=LBRN, width=2)
    d.line([(31, 20), (17, 34)], fill=LBRN, width=2)
    d.line([(21, 19), (21, 35)], fill=LBRN, width=2)
    d.line([(29, 19), (29, 35)], fill=LBRN, width=2)
    d.ellipse([24, 23, 27, 26], fill=DRED)
    d.ellipse([16, 26, 19, 29], fill=DRED)

def draw_croissant(d):
    d.ellipse([18, 14, 32, 36], fill=BRN)
    d.ellipse([12, 20, 24, 32], fill=BRN)
    d.ellipse([26, 20, 38, 32], fill=BRN)
    d.ellipse([8, 25, 16, 31], fill=BRN)
    d.ellipse([34, 25, 42, 31], fill=BRN)
    d.arc([18, 14, 32, 36], 190, 350, fill=LBRN, width=2)
    d.arc([12, 20, 24, 32], 190, 350, fill=LBRN, width=2)
    d.arc([26, 20, 38, 32], 190, 350, fill=LBRN, width=2)
    d.arc([18, 14, 32, 36], 10, 170, fill=DBRN, width=1)

def draw_popcorn(d):
    d.polygon([(14, 24), (36, 24), (32, 43), (18, 43)], fill=WH)
    for x in [18, 25, 32]:
        d.polygon([(x-1, 24), (x+1, 24), (x+1 + (x-25)//5, 43), (x-1 + (x-25)//5, 43)], fill=RED)
    kernels = [
        (25, 14, 6), (20, 17, 5), (30, 17, 5), (16, 22, 4), (34, 22, 4),
        (22, 21, 5), (28, 21, 5), (25, 23, 5)
    ]
    for cx, cy, r in kernels:
        d.ellipse([cx-r, cy-r, cx+r, cy+r], fill=YEL)
        d.ellipse([cx-r+1, cy-r+1, cx+r-1, cy+r-1], fill=WH)
        d.point((cx, cy), fill=ORNG)

def draw_pretzel(draw):
    draw.ellipse([12, 12, 38, 38], fill=BRN)
    draw.ellipse([15, 15, 35, 35], fill=(0,0,0,0))
    draw.ellipse([18, 20, 32, 34], fill=BRN)
    draw.ellipse([21, 23, 29, 31], fill=(0,0,0,0))
    salts = [(16, 16), (32, 16), (25, 13), (20, 32), (30, 32), (14, 26), (36, 26)]
    for sx, sy in salts:
        draw.rectangle([sx, sy, sx+1, sy+1], fill=WH)

def draw_bacon(d):
    for offset in [0, 8]:
        points = [(10+offset, 16), (15+offset, 22), (20+offset, 16), (25+offset, 22), (30+offset, 16), (35+offset, 22), (40+offset, 16)]
        d.line(points, fill=DRED, width=5)
        points_fat = [(10+offset, 17), (15+offset, 23), (20+offset, 17), (25+offset, 23), (30+offset, 17), (35+offset, 23), (40+offset, 17)]
        d.line(points_fat, fill=WH, width=2)

def draw_egg(d):
    d.ellipse([12, 14, 38, 36], fill=WH)
    d.ellipse([14, 16, 36, 34], fill=LBLU)
    d.ellipse([16, 17, 34, 31], fill=WH)
    d.ellipse([20, 20, 32, 32], fill=ORNG)
    d.ellipse([21, 21, 31, 31], fill=YEL)
    d.ellipse([23, 23, 26, 26], fill=WH)

def draw_cheese(d):
    d.polygon([(10, 34), (40, 34), (25, 14)], fill=YEL)
    d.polygon([(25, 14), (40, 34), (42, 34), (27, 14)], fill=DYEL)
    holes = [(18, 26, 3), (32, 28, 2), (23, 20, 2), (29, 21, 1)]
    for cx, cy, r in holes:
        d.ellipse([cx-r, cy-r, cx+r, cy+r], fill=DYEL)
        d.ellipse([cx-r+1, cy-r, cx+r, cy+r-1], fill=ORNG)

def draw_sandwich(d):
    d.polygon([(10, 32), (40, 32), (25, 14)], fill=BRN)
    d.polygon([(12, 32), (38, 32), (25, 16)], fill=LBRN)
    d.rectangle([11, 28, 39, 31], fill=GRN)
    d.rectangle([13, 25, 37, 28], fill=RED)
    d.polygon([(14, 25), (36, 25), (25, 28)], fill=YEL)
    d.polygon([(12, 24), (38, 24), (25, 10)], fill=BRN)
    d.polygon([(14, 24), (36, 24), (25, 12)], fill=LBRN)
    d.line([(25, 5), (25, 10)], fill=WH, width=1)
    d.ellipse([23, 2, 27, 6], fill=GRN)

def draw_soup(d):
    d.ellipse([11, 20, 39, 38], fill=BLU)
    d.rectangle([11, 20, 39, 28], fill=BLU)
    d.arc([6, 22, 12, 30], 90, 270, fill=LBLU, width=2)
    d.arc([38, 22, 44, 30], 270, 90, fill=LBLU, width=2)
    d.ellipse([11, 16, 39, 24], fill=ORNG)
    d.ellipse([16, 19, 20, 22], fill=RED)
    d.ellipse([26, 18, 30, 21], fill=GRN)
    d.ellipse([21, 20, 23, 22], fill=YEL)
    d.arc([20, 4, 25, 12], 90, 270, fill=LBLU, width=1)
    d.arc([25, 6, 30, 14], 270, 90, fill=LBLU, width=1)

def draw_drumstick(d):
    d.line([(24, 24), (38, 38)], fill=WH, width=4)
    d.ellipse([34, 34, 38, 38], fill=WH)
    d.ellipse([36, 36, 40, 40], fill=WH)
    d.ellipse([11, 11, 31, 31], fill=BRN)
    d.ellipse([13, 13, 29, 29], fill=LBRN)
    for cx, cy in [(14, 18), (22, 14), (20, 24), (16, 26), (26, 20)]:
        d.rectangle([cx, cy, cx+2, cy+2], fill=BRN)

def draw_steak(d):
    d.ellipse([10, 12, 40, 34], fill=DBRN)
    d.ellipse([12, 14, 38, 32], fill=BRN)
    d.line([(25, 14), (25, 28)], fill=WH, width=3)
    d.line([(18, 16), (32, 16)], fill=WH, width=3)
    d.line([(14, 22), (20, 28)], fill=BK, width=1)
    d.line([(28, 20), (34, 26)], fill=BK, width=1)
    d.line([(15, 26), (22, 31)], fill=BK, width=1)
    d.rectangle([21, 20, 27, 24], fill=YEL)
    d.rectangle([22, 21, 26, 23], fill=WH)

def draw_tempura(d):
    d.polygon([(10, 10), (16, 8), (13, 16)], fill=RED)
    d.polygon([(9, 11), (15, 7), (12, 15)], fill=DRED)
    bumps = [
        (25, 25, 8), (20, 20, 7), (16, 16, 6), (30, 30, 7), (35, 35, 6),
        (23, 21, 7), (29, 26, 8)
    ]
    for cx, cy, r in bumps:
        d.ellipse([cx-r, cy-r, cx+r, cy+r], fill=ORNG)
        d.ellipse([cx-r+2, cy-r+2, cx+r-2, cy+r-2], fill=YEL)

def draw_onigiri(d):
    d.polygon([(13, 34), (37, 34), (25, 12)], fill=WH)
    d.rectangle([20, 24, 30, 34], fill=BK)
    for sx, sy in [(22, 16), (28, 17), (24, 19), (26, 15), (20, 20), (30, 21)]:
        d.point((sx, sy), fill=BK)

def draw_ramen(d):
    d.ellipse([10, 22, 40, 40], fill=RED)
    d.rectangle([10, 22, 40, 32], fill=RED)
    d.ellipse([10, 18, 40, 26], fill=ORNG)
    d.arc([13, 19, 25, 23], 0, 180, fill=YEL, width=1)
    d.arc([17, 21, 29, 25], 0, 180, fill=YEL, width=1)
    d.arc([23, 19, 35, 23], 0, 180, fill=YEL, width=1)
    d.ellipse([15, 20, 21, 26], fill=WH)
    d.ellipse([17, 22, 20, 25], fill=YEL)
    d.ellipse([18, 23, 20, 25], fill=ORNG)
    d.ellipse([27, 21, 33, 26], fill=WH)
    d.point((30, 23), fill=PNK)
    d.rectangle([32, 12, 38, 22], fill=BK)

def draw_coffee(d):
    d.rectangle([14, 18, 34, 38], fill=BLU)
    d.ellipse([14, 32, 34, 40], fill=BLU)
    d.arc([30, 20, 40, 32], 270, 90, fill=LBLU, width=3)
    d.ellipse([14, 14, 34, 22], fill=BRN)
    d.ellipse([20, 16, 27, 20], fill=WH)
    d.ellipse([23, 16, 30, 20], fill=WH)
    d.polygon([(20,18), (30,18), (25,21)], fill=WH)

def draw_soda(d):
    d.rectangle([16, 14, 34, 38], fill=RED)
    d.ellipse([16, 34, 34, 40], fill=RED)
    d.ellipse([16, 10, 34, 16], fill=WH)
    d.ellipse([22, 11, 28, 14], fill=LBLU)
    d.arc([16, 20, 34, 32], 0, 180, fill=WH, width=2)
    d.point((19, 18), fill=LBLU)
    d.point((31, 26), fill=LBLU)

def draw_beer(d):
    d.rectangle([16, 18, 34, 38], fill=ORNG)
    d.ellipse([16, 34, 34, 40], fill=ORNG)
    d.arc([30, 20, 40, 32], 270, 90, fill=WH, width=3)
    for bx, by in [(20, 30), (28, 28), (24, 24), (18, 22), (30, 20)]:
        d.point((bx, by), fill=YEL)
    foam_circles = [
        (25, 14, 6), (20, 16, 5), (30, 16, 5), (16, 18, 4), (34, 18, 4)
    ]
    for cx, cy, r in foam_circles:
        d.ellipse([cx-r, cy-r, cx+r, cy+r], fill=WH)
        d.ellipse([cx-r+1, cy-r+1, cx+r-1, cy+r-1], fill=WH)

def draw_cocktail(d):
    d.line([25, 22, 25, 38], fill=WH, width=2)
    d.line([18, 38, 32, 38], fill=WH, width=2)
    d.polygon([(13, 10), (37, 10), (25, 22)], fill=WH)
    d.polygon([(16, 13), (34, 13), (25, 22)], fill=RED)
    d.ellipse([12, 6, 18, 12], fill=YEL)
    d.ellipse([13, 7, 17, 11], fill=WH)
    d.line([(25, 15), (32, 4)], fill=BROWN, width=1)
    d.polygon([(30, 4), (35, 8), (28, 10)], fill=BLU)

def draw_bubbletea(d):
    d.polygon([(16, 14), (34, 14), (30, 39), (20, 39)], fill=LBRN)
    boba_spots = [
        (22, 33), (25, 34), (28, 33), (21, 36), (24, 37), (27, 36), (30, 35),
        (23, 31), (27, 31)
    ]
    for px, py in boba_spots:
        d.ellipse([px-2, py-2, px+2, py+2], fill=BK)
    d.line([(25, 4), (25, 28)], fill=PNK, width=3)
    d.ellipse([16, 11, 34, 16], fill=WH)

def draw_chocolate(d):
    d.rectangle([14, 14, 36, 38], fill=RED)
    d.rectangle([14, 14, 36, 22], fill=DBRN)
    d.line([(25, 14), (25, 22)], fill=BK, width=1)
    d.line([(14, 18), (36, 18)], fill=BK, width=1)
    d.polygon([(14, 22), (20, 24), (25, 21), (30, 24), (36, 22), (36, 25), (14, 25)], fill=WH)

def draw_candycane(d):
    d.arc([16, 10, 34, 24], 180, 360, fill=WH, width=6)
    d.line([(16, 17), (16, 40)], fill=WH, width=6)
    d.arc([16, 10, 34, 24], 180, 220, fill=RED, width=6)
    d.arc([16, 10, 34, 24], 280, 320, fill=RED, width=6)
    for y in [18, 25, 32, 38]:
        d.polygon([(13, y), (19, y-3), (19, y), (13, y+3)], fill=RED)

def draw_lollipop(d):
    d.line([25, 24, 25, 43], fill=WH, width=2)
    d.ellipse([14, 8, 36, 30], fill=RED)
    d.arc([16, 10, 34, 28], 0, 360, fill=YEL, width=3)
    d.arc([19, 13, 31, 25], 0, 360, fill=RED, width=3)
    d.arc([22, 16, 28, 22], 0, 360, fill=YEL, width=2)

def draw_macaron(d):
    d.ellipse([12, 12, 38, 22], fill=PNK)
    d.rectangle([12, 20, 38, 24], fill=DPNK)
    d.rectangle([12, 22, 38, 26], fill=WH)
    d.ellipse([12, 24, 38, 34], fill=PNK)
    d.rectangle([12, 24, 38, 28], fill=DPNK)

def draw_pudding(d):
    d.ellipse([9, 26, 41, 41], fill=BLU)
    d.ellipse([11, 28, 39, 39], fill=LBLU)
    d.polygon([(17, 18), (33, 18), (37, 33), (13, 33)], fill=YEL)
    d.ellipse([17, 15, 33, 21], fill=BRN)
    d.polygon([(17, 18), (22, 25), (25, 18)], fill=BRN)
    d.polygon([(27, 18), (30, 27), (33, 18)], fill=BRN)

def draw_toast(d):
    d.rectangle([12, 12, 38, 37], fill=BRN)
    d.ellipse([12, 9, 26, 21], fill=BRN)
    d.ellipse([24, 9, 38, 21], fill=BRN)
    d.rectangle([14, 15, 36, 35], fill=CREAM)
    d.ellipse([14, 12, 25, 20], fill=CREAM)
    d.ellipse([25, 12, 36, 20], fill=CREAM)
    d.rectangle([21, 18, 29, 26], fill=YEL)
    d.ellipse([18, 22, 32, 32], fill=RED)

def draw_kabob(d):
    d.line([5, 45, 45, 5], fill=CREAM, width=2)
    d.rectangle([10, 30, 18, 38], fill=DBRN)
    d.ellipse([16, 22, 26, 32], fill=GRN)
    d.rectangle([24, 14, 32, 22], fill=RED)
    d.rectangle([30, 6, 38, 14], fill=DBRN)
    d.line([(11, 32), (15, 36)], fill=BK)
    d.line([(31, 8), (35, 12)], fill=BK)

def draw_friedshrimp(d):
    for cx, cy, r in [(25, 25, 8), (20, 20, 7), (16, 16, 6), (30, 30, 7), (34, 34, 6)]:
        d.ellipse([cx-r, cy-r, cx+r, cy+r], fill=ORNG)
        d.ellipse([cx-r+2, cy-r+2, cx+r-2, cy+r-2], fill=YEL)
    d.polygon([(32, 14), (41, 6), (36, 17)], fill=RED)
    d.polygon([(34, 16), (42, 13), (38, 19)], fill=RED)

def draw_hotcocoa(d):
    d.rectangle([14, 18, 34, 38], fill=RED)
    d.ellipse([14, 32, 34, 40], fill=RED)
    d.arc([30, 20, 40, 32], 270, 90, fill=RED, width=3)
    d.ellipse([14, 14, 34, 22], fill=DBRN)
    d.rectangle([18, 16, 22, 20], fill=WHITE)
    d.rectangle([25, 17, 29, 21], fill=WHITE)
    d.line([(24, 8), (30, 16)], fill=BROWN, width=3)

def draw_dango(d):
    d.line([25, 8, 25, 44], fill=BROWN, width=2)
    d.ellipse([19, 10, 31, 22], fill=PNK)
    d.ellipse([19, 19, 31, 31], fill=WH)
    d.ellipse([19, 28, 31, 40], fill=GRN)
    d.arc([19, 10, 31, 40], 270, 90, fill=YEL, width=2)

def draw_fortune(d):
    d.ellipse([14, 14, 36, 36], fill=LBRN)
    d.polygon([(25, 23), (16, 33), (34, 33)], fill=BRN)
    d.polygon([(30, 14), (42, 12), (40, 18), (28, 20)], fill=WHITE)
    d.line([(32, 15), (38, 14)], fill=RED, width=1)

def draw_softserve(d):
    d.polygon([(18, 26), (32, 26), (25, 45)], fill=LBRN)
    d.ellipse([13, 18, 37, 28], fill=WH)
    d.ellipse([16, 12, 34, 22], fill=PNK)
    d.ellipse([19, 6, 31, 15], fill=WH)
    d.point((25, 10), fill=YEL)
    d.point((20, 18), fill=BLU)

def draw_honeypot(d):
    d.ellipse([12, 16, 38, 38], fill=ORNG)
    d.ellipse([15, 13, 35, 18], fill=ORNG)
    d.rectangle([16, 23, 34, 29], fill=CREAM)
    d.ellipse([18, 13, 32, 17], fill=YEL)
    d.polygon([(20, 16), (23, 31), (26, 16)], fill=YEL)

def draw_avocadotoast(d):
    d.rectangle([12, 12, 38, 37], fill=BRN)
    d.rectangle([14, 14, 36, 35], fill=CREAM)
    d.ellipse([15, 15, 35, 33], fill=GRN)
    for ax, ay in [(18, 20), (28, 18), (22, 27), (31, 26)]:
        d.ellipse([ax-1, ay-1, ax+1, ay+1], fill=DGRN)
    for rx, ry in [(20, 22), (29, 22), (23, 30)]:
        d.point((rx, ry), fill=RED)

def draw_cinnamon(d):
    d.ellipse([12, 12, 38, 38], fill=LBRN)
    d.arc([14, 14, 36, 36], 0, 360, fill=BRN, width=2)
    d.arc([18, 18, 32, 32], 0, 360, fill=BRN, width=2)
    d.ellipse([20, 18, 30, 28], fill=WH)
    d.polygon([(22, 20), (24, 34), (27, 20)], fill=WH)

def draw_muffin(d):
    d.polygon([(16, 24), (34, 24), (30, 42), (20, 42)], fill=WH)
    d.ellipse([10, 12, 40, 26], fill=LBRN)
    for cx, cy in [(15, 17), (25, 14), (34, 17), (21, 21), (29, 21)]:
        d.ellipse([cx-2, cy-2, cx+2, cy+2], fill=DBRN)

def draw_gingerbread(d):
    d.ellipse([20, 9, 30, 19], fill=BRN)
    d.rectangle([17, 18, 33, 32], fill=BRN)
    d.line([(17, 20), (9, 24)], fill=BRN, width=4)
    d.line([(33, 20), (41, 24)], fill=BRN, width=4)
    d.line([(19, 32), (15, 42)], fill=BRN, width=4)
    d.line([(31, 32), (35, 42)], fill=BRN, width=4)
    d.line([(10, 22), (12, 25)], fill=WH, width=1)
    d.line([(38, 25), (40, 22)], fill=WH, width=1)
    d.point((22, 13), fill=WH)
    d.point((28, 13), fill=WH)
    d.ellipse([23, 21, 27, 25], fill=RED)
    d.ellipse([23, 27, 27, 31], fill=GRN)

def draw_crepe(d):
    d.polygon([(11, 18), (39, 18), (25, 42)], fill=CREAM)
    d.line([(14, 20), (20, 26), (26, 20), (32, 26), (36, 20)], fill=DBRN, width=2)
    d.ellipse([18, 13, 24, 19], fill=RED)
    d.ellipse([26, 12, 32, 18], fill=RED)
    d.ellipse([21, 14, 29, 22], fill=WH)

# 51-200: 150 NEW Unique Food & Dessert Drawing Functions
def draw_bagel(d):
    d.ellipse([11, 11, 39, 39], fill=LBRN)
    d.ellipse([14, 14, 36, 36], fill=WH) # Cream cheese spread
    d.ellipse([20, 20, 30, 30], fill=(0,0,0,0)) # Hole

def draw_burrito(d):
    d.polygon([(12, 20), (38, 12), (32, 40), (16, 42)], fill=CREAM) # Tortilla
    # Filling sticking out at top
    d.ellipse([20, 12, 30, 18], fill=DBRN) # meat
    d.ellipse([28, 10, 34, 15], fill=RED) # salsa
    d.ellipse([16, 14, 22, 18], fill=GRN) # lettuce

def draw_quesadilla(d):
    d.ellipse([10, 10, 40, 40], fill=CREAM)
    d.rectangle([10, 10, 40, 25], fill=(0,0,0,0)) # half circle
    d.line([(10, 25), (40, 25)], fill=DYEL, width=2) # cheese border

def draw_nachos(d):
    # Pile of yellow triangles
    for x, y in [(15, 28), (25, 25), (32, 30), (20, 34), (28, 35)]:
        d.polygon([(x, y), (x+8, y-4), (x+4, y+6)], fill=YEL)
    # Cheese drizzle
    d.line([(16, 30), (34, 30)], fill=ORNG, width=2)
    # Jalapenos (green dots)
    for x, y in [(20, 28), (28, 26), (25, 34)]:
        d.ellipse([x-1, y-1, x+1, y+1], fill=DGRN)

def draw_guacamole(d):
    d.ellipse([12, 22, 38, 38], fill=BRN) # Bowl
    d.ellipse([12, 18, 38, 26], fill=GRN) # Guac
    # Red tomato speckles
    for x, y in [(18, 20), (28, 22), (24, 24)]:
        d.point((x, y), fill=RED)
    # Tortilla chip sticking out
    d.polygon([(14, 12), (20, 18), (12, 20)], fill=YEL)

def draw_salsa(d):
    d.ellipse([12, 22, 38, 38], fill=BLU) # Bowl
    d.ellipse([12, 18, 38, 26], fill=RED) # Salsa
    # Green onion specks
    for x, y in [(18, 20), (28, 22), (24, 24)]:
        d.point((x, y), fill=GRN)

def draw_churro(d):
    d.line([(15, 38), (35, 12)], fill=LBRN, width=4) # Churro stick
    # Cinnamon ribs
    d.line([(16, 37), (36, 11)], fill=BRN, width=1)
    # Sugar specks
    for x, y in [(18, 33), (25, 25), (32, 17)]:
        d.point((x, y), fill=WH)

def draw_flan(d):
    d.ellipse([10, 36, 40, 44], fill=SHD)
    d.polygon([(18, 20), (32, 20), (36, 34), (14, 34)], fill=YEL)
    d.ellipse([18, 17, 33, 23], fill=BRN) # Caramel glaze top

def draw_tiramisu(d):
    # Cake slice with layered coffee cream
    d.rectangle([12, 16, 38, 38], fill=DBRN)
    d.rectangle([12, 22, 38, 28], fill=CREAM)
    d.rectangle([12, 34, 38, 38], fill=CREAM)
    # Cocoa dusting top (speckled)
    for x in range(14, 38, 4):
        d.point((x, 16), fill=DBRN)

def draw_pannacotta(d):
    d.ellipse([10, 32, 40, 40], fill=BLU) # plate
    d.polygon([(18, 18), (32, 18), (35, 32), (15, 32)], fill=WH) # panna cotta dome
    d.ellipse([21, 15, 29, 21], fill=RED) # strawberry sauce top

def draw_baklava(d):
    d.rectangle([12, 14, 38, 36], fill=LBRN)
    # Layer horizontal cuts
    for y in [20, 26, 32]:
        d.line([(12, y), (38, y)], fill=BRN, width=1)
    # Pistachio nuts top (green flakes)
    for x in [16, 24, 32]:
        d.rectangle([x, 15, x+2, 17], fill=GRN)

def draw_eclair(d):
    d.ellipse([10, 20, 40, 30], fill=LBRN)
    # Chocolate icing top layer
    d.ellipse([12, 18, 38, 26], fill=DBRN)
    # White glaze drizzle highlight
    d.line([(15, 20), (35, 20)], fill=WH, width=1)

def draw_tart(d):
    d.ellipse([10, 16, 40, 38], fill=BRN) # Crust
    d.ellipse([13, 19, 37, 35], fill=YEL) # Custard
    # Fruit toppings
    d.ellipse([18, 22, 24, 28], fill=RED) # Strawberry
    d.ellipse([26, 24, 30, 28], fill=GRN) # Kiwi
    d.ellipse([22, 28, 25, 31], fill=BLU) # Blueberry

def draw_cheesecake(d):
    # Slice of cheesecake
    d.polygon([(10, 34), (40, 34), (25, 14)], fill=CREAM)
    # Graham crust back
    d.line([(40, 34), (25, 14)], fill=BRN, width=2)
    # Strawberry glaze topping
    d.polygon([(10, 34), (32, 20), (25, 14)], fill=RED)

def draw_bananasplit(d):
    d.ellipse([8, 26, 42, 40], fill=WH) # long banana dish
    d.ellipse([10, 20, 20, 30], fill=YEL) # banana 1
    d.ellipse([30, 20, 40, 30], fill=YEL) # banana 2
    # Scoops of ice cream
    d.ellipse([16, 18, 24, 26], fill=WH) # vanilla
    d.ellipse([26, 18, 34, 26], fill=PNK) # strawberry
    # Cherry
    d.ellipse([23, 12, 27, 16], fill=RED)

def draw_milkshake(d):
    d.polygon([(16, 16), (34, 16), (30, 42), (20, 42)], fill=LBLU) # glass
    d.polygon([(17, 17), (33, 17), (29, 41), (21, 41)], fill=PNK) # milkshake pink
    # Whipped cream top dome
    d.ellipse([18, 10, 32, 18], fill=WH)
    # Straw
    d.line([(25, 4), (28, 20)], fill=RED, width=2)

def draw_sundae(d):
    d.ellipse([12, 22, 38, 38], fill=PNK) # Ice cream bowl
    # Ice cream scoop
    d.ellipse([16, 12, 34, 28], fill=WH)
    # Hot fudge chocolate drizzle
    d.ellipse([21, 14, 29, 20], fill=DBRN)
    # Cherry
    d.ellipse([23, 6, 27, 10], fill=RED)

def draw_parfait(d):
    d.rectangle([16, 16, 34, 38], fill=WH) # Yogurt layered glass
    # Fruit layers (red and orange)
    d.rectangle([16, 22, 34, 26], fill=RED)
    d.rectangle([16, 30, 34, 34], fill=ORNG)

def draw_sherbet(d):
    d.ellipse([12, 22, 38, 38], fill=BLU) # Cup
    # Layered Sherbet Scoop (rainbow)
    d.ellipse([15, 12, 35, 28], fill=PNK)
    d.ellipse([18, 14, 32, 28], fill=ORNG)
    d.ellipse([21, 16, 29, 28], fill=GRN)

def draw_mochi(d):
    d.ellipse([12, 18, 38, 38], fill=GRN) # Green tea mochi ball
    # Powder coating dust
    for sx, sy in [(22, 22), (28, 24), (20, 28)]:
        d.point((sx, sy), fill=WH)

def draw_cannoli(d):
    d.ellipse([12, 18, 38, 30], fill=LBRN) # shell
    # Cream filling showing at ends
    d.ellipse([10, 20, 16, 28], fill=WH)
    d.ellipse([34, 20, 40, 28], fill=WH)
    # Chocolate chips inside cream ends
    d.point((12, 24), fill=DBRN)
    d.point((38, 24), fill=DBRN)

def draw_gelato(d):
    d.ellipse([12, 24, 38, 38], fill=PNK) # Cup
    # Multi-scoops
    d.ellipse([15, 14, 27, 26], fill=ORNG)
    d.ellipse([23, 14, 35, 26], fill=YEL)
    d.ellipse([18, 10, 32, 20], fill=GRN)

def draw_scone(d):
    d.polygon([(12, 34), (38, 34), (25, 14)], fill=LBRN) # scone body
    # Blueberry dots
    for bx, by in [(18, 26), (28, 28), (24, 20)]:
        d.ellipse([bx-1, by-1, bx+1, by+1], fill=BLU)

def draw_baguette(d):
    d.line([(10, 38), (40, 12)], fill=BRN, width=6) # Baguette loaf
    # Diagonal cuts
    for x in [18, 26, 34]:
        d.line([(x-2, 42-x), (x+2, 38-x)], fill=LBRN, width=2)

def draw_garlicbread(d):
    d.line([(10, 38), (40, 12)], fill=LBRN, width=6)
    # Parsley herbs (green specks)
    for x in [15, 22, 29, 36]:
        d.point((x, 48-x), fill=GRN)

def draw_cornbread(d):
    d.rectangle([12, 14, 38, 36], fill=YEL) # cornbread square
    d.rectangle([12, 30, 38, 36], fill=DYEL) # side shadow
    # Butter pat
    d.rectangle([21, 20, 29, 26], fill=WH)

def draw_sourdough(d):
    d.ellipse([10, 12, 40, 38], fill=BRN) # Loaf
    # Cross slash slash marks
    d.line([(18, 16), (32, 34)], fill=LBRN, width=2)
    d.line([(32, 16), (18, 34)], fill=LBRN, width=2)

def draw_ryebread(d):
    d.ellipse([12, 14, 38, 36], fill=DBRN) # dark rye slice
    # Seeds specks
    for sx, sy in [(18, 20), (28, 24), (20, 30), (32, 28)]:
        d.point((sx, sy), fill=LBRN)

def draw_pitabread(d):
    d.ellipse([10, 18, 40, 38], fill=CREAM)
    d.rectangle([10, 18, 40, 26], fill=(0,0,0,0)) # pocket cut
    # Falafels and salad sticking out
    d.ellipse([18, 16, 24, 22], fill=BRN) # falafel
    d.ellipse([26, 15, 32, 21], fill=BRN) # falafel
    d.ellipse([21, 18, 28, 24], fill=GRN) # lettuce

def draw_naan(d):
    d.ellipse([10, 14, 40, 38], fill=CREAM)
    # Tandoor brown char bubbles
    for cx, cy in [(18, 22), (28, 26), (32, 18), (22, 32)]:
        d.ellipse([cx-2, cy-2, cx+2, cy+2], fill=BRN)

def draw_challah(d):
    # Braided segments
    d.ellipse([16, 12, 34, 38], fill=BRN)
    for y in [18, 26, 34]:
        d.ellipse([20, y, 30, y+6], fill=LBRN)

def draw_brioche(d):
    d.ellipse([12, 16, 38, 38], fill=BRN) # bun base
    d.ellipse([20, 10, 30, 20], fill=LBRN) # top brioche knot

def draw_focaccia(d):
    d.rectangle([12, 12, 38, 38], fill=LBRN)
    # Cherry tomatoes (red dots)
    d.ellipse([16, 16, 20, 20], fill=RED)
    d.ellipse([30, 28, 34, 32], fill=RED)
    # Rosemary sprigs (green lines)
    d.line([(22, 22), (26, 26)], fill=GRN, width=2)
    d.line([(26, 26), (28, 24)], fill=GRN, width=1)

def draw_bruschetta(d):
    d.polygon([(10, 32), (40, 32), (25, 14)], fill=BRN) # bread toast
    # Diced tomato toppings
    for tx, ty in [(18, 24), (28, 22), (22, 28), (30, 28)]:
        d.rectangle([tx, ty, tx+3, ty+3], fill=RED)
    # Basil leaves
    d.point((24, 22), fill=GRN)

def draw_calzone(d):
    d.ellipse([10, 14, 40, 38], fill=LBRN) # folded dough
    # Cut out half
    d.rectangle([25, 14, 40, 38], fill=(0,0,0,0))
    # Fold crimp marks
    for y in range(16, 38, 4):
        d.line([(24, y), (26, y)], fill=BRN, width=1)

def draw_garlicknots(d):
    d.ellipse([16, 16, 34, 34], fill=LBRN) # knot shape
    d.ellipse([20, 20, 30, 30], fill=(0,0,0,0)) # knot inner
    # Garlic butter glaze herbs (green dots)
    for gx, gy in [(18, 18), (30, 20), (28, 30), (20, 28)]:
        d.point((gx, gy), fill=GRN)

def draw_stromboli(d):
    d.rectangle([12, 14, 38, 36], fill=LBRN) # rolled bread
    # Spiral score cuts showing meat/cheese
    d.line([(16, 18), (22, 24)], fill=RED, width=2)
    d.line([(24, 22), (30, 28)], fill=RED, width=2)

def draw_gyoza(d):
    d.ellipse([12, 16, 38, 36], fill=CREAM) # dumpling
    d.rectangle([12, 16, 38, 24], fill=(0,0,0,0)) # top half empty
    # Golden brown pan fried bottom
    d.ellipse([12, 28, 38, 36], fill=BRN)

def draw_baozi(d):
    d.ellipse([12, 14, 38, 38], fill=WH) # steamed bun
    # Pleats center point swirl
    d.ellipse([23, 16, 27, 20], fill=LBLU)

def draw_siumai(d):
    d.rectangle([15, 20, 35, 40], fill=YEL) # yellow wrapper
    d.ellipse([15, 16, 35, 24], fill=YEL) # open top
    # Orange roe topping
    d.ellipse([22, 16, 28, 20], fill=ORNG)

def draw_hargow(d):
    d.ellipse([12, 16, 38, 36], fill=WH) # translucent shell
    # Pink shrimp color glowing inside
    d.ellipse([18, 20, 32, 32], fill=PNK)

def draw_springroll(d):
    d.line([(12, 36), (36, 12)], fill=LBRN, width=6) # Crispy roll
    d.ellipse([10, 34, 15, 38], fill=BRN) # wrapper fold end
    d.ellipse([34, 10, 39, 14], fill=BRN) # wrapper fold end

def draw_friedrice(d):
    d.ellipse([12, 22, 38, 38], fill=RED) # Bowl
    d.ellipse([12, 18, 38, 26], fill=YEL) # Rice pile
    # Peas (green) and carrots (orange)
    for px, py in [(18, 20), (28, 22), (22, 24)]:
        d.point((px, py), fill=GRN)
    for cx, cy in [(22, 19), (32, 21), (25, 23)]:
        d.point((cx, cy), fill=ORNG)

def draw_lomein(d):
    d.ellipse([12, 22, 38, 38], fill=BLU) # Bowl
    # Swirly noodles
    d.arc([14, 18, 36, 28], 0, 360, fill=YEL, width=2)
    d.arc([18, 20, 32, 26], 0, 360, fill=BROWN, width=2)

def draw_kungpao(d):
    d.ellipse([12, 22, 38, 38], fill=WH) # Plate
    # Chicken and peanut chunks
    for cx, cy in [(18, 24), (28, 22), (24, 28)]:
        d.rectangle([cx, cy, cx+3, cy+3], fill=BRN) # chicken
    for px, py in [(22, 20), (32, 26)]:
        d.ellipse([px-1, py-1, px+1, py+1], fill=YEL) # peanuts

def draw_sweetpork(d):
    d.ellipse([12, 22, 38, 38], fill=WH)
    # Red pork pieces and green bell peppers
    for rx, ry in [(18, 24), (28, 22), (24, 28)]:
        d.rectangle([rx, ry, rx+3, ry+3], fill=RED) # pork
    # Pineapple yellow blocks
    for yx, yy in [(22, 20), (32, 26)]:
        d.rectangle([yx, yy, yx+2, yy+2], fill=YEL)

def draw_mapotofu(d):
    d.ellipse([12, 22, 38, 38], fill=RED) # Bowl
    d.ellipse([12, 18, 38, 26], fill=DRED) # Spicy sauce
    # Tofu white cubes
    for tx, ty in [(18, 22), (28, 21), (24, 24)]:
        d.rectangle([tx, ty, tx+3, ty+3], fill=WH)

def draw_pekingduck(d):
    d.ellipse([12, 16, 38, 38], fill=CREAM) # pancake wrapper
    # Crispy brown duck meat inside
    d.rectangle([20, 20, 30, 32], fill=DBRN)
    d.line([(18, 24), (32, 24)], fill=GRN, width=2) # green scallions

def draw_chowmein(d):
    # Crispy thin dry noodles pile
    d.ellipse([12, 22, 38, 38], fill=BLU) # Bowl
    for y in range(18, 26, 3):
        d.line([(14, y), (36, y+2)], fill=YEL, width=1)
        d.line([(36, y), (14, y+2)], fill=YEL, width=1)

def draw_eggdropsoup(d):
    d.ellipse([12, 22, 38, 38], fill=RED) # Bowl
    d.ellipse([12, 18, 38, 26], fill=YEL) # Yellow broth
    # Egg drop ribbons (white swirls)
    d.arc([16, 19, 34, 25], 0, 180, fill=WH, width=2)

def draw_hotsoursoup(d):
    d.ellipse([12, 22, 38, 38], fill=RED) # Bowl
    d.ellipse([12, 18, 38, 26], fill=DBRN) # Dark broth
    # Tofu cubes
    d.rectangle([20, 20, 23, 23], fill=WH)
    d.rectangle([26, 21, 29, 24], fill=WH)

def draw_wontonsoup(d):
    d.ellipse([12, 22, 38, 38], fill=BLU) # Bowl
    d.ellipse([12, 18, 38, 26], fill=LBLU) # Clear broth
    # Floating wontons
    d.ellipse([18, 20, 23, 25], fill=CREAM)
    d.ellipse([26, 21, 31, 26], fill=CREAM)

def draw_crabrangoon(d):
    # Star-shaped wonton pouch
    d.polygon([(25, 12), (18, 26), (32, 26)], fill=LBRN)
    d.polygon([(25, 38), (18, 24), (32, 24)], fill=LBRN)

def draw_eggroll(d):
    d.rectangle([12, 18, 38, 32], fill=LBRN) # Roll
    # Bubbles texture
    d.ellipse([15, 20, 17, 22], fill=BRN)
    d.ellipse([30, 26, 32, 28], fill=BRN)

def draw_falafel(d):
    d.ellipse([12, 22, 38, 38], fill=WH) # Plate
    # Three crispy brown balls
    d.ellipse([16, 24, 22, 30], fill=DBRN)
    d.ellipse([24, 22, 30, 28], fill=DBRN)
    d.ellipse([22, 28, 28, 34], fill=DBRN)

def draw_hummus(d):
    d.ellipse([12, 22, 38, 38], fill=BLU) # Bowl
    d.ellipse([12, 18, 38, 26], fill=CREAM) # Hummus
    # Olive oil pool (yellow) in center
    d.ellipse([21, 20, 29, 24], fill=YEL)

def draw_shawarma(d):
    # Rolled pita wrap
    d.polygon([(16, 14), (34, 14), (30, 42), (20, 42)], fill=CREAM)
    # Meat shreds showing at open top
    d.rectangle([20, 14, 30, 20], fill=DBRN)

def draw_gyros(d):
    # Pita wrap open showing meat & tzatziki sauce
    d.ellipse([14, 14, 36, 42], fill=CREAM)
    d.ellipse([20, 16, 30, 28], fill=DBRN) # meat
    d.line([(22, 18), (28, 24)], fill=WH, width=2) # tzatziki

def draw_kebab(d):
    # Chicken pieces skewered
    d.line([25, 8, 25, 42], fill=WH, width=2)
    for y in [14, 22, 30]:
        d.rectangle([18, y, 32, y+6], fill=BRN)

def draw_tikkamasala(d):
    d.ellipse([12, 22, 38, 38], fill=RED) # Bowl
    d.ellipse([12, 18, 38, 26], fill=ORNG) # Curry orange
    # Chicken pieces
    for cx, cy in [(18, 20), (28, 22), (24, 24)]:
        d.rectangle([cx, cy, cx+2, cy+2], fill=BRN)

def draw_samosa(d):
    # Golden brown triangle pastry
    d.polygon([(12, 34), (38, 34), (25, 14)], fill=LBRN)
    d.polygon([(12, 34), (38, 34), (25, 14)], outline=BRN)

def draw_biryani(d):
    d.ellipse([12, 22, 38, 38], fill=WH) # Plate
    d.ellipse([12, 18, 38, 26], fill=YEL) # Rice pile
    # Almonds (white) and chicken (brown)
    d.ellipse([22, 20, 25, 23], fill=WH)
    d.rectangle([26, 21, 30, 25], fill=BRN)

def draw_curry(d):
    d.ellipse([12, 22, 38, 38], fill=RED) # Bowl
    d.ellipse([12, 18, 38, 26], fill=GRN) # Green curry
    # Veggie chunks
    d.ellipse([22, 20, 25, 23], fill=ORNG) # carrot
    d.ellipse([26, 21, 29, 24], fill=WH) # potato

def draw_pho(d):
    d.ellipse([11, 20, 39, 38], fill=BLU) # Bowl
    d.ellipse([11, 16, 39, 24], fill=LBLU) # Broth
    # White noodles & beef
    d.line([(15, 19), (35, 21)], fill=WH, width=2)
    d.ellipse([18, 18, 24, 22], fill=BRN) # beef

def draw_padthai(d):
    d.ellipse([12, 22, 38, 38], fill=WH) # Plate
    # Noodles & peanuts
    d.ellipse([12, 18, 38, 26], fill=YEL)
    d.point((20, 20), fill=BRN) # crushed peanuts
    d.point((30, 22), fill=BRN)

def draw_tomyum(d):
    d.ellipse([12, 22, 38, 38], fill=RED) # Bowl
    d.ellipse([12, 18, 38, 26], fill=ORNG) # Tom Yum red/orange broth
    d.ellipse([20, 20, 25, 23], fill=PNK) # shrimp

def draw_satay(d):
    # Skewered chicken strip with peanut sauce
    d.line([15, 38, 35, 12], fill=WH, width=2) # stick
    d.line([(18, 34), (32, 16)], fill=BRN, width=4) # chicken
    # Sauce drip
    d.ellipse([24, 24, 28, 28], fill=YEL)

def draw_gimbap(d):
    d.ellipse([12, 12, 38, 38], fill=BK) # Nori wrapper
    d.ellipse([14, 14, 36, 36], fill=WH) # Rice
    # Cucumber (green), pickled radish (yellow), ham (pink)
    d.rectangle([18, 20, 22, 24], fill=GRN)
    d.rectangle([26, 20, 30, 24], fill=YEL)
    d.rectangle([22, 26, 26, 30], fill=PNK)

def draw_bibimbap(d):
    d.ellipse([11, 20, 39, 38], fill=BK) # Stone bowl
    d.ellipse([11, 16, 39, 24], fill=WH) # Rice base
    # Rainbow toppings around egg yolk center
    d.ellipse([22, 18, 28, 22], fill=ORNG) # Egg yolk center
    d.rectangle([14, 16, 18, 20], fill=GRN) # Spinach
    d.rectangle([30, 16, 34, 20], fill=RED) # Gochujang
    d.rectangle([22, 24, 28, 28], fill=BRN) # Bulgogi beef

def draw_tteokbokki(d):
    d.ellipse([12, 22, 38, 38], fill=WH) # Plate
    # Red spicy cylinders
    d.line([(18, 20), (28, 20)], fill=RED, width=3)
    d.line([(20, 26), (30, 26)], fill=RED, width=3)
    d.line([(16, 32), (26, 32)], fill=RED, width=3)

def draw_kimchi(d):
    d.ellipse([12, 22, 38, 38], fill=RED) # Bowl
    d.ellipse([12, 18, 38, 26], fill=DRED) # Fermented red
    # Cabbage green/white chunks
    d.rectangle([18, 20, 22, 24], fill=GRN)
    d.rectangle([26, 21, 30, 25], fill=WH)

def draw_bulgogi(d):
    d.ellipse([12, 22, 38, 38], fill=WH) # Plate
    # Thin marinated beef slices
    d.ellipse([16, 20, 28, 28], fill=DBRN)
    d.ellipse([24, 22, 34, 30], fill=DBRN)

def draw_japchae(d):
    d.ellipse([12, 22, 38, 38], fill=BLU) # Bowl
    # Glass noodles
    d.arc([14, 18, 36, 28], 0, 360, fill=LBLU, width=2)
    d.point((20, 22), fill=GRN) # spinach flake

def draw_tonkatsu(d):
    d.ellipse([12, 22, 38, 38], fill=WH) # Plate
    # Golden brown cutlet sliced
    d.rectangle([14, 20, 36, 32], fill=ORNG)
    # Sauce stripes
    for x in [18, 24, 30]:
        d.line([(x, 20), (x, 32)], fill=DBRN, width=2)

def draw_tempuradon(d):
    d.ellipse([12, 22, 38, 38], fill=BLU) # Bowl
    d.ellipse([12, 18, 38, 26], fill=WH) # Rice
    # Tempura shrimp sticking out
    d.line([(18, 14), (28, 24)], fill=ORNG, width=4)
    d.polygon([(14, 10), (20, 8), (17, 14)], fill=RED) # tail

def draw_udon(d):
    d.ellipse([11, 20, 39, 38], fill=RED) # Bowl
    d.ellipse([11, 16, 39, 24], fill=YEL) # Broth
    # Thick white noodles
    d.line([(16, 19), (34, 21)], fill=WH, width=3)

def draw_soba(d):
    d.rectangle([12, 22, 38, 38], fill=BRN) # bamboo mat
    # Buckwheat cold noodles
    d.rectangle([14, 24, 36, 36], fill=DBRN)

def draw_yakitori(d):
    # Skewered chicken bites
    d.line([25, 8, 25, 42], fill=WH, width=2)
    for y in [14, 22, 30]:
        d.ellipse([20, y, 30, y+6], fill=BRN)

def draw_takoyaki(d):
    # Three octopus balls on a plate
    d.ellipse([12, 22, 38, 38], fill=WH)
    d.ellipse([16, 24, 24, 32], fill=LBRN)
    d.ellipse([26, 24, 34, 32], fill=LBRN)
    d.ellipse([21, 20, 29, 28], fill=LBRN)
    # Mayo/brown sauce swirl
    d.line([(18, 26), (32, 26)], fill=DBRN, width=1)

def draw_okonomiyaki(d):
    d.ellipse([12, 12, 38, 38], fill=LBRN) # cabbage pancake
    # Brown sauce and mayonnaise zig zag grid
    for x in range(16, 36, 6):
        d.line([(x, 12), (x, 38)], fill=DBRN, width=1)
        d.line([(12, x), (38, x)], fill=WH, width=1)

def draw_matchalatte(d):
    d.rectangle([14, 18, 34, 38], fill=BLU) # Cup
    d.ellipse([14, 32, 34, 40], fill=BLU)
    # Green matcha surface
    d.ellipse([14, 14, 34, 22], fill=GRN)
    # Leaf art (white)
    d.ellipse([21, 16, 29, 20], fill=WH)

def draw_taiyaki(d):
    # Fish-shaped waffle
    d.ellipse([12, 16, 38, 34], fill=LBRN)
    d.polygon([(32, 20), (40, 14), (40, 36), (32, 30)], fill=LBRN) # tail
    # Fish eye
    d.ellipse([18, 22, 20, 24], fill=BK)

def draw_dorayaki(d):
    # Pancake sandwiches
    d.ellipse([12, 14, 38, 26], fill=LBRN) # top pancake
    d.rectangle([12, 24, 38, 28], fill=DBRN) # sweet red bean layer
    d.ellipse([12, 26, 38, 38], fill=LBRN) # bottom pancake

def draw_kakigori(d):
    d.ellipse([12, 22, 38, 38], fill=BLU) # bowl
    # Shaved ice heap (white)
    d.polygon([(14, 24), (36, 24), (25, 8)], fill=WH)
    # Red strawberry syrup drizzle
    d.polygon([(22, 14), (28, 14), (25, 24)], fill=RED)

def draw_crepecake(d):
    # Slice of crepe cake with layered lines
    d.polygon([(10, 36), (40, 36), (25, 14)], fill=CREAM)
    for y in range(18, 36, 3):
        d.line([(12, y), (38, y)], fill=LBRN, width=1)

def draw_fruitsalad(d):
    d.ellipse([12, 22, 38, 38], fill=BLU) # Bowl
    # Fruit chunks
    d.ellipse([16, 20, 21, 25], fill=RED) # watermelon
    d.ellipse([25, 18, 30, 23], fill=YEL) # banana
    d.ellipse([21, 24, 25, 28], fill=GRN) # grape

def draw_greensalad(d):
    d.ellipse([12, 22, 38, 38], fill=WH) # Bowl
    d.ellipse([12, 18, 38, 26], fill=GRN) # Lettuce
    # Cherry tomatoes
    d.ellipse([18, 20, 22, 24], fill=RED)
    d.ellipse([28, 21, 32, 25], fill=RED)

def draw_caesarsalad(d):
    d.ellipse([12, 22, 38, 38], fill=WH) # Bowl
    d.ellipse([12, 18, 38, 26], fill=GRN) # Lettuce
    # Croutons (yellow/brown cubes)
    d.rectangle([18, 20, 21, 23], fill=LBRN)
    d.rectangle([28, 21, 31, 24], fill=LBRN)

def draw_coleslaw(d):
    d.ellipse([12, 22, 38, 38], fill=RED) # Bowl
    d.ellipse([12, 18, 38, 26], fill=WH) # Shredded cabbage
    # Carrots (orange strips)
    d.line([(16, 19), (20, 21)], fill=ORNG, width=1)
    d.line([(26, 21), (30, 23)], fill=ORNG, width=1)

def draw_potatosalad(d):
    d.ellipse([12, 22, 38, 38], fill=BLU) # Bowl
    # Creamy yellow potato chunks
    for cx, cy in [(18, 20), (28, 22), (23, 25)]:
        d.rectangle([cx, cy, cx+4, cy+4], fill=YEL)
    # Chives green specks
    d.point((21, 22), fill=GRN)

def draw_bakedpotato(d):
    d.ellipse([10, 16, 40, 34], fill=BRN) # Potato
    d.rectangle([15, 23, 35, 27], fill=WH) # Sour cream center
    d.rectangle([22, 22, 28, 25], fill=YEL) # Melting butter

def draw_mashedpotato(d):
    d.ellipse([12, 22, 38, 38], fill=WH) # Plate
    # Mashed potato dome (cream)
    d.ellipse([15, 16, 35, 32], fill=CREAM)
    # Gravy pool center (brown)
    d.ellipse([21, 20, 29, 26], fill=BRN)

def draw_maccheese(d):
    d.ellipse([12, 22, 38, 38], fill=RED) # Bowl
    # Macaroni elbows (yellow macaroni curves)
    for y in [18, 22, 26]:
        d.arc([14, y, 22, y+6], 0, 180, fill=YEL, width=2)
        d.arc([26, y, 34, y+6], 0, 180, fill=YEL, width=2)

def draw_lasagna(d):
    # Square slice showing layers
    d.rectangle([12, 14, 38, 36], fill=YEL)
    d.rectangle([12, 30, 38, 36], fill=DYEL) # side
    # Pasta red sauce layers
    d.line([(12, 20), (38, 20)], fill=RED, width=2)
    d.line([(12, 28), (38, 28)], fill=RED, width=2)

def draw_spaghetti(d):
    d.ellipse([12, 22, 38, 38], fill=WH) # Plate
    # Noodles heap
    d.ellipse([15, 18, 35, 32], fill=YEL)
    # Meat sauce on top
    d.ellipse([20, 20, 30, 28], fill=RED)
    d.point((25, 22), fill=GRN) # basil leaf

def draw_meatballs(d):
    d.ellipse([12, 22, 38, 38], fill=RED) # Bowl
    d.ellipse([12, 18, 38, 26], fill=RED) # Sauce
    # Three brown balls
    d.ellipse([16, 22, 22, 28], fill=BRN)
    d.ellipse([26, 22, 32, 28], fill=BRN)
    d.ellipse([21, 26, 27, 32], fill=BRN)

def draw_chili(d):
    d.ellipse([12, 22, 38, 38], fill=RED) # Bowl
    d.ellipse([12, 18, 38, 26], fill=DBRN) # Chili stew
    # Shredded cheese (yellow specs)
    for sx, sy in [(18, 20), (28, 22), (24, 24)]:
        d.point((sx, sy), fill=YEL)

def draw_corncob(d):
    d.ellipse([12, 36, 38, 42], fill=SHD)
    d.line([(15, 35), (35, 15)], fill=YEL, width=6) # corn cob
    d.rectangle([21, 21, 29, 29], fill=WH) # butter glaze

def draw_clamchowder(d):
    d.ellipse([12, 16, 38, 38], fill=BRN) # Bread bowl
    # White clam chowder soup inside
    d.ellipse([16, 20, 34, 34], fill=WH)
    # Herbs (green specks)
    d.point((22, 24), fill=GRN)

def draw_fishchips(d):
    d.ellipse([12, 22, 38, 38], fill=WH) # Plate
    # Fried fish fillet (golden brown)
    d.ellipse([14, 18, 30, 30], fill=ORNG)
    # Fries sticks
    for x in range(24, 36, 3):
        d.rectangle([x, 22, x+2, 34], fill=YEL)

def draw_calamari(d):
    d.ellipse([12, 22, 38, 38], fill=WH) # Plate
    # Fried squid rings (golden loops)
    d.ellipse([16, 20, 24, 28], fill=ORNG)
    d.ellipse([18, 22, 22, 26], fill=(0,0,0,0))
    d.ellipse([26, 24, 34, 32], fill=ORNG)
    d.ellipse([28, 26, 32, 30], fill=(0,0,0,0))

def draw_lobstertail(d):
    # Grilled red lobster tail
    d.ellipse([12, 14, 38, 36], fill=RED)
    # Tail fan fins
    d.polygon([(12, 14), (20, 10), (16, 20)], fill=DRED)
    d.polygon([(38, 14), (30, 10), (34, 20)], fill=DRED)

def draw_oysters(d):
    # Oyster on shell
    d.ellipse([12, 14, 38, 36], fill=DGY) # shell
    d.ellipse([16, 18, 34, 32], fill=LBLU) # oyster meat

def draw_paella(d):
    d.ellipse([10, 10, 40, 40], fill=BK) # black pan
    d.ellipse([12, 12, 38, 38], fill=ORNG) # saffron yellow rice
    # Mussels (black shell, orange meat)
    d.ellipse([16, 18, 20, 22], fill=BK)
    d.ellipse([28, 26, 32, 30], fill=BK)

def draw_crabcake(d):
    d.ellipse([12, 22, 38, 38], fill=WH) # Plate
    # Pan-fried crab cake patty
    d.ellipse([16, 20, 34, 34], fill=BRN)
    # Green herb flakes
    d.point((22, 26), fill=GRN)

def draw_clambake(d):
    d.ellipse([11, 20, 39, 38], fill=BLU) # Pot
    d.ellipse([11, 16, 39, 24], fill=WH) # Clams/corn heap
    d.ellipse([22, 15, 28, 21], fill=YEL) # corn cob piece

def draw_beefstew(d):
    d.ellipse([12, 22, 38, 38], fill=RED) # Bowl
    d.ellipse([12, 18, 38, 26], fill=DBRN) # Brown gravy
    # Beef and carrot chunks
    d.rectangle([18, 20, 21, 23], fill=BRN)
    d.ellipse([26, 21, 29, 24], fill=ORNG)

def draw_beefwellington(d):
    # Pastry wrapped steak slice showing pink meat center
    d.ellipse([12, 14, 38, 36], fill=LBRN) # golden pastry outer
    d.ellipse([16, 18, 34, 32], fill=PNK) # pink steak center
    d.ellipse([18, 20, 32, 30], fill=RED)

def draw_porkchop(d):
    d.ellipse([12, 22, 38, 38], fill=WH) # Plate
    # Grilled chop
    d.ellipse([14, 18, 36, 32], fill=LBRN)
    # Bone end
    d.rectangle([12, 24, 16, 28], fill=WH)

def draw_ribs(d):
    d.rectangle([12, 16, 38, 34], fill=DBRN) # slab of ribs
    # Sauce sheen lines
    d.line([(14, 20), (36, 20)], fill=RED, width=1)
    d.line([(14, 28), (36, 28)], fill=RED, width=1)

def draw_meatloaf(d):
    # Slice of meatloaf
    d.rectangle([14, 16, 36, 36], fill=BRN)
    # Red ketchup glaze topping
    d.rectangle([14, 16, 36, 22], fill=RED)

def draw_potroast(d):
    d.ellipse([12, 22, 38, 38], fill=WH) # Plate
    # Sliced beef roast with gravy
    d.rectangle([16, 20, 34, 32], fill=DBRN)
    d.ellipse([20, 24, 30, 28], fill=BRN)

def draw_chickenpotpie(d):
    d.ellipse([12, 18, 38, 38], fill=LBRN) # Crust dome
    # Cut out section showing veggie filling
    d.polygon([(25, 25), (18, 38), (32, 38)], fill=YEL) # gravy
    d.point((22, 32), fill=GRN) # pea

def draw_chickenwings(d):
    d.ellipse([12, 22, 38, 38], fill=WH) # Plate
    # Buffalo wings (red/orange wings)
    d.ellipse([15, 20, 25, 28], fill=ORNG)
    d.ellipse([25, 22, 35, 30], fill=ORNG)

def draw_chickennuggets(d):
    d.ellipse([12, 22, 38, 38], fill=WH) # Plate
    # Three nuggets
    d.ellipse([16, 24, 22, 30], fill=LBRN)
    d.ellipse([24, 22, 30, 28], fill=LBRN)
    d.ellipse([22, 28, 28, 34], fill=LBRN)

def draw_quesofundido(d):
    d.ellipse([12, 12, 38, 38], fill=BK) # skillet
    d.ellipse([14, 14, 36, 36], fill=YEL) # melted cheese
    # Red chorizo bits on top
    for cx, cy in [(18, 20), (28, 22), (24, 28)]:
        d.point((cx, cy), fill=RED)

def draw_empanada(d):
    # Golden pastry pocket
    d.ellipse([10, 16, 40, 36], fill=LBRN)
    d.rectangle([10, 16, 40, 26], fill=(0,0,0,0)) # half circle
    # Crimped edge lines
    for x in range(12, 38, 4):
        d.line([(x, 26), (x, 28)], fill=BRN, width=1)

def draw_arepa(d):
    d.ellipse([12, 14, 38, 38], fill=CREAM) # corn cake
    # Cheese filling showing inside
    d.rectangle([12, 24, 38, 28], fill=YEL)

def draw_pupusa(d):
    d.ellipse([12, 12, 38, 38], fill=CREAM)
    # Cheese oozing out at edge
    d.ellipse([10, 22, 14, 28], fill=YEL)

def draw_ceviche(d):
    d.ellipse([12, 22, 38, 38], fill=BLU) # Bowl
    d.ellipse([12, 18, 38, 26], fill=WH) # Marinated fish
    # Lime (green) & onion (purple) specs
    for lx, ly in [(18, 20), (28, 22)]:
        d.point((lx, ly), fill=GRN)
    for px, py in [(22, 24), (25, 19)]:
        d.point((px, py), fill=PURP)

def draw_tostada(d):
    d.ellipse([12, 24, 38, 38], fill=YEL) # flat crispy shell
    # Toppings
    d.rectangle([15, 20, 35, 28], fill=GRN) # lettuce
    d.ellipse([21, 18, 29, 24], fill=RED) # salsa

def draw_chilesrellenos(d):
    d.ellipse([12, 22, 38, 38], fill=WH) # Plate
    # Stuffed pepper (green) in red sauce
    d.ellipse([14, 20, 36, 32], fill=RED) # sauce
    d.ellipse([18, 22, 32, 28], fill=GRN) # pepper

def draw_tamale(d):
    # Corn husk wrapped tamale
    d.rectangle([14, 18, 36, 32], fill=YEL)
    # Husk ties
    d.line([(18, 18), (18, 32)], fill=BRN, width=2)
    d.line([(32, 18), (32, 32)], fill=BRN, width=2)

def draw_elote(d):
    d.line([10, 38, 40, 12], fill=YEL, width=6) # Corn cob
    # White cotija cheese crumbles coating
    for x in range(15, 36, 4):
        d.point((x, 48-x), fill=WH)

def draw_chilaquiles(d):
    d.ellipse([12, 22, 38, 38], fill=RED) # Bowl
    # Simmered green chips
    for x, y in [(16, 20), (24, 22), (30, 21)]:
        d.polygon([(x, y), (x+6, y-3), (x+3, y+5)], fill=GRN)
    # Fried egg on top
    d.ellipse([22, 18, 28, 24], fill=WH)
    d.point((25, 21), fill=YEL)

def draw_poutine(d):
    d.ellipse([12, 22, 38, 38], fill=WH) # Plate
    # Fries
    for x in range(16, 34, 3):
        d.rectangle([x, 22, x+2, 34], fill=YEL)
    # Curds (white cubes) & gravy (brown drizzle)
    for cx, cy in [(18, 24), (28, 26), (23, 28)]:
        d.rectangle([cx, cy, cx+2, cy+2], fill=WH)
    d.line([(16, 26), (34, 26)], fill=BRN, width=2)

def draw_shepherdspie(d):
    d.rectangle([12, 14, 38, 36], fill=DBRN) # casserole
    # Mashed potato peaks (whipped white peak rows)
    for y in [18, 26, 34]:
        d.line([(14, y), (36, y)], fill=WH, width=2)

def draw_scotchegg(d):
    # Breaded sausage ball split open showing egg center
    d.ellipse([12, 14, 38, 36], fill=LBRN) # breaded outer
    d.ellipse([16, 18, 34, 32], fill=WH) # egg white
    d.ellipse([20, 22, 30, 28], fill=YEL) # egg yolk

def draw_bangersmash(d):
    d.ellipse([12, 22, 38, 38], fill=WH) # Plate
    d.ellipse([15, 18, 35, 32], fill=CREAM) # Mashed potatoes
    # Sausage links (bangers)
    d.line([(16, 22), (28, 26)], fill=BRN, width=4)
    d.line([(22, 26), (34, 30)], fill=BRN, width=4)

def draw_fishcake(d):
    d.ellipse([12, 22, 38, 38], fill=WH) # Plate
    # Pan-fried fish patty (golden brown)
    d.ellipse([16, 20, 34, 34], fill=LBRN)
    d.ellipse([18, 22, 32, 32], fill=CREAM)

def draw_croquemonsieur(d):
    d.rectangle([12, 12, 38, 36], fill=LBRN) # toast
    d.rectangle([12, 12, 38, 18], fill=WH) # white sauce topping
    d.line([(12, 26), (38, 26)], fill=PNK, width=2) # ham showing in middle

def draw_quiche(d):
    # Slice of egg quiche showing fillings
    d.polygon([(10, 34), (40, 34), (25, 14)], fill=YEL)
    d.line([(40, 34), (25, 14)], fill=BRN, width=2) # crust
    # Spinach (green specks) and bacon (red specks)
    for sx, sy in [(16, 28), (28, 30), (22, 20)]:
        d.point((sx, sy), fill=GRN)
    for rx, ry in [(20, 28), (24, 25)]:
        d.point((rx, ry), fill=RED)

def draw_ratatouille(d):
    # Layers of baked sliced vegetables
    d.ellipse([12, 12, 38, 38], fill=RED) # tomato sauce bottom
    # Layered green/purple/red rings
    d.arc([16, 16, 34, 34], 0, 360, fill=GRN, width=2)
    d.arc([19, 19, 31, 31], 0, 360, fill=PURP, width=2)
    d.arc([22, 22, 28, 28], 0, 360, fill=RED, width=2)

def draw_escargot(d):
    # Snail shells with garlic butter pool
    d.ellipse([12, 22, 38, 38], fill=WH) # Plate
    # Snails
    d.ellipse([16, 22, 24, 30], fill=BRN)
    d.ellipse([26, 24, 34, 32], fill=BRN)
    # Green herb butter pools
    d.point((20, 26), fill=GRN)
    d.point((30, 28), fill=GRN)

def draw_fondue(d):
    d.ellipse([12, 22, 38, 38], fill=WH) # Plate
    # Pot of cheese
    d.rectangle([14, 18, 36, 34], fill=RED)
    d.ellipse([14, 14, 36, 22], fill=YEL) # melted cheese top
    # Bread cube dipping fork
    d.line([(25, 4), (25, 16)], fill=WH, width=1)
    d.rectangle([23, 14, 27, 18], fill=LBRN)

def draw_pierogi(d):
    d.ellipse([12, 22, 38, 38], fill=WH) # Plate
    # Dumplings with fried onion toppings
    d.ellipse([16, 24, 28, 32], fill=CREAM)
    d.ellipse([24, 22, 36, 30], fill=CREAM)
    # Butter glaze/onions (brown dots)
    d.point((22, 26), fill=BRN)
    d.point((30, 24), fill=BRN)

def draw_goulash(d):
    d.ellipse([12, 22, 38, 38], fill=RED) # Bowl
    d.ellipse([12, 18, 38, 26], fill=DRED) # Paprika red stew
    # Noodles
    d.line([(16, 19), (34, 21)], fill=YEL, width=2)

def draw_schnitzel(d):
    d.ellipse([12, 22, 38, 38], fill=WH) # Plate
    # Crispy pork cutlet
    d.ellipse([14, 18, 36, 32], fill=LBRN)
    # Lemon wedge
    d.polygon([(16, 16), (22, 12), (20, 18)], fill=YEL)

def draw_borsch(d):
    d.ellipse([12, 22, 38, 38], fill=RED) # Bowl
    d.ellipse([12, 18, 38, 26], fill=DRED) # Beet red soup
    # Sour cream swirl (white)
    d.ellipse([22, 20, 28, 24], fill=WH)

def draw_khachapuri(d):
    # Bread boat with egg yolk
    d.ellipse([12, 16, 38, 34], fill=LBRN)
    d.ellipse([16, 19, 34, 31], fill=WH) # cheese inside boat
    # Egg yolk center
    d.ellipse([22, 22, 28, 28], fill=YEL)

def draw_gelatin(d):
    # Wobbly ring jelly mold
    d.ellipse([12, 16, 38, 38], fill=RED)
    d.ellipse([20, 22, 30, 32], fill=(0,0,0,0)) # center hole ring shape

def draw_ricepudding(d):
    d.ellipse([12, 22, 38, 38], fill=BLU) # Bowl
    d.ellipse([12, 18, 38, 26], fill=WH) # Rice pudding
    # Cinnamon dust specs
    for sx, sy in [(18, 20), (28, 22), (24, 24)]:
        d.point((sx, sy), fill=BRN)

def draw_breadpudding(d):
    # Baked custard bread squares
    d.rectangle([12, 14, 38, 36], fill=LBRN)
    # Squares cut lines
    d.line([(25, 14), (25, 36)], fill=BRN, width=1)
    d.line([(12, 25), (38, 25)], fill=BRN, width=1)

def draw_fruitcrisp(d):
    d.ellipse([12, 18, 38, 38], fill=BRN) # baking dish
    # Oats crisp texture top
    for x in range(14, 36, 3):
        d.point((x, 22), fill=LBRN)
        d.point((x+1, 26), fill=DBRN)

def draw_stickypudding(d):
    d.ellipse([12, 32, 38, 38], fill=WH) # Plate
    # Dark cake
    d.rectangle([14, 18, 36, 34], fill=DBRN)
    # Toffee caramel sauce glaze pouring
    d.polygon([(18, 14), (32, 14), (28, 34), (22, 34)], fill=BRN)

def draw_lavacake(d):
    # Cake split showing hot chocolate oozing out
    d.ellipse([12, 16, 38, 36], fill=DBRN)
    # Oozing center
    d.polygon([(25, 24), (20, 34), (30, 34)], fill=BROWN)

def draw_pavlova(d):
    # Meringue cake topped with cream/kiwi/strawberry
    d.ellipse([12, 18, 38, 38], fill=WH) # meringue
    d.ellipse([18, 20, 32, 30], fill=WH) # cream
    d.point((22, 22), fill=RED) # strawberry
    d.point((28, 22), fill=GRN) # kiwi

def draw_profiteroles(d):
    # Cream puff stack
    d.ellipse([16, 24, 24, 32], fill=LBRN)
    d.ellipse([26, 24, 34, 32], fill=LBRN)
    d.ellipse([21, 16, 29, 24], fill=LBRN)
    # Chocolate drizzle
    d.line([(21, 15), (29, 32)], fill=DBRN, width=1)

def draw_shortcake(d):
    # Biscuit sandwich
    d.ellipse([12, 14, 38, 22], fill=LBRN) # top biscuit
    # Strawberries & cream center
    d.rectangle([12, 22, 38, 28], fill=WH) # cream
    d.ellipse([22, 22, 28, 28], fill=RED) # strawberry
    d.ellipse([12, 28, 38, 36], fill=LBRN) # bottom biscuit

def draw_fruitcobbler(d):
    d.ellipse([12, 18, 38, 38], fill=BRN) # dish
    d.ellipse([14, 20, 36, 36], fill=RED) # berry cobbler base
    # Biscuit drops on top (little cream circles)
    for bx, by in [(18, 22), (28, 24), (23, 29)]:
        d.ellipse([bx-2, by-2, bx+2, by+2], fill=CREAM)


def draw_omelette(d):
    # Shadow
    d.ellipse([10, 28, 42, 38], fill=DBRN)
    # Folded egg
    d.chord([10, 16, 40, 36], start=0, end=180, fill=YEL)
    d.chord([12, 18, 38, 34], start=0, end=180, fill=CREAM)
    # Herbs & Tomatoes
    for x, y in [(16, 22), (24, 20), (30, 24), (34, 28)]:
        d.ellipse([x, y, x+3, y+3], fill=RED)
    for x, y in [(14, 26), (20, 22), (28, 26), (36, 24)]:
        d.ellipse([x, y, x+2, y+2], fill=GRN)

def draw_macaroni(d):
    # Bowl
    d.ellipse([8, 22, 42, 40], fill=LBLU)
    d.ellipse([8, 16, 42, 28], fill=WH)
    # Macaroni
    d.ellipse([10, 18, 40, 26], fill=ORNG)
    for x, y in [(14, 18), (20, 20), (28, 18), (34, 22), (18, 24), (26, 22)]:
        d.arc([x, y, x+6, y+4], start=180, end=0, fill=YEL, width=2)

def draw_tomatosoup(d):
    # Bowl
    d.ellipse([8, 22, 42, 40], fill=WH)
    d.ellipse([8, 16, 42, 28], fill=LBLU)
    # Soup
    d.ellipse([12, 18, 38, 26], fill=RED)
    # Cream swirl
    d.arc([18, 20, 32, 24], start=0, end=180, fill=WH, width=2)
    d.arc([14, 20, 28, 24], start=180, end=360, fill=WH, width=2)
    # Basil
    d.ellipse([26, 18, 30, 22], fill=GRN)
    d.ellipse([22, 18, 26, 20], fill=DGRN)

def draw_chickensoup(d):
    # Bowl
    d.ellipse([8, 22, 42, 40], fill=WH)
    d.ellipse([8, 16, 42, 28], fill=WH)
    # Broth
    d.ellipse([10, 18, 40, 26], fill=YEL)
    # Carrots, chicken, celery
    for x, y in [(14, 20), (28, 24), (32, 20)]:
        d.rectangle([x, y, x+3, y+3], fill=ORNG)
    for x, y in [(20, 22), (36, 24), (16, 24)]:
        d.rectangle([x, y, x+4, y+2], fill=CREAM)
    for x, y in [(24, 20), (34, 22)]:
        d.ellipse([x, y, x+2, y+2], fill=GRN)

def draw_fishtaco(d):
    # Tortilla
    d.polygon([(10, 16), (20, 40), (40, 36), (36, 12)], fill=WH)
    d.polygon([(12, 18), (20, 38), (38, 34), (34, 14)], fill=CREAM)
    # Fish chunks
    d.polygon([(16, 20), (22, 36), (30, 32), (28, 18)], fill=LBRN)
    d.polygon([(18, 22), (22, 34), (28, 30), (26, 20)], fill=WH)
    # Cabbage and sauce
    for x, y in [(18, 20), (22, 26), (26, 32), (32, 22)]:
        d.rectangle([x, y, x+2, y+2], fill=GRN)
    d.line([(20, 18), (28, 34)], fill=WH, width=2)

def draw_sausage(d):
    # Grill plate
    d.ellipse([6, 26, 44, 40], fill=DGY)
    d.line([(10, 30), (40, 30)], fill=BK, width=1)
    d.line([(8, 34), (42, 34)], fill=BK, width=1)
    # Sausage
    d.ellipse([10, 16, 40, 32], fill=DBRN)
    d.ellipse([12, 18, 38, 30], fill=BRN)
    # Grill marks
    for x in range(16, 36, 6):
        d.line([(x, 18), (x+4, 30)], fill=DBRN, width=2)
    # Mustard
    d.line([(14, 22), (36, 26)], fill=YEL, width=2)

def draw_meatpie(d):
    # Tin
    d.polygon([(12, 24), (38, 24), (34, 40), (16, 40)], fill=DGY)
    # Crust
    d.ellipse([8, 16, 42, 28], fill=LBRN)
    d.ellipse([10, 18, 40, 26], fill=BRN)
    # Steam
    d.line([(20, 8), (22, 14)], fill=WH, width=1)
    d.line([(25, 6), (27, 12)], fill=WH, width=1)
    d.line([(30, 8), (32, 14)], fill=WH, width=1)

def draw_quesodip(d):
    # Bowl
    d.ellipse([10, 20, 40, 42], fill=DGY)
    d.ellipse([10, 16, 40, 26], fill=WH)
    # Queso
    d.ellipse([12, 18, 38, 24], fill=YEL)
    # Peppers
    d.point((20, 20), fill=RED)
    d.point((28, 22), fill=GRN)
    d.point((24, 22), fill=RED)
    # Chips
    d.polygon([(6, 12), (16, 20), (12, 26)], fill=LBRN)
    d.polygon([(34, 12), (44, 16), (36, 24)], fill=LBRN)

def draw_potatochips(d):
    # Shadow
    d.ellipse([8, 30, 42, 44], fill=DBRN)
    # Chips (wavy ovals)
    chips = [(16, 24), (26, 22), (32, 28), (14, 32), (24, 32)]
    for cx, cy in chips:
        d.ellipse([cx-6, cy-8, cx+6, cy+8], fill=BRN)
        d.ellipse([cx-5, cy-7, cx+5, cy+7], fill=YEL)
        d.arc([cx-4, cy-6, cx+4, cy+6], start=0, end=180, fill=LBRN, width=1)
        d.arc([cx-4, cy-2, cx+4, cy+2], start=180, end=360, fill=LBRN, width=1)

def draw_poptart(d):
    # Pastry
    d.rectangle([10, 10, 40, 40], fill=BRN)
    d.rectangle([12, 12, 38, 38], fill=LBRN)
    # Frosting
    d.rectangle([14, 14, 36, 36], fill=WH)
    # Sprinkles
    colors = [RED, BLU, YEL, GRN, ORNG, PNK]
    pts = [(18,18), (28,16), (32,24), (20,30), (28,34), (16,24), (24,24)]
    for i, (x, y) in enumerate(pts):
        d.rectangle([x, y, x+1, y+1], fill=colors[i % len(colors)])

def draw_onionrings(d):
    # Basket
    d.polygon([(10, 26), (40, 26), (36, 42), (14, 42)], fill=RED)
    # Rings
    d.ellipse([14, 14, 28, 28], outline=BRN, width=3)
    d.ellipse([15, 15, 27, 27], outline=YEL, width=2)
    
    d.ellipse([22, 12, 36, 26], outline=BRN, width=3)
    d.ellipse([23, 13, 35, 25], outline=YEL, width=2)
    
    d.ellipse([18, 20, 32, 34], outline=BRN, width=3)
    d.ellipse([19, 21, 31, 33], outline=YEL, width=2)

def draw_turnover(d):
    # Triangular pastry
    d.polygon([(10, 36), (40, 36), (25, 12)], fill=BRN)
    d.polygon([(13, 34), (37, 34), (25, 15)], fill=LBRN)
    # Slits
    d.line([(20, 24), (25, 20)], fill=DBRN, width=1)
    d.line([(25, 30), (30, 26)], fill=DBRN, width=1)
    # Cherry filling peeking out
    d.ellipse([21, 23, 23, 25], fill=RED)
    d.ellipse([26, 29, 28, 31], fill=RED)
    # Glaze
    d.line([(15, 25), (35, 32)], fill=WH, width=2)

def draw_friedchicken(d):
    # Bucket
    d.polygon([(12, 28), (38, 28), (34, 46), (16, 46)], fill=RED)
    d.line([(16, 34), (34, 34)], fill=WH, width=2)
    # Chicken pieces
    d.ellipse([14, 14, 26, 26], fill=BRN)
    d.ellipse([16, 16, 24, 24], fill=ORNG)
    
    d.ellipse([24, 12, 36, 24], fill=BRN)
    d.ellipse([26, 14, 34, 22], fill=ORNG)
    
    d.ellipse([18, 20, 32, 32], fill=BRN)
    d.ellipse([20, 22, 30, 30], fill=ORNG)
    # Crispy texture
    d.point((18, 18), fill=DBRN)
    d.point((30, 16), fill=DBRN)
    d.point((24, 26), fill=DBRN)

def draw_beefjerky(d):
    # Wood board
    d.polygon([(8, 36), (42, 36), (46, 42), (4, 42)], fill=LBRN)
    # Jerky strips
    d.polygon([(12, 14), (18, 12), (24, 34), (16, 36)], fill=DBRN)
    d.polygon([(22, 16), (28, 14), (34, 32), (26, 34)], fill=DBRN)
    d.polygon([(32, 12), (38, 10), (42, 30), (36, 32)], fill=DBRN)
    # Meat texture
    for x, y in [(16, 24), (26, 24), (36, 20)]:
        d.line([(x, y), (x+2, y+6)], fill=BRN, width=1)
        d.line([(x-2, y-4), (x, y+2)], fill=DRED, width=1)

def draw_grilledcheese(d):
    # Plate
    d.ellipse([6, 32, 44, 42], fill=WH)
    # Bottom sandwich half
    d.polygon([(12, 34), (38, 34), (25, 20)], fill=BRN)
    d.polygon([(14, 32), (36, 32), (25, 22)], fill=LBRN)
    # Cheese melt
    d.polygon([(16, 32), (34, 32), (25, 36)], fill=YEL)
    # Top sandwich half
    d.polygon([(10, 28), (36, 28), (23, 14)], fill=BRN)
    d.polygon([(12, 26), (34, 26), (23, 16)], fill=LBRN)
    # Grill lines
    d.line([(16, 22), (24, 28)], fill=DBRN, width=1)
    d.line([(22, 18), (30, 24)], fill=DBRN, width=1)

def draw_clubsandwich(d):
    # Toothpick
    d.line([(25, 8), (25, 38)], fill=LBRN, width=2)
    d.ellipse([23, 6, 27, 10], fill=RED)
    # Layers (bread, lettuce, tomato, turkey, bacon)
    y_offsets = [14, 22, 30]
    for y in y_offsets:
        d.polygon([(14, y), (36, y), (25, y+8)], fill=LBRN)
        if y != 30:
            d.line([(16, y+2), (34, y+2)], fill=GRN, width=1)
            d.line([(18, y+4), (32, y+4)], fill=RED, width=1)
            d.line([(20, y+6), (30, y+6)], fill=CREAM, width=1)

def draw_blt(d):
    # Sandwich stacked
    d.ellipse([12, 30, 38, 40], fill=BRN)
    d.ellipse([14, 32, 36, 38], fill=LBRN)
    
    # Bacon
    d.line([(14, 26), (36, 28)], fill=DRED, width=3)
    d.line([(14, 28), (36, 30)], fill=DBRN, width=2)
    
    # Tomato
    d.ellipse([16, 22, 34, 26], fill=RED)
    
    # Lettuce
    d.polygon([(12, 20), (38, 18), (34, 24), (16, 22)], fill=GRN)
    
    # Top Bread
    d.ellipse([12, 12, 38, 22], fill=BRN)
    d.ellipse([14, 14, 36, 20], fill=LBRN)

def draw_pbtoast(d):
    # Toast
    d.polygon([(12, 16), (38, 16), (36, 38), (14, 38)], fill=BRN)
    d.polygon([(14, 18), (36, 18), (34, 36), (16, 36)], fill=LBRN)
    # Peanut butter
    d.polygon([(16, 20), (34, 20), (32, 34), (18, 34)], fill=ORNG)
    # Swirls and nut bits
    d.arc([20, 22, 30, 32], start=0, end=180, fill=BRN, width=2)
    for x, y in [(22, 24), (28, 28), (24, 30), (30, 22)]:
        d.rectangle([x, y, x+2, y+2], fill=DBRN)

def draw_frenchtoast(d):
    # Two slices stacked
    d.polygon([(14, 20), (36, 20), (34, 36), (16, 36)], fill=DBRN)
    d.polygon([(15, 21), (35, 21), (33, 35), (17, 35)], fill=BRN)
    
    d.polygon([(10, 14), (32, 14), (30, 30), (12, 30)], fill=DBRN)
    d.polygon([(11, 15), (31, 15), (29, 29), (13, 29)], fill=LBRN)
    # Butter
    d.polygon([(18, 18), (24, 16), (26, 20), (20, 22)], fill=YEL)
    # Syrup
    d.line([(24, 20), (28, 26)], fill=ORNG, width=2)
    d.line([(22, 22), (24, 32)], fill=ORNG, width=2)

def draw_oatmeal(d):
    # Bowl
    d.ellipse([8, 24, 42, 42], fill=LBLU)
    d.ellipse([8, 18, 42, 30], fill=WH)
    # Oats
    d.ellipse([12, 20, 38, 28], fill=LBRN)
    # Berries
    for x, y in [(16, 22), (20, 24), (24, 22), (28, 26), (32, 22)]:
        d.ellipse([x, y, x+4, y+4], fill=BLU)
    # Brown sugar
    d.ellipse([22, 20, 30, 24], fill=BRN)

def draw_cereal(d):
    # Bowl
    d.ellipse([8, 24, 42, 42], fill=ORNG)
    d.ellipse([8, 18, 42, 30], fill=WH)
    # Milk
    d.ellipse([10, 20, 40, 28], fill=CREAM)
    # Colorful loops
    colors = [RED, BLU, YEL, GRN, ORNG, PNK]
    pts = [(16, 22), (24, 24), (32, 22), (20, 26), (28, 26), (14, 24), (34, 24)]
    for i, (x, y) in enumerate(pts):
        d.ellipse([x, y, x+4, y+4], outline=colors[i % len(colors)], width=2)

def draw_granolabar(d):
    # Wrapper pulled down
    d.polygon([(12, 28), (38, 28), (36, 42), (14, 42)], fill=BLU)
    d.line([(14, 32), (36, 32)], fill=WH, width=2)
    # Bar
    d.polygon([(14, 10), (36, 10), (36, 28), (14, 28)], fill=LBRN)
    # Oats & Chocolate chips
    for x, y in [(16, 12), (24, 16), (32, 14), (18, 22), (28, 20)]:
        d.point((x, y), fill=DBRN)
    for x, y in [(20, 14), (28, 12), (22, 18), (30, 24)]:
        d.point((x, y), fill=WH)

def draw_smoothie(d):
    # Tall glass
    d.polygon([(14, 12), (36, 12), (32, 40), (18, 40)], fill=WH)
    # Pink smoothie
    d.polygon([(15, 16), (35, 16), (31, 38), (19, 38)], fill=PNK)
    # Highlights
    d.line([(20, 20), (18, 34)], fill=WH, width=2)
    # Straw
    d.line([(25, 4), (25, 36)], fill=GRN, width=2)
    # Fruit garnish
    d.ellipse([30, 10, 38, 18], fill=RED)
    d.ellipse([32, 12, 36, 16], fill=YEL)

def draw_applejuice(d):
    # Box
    d.rectangle([14, 16, 36, 42], fill=ORNG)
    d.rectangle([14, 10, 36, 16], fill=YEL)
    # Apple logo
    d.ellipse([20, 24, 30, 34], fill=RED)
    d.line([(25, 20), (25, 24)], fill=DBRN, width=1)
    d.ellipse([25, 20, 29, 22], fill=GRN)
    # Straw
    d.polygon([(25, 10), (28, 10), (32, 4), (29, 4)], fill=WH)

def draw_orangejuice(d):
    # Pitcher
    d.polygon([(16, 14), (34, 14), (36, 40), (14, 40)], fill=WH)
    d.arc([34, 20, 42, 34], start=270, end=90, fill=WH, width=3)
    # Juice
    d.polygon([(17, 20), (33, 20), (34, 38), (16, 38)], fill=ORNG)
    # Orange slice on rim
    d.ellipse([10, 10, 20, 20], fill=ORNG)
    d.ellipse([12, 12, 18, 18], fill=YEL)

def draw_lemonade(d):
    # Glass jar
    d.rectangle([14, 16, 36, 40], fill=WH)
    d.rectangle([12, 12, 38, 16], fill=LBLU)
    # Yellow lemonade
    d.rectangle([16, 20, 34, 38], fill=YEL)
    # Ice cubes & lemon
    d.rectangle([18, 24, 22, 28], outline=WH, width=1)
    d.rectangle([26, 30, 30, 34], outline=WH, width=1)
    d.ellipse([24, 22, 32, 30], fill=CREAM)
    # Straw
    d.line([(25, 6), (25, 38)], fill=RED, width=2)

def draw_hottea(d):
    # Teacup
    d.ellipse([10, 20, 40, 36], fill=WH)
    d.arc([36, 22, 44, 32], start=270, end=90, fill=WH, width=2)
    # Saucer
    d.ellipse([6, 32, 44, 42], fill=LBLU)
    # Tea
    d.ellipse([14, 22, 36, 28], fill=BRN)
    # Tea tag
    d.line([(25, 24), (16, 12)], fill=WH, width=1)
    d.rectangle([12, 8, 18, 14], fill=YEL)

def draw_milkcarton(d):
    # Carton shape
    d.polygon([(14, 20), (36, 20), (36, 42), (14, 42)], fill=WH)
    d.polygon([(14, 20), (36, 20), (25, 10)], fill=LBLU)
    # Label / Cow spots
    d.polygon([(18, 26), (24, 24), (26, 30), (20, 32)], fill=BK)
    d.polygon([(30, 30), (34, 32), (32, 38), (28, 36)], fill=BK)
    # Text line
    d.line([(18, 36), (26, 36)], fill=BLU, width=2)

def draw_crackers(d):
    # Stack of round crackers
    y_offsets = [32, 28, 24, 20, 16]
    for y in y_offsets:
        d.ellipse([16, y, 34, y+10], fill=DBRN)
        d.ellipse([16, y, 34, y+8], fill=YEL)
        # Cracker holes
        for x, hy in [(21, y+3), (25, y+5), (29, y+3), (25, y+2)]:
            d.point((x, hy), fill=BRN)

def draw_grahamcrackers(d):
    # Rectangular cracker with perforated line
    d.polygon([(12, 16), (36, 10), (40, 30), (16, 36)], fill=BRN)
    d.polygon([(12, 14), (36, 8), (40, 28), (16, 34)], fill=LBRN)
    # Center perforation
    d.line([(24, 11), (28, 31)], fill=BRN, width=1)
    # Dots
    for x, y in [(18, 18), (22, 28), (30, 14), (34, 24)]:
        d.point((x, y), fill=DBRN)

def draw_marshmallow(d):
    # Stick
    d.line([(25, 34), (25, 46)], fill=BRN, width=2)
    # Fluffy cylinder
    d.ellipse([16, 22, 34, 34], fill=WH)
    d.rectangle([16, 14, 34, 28], fill=WH)
    d.ellipse([16, 8, 34, 20], fill=CREAM)
    # Toasted spot
    d.ellipse([20, 16, 30, 26], fill=LBRN)
    d.ellipse([24, 18, 28, 22], fill=DBRN)

def draw_smores(d):
    # Graham cracker bottom
    d.polygon([(10, 32), (40, 32), (36, 40), (14, 40)], fill=BRN)
    # Chocolate bar
    d.polygon([(12, 28), (38, 28), (34, 34), (16, 34)], fill=DBRN)
    # Melted Marshmallow
    d.ellipse([14, 22, 36, 32], fill=WH)
    d.polygon([(18, 20), (32, 20), (34, 30), (16, 30)], fill=WH)
    # Graham cracker top
    d.polygon([(12, 14), (38, 14), (36, 24), (14, 24)], fill=LBRN)
    # Crumb dots
    d.point((20, 18), fill=DBRN)
    d.point((30, 18), fill=DBRN)

def draw_caramelapple(d):
    # Stick
    d.line([(25, 6), (25, 20)], fill=LBRN, width=2)
    # Apple
    d.ellipse([14, 20, 36, 42], fill=RED)
    # Caramel coating
    d.chord([12, 18, 38, 44], start=0, end=180, fill=YEL)
    # Nut sprinkles
    for x, y in [(16, 34), (20, 38), (24, 32), (28, 36), (32, 34), (20, 30), (30, 30)]:
        d.ellipse([x, y, x+2, y+2], fill=DBRN)

def draw_cottoncandy(d):
    # Cone
    d.polygon([(22, 28), (28, 28), (25, 46)], fill=WH)
    # Fluffy cloud layers (Pink and Blue)
    d.ellipse([12, 18, 28, 32], fill=PNK)
    d.ellipse([22, 18, 38, 32], fill=LBLU)
    d.ellipse([10, 10, 30, 24], fill=LBLU)
    d.ellipse([20, 8, 40, 22], fill=PNK)
    d.ellipse([16, 4, 34, 18], fill=PNK)

def draw_snowcone(d):
    # Paper cone
    d.polygon([(16, 24), (34, 24), (25, 46)], fill=WH)
    # Syrup stripes on cone
    d.line([(18, 30), (32, 30)], fill=RED, width=2)
    d.line([(20, 36), (30, 36)], fill=BLU, width=2)
    # Ice dome
    d.chord([12, 10, 38, 34], start=180, end=0, fill=WH)
    # Flavored syrups
    d.chord([12, 10, 25, 34], start=180, end=0, fill=RED)
    d.chord([25, 10, 38, 34], start=180, end=0, fill=BLU)

def draw_fudge(d):
    # Stack of fudge squares
    d.polygon([(12, 28), (30, 22), (40, 26), (22, 32)], fill=DBRN)
    d.polygon([(12, 34), (30, 28), (40, 32), (22, 38)], fill=BRN)
    
    d.polygon([(10, 22), (28, 16), (38, 20), (20, 26)], fill=DBRN)
    d.polygon([(10, 28), (28, 22), (38, 26), (20, 32)], fill=BK)
    
    # Walnut bits
    for x, y in [(18, 22), (24, 26), (32, 20)]:
        d.ellipse([x, y, x+3, y+2], fill=YEL)

def draw_brownie(d):
    # Square brownie
    d.polygon([(12, 20), (34, 16), (40, 28), (18, 32)], fill=DBRN)
    d.polygon([(12, 28), (34, 24), (40, 36), (18, 40)], fill=BK)
    # Chocolate chips and cracks
    for x, y in [(20, 20), (28, 26), (32, 22)]:
        d.ellipse([x, y, x+2, y+2], fill=BRN)
    d.line([(16, 24), (24, 28)], fill=BRN, width=1)
    # Powdered sugar
    d.point((24, 22), fill=WH)
    d.point((30, 24), fill=WH)

def draw_trifle(d):
    # Glass bowl
    d.polygon([(12, 14), (38, 14), (32, 40), (18, 40)], fill=WH)
    # Layers (Cake, jelly, custard, cream)
    d.polygon([(14, 30), (36, 30), (33, 38), (17, 38)], fill=YEL)
    d.polygon([(13, 22), (37, 22), (36, 30), (14, 30)], fill=RED)
    d.polygon([(12, 14), (38, 14), (37, 22), (13, 22)], fill=CREAM)
    # Cream dollops & strawberries on top
    d.ellipse([16, 8, 26, 16], fill=WH)
    d.ellipse([24, 8, 34, 16], fill=WH)
    d.ellipse([22, 4, 28, 12], fill=RED)

def draw_swissroll(d):
    # Sliced spiral cake
    d.ellipse([12, 18, 38, 36], fill=DBRN)
    d.ellipse([14, 20, 36, 34], fill=BRN)
    # Cream swirl (thick white line)
    d.arc([18, 22, 32, 32], start=0, end=270, fill=WH, width=3)
    d.arc([22, 24, 28, 28], start=90, end=360, fill=WH, width=2)

def draw_plumpudding(d):
    # Pudding dome
    d.ellipse([12, 14, 38, 38], fill=DBRN)
    d.ellipse([14, 16, 36, 36], fill=BK)
    # White cream dripping
    d.chord([14, 14, 36, 28], start=180, end=0, fill=WH)
    d.polygon([(18, 26), (22, 32), (26, 26)], fill=WH)
    d.polygon([(26, 24), (30, 30), (34, 24)], fill=WH)
    # Holly & berries
    d.ellipse([22, 10, 26, 14], fill=RED)
    d.ellipse([26, 12, 30, 16], fill=RED)
    d.polygon([(18, 12), (24, 8), (22, 14)], fill=GRN)

def draw_custard(d):
    # Ramekin
    d.polygon([(12, 22), (38, 22), (34, 40), (16, 40)], fill=LBLU)
    # Custard surface
    d.ellipse([12, 18, 38, 26], fill=CREAM)
    # Caramelized spots
    d.ellipse([18, 20, 28, 24], fill=BRN)
    d.ellipse([26, 21, 32, 25], fill=YEL)
    # Spoon
    d.line([(34, 10), (28, 22)], fill=WH, width=2)
    d.ellipse([26, 20, 30, 24], fill=WH)

def draw_fruitcake(d):
    # Cake slice
    d.polygon([(12, 32), (38, 32), (32, 14), (18, 14)], fill=DBRN)
    d.polygon([(10, 34), (40, 34), (38, 32), (12, 32)], fill=BK)
    # Candied fruits
    fruits = [(20, 20, RED), (30, 24, GRN), (24, 28, YEL), (28, 18, ORNG), (22, 30, RED)]
    for x, y, col in fruits:
        d.ellipse([x, y, x+3, y+3], fill=col)

def draw_jellybeans(d):
    # Pile of shiny beans
    beans = [
        (16, 28, RED), (24, 30, YEL), (32, 26, GRN), 
        (20, 22, BLU), (28, 24, ORNG), (22, 34, PNK),
        (30, 32, PURP), (14, 32, YEL), (34, 30, RED)
    ]
    for x, y, col in beans:
        d.ellipse([x-5, y-3, x+5, y+3], fill=col)
        # Shine
        d.point((x-2, y-1), fill=WH)

def draw_gummybears(d):
    # Three bears
    colors = [RED, GRN, YEL]
    x_pos = [14, 25, 36]
    for x, col in zip(x_pos, colors):
        # Body
        d.ellipse([x-4, 24, x+4, 36], fill=col)
        # Head
        d.ellipse([x-5, 16, x+5, 26], fill=col)
        # Ears
        d.ellipse([x-6, 14, x-2, 18], fill=col)
        d.ellipse([x+2, 14, x+6, 18], fill=col)
        # Highlight
        d.ellipse([x-1, 18, x+2, 22], fill=WH)

def draw_peppermint(d):
    # Wrapper twists
    d.polygon([(16, 24), (6, 16), (6, 32)], fill=WH)
    d.polygon([(34, 24), (44, 16), (44, 32)], fill=WH)
    # Candy body
    d.ellipse([14, 14, 36, 36], fill=WH)
    # Red swirls
    d.arc([16, 16, 34, 34], start=0, end=90, fill=RED, width=4)
    d.arc([16, 16, 34, 34], start=180, end=270, fill=RED, width=4)
    d.ellipse([22, 22, 28, 28], fill=RED)

def draw_toffee(d):
    # Broken toffee shards
    d.polygon([(14, 30), (30, 16), (36, 22), (20, 38)], fill=BRN)
    d.polygon([(16, 28), (28, 18), (34, 22), (20, 34)], fill=YEL)
    
    d.polygon([(26, 38), (40, 24), (44, 32), (32, 44)], fill=BRN)
    d.polygon([(28, 36), (38, 26), (42, 32), (32, 40)], fill=YEL)
    # Nuts
    for x, y in [(24, 26), (36, 32), (20, 30)]:
        d.ellipse([x, y, x+3, y+3], fill=CREAM)

def draw_truffles(d):
    # Box
    d.polygon([(10, 20), (40, 20), (44, 36), (6, 36)], fill=RED)
    # Three truffles
    for cx, cy in [(16, 24), (25, 24), (34, 24)]:
        # Wrapper cup
        d.polygon([(cx-6, cy+8), (cx+6, cy+8), (cx+8, cy), (cx-8, cy)], fill=DBRN)
        # Truffle
        d.ellipse([cx-5, cy-6, cx+5, cy+4], fill=BRN)
        # Drizzle or powder
        d.line([(cx-3, cy-4), (cx+3, cy)], fill=WH, width=1)

def draw_yorkshirepudding(d):
    # Fluffy pastry cup
    d.ellipse([10, 18, 40, 40], fill=LBRN)
    d.ellipse([12, 16, 38, 36], fill=YEL)
    # Hollow center
    d.ellipse([16, 22, 34, 32], fill=BRN)
    # Gravy pool
    d.ellipse([18, 24, 32, 30], fill=DBRN)
    d.ellipse([20, 25, 26, 28], fill=BRN) # highlight

def draw_pigsblanket(d):
    # Three wrapped sausages
    for cy in [18, 26, 34]:
        # Sausage
        d.ellipse([14, cy-4, 36, cy+4], fill=DBRN)
        # Pastry wrap
        d.polygon([(20, cy-6), (30, cy-6), (28, cy+6), (18, cy+6)], fill=LBRN)
        d.polygon([(22, cy-4), (28, cy-4), (26, cy+4), (20, cy+4)], fill=YEL)

def draw_potatowedges(d):
    # Plate
    d.ellipse([6, 30, 44, 42], fill=WH)
    # Wedges
    for idx, (x, y) in enumerate([(16, 20), (28, 22), (22, 28)]):
        # Potato wedge shape
        d.polygon([(x-4, y-8), (x+8, y-4), (x+4, y+10)], fill=BRN) # skin
        d.polygon([(x-2, y-6), (x+6, y-4), (x+2, y+8)], fill=YEL) # flesh
        # Seasoning specks
        if idx % 2 == 0:
            d.point((x+2, y), fill=DRED)
            d.point((x, y+4), fill=GRN)

def draw_keylimepie(d):
    # Slice
    d.polygon([(10, 32), (40, 32), (25, 14)], fill=LBRN) # crust shadow
    d.polygon([(12, 30), (38, 30), (25, 16)], fill=YEL)  # filling base
    d.polygon([(14, 28), (36, 28), (25, 18)], fill=GRN)  # lime filling
    # Whipped cream star
    d.ellipse([20, 16, 30, 26], fill=WH)
    d.ellipse([22, 14, 28, 20], fill=CREAM)
    # Lime wheel slice
    d.ellipse([18, 10, 26, 18], fill=DGRN)
    d.ellipse([19, 11, 25, 17], fill=YEL)

def draw_pecanpie(d):
    # Pie slice
    d.polygon([(10, 32), (40, 32), (25, 14)], fill=DBRN) # crust
    d.polygon([(12, 30), (38, 30), (25, 16)], fill=BRN)  # filling
    # Pecan halves (detailed ovals)
    pecans = [(20, 26), (28, 26), (24, 20), (32, 28), (16, 28)]
    for px, py in pecans:
        d.ellipse([px-3, py-2, px+3, py+2], fill=DBRN)
        d.line([(px-2, py), (px+2, py)], fill=LBRN, width=1)

def draw_softtaco(d):
    # Tortilla fold
    d.polygon([(10, 16), (25, 40), (40, 16), (25, 26)], fill=CREAM)
    # Fillings
    d.polygon([(14, 20), (25, 36), (36, 20), (25, 24)], fill=DBRN) # beef
    # Lettuce & Tomato & Cheese
    for x, y in [(16, 20), (24, 22), (32, 20)]:
        d.rectangle([x, y, x+4, y+3], fill=GRN)
    for x, y in [(20, 22), (28, 20)]:
        d.rectangle([x, y, x+3, y+3], fill=RED)
    d.line([(18, 18), (32, 18)], fill=YEL, width=2) # cheese

def draw_taquitos(d):
    # Guacamole/Sour cream bed
    d.ellipse([12, 26, 38, 36], fill=GRN)
    d.ellipse([20, 24, 30, 30], fill=WH)
    # Three rolled taquitos
    for cy in [18, 24, 30]:
        d.polygon([(8, cy), (42, cy+4), (40, cy+8), (6, cy+4)], fill=BRN)
        d.polygon([(10, cy+2), (40, cy+5), (38, cy+7), (8, cy+5)], fill=YEL)

def draw_corndog(d):
    # Stick
    d.line([(25, 34), (25, 46)], fill=LBRN, width=3)
    # Breading
    d.ellipse([16, 8, 34, 36], fill=BRN)
    d.ellipse([18, 10, 32, 34], fill=ORNG)
    # Mustard drizzle
    d.line([(22, 12), (28, 16), (22, 20), (28, 24), (22, 28), (28, 32)], fill=YEL, width=2)

def draw_chickentenders(d):
    # Basket
    d.polygon([(10, 30), (40, 30), (36, 44), (14, 44)], fill=RED)
    d.line([(14, 36), (36, 36)], fill=WH, width=2)
    # Tenders
    for cx, cy in [(18, 20), (32, 22), (25, 26)]:
        d.ellipse([cx-6, cy-10, cx+6, cy+10], fill=BRN)
        d.ellipse([cx-4, cy-8, cx+4, cy+8], fill=YEL)
        d.point((cx-1, cy), fill=DBRN)

def draw_mozzarellasticks(d):
    # Plate
    d.ellipse([6, 32, 44, 42], fill=WH)
    # Three sticks stacked
    for y in [28, 24, 20]:
        d.rectangle([14, y, 36, y+6], fill=BRN)
        d.rectangle([16, y+1, 34, y+5], fill=YEL)
        # Herb flecks
        d.point((20, y+3), fill=GRN)
        d.point((30, y+2), fill=GRN)
    # Marinara dip bowl
    d.ellipse([8, 16, 20, 24], fill=WH)
    d.ellipse([10, 18, 18, 22], fill=RED)

def draw_garlicshrimp(d):
    # Cast iron skillet
    d.ellipse([6, 16, 44, 42], fill=BK)
    d.ellipse([8, 18, 42, 40], fill=DGY)
    # Shrimp
    for cx, cy in [(20, 24), (32, 28), (26, 34)]:
        d.arc([cx-6, cy-6, cx+6, cy+6], start=90, end=360, fill=PNK, width=4)
        d.polygon([(cx+6, cy-6), (cx+10, cy-8), (cx+10, cy-2)], fill=RED) # tail
        # Garlic bits
        d.ellipse([cx-2, cy-2, cx+1, cy+1], fill=YEL)

def draw_bakedbeans(d):
    # Clay pot
    d.polygon([(10, 22), (40, 22), (36, 40), (14, 40)], fill=DBRN)
    d.polygon([(12, 24), (38, 24), (34, 38), (16, 38)], fill=BRN)
    # Bean surface
    d.ellipse([10, 18, 40, 28], fill=DRED)
    # Individual beans
    for x, y in [(16, 22), (22, 20), (28, 24), (32, 22), (20, 24), (26, 20)]:
        d.ellipse([x, y, x+4, y+3], fill=RED)
        d.point((x+1, y+1), fill=WH)

def draw_ricekrispies(d):
    # Square treat
    d.polygon([(14, 16), (36, 12), (40, 30), (18, 34)], fill=LBRN)
    d.polygon([(14, 20), (36, 16), (36, 30), (14, 34)], fill=CREAM)
    # Marshmallow strings and krispy bumps
    for x in range(16, 36, 4):
        for y in range(18, 32, 4):
            d.ellipse([x, y, x+2, y+2], fill=WH)
            d.point((x+1, y), fill=YEL)

def draw_animalcrackers(d):
    # Box string
    d.line([(25, 6), (25, 16)], fill=WH, width=1)
    # Circus box
    d.polygon([(14, 16), (36, 16), (36, 42), (14, 42)], fill=RED)
    d.polygon([(16, 18), (34, 18), (34, 30), (16, 30)], fill=YEL)
    # Animal shapes on box
    d.ellipse([18, 22, 24, 26], fill=RED) # elephant
    d.ellipse([26, 22, 32, 26], fill=RED) # lion
    d.line([(18, 34), (32, 34)], fill=WH, width=2)
    d.line([(18, 38), (32, 38)], fill=WH, width=2)

def draw_pretzelbites(d):
    # Paper cup
    d.polygon([(16, 26), (34, 26), (30, 44), (20, 44)], fill=WH)
    d.line([(18, 34), (32, 34)], fill=RED, width=2)
    # Bites piled up
    bites = [(20, 22), (28, 24), (24, 18), (32, 20), (16, 26)]
    for bx, by in bites:
        d.ellipse([bx-4, by-4, bx+4, by+4], fill=DBRN)
        d.ellipse([bx-3, by-3, bx+3, by+3], fill=BRN)
        # Salt
        d.point((bx-1, by-1), fill=WH)
        d.point((bx+1, by+1), fill=WH)

def draw_bananabread(d):
    # Thick slice
    d.polygon([(12, 34), (38, 34), (38, 16), (25, 10), (12, 16)], fill=DBRN) # crust
    d.polygon([(14, 32), (36, 32), (36, 18), (25, 12), (14, 18)], fill=BRN)  # cake
    # Walnut and banana mash textures
    for x, y in [(20, 20), (28, 26), (22, 28), (30, 20)]:
        d.ellipse([x, y, x+3, y+2], fill=YEL)
    for x, y in [(18, 26), (32, 24), (26, 22)]:
        d.ellipse([x, y, x+2, y+2], fill=BK)

def draw_meatballsub(d):
    # Sub roll
    d.ellipse([8, 16, 42, 36], fill=BRN)
    d.ellipse([10, 18, 40, 34], fill=LBRN)
    # Meatballs
    for cx in [16, 25, 34]:
        d.ellipse([cx-5, 20, cx+5, 30], fill=DBRN)
    # Marinara & Cheese
    d.line([(12, 28), (38, 28)], fill=RED, width=4)
    d.line([(14, 26), (20, 30), (26, 26), (32, 30), (36, 26)], fill=WH, width=2)

def draw_pulledpork(d):
    # Bun top
    d.ellipse([10, 10, 40, 24], fill=BRN)
    d.ellipse([12, 12, 38, 22], fill=LBRN)
    # Shredded pork
    d.polygon([(12, 20), (38, 20), (40, 32), (10, 32)], fill=DBRN)
    for x, y in [(14, 24), (20, 28), (28, 26), (34, 30), (24, 22)]:
        d.line([(x, y), (x+4, y+2)], fill=RED, width=2) # BBQ sauce
    # Bun bottom
    d.ellipse([10, 30, 40, 38], fill=LBRN)

def draw_eggsaladsandwich(d):
    # White bread slices
    d.polygon([(10, 34), (40, 34), (25, 10)], fill=LBRN) # crust
    d.polygon([(12, 32), (38, 32), (25, 12)], fill=WH)
    # Egg salad filling bursting out
    d.polygon([(14, 26), (36, 26), (34, 32), (16, 32)], fill=YEL)
    d.polygon([(16, 28), (34, 28), (32, 30), (18, 30)], fill=CREAM)
    # Celery and paprika
    for x, y in [(20, 28), (28, 28), (24, 30)]:
        d.point((x, y), fill=GRN)
    d.point((25, 27), fill=RED)

def draw_tunamelt(d):
    # Bread
    d.polygon([(12, 20), (38, 16), (40, 36), (14, 40)], fill=BRN)
    d.polygon([(14, 22), (36, 18), (38, 34), (16, 38)], fill=LBRN)
    # Tuna
    d.polygon([(16, 24), (34, 20), (36, 28), (18, 32)], fill=CREAM)
    # Melted Cheese
    d.polygon([(16, 22), (34, 18), (36, 24), (18, 28)], fill=YEL)
    # Drip
    d.polygon([(24, 24), (28, 22), (26, 30)], fill=YEL)
    # Tomato slice
    d.ellipse([22, 18, 30, 24], fill=RED)

def draw_fishburger(d):
    # Bun
    d.ellipse([12, 12, 38, 24], fill=BRN)
    d.ellipse([14, 14, 36, 22], fill=LBRN)
    # Square fish patty
    d.polygon([(14, 22), (36, 22), (38, 30), (12, 30)], fill=BRN)
    d.polygon([(16, 24), (34, 24), (36, 28), (14, 28)], fill=YEL)
    # Tartar sauce and lettuce
    d.line([(18, 22), (32, 22)], fill=WH, width=3)
    d.line([(10, 30), (40, 30)], fill=GRN, width=2)
    # Bottom bun
    d.ellipse([12, 32, 38, 40], fill=LBRN)

def draw_sliders(d):
    # Three mini burgers
    for cx, cy in [(14, 24), (25, 28), (36, 24)]:
        d.ellipse([cx-7, cy-8, cx+7, cy-2], fill=LBRN) # top
        d.rectangle([cx-6, cy-2, cx+6, cy+2], fill=DBRN) # patty
        d.line([(cx-7, cy-1), (cx+7, cy-1)], fill=YEL, width=1) # cheese
        d.ellipse([cx-7, cy+2, cx+7, cy+6], fill=LBRN) # bottom

def draw_potatoskins(d):
    # Two loaded potato skins
    skins = [(18, 26), (32, 22)]
    for cx, cy in skins:
        # Skin boat
        d.ellipse([cx-8, cy-6, cx+8, cy+6], fill=DBRN)
        d.ellipse([cx-6, cy-4, cx+6, cy+4], fill=BRN)
        # Cheese and Bacon
        d.ellipse([cx-4, cy-2, cx+4, cy+2], fill=YEL)
        d.point((cx-2, cy), fill=RED)
        d.point((cx+2, cy-1), fill=RED)
        # Sour cream
        d.ellipse([cx-2, cy-3, cx+2, cy+1], fill=WH)
        d.point((cx, cy-2), fill=GRN) # chive

def draw_tatertots(d):
    # Basket
    d.polygon([(10, 26), (40, 26), (34, 44), (16, 44)], fill=DGY)
    d.polygon([(12, 28), (38, 28), (32, 42), (18, 42)], fill=BK)
    # Tots (golden brown cylinders)
    tots = [(16, 24), (24, 22), (32, 24), (20, 28), (28, 28), (24, 34)]
    for tx, ty in tots:
        d.rectangle([tx-4, ty-3, tx+4, ty+3], fill=DBRN)
        d.rectangle([tx-3, ty-2, tx+3, ty+2], fill=ORNG)
        d.point((tx-1, ty), fill=YEL) # texture highlight

def draw_hashbrowns(d):
    # Oval patty
    d.ellipse([10, 16, 40, 36], fill=DBRN)
    d.ellipse([12, 18, 38, 34], fill=BRN)
    # Crispy shreds
    for x in range(16, 36, 4):
        for y in range(20, 32, 4):
            d.line([(x, y), (x+3, y+2)], fill=ORNG, width=1)
            d.line([(x+1, y), (x-2, y+2)], fill=YEL, width=1)

def draw_cinnamontoast(d):
    # Toast
    d.polygon([(12, 16), (38, 12), (40, 34), (14, 38)], fill=BRN)
    d.polygon([(14, 18), (36, 14), (38, 32), (16, 36)], fill=LBRN)
    # Butter & cinnamon sugar layer
    d.polygon([(16, 20), (34, 16), (36, 30), (18, 34)], fill=YEL)
    for x, y in [(20, 22), (28, 18), (26, 28), (32, 24), (24, 26)]:
        d.ellipse([x, y, x+2, y+2], fill=DBRN)
        d.point((x+1, y+1), fill=BRN)

def draw_breadsticks(d):
    # Bundle of breadsticks
    for i, x in enumerate([14, 22, 30]):
        d.polygon([(x, 10 + i*2), (x+8, 10 + i*2), (x+4, 40), (x-4, 40)], fill=BRN)
        d.polygon([(x+1, 12 + i*2), (x+7, 12 + i*2), (x+3, 38), (x-3, 38)], fill=LBRN)
        # Garlic butter & herbs
        d.line([(x+2, 20), (x+1, 30)], fill=YEL, width=2)
        d.point((x+2, 16 + i*2), fill=GRN)
        d.point((x+1, 26 + i*2), fill=GRN)

def draw_cheesepizza(d):
    # Pan
    d.ellipse([6, 8, 44, 46], fill=DGY)
    # Crust
    d.ellipse([8, 10, 42, 44], fill=BRN)
    d.ellipse([10, 12, 40, 42], fill=LBRN)
    # Sauce and Cheese
    d.ellipse([12, 14, 38, 40], fill=RED)
    d.ellipse([14, 16, 36, 38], fill=YEL)
    # Cheese bubbling spots
    for cx, cy in [(20, 20), (30, 24), (24, 32), (18, 30)]:
        d.ellipse([cx, cy, cx+4, cy+4], fill=CREAM)
        d.point((cx+1, cy+1), fill=ORNG)

def draw_hawaiianpizza(d):
    # Slice
    d.polygon([(10, 12), (40, 12), (25, 44)], fill=BRN)
    d.polygon([(12, 14), (38, 14), (25, 42)], fill=YEL) # Cheese
    # Ham (Pink) and Pineapple (Yellow highlights)
    for x, y in [(18, 18), (28, 24), (24, 34)]:
        d.rectangle([x, y, x+4, y+3], fill=PNK)
        d.point((x, y), fill=RED) # Ham texture
    for x, y in [(24, 16), (18, 26), (30, 18), (22, 28)]:
        d.ellipse([x, y, x+3, y+3], fill=CREAM)
        d.point((x+1, y+1), fill=ORNG) # Pineapple texture

def draw_meatpizza(d):
    # Slice
    d.polygon([(10, 12), (40, 12), (25, 44)], fill=BRN)
    d.polygon([(12, 14), (38, 14), (25, 42)], fill=YEL) # Cheese
    # Pepperoni
    for cx, cy in [(20, 18), (30, 20), (25, 30)]:
        d.ellipse([cx-3, cy-3, cx+3, cy+3], fill=RED)
        d.point((cx-1, cy-1), fill=DRED)
    # Sausage/Beef chunks
    for cx, cy in [(26, 16), (18, 24), (28, 34), (22, 36)]:
        d.ellipse([cx-2, cy-2, cx+2, cy+2], fill=DBRN)

def draw_pepperoniroll(d):
    # Baked roll cut in half
    d.ellipse([10, 16, 30, 36], fill=DBRN) # Left crust
    d.ellipse([12, 18, 28, 34], fill=LBRN)
    # Right half showing inside
    d.ellipse([20, 16, 40, 36], fill=LBRN)
    d.ellipse([22, 18, 38, 34], fill=CREAM)
    # Spiral of pepperoni and cheese
    d.arc([24, 20, 36, 32], start=0, end=360, fill=RED, width=2)
    d.arc([26, 22, 34, 30], start=0, end=180, fill=YEL, width=2)

def draw_cheesedanish(d):
    # Octagonal flaky pastry
    d.polygon([(16, 10), (34, 10), (42, 18), (42, 32), (34, 40), (16, 40), (8, 32), (8, 18)], fill=BRN)
    d.polygon([(18, 12), (32, 12), (40, 20), (40, 30), (32, 38), (18, 38), (10, 30), (10, 20)], fill=LBRN)
    # Cream cheese center
    d.ellipse([16, 18, 34, 32], fill=YEL)
    d.ellipse([18, 20, 32, 30], fill=CREAM)
    # Icing drizzle
    d.line([(12, 16), (38, 34)], fill=WH, width=2)
    d.line([(38, 16), (12, 34)], fill=WH, width=2)

def draw_stickybun(d):
    # Swirled bun
    d.ellipse([10, 10, 40, 40], fill=DBRN)
    d.ellipse([12, 12, 38, 38], fill=LBRN)
    # Cinnamon swirl
    d.arc([16, 16, 34, 34], start=0, end=270, fill=DBRN, width=3)
    d.arc([20, 20, 30, 30], start=90, end=360, fill=DBRN, width=2)
    # Sticky caramel and pecans
    d.ellipse([14, 14, 24, 24], fill=ORNG)
    d.ellipse([30, 26, 36, 32], fill=ORNG)
    for px, py in [(18, 18), (32, 28), (26, 14), (20, 32)]:
        d.ellipse([px, py, px+3, py+2], fill=DBRN)

def draw_applefritter(d):
    # Irregular lumpy shape
    pts = [(16, 10), (34, 12), (42, 24), (36, 38), (20, 42), (8, 32), (10, 18)]
    d.polygon(pts, fill=DBRN)
    pts_inner = [(18, 12), (32, 14), (40, 24), (34, 36), (22, 40), (10, 32), (12, 20)]
    d.polygon(pts_inner, fill=BRN)
    # Apple chunks
    for cx, cy in [(20, 20), (30, 18), (26, 28), (18, 30), (34, 28)]:
        d.ellipse([cx, cy, cx+4, cy+4], fill=YEL)
    # Glaze glaze
    for i in range(12, 40, 6):
        d.line([(i, 12), (i+4, 38)], fill=WH, width=1)

def draw_bearclaw(d):
    # Semicircle claw shape
    d.chord([10, 16, 40, 40], start=180, end=0, fill=DBRN)
    d.chord([12, 18, 38, 38], start=180, end=0, fill=LBRN)
    # Claw cuts
    for x in [18, 25, 32]:
        d.line([(x, 20), (x, 28)], fill=DBRN, width=3)
    # Almond slices
    for x in [16, 24, 30]:
        d.ellipse([x, 30, x+4, 34], fill=CREAM)

def draw_whoopiepie(d):
    # Two dome cakes with filling
    d.ellipse([10, 10, 40, 26], fill=DBRN) # Top cookie
    d.ellipse([10, 24, 40, 40], fill=DBRN) # Bottom cookie
    # White filling oozing
    d.ellipse([12, 20, 38, 30], fill=WH)
    d.ellipse([14, 22, 36, 28], fill=CREAM)
    # Texture
    d.point((20, 14), fill=BK)
    d.point((30, 36), fill=BK)

def draw_redvelvet(d):
    # Slice
    d.polygon([(10, 34), (40, 34), (25, 12)], fill=DRED) # Shadow/Side
    d.polygon([(12, 32), (38, 32), (25, 14)], fill=RED) # Cake
    # Frosting layers
    d.polygon([(10, 34), (40, 34), (40, 38), (10, 38)], fill=WH)
    d.line([(16, 24), (34, 24)], fill=WH, width=2)
    # Frosting dollop on back
    d.ellipse([21, 8, 29, 16], fill=WH)
    d.ellipse([23, 10, 27, 14], fill=CREAM)
    d.point((25, 12), fill=DRED) # crumb

def draw_carrotcake(d):
    # Slice
    d.polygon([(10, 34), (40, 34), (25, 12)], fill=DBRN) 
    d.polygon([(12, 32), (38, 32), (25, 14)], fill=BRN) # Spiced cake
    # Cream cheese frosting
    d.polygon([(10, 34), (40, 34), (40, 38), (10, 38)], fill=WH)
    d.line([(16, 24), (34, 24)], fill=WH, width=2)
    # Carrot garnish
    d.line([(22, 10), (28, 14)], fill=ORNG, width=3)
    d.ellipse([27, 9, 31, 13], fill=GRN) # leaf
    # Walnuts inside
    d.point((20, 28), fill=DBRN)
    d.point((28, 20), fill=DBRN)

def draw_poundcake(d):
    # Thick rectangular slice
    d.polygon([(12, 34), (38, 34), (36, 14), (14, 14)], fill=BRN) # crust edge
    d.polygon([(14, 32), (36, 32), (34, 16), (16, 16)], fill=YEL) # crumb
    d.polygon([(16, 30), (34, 30), (32, 18), (18, 18)], fill=CREAM) # center
    # Strawberry and whipped cream garnish
    d.ellipse([18, 10, 28, 20], fill=WH)
    d.ellipse([24, 14, 30, 22], fill=RED)
    d.point((27, 18), fill=YEL) # seed

def draw_rockcandy(d):
    # Stick
    d.line([(25, 34), (25, 48)], fill=LBRN, width=3)
    # Crystals (Blue/Purple geometric shapes)
    d.polygon([(20, 10), (30, 14), (34, 24), (28, 34), (18, 32), (14, 20)], fill=BLU)
    d.polygon([(22, 12), (28, 16), (30, 24), (26, 30), (20, 28), (18, 20)], fill=WH)
    # Sharp facets
    d.line([(20, 10), (26, 20)], fill=DBRN, width=1)
    d.line([(34, 24), (26, 20)], fill=DBRN, width=1)
    d.line([(28, 34), (26, 20)], fill=DBRN, width=1)

def draw_caramelcorn(d):
    # Box
    d.polygon([(14, 20), (36, 20), (32, 44), (18, 44)], fill=RED)
    d.line([(20, 20), (22, 44)], fill=WH, width=2)
    d.line([(30, 20), (28, 44)], fill=WH, width=2)
    # Caramel popcorn mound
    d.ellipse([10, 10, 40, 24], fill=BRN)
    for cx, cy in [(16, 14), (24, 12), (32, 16), (20, 20), (30, 20), (25, 16)]:
        d.ellipse([cx-4, cy-4, cx+4, cy+4], fill=YEL)
        d.arc([cx-3, cy-3, cx+3, cy+3], start=0, end=180, fill=ORNG, width=2)

def draw_chocolatemilk(d):
    # Glass tumbler
    d.polygon([(14, 12), (36, 12), (32, 42), (18, 42)], fill=WH)
    # Chocolate milk
    d.polygon([(15, 16), (35, 16), (31, 40), (19, 40)], fill=BRN)
    d.polygon([(16, 18), (34, 18), (30, 38), (20, 38)], fill=DBRN)
    # Glass highlight
    d.line([(20, 18), (22, 38)], fill=WH, width=1)
    # Straw
    d.line([(25, 6), (28, 16)], fill=RED, width=2)

def draw_applecider(d):
    # Rustic Mug
    d.rectangle([12, 16, 38, 40], fill=RED)
    d.ellipse([12, 36, 38, 44], fill=DRED) # base
    d.arc([4, 20, 16, 36], start=90, end=270, fill=RED, width=4) # handle
    # Cider
    d.ellipse([14, 14, 36, 20], fill=ORNG)
    # Cinnamon stick and apple slice
    d.line([(28, 6), (24, 18)], fill=DBRN, width=3)
    d.ellipse([16, 12, 22, 18], fill=CREAM)
    d.point((19, 15), fill=BRN) # seed

def draw_rootbeerfloat(d):
    # Tall glass mug
    d.rectangle([14, 12, 36, 42], fill=WH)
    d.arc([36, 16, 44, 38], start=270, end=90, fill=WH, width=3) # Handle
    # Root beer
    d.rectangle([16, 20, 34, 40], fill=DBRN)
    # Vanilla ice cream scoop floating
    d.ellipse([14, 8, 36, 24], fill=WH)
    d.ellipse([16, 10, 34, 22], fill=CREAM)
    # Foam bubbles
    d.ellipse([12, 18, 18, 24], fill=WH)
    d.ellipse([32, 18, 38, 24], fill=WH)

def draw_icecreamsandwich(d):
    # Isometric block
    # Top chocolate wafer
    d.polygon([(14, 18), (34, 12), (42, 20), (22, 26)], fill=DBRN)
    # Ice cream layer
    d.polygon([(14, 22), (22, 30), (42, 24), (34, 16)], fill=WH)
    d.polygon([(16, 24), (22, 28), (40, 24), (34, 20)], fill=CREAM)
    # Bottom chocolate wafer
    d.polygon([(14, 26), (22, 34), (42, 28), (34, 20)], fill=BK)
    # Wafer dimples
    d.point((22, 22), fill=BK)
    d.point((30, 18), fill=BK)

def draw_chocotaco(d):
    # Waffle taco shell
    d.polygon([(8, 16), (25, 42), (42, 16), (25, 26)], fill=BRN)
    d.polygon([(10, 18), (25, 40), (40, 18), (25, 28)], fill=LBRN)
    # Waffle grid
    d.line([(14, 24), (20, 32)], fill=DBRN, width=1)
    d.line([(36, 24), (30, 32)], fill=DBRN, width=1)
    # Fudge and peanut topping
    d.polygon([(12, 16), (25, 22), (38, 16)], fill=DBRN) # fudge
    for x, y in [(18, 18), (24, 20), (32, 18)]:
        d.ellipse([x, y, x+2, y+2], fill=YEL) # nuts

def draw_chocolatemousse(d):
    # Fancy dessert cup
    d.polygon([(18, 22), (32, 22), (28, 42), (22, 42)], fill=WH)
    d.line([(14, 42), (36, 42)], fill=WH, width=2) # base
    # Mousse
    d.ellipse([14, 14, 36, 24], fill=DBRN)
    d.ellipse([16, 16, 34, 22], fill=BRN)
    # Whipped cream and chocolate curl
    d.ellipse([20, 8, 30, 18], fill=WH)
    d.arc([22, 4, 28, 12], start=180, end=360, fill=DBRN, width=2)

def draw_cremebrulee(d):
    # Oval shallow ramekin
    d.ellipse([8, 24, 42, 40], fill=WH)
    d.ellipse([10, 20, 40, 32], fill=LBLU)
    # Custard base
    d.ellipse([12, 22, 38, 30], fill=CREAM)
    # Hard caramel crust (burnt spots)
    d.ellipse([14, 23, 36, 29], fill=BRN)
    d.ellipse([20, 24, 30, 28], fill=DBRN) # burnt center
    # Strawberry garnish
    d.ellipse([16, 20, 24, 26], fill=RED)
    d.point((22, 19), fill=GRN)

def draw_bakedalaska(d):
    # Toasted meringue spikes
    d.polygon([(12, 34), (38, 34), (30, 10), (20, 14)], fill=WH)
    d.polygon([(14, 34), (36, 34), (30, 14), (20, 18)], fill=CREAM)
    # Torched edges (Brown spikes)
    d.line([(20, 14), (16, 28)], fill=BRN, width=2)
    d.line([(30, 10), (28, 26)], fill=BRN, width=2)
    d.line([(25, 12), (25, 24)], fill=DBRN, width=1)
    # Sponge cake base
    d.polygon([(10, 34), (40, 34), (38, 40), (12, 40)], fill=LBRN)

def draw_sorbet(d):
    # Glass goblet
    d.arc([14, 16, 36, 32], start=0, end=180, fill=WH, width=2)
    d.line([(25, 32), (25, 42)], fill=WH, width=2)
    d.line([(18, 42), (32, 42)], fill=WH, width=2)
    # Three scoops (Lemon, Raspberry, Mango)
    d.ellipse([16, 12, 26, 22], fill=YEL) # lemon
    d.ellipse([24, 12, 34, 22], fill=ORNG) # mango
    d.ellipse([20, 6, 30, 16], fill=PNK) # raspberry
    # Mint leaf
    d.ellipse([25, 4, 29, 8], fill=GRN)

def draw_pushpop(d):
    # Plastic stick and plunger
    d.line([(25, 30), (25, 46)], fill=WH, width=3)
    d.line([(20, 46), (30, 46)], fill=WH, width=2)
    # Clear tube
    d.rectangle([18, 20, 32, 36], outline=WH, width=1)
    # Rainbow sherbet pushed up
    d.rectangle([20, 10, 30, 16], fill=PNK)
    d.rectangle([20, 16, 30, 24], fill=ORNG)
    d.rectangle([20, 24, 30, 30], fill=RED)
    # Dome top
    d.chord([20, 6, 30, 14], start=180, end=0, fill=PNK)

def draw_froyo(d):
    # Cup
    d.polygon([(14, 26), (36, 26), (32, 44), (18, 44)], fill=LBLU)
    d.polygon([(16, 26), (34, 26), (30, 44), (20, 44)], fill=WH)
    # Swirled Yogurt (Pink & White)
    d.ellipse([12, 20, 38, 30], fill=PNK)
    d.ellipse([16, 14, 34, 24], fill=WH)
    d.ellipse([20, 8, 30, 18], fill=PNK)
    d.ellipse([23, 4, 27, 12], fill=WH)
    # Berries and chocolate chips
    d.ellipse([16, 22, 20, 26], fill=RED)
    d.ellipse([32, 18, 36, 22], fill=BLU)
    d.point((24, 14), fill=DBRN)

def draw_fruitleather(d):
    # Plastic wrap backing
    d.polygon([(10, 10), (36, 14), (40, 40), (14, 36)], fill=WH)
    # Unrolled fruit leather strip
    d.polygon([(16, 24), (24, 16), (34, 26), (26, 34)], fill=DRED)
    d.polygon([(18, 24), (24, 18), (32, 26), (26, 32)], fill=RED)
    # The rolled up part
    d.ellipse([12, 18, 28, 34], fill=DBRN)
    d.ellipse([14, 20, 26, 32], fill=DRED)
    d.arc([16, 22, 24, 30], start=0, end=360, fill=RED, width=2)


def main():
    print("Starting generation of 300 highly-detailed Food & Dessert sprites (50x50)...")
    
    # We will build a list of all 200 items
    foods = [
        ("pizza", draw_pizza), ("burger", draw_burger), ("hotdog", draw_hotdog), ("taco", draw_taco),
        ("sushi", draw_sushi), ("fries", draw_fries), ("cupcake", draw_cupcake), ("icecream", draw_icecream),
        ("donut", draw_donut), ("cookie", draw_cookie), ("pancakes", draw_pancakes), ("waffle", draw_waffle),
        ("cake", draw_cake), ("pie", draw_pie), ("croissant", draw_croissant), ("popcorn", draw_popcorn),
        ("pretzel", draw_pretzel), ("bacon", draw_bacon), ("egg", draw_egg), ("cheese", draw_cheese),
        ("sandwich", draw_sandwich), ("soup", draw_soup), ("drumstick", draw_drumstick), ("steak", draw_steak),
        ("tempura", draw_tempura), ("onigiri", draw_onigiri), ("ramen", draw_ramen), ("coffee", draw_coffee),
        ("soda", draw_soda), ("beer", draw_beer), ("cocktail", draw_cocktail), ("bubbletea", draw_bubbletea),
        ("chocolate", draw_chocolate), ("candycane", draw_candycane), ("lollipop", draw_lollipop),
        ("macaron", draw_macaron), ("pudding", draw_pudding), ("toast", draw_toast), ("kabob", draw_kabob),
        ("friedshrimp", draw_friedshrimp), ("hotcocoa", draw_hotcocoa), ("dango", draw_dango),
        ("fortune", draw_fortune), ("softserve", draw_softserve), ("honeypot", draw_honeypot),
        ("avocadotoast", draw_avocadotoast), ("cinnamon", draw_cinnamon), ("muffin", draw_muffin),
        ("gingerbread", draw_gingerbread), ("crepe", draw_crepe),
        
        ("bagel", draw_bagel), ("burrito", draw_burrito), ("quesadilla", draw_quesadilla), ("nachos", draw_nachos),
        ("guacamole", draw_guacamole), ("salsa", draw_salsa), ("churro", draw_churro), ("flan", draw_flan),
        ("tiramisu", draw_tiramisu), ("pannacotta", draw_pannacotta), ("baklava", draw_baklava),
        ("eclair", draw_eclair), ("tart", draw_tart), ("cheesecake", draw_cheesecake), ("bananasplit", draw_bananasplit),
        ("milkshake", draw_milkshake), ("sundae", draw_sundae), ("parfait", draw_parfait), ("sherbet", draw_sherbet),
        ("mochi", draw_mochi), ("cannoli", draw_cannoli), ("gelato", draw_gelato), ("scone", draw_scone),
        ("baguette", draw_baguette), ("garlicbread", draw_garlicbread), ("cornbread", draw_cornbread),
        ("sourdough", draw_sourdough), ("ryebread", draw_ryebread), ("pitabread", draw_pitabread), ("naan", draw_naan),
        ("challah", draw_challah), ("brioche", draw_brioche), ("focaccia", draw_focaccia), ("bruschetta", draw_bruschetta),
        ("calzone", draw_calzone), ("garlicknots", draw_garlicknots), ("stromboli", draw_stromboli), ("gyoza", draw_gyoza),
        ("baozi", draw_baozi), ("siumai", draw_siumai), ("hargow", draw_hargow), ("springroll", draw_springroll),
        ("friedrice", draw_friedrice), ("lomein", draw_lomein), ("kungpao", draw_kungpao), ("sweetpork", draw_sweetpork),
        ("mapotofu", draw_mapotofu), ("pekingduck", draw_pekingduck), ("chowmein", draw_chowmein),
        ("eggdropsoup", draw_eggdropsoup), ("hotsoursoup", draw_hotsoursoup), ("wontonsoup", draw_wontonsoup),
        ("crabrangoon", draw_crabrangoon), ("eggroll", draw_eggroll), ("falafel", draw_falafel), ("hummus", draw_hummus),
        ("shawarma", draw_shawarma), ("gyros", draw_gyros), ("kebab", draw_kebab), ("tikkamasala", draw_tikkamasala),
        ("samosa", draw_samosa), ("biryani", draw_biryani), ("curry", draw_curry), ("pho", draw_pho),
        ("padthai", draw_padthai), ("tomyum", draw_tomyum), ("satay", draw_satay), ("gimbap", draw_gimbap),
        ("bibimbap", draw_bibimbap), ("tteokbokki", draw_tteokbokki), ("kimchi", draw_kimchi), ("bulgogi", draw_bulgogi),
        ("japchae", draw_japchae), ("tonkatsu", draw_tonkatsu), ("tempuradon", draw_tempuradon), ("udon", draw_udon),
        ("soba", draw_soba), ("yakitori", draw_yakitori), ("takoyaki", draw_takoyaki), ("okonomiyaki", draw_okonomiyaki),
        ("matchalatte", draw_matchalatte), ("taiyaki", draw_taiyaki), ("dorayaki", draw_dorayaki), ("kakigori", draw_kakigori),
        ("crepecake", draw_crepecake), ("fruitsalad", draw_fruitsalad), ("greensalad", draw_greensalad),
        ("caesarsalad", draw_caesarsalad), ("coleslaw", draw_coleslaw), ("potatosalad", draw_potatosalad),
        ("bakedpotato", draw_bakedpotato), ("mashedpotato", draw_mashedpotato), ("maccheese", draw_maccheese),
        ("lasagna", draw_lasagna), ("spaghetti", draw_spaghetti), ("meatballs", draw_meatballs), ("chili", draw_chili),
        ("corncob", draw_corncob), ("clamchowder", draw_clamchowder), ("fishchips", draw_fishchips), ("calamari", draw_calamari),
        ("lobstertail", draw_lobstertail), ("oysters", draw_oysters), ("paella", draw_paella), ("crabcake", draw_crabcake),
        ("clambake", draw_clambake), ("beefstew", draw_beefstew), ("beefwellington", draw_beefwellington),
        ("porkchop", draw_porkchop), ("ribs", draw_ribs), ("meatloaf", draw_meatloaf), ("potroast", draw_potroast),
        ("chickenpotpie", draw_chickenpotpie), ("chickenwings", draw_chickenwings), ("chickennuggets", draw_chickennuggets),
        ("quesofundido", draw_quesofundido), ("empanada", draw_empanada), ("arepa", draw_arepa), ("pupusa", draw_pupusa),
        ("ceviche", draw_ceviche), ("tostada", draw_tostada), ("chilesrellenos", draw_chilesrellenos), ("tamale", draw_tamale),
        ("elote", draw_elote), ("chilaquiles", draw_chilaquiles), ("poutine", draw_poutine), ("shepherdspie", draw_shepherdspie),
        ("scotchegg", draw_scotchegg), ("bangersmash", draw_bangersmash), ("fishcake", draw_fishcake),
        ("croquemonsieur", draw_croquemonsieur), ("quiche", draw_quiche), ("ratatouille", draw_ratatouille),
        ("escargot", draw_escargot), ("fondue", draw_fondue), ("pierogi", draw_pierogi), ("goulash", draw_goulash),
        ("schnitzel", draw_schnitzel), ("borsch", draw_borsch), ("khachapuri", draw_khachapuri), ("gelatin", draw_gelatin),
        ("ricepudding", draw_ricepudding), ("breadpudding", draw_breadpudding), ("fruitcrisp", draw_fruitcrisp),
        ("stickypudding", draw_stickypudding), ("lavacake", draw_lavacake), ("pavlova", draw_pavlova),
        ("profiteroles", draw_profiteroles), ("shortcake", draw_shortcake), ("fruitcobbler", draw_fruitcobbler),
        ("omelette", draw_omelette),
        ("macaroni", draw_macaroni),
        ("tomatosoup", draw_tomatosoup),
        ("chickensoup", draw_chickensoup),
        ("fishtaco", draw_fishtaco),
        ("sausage", draw_sausage),
        ("meatpie", draw_meatpie),
        ("quesodip", draw_quesodip),
        ("potatochips", draw_potatochips),
        ("poptart", draw_poptart),
        ("onionrings", draw_onionrings),
        ("turnover", draw_turnover),
        ("friedchicken", draw_friedchicken),
        ("beefjerky", draw_beefjerky),
        ("grilledcheese", draw_grilledcheese),
        ("clubsandwich", draw_clubsandwich),
        ("blt", draw_blt),
        ("pbtoast", draw_pbtoast),
        ("frenchtoast", draw_frenchtoast),
        ("oatmeal", draw_oatmeal),
        ("cereal", draw_cereal),
        ("granolabar", draw_granolabar),
        ("smoothie", draw_smoothie),
        ("applejuice", draw_applejuice),
        ("orangejuice", draw_orangejuice),
        ("lemonade", draw_lemonade),
        ("hottea", draw_hottea),
        ("milkcarton", draw_milkcarton),
        ("crackers", draw_crackers),
        ("grahamcrackers", draw_grahamcrackers),
        ("marshmallow", draw_marshmallow),
        ("smores", draw_smores),
        ("caramelapple", draw_caramelapple),
        ("cottoncandy", draw_cottoncandy),
        ("snowcone", draw_snowcone),
        ("fudge", draw_fudge),
        ("brownie", draw_brownie),
        ("trifle", draw_trifle),
        ("swissroll", draw_swissroll),
        ("plumpudding", draw_plumpudding),
        ("custard", draw_custard),
        ("fruitcake", draw_fruitcake),
        ("jellybeans", draw_jellybeans),
        ("gummybears", draw_gummybears),
        ("peppermint", draw_peppermint),
        ("toffee", draw_toffee),
        ("truffles", draw_truffles),
        ("yorkshirepudding", draw_yorkshirepudding),
        ("pigsblanket", draw_pigsblanket),
        ("potatowedges", draw_potatowedges),
        ("keylimepie", draw_keylimepie),
        ("pecanpie", draw_pecanpie),
        ("softtaco", draw_softtaco),
        ("taquitos", draw_taquitos),
        ("corndog", draw_corndog),
        ("chickentenders", draw_chickentenders),
        ("mozzarellasticks", draw_mozzarellasticks),
        ("garlicshrimp", draw_garlicshrimp),
        ("bakedbeans", draw_bakedbeans),
        ("ricekrispies", draw_ricekrispies),
        ("animalcrackers", draw_animalcrackers),
        ("pretzelbites", draw_pretzelbites),
        ("bananabread", draw_bananabread),
        ("meatballsub", draw_meatballsub),
        ("pulledpork", draw_pulledpork),
        ("eggsaladsandwich", draw_eggsaladsandwich),
        ("tunamelt", draw_tunamelt),
        ("fishburger", draw_fishburger),
        ("sliders", draw_sliders),
        ("potatoskins", draw_potatoskins),
        ("tatertots", draw_tatertots),
        ("hashbrowns", draw_hashbrowns),
        ("cinnamontoast", draw_cinnamontoast),
        ("breadsticks", draw_breadsticks),
        ("cheesepizza", draw_cheesepizza),
        ("hawaiianpizza", draw_hawaiianpizza),
        ("meatpizza", draw_meatpizza),
        ("pepperoniroll", draw_pepperoniroll),
        ("cheesedanish", draw_cheesedanish),
        ("stickybun", draw_stickybun),
        ("applefritter", draw_applefritter),
        ("bearclaw", draw_bearclaw),
        ("whoopiepie", draw_whoopiepie),
        ("redvelvet", draw_redvelvet),
        ("carrotcake", draw_carrotcake),
        ("poundcake", draw_poundcake),
        ("rockcandy", draw_rockcandy),
        ("caramelcorn", draw_caramelcorn),
        ("chocolatemilk", draw_chocolatemilk),
        ("applecider", draw_applecider),
        ("rootbeerfloat", draw_rootbeerfloat),
        ("icecreamsandwich", draw_icecreamsandwich),
        ("chocotaco", draw_chocotaco),
        ("chocolatemousse", draw_chocolatemousse),
        ("cremebrulee", draw_cremebrulee),
        ("bakedalaska", draw_bakedalaska),
        ("sorbet", draw_sorbet),
        ("pushpop", draw_pushpop),
        ("froyo", draw_froyo),
        ("fruitleather", draw_fruitleather)
    ]
    
    for name, func in foods:
        save_sprite(name, func)
        
    print(f"Done! Generated all {len(foods)} Food & Dessert sprites successfully.")

if __name__ == "__main__":
    main()
