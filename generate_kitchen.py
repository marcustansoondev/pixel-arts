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

# Shared palette (<=10 colours used per sprite)
SILVER    = (180, 180, 190, 255)
STEEL     = (120, 125, 135, 255)
DARK      = ( 50,  50,  55, 255)
WHITE     = (245, 245, 245, 255)
CREAM     = (230, 220, 200, 255)
TAN       = (190, 160, 110, 255)
BROWN     = (130,  90,  50, 255)
RED       = (210,  50,  50, 255)
DKRED     = (160,  30,  30, 255)
ORANGE    = (230, 120,  30, 255)
YELLOW    = (230, 200,  40, 255)
GREEN     = ( 70, 160,  60, 255)
DKGREEN   = ( 30, 100,  30, 255)
BLUE      = ( 60, 110, 200, 255)
DKBLUE    = ( 30,  70, 160, 255)
BLACK     = ( 20,  20,  20, 255)
GLASS     = (180, 215, 240, 200)
HIGHLIGHT = (255, 255, 255, 180)
PINK      = (230, 130, 150, 255)
PURPLE    = (130,  70, 190, 255)


# ── 1. POT ──────────────────────────────────────
def draw_pot(draw):
    draw.rounded_rectangle([10,18,40,42], radius=4, fill=STEEL)
    draw.rounded_rectangle([12,20,38,40], radius=3, fill=SILVER)
    draw.rectangle([9,16,41,19], fill=DARK)
    draw.ellipse([10,10,40,19], fill=STEEL)
    draw.ellipse([13,11,37,18], fill=SILVER)
    draw.ellipse([21,7,29,12], fill=DARK)
    draw.ellipse([2,24,12,34], fill=DARK)
    draw.ellipse([4,26,10,32], fill=(0,0,0,0))
    draw.ellipse([38,24,48,34], fill=DARK)
    draw.ellipse([40,26,46,32], fill=(0,0,0,0))

# ── 2. PAN ──────────────────────────────────────
def draw_pan(draw):
    draw.ellipse([8,22,42,44], fill=DARK)
    draw.ellipse([10,24,40,42], fill=(60,60,65,255))
    draw.arc([12,25,25,38], 200, 320, fill=(90,90,95,255), width=2)
    draw.rounded_rectangle([38,30,50,36], radius=3, fill=BROWN)
    draw.line([42,33,49,33], fill=DARK, width=1)

# ── 3. KNIFE ─────────────────────────────────────
def draw_knife(draw):
    draw.polygon([(8,22),(42,18),(42,23),(8,30)], fill=SILVER)
    draw.polygon([(8,22),(42,18),(42,20),(8,24)], fill=WHITE)
    draw.rounded_rectangle([4,28,20,38], radius=3, fill=BROWN)
    draw.line([8,31,16,31], fill=DARK, width=1)
    draw.line([8,34,16,34], fill=DARK, width=1)
    draw.rectangle([18,26,22,40], fill=STEEL)

# ── 4. FORK ──────────────────────────────────────
def draw_fork(draw):
    draw.rounded_rectangle([22,34,28,48], radius=3, fill=SILVER)
    draw.rectangle([23,24,27,34], fill=SILVER)
    for x in [20,23,26,29]:
        draw.rectangle([x,8,x+2,24], fill=SILVER)
    draw.rectangle([20,22,31,25], fill=SILVER)

# ── 5. SPOON ─────────────────────────────────────
def draw_spoon(draw):
    draw.rounded_rectangle([22,30,28,48], radius=3, fill=SILVER)
    draw.rounded_rectangle([23,20,27,30], radius=2, fill=SILVER)
    draw.ellipse([17,8,33,22], fill=SILVER)
    draw.ellipse([18,9,32,20], fill=(200,205,215,255))

# ── 6. MUG ───────────────────────────────────────
def draw_mug(draw):
    draw.rounded_rectangle([10,16,36,44], radius=4, fill=RED)
    draw.rounded_rectangle([12,18,34,42], radius=3, fill=(225,65,65,255))
    draw.rectangle([10,14,36,17], fill=DKRED)
    draw.arc([32,22,46,38], 300, 60, fill=DKRED, width=5)
    draw.arc([14,6,20,14], 180, 0, fill=WHITE, width=2)
    draw.arc([22,6,28,14], 180, 0, fill=WHITE, width=2)

# ── 7. BOWL ──────────────────────────────────────
def draw_bowl(draw):
    draw.chord([6,18,44,48], 0, 180, fill=CREAM)
    draw.arc([6,18,44,48], 0, 180, fill=TAN, width=2)
    draw.ellipse([6,16,44,24], fill=CREAM)
    draw.ellipse([8,17,42,23], fill=WHITE)
    draw.chord([14,22,36,44], 0, 180, fill=(210,200,180,255))

# ── 8. PLATE ─────────────────────────────────────
def draw_plate(draw):
    draw.ellipse([4,14,46,42], fill=WHITE)
    draw.ellipse([6,16,44,40], fill=(250,250,252,255))
    draw.arc([4,14,46,42], 0, 360, fill=SILVER, width=2)
    draw.ellipse([12,20,38,36], fill=(240,240,242,255))
    draw.arc([12,20,38,36], 0, 360, fill=SILVER, width=1)

# ── 9. KETTLE ────────────────────────────────────
def draw_kettle(draw):
    draw.ellipse([10,18,40,44], fill=BLUE)
    draw.ellipse([12,20,38,42], fill=(80,130,220,255))
    draw.polygon([(38,26),(48,18),(49,22),(40,30)], fill=BLUE)
    draw.rectangle([16,14,34,19], fill=DKBLUE)
    draw.ellipse([21,10,29,16], fill=DARK)
    draw.arc([2,22,16,40], 300, 60, fill=DKBLUE, width=5)
    draw.arc([14,22,24,32], 200, 300, fill=HIGHLIGHT, width=2)

# ── 10. ROLLING PIN ──────────────────────────────
def draw_rolling_pin(draw):
    draw.rounded_rectangle([2,21,12,29], radius=3, fill=TAN)
    draw.rounded_rectangle([10,18,40,32], radius=5, fill=CREAM)
    draw.rounded_rectangle([11,19,39,31], radius=4, fill=WHITE)
    draw.line([12,28,38,28], fill=(200,190,170,255), width=2)
    draw.rounded_rectangle([38,21,48,29], radius=3, fill=TAN)

# ── 11. WHISK ────────────────────────────────────
def draw_whisk(draw):
    draw.rounded_rectangle([22,30,28,48], radius=3, fill=SILVER)
    draw.line([25,20,25,30], fill=SILVER, width=2)
    draw.arc([14,10,36,28], 30, 150, fill=SILVER, width=2)
    draw.arc([16,12,34,26], 30, 150, fill=STEEL, width=2)
    draw.arc([14,14,36,30], 210, 330, fill=SILVER, width=2)
    draw.line([14,22,25,20], fill=STEEL, width=1)
    draw.line([36,22,25,20], fill=STEEL, width=1)

# ── 12. CUTTING BOARD ────────────────────────────
def draw_cutting_board(draw):
    draw.rounded_rectangle([6,10,44,42], radius=4, fill=TAN)
    for y in [16,22,28,34]:
        draw.line([8,y,42,y], fill=BROWN, width=1)
    draw.rounded_rectangle([34,18,46,34], radius=4, fill=BROWN)
    draw.ellipse([37,24,43,30], fill=(0,0,0,0))

# ── 13. GRATER ───────────────────────────────────
def draw_grater(draw):
    draw.rounded_rectangle([14,8,36,44], radius=3, fill=SILVER)
    for row in range(3):
        for col in range(3):
            x = 18 + col*6
            y = 13 + row*9
            draw.ellipse([x,y,x+3,y+4], fill=DARK)
    draw.rounded_rectangle([20,4,30,10], radius=3, fill=STEEL)

# ── 14. OVEN MITT ────────────────────────────────
def draw_oven_mitt(draw):
    draw.ellipse([30,10,42,28], fill=RED)
    draw.rounded_rectangle([8,16,40,44], radius=8, fill=RED)
    draw.rectangle([8,38,28,46], fill=DKRED)
    draw.line([10,26,38,26], fill=(220,80,80,255), width=2)
    draw.line([10,32,38,32], fill=(220,80,80,255), width=2)

# ── 15. TIMER ────────────────────────────────────
def draw_timer(draw):
    draw.ellipse([8,12,42,46], fill=CREAM)
    draw.ellipse([10,14,40,44], fill=WHITE)
    draw.arc([8,12,42,46], 0, 360, fill=STEEL, width=2)
    for pt in [(25,14),(40,29),(25,44),(10,29)]:
        draw.ellipse([pt[0]-1,pt[1]-1,pt[0]+1,pt[1]+1], fill=DARK)
    draw.line([25,29,25,18], fill=DARK, width=2)
    draw.line([25,29,34,29], fill=RED, width=2)
    draw.ellipse([23,27,27,31], fill=DARK)
    draw.rectangle([21,8,29,13], fill=STEEL)
    draw.ellipse([22,5,28,10], fill=DARK)

# ── 16. SPATULA ──────────────────────────────────
def draw_spatula(draw):
    draw.rounded_rectangle([20,28,30,48], radius=4, fill=BROWN)
    draw.line([24,30,26,46], fill=TAN, width=2)
    draw.rectangle([23,20,27,28], fill=STEEL)
    draw.rounded_rectangle([14,8,36,22], radius=3, fill=SILVER)
    draw.line([16,12,34,12], fill=WHITE, width=1)
    draw.line([16,18,34,18], fill=STEEL, width=1)
    draw.rectangle([19,10,22,20], fill=(0,0,0,0))
    draw.rectangle([25,10,28,20], fill=(0,0,0,0))

# ── 17. COLANDER ─────────────────────────────────
def draw_colander(draw):
    draw.chord([6,20,44,50], 0, 180, fill=SILVER)
    draw.chord([8,22,42,48], 0, 180, fill=(195,195,205,255))
    draw.ellipse([6,18,44,26], fill=STEEL)
    draw.ellipse([8,19,42,25], fill=SILVER)
    for col in range(5):
        for row in range(3):
            x = 12+col*6; y = 26+row*6
            draw.ellipse([x,y,x+3,y+3], fill=DARK)
    draw.rectangle([2,20,8,24], fill=STEEL)
    draw.rectangle([42,20,48,24], fill=STEEL)

# ── 18. LADLE ────────────────────────────────────
def draw_ladle(draw):
    draw.rounded_rectangle([26,16,32,46], radius=3, fill=SILVER)
    draw.chord([8,26,30,46], 0, 180, fill=SILVER)
    draw.arc([8,26,30,46], 0, 180, fill=STEEL, width=2)
    draw.chord([10,28,28,44], 0, 180, fill=(200,205,215,255))

# ── 19. TOASTER ──────────────────────────────────
def draw_toaster(draw):
    draw.rounded_rectangle([6,22,44,44], radius=4, fill=STEEL)
    draw.rounded_rectangle([8,24,42,42], radius=3, fill=SILVER)
    draw.rounded_rectangle([10,20,20,28], radius=2, fill=DARK)
    draw.rounded_rectangle([22,20,32,28], radius=2, fill=DARK)
    draw.rounded_rectangle([11,12,19,22], radius=2, fill=YELLOW)
    draw.rounded_rectangle([23,10,31,22], radius=2, fill=ORANGE)
    draw.ellipse([36,30,42,36], fill=DARK)
    draw.ellipse([37,31,41,35], fill=STEEL)
    draw.rectangle([8,42,14,46], fill=DARK)
    draw.rectangle([36,42,42,46], fill=DARK)

# ── 20. BLENDER ──────────────────────────────────
def draw_blender(draw):
    draw.rounded_rectangle([12,36,38,46], radius=4, fill=DARK)
    draw.rounded_rectangle([14,38,36,44], radius=3, fill=(60,60,65,255))
    draw.polygon([(16,10),(14,36),(36,36),(34,10)], fill=GLASS)
    draw.polygon([(18,12),(16,34),(34,34),(32,12)], fill=HIGHLIGHT)
    draw.rounded_rectangle([16,6,34,12], radius=3, fill=DARK)
    draw.ellipse([22,4,28,10], fill=STEEL)
    draw.line([18,34,32,34], fill=SILVER, width=2)
    draw.ellipse([23,32,27,36], fill=STEEL)
    draw.ellipse([22,40,28,44], fill=RED)

# ── 21. POT LID ──────────────────────────────────
def draw_pot_lid(draw):
    draw.ellipse([6,20,44,36], fill=SILVER)
    draw.ellipse([8,21,42,34], fill=(200,205,215,255))
    draw.arc([8,21,42,34], 180, 360, fill=WHITE, width=1)
    draw.ellipse([20,12,30,22], fill=STEEL)
    draw.ellipse([22,13,28,21], fill=SILVER)

# ── 22. WOODEN SPOON ─────────────────────────────
def draw_wooden_spoon(draw):
    draw.rounded_rectangle([22,30,28,48], radius=3, fill=TAN)
    draw.rounded_rectangle([23,20,27,30], radius=2, fill=TAN)
    draw.ellipse([17,8,33,22], fill=TAN)
    draw.ellipse([19,10,31,20], fill=CREAM)
    draw.line([22,10,22,20], fill=BROWN, width=1)

# ── 23. CHEESE GRATER ────────────────────────────
def draw_cheese_grater(draw):
    # A box grater shape
    draw.polygon([(10,8),(40,8),(44,44),(6,44)], fill=YELLOW)
    draw.polygon([(12,10),(38,10),(42,42),(8,42)], fill=(240,210,60,255))
    for row in range(4):
        for col in range(3):
            x = 14 + col*8
            y = 14 + row*8
            draw.polygon([(x,y),(x+4,y),(x+2,y+5)], fill=ORANGE)
    # handle
    draw.rounded_rectangle([18,4,32,10], radius=3, fill=TAN)

# ── 24. TONGS ────────────────────────────────────
def draw_tongs(draw):
    # two arms crossing
    draw.line([12,8,32,42], fill=STEEL, width=4)
    draw.line([38,8,18,42], fill=STEEL, width=4)
    # pivot ring
    draw.ellipse([22,22,28,28], fill=DARK)
    # tips (wide end)
    draw.rounded_rectangle([8,38,18,44], radius=3, fill=SILVER)
    draw.rounded_rectangle([32,38,42,44], radius=3, fill=SILVER)
    # grip loop at top
    draw.arc([10,4,20,16], 0, 360, fill=STEEL, width=3)

# ── 25. MEASURING CUP ────────────────────────────
def draw_measuring_cup(draw):
    draw.polygon([(12,10),(38,10),(42,44),(8,44)], fill=GLASS)
    draw.polygon([(14,12),(36,12),(40,42),(10,42)], fill=HIGHLIGHT)
    # spout
    draw.polygon([(38,10),(46,8),(44,16),(38,16)], fill=GLASS)
    # handle
    draw.arc([38,20,48,38], 330, 30, fill=STEEL, width=4)
    # measure lines
    for y in [20,27,34]:
        draw.line([16,y,34,y], fill=SILVER, width=1)
    # rim
    draw.rectangle([12,8,38,12], fill=STEEL)

# ── 26. SALT SHAKER ──────────────────────────────
def draw_salt_shaker(draw):
    draw.rounded_rectangle([16,14,34,44], radius=6, fill=WHITE)
    draw.rounded_rectangle([18,12,32,16], radius=3, fill=SILVER)
    draw.ellipse([21,8,29,14], fill=STEEL)
    # holes
    for dx,dy in [(-3,-3),(0,-3),(3,-3),(-3,0),(3,0)]:
        draw.ellipse([24+dx,24+dy,26+dx,26+dy], fill=STEEL)
    # label line
    draw.line([18,34,32,34], fill=STEEL, width=1)
    draw.line([18,38,32,38], fill=STEEL, width=1)

# ── 27. PEPPER SHAKER ────────────────────────────
def draw_pepper_shaker(draw):
    draw.rounded_rectangle([16,14,34,44], radius=6, fill=DARK)
    draw.rounded_rectangle([18,12,32,16], radius=3, fill=STEEL)
    draw.ellipse([21,8,29,14], fill=SILVER)
    # holes
    for dx,dy in [(-3,-3),(0,-3),(3,-3),(-3,0),(3,0)]:
        draw.ellipse([24+dx,24+dy,26+dx,26+dy], fill=SILVER)

# ── 28. WINE GLASS ───────────────────────────────
def draw_wine_glass(draw):
    # bowl
    draw.chord([10,8,40,34], 0, 180, fill=GLASS)
    draw.chord([12,10,38,32], 0, 180, fill=HIGHLIGHT)
    # stem
    draw.rectangle([23,32,27,44], fill=GLASS)
    # base
    draw.rounded_rectangle([14,42,36,46], radius=3, fill=GLASS)
    # wine inside
    draw.chord([12,22,38,34], 0, 180, fill=(160,30,50,200))

# ── 29. GLASS / TUMBLER ──────────────────────────
def draw_glass(draw):
    draw.polygon([(14,10),(36,10),(40,44),(10,44)], fill=GLASS)
    draw.polygon([(16,12),(34,12),(38,42),(12,42)], fill=HIGHLIGHT)
    # ice cube
    draw.rectangle([18,30,28,40], fill=WHITE)
    draw.rectangle([26,24,34,32], fill=(220,235,245,255))
    # rim highlight
    draw.line([14,10,36,10], fill=WHITE, width=2)

# ── 30. CHEESE BLOCK ─────────────────────────────
def draw_cheese(draw):
    # main wedge
    draw.polygon([(6,16),(44,16),(44,42),(6,42)], fill=YELLOW)
    draw.polygon([(8,18),(42,18),(42,40),(8,40)], fill=(240,210,60,255))
    # holes
    draw.ellipse([14,22,22,30], fill=ORANGE)
    draw.ellipse([28,26,34,32], fill=ORANGE)
    draw.ellipse([20,30,26,36], fill=ORANGE)
    # wedge triangle cut top-right
    draw.polygon([(44,16),(44,4),(30,16)], fill=YELLOW)
    draw.polygon([(42,16),(42,6),(32,16)], fill=(240,210,60,255))

# ── 31. BREAD LOAF ───────────────────────────────
def draw_bread(draw):
    draw.rounded_rectangle([6,20,44,44], radius=6, fill=TAN)
    draw.ellipse([10,10,40,28], fill=(200,165,90,255))
    draw.line([8,36,42,36], fill=BROWN, width=1)
    draw.line([14,42,36,42], fill=BROWN, width=1)
    # scoring
    draw.line([14,24,36,24], fill=BROWN, width=1)

# ── 32. ROLLING DOUGH ────────────────────────────
def draw_dough(draw):
    # flat dough circle
    draw.ellipse([4,22,46,38], fill=CREAM)
    draw.ellipse([6,23,44,37], fill=WHITE)
    # flour dusting dots
    for px,py in [(14,26),(24,25),(34,27),(19,32),(29,31)]:
        draw.ellipse([px,py,px+2,py+2], fill=SILVER)

# ── 33. APRON ────────────────────────────────────
def draw_apron(draw):
    # bib
    draw.rounded_rectangle([14,6,36,22], radius=3, fill=BLUE)
    # straps
    draw.line([14,8,6,4], fill=DKBLUE, width=3)
    draw.line([36,8,44,4], fill=DKBLUE, width=3)
    # body
    draw.polygon([(8,22),(42,22),(46,48),(4,48)], fill=BLUE)
    draw.polygon([(10,24),(40,24),(44,46),(6,46)], fill=(80,130,220,255))
    # pocket
    draw.rounded_rectangle([16,32,34,44], radius=3, fill=DKBLUE)

# ── 34. SIEVE / STRAINER ─────────────────────────
def draw_strainer(draw):
    draw.chord([6,16,44,46], 0, 180, fill=SILVER)
    draw.chord([8,18,42,44], 0, 180, fill=(200,205,215,255))
    draw.ellipse([6,14,44,22], fill=STEEL)
    draw.ellipse([8,15,42,21], fill=SILVER)
    # mesh dots
    for col in range(6):
        for row in range(3):
            x = 10 + col*5; y = 24 + row*5
            draw.point((x,y), fill=DARK)
    # long handle
    draw.rounded_rectangle([38,16,50,22], radius=3, fill=TAN)

# ── 35. MORTAR AND PESTLE ────────────────────────
def draw_mortar_pestle(draw):
    # mortar bowl
    draw.chord([8,24,42,50], 0, 180, fill=DARK)
    draw.chord([10,26,40,48], 0, 180, fill=STEEL)
    draw.ellipse([8,22,42,30], fill=DARK)
    draw.ellipse([10,23,40,29], fill=STEEL)
    # pestle
    draw.rounded_rectangle([22,6,28,26], radius=3, fill=DARK)
    draw.ellipse([18,22,32,30], fill=STEEL)

# ── 36. GARLIC PRESS ─────────────────────────────
def draw_garlic_press(draw):
    # handles
    draw.rounded_rectangle([4,8,22,14], radius=3, fill=STEEL)
    draw.rounded_rectangle([4,36,22,42], radius=3, fill=STEEL)
    # hinge
    draw.ellipse([18,22,26,28], fill=DARK)
    # press head
    draw.rounded_rectangle([22,16,44,34], radius=4, fill=SILVER)
    # holes in head
    for dx,dy in [(-4,-3),(0,-3),(4,-3),(-4,3),(0,3),(4,3)]:
        draw.ellipse([33+dx,25+dy,35+dx,27+dy], fill=DARK)

# ── 37. BOTTLE OPENER ────────────────────────────
def draw_bottle_opener(draw):
    # body
    draw.rounded_rectangle([20,6,30,44], radius=4, fill=STEEL)
    draw.rounded_rectangle([21,7,29,43], radius=3, fill=SILVER)
    # hook at bottom
    draw.arc([16,36,30,48], 180, 360, fill=STEEL, width=5)
    draw.arc([18,38,28,46], 180, 360, fill=SILVER, width=3)
    # bottle cap key hole
    draw.ellipse([21,10,29,18], fill=DARK)
    draw.rectangle([23,16,27,22], fill=DARK)

# ── 38. CAN OPENER ───────────────────────────────
def draw_can_opener(draw):
    # handle 1
    draw.rounded_rectangle([4,8,20,14], radius=3, fill=RED)
    # handle 2
    draw.rounded_rectangle([4,36,20,42], radius=3, fill=RED)
    # body / gear joint
    draw.ellipse([16,20,28,32], fill=STEEL)
    draw.ellipse([18,22,26,30], fill=SILVER)
    # cutting wheel
    draw.ellipse([26,24,36,34], fill=DARK)
    draw.ellipse([27,25,35,33], fill=STEEL)
    # hinge arm
    draw.line([20,11,24,25], fill=DARK, width=3)
    draw.line([20,39,24,27], fill=DARK, width=3)

# ── 39. DISH / SPONGE ────────────────────────────
def draw_sponge(draw):
    draw.rounded_rectangle([6,16,44,38], radius=6, fill=YELLOW)
    draw.rounded_rectangle([8,18,42,36], radius=5, fill=(245,215,60,255))
    # pore holes
    for px,py in [(14,22),(22,20),(30,22),(38,22),(18,30),(26,28),(34,30),(20,24),(32,26)]:
        draw.ellipse([px,py,px+3,py+3], fill=ORANGE)
    # soap suds
    for bx,by in [(10,12),(18,10),(26,12),(34,10),(40,13)]:
        draw.ellipse([bx,by,bx+5,by+5], fill=WHITE)

# ── 40. DISH RACK ────────────────────────────────
def draw_dish_rack(draw):
    # base tray
    draw.rounded_rectangle([4,40,46,48], radius=3, fill=STEEL)
    # vertical dividers
    for x in range(8, 46, 6):
        draw.line([x,14,x,40], fill=SILVER, width=2)
    # horizontal rails
    draw.line([6,14,44,14], fill=DARK, width=2)
    draw.line([6,26,44,26], fill=DARK, width=2)
    # plates in rack (zigzag)
    for x in [11,17,23,29,35,41]:
        draw.arc([x-3,16,x+3,36], 200, 340, fill=WHITE, width=2)

# ── 41. COOKBOOK ─────────────────────────────────
def draw_cookbook(draw):
    # cover
    draw.rounded_rectangle([6,6,44,46], radius=4, fill=RED)
    draw.rounded_rectangle([8,8,42,44], radius=3, fill=DKRED)
    # spine
    draw.rectangle([6,6,12,46], fill=DKRED)
    # title lines
    draw.line([14,16,40,16], fill=WHITE, width=2)
    draw.line([14,22,34,22], fill=(220,80,80,255), width=1)
    # chef hat icon
    draw.ellipse([20,26,30,34], fill=WHITE)
    draw.line([20,32,30,32], fill=WHITE, width=3)

# ── 42. SUGAR JAR ────────────────────────────────
def draw_sugar_jar(draw):
    draw.rounded_rectangle([12,14,38,44], radius=5, fill=GLASS)
    draw.rounded_rectangle([14,16,36,42], radius=4, fill=HIGHLIGHT)
    # lid
    draw.rounded_rectangle([14,10,36,16], radius=3, fill=STEEL)
    draw.ellipse([21,6,29,12], fill=DARK)
    # sugar label
    draw.line([16,26,34,26], fill=STEEL, width=1)
    draw.line([16,30,34,30], fill=STEEL, width=1)
    # sugar crystals
    for px,py in [(18,34),(24,33),(30,34),(22,38),(28,37)]:
        draw.ellipse([px,py,px+3,py+3], fill=WHITE)

# ── 43. COFFEE POT ───────────────────────────────
def draw_coffee_pot(draw):
    # body
    draw.rounded_rectangle([12,14,38,44], radius=5, fill=DARK)
    draw.rounded_rectangle([14,16,36,42], radius=4, fill=(60,60,65,255))
    # spout
    draw.polygon([(38,20),(48,14),(48,20),(40,24)], fill=DARK)
    # handle
    draw.arc([2,20,16,40], 300, 60, fill=DARK, width=5)
    # lid
    draw.rounded_rectangle([18,10,32,16], radius=3, fill=STEEL)
    draw.ellipse([22,6,28,12], fill=DARK)
    # steam
    draw.arc([18,2,24,10], 180, 0, fill=SILVER, width=2)
    draw.arc([26,2,32,10], 180, 0, fill=SILVER, width=2)

# ── 44. PEELER ───────────────────────────────────
def draw_peeler(draw):
    # handle
    draw.rounded_rectangle([18,28,32,48], radius=5, fill=GREEN)
    draw.line([22,30,28,46], fill=DKGREEN, width=2)
    # neck
    draw.rectangle([23,20,27,28], fill=STEEL)
    # blade (Y-shaped slot)
    draw.rounded_rectangle([14,10,36,22], radius=3, fill=SILVER)
    draw.rectangle([20,10,30,22], fill=(0,0,0,0))  # slot cutout
    draw.line([16,16,20,16], fill=STEEL, width=2)
    draw.line([30,16,34,16], fill=STEEL, width=2)

# ── 45. MIXING BOWL ──────────────────────────────
def draw_mixing_bowl(draw):
    draw.chord([4,16,46,50], 0, 180, fill=(80,120,200,255))
    draw.chord([6,18,44,48], 0, 180, fill=(100,140,220,255))
    draw.ellipse([4,14,46,24], fill=(80,120,200,255))
    draw.ellipse([6,15,44,23], fill=(110,150,230,255))
    # batter swirl
    draw.arc([14,22,36,42], 30, 300, fill=CREAM, width=3)
    # spout
    draw.polygon([(42,16),(48,12),(48,18),(42,20)], fill=(80,120,200,255))

# ── 46. BREAD KNIFE ──────────────────────────────
def draw_bread_knife(draw):
    # serrated blade
    draw.polygon([(6,20),(42,16),(42,22),(6,28)], fill=SILVER)
    # serration teeth
    for x in range(10, 42, 5):
        draw.polygon([(x,22),(x+2,26),(x+4,22)], fill=WHITE)
    # handle
    draw.rounded_rectangle([2,26,18,36], radius=3, fill=BROWN)
    draw.line([4,29,16,29], fill=TAN, width=1)
    draw.line([4,33,16,33], fill=TAN, width=1)
    # guard
    draw.rectangle([16,24,20,38], fill=STEEL)

# ── 47. POT HOLDER / TRIVET ──────────────────────
def draw_trivet(draw):
    # hexagonal trivet shape
    draw.polygon([(25,6),(40,14),(40,30),(25,38),(10,30),(10,14)], fill=BROWN)
    draw.polygon([(25,9),(37,16),(37,28),(25,35),(13,28),(13,16)], fill=TAN)
    # inner lattice
    draw.line([25,9,25,35], fill=BROWN, width=2)
    draw.line([13,16,37,28], fill=BROWN, width=2)
    draw.line([37,16,13,28], fill=BROWN, width=2)
    # legs
    for px in [14,25,36]:
        draw.rectangle([px,36,px+3,42], fill=DARK)

# ── 48. COLANDER LID / PLATE COVER ───────────────
def draw_plate_cover(draw):
    # dome
    draw.chord([6,10,44,42], 180, 360, fill=SILVER)
    draw.chord([8,12,42,40], 180, 360, fill=(200,205,215,255))
    # shine arc on dome
    draw.arc([10,13,28,28], 200, 320, fill=WHITE, width=2)
    # knob
    draw.ellipse([21,36,29,44], fill=STEEL)
    draw.ellipse([23,38,27,42], fill=SILVER)
    # rim shadow
    draw.line([6,10,44,10], fill=DARK, width=2)

# ── 49. JUICER ───────────────────────────────────
def draw_juicer(draw):
    # base
    draw.rounded_rectangle([10,36,40,46], radius=4, fill=STEEL)
    draw.rounded_rectangle([12,38,38,44], radius=3, fill=SILVER)
    # cup
    draw.polygon([(14,14),(36,14),(38,36),(12,36)], fill=GLASS)
    draw.polygon([(15,15),(35,15),(37,35),(13,35)], fill=HIGHLIGHT)
    # juicer cone
    draw.polygon([(18,10),(32,10),(26,20)], fill=YELLOW)
    draw.polygon([(19,11),(31,11),(26,19)], fill=ORANGE)
    # spout
    draw.rectangle([36,30,42,34], fill=STEEL)
    # juice level
    draw.rectangle([15,28,35,34], fill=ORANGE)

# ── 50. CHOPSTICKS ───────────────────────────────
def draw_chopsticks(draw):
    # two chopsticks slightly angled
    draw.polygon([(16,4),(19,4),(28,46),(25,46)], fill=TAN)
    draw.polygon([(17,5),(18,5),(27,45),(26,45)], fill=CREAM)
    draw.polygon([(31,4),(34,4),(25,46),(22,46)], fill=TAN)
    draw.polygon([(32,5),(33,5),(24,45),(23,45)], fill=CREAM)
    # decorative band near top
    draw.rectangle([15,12,20,15], fill=RED)
    draw.rectangle([30,12,35,15], fill=RED)


# ── BUILD ALL ────────────────────────────────────
items = [
    ("pot",           draw_pot),
    ("pan",           draw_pan),
    ("knife",         draw_knife),
    ("fork",          draw_fork),
    ("spoon",         draw_spoon),
    ("mug",           draw_mug),
    ("bowl",          draw_bowl),
    ("plate",         draw_plate),
    ("kettle",        draw_kettle),
    ("rolling_pin",   draw_rolling_pin),
    ("whisk",         draw_whisk),
    ("cutting_board", draw_cutting_board),
    ("grater",        draw_grater),
    ("oven_mitt",     draw_oven_mitt),
    ("timer",         draw_timer),
    ("spatula",       draw_spatula),
    ("colander",      draw_colander),
    ("ladle",         draw_ladle),
    ("toaster",       draw_toaster),
    ("blender",       draw_blender),
    ("pot_lid",       draw_pot_lid),
    ("wooden_spoon",  draw_wooden_spoon),
    ("cheese_grater", draw_cheese_grater),
    ("tongs",         draw_tongs),
    ("measuring_cup", draw_measuring_cup),
    ("salt_shaker",   draw_salt_shaker),
    ("pepper_shaker", draw_pepper_shaker),
    ("wine_glass",    draw_wine_glass),
    ("glass",         draw_glass),
    ("cheese",        draw_cheese),
    ("bread",         draw_bread),
    ("dough",         draw_dough),
    ("apron",         draw_apron),
    ("strainer",      draw_strainer),
    ("mortar_pestle", draw_mortar_pestle),
    ("garlic_press",  draw_garlic_press),
    ("bottle_opener", draw_bottle_opener),
    ("can_opener",    draw_can_opener),
    ("sponge",        draw_sponge),
    ("dish_rack",     draw_dish_rack),
    ("cookbook",      draw_cookbook),
    ("sugar_jar",     draw_sugar_jar),
    ("coffee_pot",    draw_coffee_pot),
    ("peeler",        draw_peeler),
    ("mixing_bowl",   draw_mixing_bowl),
    ("bread_knife",   draw_bread_knife),
    ("trivet",        draw_trivet),
    ("plate_cover",   draw_plate_cover),
    ("juicer",        draw_juicer),
    ("chopsticks",    draw_chopsticks),
]

print(f"Generating {len(items)} kitchen sprites in '{OUTPUT_DIR}/'...")
for name, func in items:
    create_sprite(name, func)
print(f"\nAll {len(items)} kitchen sprites generated successfully!")
