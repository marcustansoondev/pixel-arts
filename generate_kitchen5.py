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
PINK      = (230, 130, 150, 255)
PURPLE    = (130,  70, 190, 255)
GREY      = (160, 160, 165, 255)

# 1. Garlic Roaster
def draw_garlic_roaster(draw):
    draw.ellipse([10, 18, 40, 44], fill=TAN)
    # terra cotta lid dome
    draw.chord([12, 12, 38, 32], 180, 360, fill=ORANGE)
    draw.ellipse([21, 8, 29, 14], fill=DKRED)

# 2. Whistling Tea Kettle
def draw_tea_kettle_whistling(draw):
    draw.ellipse([10, 18, 40, 44], fill=ORANGE) # copper body
    # whistling spout
    draw.line([(12, 22), (2, 14)], fill=STEEL, width=4)
    # top loop handle
    draw.arc([14, 8, 36, 26], 180, 360, fill=DARK, width=4)

# 3. Slat Wooden Trivet
def draw_trivet_wooden(draw):
    draw.rounded_rectangle([8, 12, 42, 38], radius=4, fill=BROWN)
    # slots/slats
    for x in range(14, 38, 6):
        draw.line([x, 16, x, 34], fill=DARK, width=2)

# 4. Cake Tester
def draw_cake_tester(draw):
    # long thin metal pin
    draw.line([25, 14, 25, 46], fill=SILVER, width=2)
    # decorative plastic loop handle at top
    draw.ellipse([18, 4, 32, 16], fill=PINK)
    draw.ellipse([21, 7, 29, 13], fill=(0,0,0,0))

# 5. Pot Scraper
def draw_pot_scraper(draw):
    # small red plastic scraping card with curves
    draw.rounded_rectangle([10, 12, 40, 38], radius=6, fill=RED)
    draw.line([12, 14, 38, 14], fill=DKRED, width=3)

# 6. Ceramic Oil Cruet
def draw_oil_cruet(draw):
    draw.rounded_rectangle([16, 18, 34, 44], radius=5, fill=BLUE)
    draw.rectangle([21, 10, 29, 18], fill=BLUE)
    # silver metal long thin spout
    draw.arc([16, 4, 25, 12], 90, 270, fill=SILVER, width=2)

# 7. Collapsible Funnel
def draw_funnel_collapsible(draw):
    # silicone steps
    draw.polygon([(10, 12), (40, 12), (32, 22), (18, 22)], fill=GREEN)
    draw.polygon([(18, 22), (32, 22), (28, 32), (22, 32)], fill=DKGREEN)
    draw.rectangle([22, 32, 28, 42], fill=GREEN)

# 8. Spoon Rest
def draw_spoon_rest(draw):
    # shallow oval ceramic rest
    draw.ellipse([14, 12, 36, 42], fill=CREAM)
    draw.ellipse([16, 14, 34, 40], fill=WHITE)
    # blue rim pattern
    draw.arc([14, 12, 36, 42], 0, 360, fill=BLUE, width=1)

# 9. Bag Clip
def draw_bag_clip(draw):
    # plastic spring clip
    draw.rounded_rectangle([12, 18, 38, 28], radius=3, fill=RED)
    # hinge clamp lines
    draw.line([25, 18, 25, 28], fill=DKRED, width=3)

# 10. Egg Counter Rack
def draw_egg_rack(draw):
    # wooden frame rack
    draw.rounded_rectangle([8, 14, 42, 40], radius=4, fill=BROWN)
    # circles with white eggs sitting inside
    for ex, ey in [(15, 20), (25, 20), (35, 20), (15, 30), (25, 30), (35, 30)]:
        draw.ellipse([ex-4, ey-4, ex+4, ey+4], fill=WHITE)

# 11. Kitchen Shears
def draw_kitchen_shears(draw):
    # crossed blades
    draw.line([14, 10, 28, 30], fill=SILVER, width=3)
    draw.line([36, 10, 22, 30], fill=SILVER, width=3)
    # black handles
    draw.ellipse([8, 30, 20, 42], fill=BLACK)
    draw.ellipse([11, 33, 17, 39], fill=(0,0,0,0))
    draw.ellipse([30, 30, 42, 42], fill=BLACK)
    draw.ellipse([33, 33, 39, 39], fill=(0,0,0,0))

# 12. Poultry Shears
def draw_poultry_shears(draw):
    # curved blades
    draw.arc([14, 10, 36, 32], 200, 340, fill=SILVER, width=3)
    # metal spring handle latch
    draw.line([16, 32, 22, 46], fill=STEEL, width=3)
    draw.line([34, 32, 28, 46], fill=STEEL, width=3)

# 13. Meat Claws
def draw_meat_claws(draw):
    # shredder claw with sharp spikes
    draw.rounded_rectangle([10, 10, 40, 20], radius=3, fill=BLACK) # handle loop
    # claws
    for x in range(12, 40, 5):
        draw.polygon([(x, 20), (x+3, 20), (x+1, 38)], fill=SILVER)

# 14. Fish Scaler
def draw_fish_scaler(draw):
    draw.rounded_rectangle([21, 26, 29, 48], radius=3, fill=BROWN) # wood handle
    draw.line([25, 18, 25, 26], fill=STEEL, width=3)
    # jagged scaler head
    draw.rectangle([16, 10, 34, 18], fill=SILVER)
    for x in range(17, 34, 4):
        draw.polygon([(x, 10), (x+2, 10), (x+1, 6)], fill=SILVER)

# 15. Apple Corer
def draw_apple_corer(draw):
    draw.rounded_rectangle([12, 8, 38, 14], radius=3, fill=BLACK) # handle
    draw.line([25, 14, 25, 34], fill=SILVER, width=4) # shaft
    # hollow circle tip
    draw.ellipse([21, 34, 29, 42], fill=SILVER)
    draw.ellipse([23, 36, 27, 40], fill=(0,0,0,0))

# 16. Pineapple Corer
def draw_pineapple_corer(draw):
    draw.rounded_rectangle([12, 6, 38, 12], radius=3, fill=BLACK) # handle
    draw.line([25, 12, 25, 36], fill=SILVER, width=4) # shaft
    # spiral blades at bottom
    draw.ellipse([16, 34, 34, 44], fill=YELLOW)
    draw.arc([16, 34, 34, 44], 0, 360, fill=STEEL, width=2)

# 17. Olive Spoon
def draw_olive_spoon(draw):
    # long thin handle, tiny bowl with drain holes
    draw.line([25, 10, 25, 36], fill=SILVER, width=2)
    draw.ellipse([18, 34, 32, 46], fill=SILVER)
    draw.ellipse([20, 36, 30, 44], fill=STEEL)
    # holes
    draw.point((23, 40), fill=(0,0,0,0))
    draw.point((27, 40), fill=(0,0,0,0))

# 18. Cheese Slicer / Plane
def draw_cheese_slicer(draw):
    draw.rounded_rectangle([22, 28, 28, 48], radius=3, fill=BLACK) # handle
    # flat shovel blade with central slot
    draw.polygon([(16, 12), (34, 12), (28, 28), (22, 28)], fill=SILVER)
    draw.line([20, 18, 30, 18], fill=(0,0,0,0), width=2) # slot

# 19. Cheese Wire Board
def draw_cheese_wire(draw):
    draw.rounded_rectangle([8, 18, 42, 42], radius=4, fill=TAN)
    # metal cutting wire arm
    draw.arc([10, 10, 40, 28], 180, 360, fill=SILVER, width=2)
    draw.line([25, 18, 25, 42], fill=STEEL, width=1) # wire slot

# 20. Danish Dough Whisk
def draw_dough_whisk(draw):
    draw.rounded_rectangle([22, 28, 28, 48], radius=3, fill=BROWN) # wooden handle
    # looping wire rings
    draw.ellipse([14, 10, 36, 32], fill=(0,0,0,0), outline=SILVER, width=2)
    draw.ellipse([18, 14, 32, 28], fill=(0,0,0,0), outline=SILVER, width=2)
    draw.ellipse([22, 18, 28, 24], fill=(0,0,0,0), outline=SILVER, width=2)

# 21. Pastry Blender
def draw_pastry_blender(draw):
    draw.rounded_rectangle([14, 8, 36, 15], radius=3, fill=BROWN) # handle
    # parallel wire blades
    for x in [16, 20, 24, 28, 32, 34]:
        draw.arc([x-4, 14, x+4, 40], 0, 180, fill=SILVER, width=2)

# 22. Bowl Scraper
def draw_bowl_scraper(draw):
    # half-circle flexible plastic scraper card
    draw.chord([10, 12, 40, 42], 0, 180, fill=BLUE)
    draw.line([10, 27, 40, 27], fill=DKBLUE, width=3)

# 23. Pie Weights
def draw_pie_weights(draw):
    # jar with tiny round ceramic beads
    draw.rounded_rectangle([14, 16, 36, 44], radius=4, fill=GLASS)
    # beads
    for bx in range(18, 34, 4):
        for by in range(24, 42, 4):
            draw.ellipse([bx-1, by-1, bx+1, by+1], fill=CREAM)
    # red lid
    draw.rounded_rectangle([16, 12, 34, 18], radius=2, fill=RED)

# 24. Pie Bird
def draw_pie_bird(draw):
    # ceramic pie chimney bird shape
    draw.ellipse([16, 20, 34, 42], fill=WHITE)
    draw.polygon([(16, 24), (10, 20), (16, 30)], fill=WHITE) # beak
    draw.ellipse([22, 12, 28, 20], fill=WHITE) # head

# 25. Pie Crust Shield
def draw_pie_crust_shield(draw):
    # hollow metal ring protector
    draw.ellipse([8, 8, 42, 42], fill=SILVER)
    draw.ellipse([14, 14, 36, 36], fill=(0,0,0,0))
    # shield segments
    for angle in range(0, 360, 45):
        draw.arc([8, 8, 42, 42], angle, angle+20, fill=STEEL, width=2)

# 26. Cake Leveler
def draw_cake_leveler(draw):
    # large metal arch frame with thin wire stretching across
    draw.arc([6, 10, 44, 44], 180, 360, fill=SILVER, width=3)
    # wire
    draw.line([6, 36, 44, 36], fill=STEEL, width=1)

# 27. Icing Spatula
def draw_icing_spatula(draw):
    # offset metal palette knife
    draw.rounded_rectangle([4, 28, 16, 36], radius=2, fill=BROWN) # handle
    # bent metal blade
    draw.line([16, 32, 24, 24], fill=SILVER, width=2)
    draw.rounded_rectangle([24, 18, 46, 24], radius=1, fill=SILVER)

# 28. Cake Scraper
def draw_cake_scraper(draw):
    # tall metal card with serrated details
    draw.rectangle([14, 8, 36, 42], fill=SILVER)
    # serrated side teeth
    for y in range(12, 40, 4):
        draw.polygon([(36, y), (36, y+2), (40, y+1)], fill=SILVER)

# 29. Cookie Scoop
def draw_cookie_scoop(draw):
    # scoop with sweeping release lever inside
    draw.rounded_rectangle([4, 22, 26, 28], radius=3, fill=SILVER)
    draw.ellipse([24, 16, 42, 34], fill=SILVER)
    draw.ellipse([26, 18, 40, 32], fill=STEEL)
    # sweeping bar
    draw.line([33, 18, 33, 32], fill=YELLOW, width=2)

# 30. Biscuit Cutter
def draw_biscuit_cutter(draw):
    draw.ellipse([10, 16, 40, 44], fill=SILVER)
    draw.ellipse([12, 18, 38, 42], fill=(0,0,0,0))
    # handle loop over the top
    draw.arc([10, 8, 40, 24], 180, 360, fill=STEEL, width=3)

# 31. Rolling Mat
def draw_rolling_mat(draw):
    # silicone mat with circle target guides
    draw.rounded_rectangle([6, 14, 44, 38], radius=2, fill=CREAM)
    # circle target
    draw.ellipse([16, 18, 34, 34], fill=(0,0,0,0), outline=RED, width=1)

# 32. Pizza Stone
def draw_pizza_stone(draw):
    draw.ellipse([8, 8, 42, 42], fill=TAN)
    draw.ellipse([10, 10, 40, 40], fill=CREAM)
    # speckles
    for x in [16, 32, 20, 28]:
        draw.point((x, x), fill=BROWN)

# 33. Pizza Peel
def draw_pizza_peel(draw):
    # wooden flat paddle
    draw.line([6, 44, 22, 28], fill=BROWN, width=4) # handle
    draw.ellipse([16, 10, 42, 32], fill=TAN)

# 34. Wool Ball Trivet
def draw_trivet_wool(draw):
    # colorful round felt balls
    for bx, by, color in [(16, 16, RED), (25, 14, BLUE), (34, 16, GREEN), (14, 25, YELLOW), (25, 25, PINK), (36, 25, PURPLE), (16, 34, ORANGE), (25, 36, RED), (34, 34, BLUE)]:
        draw.ellipse([bx-4, by-4, bx+4, by+4], fill=color)

# 35. Bamboo Trivet
def draw_trivet_bamboo(draw):
    draw.rounded_rectangle([8, 8, 42, 42], radius=4, fill=TAN)
    # lattice lines
    for x in range(12, 40, 6):
        draw.line([x, 10, x, 40], fill=BROWN, width=2)
        draw.line([10, x, 40, x], fill=BROWN, width=2)

# 36. Pan Protectors
def draw_pan_protectors(draw):
    # star shaped separator pad
    draw.polygon([(25, 6), (29, 20), (42, 20), (32, 28), (38, 42), (25, 34), (12, 42), (18, 28), (8, 20), (21, 20)], fill=GREEN)

# 37. Bag Sealer
def draw_bag_sealer(draw):
    # handheld stapler-like tool
    draw.rounded_rectangle([10, 18, 40, 28], radius=3, fill=WHITE)
    draw.rounded_rectangle([10, 28, 40, 34], radius=2, fill=STEEL)
    # teal seal button
    draw.ellipse([30, 14, 36, 20], fill=BLUE)

# 38. Yogurt Maker
def draw_yogurt_maker(draw):
    draw.rounded_rectangle([10, 16, 40, 44], radius=5, fill=WHITE)
    # clear lid
    draw.ellipse([12, 10, 38, 18], fill=GLASS)
    # little glass jars inside
    for x in [16, 25, 34]:
        draw.rectangle([x-2, 22, x+2, 36], fill=GLASS)

# 39. Soda Maker
def draw_soda_maker(draw):
    # carbonator column
    draw.rounded_rectangle([16, 8, 34, 44], radius=4, fill=DARK)
    # bottle nested inside
    draw.rounded_rectangle([20, 20, 30, 42], radius=3, fill=GLASS)
    draw.chord([20, 26, 30, 42], 0, 180, fill=BLUE) # carbonated water

# 40. Ice Crusher
def draw_ice_crusher(draw):
    draw.rounded_rectangle([14, 18, 36, 44], radius=4, fill=STEEL)
    # chrome handle crank on side
    draw.line([36, 26, 44, 26], fill=SILVER, width=3)
    draw.line([44, 26, 44, 14], fill=SILVER, width=2)
    # red grip knob
    draw.ellipse([42, 11, 46, 17], fill=RED)

# 41. Wooden Salad Bowl
def draw_salad_bowl(draw):
    # large wooden bowl filled with green salad
    draw.ellipse([8, 16, 42, 42], fill=BROWN)
    draw.ellipse([10, 18, 40, 40], fill=GREEN)
    # red tomato slices
    draw.ellipse([18, 24, 22, 28], fill=RED)
    draw.ellipse([28, 28, 32, 32], fill=RED)

# 42. Salad Servers
def draw_salad_servers(draw):
    # pair of large spoons crossed
    draw.line([12, 10, 28, 38], fill=BROWN, width=3)
    draw.line([38, 10, 22, 38], fill=BROWN, width=3)
    # spoon heads
    draw.ellipse([24, 34, 32, 44], fill=BROWN)
    draw.ellipse([18, 34, 26, 44], fill=BROWN)

# 43. Butter Spreader
def draw_butter_spreader(draw):
    # small rounded knife
    draw.rounded_rectangle([6, 28, 18, 36], radius=2, fill=BROWN) # handle
    draw.line([18, 32, 44, 32], fill=SILVER, width=3) # blunt blade

# 44. Honey Jar
def draw_honey_jar(draw):
    draw.rounded_rectangle([14, 18, 36, 44], radius=4, fill=GLASS)
    draw.rounded_rectangle([16, 22, 34, 42], radius=3, fill=YELLOW) # honey
    # lid with notch
    draw.rounded_rectangle([16, 12, 34, 18], radius=2, fill=BROWN)

# 45. Salt Grinder / Mill
def draw_salt_grinder(draw):
    # acrylic clear body showing white crystals
    draw.rounded_rectangle([16, 14, 34, 44], radius=3, fill=GLASS)
    # white salt crystals inside
    for x in range(18, 32, 3):
        for y in range(24, 42, 4):
            draw.point((x, y), fill=WHITE)
    # top adjustment cap
    draw.rectangle([20, 8, 30, 14], fill=STEEL)

# 46. Oil Can (Long Snout)
def draw_oil_can(draw):
    draw.ellipse([14, 22, 36, 44], fill=STEEL)
    # long curved snout
    draw.arc([4, 10, 22, 34], 90, 270, fill=SILVER, width=2)
    # handle loop
    draw.arc([30, 22, 42, 40], 300, 60, fill=STEEL, width=3)

# 47. Bottle Capper
def draw_bottle_capper(draw):
    # red twin-lever hand capper tool
    draw.line([12, 14, 38, 14], fill=RED, width=4) # top bar
    draw.line([16, 14, 16, 42], fill=RED, width=3) # left arm
    draw.line([34, 14, 34, 42], fill=RED, width=3) # right arm
    # central bell cup
    draw.rectangle([21, 14, 29, 24], fill=STEEL)

# 50. Ice Scoop
def draw_ice_scoop(draw):
    draw.rounded_rectangle([6, 20, 20, 28], radius=2, fill=BROWN) # wood handle
    # metal scoop shovel bowl
    draw.polygon([(18, 14), (44, 10), (44, 38), (18, 34)], fill=SILVER)
    draw.polygon([(20, 16), (42, 12), (42, 36), (20, 32)], fill=STEEL)

# 48. Wine Rack
def draw_wine_rack(draw):
    # wooden frame displaying bottles
    draw.rounded_rectangle([6, 14, 44, 40], radius=4, fill=BROWN)
    # bottle slots/necks
    draw.ellipse([14, 22, 22, 30], fill=DKGREEN)
    draw.ellipse([28, 22, 36, 30], fill=DKGREEN)

# 49. Wine Thermometer
def draw_wine_thermometer(draw):
    # metal snap band with digital display
    draw.arc([10, 12, 40, 42], 0, 360, fill=SILVER, width=4)
    # display box
    draw.rectangle([18, 18, 32, 26], fill=BLACK)
    # Draw digital red segments for '16'
    # Digit 1 (line for '1')
    draw.line([(21, 20), (21, 24)], fill=RED, width=1)
    # Digit 6 (simple block/loop)
    draw.rectangle([25, 20, 28, 24], outline=RED, fill=(0,0,0,0))
    draw.line([(25, 20), (25, 24)], fill=RED, width=1)

# Build all 50 items
items = [
    ("garlic_roaster", draw_garlic_roaster),
    ("tea_kettle_whistling", draw_tea_kettle_whistling),
    ("trivet_wooden", draw_trivet_wooden),
    ("cake_tester", draw_cake_tester),
    ("pot_scraper", draw_pot_scraper),
    ("oil_cruet", draw_oil_cruet),
    ("funnel_collapsible", draw_funnel_collapsible),
    ("spoon_rest", draw_spoon_rest),
    ("bag_clip", draw_bag_clip),
    ("egg_rack", draw_egg_rack),
    ("kitchen_shears", draw_kitchen_shears),
    ("poultry_shears", draw_poultry_shears),
    ("meat_claws", draw_meat_claws),
    ("fish_scaler", draw_fish_scaler),
    ("apple_corer", draw_apple_corer),
    ("pineapple_corer", draw_pineapple_corer),
    ("olive_spoon", draw_olive_spoon),
    ("cheese_slicer", draw_cheese_slicer),
    ("cheese_wire", draw_cheese_wire),
    ("dough_whisk", draw_dough_whisk),
    ("pastry_blender", draw_pastry_blender),
    ("bowl_scraper", draw_bowl_scraper),
    ("pie_weights", draw_pie_weights),
    ("pie_bird", draw_pie_bird),
    ("pie_crust_shield", draw_pie_crust_shield),
    ("cake_leveler", draw_cake_leveler),
    ("icing_spatula", draw_icing_spatula),
    ("cake_scraper", draw_cake_scraper),
    ("cookie_scoop", draw_cookie_scoop),
    ("biscuit_cutter", draw_biscuit_cutter),
    ("rolling_mat", draw_rolling_mat),
    ("pizza_stone", draw_pizza_stone),
    ("pizza_peel", draw_pizza_peel),
    ("trivet_wool", draw_trivet_wool),
    ("trivet_bamboo", draw_trivet_bamboo),
    ("pan_protectors", draw_pan_protectors),
    ("bag_sealer", draw_bag_sealer),
    ("yogurt_maker", draw_yogurt_maker),
    ("soda_maker", draw_soda_maker),
    ("ice_crusher", draw_ice_crusher),
    ("salad_bowl", draw_salad_bowl),
    ("salad_servers", draw_salad_servers),
    ("butter_spreader", draw_butter_spreader),
    ("honey_jar", draw_honey_jar),
    ("salt_grinder", draw_salt_grinder),
    ("oil_can", draw_oil_can),
    ("bottle_capper", draw_bottle_capper),
    ("wine_rack", draw_wine_rack),
    ("wine_thermometer", draw_wine_thermometer),
    ("ice_scoop", draw_ice_scoop)
]

print(f"Generating {len(items)} new kitchen sprites in '{OUTPUT_DIR}'...")
for name, func in items:
    create_sprite(name, func)
print("\nAll 50 new kitchen sprites generated successfully!")
