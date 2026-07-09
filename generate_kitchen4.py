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

# Color constants
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
GREY      = (160, 160, 165, 255)

# 1. Egg Slicer
def draw_egg_slicer(draw):
    draw.rounded_rectangle([10, 10, 40, 40], radius=4, fill=WHITE)
    draw.ellipse([14, 14, 36, 36], fill=CREAM)
    # steel slicing wires
    for x in range(18, 34, 3):
        draw.line([x, 14, x, 36], fill=SILVER, width=1)

# 2. Oil Sprayer
def draw_oil_sprayer(draw):
    draw.rounded_rectangle([16, 18, 34, 44], radius=3, fill=GLASS)
    draw.rounded_rectangle([18, 20, 32, 42], radius=2, fill=YELLOW)
    # spray cap
    draw.rectangle([16, 12, 34, 18], fill=SILVER)
    draw.line([25, 12, 25, 8], fill=WHITE, width=2)
    # nozzle hole
    draw.ellipse([23, 10, 27, 14], fill=DARK)

# 3. Dough Scraper
def draw_dough_scraper(draw):
    draw.rectangle([8, 12, 42, 18], fill=BROWN) # handle
    draw.rounded_rectangle([10, 18, 40, 38], radius=2, fill=SILVER) # metal blade
    draw.line([10, 38, 40, 38], fill=WHITE, width=1)

# 4. Flour Sifter
def draw_flour_sifter(draw):
    draw.rounded_rectangle([14, 12, 36, 40], radius=4, fill=SILVER)
    # handle loop
    draw.arc([6, 18, 16, 34], 90, 270, fill=STEEL, width=4)
    # crank knob
    draw.line([36, 26, 44, 26], fill=STEEL, width=2)
    draw.ellipse([42, 23, 46, 29], fill=RED)

# 5. Garlic Grater
def draw_garlic_grater(draw):
    # ceramic rasp dish
    draw.ellipse([10, 10, 40, 40], fill=CREAM)
    draw.ellipse([14, 14, 36, 36], fill=WHITE)
    # central bumpy teeth pattern
    for x in range(20, 32, 3):
        for y in range(20, 32, 3):
            draw.point((x, y), fill=BROWN)

# 6. Potato Masher
def draw_potato_masher(draw):
    draw.rounded_rectangle([22, 10, 28, 32], radius=3, fill=BROWN) # handle
    # wavy mashing plate at bottom
    draw.line([14, 32, 14, 40], fill=SILVER, width=2)
    draw.line([36, 32, 36, 40], fill=SILVER, width=2)
    draw.arc([14, 36, 36, 44], 0, 180, fill=SILVER, width=3)

# 7. Basting Bulb
def draw_basting_bulb(draw):
    # red silicone bulb
    draw.ellipse([18, 6, 32, 20], fill=RED)
    draw.ellipse([20, 8, 30, 18], fill=DKRED)
    # long tube
    draw.polygon([(22, 20), (28, 20), (26, 44), (24, 44)], fill=GLASS)

# 8. Meat Thermometer
def draw_meat_thermometer(draw):
    draw.line([25, 20, 25, 46], fill=SILVER, width=2) # probe
    # dial face
    draw.ellipse([15, 6, 35, 26], fill=SILVER)
    draw.ellipse([17, 8, 33, 24], fill=WHITE)
    # red needle
    draw.line([25, 16, 29, 12], fill=RED, width=2)

# 9. Herb Stripper
def draw_herb_stripper(draw):
    # metal plate with holes of varying sizes
    draw.rounded_rectangle([12, 12, 38, 38], radius=4, fill=SILVER)
    draw.rounded_rectangle([14, 14, 36, 36], radius=3, fill=STEEL)
    # holes
    for hx, hy, r in [(18, 20, 1), (25, 20, 2), (32, 20, 3), (25, 30, 4)]:
        draw.ellipse([hx-r, hy-r, hx+r, hy+r], fill=(0,0,0,0))

# 10. Jar Opener
def draw_jar_opener(draw):
    # circular rubber pad
    draw.ellipse([10, 10, 40, 40], fill=RED)
    draw.ellipse([12, 12, 38, 38], fill=DKRED)
    # ribbed grips
    for angle in range(0, 360, 30):
        draw.arc([10, 10, 40, 40], angle, angle+10, fill=WHITE, width=2)

# 11. Melon Slicer
def draw_melon_slicer(draw):
    # large circular frame with spokes
    draw.ellipse([6, 6, 44, 44], fill=GREEN)
    draw.ellipse([10, 10, 40, 40], fill=(0,0,0,0))
    # wire spokes
    for angle in range(0, 360, 45):
        draw.arc([8, 8, 42, 42], angle, angle+2, fill=SILVER, width=2)

# 12. Avocado Slicer
def draw_avocado_slicer(draw):
    draw.rounded_rectangle([20, 6, 30, 24], radius=3, fill=GREEN) # handle
    # loop blades
    draw.ellipse([14, 22, 36, 44], fill=GREEN)
    draw.ellipse([18, 26, 32, 40], fill=(0,0,0,0))
    for y in range(28, 38, 3):
        draw.line([18, y, 32, y], fill=STEEL, width=1)

# 13. Salad Tongs
def draw_salad_tongs(draw):
    # wooden hand forks
    draw.line([16, 10, 20, 42], fill=TAN, width=3)
    draw.line([34, 10, 30, 42], fill=TAN, width=3)
    # hand fingers
    draw.polygon([(18, 40), (22, 46), (22, 40)], fill=BROWN)
    draw.polygon([(32, 40), (28, 46), (28, 40)], fill=BROWN)

# 14. Butter Crock
def draw_butter_crock(draw):
    # ceramic jar base
    draw.rounded_rectangle([12, 22, 38, 46], radius=4, fill=BLUE)
    draw.rounded_rectangle([14, 24, 36, 44], radius=3, fill=DKBLUE)
    # bell lid
    draw.rounded_rectangle([14, 10, 36, 22], radius=4, fill=BLUE)
    draw.ellipse([21, 6, 29, 12], fill=WHITE)

# 15. Honey Pot
def draw_honey_pot(draw):
    # ceramic pot
    draw.ellipse([12, 16, 38, 44], fill=ORANGE)
    draw.ellipse([14, 18, 36, 42], fill=YELLOW)
    # lid
    draw.rounded_rectangle([16, 12, 34, 18], radius=2, fill=ORANGE)
    draw.ellipse([22, 8, 28, 14], fill=BROWN)
    # honey splash
    draw.chord([14, 24, 36, 34], 0, 180, fill=WHITE)

# 16. Salt Cellar
def draw_salt_cellar(draw):
    # wooden dish with pivoting lid swung open
    draw.rounded_rectangle([8, 24, 34, 44], radius=4, fill=BROWN)
    draw.ellipse([12, 28, 30, 40], fill=WHITE) # salt inside
    # swung lid
    draw.rounded_rectangle([20, 10, 44, 20], radius=4, fill=TAN)
    draw.ellipse([24, 14, 28, 18], fill=BROWN)

# 17. Ice Bucket
def draw_ice_bucket(draw):
    draw.rounded_rectangle([12, 16, 38, 44], radius=4, fill=SILVER)
    draw.ellipse([12, 14, 38, 20], fill=STEEL)
    # ice cubes sticking out
    draw.rectangle([16, 10, 24, 16], fill=GLASS)
    draw.rectangle([26, 8, 34, 15], fill=GLASS)
    # handles
    draw.arc([8, 18, 42, 40], 180, 360, fill=WHITE, width=2)

# 18. Cocktail Shaker
def draw_cocktail_shaker(draw):
    draw.polygon([(14, 16), (36, 16), (32, 44), (18, 44)], fill=SILVER)
    # cap/strainer lid
    draw.polygon([(16, 16), (34, 16), (30, 10), (20, 10)], fill=STEEL)
    draw.rounded_rectangle([22, 4, 28, 10], radius=2, fill=SILVER)

# 19. Jigger
def draw_jigger(draw):
    # double sided measuring cup (hourglass shape)
    draw.polygon([(16, 10), (34, 10), (25, 25)], fill=SILVER)
    draw.polygon([(18, 40), (32, 40), (25, 25)], fill=SILVER)
    # inside lines
    draw.line([20, 14, 30, 14], fill=STEEL, width=1)

# 20. Muddler
def draw_muddler(draw):
    # wooden cocktail muddler with teeth at bottom
    draw.rounded_rectangle([20, 6, 30, 40], radius=4, fill=BROWN)
    # grid teeth at bottom
    draw.rectangle([20, 40, 30, 45], fill=DARK)
    for x in range(21, 30, 3):
        draw.line([x, 40, x, 45], fill=BROWN, width=1)

# 21. Cocktail Strainer
def draw_cocktail_strainer(draw):
    draw.rounded_rectangle([8, 26, 16, 46], radius=3, fill=SILVER) # handle
    # strainer disk with spring coil around it
    draw.ellipse([16, 10, 40, 34], fill=SILVER)
    draw.ellipse([18, 12, 38, 32], fill=STEEL)
    draw.arc([16, 10, 40, 34], 0, 360, fill=WHITE, width=2) # spring coil representation

# 22. Bottle Stopper
def draw_bottle_stopper(draw):
    # cork bottom
    draw.rounded_rectangle([20, 24, 30, 44], radius=3, fill=TAN)
    # decorative top
    draw.ellipse([16, 8, 34, 24], fill=RED)
    draw.ellipse([20, 12, 30, 20], fill=HIGHLIGHT)

# 23. Wine Decanter
def draw_wine_decanter(draw):
    # wide bottom glass decanter
    draw.ellipse([10, 22, 40, 46], fill=GLASS)
    # red wine inside
    draw.chord([12, 28, 38, 44], 0, 180, fill=DKRED)
    # neck
    draw.polygon([(20, 10), (30, 10), (26, 24), (24, 24)], fill=GLASS)

# 24. Wine Aerator
def draw_wine_aerator(draw):
    # clear acrylic tube funnel
    draw.polygon([(16, 12), (34, 12), (28, 34), (22, 34)], fill=GLASS)
    draw.polygon([(18, 14), (32, 14), (26, 32), (24, 32)], fill=HIGHLIGHT)
    # internal valves
    draw.line([22, 22, 28, 22], fill=DARK, width=2)

# 25. Wine Cooler
def draw_wine_cooler(draw):
    # metallic cylinder with wine bottle neck sticking out
    draw.rounded_rectangle([14, 22, 36, 46], radius=4, fill=SILVER)
    draw.rounded_rectangle([16, 24, 34, 44], radius=3, fill=STEEL)
    # wine bottle neck
    draw.rectangle([22, 10, 28, 22], fill=DKGREEN)
    draw.ellipse([22, 8, 28, 12], fill=RED)

# 26. Champagne Stopper
def draw_champagne_stopper(draw):
    # heavy metal pressure cap
    draw.rounded_rectangle([16, 12, 34, 24], radius=4, fill=SILVER)
    # clamp wings
    draw.line([16, 22, 12, 38], fill=STEEL, width=3)
    draw.line([34, 22, 38, 38], fill=STEEL, width=3)

# 27. Beer Mug
def draw_beer_mug(draw):
    # glass mug
    draw.rounded_rectangle([12, 16, 34, 44], radius=4, fill=GLASS)
    # golden beer level & foam
    draw.rectangle([14, 22, 32, 42], fill=ORANGE)
    draw.rounded_rectangle([12, 14, 34, 22], radius=4, fill=WHITE)
    # handle
    draw.arc([30, 22, 44, 38], 300, 60, fill=WHITE, width=4)

# 28. Shot Glass
def draw_shot_glass(draw):
    draw.polygon([(16, 14), (34, 14), (31, 44), (19, 44)], fill=GLASS)
    # heavy base
    draw.rectangle([19, 38, 31, 44], fill=HIGHLIGHT)
    # green liquid
    draw.polygon([(18, 24), (32, 24), (30, 38), (20, 38)], fill=GREEN)

# 29. Whiskey Stones
def draw_whiskey_stones(draw):
    # 3 grey cubes stacked
    draw.rounded_rectangle([18, 24, 32, 38], radius=2, fill=GREY)
    draw.rounded_rectangle([24, 14, 38, 28], radius=2, fill=DARK)
    draw.rounded_rectangle([10, 16, 24, 30], radius=2, fill=STEEL)

# 30. Pocket Flask
def draw_flask(draw):
    # curved metal flask
    draw.rounded_rectangle([12, 16, 38, 44], radius=6, fill=SILVER)
    # texture line
    draw.arc([10, 16, 40, 44], 180, 360, fill=STEEL, width=2)
    # screw cap
    draw.rectangle([22, 10, 28, 16], fill=STEEL)

# 31. Tea Caddy
def draw_tea_caddy(draw):
    # metal storage tin
    draw.rounded_rectangle([14, 14, 36, 44], radius=3, fill=DKGREEN)
    draw.rounded_rectangle([14, 12, 36, 18], radius=2, fill=DKBLUE)
    # gold label
    draw.rectangle([18, 24, 32, 34], fill=YELLOW)

# 32. Coffee Canister
def draw_coffee_canister(draw):
    draw.rounded_rectangle([14, 14, 36, 44], radius=4, fill=DARK)
    # metal clamp latch
    draw.line([36, 20, 40, 20], fill=SILVER, width=2)
    draw.line([40, 20, 40, 30], fill=SILVER, width=2)
    # brown bean label
    draw.ellipse([21, 24, 29, 32], fill=BROWN)

# 33. Sugar Bowl
def draw_sugar_bowl(draw):
    # ceramic bowl with handles
    draw.ellipse([12, 18, 38, 42], fill=CREAM)
    # lid
    draw.ellipse([14, 12, 36, 20], fill=WHITE)
    draw.ellipse([22, 8, 28, 14], fill=BROWN)
    # handle ears
    draw.arc([6, 22, 14, 34], 90, 270, fill=CREAM, width=3)
    draw.arc([36, 22, 44, 34], 270, 90, fill=CREAM, width=3)

# 34. Cream Pitcher
def draw_cream_pitcher(draw):
    draw.rounded_rectangle([16, 20, 36, 44], radius=4, fill=WHITE)
    # pour spout
    draw.polygon([(16, 20), (10, 16), (20, 20)], fill=WHITE)
    # handle
    draw.arc([32, 24, 42, 38], 300, 60, fill=WHITE, width=3)

# 35. Tea Tray (Gongfu)
def draw_tea_tray(draw):
    # wooden rectangular tray
    draw.rounded_rectangle([6, 24, 44, 40], radius=4, fill=BROWN)
    # slats
    for x in range(12, 40, 6):
        draw.line([x, 26, x, 38], fill=DARK, width=2)

# 36. Tea Timer
def draw_tea_timer(draw):
    # 3 small hourglasses side by side
    draw.rounded_rectangle([10, 12, 40, 38], radius=2, fill=BROWN)
    # timers
    for x, color in [(14, RED), (25, YELLOW), (36, GREEN)]:
        draw.polygon([(x-3, 16), (x+3, 16), (x, 25)], fill=color)
        draw.polygon([(x-3, 34), (x+3, 34), (x, 25)], fill=color)

# 37. Coffee Grinder
def draw_coffee_grinder(draw):
    # wooden box
    draw.rounded_rectangle([14, 22, 36, 44], radius=4, fill=BROWN)
    # metal hopper
    draw.polygon([(16, 22), (34, 22), (28, 16), (22, 16)], fill=STEEL)
    # hand crank handle
    draw.line([25, 16, 38, 10], fill=SILVER, width=2)
    draw.ellipse([36, 7, 40, 13], fill=BROWN)

# 38. Milk Frother
def draw_milk_frother(draw):
    draw.rounded_rectangle([20, 6, 30, 26], radius=4, fill=BLACK) # handle
    # wand
    draw.line([25, 26, 25, 42], fill=SILVER, width=2)
    # frothing ring
    draw.ellipse([22, 40, 28, 46], fill=SILVER)

# 39. French Press
def draw_french_press(draw):
    draw.rounded_rectangle([14, 14, 36, 44], radius=4, fill=GLASS)
    draw.rectangle([16, 24, 34, 42], fill=BROWN) # coffee level
    # metal frame
    draw.line([14, 14, 14, 44], fill=SILVER, width=2)
    draw.line([14, 44, 36, 44], fill=SILVER, width=2)
    # plunger knob
    draw.line([25, 6, 25, 14], fill=STEEL, width=2)
    draw.ellipse([22, 3, 28, 9], fill=DARK)

# 40. Pour Over Cone
def draw_pour_over_cone(draw):
    # ceramic filter cone
    draw.polygon([(12, 12), (38, 12), (28, 34), (22, 34)], fill=WHITE)
    # ring stand base
    draw.ellipse([14, 32, 36, 38], fill=WHITE)
    # paper filter inside
    draw.polygon([(14, 14), (36, 14), (25, 30)], fill=CREAM)

# 41. Gooseneck Kettle
def draw_gooseneck_kettle(draw):
    draw.ellipse([12, 22, 38, 44], fill=DARK)
    # gooseneck spout
    draw.arc([6, 12, 20, 36], 90, 270, fill=DARK, width=3)
    # handle loop
    draw.arc([30, 22, 42, 40], 300, 60, fill=DARK, width=4)
    # lid knob
    draw.ellipse([22, 14, 28, 20], fill=STEEL)

# 42. Digital Timer
def draw_digital_timer(draw):
    draw.rounded_rectangle([10, 14, 40, 38], radius=4, fill=WHITE)
    # LCD display
    draw.rounded_rectangle([14, 18, 36, 28], radius=2, fill=GREEN)
    # Simple segments for 00:00
    draw.point((25, 22), fill=DKGREEN)
    draw.point((25, 24), fill=DKGREEN)
    draw.rectangle([17, 20, 20, 26], outline=DKGREEN, fill=(255,255,255,0))
    draw.rectangle([21, 20, 24, 26], outline=DKGREEN, fill=(255,255,255,0))
    draw.rectangle([26, 20, 29, 26], outline=DKGREEN, fill=(255,255,255,0))
    draw.rectangle([30, 20, 33, 26], outline=DKGREEN, fill=(255,255,255,0))
    # buttons
    draw.ellipse([16, 31, 20, 35], fill=RED)
    draw.ellipse([30, 31, 34, 35], fill=BLUE)

# 43. Recipe Holder
def draw_recipe_holder(draw):
    # easel back
    draw.line([25, 14, 16, 42], fill=BROWN, width=3)
    # front ledge
    draw.rounded_rectangle([10, 14, 40, 38], radius=2, fill=TAN)
    draw.rectangle([8, 36, 42, 40], fill=BROWN)

# 44. Cork Trivet
def draw_trivet_cork(draw):
    # circular cork pad
    draw.ellipse([8, 8, 42, 42], fill=TAN)
    # speckled pattern
    for x in range(12, 40, 4):
        for y in range(12, 40, 4):
            draw.point((x, y), fill=BROWN)

# 45. Pinch Bowls
def draw_pinch_bowls(draw):
    # 3 small bowls nested/layered
    draw.ellipse([6, 22, 24, 40], fill=RED)
    draw.ellipse([26, 22, 44, 40], fill=BLUE)
    draw.ellipse([16, 14, 34, 32], fill=YELLOW)

# 46. Toothpick Holder
def draw_toothpick_holder(draw):
    draw.rounded_rectangle([16, 18, 34, 44], radius=3, fill=GLASS)
    # toothpicks sticking out
    for x in range(19, 32, 3):
        draw.line([x, 10, x, 30], fill=TAN, width=1)

# 47. Slate Coaster
def draw_coaster(draw):
    draw.rounded_rectangle([10, 20, 40, 40], radius=3, fill=DARK)
    # texture scratches
    draw.line([14, 24, 36, 36], fill=STEEL, width=1)

# 48. Napkin Holder
def draw_napkin_holder(draw):
    # metal rack with napkins inside
    draw.polygon([(10, 14), (25, 34), (40, 14)], fill=WHITE) # folded napkins
    # metal loop holding them
    draw.arc([14, 20, 36, 44], 180, 360, fill=SILVER, width=3)

# 49. Dish Brush
def draw_dish_brush(draw):
    draw.rounded_rectangle([20, 6, 30, 32], radius=4, fill=TAN)
    # round bristle head
    draw.ellipse([14, 30, 36, 46], fill=CREAM)
    for x in range(16, 36, 4):
        draw.line([x, 34, x, 44], fill=BROWN, width=2)

# 50. Lemon Squeezer
def draw_lemon_squeezer(draw):
    # hinged metal squeezer
    draw.rounded_rectangle([4, 18, 26, 24], radius=3, fill=YELLOW)
    # hinge
    draw.ellipse([22, 22, 28, 28], fill=STEEL)
    # handles
    draw.line([25, 25, 46, 28], fill=SILVER, width=3)
    draw.line([25, 21, 46, 18], fill=SILVER, width=3)

# Build all 50 items
items = [
    ("egg_slicer", draw_egg_slicer),
    ("oil_sprayer", draw_oil_sprayer),
    ("dough_scraper", draw_dough_scraper),
    ("flour_sifter", draw_flour_sifter),
    ("garlic_grater", draw_garlic_grater),
    ("potato_masher", draw_potato_masher),
    ("basting_bulb", draw_basting_bulb),
    ("meat_thermometer", draw_meat_thermometer),
    ("herb_stripper", draw_herb_stripper),
    ("jar_opener", draw_jar_opener),
    ("melon_slicer", draw_melon_slicer),
    ("avocado_slicer", draw_avocado_slicer),
    ("salad_tongs", draw_salad_tongs),
    ("butter_crock", draw_butter_crock),
    ("honey_pot", draw_honey_pot),
    ("salt_cellar", draw_salt_cellar),
    ("ice_bucket", draw_ice_bucket),
    ("cocktail_shaker", draw_cocktail_shaker),
    ("jigger", draw_jigger),
    ("muddler", draw_muddler),
    ("cocktail_strainer", draw_cocktail_strainer),
    ("bottle_stopper", draw_bottle_stopper),
    ("wine_decanter", draw_wine_decanter),
    ("wine_aerator", draw_wine_aerator),
    ("wine_cooler", draw_wine_cooler),
    ("champagne_stopper", draw_champagne_stopper),
    ("beer_mug", draw_beer_mug),
    ("shot_glass", draw_shot_glass),
    ("whiskey_stones", draw_whiskey_stones),
    ("flask", draw_flask),
    ("tea_caddy", draw_tea_caddy),
    ("coffee_canister", draw_coffee_canister),
    ("sugar_bowl", draw_sugar_bowl),
    ("cream_pitcher", draw_cream_pitcher),
    ("tea_tray", draw_tea_tray),
    ("tea_timer", draw_tea_timer),
    ("coffee_grinder", draw_coffee_grinder),
    ("milk_frother", draw_milk_frother),
    ("french_press", draw_french_press),
    ("pour_over_cone", draw_pour_over_cone),
    ("gooseneck_kettle", draw_gooseneck_kettle),
    ("digital_timer", draw_digital_timer),
    ("recipe_holder", draw_recipe_holder),
    ("trivet_cork", draw_trivet_cork),
    ("pinch_bowls", draw_pinch_bowls),
    ("toothpick_holder", draw_toothpick_holder),
    ("coaster", draw_coaster),
    ("napkin_holder", draw_napkin_holder),
    ("dish_brush", draw_dish_brush),
    ("lemon_squeezer", draw_lemon_squeezer)
]

print(f"Generating {len(items)} new kitchen sprites in '{OUTPUT_DIR}'...")
for name, func in items:
    create_sprite(name, func)
print("\nAll 50 new kitchen sprites generated successfully!")
