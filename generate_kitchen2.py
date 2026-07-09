import os
from PIL import Image, ImageDraw

OUTPUT_DIR = "images/kitchen"
os.makedirs(OUTPUT_DIR, exist_ok=True)

def create_sprite(name, draw_func):
    img = Image.new("RGBA", (50, 50), (255, 255, 255, 0))
    draw = ImageDraw.Draw(img)
    draw_func(draw)
    path = os.path.join(OUTPUT_DIR, f"{name}_50x50.png")
    img.save(path)
    print(f"  Saved: {path}")

# Shared colours (≤10 per sprite)
SILVER  = (180, 180, 190, 255)
STEEL   = (120, 125, 135, 255)
DARK    = ( 50,  50,  55, 255)
WHITE   = (245, 245, 245, 255)
CREAM   = (230, 220, 200, 255)
TAN     = (190, 160, 110, 255)
BROWN   = (130,  90,  50, 255)
RED     = (210,  50,  50, 255)
DKRED   = (160,  30,  30, 255)
ORANGE  = (230, 120,  30, 255)
YELLOW  = (230, 200,  40, 255)
GREEN   = ( 70, 160,  60, 255)
DKGREEN = ( 30, 100,  30, 255)
BLUE    = ( 60, 110, 200, 255)
DKBLUE  = ( 30,  70, 160, 255)
BLACK   = ( 20,  20,  20, 255)
GLASS   = (180, 215, 240, 200)
PINK    = (230, 130, 150, 255)
PURPLE  = (130,  70, 190, 255)
GREY    = (160, 160, 165, 255)


# ── 51. WOK ──────────────────────────────────────
def draw_wok(draw):
    # deep rounded wok bowl
    draw.chord([4, 18, 46, 50], 0, 180, fill=DARK)
    draw.chord([6, 20, 44, 48], 0, 180, fill=(60, 60, 65, 255))
    # flat rim
    draw.ellipse([4, 16, 46, 24], fill=DARK)
    draw.ellipse([6, 17, 44, 23], fill=STEEL)
    # two short side handles
    draw.rounded_rectangle([0, 17, 6, 22], radius=2, fill=BROWN)
    draw.rounded_rectangle([44, 17, 50, 22], radius=2, fill=BROWN)
    # shine arc
    draw.arc([8, 22, 22, 34], 200, 320, fill=STEEL, width=2)

# ── 52. WAFFLE IRON ──────────────────────────────
def draw_waffle_iron(draw):
    # base unit
    draw.rounded_rectangle([4, 28, 46, 46], radius=4, fill=DARK)
    draw.rounded_rectangle([6, 30, 44, 44], radius=3, fill=(60, 60, 65, 255))
    # top plate
    draw.rounded_rectangle([6, 16, 44, 30], radius=4, fill=DARK)
    draw.rounded_rectangle([8, 18, 42, 28], radius=3, fill=(60, 60, 65, 255))
    # waffle grid on top
    for x in [12, 20, 28, 36]:
        draw.line([x, 18, x, 28], fill=STEEL, width=1)
    for y in [21, 25]:
        draw.line([8, y, 42, y], fill=STEEL, width=1)
    # hinge
    draw.rectangle([20, 14, 30, 18], fill=STEEL)
    # handle
    draw.rounded_rectangle([34, 10, 46, 16], radius=3, fill=BROWN)

# ── 53. ICE CREAM SCOOP ──────────────────────────
def draw_ice_cream_scoop(draw):
    # handle
    draw.rounded_rectangle([4, 28, 28, 36], radius=4, fill=SILVER)
    draw.line([6, 32, 26, 32], fill=WHITE, width=1)
    # neck
    draw.rectangle([26, 30, 32, 34], fill=STEEL)
    # scoop bowl (half circle)
    draw.chord([30, 16, 48, 34], 0, 180, fill=SILVER)
    draw.chord([32, 18, 46, 32], 0, 180, fill=(200, 205, 215, 255))
    # release lever
    draw.line([6, 29, 24, 29], fill=DARK, width=2)

# ── 54. PIZZA CUTTER ─────────────────────────────
def draw_pizza_cutter(draw):
    # handle
    draw.rounded_rectangle([4, 8, 22, 26], radius=5, fill=RED)
    draw.line([8, 12, 18, 22], fill=DKRED, width=2)
    # axle rod
    draw.line([20, 20, 34, 34], fill=STEEL, width=3)
    # circular blade
    draw.ellipse([30, 30, 48, 48], fill=SILVER)
    draw.ellipse([32, 32, 46, 46], fill=(200, 205, 215, 255))
    draw.ellipse([37, 37, 41, 41], fill=DARK)

# ── 55. MEAT TENDERIZER ──────────────────────────
def draw_meat_tenderizer(draw):
    # handle
    draw.rounded_rectangle([22, 26, 28, 48], radius=4, fill=BROWN)
    draw.line([24, 28, 26, 46], fill=TAN, width=1)
    # neck
    draw.rectangle([20, 20, 30, 26], fill=STEEL)
    # square head
    draw.rectangle([10, 8, 40, 22], fill=SILVER)
    draw.rectangle([12, 10, 38, 20], fill=(200, 205, 215, 255))
    # spike grid on face
    for col in range(4):
        for row in range(2):
            x = 14 + col * 6
            y = 11 + row * 5
            draw.ellipse([x, y, x+3, y+3], fill=DARK)

# ── 56. KITCHEN SCALE ────────────────────────────
def draw_kitchen_scale(draw):
    # base
    draw.rounded_rectangle([4, 34, 46, 46], radius=5, fill=WHITE)
    draw.rounded_rectangle([6, 36, 44, 44], radius=4, fill=CREAM)
    # bowl/platform
    draw.chord([8, 18, 42, 38], 180, 360, fill=SILVER)
    draw.chord([10, 20, 40, 36], 180, 360, fill=(200, 205, 215, 255))
    draw.ellipse([8, 16, 42, 24], fill=SILVER)
    draw.ellipse([10, 17, 40, 23], fill=WHITE)
    # display window
    draw.rounded_rectangle([14, 36, 36, 42], radius=2, fill=GREEN)
    draw.rectangle([16, 37, 22, 41], fill=DKGREEN)

# ── 57. SLOTTED SPOON ────────────────────────────
def draw_slotted_spoon(draw):
    # handle
    draw.rounded_rectangle([22, 30, 28, 48], radius=3, fill=SILVER)
    draw.rounded_rectangle([23, 20, 27, 30], radius=2, fill=SILVER)
    # spoon bowl
    draw.ellipse([16, 8, 34, 22], fill=SILVER)
    draw.ellipse([17, 9, 33, 21], fill=(200, 205, 215, 255))
    # drainage slots
    draw.ellipse([19, 11, 22, 14], fill=(0, 0, 0, 0))
    draw.ellipse([24, 11, 27, 14], fill=(0, 0, 0, 0))
    draw.ellipse([29, 11, 32, 14], fill=(0, 0, 0, 0))
    draw.ellipse([21, 15, 24, 18], fill=(0, 0, 0, 0))
    draw.ellipse([27, 15, 30, 18], fill=(0, 0, 0, 0))

# ── 58. PASTRY BRUSH ─────────────────────────────
def draw_pastry_brush(draw):
    # handle
    draw.rounded_rectangle([20, 6, 30, 32], radius=4, fill=TAN)
    draw.line([24, 8, 26, 30], fill=BROWN, width=1)
    # ferrule (metal band)
    draw.rectangle([20, 30, 30, 34], fill=STEEL)
    # bristles
    for x in range(18, 32, 2):
        draw.line([x, 34, x, 46], fill=CREAM, width=1)
    draw.line([18, 34, 32, 34], fill=STEEL, width=1)

# ── 59. MELON BALLER ─────────────────────────────
def draw_melon_baller(draw):
    # handle
    draw.rounded_rectangle([4, 22, 30, 28], radius=4, fill=SILVER)
    draw.line([6, 25, 28, 25], fill=WHITE, width=1)
    # neck
    draw.rectangle([28, 23, 34, 27], fill=STEEL)
    # scoop hemisphere
    draw.chord([33, 18, 47, 32], 0, 180, fill=SILVER)
    draw.chord([34, 19, 46, 31], 0, 180, fill=(200, 205, 215, 255))

# ── 60. ZESTER ───────────────────────────────────
def draw_zester(draw):
    # handle
    draw.rounded_rectangle([4, 22, 26, 28], radius=4, fill=GREEN)
    draw.line([6, 25, 24, 25], fill=DKGREEN, width=1)
    # neck
    draw.rectangle([24, 23, 30, 27], fill=STEEL)
    # zester head (long flat paddle)
    draw.rounded_rectangle([28, 16, 48, 34], radius=3, fill=SILVER)
    draw.rounded_rectangle([30, 18, 46, 32], radius=2, fill=(200, 205, 215, 255))
    # tiny zester holes
    for col in range(3):
        for row in range(3):
            x = 32 + col * 4
            y = 20 + row * 4
            draw.ellipse([x, y, x+2, y+2], fill=DARK)

# ── 61. MANDOLINE SLICER ─────────────────────────
def draw_mandoline_slicer(draw):
    # main board (angled)
    draw.polygon([(4, 40), (46, 10), (46, 18), (4, 46)], fill=CREAM)
    draw.polygon([(6, 40), (44, 12), (44, 16), (6, 44)], fill=WHITE)
    # blade slot
    draw.line([10, 38, 42, 14], fill=STEEL, width=3)
    # blade highlight
    draw.line([10, 36, 42, 12], fill=SILVER, width=1)
    # handle guard at top
    draw.rounded_rectangle([38, 6, 48, 14], radius=3, fill=RED)
    # feet/stands
    draw.rectangle([4, 44, 10, 48], fill=DARK)
    draw.rectangle([38, 16, 44, 20], fill=DARK)

# ── 62. STOCKPOT ─────────────────────────────────
def draw_stockpot(draw):
    # taller body than regular pot
    draw.rounded_rectangle([8, 12, 42, 44], radius=4, fill=STEEL)
    draw.rounded_rectangle([10, 14, 40, 42], radius=3, fill=SILVER)
    # rim
    draw.rectangle([7, 10, 43, 13], fill=DARK)
    # lid
    draw.ellipse([8, 4, 42, 12], fill=STEEL)
    draw.ellipse([11, 5, 39, 11], fill=SILVER)
    draw.ellipse([21, 2, 29, 8], fill=DARK)
    # two handles
    draw.ellipse([0, 18, 10, 28], fill=DARK)
    draw.ellipse([2, 20, 8, 26], fill=(0, 0, 0, 0))
    draw.ellipse([40, 18, 50, 28], fill=DARK)
    draw.ellipse([42, 20, 48, 26], fill=(0, 0, 0, 0))

# ── 63. CAST IRON SKILLET ────────────────────────
def draw_skillet(draw):
    # pan body (round and heavy)
    draw.ellipse([6, 16, 44, 46], fill=DARK)
    draw.ellipse([8, 18, 42, 44], fill=(40, 40, 45, 255))
    # seasoning sheen
    draw.arc([10, 20, 24, 34], 200, 320, fill=(60, 60, 65, 255), width=2)
    # long handle
    draw.rounded_rectangle([40, 28, 50, 34], radius=3, fill=DARK)
    draw.rectangle([44, 30, 50, 32], fill=(60, 60, 65, 255))
    # pour spout notch
    draw.polygon([(6, 24), (2, 20), (6, 18)], fill=DARK)

# ── 64. DUTCH OVEN ───────────────────────────────
def draw_dutch_oven(draw):
    # wide deep body
    draw.rounded_rectangle([6, 16, 44, 44], radius=6, fill=(180, 50, 50, 255))
    draw.rounded_rectangle([8, 18, 42, 42], radius=5, fill=RED)
    # rim
    draw.rectangle([5, 14, 45, 17], fill=DKRED)
    # lid (domed)
    draw.ellipse([6, 6, 44, 16], fill=(180, 50, 50, 255))
    draw.ellipse([9, 7, 41, 15], fill=RED)
    draw.ellipse([21, 3, 29, 9], fill=DKRED)
    # side handles
    draw.rounded_rectangle([0, 22, 8, 30], radius=3, fill=DKRED)
    draw.rounded_rectangle([42, 22, 50, 30], radius=3, fill=DKRED)

# ── 65. SALAD SPINNER ────────────────────────────
def draw_salad_spinner(draw):
    # outer bowl
    draw.chord([4, 18, 46, 50], 0, 180, fill=GLASS)
    draw.chord([6, 20, 44, 48], 0, 180, fill=(210, 235, 250, 220))
    draw.ellipse([4, 16, 46, 24], fill=GLASS)
    draw.ellipse([6, 17, 44, 23], fill=WHITE)
    # lid with pump knob on top
    draw.ellipse([6, 8, 44, 18], fill=GLASS)
    draw.ellipse([8, 9, 42, 17], fill=WHITE)
    draw.ellipse([20, 4, 30, 12], fill=GREEN)
    draw.ellipse([22, 5, 28, 11], fill=DKGREEN)

# ── 66. EGG CUP ──────────────────────────────────
def draw_egg_cup(draw):
    # cup base
    draw.rounded_rectangle([16, 34, 34, 46], radius=4, fill=YELLOW)
    draw.rounded_rectangle([12, 38, 38, 44], radius=3, fill=(240, 210, 50, 255))
    # stem
    draw.rectangle([23, 28, 27, 34], fill=YELLOW)
    # cup bowl
    draw.chord([14, 20, 36, 34], 0, 180, fill=YELLOW)
    draw.ellipse([14, 18, 36, 26], fill=YELLOW)
    draw.ellipse([16, 19, 34, 25], fill=(240, 210, 50, 255))
    # egg sitting in cup
    draw.ellipse([18, 8, 32, 22], fill=WHITE)
    draw.ellipse([19, 9, 31, 21], fill=CREAM)

# ── 67. BUTTER DISH ──────────────────────────────
def draw_butter_dish(draw):
    # dish base
    draw.rounded_rectangle([6, 34, 44, 44], radius=4, fill=CREAM)
    draw.rounded_rectangle([8, 36, 42, 42], radius=3, fill=WHITE)
    # dome lid
    draw.chord([6, 18, 44, 36], 180, 360, fill=GLASS)
    draw.chord([8, 20, 42, 34], 180, 360, fill=WHITE)
    # butter block inside
    draw.rounded_rectangle([10, 28, 40, 36], radius=2, fill=YELLOW)
    draw.rounded_rectangle([12, 30, 38, 34], radius=1, fill=(245, 215, 60, 255))
    # lid knob
    draw.ellipse([22, 14, 28, 20], fill=CREAM)

# ── 68. BREAD BOX ────────────────────────────────
def draw_bread_box(draw):
    # main body
    draw.rounded_rectangle([4, 16, 46, 46], radius=4, fill=CREAM)
    draw.rounded_rectangle([6, 18, 44, 44], radius=3, fill=WHITE)
    # roll-top slats
    for y in [18, 21, 24, 27, 30]:
        draw.line([6, y, 44, y], fill=(210, 200, 180, 255), width=1)
    # front face
    draw.rectangle([6, 32, 44, 44], fill=TAN)
    draw.rounded_rectangle([8, 34, 42, 42], radius=2, fill=(200, 170, 120, 255))
    # handle
    draw.rounded_rectangle([20, 36, 30, 40], radius=3, fill=BROWN)
    # wood grain on front
    draw.line([10, 36, 10, 42], fill=BROWN, width=1)
    draw.line([20, 36, 20, 42], fill=BROWN, width=1)

# ── 69. SPICE RACK ───────────────────────────────
def draw_spice_rack(draw):
    # wooden frame
    draw.rounded_rectangle([4, 6, 46, 46], radius=3, fill=TAN)
    draw.rounded_rectangle([6, 8, 44, 44], radius=2, fill=BROWN)
    # two shelves
    draw.rectangle([6, 22, 44, 24], fill=TAN)
    draw.rectangle([6, 36, 44, 38], fill=TAN)
    # top row: 3 jars
    for x in [8, 19, 30]:
        draw.rounded_rectangle([x, 10, x+8, 22], radius=2, fill=GLASS)
        draw.rectangle([x+1, 10, x+7, 13], fill=STEEL)
    # bottom row: 3 jars
    for x in [8, 19, 30]:
        draw.rounded_rectangle([x, 26, x+8, 36], radius=2, fill=GLASS)
        draw.rectangle([x+1, 26, x+7, 29], fill=STEEL)

# ── 70. KITCHEN TOWEL ────────────────────────────
def draw_kitchen_towel(draw):
    # folded towel body
    draw.rounded_rectangle([8, 10, 42, 44], radius=4, fill=WHITE)
    draw.rounded_rectangle([10, 12, 40, 42], radius=3, fill=(240, 240, 245, 255))
    # stripe pattern
    for y in [16, 20, 34, 38]:
        draw.line([10, y, 40, y], fill=BLUE, width=2)
    # fold crease
    draw.line([10, 28, 40, 28], fill=(200, 200, 210, 255), width=1)
    # hanging loop at top
    draw.arc([20, 6, 30, 14], 180, 360, fill=WHITE, width=3)


# ── BUILD ALL ────────────────────────────────────
items = [
    ("wok",             draw_wok),
    ("waffle_iron",     draw_waffle_iron),
    ("ice_cream_scoop", draw_ice_cream_scoop),
    ("pizza_cutter",    draw_pizza_cutter),
    ("meat_tenderizer", draw_meat_tenderizer),
    ("kitchen_scale",   draw_kitchen_scale),
    ("slotted_spoon",   draw_slotted_spoon),
    ("pastry_brush",    draw_pastry_brush),
    ("melon_baller",    draw_melon_baller),
    ("zester",          draw_zester),
    ("mandoline_slicer",draw_mandoline_slicer),
    ("stockpot",        draw_stockpot),
    ("skillet",         draw_skillet),
    ("dutch_oven",      draw_dutch_oven),
    ("salad_spinner",   draw_salad_spinner),
    ("egg_cup",         draw_egg_cup),
    ("butter_dish",     draw_butter_dish),
    ("bread_box",       draw_bread_box),
    ("spice_rack",      draw_spice_rack),
    ("kitchen_towel",   draw_kitchen_towel),
]

print(f"Generating {len(items)} additional kitchen sprites in '{OUTPUT_DIR}/'...")
for name, func in items:
    create_sprite(name, func)
print(f"\nAll {len(items)} additional kitchen sprites generated successfully!")
