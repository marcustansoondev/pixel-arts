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

# Color constants
RED       = (220, 40, 40, 255)
DKRED     = (130, 20, 20, 255)
LIGHTRED  = (255, 100, 100, 255)
ORANGE    = (255, 140, 0, 255)
LIGHTORANGE = (255, 180, 70, 255)
YELLOW    = (240, 220, 40, 255)
LIGHTYELLOW = (255, 245, 140, 255)
GREEN     = (40, 160, 40, 255)
DKGREEN   = (20, 90, 20, 255)
LIGHTGREEN = (120, 220, 120, 255)
BROWN     = (110, 70, 30, 255)
DKBROWN   = (65, 40, 15, 255)
WHITE     = (255, 255, 255, 255)
BLACK     = (0, 0, 0, 255)
DARKBLUE  = (20, 30, 70, 255)
PURPLE    = (100, 40, 120, 255)
MAROON    = (80, 15, 40, 255)
BEIGE     = (220, 190, 150, 255)

# 1. Rambutan
def draw_rambutan(draw):
    draw.ellipse([14, 14, 36, 36], fill=RED)
    # hairy spikes
    spikes = [(14, 10), (10, 14), (25, 8), (36, 10), (40, 14), (42, 25), (40, 36), (36, 40), (25, 42), (14, 40), (10, 36), (8, 25)]
    for sx, sy in spikes:
        draw.line([(25, 25), (sx, sy)], fill=DKRED, width=2)
    draw.ellipse([16, 16, 34, 34], fill=RED)
    draw.ellipse([18, 18, 30, 30], fill=LIGHTRED)

# 2. Breadfruit
def draw_breadfruit(draw):
    draw.ellipse([12, 12, 38, 38], fill=DKGREEN)
    # grid bumps
    for x in range(16, 36, 4):
        for y in range(16, 36, 4):
            draw.point((x, y), fill=LIGHTGREEN)
    draw.line([(25, 12), (25, 6)], fill=BROWN, width=2)

# 3. Salak (Snake Fruit)
def draw_salak(draw):
    # brown scaly teardrop
    draw.polygon([(25, 10), (12, 34), (16, 40), (34, 40), (38, 34)], fill=DKBROWN)
    draw.polygon([(25, 14), (16, 34), (18, 38), (32, 38), (34, 34)], fill=BROWN)
    # scales
    for y in range(20, 40, 5):
        draw.arc([16, y, 34, y+6], 0, 180, fill=DKBROWN, width=1)

# 4. Soursop
def draw_soursop(draw):
    # bumpy/spiky dark green kidney shape
    draw.ellipse([12, 14, 38, 38], fill=DKGREEN)
    draw.ellipse([16, 20, 32, 42], fill=DKGREEN)
    # spikes
    spikes = [(10, 20), (14, 12), (25, 10), (36, 12), (40, 20), (38, 30), (34, 40), (25, 44), (16, 40), (12, 30)]
    for sx, sy in spikes:
        draw.polygon([(25, 25), (sx, sy), (sx+2, sy+2)], fill=DKGREEN)
    draw.ellipse([14, 16, 36, 36], fill=GREEN)

# 5. Custard Apple
def draw_custard_apple(draw):
    # green bumpy round shape
    draw.ellipse([12, 12, 38, 38], fill=DKGREEN)
    for cx, cy in [(17, 17), (25, 15), (33, 17), (15, 25), (25, 25), (35, 25), (17, 33), (25, 35), (33, 33)]:
        draw.ellipse([cx-4, cy-4, cx+4, cy+4], fill=GREEN)
        draw.ellipse([cx-2, cy-2, cx+2, cy+2], fill=LIGHTGREEN)

# 6. Longan
def draw_longan(draw):
    # brown-beige small round fruit
    draw.ellipse([6, 16, 28, 38], fill=BEIGE)
    draw.ellipse([8, 18, 26, 36], fill=BROWN)
    # peeled version showing white flesh & black seed
    draw.ellipse([22, 14, 44, 36], fill=WHITE)
    draw.ellipse([26, 18, 40, 32], fill=BLACK)
    draw.ellipse([28, 20, 32, 24], fill=WHITE)

# 7. Medlar
def draw_medlar(draw):
    # brown round fruit with a crown/opening at bottom
    draw.ellipse([12, 12, 38, 38], fill=DKBROWN)
    draw.ellipse([14, 14, 36, 36], fill=BROWN)
    # puckered top/star opening
    draw.polygon([(25, 30), (22, 38), (28, 38)], fill=DKBROWN)
    draw.polygon([(25, 38), (22, 30), (28, 30)], fill=DKBROWN)
    draw.polygon([(20, 34), (30, 34), (25, 34)], fill=DKBROWN)

# 8. Loquat
def draw_loquat(draw):
    draw.ellipse([14, 16, 36, 42], fill=ORANGE)
    draw.ellipse([16, 18, 34, 40], fill=LIGHTORANGE)
    draw.line([(25, 16), (25, 8)], fill=DKGREEN, width=2)
    draw.polygon([(25, 10), (32, 6), (28, 12)], fill=GREEN)

# 9. Bilberry
def draw_bilberry(draw):
    # deep blue-black small berry
    draw.ellipse([12, 18, 36, 42], fill=DARKBLUE)
    draw.ellipse([15, 21, 33, 39], fill=(40, 50, 110, 255))
    # crown at the top
    draw.polygon([(21, 18), (25, 14), (29, 18)], fill=BLACK)
    draw.polygon([(25, 18), (25, 22), (29, 18)], fill=BLACK)
    # double berry cluster
    draw.ellipse([22, 12, 42, 32], fill=DARKBLUE)

# 10. Cloudberry
def draw_cloudberry(draw):
    # amber/orange aggregate drupelets
    offsets = [(21, 14), (29, 14), (17, 20), (25, 20), (33, 20), (21, 26), (29, 26), (25, 32)]
    for gx, gy in offsets:
        draw.ellipse([gx, gy, gx+8, gy+8], fill=ORANGE)
        draw.ellipse([gx+1, gy+1, gx+5, gy+5], fill=LIGHTORANGE)
    # green sepals at base
    draw.polygon([(14, 32), (20, 38), (25, 32)], fill=GREEN)
    draw.polygon([(36, 32), (30, 38), (25, 32)], fill=GREEN)

# 11. Huckleberry
def draw_huckleberry(draw):
    # dark purple small berry
    draw.ellipse([12, 18, 36, 42], fill=PURPLE)
    draw.ellipse([15, 21, 33, 39], fill=(150, 70, 180, 255))
    draw.polygon([(22, 18), (25, 13), (28, 18)], fill=BLACK)

# 12. Lingonberry
def draw_lingonberry(draw):
    # bright red round berry
    draw.ellipse([10, 18, 32, 40], fill=DKRED)
    draw.ellipse([12, 20, 30, 38], fill=RED)
    draw.ellipse([14, 22, 24, 32], fill=LIGHTRED)
    # sepals/black dot at base
    draw.ellipse([20, 38, 23, 41], fill=BLACK)
    # another berry
    draw.ellipse([22, 12, 42, 32], fill=DKRED)
    draw.ellipse([24, 14, 40, 30], fill=RED)

# 13. Feijoa
def draw_feijoa(draw):
    # green egg-shaped fruit with cross-shaped crown
    draw.ellipse([14, 14, 36, 42], fill=DKGREEN)
    draw.ellipse([16, 16, 34, 40], fill=GREEN)
    # cross-shaped crown at top
    draw.line([(22, 12), (28, 16)], fill=DKBROWN, width=2)
    draw.line([(28, 12), (22, 16)], fill=DKBROWN, width=2)

# 14. Tamarind
def draw_tamarind(draw):
    # brown curved pod shape
    draw.arc([10, 10, 40, 40], 40, 180, fill=DKBROWN, width=6)
    draw.ellipse([9, 26, 15, 32], fill=BROWN)
    draw.ellipse([35, 17, 41, 23], fill=BROWN)

# 15. Ugli Fruit
def draw_ugli_fruit(draw):
    # wrinkled yellow-green teardrop shape
    draw.ellipse([10, 16, 40, 44], fill=(190, 190, 40, 255))
    draw.polygon([(25, 8), (14, 20), (36, 20)], fill=(190, 190, 40, 255))
    draw.ellipse([12, 18, 38, 42], fill=(210, 210, 50, 255))
    # brown spots
    draw.point((20, 24), fill=BROWN)
    draw.point((30, 28), fill=BROWN)
    draw.point((24, 36), fill=BROWN)
    # green stem
    draw.line([(25, 8), (25, 4)], fill=DKGREEN, width=2)

# 16. Clementine
def draw_clementine(draw):
    # small bright orange sphere with leaf
    draw.ellipse([12, 16, 38, 42], fill=ORANGE)
    draw.ellipse([16, 20, 34, 38], fill=LIGHTORANGE)
    # leaf
    draw.polygon([(25, 16), (35, 8), (28, 6)], fill=GREEN)
    draw.line([(25, 16), (25, 12)], fill=BROWN, width=2)

# 17. Satsuma
def draw_satsuma(draw):
    # squashed orange citrus
    draw.ellipse([10, 16, 40, 42], fill=ORANGE)
    draw.ellipse([12, 18, 38, 40], fill=LIGHTORANGE)
    # green button center
    draw.ellipse([23, 14, 27, 18], fill=DKGREEN)

# 18. Yuzu
def draw_yuzu(draw):
    # rough pale yellow citrus
    draw.ellipse([12, 14, 38, 40], fill=YELLOW)
    draw.ellipse([14, 16, 36, 38], fill=LIGHTYELLOW)
    # rough textures
    for x, y in [(18, 22), (32, 24), (20, 32), (30, 34), (25, 28)]:
        draw.point((x, y), fill=ORANGE)
    draw.line([(25, 14), (25, 10)], fill=DKGREEN, width=2)

# 19. Buddha's Hand
def draw_buddhas_hand(draw):
    # fingered yellow citrus shape
    draw.ellipse([16, 12, 34, 30], fill=YELLOW)
    # fingers hanging down
    for fx in [14, 18, 22, 26, 30, 34]:
        draw.line([(fx, 25), (fx + (fx-25)//2, 44)], fill=YELLOW, width=2)
    # stem
    draw.line([(25, 12), (25, 6)], fill=DKGREEN, width=2)

# 20. Rowanberry
def draw_rowanberry(draw):
    # clusters of tiny orange-red berries
    draw.line([(25, 8), (18, 24)], fill=BROWN, width=1)
    draw.line([(25, 8), (32, 24)], fill=BROWN, width=1)
    offsets = [(14, 20), (22, 20), (30, 20), (10, 26), (18, 26), (26, 26), (34, 26), (14, 32), (22, 32), (30, 32)]
    for rx, ry in offsets:
        draw.ellipse([rx, ry, rx+6, ry+6], fill=RED)
        draw.ellipse([rx+1, ry+1, rx+3, ry+3], fill=LIGHTORANGE)
        draw.point((rx+3, ry+5), fill=BLACK)

# 21. Barberry
def draw_barberry(draw):
    # elongated bright red berries
    draw.line([(25, 8), (18, 22)], fill=BROWN, width=1)
    draw.line([(25, 8), (32, 22)], fill=BROWN, width=1)
    # berry 1
    draw.rounded_rectangle([14, 20, 22, 36], radius=3, fill=RED)
    draw.ellipse([16, 22, 20, 28], fill=LIGHTRED)
    # berry 2
    draw.rounded_rectangle([28, 20, 36, 36], radius=3, fill=RED)
    draw.ellipse([30, 22, 34, 28], fill=LIGHTRED)

# 22. Juniper Berry
def draw_juniper_berry(draw):
    # dusty blue-purple berry with scales
    draw.ellipse([12, 16, 38, 42], fill=DARKBLUE)
    draw.ellipse([14, 18, 36, 40], fill=PURPLE)
    # tri-lobed scale mark
    draw.line([(25, 29), (21, 23)], fill=BLACK, width=1)
    draw.line([(25, 29), (29, 23)], fill=BLACK, width=1)
    draw.line([(25, 29), (25, 37)], fill=BLACK, width=1)

# 23. Marionberry
def draw_marionberry(draw):
    # dark maroon-black aggregate berry
    for offset in [(0,0), (-4, 4), (4, 4), (-6, 10), (0, 10), (6, 10), (-4, 16), (4, 16), (0, 20)]:
        draw.ellipse([22+offset[0], 16+offset[1], 28+offset[0], 22+offset[1]], fill=MAROON)
        draw.ellipse([23+offset[0], 17+offset[1], 26+offset[0], 20+offset[1]], fill=BLACK)
    draw.polygon([(21, 16), (25, 11), (29, 16)], fill=GREEN)

# 24. Physalis (Cape Gooseberry)
def draw_physalis(draw):
    # yellow-orange papery husk enclosing a berry
    draw.polygon([(25, 6), (10, 30), (25, 44), (40, 30)], fill=YELLOW)
    # outer veins
    draw.line([(25, 6), (25, 44)], fill=ORANGE, width=1)
    draw.line([(10, 30), (40, 30)], fill=ORANGE, width=1)
    # inner berry hint visible via cut
    draw.ellipse([20, 22, 30, 32], fill=ORANGE)
    draw.ellipse([22, 24, 28, 30], fill=LIGHTORANGE)

# 25. Miracle Fruit
def draw_miracle_fruit(draw):
    # small oblong bright red berry
    draw.rounded_rectangle([16, 14, 34, 38], radius=6, fill=DKRED)
    draw.rounded_rectangle([18, 16, 32, 36], radius=5, fill=RED)
    draw.ellipse([20, 18, 26, 24], fill=LIGHTRED)
    # green stem
    draw.line([(25, 14), (25, 8)], fill=DKGREEN, width=2)

# Build all 25 new fruits
fruits = [
    ("rambutan", draw_rambutan),
    ("breadfruit", draw_breadfruit),
    ("salak", draw_salak),
    ("soursop", draw_soursop),
    ("custard_apple", draw_custard_apple),
    ("longan", draw_longan),
    ("medlar", draw_medlar),
    ("loquat", draw_loquat),
    ("bilberry", draw_bilberry),
    ("cloudberry", draw_cloudberry),
    ("huckleberry", draw_huckleberry),
    ("lingonberry", draw_lingonberry),
    ("feijoa", draw_feijoa),
    ("tamarind", draw_tamarind),
    ("ugli_fruit", draw_ugli_fruit),
    ("clementine", draw_clementine),
    ("satsuma", draw_satsuma),
    ("yuzu", draw_yuzu),
    ("buddhas_hand", draw_buddhas_hand),
    ("rowanberry", draw_rowanberry),
    ("barberry", draw_barberry),
    ("juniper_berry", draw_juniper_berry),
    ("marionberry", draw_marionberry),
    ("physalis", draw_physalis),
    ("miracle_fruit", draw_miracle_fruit)
]

print(f"Generating {len(fruits)} new fruit sprites in '{OUTPUT_DIR}'...")
for name, func in fruits:
    create_sprite(name, func)
print("\nAll 25 new fruit sprites generated successfully!")
