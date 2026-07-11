import os
from PIL import Image, ImageDraw

OUTPUT_DIR = "images/clothing"
os.makedirs(OUTPUT_DIR, exist_ok=True)

def create_sprite(name, draw_func):
    base_img = Image.new("RGBA", (50, 50), (255, 255, 255, 0))
    draw = ImageDraw.Draw(base_img)
    draw_func(draw)
    
    # --- Add realistic 3D detail (pixel drop shadow and glossy reflection) ---
    r, g, b, a = base_img.split()
    shadow_mask = a.point(lambda p: 255 if p > 128 else 0)
    
    combined = Image.new("RGBA", (50, 50), (255, 255, 255, 0))
    # 1. Drop Shadow (offset by 2,2)
    shadow_color = Image.new("RGBA", (50, 50), (30, 30, 35, 255))
    combined.paste(shadow_color, (2, 2), mask=shadow_mask)
    
    # 2. Base Image
    combined = Image.alpha_composite(combined, base_img)
    
    # 3. Glossy Reflection Glare
    gloss = Image.new("RGBA", (50, 50), (0, 0, 0, 0))
    gloss_draw = ImageDraw.Draw(gloss)
    gloss_draw.polygon([(0, 0), (35, 0), (0, 35)], fill=(255, 255, 255, 45))
    gloss_draw.polygon([(50, 25), (50, 50), (25, 50)], fill=(0, 0, 0, 45))
    gloss_masked = Image.new("RGBA", (50, 50), (0, 0, 0, 0))
    gloss_masked.paste(gloss, (0, 0), mask=shadow_mask)
    combined = Image.alpha_composite(combined, gloss_masked)
    
    # --- Quantize to strictly <= 9 colors ---
    flat = Image.new("RGB", (50, 50), (255, 255, 255))
    comb_a = combined.split()[3].point(lambda p: 255 if p > 128 else 0)
    flat.paste(combined, mask=comb_a)
    
    q = flat.quantize(colors=8, method=Image.MEDIANCUT)
    final = q.convert("RGBA")
    
    # Force all transparent pixels to a single identical RGBA value
    data = final.getdata()
    alpha_data = comb_a.getdata()
    new_data = []
    for i in range(len(data)):
        if alpha_data[i] == 0:
            new_data.append((0, 0, 0, 0))
        else:
            new_data.append((data[i][0], data[i][1], data[i][2], 255))
    final.putdata(new_data)
    
    path = os.path.join(OUTPUT_DIR, f"{name}_50x50.png")
    final.save(path)
    print(f"  Saved: {path}")

# Color constants
RED       = (210, 45, 45, 255)
DKRED     = (130, 20, 20, 255)
BLUE      = (50, 110, 210, 255)
DKBLUE    = (20, 50, 140, 255)
YELLOW    = (240, 200, 30, 255)
GREEN     = (50, 160, 60, 255)
DKGREEN   = (20, 90, 20, 255)
WHITE     = (245, 245, 245, 255)
BLACK     = (25, 25, 25, 255)
GREY      = (160, 160, 165, 255)
DKGREY    = (80, 80, 85, 255)
ORANGE    = (235, 110, 25, 255)
BROWN     = (130, 85, 45, 255)
PURPLE    = (130, 60, 180, 255)
LIGHTBLUE = (170, 220, 250, 255)
STEEL     = (120, 125, 135, 255)
SILVER    = (180, 180, 190, 255)
GOLD      = (212, 175, 55, 255)
PINK      = (240, 130, 180, 255)
DKPINK    = (180, 80, 120, 255)
BEIGE     = (225, 200, 170, 255)
DKBROWN   = (80, 50, 25, 255)
KHAKI     = (195, 176, 145, 255)
TEAL      = (30, 140, 150, 255)
DKCYAN    = (0, 130, 130, 255)

# --- 1. T-Shirt ---
def draw_tshirt(draw):
    draw.rectangle([14, 15, 36, 42], fill=RED)
    draw.rectangle([10, 15, 14, 25], fill=RED)
    draw.rectangle([36, 15, 40, 25], fill=RED)
    # White V-neck collar & stripes
    draw.polygon([(22, 15), (28, 15), (25, 18)], fill=WHITE)
    draw.rectangle([10, 24, 14, 25], fill=WHITE)
    draw.rectangle([36, 24, 40, 25], fill=WHITE)
    draw.rectangle([14, 41, 36, 42], fill=WHITE)

# --- 2. Denim Jeans ---
def draw_jeans(draw):
    draw.rectangle([15, 12, 35, 44], fill=BLUE)
    draw.rectangle([24, 22, 26, 44], fill=0) # crotch gap
    # Belts & pockets
    draw.rectangle([15, 12, 35, 15], fill=DKBLUE)
    draw.rectangle([18, 16, 21, 20], fill=DKBLUE)
    draw.rectangle([29, 16, 32, 20], fill=DKBLUE)
    draw.ellipse([24, 13, 26, 15], fill=GOLD) # button

# --- 3. Hoodie ---
def draw_hoodie(draw):
    draw.rectangle([14, 16, 36, 44], fill=DKGREY)
    draw.rectangle([9, 18, 14, 38], fill=DKGREY)
    draw.rectangle([36, 18, 41, 38], fill=DKGREY)
    # Hood & pocket
    draw.rounded_rectangle([18, 8, 32, 17], radius=3, fill=DKGREY)
    draw.rectangle([19, 32, 31, 38], fill=GREY) # front pocket
    # strings
    draw.line([22, 16, 22, 22], fill=WHITE, width=1)
    draw.line([28, 16, 28, 22], fill=WHITE, width=1)

# --- 4. Sneakers ---
def draw_sneakers(draw):
    # Left shoe
    draw.rounded_rectangle([8, 26, 24, 38], radius=2, fill=RED)
    draw.rectangle([8, 36, 24, 38], fill=WHITE) # sole
    draw.polygon([(18, 26), (24, 26), (24, 35)], fill=WHITE) # tongue / front
    draw.line([14, 28, 18, 28], fill=BLACK) # laces
    
    # Right shoe
    draw.rounded_rectangle([26, 26, 42, 38], radius=2, fill=RED)
    draw.rectangle([26, 36, 42, 38], fill=WHITE) # sole
    draw.polygon([(36, 26), (42, 26), (42, 35)], fill=WHITE)
    draw.line([32, 28, 36, 28], fill=BLACK)

# --- 5. Baseball Cap ---
def draw_cap(draw):
    draw.ellipse([14, 15, 36, 35], fill=DKBLUE)
    draw.rectangle([14, 28, 42, 33], fill=DKBLUE) # visor
    draw.ellipse([23, 14, 27, 16], fill=GOLD) # top button
    draw.rectangle([23, 22, 27, 26], fill=WHITE) # front logo

# --- 6. Leather Jacket ---
def draw_leather_jacket(draw):
    draw.rectangle([14, 14, 36, 43], fill=BLACK)
    draw.rectangle([9, 16, 14, 39], fill=BLACK)
    draw.rectangle([36, 16, 41, 39], fill=BLACK)
    # Metal zippers & collars
    draw.line([25, 14, 25, 43], fill=SILVER, width=1)
    draw.polygon([(14, 14), (20, 14), (16, 20)], fill=DKGREY)
    draw.polygon([(36, 14), (30, 14), (34, 20)], fill=DKGREY)

# --- 7. Trench Coat ---
def draw_trench_coat(draw):
    draw.rectangle([13, 12, 37, 46], fill=KHAKI)
    draw.rectangle([8, 14, 13, 38], fill=KHAKI)
    draw.rectangle([37, 14, 42, 38], fill=KHAKI)
    # belt & buttons
    draw.rectangle([13, 26, 37, 28], fill=DKBROWN)
    draw.rectangle([23, 25, 27, 29], fill=GOLD) # buckle
    for y in [18, 22, 32, 36]:
        draw.ellipse([17, y, 19, y+2], fill=DKBROWN)
        draw.ellipse([31, y, 33, y+2], fill=DKBROWN)

# --- 8. Suit Jacket ---
def draw_suit_jacket(draw):
    draw.rectangle([13, 13, 37, 44], fill=DKBLUE)
    draw.rectangle([8, 15, 13, 40], fill=DKBLUE)
    draw.rectangle([37, 15, 42, 40], fill=DKBLUE)
    # shirt & tie
    draw.polygon([(21, 13), (29, 13), (25, 23)], fill=WHITE)
    draw.polygon([(24, 17), (26, 17), (25, 25)], fill=RED)
    draw.ellipse([21, 30, 23, 32], fill=GOLD) # button
    draw.ellipse([21, 36, 23, 38], fill=GOLD)

# --- 9. Dress Pants ---
def draw_dress_pants(draw):
    draw.rectangle([16, 11, 34, 44], fill=DKGREY)
    draw.rectangle([24, 20, 26, 44], fill=0) # crease gap
    draw.rectangle([16, 11, 34, 14], fill=BLACK) # belt
    draw.rectangle([23, 11, 27, 14], fill=SILVER) # buckle

# --- 10. Sunglasses ---
def draw_sunglasses(draw):
    draw.rounded_rectangle([10, 18, 24, 28], radius=2, fill=BLACK)
    draw.rounded_rectangle([26, 18, 40, 28], radius=2, fill=BLACK)
    draw.line([22, 20, 28, 20], fill=BLACK, width=2) # bridge
    draw.line([10, 20, 6, 24], fill=BLACK, width=1) # temples
    draw.line([40, 20, 44, 24], fill=BLACK, width=1)
    # reflections
    draw.line([13, 21, 19, 27], fill=LIGHTBLUE, width=1)
    draw.line([29, 21, 35, 27], fill=LIGHTBLUE, width=1)

# --- 11. Winter Beanie ---
def draw_winter_beanie(draw):
    draw.ellipse([14, 13, 36, 38], fill=TEAL)
    draw.rectangle([12, 30, 38, 38], fill=DKBLUE) # folded brim
    draw.ellipse([22, 7, 28, 13], fill=WHITE) # pompom

# --- 12. Wool Scarf ---
def draw_scarf(draw):
    # Main wrap
    draw.rounded_rectangle([14, 15, 36, 25], radius=2, fill=RED)
    # hanging tails
    draw.rectangle([16, 25, 22, 42], fill=RED)
    draw.rectangle([26, 25, 31, 38], fill=RED)
    # stripes
    for y in [18, 22]:
        draw.line([14, y, 36, y], fill=YELLOW, width=1)
    for y in [28, 34, 40]:
        draw.line([16, y, 22, y], fill=YELLOW, width=1)

# --- 13. Mittens ---
def draw_mittens(draw):
    # Left mitten
    draw.rounded_rectangle([12, 18, 22, 34], radius=3, fill=PINK)
    draw.rounded_rectangle([20, 24, 24, 30], radius=1, fill=PINK) # thumb
    draw.rectangle([12, 32, 22, 35], fill=WHITE) # cuff
    
    # Right mitten
    draw.rounded_rectangle([28, 18, 38, 34], radius=3, fill=PINK)
    draw.rounded_rectangle([26, 24, 30, 30], radius=1, fill=PINK) # thumb
    draw.rectangle([28, 32, 38, 35], fill=WHITE) # cuff
    
    # string
    draw.arc([16, 32, 34, 44], 0, 180, fill=WHITE, width=1)

# --- 14. Crew Socks ---
def draw_socks(draw):
    # Left sock
    draw.rectangle([13, 15, 20, 34], fill=WHITE)
    draw.rectangle([13, 31, 25, 36], fill=WHITE) # foot
    draw.rectangle([13, 15, 20, 17], fill=RED) # stripes
    draw.rectangle([13, 19, 20, 21], fill=BLUE)
    
    # Right sock
    draw.rectangle([28, 15, 35, 34], fill=WHITE)
    draw.rectangle([28, 31, 40, 36], fill=WHITE) # foot
    draw.rectangle([28, 15, 35, 17], fill=RED) # stripes
    draw.rectangle([28, 19, 35, 21], fill=BLUE)

# --- 15. High Heels ---
def draw_high_heels(draw):
    draw.polygon([(12, 34), (38, 34), (34, 18), (30, 18)], fill=RED)
    draw.rectangle([34, 18, 38, 44], fill=BLACK) # heel spike
    draw.polygon([(12, 34), (22, 42), (38, 42)], fill=RED) # sole/platform
    # buckle / straps
    draw.ellipse([30, 20, 34, 24], fill=GOLD)

# --- 16. Leather Boots ---
def draw_boots(draw):
    # Left boot
    draw.rectangle([11, 18, 21, 38], fill=BROWN)
    draw.rectangle([11, 34, 26, 42], fill=BROWN)
    draw.rectangle([10, 40, 26, 42], fill=BLACK) # sole
    draw.line([16, 22, 16, 32], fill=YELLOW, width=1) # laces
    
    # Right boot
    draw.rectangle([28, 18, 38, 38], fill=BROWN)
    draw.rectangle([28, 34, 43, 42], fill=BROWN)
    draw.rectangle([27, 40, 43, 42], fill=BLACK) # sole
    draw.line([33, 22, 33, 32], fill=YELLOW, width=1)

# --- 17. Sandals ---
def draw_sandals(draw):
    # Left sandal
    draw.rectangle([12, 38, 22, 42], fill=BROWN) # sole
    draw.line([14, 30, 14, 38], fill=ORANGE, width=2) # straps
    draw.line([20, 30, 20, 38], fill=ORANGE, width=2)
    draw.line([12, 33, 22, 33], fill=ORANGE, width=2)
    
    # Right sandal
    draw.rectangle([28, 38, 38, 42], fill=BROWN) # sole
    draw.line([30, 30, 30, 38], fill=ORANGE, width=2)
    draw.line([36, 30, 36, 38], fill=ORANGE, width=2)
    draw.line([28, 33, 38, 33], fill=ORANGE, width=2)

# --- 18. Swimsuit ---
def draw_swimsuit(draw):
    draw.rectangle([16, 16, 34, 42], fill=TEAL)
    # cutouts
    draw.polygon([(16, 16), (22, 16), (16, 26)], fill=0)
    draw.polygon([(34, 16), (28, 16), (34, 26)], fill=0)
    draw.polygon([(16, 34), (25, 42), (16, 42)], fill=0)
    draw.polygon([(34, 34), (25, 42), (34, 42)], fill=0)
    # stripes
    draw.line([16, 26, 34, 26], fill=WHITE, width=2)

# --- 19. Bathrobe ---
def draw_bathrobe(draw):
    draw.rectangle([14, 12, 36, 46], fill=WHITE)
    draw.rectangle([8, 15, 14, 38], fill=WHITE)
    draw.rectangle([36, 15, 42, 38], fill=WHITE)
    # collar trim & belt
    draw.polygon([(20, 12), (30, 12), (25, 24)], fill=LIGHTBLUE)
    draw.rectangle([12, 28, 38, 31], fill=LIGHTBLUE) # belt
    draw.rectangle([22, 27, 28, 34], fill=LIGHTBLUE) # knot

# --- 20. Necktie ---
def draw_tie(draw):
    draw.polygon([(22, 10), (28, 10), (26, 14), (24, 14)], fill=RED) # knot
    draw.polygon([(23, 14), (27, 14), (29, 42), (25, 46), (21, 42)], fill=RED) # body
    # diagonal stripes
    for y in range(18, 42, 6):
        draw.line([22, y, 28, y-3], fill=YELLOW, width=1)

# --- 21. Bowtie ---
def draw_bowtie(draw):
    draw.polygon([(15, 18), (25, 23), (15, 28)], fill=BLACK)
    draw.polygon([(35, 18), (25, 23), (35, 28)], fill=BLACK)
    draw.ellipse([23, 20, 27, 26], fill=DKGREY) # center knot

# --- 22. Leather Belt ---
def draw_belt(draw):
    draw.rectangle([8, 22, 42, 26], fill=DKBROWN)
    draw.rectangle([21, 20, 29, 28], fill=GOLD, outline=BLACK, width=1) # buckle
    draw.rectangle([24, 23, 26, 25], fill=DKBROWN) # prong hole

# --- 23. Pleated Skirt ---
def draw_skirt(draw):
    draw.polygon([(18, 18), (32, 18), (40, 42), (10, 42)], fill=BLUE)
    # Pleats shading
    for x in range(14, 38, 4):
        draw.line([x, 18, x*1.1 - 2, 42], fill=DKBLUE, width=1)

# --- 24. Evening Dress ---
def draw_dress(draw):
    draw.polygon([(18, 14), (32, 14), (28, 24), (22, 24)], fill=PINK) # bodice
    draw.polygon([(22, 24), (28, 24), (42, 46), (8, 46)], fill=PINK) # skirt
    # sparkles
    draw.ellipse([20, 18, 21, 19], fill=WHITE)
    draw.ellipse([30, 28, 31, 29], fill=WHITE)
    draw.ellipse([15, 40, 16, 41], fill=WHITE)

# --- 25. Knit Sweater ---
def draw_sweater(draw):
    draw.rectangle([13, 14, 37, 43], fill=GREEN)
    draw.rectangle([8, 16, 13, 38], fill=GREEN)
    draw.rectangle([37, 16, 42, 38], fill=GREEN)
    # patterns
    draw.line([13, 24, 37, 24], fill=YELLOW, width=1)
    draw.line([13, 28, 37, 28], fill=YELLOW, width=1)
    for x in range(15, 36, 5):
        draw.line([x, 24, x+2, 28], fill=RED, width=1)

# --- 26. Cargo Shorts ---
def draw_cargo_shorts(draw):
    draw.rectangle([14, 15, 36, 38], fill=KHAKI)
    draw.rectangle([24, 24, 26, 38], fill=0) # crotch gap
    # Side pockets
    draw.rectangle([11, 22, 14, 30], fill=DKBROWN)
    draw.rectangle([36, 22, 39, 30], fill=DKBROWN)

# --- 27. Raincoat ---
def draw_raincoat(draw):
    draw.rectangle([13, 13, 37, 45], fill=YELLOW)
    draw.rectangle([8, 16, 13, 39], fill=YELLOW)
    draw.rectangle([37, 16, 42, 39], fill=YELLOW)
    # hood and pockets
    draw.rounded_rectangle([17, 6, 33, 14], radius=3, fill=YELLOW)
    draw.rectangle([15, 32, 21, 37], fill=ORANGE)
    draw.rectangle([29, 32, 35, 37], fill=ORANGE)

# --- 28. Striped Pajamas ---
def draw_pajamas(draw):
    # shirt
    draw.rectangle([14, 12, 36, 27], fill=LIGHTBLUE)
    # pants
    draw.rectangle([15, 29, 35, 45], fill=LIGHTBLUE)
    draw.rectangle([24, 34, 26, 45], fill=0)
    # stripes
    for x in [18, 22, 28, 32]:
        draw.line([x, 12, x, 27], fill=WHITE)
        draw.line([x, 29, x, 45], fill=WHITE)

# --- 29. Apron ---
def draw_apron(draw):
    draw.rectangle([16, 18, 34, 42], fill=GREY)
    draw.rectangle([19, 12, 31, 18], fill=GREY) # bib
    # straps
    draw.arc([19, 9, 31, 15], 180, 360, fill=BLACK) # neck strap
    draw.line([16, 24, 11, 24], fill=BLACK) # waist ties
    draw.line([34, 24, 39, 24], fill=BLACK)
    draw.rectangle([20, 28, 30, 35], fill=DKGREY) # front pocket

# --- 30. Leather Gloves ---
def draw_gloves(draw):
    # Left glove
    draw.rounded_rectangle([11, 16, 22, 35], radius=2, fill=DKBROWN)
    draw.rectangle([12, 16, 14, 24], fill=0) # finger slits
    draw.rectangle([16, 16, 18, 24], fill=0)
    draw.rectangle([11, 32, 22, 35], fill=BLACK) # cuff
    
    # Right glove
    draw.rounded_rectangle([28, 16, 39, 35], radius=2, fill=DKBROWN)
    draw.rectangle([29, 16, 31, 24], fill=0)
    draw.rectangle([33, 16, 35, 24], fill=0)
    draw.rectangle([28, 32, 39, 35], fill=BLACK)

# --- 31. Fedora Hat ---
def draw_fedora(draw):
    draw.ellipse([14, 18, 36, 32], fill=DKGREY)
    draw.ellipse([10, 26, 40, 34], fill=DKGREY) # brim
    draw.rectangle([15, 25, 35, 28], fill=BLACK) # hat band

# --- 32. Straw Hat ---
def draw_straw_hat(draw):
    draw.ellipse([14, 18, 36, 32], fill=BEIGE)
    draw.ellipse([8, 26, 42, 36], fill=BEIGE) # wide brim
    draw.rectangle([14, 26, 36, 29], fill=RED) # red ribbon

# --- 33. Denim Overalls ---
def draw_overalls(draw):
    # pants section
    draw.rectangle([15, 22, 35, 45], fill=BLUE)
    draw.rectangle([24, 30, 26, 45], fill=0)
    # bib section
    draw.rectangle([17, 14, 33, 22], fill=BLUE)
    # straps
    draw.line([17, 14, 17, 8], fill=DKBLUE, width=2)
    draw.line([33, 14, 33, 8], fill=DKBLUE, width=2)
    draw.ellipse([16, 14, 19, 17], fill=GOLD) # buckles
    draw.ellipse([31, 14, 34, 17], fill=GOLD)

# --- 34. Sporty Windbreaker ---
def draw_windbreaker(draw):
    draw.rectangle([13, 15, 37, 43], fill=PURPLE)
    draw.rectangle([8, 17, 13, 38], fill=TEAL) # sleeves contrast
    draw.rectangle([37, 17, 42, 38], fill=TEAL)
    # diagonal chest panel
    draw.polygon([(13, 15), (37, 15), (25, 26)], fill=WHITE)
    draw.line([25, 15, 25, 43], fill=BLACK) # zipper

# --- 35. Tracksuit Pants ---
def draw_tracksuit(draw):
    draw.rectangle([16, 12, 34, 45], fill=BLACK)
    draw.rectangle([24, 22, 26, 45], fill=0)
    # side stripes
    draw.line([16, 12, 16, 45], fill=WHITE, width=1)
    draw.line([34, 12, 34, 45], fill=WHITE, width=1)

# --- 36. Swim Trunks ---
def draw_swim_trunks(draw):
    draw.rectangle([14, 16, 36, 36], fill=RED)
    draw.rectangle([24, 26, 26, 36], fill=0)
    # drawstrings
    draw.line([23, 18, 21, 24], fill=WHITE, width=1)
    draw.line([27, 18, 29, 24], fill=WHITE, width=1)
    # side white stripe
    draw.rectangle([14, 16, 16, 36], fill=WHITE)

# --- 37. Cozy Cardigan ---
def draw_cardigan(draw):
    draw.rectangle([13, 14, 37, 44], fill=BEIGE)
    draw.rectangle([8, 16, 13, 38], fill=BEIGE)
    draw.rectangle([37, 16, 42, 38], fill=BEIGE)
    # open V-neck
    draw.polygon([(20, 14), (30, 14), (25, 36)], fill=0)
    # buttons
    for y in [24, 30, 36]:
        draw.ellipse([24, y, 26, y+2], fill=DKBROWN)

# --- 38. Down Puffer Vest ---
def draw_puffer_vest(draw):
    draw.rectangle([14, 14, 36, 42], fill=ORANGE)
    # puffy segments
    for y in [20, 26, 32, 38]:
        draw.line([14, y, 36, y], fill=DKRED, width=1)
    draw.line([25, 14, 25, 42], fill=BLACK, width=1) # zipper

# --- 39. Ballet Tutu ---
def draw_tutu(draw):
    # waistband
    draw.rectangle([18, 18, 32, 21], fill=WHITE)
    # fluffy layered skirt
    draw.ellipse([10, 21, 40, 36], fill=PINK)
    draw.ellipse([12, 24, 38, 38], fill=DKPINK)

# --- 40. Kimono Dress ---
def draw_kimono(draw):
    draw.rectangle([14, 12, 36, 46], fill=RED)
    draw.rectangle([6, 16, 14, 34], fill=RED) # wide sleeves
    draw.rectangle([36, 16, 44, 34], fill=RED)
    # Obi (wide sash belt)
    draw.rectangle([14, 24, 36, 30], fill=GOLD)
    draw.rectangle([21, 23, 29, 31], fill=WHITE)

# --- 41. Striped Poncho ---
def draw_poncho(draw):
    draw.polygon([(25, 10), (42, 24), (25, 44), (8, 24)], fill=BROWN)
    # neck hole
    draw.ellipse([22, 14, 28, 20], fill=0)
    # stripes
    draw.line([12, 24, 38, 24], fill=YELLOW, width=2)
    draw.line([16, 30, 34, 30], fill=RED, width=2)

# --- 42. Flat Cap ---
def draw_flat_cap(draw):
    draw.ellipse([13, 18, 37, 30], fill=GREY)
    draw.rectangle([16, 26, 34, 31], fill=GREY)
    draw.line([20, 29, 36, 29], fill=DKGREY, width=1) # visor line

# --- 43. Fuzzy Slippers ---
def draw_slippers(draw):
    # Left slipper
    draw.rounded_rectangle([11, 28, 22, 42], radius=3, fill=BEIGE)
    draw.ellipse([11, 26, 22, 34], fill=WHITE) # fluffy cuff
    
    # Right slipper
    draw.rounded_rectangle([28, 28, 39, 42], radius=3, fill=BEIGE)
    draw.ellipse([28, 26, 39, 34], fill=WHITE)

# --- 44. Sombrero Hat ---
def draw_sombrero(draw):
    draw.ellipse([18, 10, 32, 24], fill=BEIGE) # crown
    draw.ellipse([6, 22, 44, 36], fill=BEIGE) # wide brim
    # colorful hatband
    draw.rectangle([17, 21, 33, 23], fill=RED)
    draw.rectangle([18, 23, 32, 24], fill=GREEN)

# --- 45. Chef's Toque Hat ---
def draw_chef_hat(draw):
    draw.ellipse([14, 10, 36, 32], fill=WHITE)
    draw.rectangle([17, 28, 33, 38], fill=WHITE) # band
    # folds
    draw.line([20, 14, 20, 28], fill=GREY)
    draw.line([25, 12, 25, 28], fill=GREY)
    draw.line([30, 14, 30, 28], fill=GREY)

# --- 46. Fluffy Earmuffs ---
def draw_earmuffs(draw):
    # headband
    draw.arc([14, 12, 36, 36], 180, 360, fill=BLACK, width=2)
    # ear pads
    draw.ellipse([10, 24, 16, 32], fill=PINK)
    draw.ellipse([34, 24, 40, 32], fill=PINK)

# --- 47. Formal Suit Vest ---
def draw_formal_vest(draw):
    draw.rectangle([14, 14, 36, 42], fill=BLACK)
    # V-neck cutout
    draw.polygon([(18, 14), (32, 14), (25, 30)], fill=0)
    draw.polygon([(23, 20), (27, 20), (25, 30)], fill=RED) # tie inside
    # buttons
    for y in [32, 36, 40]:
        draw.ellipse([24, y, 26, y+2], fill=SILVER)

# --- 48. Running Shorts ---
def draw_running_shorts(draw):
    draw.rectangle([15, 16, 35, 34], fill=BLUE)
    draw.rectangle([24, 24, 26, 34], fill=0)
    # white trim around bottom
    draw.rectangle([15, 32, 23, 34], fill=WHITE)
    draw.rectangle([27, 32, 35, 34], fill=WHITE)

# --- 49. Knit Cardigan Vest ---
def draw_cardigan_vest(draw):
    draw.rectangle([14, 14, 36, 42], fill=DKGREEN)
    # V-neck
    draw.polygon([(19, 14), (31, 14), (25, 28)], fill=0)
    # pattern stripes
    draw.line([14, 34, 36, 34], fill=GREY)
    draw.line([14, 37, 36, 37], fill=GREY)

# --- 50. Wooden Clogs ---
def draw_clogs(draw):
    # Left clog
    draw.rounded_rectangle([10, 28, 22, 42], radius=4, fill=BEIGE)
    draw.rectangle([10, 36, 22, 42], fill=BROWN) # wooden sole
    draw.ellipse([14, 30, 18, 34], fill=BROWN) # buckle strap
    
    # Right clog
    draw.rounded_rectangle([28, 28, 40, 42], radius=4, fill=BEIGE)
    draw.rectangle([28, 36, 40, 42], fill=BROWN)
    draw.ellipse([32, 30, 36, 34], fill=BROWN)

# --- 51. Knee-High Leather Boots ---
def draw_leather_boots_tall(draw):
    # Left boot
    draw.rectangle([11, 10, 20, 38], fill=DKBROWN)
    draw.rectangle([11, 34, 25, 41], fill=DKBROWN)
    draw.rectangle([10, 39, 25, 42], fill=BLACK) # sole
    draw.ellipse([18, 12, 22, 16], fill=GOLD) # top buckle
    
    # Right boot
    draw.rectangle([29, 10, 38, 38], fill=DKBROWN)
    draw.rectangle([29, 34, 43, 41], fill=DKBROWN)
    draw.rectangle([28, 39, 43, 42], fill=BLACK) # sole
    draw.ellipse([36, 12, 40, 16], fill=GOLD)

# --- 52. Denim Vest ---
def draw_denim_vest(draw):
    draw.rectangle([14, 15, 36, 42], fill=BLUE)
    # cut sleeves
    draw.polygon([(14, 15), (20, 15), (14, 25)], fill=0)
    draw.polygon([(36, 15), (30, 15), (36, 25)], fill=0)
    # open chest V
    draw.polygon([(21, 15), (29, 15), (25, 25)], fill=0)
    # buttons
    for y in [27, 33, 39]:
        draw.ellipse([24, y, 26, y+2], fill=GOLD)

# --- 53. Puffer Jacket ---
def draw_puffer_jacket(draw):
    draw.rectangle([13, 14, 37, 43], fill=RED)
    draw.rectangle([7, 16, 13, 38], fill=RED)
    draw.rectangle([37, 16, 42, 38], fill=RED)
    # puffer horizontal segments
    for y in [20, 26, 32, 38]:
        draw.line([13, y, 37, y], fill=DKRED, width=1)
        draw.line([7, y, 13, y], fill=DKRED, width=1)
        draw.line([37, y, 42, y], fill=DKRED, width=1)
    draw.line([25, 14, 25, 43], fill=BLACK) # zipper

# --- 54. Slouchy Beanie Hat ---
def draw_beanie_slouchy(draw):
    draw.ellipse([14, 15, 36, 38], fill=PURPLE)
    draw.ellipse([26, 20, 42, 38], fill=PURPLE) # slouch bag
    draw.rectangle([13, 31, 37, 37], fill=DKRED) # folded brim

# --- 55. Bikini Set ---
def draw_bathingsuit_bikini(draw):
    draw.polygon([(16, 16), (22, 16), (19, 22)], fill=PINK)
    draw.polygon([(28, 16), (34, 16), (31, 22)], fill=PINK)
    draw.line([14, 16, 36, 16], fill=WHITE, width=1)
    draw.polygon([(17, 32), (33, 32), (25, 42)], fill=PINK)
    draw.line([15, 32, 35, 32], fill=WHITE, width=1)

# --- 56. Cargo Pants ---
def draw_cargo_pants(draw):
    draw.rectangle([15, 12, 35, 44], fill=KHAKI)
    draw.rectangle([24, 22, 26, 44], fill=0)
    draw.rectangle([12, 26, 16, 32], fill=DKBROWN)
    draw.rectangle([34, 26, 38, 32], fill=DKBROWN)

# --- 57. Silk Kimono Robe ---
def draw_kimono_robe(draw):
    draw.rectangle([15, 12, 35, 46], fill=DKBLUE)
    draw.rectangle([7, 16, 15, 32], fill=DKBLUE)
    draw.rectangle([35, 16, 43, 32], fill=DKBLUE)
    draw.rectangle([15, 24, 35, 29], fill=GOLD)
    draw.ellipse([18, 16, 21, 19], fill=WHITE)
    draw.ellipse([30, 36, 33, 39], fill=WHITE)

# --- 58. French Wool Beret ---
def draw_beret(draw):
    draw.ellipse([12, 18, 38, 30], fill=RED)
    draw.ellipse([18, 16, 32, 22], fill=RED)
    draw.line([25, 13, 25, 16], fill=BLACK, width=1)

# --- 59. Fingerless Leather Gloves ---
def draw_leather_gloves_fingerless(draw):
    draw.rectangle([11, 20, 22, 35], fill=BLACK)
    draw.rectangle([11, 20, 22, 22], fill=GREY)
    draw.rectangle([11, 31, 22, 35], fill=DKGREY)
    draw.rectangle([28, 20, 39, 35], fill=BLACK)
    draw.rectangle([28, 20, 39, 22], fill=GREY)
    draw.rectangle([28, 31, 39, 35], fill=DKGREY)

# --- 60. Tuxedo Jacket ---
def draw_tuxedo_jacket(draw):
    draw.rectangle([13, 13, 37, 44], fill=BLACK)
    draw.rectangle([8, 15, 13, 40], fill=BLACK)
    draw.rectangle([37, 15, 42, 40], fill=BLACK)
    draw.polygon([(20, 13), (30, 13), (25, 25)], fill=WHITE)
    draw.polygon([(22, 15), (25, 17), (22, 19)], fill=BLACK)
    draw.polygon([(28, 15), (25, 17), (28, 19)], fill=BLACK)

# --- 61. Plaid Skirt ---
def draw_plaid_skirt(draw):
    draw.polygon([(18, 18), (32, 18), (40, 42), (10, 42)], fill=RED)
    for x in range(14, 38, 6):
        draw.line([x, 18, x*1.1 - 2, 42], fill=DKBLUE, width=1)
    for y in range(22, 42, 6):
        draw.line([14, y, 36, y], fill=YELLOW, width=1)

# --- 62. Wrap Dress ---
def draw_wrap_dress(draw):
    draw.polygon([(18, 14), (32, 14), (28, 24), (22, 24)], fill=TEAL)
    draw.polygon([(22, 24), (28, 24), (38, 45), (12, 45)], fill=TEAL)
    draw.line([18, 14, 28, 24], fill=WHITE, width=1)
    draw.line([28, 24, 16, 45], fill=WHITE, width=1)
    draw.ellipse([27, 23, 31, 26], fill=WHITE)

# --- 63. Hawaiian Shirt ---
def draw_hawaiian_shirt(draw):
    draw.rectangle([14, 15, 36, 42], fill=LIGHTBLUE)
    draw.rectangle([9, 15, 14, 25], fill=LIGHTBLUE)
    draw.rectangle([36, 15, 41, 25], fill=LIGHTBLUE)
    draw.ellipse([18, 20, 21, 23], fill=RED)
    draw.ellipse([30, 28, 33, 31], fill=YELLOW)
    draw.ellipse([22, 34, 25, 37], fill=RED)
    draw.polygon([(22, 15), (28, 15), (25, 19)], fill=WHITE)

# --- 64. Polo Collared Shirt ---
def draw_polo_shirt(draw):
    draw.rectangle([14, 15, 36, 42], fill=GREEN)
    draw.rectangle([10, 15, 14, 25], fill=GREEN)
    draw.rectangle([36, 15, 40, 25], fill=GREEN)
    draw.polygon([(20, 15), (25, 18), (25, 15)], fill=DKGREEN)
    draw.polygon([(30, 15), (25, 18), (25, 15)], fill=DKGREEN)
    draw.rectangle([17, 20, 19, 22], fill=WHITE)

# --- 65. Fleece Zip-Up Vest ---
def draw_fleece_vest(draw):
    draw.rectangle([14, 15, 36, 42], fill=BLUE)
    draw.polygon([(14, 15), (18, 15), (14, 23)], fill=0)
    draw.polygon([(36, 15), (32, 15), (36, 23)], fill=0)
    draw.line([25, 15, 25, 42], fill=SILVER, width=1)
    draw.rectangle([18, 12, 32, 15], fill=GREY)

# --- 66. Bowler Hat ---
def draw_bowler_hat(draw):
    draw.ellipse([16, 16, 34, 30], fill=BLACK)
    draw.ellipse([11, 25, 39, 32], fill=BLACK)
    draw.rectangle([16, 24, 34, 26], fill=DKGREY)

# --- 67. Summer Espadrilles ---
def draw_espadrilles(draw):
    draw.rounded_rectangle([10, 28, 22, 41], radius=3, fill=BEIGE)
    draw.rectangle([10, 38, 22, 41], fill=YELLOW)
    draw.rounded_rectangle([28, 28, 40, 41], radius=3, fill=BEIGE)
    draw.rectangle([28, 38, 40, 41], fill=YELLOW)

# --- 68. Double-Buckle Leather Belt ---
def draw_leather_belt_double(draw):
    draw.rectangle([8, 20, 42, 28], fill=DKBROWN)
    draw.rectangle([18, 18, 24, 30], fill=GOLD, outline=BLACK, width=1)
    draw.rectangle([26, 18, 32, 30], fill=GOLD, outline=BLACK, width=1)

# --- 69. Rubber Rain Boots ---
def draw_rain_boots(draw):
    draw.rectangle([11, 16, 20, 38], fill=YELLOW)
    draw.rectangle([11, 32, 25, 41], fill=YELLOW)
    draw.rectangle([10, 39, 25, 42], fill=BLACK)
    draw.rectangle([11, 16, 20, 18], fill=BLACK)
    draw.rectangle([29, 16, 38, 38], fill=YELLOW)
    draw.rectangle([29, 32, 43, 41], fill=YELLOW)
    draw.rectangle([28, 39, 43, 42], fill=BLACK)
    draw.rectangle([29, 16, 38, 18], fill=BLACK)

# --- 70. Yellow Sun Dress ---
def draw_sun_dress(draw):
    draw.polygon([(18, 14), (32, 14), (28, 24), (22, 24)], fill=YELLOW)
    draw.polygon([(22, 24), (28, 24), (40, 45), (10, 45)], fill=YELLOW)
    draw.ellipse([20, 28, 22, 30], fill=BLUE)
    draw.ellipse([30, 36, 32, 38], fill=BLUE)
    draw.ellipse([16, 40, 18, 42], fill=BLUE)

# --- 71. Cozy Fleece Sweatpants ---
def draw_sweatpants(draw):
    draw.rectangle([15, 12, 35, 44], fill=GREY)
    draw.rectangle([24, 22, 26, 44], fill=0)
    draw.ellipse([24, 14, 26, 16], fill=WHITE)
    draw.line([23, 15, 21, 20], fill=WHITE)
    draw.line([27, 15, 29, 20], fill=WHITE)

# --- 72. Knit Earmuffs ---
def draw_earmuffs_knit(draw):
    draw.arc([13, 12, 37, 37], 180, 360, fill=RED, width=3)
    draw.ellipse([9, 23, 16, 31], fill=YELLOW)
    draw.ellipse([33, 23, 40, 31], fill=YELLOW)

# --- 73. Medical Scrubs Top ---
def draw_scrubs_shirt(draw):
    draw.rectangle([14, 15, 36, 42], fill=TEAL)
    draw.rectangle([9, 15, 14, 25], fill=TEAL)
    draw.rectangle([36, 15, 41, 25], fill=TEAL)
    draw.polygon([(21, 15), (29, 15), (25, 20)], fill=WHITE)
    draw.rectangle([28, 26, 33, 32], fill=DKCYAN)

# --- 74. Medical Scrubs Pants ---
def draw_scrubs_pants(draw):
    draw.rectangle([15, 12, 35, 44], fill=TEAL)
    draw.rectangle([24, 22, 26, 44], fill=0)
    draw.rectangle([12, 22, 15, 28], fill=DKCYAN)

# --- 75. Varsity Letterman Jacket ---
def draw_varsity_jacket(draw):
    draw.rectangle([14, 14, 36, 43], fill=DKBLUE)
    draw.rectangle([8, 16, 14, 39], fill=WHITE)
    draw.rectangle([36, 16, 42, 39], fill=WHITE)
    draw.rectangle([8, 37, 14, 39], fill=DKBLUE)
    draw.rectangle([36, 37, 42, 39], fill=DKBLUE)
    draw.line([17, 20, 20, 24], fill=YELLOW, width=1)
    draw.line([20, 20, 17, 24], fill=YELLOW, width=1)

# --- 76. Sleek Black Leather Skirt ---
def draw_leather_skirt(draw):
    draw.polygon([(18, 18), (32, 18), (37, 38), (13, 38)], fill=BLACK)
    draw.line([25, 18, 25, 38], fill=SILVER, width=1)

# --- 77. Classic Cowboy Hat ---
def draw_cowboy_hat(draw):
    draw.ellipse([15, 14, 35, 26], fill=BROWN)
    draw.ellipse([21, 12, 29, 17], fill=DKBROWN)
    draw.ellipse([8, 22, 42, 32], fill=BROWN)
    draw.arc([8, 22, 42, 32], 0, 180, fill=DKBROWN, width=1)

# --- 78. Cowboy Boots ---
def draw_cowboy_boots(draw):
    draw.rectangle([11, 14, 20, 38], fill=BROWN)
    draw.rectangle([11, 33, 26, 41], fill=BROWN)
    draw.polygon([(11, 14), (20, 14), (15, 18)], fill=0)
    draw.ellipse([14, 22, 17, 26], fill=GOLD)
    draw.rectangle([10, 40, 26, 42], fill=BLACK)
    draw.rectangle([29, 14, 38, 38], fill=BROWN)
    draw.rectangle([29, 33, 44, 41], fill=BROWN)
    draw.polygon([(29, 14), (38, 14), (33, 18)], fill=0)
    draw.ellipse([32, 22, 35, 26], fill=GOLD)
    draw.rectangle([28, 40, 44, 42], fill=BLACK)

# --- 79. Knee-High Socks ---
def draw_knee_high_socks(draw):
    draw.rectangle([13, 12, 20, 34], fill=WHITE)
    draw.rectangle([13, 31, 24, 36], fill=WHITE)
    draw.rectangle([13, 12, 20, 14], fill=BLUE)
    draw.rectangle([13, 16, 20, 18], fill=RED)
    draw.rectangle([29, 12, 36, 34], fill=WHITE)
    draw.rectangle([29, 31, 40, 36], fill=WHITE)
    draw.rectangle([29, 12, 36, 14], fill=BLUE)
    draw.rectangle([29, 16, 36, 18], fill=RED)

# --- 80. Neon Green Running Shoes ---
def draw_running_shoes_neon(draw):
    draw.rounded_rectangle([8, 27, 24, 39], radius=2, fill=GREEN)
    draw.rectangle([8, 37, 24, 39], fill=BLACK)
    draw.polygon([(18, 27), (24, 27), (24, 36)], fill=BLACK)
    draw.rounded_rectangle([26, 27, 42, 39], radius=2, fill=GREEN)
    draw.rectangle([26, 37, 42, 39], fill=BLACK)
    draw.polygon([(36, 27), (42, 27), (42, 36)], fill=BLACK)

# --- 81. Silicone Swim Cap ---
def draw_swim_cap(draw):
    draw.ellipse([14, 15, 36, 35], fill=ORANGE)
    draw.rectangle([14, 25, 36, 32], fill=ORANGE)
    draw.arc([20, 22, 30, 28], 0, 180, fill=WHITE, width=2)

# --- 82. Top Hat ---
def draw_top_hat(draw):
    draw.rectangle([16, 10, 34, 30], fill=BLACK)
    draw.ellipse([11, 28, 39, 34], fill=BLACK)
    draw.rectangle([16, 27, 34, 29], fill=RED)

# --- 83. Aviator Hat with Goggles ---
def draw_aviator_hat(draw):
    draw.ellipse([14, 15, 36, 35], fill=BROWN)
    draw.rectangle([14, 30, 18, 40], fill=BROWN)
    draw.rectangle([32, 30, 36, 40], fill=BROWN)
    draw.rectangle([14, 22, 36, 26], fill=BLACK)
    draw.ellipse([18, 20, 24, 26], fill=LIGHTBLUE, outline=SILVER, width=1)
    draw.ellipse([26, 20, 32, 26], fill=LIGHTBLUE, outline=SILVER, width=1)

# --- 84. Cozy Pajama Shorts ---
def draw_pajama_shorts(draw):
    draw.rectangle([15, 18, 35, 36], fill=PINK)
    draw.rectangle([24, 26, 26, 36], fill=0)
    draw.ellipse([18, 21, 20, 23], fill=WHITE)
    draw.ellipse([30, 23, 32, 25], fill=WHITE)
    draw.ellipse([21, 29, 23, 31], fill=WHITE)

# --- 85. Boxing Gloves ---
def draw_boxing_gloves(draw):
    draw.rounded_rectangle([10, 16, 22, 35], radius=5, fill=RED)
    draw.rectangle([10, 30, 22, 35], fill=WHITE)
    draw.rounded_rectangle([27, 16, 39, 35], radius=5, fill=RED)
    draw.rectangle([27, 30, 39, 35], fill=WHITE)

# --- 86. Cycling Jersey ---
def draw_cycling_jersey(draw):
    draw.rectangle([14, 15, 36, 42], fill=YELLOW)
    draw.rectangle([9, 15, 14, 24], fill=YELLOW)
    draw.rectangle([36, 15, 41, 24], fill=YELLOW)
    draw.rectangle([14, 24, 17, 42], fill=BLACK)
    draw.rectangle([33, 24, 36, 42], fill=BLACK)
    draw.line([25, 15, 25, 28], fill=BLACK)

# --- 87. Cycling Shorts ---
def draw_cycling_shorts(draw):
    draw.rectangle([16, 16, 34, 38], fill=BLACK)
    draw.rectangle([24, 26, 26, 38], fill=0)
    draw.rectangle([16, 35, 23, 38], fill=YELLOW)
    draw.rectangle([27, 35, 34, 38], fill=YELLOW)

# --- 88. Summer Yukata Kimono ---
def draw_kimono_yukata(draw):
    draw.rectangle([15, 12, 35, 46], fill=BLUE)
    draw.rectangle([7, 16, 15, 30], fill=BLUE)
    draw.rectangle([35, 16, 43, 30], fill=BLUE)
    draw.rectangle([15, 25, 35, 29], fill=RED)
    draw.ellipse([18, 34, 20, 36], fill=YELLOW)
    draw.ellipse([29, 18, 31, 20], fill=YELLOW)

# --- 89. Winter Ski Jacket ---
def draw_ski_jacket(draw):
    draw.rectangle([13, 12, 37, 44], fill=ORANGE)
    draw.rectangle([7, 15, 13, 40], fill=ORANGE)
    draw.rectangle([37, 15, 42, 40], fill=ORANGE)
    draw.rounded_rectangle([16, 6, 34, 14], radius=3, fill=BEIGE)
    draw.rectangle([24, 15, 26, 44], fill=WHITE)

# --- 90. Waterproof Ski Pants ---
def draw_ski_pants(draw):
    draw.rectangle([15, 12, 35, 44], fill=ORANGE)
    draw.rectangle([24, 22, 26, 44], fill=0)
    draw.rectangle([17, 26, 21, 32], fill=BLACK)
    draw.rectangle([29, 26, 33, 32], fill=BLACK)

# --- 91. Graduation Gown ---
def draw_graduation_gown(draw):
    draw.rectangle([14, 14, 36, 46], fill=BLACK)
    draw.rectangle([7, 16, 14, 40], fill=BLACK)
    draw.rectangle([36, 16, 43, 40], fill=BLACK)
    draw.polygon([(21, 14), (29, 14), (25, 28)], fill=PURPLE)

# --- 92. Graduation Cap ---
def draw_graduation_cap(draw):
    draw.polygon([(25, 10), (41, 18), (25, 26), (9, 18)], fill=BLACK)
    draw.rectangle([19, 21, 31, 28], fill=BLACK)
    draw.line([25, 18, 36, 18], fill=YELLOW)
    draw.line([36, 18, 36, 28], fill=YELLOW)

# --- 93. Full Wetsuit ---
def draw_wetsuit(draw):
    draw.rectangle([14, 12, 36, 46], fill=BLACK)
    draw.rectangle([24, 28, 26, 46], fill=0)
    draw.rectangle([14, 12, 36, 18], fill=BLUE)
    draw.rectangle([8, 15, 14, 32], fill=BLUE)
    draw.rectangle([36, 15, 42, 32], fill=BLUE)

# --- 94. Leather Harness Suspenders ---
def draw_leather_harness(draw):
    draw.line([16, 10, 16, 42], fill=DKBROWN, width=2)
    draw.line([34, 10, 34, 42], fill=DKBROWN, width=2)
    draw.line([16, 22, 34, 22], fill=DKBROWN, width=2)
    draw.ellipse([14, 20, 18, 24], fill=SILVER)
    draw.ellipse([32, 20, 36, 24], fill=SILVER)

# --- 95. Victorian Corset ---
def draw_corset(draw):
    draw.polygon([(16, 14), (34, 14), (30, 38), (20, 38)], fill=RED)
    for y in range(18, 36, 4):
        draw.line([23, y, 27, y+2], fill=BLACK, width=1)
        draw.line([27, y, 23, y+2], fill=BLACK, width=1)
    draw.line([16, 14, 34, 14], fill=GOLD, width=1)

# --- 96. Scottish Kilt Skirt ---
def draw_kilt(draw):
    draw.polygon([(18, 18), (32, 18), (36, 38), (14, 38)], fill=GREEN)
    for x in range(16, 36, 4):
        draw.line([x, 18, x, 38], fill=RED, width=1)
    for y in range(22, 38, 4):
        draw.line([14, y, 36, y], fill=YELLOW, width=1)
    draw.rectangle([22, 22, 28, 28], fill=BROWN)

# --- 97. Silk Nightgown Dress ---
def draw_nightgown(draw):
    draw.polygon([(19, 14), (31, 14), (27, 24), (23, 24)], fill=LIGHTBLUE)
    draw.polygon([(23, 24), (27, 24), (36, 45), (14, 45)], fill=LIGHTBLUE)
    draw.rectangle([14, 44, 36, 45], fill=WHITE)
    draw.line([19, 14, 31, 14], fill=WHITE)

# --- 98. Shearling Coat ---
def draw_shearling_coat(draw):
    draw.rectangle([13, 12, 37, 45], fill=BROWN)
    draw.rectangle([8, 15, 13, 38], fill=BROWN)
    draw.rectangle([37, 15, 42, 38], fill=BROWN)
    draw.polygon([(20, 12), (30, 12), (25, 26)], fill=WHITE)
    draw.rectangle([8, 36, 13, 38], fill=WHITE)
    draw.rectangle([37, 36, 42, 38], fill=WHITE)

# --- 99. Short Denim Overalls ---
def draw_overalls_short(draw):
    draw.rectangle([15, 22, 35, 36], fill=BLUE)
    draw.rectangle([24, 28, 26, 36], fill=0)
    draw.rectangle([17, 15, 33, 22], fill=BLUE)
    draw.line([17, 15, 17, 10], fill=DKBLUE, width=2)
    draw.line([33, 15, 33, 10], fill=DKBLUE, width=2)
    draw.rectangle([12, 10, 15, 18], fill=PINK)
    draw.rectangle([35, 10, 38, 18], fill=PINK)

# --- 100. Clear Rain Poncho ---
def draw_poncho_rain(draw):
    draw.polygon([(25, 10), (43, 25), (25, 45), (7, 25)], fill=(230, 240, 250, 80))
    draw.ellipse([18, 8, 32, 18], fill=(230, 240, 250, 120))
    draw.rectangle([18, 18, 32, 34], fill=BLUE)

# --- 101. Striped T-Shirt ---
def draw_tshirt_striped(draw):
    draw.rectangle([14, 15, 36, 42], fill=RED)
    draw.rectangle([10, 15, 14, 25], fill=RED)
    draw.rectangle([36, 15, 40, 25], fill=RED)
    for y in range(18, 42, 6):
        draw.line([14, y, 36, y], fill=WHITE, width=2)

# --- 102. Ripped Denim Jeans ---
def draw_ripped_jeans(draw):
    draw.rectangle([15, 12, 35, 44], fill=BLUE)
    draw.rectangle([24, 22, 26, 44], fill=0)
    # ripped slits
    draw.line([18, 22, 22, 22], fill=WHITE)
    draw.line([28, 28, 32, 28], fill=WHITE)

# --- 103. Bomber Jacket ---
def draw_bomber_jacket(draw):
    draw.rectangle([14, 15, 36, 43], fill=GREEN)
    draw.rectangle([8, 17, 14, 39], fill=GREEN)
    draw.rectangle([36, 17, 42, 39], fill=GREEN)
    # black cuffs & collar
    draw.rectangle([8, 37, 14, 39], fill=BLACK)
    draw.rectangle([36, 37, 42, 39], fill=BLACK)
    draw.rectangle([14, 41, 36, 43], fill=BLACK)
    draw.line([25, 15, 25, 41], fill=SILVER)

# --- 104. Leather Combat Boots ---
def draw_combat_boots(draw):
    # Left boot
    draw.rectangle([11, 14, 20, 38], fill=BLACK)
    draw.rectangle([11, 32, 25, 41], fill=BLACK)
    draw.rectangle([10, 39, 25, 42], fill=GREY) # sole
    draw.line([16, 18, 16, 30], fill=YELLOW, width=1) # laces
    
    # Right boot
    draw.rectangle([29, 14, 38, 38], fill=BLACK)
    draw.rectangle([29, 32, 43, 41], fill=BLACK)
    draw.rectangle([28, 39, 43, 42], fill=GREY)
    draw.line([34, 18, 34, 30], fill=YELLOW, width=1)

# --- 105. Sun Visor Cap ---
def draw_sun_visor(draw):
    draw.rectangle([14, 25, 36, 29], fill=WHITE) # band
    draw.rectangle([14, 27, 42, 31], fill=BLUE) # visor bill
    draw.arc([16, 24, 34, 32], 180, 360, fill=GREY)

# --- 106. Denim Jacket ---
def draw_denim_jacket(draw):
    draw.rectangle([14, 14, 36, 42], fill=BLUE)
    draw.rectangle([9, 16, 14, 38], fill=BLUE)
    draw.rectangle([36, 16, 41, 38], fill=BLUE)
    # collars
    draw.polygon([(14, 14), (20, 14), (16, 20)], fill=DKBLUE)
    draw.polygon([(36, 14), (30, 14), (34, 20)], fill=DKBLUE)
    # buttons
    for y in [22, 28, 34]:
        draw.ellipse([24, y, 26, y+2], fill=SILVER)

# --- 107. Black Leather Pants ---
def draw_leather_pants(draw):
    draw.rectangle([15, 12, 35, 44], fill=BLACK)
    draw.rectangle([24, 22, 26, 44], fill=0)
    # silver studs
    for y in [14, 20, 26, 32]:
        draw.ellipse([16, y, 17, y+1], fill=SILVER)
        draw.ellipse([32, y, 33, y+1], fill=SILVER)

# --- 108. Hooded Cloak ---
def draw_hooded_cloak(draw):
    draw.polygon([(25, 10), (44, 46), (6, 46)], fill=PURPLE)
    # hood
    draw.rounded_rectangle([18, 8, 32, 18], radius=3, fill=DKGREY)
    # cloak tie
    draw.ellipse([24, 18, 26, 20], fill=GOLD)

# --- 109. Plaid Suit Blazer ---
def draw_blazer_plaid(draw):
    draw.rectangle([13, 13, 37, 44], fill=GREY)
    draw.rectangle([8, 15, 13, 40], fill=GREY)
    draw.rectangle([37, 15, 42, 40], fill=GREY)
    # plaid lines
    for x in [16, 22, 28, 34]:
        draw.line([x, 13, x, 44], fill=RED)
    for y in [18, 26, 34]:
        draw.line([13, y, 37, y], fill=RED)

# --- 110. Swim Goggles ---
def draw_swim_goggles(draw):
    draw.line([10, 22, 40, 22], fill=YELLOW, width=2) # strap
    # lenses
    draw.ellipse([14, 18, 22, 26], fill=DKBLUE, outline=WHITE)
    draw.ellipse([26, 18, 34, 26], fill=DKBLUE, outline=WHITE)

# --- 111. Winter Gloves ---
def draw_winter_gloves(draw):
    # Left glove
    draw.rounded_rectangle([11, 18, 22, 35], radius=3, fill=BLUE)
    draw.rectangle([11, 32, 22, 35], fill=BLACK) # cuff
    
    # Right glove
    draw.rounded_rectangle([28, 18, 39, 35], radius=3, fill=BLUE)
    draw.rectangle([28, 32, 39, 35], fill=BLACK)

# --- 112. Feather Boa Scarf ---
def draw_boa(draw):
    # Fluffy boa draped around neck
    draw.ellipse([13, 14, 37, 28], fill=PINK)
    draw.ellipse([15, 16, 35, 26], fill=0)
    # fluffy textures
    for x in range(12, 38, 4):
        draw.ellipse([x, 12, x+3, 15], fill=DKPINK)
        draw.ellipse([x, 25, x+3, 28], fill=DKPINK)

# --- 113. Polka-Dot Socks ---
def draw_socks_patterned(draw):
    # Left sock
    draw.rectangle([13, 15, 20, 34], fill=BLUE)
    draw.rectangle([13, 31, 25, 36], fill=BLUE)
    draw.ellipse([15, 20, 17, 22], fill=WHITE)
    draw.ellipse([16, 28, 18, 30], fill=WHITE)
    
    # Right sock
    draw.rectangle([28, 15, 35, 34], fill=BLUE)
    draw.rectangle([28, 31, 40, 36], fill=BLUE)
    draw.ellipse([30, 20, 32, 22], fill=WHITE)
    draw.ellipse([31, 28, 33, 30], fill=WHITE)

# --- 114. Suede Ankle Boots ---
def draw_ankle_boots(draw):
    # Left boot
    draw.rectangle([11, 24, 21, 38], fill=BROWN)
    draw.rectangle([11, 34, 25, 41], fill=BROWN)
    draw.rectangle([10, 40, 25, 42], fill=BLACK) # sole
    
    # Right boot
    draw.rectangle([28, 24, 38, 38], fill=BROWN)
    draw.rectangle([28, 34, 42, 41], fill=BROWN)
    draw.rectangle([27, 40, 42, 42], fill=BLACK)

# --- 115. Stiletto Strappy Sandals ---
def draw_stiletto_sandals(draw):
    # Left sandal
    draw.line([14, 28, 14, 40], fill=BLACK, width=1) # heel
    draw.polygon([(12, 38), (22, 38), (14, 40)], fill=BLACK)
    draw.line([12, 32, 22, 32], fill=RED, width=2) # straps
    
    # Right sandal
    draw.line([30, 28, 30, 40], fill=BLACK, width=1)
    draw.polygon([(28, 38), (38, 38), (30, 40)], fill=BLACK)
    draw.line([28, 32, 38, 32], fill=RED, width=2)

# --- 116. Camouflage Cargo Shorts ---
def draw_cargo_shorts_camo(draw):
    draw.rectangle([14, 15, 36, 38], fill=GREEN)
    draw.rectangle([24, 24, 26, 38], fill=0)
    # camo spots
    draw.rectangle([16, 18, 20, 22], fill=DKGREEN)
    draw.rectangle([28, 20, 32, 24], fill=BROWN)
    draw.rectangle([18, 28, 22, 32], fill=DKGREY)

# --- 117. Packable Rain Jacket ---
def draw_rain_jacket_packable(draw):
    draw.rectangle([14, 15, 36, 42], fill=BLUE)
    draw.rectangle([9, 17, 14, 38], fill=BLUE)
    draw.rectangle([36, 17, 41, 38], fill=BLUE)
    # hood
    draw.rounded_rectangle([18, 8, 32, 16], radius=3, fill=BLUE)
    # front pocket pouch
    draw.rectangle([20, 26, 30, 32], fill=DKBLUE)

# --- 118. Flannel Pajama Pants ---
def draw_pajama_pants(draw):
    draw.rectangle([15, 12, 35, 44], fill=RED)
    draw.rectangle([24, 22, 26, 44], fill=0)
    # flannel grids
    for x in [18, 22, 28, 32]:
        draw.line([x, 12, x, 44], fill=BLACK, width=1)
    for y in range(16, 44, 6):
        draw.line([15, y, 35, y], fill=BLACK, width=1)

# --- 119. Victorian Waistcoat Vest ---
def draw_waistcoat(draw):
    draw.rectangle([14, 14, 36, 42], fill=DKBROWN)
    # V neck
    draw.polygon([(18, 14), (32, 14), (25, 26)], fill=0)
    # watch chain line
    draw.line([18, 32, 25, 36], fill=GOLD, width=1)
    # buttons
    for y in [28, 34, 40]:
        draw.ellipse([24, y, 26, y+2], fill=GOLD)

# --- 120. Safety Reflective Vest ---
def draw_safety_vest(draw):
    draw.rectangle([14, 14, 36, 42], fill=YELLOW)
    # V neck
    draw.polygon([(19, 14), (31, 14), (25, 26)], fill=0)
    # silver reflective stripes
    draw.line([14, 24, 36, 24], fill=SILVER, width=2)
    draw.line([14, 34, 36, 34], fill=SILVER, width=2)

# --- 121. Panama Straw Hat ---
def draw_panama_hat(draw):
    draw.ellipse([15, 16, 35, 28], fill=BEIGE)
    draw.ellipse([10, 24, 40, 32], fill=BEIGE) # brim
    draw.rectangle([15, 23, 35, 25], fill=BLACK) # ribbon

# --- 122. Double-Pom Beanie ---
def draw_beanie_pom(draw):
    draw.ellipse([14, 14, 36, 38], fill=PINK)
    draw.rectangle([13, 30, 37, 38], fill=DKPINK)
    # two pom poms
    draw.ellipse([11, 7, 17, 13], fill=WHITE)
    draw.ellipse([33, 7, 39, 13], fill=WHITE)

# --- 123. Overall Pinafore Skirt ---
def draw_overalls_skirt(draw):
    # white shirt underneath
    draw.rectangle([16, 12, 34, 22], fill=WHITE)
    # pinafore blue denim skirt
    draw.polygon([(18, 18), (32, 18), (38, 42), (12, 42)], fill=BLUE)
    # bib & straps
    draw.rectangle([19, 18, 31, 26], fill=BLUE)
    draw.line([19, 18, 19, 12], fill=DKBLUE, width=1)
    draw.line([31, 18, 31, 12], fill=DKBLUE, width=1)

# --- 124. Sporty Windbreaker Pants ---
def draw_windbreaker_pants(draw):
    draw.rectangle([15, 12, 35, 44], fill=TEAL)
    draw.rectangle([24, 22, 26, 44], fill=0)
    # purple side panels
    draw.rectangle([15, 12, 18, 44], fill=PURPLE)
    draw.rectangle([32, 12, 35, 44], fill=PURPLE)

# --- 125. Striped Swim Trunks ---
def draw_swimming_trunks_striped(draw):
    draw.rectangle([14, 16, 36, 36], fill=ORANGE)
    draw.rectangle([24, 26, 26, 36], fill=0)
    # yellow stripes
    for x in [18, 22, 28, 32]:
        draw.line([x, 16, x, 36], fill=YELLOW, width=2)

# --- 126. Haori Kimono Jacket ---
def draw_kimono_haori(draw):
    draw.rectangle([13, 14, 37, 40], fill=BLACK)
    draw.rectangle([7, 16, 13, 32], fill=BLACK)
    draw.rectangle([37, 16, 42, 32], fill=BLACK)
    # gold trim borders
    draw.rectangle([13, 38, 37, 40], fill=GOLD)
    draw.line([25, 14, 25, 38], fill=GOLD)

# --- 127. Oversized Knit Cardigan ---
def draw_cardigan_oversized(draw):
    draw.rectangle([12, 13, 38, 45], fill=GREY)
    draw.rectangle([6, 15, 12, 40], fill=GREY)
    draw.rectangle([38, 15, 44, 40], fill=GREY)
    # open neckline
    draw.polygon([(18, 13), (32, 13), (25, 32)], fill=0)

# --- 128. Hooded Puffer Vest ---
def draw_vest_puffer_hooded(draw):
    draw.rectangle([14, 16, 36, 42], fill=BLUE)
    # puffer horizontal seams
    for y in [22, 28, 34, 40]:
        draw.line([14, y, 36, y], fill=DKBLUE)
    # grey hood
    draw.rounded_rectangle([18, 8, 32, 16], radius=3, fill=GREY)

# --- 129. Ballet Flat Shoes ---
def draw_ballet_flat(draw):
    # Left flat
    draw.rounded_rectangle([10, 30, 22, 41], radius=2, fill=BLACK)
    draw.ellipse([14, 32, 18, 35], fill=GOLD) # bow
    
    # Right flat
    draw.rounded_rectangle([28, 30, 40, 41], radius=2, fill=BLACK)
    draw.ellipse([32, 32, 36, 35], fill=GOLD)

# --- 130. Mariachi Sombrero ---
def draw_sombrero_mariachi(draw):
    draw.ellipse([18, 10, 32, 24], fill=BLACK)
    draw.ellipse([6, 22, 44, 36], fill=BLACK)
    # silver embroidery details
    draw.arc([6, 22, 44, 36], 0, 360, fill=SILVER, width=1)
    draw.rectangle([17, 21, 33, 23], fill=SILVER)

# --- 131. Furry Winter Earmuffs ---
def draw_earmuffs_furry(draw):
    draw.arc([14, 12, 36, 36], 180, 360, fill=BLACK, width=2)
    # fluffy white earmuffs
    draw.ellipse([9, 24, 16, 32], fill=WHITE)
    draw.ellipse([33, 24, 40, 32], fill=WHITE)

# --- 132. Formal Tuxedo Trousers ---
def draw_formal_trousers(draw):
    draw.rectangle([16, 12, 34, 44], fill=BLACK)
    draw.rectangle([24, 22, 26, 44], fill=0)
    # satin stripe down sides
    draw.line([16, 12, 16, 44], fill=DKGREY, width=1)
    draw.line([34, 12, 34, 44], fill=DKGREY, width=1)

# --- 133. Split Running Shorts ---
def draw_running_shorts_split(draw):
    draw.rectangle([15, 16, 35, 34], fill=RED)
    draw.rectangle([24, 24, 26, 34], fill=0)
    # split side panels (drawn as side slits)
    draw.polygon([(15, 26), (18, 34), (15, 34)], fill=0)
    draw.polygon([(35, 26), (32, 34), (35, 34)], fill=0)

# --- 134. Long Duster Cardigan ---
def draw_cardigan_long(draw):
    draw.rectangle([14, 12, 36, 46], fill=YELLOW)
    draw.rectangle([8, 14, 14, 38], fill=YELLOW)
    draw.rectangle([36, 14, 42, 38], fill=YELLOW)
    # long open split front
    draw.rectangle([23, 12, 27, 46], fill=0)

# --- 135. Japanese Wooden Geta ---
def draw_wooden_geta(draw):
    # Left geta
    draw.rectangle([10, 30, 22, 38], fill=BEIGE) # wood base
    draw.rectangle([12, 38, 14, 42], fill=BEIGE) # support teeth
    draw.rectangle([18, 38, 20, 42], fill=BEIGE)
    draw.line([10, 32, 16, 30], fill=RED, width=1) # straps
    draw.line([22, 32, 16, 30], fill=RED, width=1)
    
    # Right geta
    draw.rectangle([28, 30, 40, 38], fill=BEIGE)
    draw.rectangle([30, 38, 32, 42], fill=BEIGE)
    draw.rectangle([36, 38, 38, 42], fill=BEIGE)
    draw.line([28, 32, 34, 30], fill=RED, width=1)
    draw.line([40, 32, 34, 30], fill=RED, width=1)

# --- 136. Heavy Winter Down Coat ---
def draw_winter_coat(draw):
    draw.rectangle([13, 12, 37, 45], fill=RED)
    draw.rectangle([7, 14, 13, 40], fill=RED)
    draw.rectangle([37, 14, 42, 40], fill=RED)
    # fur hood trim
    draw.rounded_rectangle([16, 6, 34, 14], radius=3, fill=WHITE)
    draw.rectangle([8, 38, 13, 40], fill=WHITE) # fur cuffs
    draw.rectangle([37, 38, 42, 40], fill=WHITE)

# --- 137. Vintage Tweed Jacket ---
def draw_tweed_jacket(draw):
    draw.rectangle([13, 13, 37, 43], fill=BROWN)
    draw.rectangle([8, 15, 13, 40], fill=BROWN)
    draw.rectangle([37, 15, 42, 40], fill=BROWN)
    # textured tweed look (dark brown spots)
    for x in range(14, 36, 4):
        for y in range(16, 42, 6):
            draw.ellipse([x, y, x+1, y+1], fill=DKBROWN)

# --- 138. Highland Traditional Kilt ---
def draw_kilt_tartan_traditional(draw):
    draw.polygon([(18, 18), (32, 18), (36, 38), (14, 38)], fill=RED)
    # green checks
    for x in range(16, 36, 4):
        draw.line([x, 18, x, 38], fill=GREEN, width=1)
    for y in range(22, 38, 4):
        draw.line([14, y, 36, y], fill=GREEN, width=1)
    # black sporran pouch
    draw.rectangle([21, 22, 29, 30], fill=BLACK)

# --- 139. Vintage Lace Nightgown ---
def draw_nightgown_vintage(draw):
    draw.polygon([(19, 14), (31, 14), (27, 24), (23, 24)], fill=WHITE)
    draw.polygon([(23, 24), (27, 24), (36, 45), (14, 45)], fill=WHITE)
    # pink neck bow
    draw.ellipse([23, 15, 27, 18], fill=PINK)

# --- 140. Fleece Half-Zip Pullover ---
def draw_fleece_pullover(draw):
    draw.rectangle([14, 15, 36, 42], fill=GREY)
    draw.rectangle([8, 17, 14, 38], fill=GREY)
    draw.rectangle([36, 17, 42, 38], fill=GREY)
    # blue collar & zipper
    draw.rectangle([17, 11, 33, 15], fill=BLUE)
    draw.line([25, 15, 25, 26], fill=SILVER)

# --- 141. Canvas Work Overalls ---
def draw_overalls_work(draw):
    draw.rectangle([15, 22, 35, 45], fill=BROWN)
    draw.rectangle([24, 30, 26, 45], fill=0)
    # bib & metallic buckles
    draw.rectangle([17, 14, 33, 22], fill=BROWN)
    draw.ellipse([16, 14, 19, 17], fill=SILVER)
    draw.ellipse([31, 14, 34, 17], fill=SILVER)

# --- 142. Knitted Fringe Poncho ---
def draw_poncho_knitted(draw):
    draw.polygon([(25, 10), (42, 24), (25, 44), (8, 24)], fill=RED)
    # white stripe pattern
    draw.line([13, 24, 37, 24], fill=WHITE, width=2)
    # fringe dots at bottom edges
    for x in range(10, 42, 4):
        draw.ellipse([x, 26 + (16 - abs(25-x))*0.8, x+2, 28 + (16 - abs(25-x))*0.8], fill=WHITE)

# --- 143. Straw Visor Sun Hat ---
def draw_visor_hat(draw):
    draw.rectangle([14, 25, 36, 28], fill=BEIGE) # visor band
    draw.rectangle([12, 27, 38, 31], fill=BEIGE) # straw bill

# --- 144. Chef Apron with Stripe ---
def draw_chef_apron_bib(draw):
    draw.rectangle([16, 18, 34, 42], fill=WHITE)
    draw.rectangle([19, 12, 31, 18], fill=WHITE)
    # red stripe down side
    draw.rectangle([18, 18, 20, 42], fill=RED)

# --- 145. Leather Flight Jacket ---
def draw_flight_jacket(draw):
    draw.rectangle([14, 14, 36, 43], fill=BROWN)
    draw.rectangle([8, 16, 14, 39], fill=BROWN)
    draw.rectangle([36, 16, 42, 39], fill=BROWN)
    # beige wool collar
    draw.rounded_rectangle([17, 10, 33, 16], radius=2, fill=BEIGE)

# --- 146. Distressed Denim Shorts ---
def draw_distressed_shorts(draw):
    draw.rectangle([14, 15, 36, 35], fill=BLUE)
    draw.rectangle([24, 26, 26, 35], fill=0)
    # frayed bottom white fringe
    draw.rectangle([14, 34, 23, 35], fill=WHITE)
    draw.rectangle([27, 34, 36, 35], fill=WHITE)

# --- 147. Silk Sleeping Mask ---
def draw_sleeping_mask(draw):
    draw.rounded_rectangle([12, 20, 38, 30], radius=3, fill=PINK)
    draw.line([8, 25, 42, 25], fill=PINK, width=1) # elastic strap
    # ZZZ text
    draw.line([20, 23, 24, 23], fill=YELLOW)
    draw.line([24, 23, 20, 27], fill=YELLOW)
    draw.line([20, 27, 24, 27], fill=YELLOW)

# --- 148. Trail Running Sneakers ---
def draw_running_shoes_trail(draw):
    # Left shoe
    draw.rounded_rectangle([8, 26, 24, 38], radius=2, fill=GREY)
    draw.rectangle([8, 36, 24, 38], fill=ORANGE) # sole
    draw.line([14, 28, 18, 28], fill=BLACK)
    
    # Right shoe
    draw.rounded_rectangle([26, 26, 42, 38], radius=2, fill=GREY)
    draw.rectangle([26, 36, 42, 38], fill=ORANGE)
    draw.line([32, 28, 36, 28], fill=BLACK)

# --- 149. Retro High-Waisted Swimsuit ---
def draw_swimming_suit_retro(draw):
    draw.rectangle([16, 16, 34, 42], fill=WHITE)
    # black high-waisted bottom panel
    draw.rectangle([16, 28, 34, 42], fill=BLACK)
    draw.polygon([(16, 34), (25, 42), (16, 42)], fill=0)
    draw.polygon([(34, 34), (25, 42), (34, 42)], fill=0)

# --- 150. Gothic Leather Trench Coat ---
def draw_leather_trench(draw):
    draw.rectangle([13, 12, 37, 46], fill=BLACK)
    draw.rectangle([8, 14, 13, 38], fill=BLACK)
    draw.rectangle([37, 14, 42, 38], fill=BLACK)
    # silver button rows
    for y in [18, 24, 30]:
        draw.ellipse([18, y, 20, y+2], fill=SILVER)
        draw.ellipse([30, y, 32, y+2], fill=SILVER)

# --- 151. Camouflage Jacket ---
def draw_camo_jacket(draw):
    draw.rectangle([13, 14, 37, 43], fill=GREEN)
    draw.rectangle([8, 16, 13, 38], fill=GREEN)
    draw.rectangle([37, 16, 42, 38], fill=GREEN)
    # camo spots
    draw.rectangle([16, 18, 20, 22], fill=DKGREEN)
    draw.rectangle([28, 22, 32, 26], fill=BROWN)
    draw.rectangle([18, 30, 22, 34], fill=DKGREY)

# --- 152. Suede Moccasin Slippers ---
def draw_moccasins(draw):
    # Left shoe
    draw.rounded_rectangle([10, 28, 22, 42], radius=3, fill=BROWN)
    draw.arc([12, 28, 20, 36], 0, 180, fill=BEIGE, width=1) # stitching
    
    # Right shoe
    draw.rounded_rectangle([28, 28, 40, 42], radius=3, fill=BROWN)
    draw.arc([30, 28, 38, 36], 0, 180, fill=BEIGE, width=1)

# --- 153. Harem Yoga Pants ---
def draw_harem_pants(draw):
    # Baggy harem pants shape
    draw.ellipse([14, 14, 36, 44], fill=PURPLE)
    draw.rectangle([24, 24, 26, 44], fill=0) # split gap
    draw.rectangle([14, 12, 36, 15], fill=BLACK) # waist cuff

# --- 154. Chunky Knit Cowl Scarf ---
def draw_knit_cowl(draw):
    draw.ellipse([14, 14, 36, 28], fill=YELLOW)
    # chunky knit vertical stripes
    for x in range(16, 36, 4):
        draw.line([x, 14, x, 28], fill=ORANGE, width=1)

# --- 155. Spandex Biker Shorts ---
def draw_biker_shorts(draw):
    draw.rectangle([16, 18, 34, 36], fill=BLACK)
    draw.rectangle([24, 24, 26, 36], fill=0)

# --- 156. Tie-Dye Bucket Hat ---
def draw_bucket_hat(draw):
    draw.ellipse([15, 18, 35, 30], fill=PURPLE)
    draw.ellipse([11, 26, 39, 34], fill=TEAL) # tie dye brim split
    # spots of pink
    draw.ellipse([18, 20, 22, 24], fill=PINK)
    draw.ellipse([28, 24, 32, 28], fill=PINK)

# --- 157. Hooded Monk Robe ---
def draw_monk_robe(draw):
    draw.rectangle([14, 14, 36, 46], fill=BROWN)
    draw.rounded_rectangle([18, 8, 32, 16], radius=3, fill=BROWN) # hood
    # rope belt
    draw.line([14, 28, 36, 28], fill=WHITE, width=2)
    draw.line([25, 28, 25, 38], fill=WHITE, width=2)

# --- 158. Safari Utility Jacket ---
def draw_safari_jacket(draw):
    draw.rectangle([13, 14, 37, 43], fill=KHAKI)
    draw.rectangle([8, 16, 13, 38], fill=KHAKI)
    draw.rectangle([37, 16, 42, 38], fill=KHAKI)
    # four front pockets
    draw.rectangle([16, 18, 21, 23], fill=DKBROWN)
    draw.rectangle([29, 18, 34, 23], fill=DKBROWN)
    draw.rectangle([16, 30, 21, 36], fill=DKBROWN)
    draw.rectangle([29, 30, 34, 36], fill=DKBROWN)

# --- 159. Tweed Newsboy Cap ---
def draw_tweed_cap(draw):
    draw.ellipse([13, 18, 37, 30], fill=DKGREY)
    draw.rectangle([16, 26, 34, 31], fill=DKGREY)
    draw.ellipse([24, 16, 26, 18], fill=BLACK) # button top

# --- 160. High-Top Canvas Sneakers ---
def draw_high_tops(draw):
    # Left shoe
    draw.rectangle([10, 20, 22, 38], fill=BLACK)
    draw.rounded_rectangle([8, 30, 24, 38], radius=2, fill=BLACK)
    draw.rectangle([8, 36, 24, 38], fill=WHITE) # sole
    draw.rectangle([8, 30, 12, 35], fill=WHITE) # rubber toe cap
    
    # Right shoe
    draw.rectangle([28, 20, 40, 38], fill=BLACK)
    draw.rounded_rectangle([26, 30, 42, 38], radius=2, fill=BLACK)
    draw.rectangle([26, 36, 42, 38], fill=WHITE)
    draw.rectangle([26, 30, 30, 35], fill=WHITE)

# --- 161. Halter Neck Bikini ---
def draw_swimming_bikini_halter(draw):
    # Halter top
    draw.polygon([(16, 16), (22, 16), (25, 10)], fill=TEAL)
    draw.polygon([(28, 16), (34, 16), (25, 10)], fill=TEAL)
    # Bottom
    draw.polygon([(17, 32), (33, 32), (25, 42)], fill=TEAL)

# --- 162. Sherpa Fleece Hoodie ---
def draw_fleece_hoodie(draw):
    # Fluffy white sherpa jacket
    draw.rectangle([14, 16, 36, 44], fill=WHITE)
    draw.rectangle([9, 18, 14, 38], fill=WHITE)
    draw.rectangle([36, 18, 41, 38], fill=WHITE)
    draw.rounded_rectangle([18, 8, 32, 17], radius=3, fill=WHITE)
    # drawstrings
    draw.line([22, 17, 22, 24], fill=BLACK)
    draw.line([28, 17, 28, 24], fill=BLACK)

# --- 163. Fur Cossack Winter Hat ---
def draw_cossack_hat(draw):
    # Cylinder fur hat
    draw.rounded_rectangle([15, 14, 35, 32], radius=4, fill=BLACK)
    # grey textured lines
    for y in [18, 24, 30]:
        draw.line([16, y, 34, y], fill=DKGREY)

# --- 164. Studded Leather Corset ---
def draw_leather_corset(draw):
    draw.polygon([(16, 14), (34, 14), (30, 38), (20, 38)], fill=BLACK)
    # silver studs trim
    for y in range(16, 38, 4):
        draw.ellipse([18, y, 19, y+1], fill=SILVER)
        draw.ellipse([31, y, 32, y+1], fill=SILVER)

# --- 165. Sheer Mesh Top ---
def draw_mesh_top(draw):
    # Red tank under
    draw.rectangle([18, 20, 32, 40], fill=RED)
    # black transparent mesh grid (simulated by lines)
    for x in range(14, 38, 3):
        draw.line([x, 15, x, 42], fill=BLACK)
    for y in range(15, 42, 3):
        draw.line([14, y, 36, y], fill=BLACK)

# --- 166. Pajama Nightshirt ---
def draw_pajama_nightshirt(draw):
    draw.rectangle([14, 14, 36, 45], fill=BLUE)
    draw.rectangle([9, 16, 14, 28], fill=BLUE)
    draw.rectangle([36, 16, 41, 28], fill=BLUE)
    # buttons down middle
    for y in [20, 26, 32, 38]:
        draw.ellipse([24, y, 26, y+2], fill=WHITE)

# --- 167. Hooded Rain Poncho ---
def draw_poncho_hooded(draw):
    draw.polygon([(25, 10), (43, 24), (25, 44), (7, 24)], fill=RED)
    draw.rounded_rectangle([18, 8, 32, 16], radius=3, fill=RED)

# --- 168. Distressed Denim Skirt ---
def draw_denim_skirt(draw):
    draw.polygon([(18, 18), (32, 18), (36, 38), (14, 38)], fill=BLUE)
    # white frayed bottom
    draw.rectangle([14, 36, 36, 38], fill=WHITE)

# --- 169. Suede Chelsea Boots ---
def draw_chelsea_boots(draw):
    # Left boot
    draw.rectangle([11, 20, 20, 38], fill=BEIGE)
    draw.rectangle([11, 33, 25, 41], fill=BEIGE)
    draw.rectangle([16, 24, 19, 32], fill=BLACK) # black elastic side
    draw.rectangle([10, 40, 25, 42], fill=BROWN) # sole
    
    # Right boot
    draw.rectangle([29, 20, 38, 38], fill=BEIGE)
    draw.rectangle([29, 33, 43, 41], fill=BEIGE)
    draw.rectangle([30, 24, 33, 32], fill=BLACK)
    draw.rectangle([28, 40, 43, 42], fill=BROWN)

# --- 170. Traditional Silk Sari ---
def draw_sari(draw):
    # Red wrap with gold border
    draw.polygon([(18, 12), (32, 12), (36, 46), (14, 46)], fill=RED)
    # gold shoulder drape diagonal
    draw.line([18, 12, 36, 36], fill=GOLD, width=3)
    # gold bottom border
    draw.rectangle([14, 44, 36, 46], fill=GOLD)

# --- 171. Wellington Rain Boots ---
def draw_wellington_boots(draw):
    # Left boot
    draw.rectangle([11, 16, 20, 38], fill=GREEN)
    draw.rectangle([11, 32, 25, 41], fill=GREEN)
    draw.rectangle([10, 40, 25, 42], fill=BLACK)
    
    # Right boot
    draw.rectangle([29, 16, 38, 38], fill=GREEN)
    draw.rectangle([29, 32, 43, 41], fill=GREEN)
    draw.rectangle([28, 40, 43, 42], fill=BLACK)

# --- 172. Bavarian Dirndl Dress ---
def draw_dirndl(draw):
    # Green skirt
    draw.polygon([(20, 24), (30, 24), (38, 46), (12, 46)], fill=GREEN)
    # red apron
    draw.polygon([(22, 24), (28, 24), (32, 42), (18, 42)], fill=RED)
    # white blouse chest
    draw.rectangle([16, 12, 34, 24], fill=WHITE)
    # black corset vest
    draw.polygon([(17, 18), (33, 18), (30, 24), (20, 24)], fill=BLACK)

# --- 173. Traditional Lederhosen ---
def draw_lederhosen(draw):
    draw.rectangle([15, 20, 35, 38], fill=BROWN)
    draw.rectangle([24, 28, 26, 38], fill=0)
    # cross suspenders
    draw.line([17, 10, 17, 20], fill=DKBROWN, width=2)
    draw.line([33, 10, 33, 20], fill=DKBROWN, width=2)
    draw.line([17, 14, 33, 14], fill=DKBROWN, width=2) # chest band

# --- 174. Classic Sailor Collar Suit ---
def draw_sailor_suit(draw):
    draw.rectangle([14, 15, 36, 42], fill=WHITE)
    # blue collar V neck
    draw.polygon([(18, 15), (32, 15), (25, 26)], fill=BLUE)
    draw.polygon([(21, 15), (29, 15), (25, 20)], fill=WHITE) # inner neck white
    # red tie knot
    draw.ellipse([24, 23, 26, 26], fill=RED)

# --- 175. Medieval Linen Tunic ---
def draw_tunic_medieval(draw):
    draw.rectangle([14, 14, 36, 43], fill=BEIGE)
    draw.rectangle([8, 16, 14, 30], fill=BEIGE)
    draw.rectangle([35, 16, 41, 30], fill=BEIGE)
    # brown waist belt
    draw.rectangle([14, 28, 36, 30], fill=BROWN)
    draw.ellipse([24, 27, 26, 31], fill=GOLD)

# --- 176. Victorian Silk Cravat ---
def draw_cravat(draw):
    draw.ellipse([20, 14, 30, 26], fill=PURPLE) # cravat puff
    draw.ellipse([22, 14, 28, 24], fill=WHITE) # collar overlay
    # gold pin in center
    draw.ellipse([24, 20, 26, 22], fill=GOLD)

# --- 177. Vintage Shoe Spats ---
def draw_spats(draw):
    # Left foot
    draw.rounded_rectangle([10, 30, 22, 42], radius=2, fill=BLACK) # shoe
    draw.rectangle([11, 26, 21, 36], fill=WHITE) # spats wrap
    # spats buttons
    draw.ellipse([20, 30, 21, 31], fill=BLACK)
    
    # Right foot
    draw.rounded_rectangle([28, 30, 40, 42], radius=2, fill=BLACK)
    draw.rectangle([29, 26, 39, 36], fill=WHITE)
    draw.ellipse([38, 30, 39, 31], fill=BLACK)

# --- 178. Utility Boiler Suit ---
def draw_boiler_suit(draw):
    draw.rectangle([14, 12, 36, 46], fill=DKGREY)
    draw.rectangle([24, 28, 26, 46], fill=0) # split
    draw.rectangle([8, 15, 14, 40], fill=DKGREY) # sleeves
    draw.rectangle([36, 15, 42, 40], fill=DKGREY)
    # silver front zipper
    draw.line([25, 12, 25, 28], fill=SILVER, width=1)

# --- 179. Packable Cagoule Windbreaker ---
def draw_cagoule(draw):
    draw.rectangle([13, 14, 37, 42], fill=YELLOW)
    draw.rectangle([8, 16, 13, 38], fill=YELLOW)
    draw.rectangle([37, 16, 42, 38], fill=YELLOW)
    # hood & half zipper
    draw.rounded_rectangle([17, 6, 33, 14], radius=3, fill=YELLOW)
    draw.line([25, 14, 25, 26], fill=SILVER, width=1)

# --- 180. Utility Hunting Vest ---
def draw_hunting_vest(draw):
    draw.rectangle([14, 15, 36, 42], fill=GREEN)
    # cut sleeves
    draw.polygon([(14, 15), (18, 15), (14, 23)], fill=0)
    draw.polygon([(36, 15), (32, 15), (36, 23)], fill=0)
    # brown pockets
    draw.rectangle([16, 26, 21, 32], fill=BROWN)
    draw.rectangle([29, 26, 34, 32], fill=BROWN)

# --- 181. Academic Graduation Hood ---
def draw_academic_hood(draw):
    draw.polygon([(25, 14), (36, 28), (25, 42), (14, 28)], fill=BLACK)
    # red velvet inner border
    draw.polygon([(25, 18), (32, 28), (25, 38), (18, 28)], fill=RED)

# --- 182. Safety Life Vest ---
def draw_life_vest(draw):
    draw.rectangle([14, 14, 36, 42], fill=ORANGE)
    # black strap buckles
    draw.rectangle([17, 24, 33, 26], fill=BLACK)
    draw.rectangle([17, 32, 33, 34], fill=BLACK)
    draw.ellipse([24, 23, 26, 27], fill=GOLD) # buckles
    draw.ellipse([24, 31, 26, 35], fill=GOLD)

# --- 183. Russian Ushanka Hat ---
def draw_ushanka(draw):
    draw.ellipse([15, 15, 35, 28], fill=GREY)
    draw.rectangle([16, 24, 34, 30], fill=GREY)
    # folded up side ear flaps
    draw.rectangle([12, 16, 16, 26], fill=WHITE)
    draw.rectangle([34, 16, 38, 26], fill=WHITE)
    draw.rectangle([16, 24, 34, 28], fill=WHITE) # front fur band

# --- 184. Knight Tabard ---
def draw_tabard(draw):
    draw.rectangle([16, 14, 34, 44], fill=RED)
    # gold cross emblem in center
    draw.line([25, 18, 25, 38], fill=GOLD, width=3)
    draw.line([19, 26, 31, 26], fill=GOLD, width=3)

# --- 185. Renaissance Velvet Doublet ---
def draw_doublet(draw):
    draw.rectangle([14, 14, 36, 42], fill=PURPLE)
    # split bottom tail panels
    draw.polygon([(14, 38), (20, 38), (14, 44)], fill=PURPLE)
    draw.polygon([(36, 38), (30, 38), (36, 44)], fill=PURPLE)
    # gold scroll embroidery outline
    draw.line([14, 14, 25, 26], fill=GOLD, width=1)
    draw.line([36, 14, 25, 26], fill=GOLD, width=1)

# --- 186. Roman Toga Wrap ---
def draw_toga(draw):
    draw.polygon([(18, 12), (32, 12), (36, 46), (14, 46)], fill=WHITE)
    # red border draped over left shoulder
    draw.line([18, 12, 14, 46], fill=RED, width=3)
    draw.line([32, 12, 36, 46], fill=WHITE, width=2)

# --- 187. Wool Navy Peacoat ---
def draw_peacoat(draw):
    draw.rectangle([13, 12, 37, 44], fill=DKBLUE)
    draw.rectangle([8, 14, 13, 38], fill=DKBLUE)
    draw.rectangle([37, 14, 42, 38], fill=DKBLUE)
    # double breasted gold buttons
    for y in [18, 24, 30]:
        draw.ellipse([17, y, 19, y+2], fill=GOLD)
        draw.ellipse([31, y, 33, y+2], fill=GOLD)

# --- 188. Track Jacket ---
def draw_track_jacket(draw):
    draw.rectangle([13, 14, 37, 43], fill=RED)
    draw.rectangle([8, 16, 13, 38], fill=RED)
    draw.rectangle([37, 16, 42, 38], fill=RED)
    # white stripes down sleeves
    draw.line([10, 16, 10, 38], fill=WHITE, width=1)
    draw.line([40, 16, 40, 38], fill=WHITE, width=1)
    draw.line([25, 14, 25, 43], fill=BLACK) # zip

# --- 189. Ski Goggles ---
def draw_ski_goggles(draw):
    draw.line([8, 24, 42, 24], fill=BLACK, width=4) # thick strap
    # pink reflective lens
    draw.rounded_rectangle([12, 18, 38, 30], radius=3, fill=PINK, outline=WHITE)

# --- 190. Chef Neckerchief ---
def draw_chef_neckerchief(draw):
    draw.polygon([(20, 15), (30, 15), (25, 23)], fill=RED)
    draw.ellipse([23, 20, 27, 24], fill=RED) # knot

# --- 191. Shawl Cardigan ---
def draw_cardigan_shawl(draw):
    draw.rectangle([13, 14, 37, 44], fill=BLUE)
    draw.rectangle([8, 16, 13, 38], fill=BLUE)
    draw.rectangle([37, 16, 42, 38], fill=BLUE)
    # shawl collar rolled lapel
    draw.polygon([(18, 14), (32, 14), (25, 30)], fill=DKBLUE)

# --- 192. Running Singlet ---
def draw_running_singlet(draw):
    draw.rectangle([16, 15, 34, 42], fill=BLUE)
    # deep neck & sleeve cuts
    draw.polygon([(16, 15), (22, 15), (16, 23)], fill=0)
    draw.polygon([(34, 15), (28, 15), (34, 23)], fill=0)
    draw.polygon([(21, 15), (29, 15), (25, 21)], fill=0)
    # white trim borders
    draw.line([16, 15, 16, 42], fill=WHITE)
    draw.line([34, 15, 34, 42], fill=WHITE)

# --- 193. Tweed Pants ---
def draw_tweed_pants(draw):
    draw.rectangle([15, 12, 35, 44], fill=BROWN)
    draw.rectangle([24, 22, 26, 44], fill=0)
    # dark spots tweed
    for x in [17, 21, 29, 33]:
        for y in range(16, 44, 8):
            draw.ellipse([x, y, x+1, y+1], fill=DKBROWN)

# --- 194. Fur Muff Handwarmer ---
def draw_muff(draw):
    # Fur cylinder
    draw.rounded_rectangle([12, 18, 38, 32], radius=4, fill=GREY)
    # white fur highlights
    for x in range(14, 38, 4):
        draw.ellipse([x, 20, x+1, 21], fill=WHITE)
        draw.ellipse([x, 28, x+1, 29], fill=WHITE)

# --- 195. Cowboy Leather Chaps ---
def draw_leather_chaps(draw):
    draw.rectangle([14, 12, 36, 15], fill=BROWN) # belt
    # leg panels
    draw.rectangle([13, 16, 21, 44], fill=BROWN)
    draw.rectangle([29, 16, 37, 44], fill=BROWN)
    # fringe on sides
    for y in range(18, 44, 4):
        draw.line([13, y, 10, y], fill=DKBROWN)
        draw.line([37, y, 40, y], fill=DKBROWN)

# --- 196. Plaid Flannel Shirt ---
def draw_flannel_shirt(draw):
    draw.rectangle([14, 15, 36, 42], fill=RED)
    draw.rectangle([8, 16, 14, 38], fill=RED)
    draw.rectangle([36, 16, 42, 38], fill=RED)
    # black check pattern
    for x in range(16, 36, 5):
        draw.line([x, 15, x, 42], fill=BLACK)
    for y in range(18, 42, 5):
        draw.line([14, y, 36, y], fill=BLACK)

# --- 197. Sporty Crop Top ---
def draw_crop_top(draw):
    draw.rectangle([16, 16, 34, 30], fill=GREY)
    # neck cuts
    draw.polygon([(21, 16), (29, 16), (25, 21)], fill=0)
    # bottom white elastic band
    draw.rectangle([16, 28, 34, 30], fill=WHITE)

# --- 198. Camouflage Ghillie Suit ---
def draw_ghillie_suit(draw):
    draw.rectangle([14, 14, 36, 44], fill=DKGREEN)
    draw.rectangle([24, 28, 26, 44], fill=0)
    # grass strands
    for x in range(12, 38, 3):
        for y in range(16, 44, 6):
            draw.line([x, y, x-2, y+4], fill=GREEN)
            draw.line([x, y, x+2, y+4], fill=BROWN)

# --- 199. Corduroy Dungarees ---
def draw_dungarees(draw):
    draw.rectangle([15, 20, 35, 45], fill=GREEN)
    draw.rectangle([24, 28, 26, 45], fill=0)
    # corduroy vertical rib lines
    for x in [18, 22, 28, 32]:
        draw.line([x, 20, x, 45], fill=DKGREEN)
    # bib & straps
    draw.rectangle([17, 14, 33, 20], fill=GREEN)
    draw.line([17, 14, 17, 8], fill=DKGREEN, width=1)
    draw.line([33, 14, 33, 8], fill=DKGREEN, width=1)

# --- 200. Explorer Pith Helmet ---
def draw_pith_helmet(draw):
    draw.ellipse([16, 15, 34, 28], fill=BEIGE) # dome
    draw.ellipse([10, 24, 40, 32], fill=BEIGE) # brim
    # brown hat band
    draw.rectangle([16, 23, 34, 25], fill=BROWN)

# Compile drawing list (200 items total)
DRAWINGS = {
    "tshirt": draw_tshirt,
    "jeans": draw_jeans,
    "hoodie": draw_hoodie,
    "sneakers": draw_sneakers,
    "baseball_cap": draw_cap,
    "leather_jacket": draw_leather_jacket,
    "trench_coat": draw_trench_coat,
    "suit_jacket": draw_suit_jacket,
    "dress_pants": draw_dress_pants,
    "sunglasses": draw_sunglasses,
    "winter_beanie": draw_winter_beanie,
    "scarf": draw_scarf,
    "mittens": draw_mittens,
    "socks": draw_socks,
    "high_heels": draw_high_heels,
    "boots": draw_boots,
    "sandals": draw_sandals,
    "swimsuit": draw_swimsuit,
    "bathrobe": draw_bathrobe,
    "tie": draw_tie,
    "bowtie": draw_bowtie,
    "belt": draw_belt,
    "skirt": draw_skirt,
    "dress": draw_dress,
    "sweater": draw_sweater,
    "cargo_shorts": draw_cargo_shorts,
    "raincoat": draw_raincoat,
    "pajamas": draw_pajamas,
    "apron": draw_apron,
    "gloves": draw_gloves,
    "fedora": draw_fedora,
    "straw_hat": draw_straw_hat,
    "overalls": draw_overalls,
    "windbreaker": draw_windbreaker,
    "tracksuit": draw_tracksuit,
    "bathingsuit_trunks": draw_swim_trunks,
    "cardigan": draw_cardigan,
    "vest": draw_puffer_vest,
    "tutu": draw_tutu,
    "kimono": draw_kimono,
    "poncho": draw_poncho,
    "flat_cap": draw_flat_cap,
    "slippers": draw_slippers,
    "sombrero": draw_sombrero,
    "chef_hat": draw_chef_hat,
    "earmuffs": draw_earmuffs,
    "vest_formal": draw_formal_vest,
    "running_shorts": draw_running_shorts,
    "cardigan_sweater": draw_cardigan_vest,
    "clogs": draw_clogs,
    
    # Items 51 to 100
    "leather_boots_tall": draw_leather_boots_tall,
    "denim_vest": draw_denim_vest,
    "puffer_jacket": draw_puffer_jacket,
    "beanie_slouchy": draw_beanie_slouchy,
    "bathingsuit_bikini": draw_bathingsuit_bikini,
    "cargo_pants": draw_cargo_pants,
    "kimono_robe": draw_kimono_robe,
    "beret": draw_beret,
    "leather_gloves_fingerless": draw_leather_gloves_fingerless,
    "tuxedo_jacket": draw_tuxedo_jacket,
    "plaid_skirt": draw_plaid_skirt,
    "wrap_dress": draw_wrap_dress,
    "hawaiian_shirt": draw_hawaiian_shirt,
    "polo_shirt": draw_polo_shirt,
    "fleece_vest": draw_fleece_vest,
    "bowler_hat": draw_bowler_hat,
    "espadrilles": draw_espadrilles,
    "leather_belt_double": draw_leather_belt_double,
    "rain_boots": draw_rain_boots,
    "sun_dress": draw_sun_dress,
    "sweatpants": draw_sweatpants,
    "earmuffs_knit": draw_earmuffs_knit,
    "scrubs_shirt": draw_scrubs_shirt,
    "scrubs_pants": draw_scrubs_pants,
    "varsity_jacket": draw_varsity_jacket,
    "leather_skirt": draw_leather_skirt,
    "cowboy_hat": draw_cowboy_hat,
    "cowboy_boots": draw_cowboy_boots,
    "knee_high_socks": draw_knee_high_socks,
    "running_shoes_neon": draw_running_shoes_neon,
    "swim_cap": draw_swim_cap,
    "top_hat": draw_top_hat,
    "aviator_hat": draw_aviator_hat,
    "pajama_shorts": draw_pajama_shorts,
    "boxing_gloves": draw_boxing_gloves,
    "cycling_jersey": draw_cycling_jersey,
    "cycling_shorts": draw_cycling_shorts,
    "kimono_yukata": draw_kimono_yukata,
    "ski_jacket": draw_ski_jacket,
    "ski_pants": draw_ski_pants,
    "graduation_gown": draw_graduation_gown,
    "graduation_cap": draw_graduation_cap,
    "wetsuit": draw_wetsuit,
    "leather_harness": draw_leather_harness,
    "corset": draw_corset,
    "kilt": draw_kilt,
    "nightgown": draw_nightgown,
    "shearling_coat": draw_shearling_coat,
    "overalls_short": draw_overalls_short,
    "poncho_rain": draw_poncho_rain,

    # Items 101 to 200
    "tshirt_striped": draw_tshirt_striped,
    "ripped_jeans": draw_ripped_jeans,
    "bomber_jacket": draw_bomber_jacket,
    "combat_boots": draw_combat_boots,
    "sun_visor": draw_sun_visor,
    "denim_jacket": draw_denim_jacket,
    "leather_pants": draw_leather_pants,
    "hooded_cloak": draw_hooded_cloak,
    "blazer_plaid": draw_blazer_plaid,
    "swim_goggles": draw_swim_goggles,
    "winter_gloves": draw_winter_gloves,
    "boa": draw_boa,
    "socks_patterned": draw_socks_patterned,
    "ankle_boots": draw_ankle_boots,
    "stiletto_sandals": draw_stiletto_sandals,
    "cargo_shorts_camo": draw_cargo_shorts_camo,
    "rain_jacket_packable": draw_rain_jacket_packable,
    "pajama_pants": draw_pajama_pants,
    "waistcoat": draw_waistcoat,
    "safety_vest": draw_safety_vest,
    "panama_hat": draw_panama_hat,
    "beanie_pom": draw_beanie_pom,
    "overalls_skirt": draw_overalls_skirt,
    "windbreaker_pants": draw_windbreaker_pants,
    "swimming_trunks_striped": draw_swimming_trunks_striped,
    "kimono_haori": draw_kimono_haori,
    "cardigan_oversized": draw_cardigan_oversized,
    "vest_puffer_hooded": draw_vest_puffer_hooded,
    "ballet_flat": draw_ballet_flat,
    "sombrero_mariachi": draw_sombrero_mariachi,
    "earmuffs_furry": draw_earmuffs_furry,
    "formal_trousers": draw_formal_trousers,
    "running_shorts_split": draw_running_shorts_split,
    "cardigan_long": draw_cardigan_long,
    "wooden_geta": draw_wooden_geta,
    "winter_coat": draw_winter_coat,
    "tweed_jacket": draw_tweed_jacket,
    "kilt_tartan_traditional": draw_kilt_tartan_traditional,
    "nightgown_vintage": draw_nightgown_vintage,
    "fleece_pullover": draw_fleece_pullover,
    "overalls_work": draw_overalls_work,
    "poncho_knitted": draw_poncho_knitted,
    "visor_hat": draw_visor_hat,
    "chef_apron_bib": draw_chef_apron_bib,
    "flight_jacket": draw_flight_jacket,
    "distressed_shorts": draw_distressed_shorts,
    "sleeping_mask": draw_sleeping_mask,
    "running_shoes_trail": draw_running_shoes_trail,
    "swimming_suit_retro": draw_swimming_suit_retro,
    "leather_trench": draw_leather_trench,
    "camo_jacket": draw_camo_jacket,
    "moccasins": draw_moccasins,
    "harem_pants": draw_harem_pants,
    "knit_cowl": draw_knit_cowl,
    "biker_shorts": draw_biker_shorts,
    "bucket_hat": draw_bucket_hat,
    "monk_robe": draw_monk_robe,
    "safari_jacket": draw_safari_jacket,
    "tweed_cap": draw_tweed_cap,
    "high_tops": draw_high_tops,
    "swimming_bikini_halter": draw_swimming_bikini_halter,
    "fleece_hoodie": draw_fleece_hoodie,
    "cossack_hat": draw_cossack_hat,
    "leather_corset": draw_leather_corset,
    "mesh_top": draw_mesh_top,
    "pajama_nightshirt": draw_pajama_nightshirt,
    "poncho_hooded": draw_poncho_hooded,
    "denim_skirt": draw_denim_skirt,
    "chelsea_boots": draw_chelsea_boots,
    "sari": draw_sari,
    "wellington_boots": draw_wellington_boots,
    "dirndl": draw_dirndl,
    "lederhosen": draw_lederhosen,
    "sailor_suit": draw_sailor_suit,
    "tunic_medieval": draw_tunic_medieval,
    "cravat": draw_cravat,
    "spats": draw_spats,
    "boiler_suit": draw_boiler_suit,
    "cagoule": draw_cagoule,
    "hunting_vest": draw_hunting_vest,
    "academic_hood": draw_academic_hood,
    "life_vest": draw_life_vest,
    "ushanka": draw_ushanka,
    "tabard": draw_tabard,
    "doublet": draw_doublet,
    "toga": draw_toga,
    "peacoat": draw_peacoat,
    "track_jacket": draw_track_jacket,
    "ski_goggles": draw_ski_goggles,
    "chef_neckerchief": draw_chef_neckerchief,
    "cardigan_shawl": draw_cardigan_shawl,
    "running_singlet": draw_running_singlet,
    "tweed_pants": draw_tweed_pants,
    "muff": draw_muff,
    "leather_chaps": draw_leather_chaps,
    "flannel_shirt": draw_flannel_shirt,
    "crop_top": draw_crop_top,
    "ghillie_suit": draw_ghillie_suit,
    "dungarees": draw_dungarees,
    "pith_helmet": draw_pith_helmet
}

if __name__ == "__main__":
    print(f"Generating 200 detailed clothing sprites inside {OUTPUT_DIR}...")
    for name, func in DRAWINGS.items():
        create_sprite(name, func)
    print("Done generating detailed clothing sprites!")
