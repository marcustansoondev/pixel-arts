import os
from PIL import Image, ImageDraw

OUTPUT_DIR = "images/fruits"
os.makedirs(OUTPUT_DIR, exist_ok=True)

def create_sprite(name, draw_func):
    img = Image.new("RGBA", (50, 50), (255, 255, 255, 0))
    draw = ImageDraw.Draw(img)
    draw_func(draw)
    path = os.path.join(OUTPUT_DIR, f"{name}_50x50.png")
    img.save(path)
    print(f"  Saved: {path}")

# Color constants (shared palette; each function uses ≤ 10)
RED         = (220, 40, 40, 255)
DKRED       = (130, 20, 20, 255)
LIGHTRED    = (255, 110, 110, 255)
ORANGE      = (255, 140, 0, 255)
LIGHTORANGE = (255, 185, 72, 255)
YELLOW      = (240, 222, 40, 255)
LIGHTYELLOW = (255, 248, 145, 255)
GREEN       = (42, 162, 42, 255)
DKGREEN     = (22, 92, 22, 255)
LIGHTGREEN  = (122, 225, 122, 255)
BROWN       = (112, 72, 30, 255)
DKBROWN     = (68, 42, 15, 255)
WHITE       = (255, 255, 255, 255)
BLACK       = (0, 0, 0, 255)
DARKBLUE    = (22, 32, 72, 255)
PURPLE      = (102, 42, 122, 255)
MAROON      = (82, 16, 42, 255)
BEIGE       = (222, 192, 152, 255)
GREY        = (185, 182, 178, 255)

# 1. Rambutan
def draw_rambutan(draw):
    # body
    draw.ellipse([14, 12, 36, 38], fill=DKRED)
    draw.ellipse([16, 14, 34, 36], fill=RED)
    draw.ellipse([17, 14, 24, 22], fill=LIGHTRED)   # highlight
    # hairy spines radiating outward
    spines = [(14,10),(10,16),(8,25),(11,34),(18,40),(25,42),
              (32,40),(39,34),(42,25),(39,16),(36,10),(25,8)]
    for sx, sy in spines:
        draw.line([(25, 25), (sx, sy)], fill=DKRED, width=2)
        draw.line([(sx, sy), (sx+(sx-25)//3, sy+(sy-25)//3)], fill=(95, 12, 12, 255), width=1)
    # re-draw body on top of spines
    draw.ellipse([14, 12, 36, 38], fill=DKRED)
    draw.ellipse([16, 14, 34, 36], fill=RED)
    draw.ellipse([17, 14, 24, 22], fill=LIGHTRED)

# 2. Breadfruit
def draw_breadfruit(draw):
    # large bumpy green sphere
    draw.ellipse([9, 9, 41, 43], fill=DKGREEN)
    draw.ellipse([11, 11, 39, 41], fill=GREEN)
    draw.ellipse([13, 11, 24, 23], fill=LIGHTGREEN)  # highlight
    # hexagonal bump grid
    for x in range(14, 38, 6):
        for y in range(14, 40, 6):
            draw.ellipse([x-2, y-2, x+3, y+3], fill=DKGREEN)
            draw.ellipse([x-1, y-1, x+2, y+2], fill=LIGHTGREEN)
    # stem
    draw.line([(25, 9), (25, 3)], fill=BROWN, width=3)
    draw.polygon([(25, 5), (32, 0), (28, 8)], fill=GREEN)

# 3. Salak (Snake Fruit)
def draw_salak(draw):
    # teardrop body
    draw.polygon([(25, 8), (12, 32), (16, 44), (34, 44), (38, 32)], fill=DKBROWN)
    draw.polygon([(25, 12), (16, 32), (18, 42), (32, 42), (34, 32)], fill=BROWN)
    draw.ellipse([18, 14, 28, 22], fill=BEIGE)   # highlight
    # snake-scale arcs stacked up the body
    for y in range(18, 42, 5):
        draw.arc([15, y-2, 35, y+5], 0, 180, fill=DKBROWN, width=2)
        draw.arc([17, y, 33, y+4],   0, 180, fill=BEIGE,   width=1)
    # tip and stem
    draw.ellipse([22, 6, 28, 12], fill=DKBROWN)
    draw.line([(25, 6), (25, 2)], fill=BROWN, width=2)

# 4. Soursop
def draw_soursop(draw):
    # kidney-shaped body
    draw.ellipse([10, 12, 40, 44], fill=DKGREEN)
    draw.ellipse([12, 14, 38, 42], fill=GREEN)
    draw.ellipse([14, 15, 26, 26], fill=LIGHTGREEN)  # highlight
    # small pointed spines evenly spaced on rim
    spines = [(10,24),(13,14),(20,10),(30,10),(37,14),(40,24),
              (37,36),(30,42),(20,42),(13,36)]
    for sx, sy in spines:
        draw.polygon([(sx, sy), (sx-2, sy-4), (sx+2, sy-4)], fill=DKGREEN)
    # stem
    draw.line([(25, 10), (25, 4)], fill=BROWN, width=2)

# 5. Custard Apple
def draw_custard_apple(draw):
    # bumpy green sphere
    draw.ellipse([10, 10, 40, 44], fill=DKGREEN)
    # round bumps arranged in overlapping grid
    bump_centers = [
        (17,16),(25,13),(33,16),(14,24),(22,22),(30,22),(38,24),
        (17,32),(25,30),(33,32),(20,40),(30,40)
    ]
    for cx, cy in bump_centers:
        draw.ellipse([cx-5, cy-5, cx+5, cy+5], fill=GREEN)
        draw.ellipse([cx-3, cy-4, cx+3, cy+1], fill=LIGHTGREEN)
    draw.ellipse([22, 12, 26, 16], fill=BROWN)   # stem nub
    # leaf
    draw.polygon([(24, 10), (18, 4), (20, 12)], fill=DKGREEN)

# 6. Longan
def draw_longan(draw):
    # whole fruit (left) – tan shell
    draw.ellipse([5, 16, 27, 40], fill=DKBROWN)
    draw.ellipse([7, 18, 25, 38], fill=BROWN)
    draw.ellipse([9, 19, 18, 28], fill=BEIGE)    # highlight
    # peeled fruit (right) – white translucent flesh
    draw.ellipse([24, 14, 46, 38], fill=BEIGE)
    draw.ellipse([26, 16, 44, 36], fill=WHITE)
    draw.ellipse([28, 18, 42, 34], fill=(245, 248, 252, 255))
    # dark shiny seed
    draw.ellipse([30, 21, 40, 31], fill=BLACK)
    draw.ellipse([31, 21, 35, 25], fill=(55, 45, 45, 255))  # seed shine

# 7. Medlar
def draw_medlar(draw):
    # squat round brown fruit
    draw.ellipse([11, 12, 39, 42], fill=DKBROWN)
    draw.ellipse([13, 14, 37, 40], fill=BROWN)
    draw.ellipse([15, 15, 26, 26], fill=BEIGE)   # highlight
    # characteristic wide open calyx at bottom
    draw.polygon([(19, 40), (16, 46), (22, 44)], fill=DKBROWN)
    draw.polygon([(25, 41), (24, 48), (28, 47)], fill=DKBROWN)
    draw.polygon([(31, 40), (34, 46), (28, 44)], fill=DKBROWN)
    draw.ellipse([20, 38, 30, 44], fill=(90, 52, 18, 255))
    # stem
    draw.line([(25, 12), (25, 6)], fill=BROWN, width=2)
    draw.polygon([(25, 7), (30, 3), (27, 10)], fill=GREEN)

# 8. Loquat
def draw_loquat(draw):
    # two loquats clustered
    draw.ellipse([6, 16, 28, 40], fill=(235, 145, 35, 255))
    draw.ellipse([8, 18, 26, 38], fill=LIGHTORANGE)
    draw.ellipse([10, 18, 18, 26], fill=(255, 225, 165, 255))  # highlight
    draw.ellipse([22, 10, 44, 38], fill=(240, 152, 38, 255))
    draw.ellipse([24, 12, 42, 36], fill=LIGHTORANGE)
    draw.ellipse([26, 12, 34, 22], fill=(255, 225, 165, 255))
    # calyx crowns
    draw.polygon([(14, 16), (10, 10), (18, 14)], fill=GREEN)
    draw.polygon([(33, 10), (28, 4), (36, 8)],  fill=GREEN)
    # stems
    draw.line([(15, 14), (22, 8)], fill=BROWN, width=2)
    draw.line([(33, 8),  (33, 3)], fill=BROWN, width=2)

# 9. Bilberry
def draw_bilberry(draw):
    # main berry cluster
    draw.ellipse([10, 16, 36, 44], fill=DARKBLUE)
    draw.ellipse([12, 18, 34, 42], fill=(42, 52, 115, 255))
    draw.ellipse([14, 18, 24, 28], fill=(75, 88, 165, 255))   # highlight
    # crown
    draw.polygon([(19, 16), (25, 11), (31, 16)], fill=BLACK)
    draw.polygon([(25, 16), (25, 20), (29, 16)], fill=BLACK)
    # second berry above-right
    draw.ellipse([24, 8, 44, 28], fill=DARKBLUE)
    draw.ellipse([26, 10, 42, 26], fill=(42, 52, 115, 255))
    draw.ellipse([28, 10, 35, 17], fill=(75, 88, 165, 255))
    draw.polygon([(33, 8), (37, 5), (38, 10)], fill=BLACK)

# 10. Cloudberry
def draw_cloudberry(draw):
    # amber orange aggregate drupelets
    offsets = [(20,12),(28,12),(16,18),(24,18),(32,18),(20,24),(28,24),(24,30)]
    for gx, gy in offsets:
        draw.ellipse([gx, gy, gx+8, gy+8],   fill=ORANGE)
        draw.ellipse([gx+1, gy+1, gx+7, gy+7], fill=LIGHTORANGE)
        draw.ellipse([gx+1, gy+1, gx+4, gy+4], fill=(255, 225, 165, 255))
    # green leaf sepals at base
    draw.polygon([(14, 30), (18, 38), (25, 31)], fill=DKGREEN)
    draw.polygon([(36, 30), (32, 38), (25, 31)], fill=GREEN)
    draw.polygon([(25, 31), (25, 40), (29, 34)], fill=DKGREEN)

# 11. Huckleberry
def draw_huckleberry(draw):
    draw.ellipse([10, 16, 40, 46], fill=PURPLE)
    draw.ellipse([12, 18, 38, 44], fill=(148, 68, 178, 255))
    draw.ellipse([14, 18, 26, 30], fill=(192, 118, 218, 255))   # highlight
    # star crown at top
    draw.polygon([(20, 16), (25, 10), (30, 16)], fill=BLACK)
    draw.polygon([(25, 16), (25, 21), (28, 16)], fill=BLACK)
    # bottom shadow
    draw.ellipse([14, 40, 36, 48], fill=(78, 28, 98, 255))

# 12. Lingonberry
def draw_lingonberry(draw):
    # two berries
    draw.ellipse([8, 18, 30, 42], fill=DKRED)
    draw.ellipse([10, 20, 28, 40], fill=RED)
    draw.ellipse([12, 20, 20, 28], fill=LIGHTRED)   # highlight
    # calyx dot
    draw.ellipse([17, 38, 21, 42], fill=BLACK)
    # second berry
    draw.ellipse([22, 10, 44, 34], fill=DKRED)
    draw.ellipse([24, 12, 42, 32], fill=RED)
    draw.ellipse([26, 12, 34, 20], fill=LIGHTRED)
    draw.ellipse([31, 30, 35, 34], fill=BLACK)
    # stems
    draw.line([(19, 18), (26, 10)], fill=GREEN, width=1)

# 13. Feijoa
def draw_feijoa(draw):
    # green egg shape
    draw.ellipse([12, 12, 38, 44], fill=DKGREEN)
    draw.ellipse([14, 14, 36, 42], fill=GREEN)
    draw.ellipse([16, 14, 26, 26], fill=LIGHTGREEN)  # highlight
    # distinctive cross-shaped flower calyx at bottom
    draw.line([(19, 40), (31, 40)], fill=DKBROWN, width=2)
    draw.line([(25, 34), (25, 46)], fill=DKBROWN, width=2)
    draw.ellipse([22, 37, 28, 43], fill=RED)         # red flower center
    # reddish petal tips
    for (px, py) in [(19,40),(31,40),(25,34),(25,46)]:
        draw.ellipse([px-2, py-2, px+2, py+2], fill=RED)
    # stem
    draw.line([(25, 12), (25, 6)], fill=BROWN, width=2)

# 14. Tamarind
def draw_tamarind(draw):
    # curved brown pod
    draw.arc([8, 10, 42, 44], 40, 185, fill=DKBROWN, width=9)
    draw.arc([10, 12, 40, 42], 42, 183, fill=BROWN,   width=5)
    draw.arc([12, 14, 38, 40], 44, 181, fill=BEIGE,   width=2)
    # constriction bumps showing seeds inside
    for a in [70, 100, 130, 160]:
        import math
        x = int(25 + 17 * math.cos(math.radians(a)))
        y = int(27 - 17 * math.sin(math.radians(a)))
        draw.ellipse([x-2, y-2, x+2, y+2], fill=DKBROWN)
    # pod end caps
    draw.ellipse([8, 23, 15, 30],  fill=BROWN)
    draw.ellipse([36, 14, 43, 21], fill=BROWN)
    # seed visible at break
    draw.ellipse([30, 25, 38, 32], fill=DKBROWN)
    draw.ellipse([32, 27, 36, 30], fill=BEIGE)

# 15. Ugli Fruit
def draw_ugli_fruit(draw):
    # large rough greenish-yellow sphere
    draw.ellipse([7, 10, 43, 46], fill=(185, 188, 38, 255))
    draw.ellipse([9, 12, 41, 44], fill=(208, 212, 52, 255))
    draw.ellipse([11, 13, 24, 26], fill=(238, 242, 115, 255))  # highlight
    # bumpy wrinkled skin texture
    for (px, py) in [(16,16),(30,14),(38,22),(40,34),(32,42),(18,44),(10,36),(8,24)]:
        draw.ellipse([px-2, py-2, px+2, py+2], fill=(165, 168, 28, 255))
        draw.ellipse([px-1, py-1, px+1, py+1], fill=(238, 242, 115, 255))
    # stem
    draw.line([(25, 10), (25, 4)], fill=BROWN, width=2)
    draw.polygon([(25, 5), (31, 1), (27, 8)], fill=DKGREEN)

# 16. Clementine
def draw_clementine(draw):
    draw.ellipse([10, 16, 40, 44], fill=ORANGE)
    draw.ellipse([12, 18, 38, 42], fill=LIGHTORANGE)
    draw.ellipse([14, 18, 24, 28], fill=(255, 225, 165, 255))   # highlight
    # segment lines
    for a in [30, 90, 150, 210, 270, 330]:
        import math
        x = int(25 + 14 * math.cos(math.radians(a)))
        y = int(30 + 13 * math.sin(math.radians(a)))
        draw.line([(25, 30), (x, y)], fill=(215, 112, 8, 255), width=1)
    # leaf & stem
    draw.line([(25, 16), (25, 9)], fill=BROWN, width=2)
    draw.polygon([(25, 10), (35, 4), (28, 12)], fill=GREEN)
    draw.line([(25, 7), (32, 5)], fill=DKGREEN, width=1)

# 17. Satsuma
def draw_satsuma(draw):
    # flattened orange sphere
    draw.ellipse([8, 18, 42, 44], fill=ORANGE)
    draw.ellipse([10, 20, 40, 42], fill=LIGHTORANGE)
    draw.ellipse([12, 20, 24, 30], fill=(255, 225, 165, 255))  # highlight
    # segment seams
    for a in [0, 60, 120, 180, 240, 300]:
        import math
        x = int(25 + 16 * math.cos(math.radians(a)))
        y = int(31 + 11 * math.sin(math.radians(a)))
        draw.line([(25, 31), (x, y)], fill=(215, 112, 8, 255), width=1)
    # stem button at top
    draw.ellipse([22, 16, 28, 20], fill=DKGREEN)
    draw.line([(25, 20), (25, 15)], fill=BROWN, width=2)

# 18. Yuzu
def draw_yuzu(draw):
    # rough pale yellow sphere
    draw.ellipse([10, 12, 40, 44], fill=YELLOW)
    draw.ellipse([12, 14, 38, 42], fill=LIGHTYELLOW)
    draw.ellipse([14, 14, 24, 24], fill=(255, 255, 218, 255))  # highlight
    # rough bumpy skin texture
    for (px, py) in [(18,20),(30,18),(36,26),(34,36),(24,42),(14,36),(10,26)]:
        draw.ellipse([px-2, py-2, px+2, py+2], fill=ORANGE)
        draw.ellipse([px-1, py-1, px+1, py+1], fill=LIGHTYELLOW)
    # stem & leaf
    draw.line([(25, 12), (25, 6)], fill=BROWN, width=2)
    draw.polygon([(25, 7), (33, 2), (28, 10)], fill=DKGREEN)

# 19. Buddha's Hand
def draw_buddhas_hand(draw):
    # main body blob
    draw.ellipse([16, 10, 34, 30], fill=YELLOW)
    draw.ellipse([18, 12, 32, 28], fill=LIGHTYELLOW)
    # finger extensions hanging down
    finger_x = [14, 18, 22, 26, 30, 34]
    for i, fx in enumerate(finger_x):
        length = 22 + (abs(i - 2.5)) * 2
        draw.line([(fx, 26), (fx + (fx-25)//3, int(26+length))],
                  fill=YELLOW, width=3)
        draw.ellipse([fx-2, int(26+length)-2, fx+2+(fx-25)//3, int(26+length)+4],
                     fill=LIGHTYELLOW)
    # re-draw body on top
    draw.ellipse([16, 10, 34, 30], fill=YELLOW)
    draw.ellipse([18, 12, 32, 28], fill=LIGHTYELLOW)
    draw.ellipse([19, 12, 26, 19], fill=(255, 255, 218, 255))  # highlight
    # stem
    draw.line([(25, 10), (25, 4)], fill=BROWN, width=2)
    draw.polygon([(25, 5), (31, 1), (27, 8)], fill=DKGREEN)

# 20. Rowanberry
def draw_rowanberry(draw):
    # branching stems
    draw.line([(25, 6), (16, 22)], fill=BROWN, width=2)
    draw.line([(25, 6), (34, 22)], fill=BROWN, width=2)
    draw.line([(16, 22), (10, 30)], fill=BROWN, width=1)
    draw.line([(16, 22), (20, 30)], fill=BROWN, width=1)
    draw.line([(34, 22), (28, 30)], fill=BROWN, width=1)
    draw.line([(34, 22), (38, 30)], fill=BROWN, width=1)
    # berries
    for (bx, by) in [(8,28),(14,32),(20,28),(26,32),(30,28),(36,32),(12,40),(22,40),(32,40)]:
        draw.ellipse([bx-4, by-4, bx+4, by+4], fill=RED)
        draw.ellipse([bx-3, by-3, bx+3, by+3], fill=LIGHTRED)
        draw.ellipse([bx-2, by-2, bx-1, by-1], fill=(255, 215, 210, 255))
        draw.ellipse([bx-1, by+2, bx+1, by+4], fill=BLACK)  # calyx dot

# 21. Barberry
def draw_barberry(draw):
    # stem with leaves
    draw.line([(25, 6), (16, 22)], fill=BROWN, width=1)
    draw.line([(25, 6), (34, 22)], fill=BROWN, width=1)
    draw.polygon([(20, 12), (14, 8), (18, 16)], fill=GREEN)
    draw.polygon([(30, 12), (36, 8), (32, 16)], fill=GREEN)
    # two elongated red berries
    draw.rounded_rectangle([11, 22, 22, 40], radius=4, fill=DKRED)
    draw.rounded_rectangle([12, 23, 21, 36], radius=3, fill=RED)
    draw.ellipse([13, 23, 18, 28], fill=LIGHTRED)
    draw.rounded_rectangle([28, 22, 39, 40], radius=4, fill=DKRED)
    draw.rounded_rectangle([29, 23, 38, 36], radius=3, fill=RED)
    draw.ellipse([30, 23, 35, 28], fill=LIGHTRED)
    # tiny stem tips
    draw.line([(16, 22), (16, 40)], fill=BROWN, width=1)
    draw.line([(33, 22), (33, 40)], fill=BROWN, width=1)

# 22. Juniper Berry
def draw_juniper_berry(draw):
    # dusty blue-purple berry
    draw.ellipse([10, 14, 40, 44], fill=DARKBLUE)
    draw.ellipse([12, 16, 38, 42], fill=PURPLE)
    draw.ellipse([14, 16, 24, 26], fill=(148, 82, 172, 255))  # highlight
    # glaucous waxy bloom (lighter overlay)
    draw.arc([12, 16, 38, 42], 200, 340, fill=(125, 95, 152, 255), width=2)
    # tri-scale mark at top (distinctive feature)
    draw.line([(25, 20), (20, 30)], fill=BLACK, width=1)
    draw.line([(25, 20), (30, 30)], fill=BLACK, width=1)
    draw.line([(25, 20), (25, 32)], fill=BLACK, width=1)
    draw.ellipse([23, 18, 27, 22], fill=BLACK)  # tip dot

# 23. Marionberry
def draw_marionberry(draw):
    drupes = [(0,0),(-4,4),(4,4),(-6,10),(0,10),(6,10),(-4,16),(4,16),(0,20)]
    for ox, oy in drupes:
        draw.ellipse([22+ox, 14+oy, 28+ox, 20+oy], fill=MAROON)
        draw.ellipse([23+ox, 15+oy, 27+ox, 19+oy], fill=(105, 28, 55, 255))
        draw.ellipse([23+ox, 15+oy, 25+ox, 17+oy], fill=(158, 68, 95, 255))
    draw.polygon([(20, 14), (25, 8),  (30, 13)], fill=GREEN)
    draw.polygon([(25, 13),(29, 8),(33, 14)],   fill=DKGREEN)
    draw.line([(25, 8), (25, 4)], fill=BROWN, width=1)

# 24. Physalis (Cape Gooseberry)
def draw_physalis(draw):
    # papery husk (lantern shape)
    draw.polygon([(25, 5), (8, 30), (25, 46), (42, 30)], fill=YELLOW)
    # husk vein ribs
    draw.line([(25, 5), (8, 30)],   fill=ORANGE, width=1)
    draw.line([(25, 5), (42, 30)],  fill=ORANGE, width=1)
    draw.line([(8, 30), (25, 46)],  fill=ORANGE, width=1)
    draw.line([(42, 30), (25, 46)], fill=ORANGE, width=1)
    draw.line([(25, 5), (25, 46)],  fill=ORANGE, width=1)
    draw.line([(8, 30), (42, 30)],  fill=ORANGE, width=1)
    draw.ellipse([22, 8, 28, 14],   fill=ORANGE)  # husk highlight
    # inner berry
    draw.ellipse([18, 22, 32, 38], fill=ORANGE)
    draw.ellipse([20, 24, 30, 36], fill=LIGHTORANGE)
    draw.ellipse([21, 24, 25, 28], fill=(255, 230, 175, 255))  # berry shine


# 25. Miracle Fruit
def draw_miracle_fruit(draw):
    # small oblong bright red berry
    draw.rounded_rectangle([15, 12, 35, 40], radius=8, fill=DKRED)
    draw.rounded_rectangle([17, 14, 33, 38], radius=7, fill=RED)
    draw.ellipse([18, 14, 26, 22], fill=LIGHTRED)   # highlight
    # longitudinal crease
    draw.line([(25, 12), (25, 40)], fill=DKRED, width=1)
    # calyx at top
    draw.polygon([(20, 12), (25, 6),  (28, 11)], fill=GREEN)
    draw.polygon([(25, 11),(30, 6),(32, 12)],   fill=DKGREEN)
    draw.ellipse([23, 9, 27, 13], fill=BROWN)  # stem nub
    # stem
    draw.line([(25, 9), (25, 4)], fill=BROWN, width=2)

# ─── DISPATCH ─────────────────────────────────────────────────────────────────

fruits = [
    ("rambutan",      draw_rambutan),
    ("breadfruit",    draw_breadfruit),
    ("salak",         draw_salak),
    ("soursop",       draw_soursop),
    ("custard_apple", draw_custard_apple),
    ("longan",        draw_longan),
    ("medlar",        draw_medlar),
    ("loquat",        draw_loquat),
    ("bilberry",      draw_bilberry),
    ("cloudberry",    draw_cloudberry),
    ("huckleberry",   draw_huckleberry),
    ("lingonberry",   draw_lingonberry),
    ("feijoa",        draw_feijoa),
    ("tamarind",      draw_tamarind),
    ("ugli_fruit",    draw_ugli_fruit),
    ("clementine",    draw_clementine),
    ("satsuma",       draw_satsuma),
    ("yuzu",          draw_yuzu),
    ("buddhas_hand",  draw_buddhas_hand),
    ("rowanberry",    draw_rowanberry),
    ("barberry",      draw_barberry),
    ("juniper_berry", draw_juniper_berry),
    ("marionberry",   draw_marionberry),
    ("physalis",      draw_physalis),
    ("miracle_fruit", draw_miracle_fruit),
]

print(f"Generating {len(fruits)} enhanced fruit sprites in '{OUTPUT_DIR}'...")
for name, func in fruits:
    create_sprite(name, func)
print("\nAll 25 enhanced fruit sprites generated successfully!")
