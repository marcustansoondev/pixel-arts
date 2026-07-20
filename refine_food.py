import re

def refine_code():
    new_funcs = """
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
"""

    with open('/home/student_04_d45e8906ee4b/pixel-arts/generate_food_desserts.py', 'r') as f:
        content = f.read()

    # Find the block from def draw_omelette(d): down to def draw_fruitleather(d): ...
    # We will use regex to find this block.
    # It starts with def draw_omelette(d): and ends before def main():
    pattern = re.compile(r'def draw_omelette\(d\):.*?def main\(\):', re.DOTALL)
    
    # We append def main(): back since we matched it.
    new_content = pattern.sub(new_funcs + '\n\ndef main():', content)
    
    with open('/home/student_04_d45e8906ee4b/pixel-arts/generate_food_desserts.py', 'w') as f:
        f.write(new_content)
    print("Replaced 100 functions successfully.")

if __name__ == '__main__':
    refine_code()
