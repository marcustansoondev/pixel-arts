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

# 1. Microwave
def draw_microwave(draw):
    draw.rounded_rectangle([6, 12, 44, 38], radius=3, fill=DARK)
    draw.rounded_rectangle([8, 14, 32, 36], radius=2, fill=GLASS)
    # keypad & knob
    draw.rectangle([34, 14, 42, 36], fill=STEEL)
    draw.ellipse([36, 16, 40, 20], fill=WHITE)
    draw.ellipse([37, 26, 39, 28], fill=YELLOW)

# 2. Coffee Maker
def draw_coffee_maker(draw):
    # main machine body
    draw.rounded_rectangle([14, 10, 36, 42], radius=4, fill=DARK)
    draw.rectangle([16, 22, 34, 38], fill=(0,0,0,0))
    # glass pot
    draw.ellipse([18, 24, 32, 38], fill=GLASS)
    draw.chord([18, 28, 32, 38], 0, 180, fill=BROWN) # coffee level
    draw.line([(28, 22), (28, 24)], fill=STEEL, width=2) # drip spout

# 3. Espresso Machine
def draw_espresso_machine(draw):
    draw.rounded_rectangle([10, 8, 40, 44], radius=4, fill=STEEL)
    draw.rectangle([12, 22, 38, 38], fill=DARK)
    # cup
    draw.rounded_rectangle([20, 32, 30, 38], radius=2, fill=WHITE)
    draw.line([25, 22, 25, 30], fill=BROWN, width=2) # drip coffee stream

# 4. Tea Infuser
def draw_tea_infuser(draw):
    draw.line([(25, 6), (25, 28)], fill=SILVER, width=2)
    # ball
    draw.ellipse([18, 26, 32, 40], fill=SILVER)
    draw.ellipse([20, 28, 30, 38], fill=STEEL)

# 5. Garbage Can
def draw_garbage_can(draw):
    draw.polygon([(12, 16), (38, 16), (34, 44), (16, 44)], fill=STEEL)
    # lid
    draw.ellipse([10, 12, 40, 18], fill=DARK)
    # pedal
    draw.rectangle([21, 44, 29, 47], fill=DARK)

# 6. Paper Towel Holder
def draw_paper_towel_holder(draw):
    draw.rectangle([23, 10, 27, 44], fill=BROWN)
    # paper roll
    draw.rounded_rectangle([14, 14, 36, 42], radius=4, fill=WHITE)
    draw.ellipse([14, 12, 36, 18], fill=CREAM)

# 7. Dish Soap
def draw_dish_soap(draw):
    draw.rounded_rectangle([16, 16, 34, 44], radius=4, fill=BLUE)
    draw.rectangle([22, 8, 28, 16], fill=WHITE)
    draw.ellipse([23, 6, 27, 10], fill=RED)

# 8. Steel Wool Scrubber
def draw_steel_wool(draw):
    # messy silver scribbly pad
    draw.ellipse([12, 14, 38, 36], fill=STEEL)
    for offset in [(-4,-4), (4,-2), (-2,4), (4,4), (0,0)]:
        draw.arc([16+offset[0], 18+offset[1], 34+offset[0], 32+offset[1]], 0, 360, fill=SILVER, width=2)

# 9. Funnel
def draw_funnel(draw):
    draw.polygon([(10, 12), (40, 12), (28, 28), (22, 28)], fill=RED)
    draw.rectangle([22, 28, 28, 42], fill=RED)

# 10. Ice Cube Tray
def draw_ice_cube_tray(draw):
    # blue tray
    draw.rounded_rectangle([6, 16, 44, 34], radius=3, fill=BLUE)
    # ice slots
    for x in range(10, 42, 6):
        draw.rectangle([x, 20, x+4, 25], fill=GLASS)
        draw.rectangle([x, 26, x+4, 31], fill=GLASS)

# 11. Corkscrew
def draw_corkscrew(draw):
    draw.rounded_rectangle([12, 8, 38, 14], radius=3, fill=BROWN) # wooden handle
    draw.line([25, 14, 25, 30], fill=SILVER, width=3) # screw shaft
    # spiral tip
    draw.arc([22, 30, 28, 36], 90, 270, fill=STEEL, width=2)
    draw.arc([22, 34, 28, 40], 270, 90, fill=STEEL, width=2)

# 12. Nutcracker
def draw_nutcracker(draw):
    # two spring-loaded steel arms hinged at top
    draw.line([20, 8, 14, 40], fill=STEEL, width=3)
    draw.line([30, 8, 36, 40], fill=STEEL, width=3)
    # hinge
    draw.ellipse([22, 6, 28, 12], fill=DARK)
    # grooved grips
    draw.rectangle([14, 18, 17, 30], fill=BROWN)
    draw.rectangle([33, 18, 36, 30], fill=BROWN)

# 13. Hourglass / Egg Timer
def draw_egg_timer(draw):
    # wooden frame
    draw.rectangle([16, 10, 34, 40], fill=BROWN)
    draw.polygon([(18, 12), (32, 12), (25, 25)], fill=GLASS)
    draw.polygon([(18, 38), (32, 38), (25, 25)], fill=GLASS)
    # sand
    draw.polygon([(20, 14), (30, 14), (25, 25)], fill=YELLOW)
    draw.polygon([(22, 38), (28, 38), (25, 30)], fill=YELLOW)

# 14. Garlic Peeler Tube
def draw_garlic_peeler(draw):
    # silicone tube
    draw.rounded_rectangle([8, 18, 42, 32], radius=4, fill=BLUE)
    draw.ellipse([8, 18, 12, 32], fill=DKBLUE)
    draw.ellipse([38, 18, 42, 32], fill=(0,0,0,0)) # open end hollow

# 15. Honey Dipper
def draw_honey_dipper(draw):
    draw.line([6, 25, 34, 25], fill=TAN, width=3) # handle
    # grooves
    draw.ellipse([30, 15, 44, 35], fill=TAN)
    for x in [32, 36, 40]:
        draw.line([x, 16, x, 34], fill=BROWN, width=2)
    # honey drops
    draw.ellipse([32, 28, 42, 36], fill=YELLOW)

# 16. Oil Dispenser (Olive Oil Cruet)
def draw_oil_dispenser(draw):
    draw.rounded_rectangle([14, 18, 36, 44], radius=5, fill=GLASS)
    # green oil level
    draw.rounded_rectangle([16, 22, 34, 42], radius=3, fill=GREEN)
    # neck and pour spout
    draw.rectangle([22, 12, 28, 18], fill=SILVER)
    draw.line([25, 12, 34, 6], fill=STEEL, width=2)

# 17. Thermos / Flask
def draw_thermos(draw):
    draw.rounded_rectangle([14, 14, 36, 44], radius=4, fill=DKBLUE)
    # silver bands
    draw.rectangle([14, 20, 36, 24], fill=SILVER)
    draw.rectangle([14, 36, 36, 38], fill=SILVER)
    # cup lid
    draw.rounded_rectangle([16, 8, 34, 14], radius=2, fill=SILVER)

# 18. Bento Box
def draw_bento_box(draw):
    draw.rounded_rectangle([8, 14, 42, 38], radius=5, fill=RED)
    # dividers
    draw.line([22, 14, 22, 38], fill=DKRED, width=2)
    # food items
    draw.ellipse([12, 20, 18, 26], fill=WHITE) # rice
    draw.ellipse([14, 22, 16, 24], fill=RED)
    draw.rounded_rectangle([26, 20, 38, 32], radius=3, fill=YELLOW) # tamago

# 19. Cake Stand with Dome
def draw_cake_stand(draw):
    # base and pillar
    draw.line([25, 34, 25, 42], fill=SILVER, width=4)
    draw.ellipse([14, 40, 36, 44], fill=SILVER)
    # flat platter
    draw.rectangle([8, 32, 42, 35], fill=SILVER)
    # glass dome
    draw.chord([10, 12, 40, 32], 180, 360, fill=GLASS)
    draw.ellipse([23, 9, 27, 13], fill=WHITE)

# 20. Cookie Cutter (Star)
def draw_cookie_cutter(draw):
    draw.polygon([(25, 10), (29, 20), (39, 20), (31, 27), (35, 37), (25, 30), (15, 37), (19, 27), (11, 20), (21, 20)], fill=GLASS)
    draw.arc([11, 10, 39, 37], 0, 360, fill=RED, width=2)

# 21. Muffin Tin
def draw_muffin_tin(draw):
    draw.rounded_rectangle([6, 14, 44, 36], radius=3, fill=STEEL)
    # muffin cups
    for cx, cy in [(14, 20), (25, 20), (36, 20), (14, 30), (25, 30), (36, 30)]:
        draw.ellipse([cx-4, cy-4, cx+4, cy+4], fill=DARK)
        draw.ellipse([cx-3, cy-3, cx+3, cy+3], fill=BROWN)

# 22. Baking Sheet / Tray
def draw_baking_sheet(draw):
    draw.rounded_rectangle([6, 12, 44, 38], radius=3, fill=STEEL)
    draw.rounded_rectangle([8, 14, 42, 36], radius=2, fill=SILVER)
    # cookies
    for cx, cy in [(14, 20), (25, 20), (36, 20), (20, 28), (30, 28)]:
        draw.ellipse([cx-3, cy-3, cx+3, cy+3], fill=TAN)
        draw.point((cx, cy), fill=BROWN)

# 23. Wire Cooling Rack
def draw_cooling_rack(draw):
    draw.rounded_rectangle([6, 12, 44, 38], radius=2, fill=DARK)
    for x in range(10, 42, 4):
        draw.line([x, 14, x, 36], fill=STEEL, width=1)
    for y in range(16, 36, 4):
        draw.line([8, y, 42, y], fill=STEEL, width=1)

# 24. Piping / Pastry Bag
def draw_piping_bag(draw):
    draw.polygon([(16, 10), (34, 10), (25, 38)], fill=WHITE)
    draw.polygon([(16, 10), (34, 10), (25, 26)], fill=PINK) # cream filling
    # nozzle
    draw.polygon([(23, 38), (27, 38), (25, 44)], fill=SILVER)

# 25. Pastry Wheel (Crimper)
def draw_pastry_wheel(draw):
    draw.rounded_rectangle([22, 26, 28, 48], radius=4, fill=BROWN)
    draw.rectangle([24, 18, 26, 26], fill=STEEL)
    # crimped wheel
    draw.ellipse([16, 8, 34, 26], fill=SILVER)
    # crimps/spokes
    for angle in range(0, 360, 45):
        draw.arc([16, 8, 34, 26], angle, angle+20, fill=DARK, width=2)

# 26. Egg Separator
def draw_egg_separator(draw):
    draw.rounded_rectangle([8, 20, 32, 28], radius=3, fill=SILVER) # handle
    # separator cup with slits
    draw.ellipse([22, 12, 42, 32], fill=SILVER)
    draw.ellipse([24, 14, 40, 30], fill=STEEL)
    # yellow yolk in center
    draw.ellipse([28, 18, 36, 26], fill=YELLOW)

# 27. Garlic Keeper (Ceramic Jar)
def draw_garlic_keeper(draw):
    draw.rounded_rectangle([12, 18, 38, 46], radius=5, fill=CREAM)
    # air holes
    for hx, hy in [(20, 30), (30, 30), (25, 36)]:
        draw.ellipse([hx-2, hy-2, hx+2, hy+2], fill=DARK)
    # lid
    draw.rounded_rectangle([14, 12, 36, 18], radius=2, fill=CREAM)
    draw.ellipse([22, 8, 28, 14], fill=BROWN)

# 28. Silicone Trivet (Hot Pad)
def draw_trivet_silicone(draw):
    # honeycomb texture hot pad
    draw.ellipse([8, 8, 42, 42], fill=BLUE)
    for x in range(12, 40, 6):
        for y in range(12, 40, 6):
            draw.ellipse([x-2, y-2, x+2, y+2], fill=DKBLUE)

# 29. Grill Pan
def draw_grill_pan(draw):
    # square ridged pan
    draw.rounded_rectangle([10, 14, 40, 44], radius=3, fill=DARK)
    draw.rounded_rectangle([12, 16, 38, 42], radius=2, fill=(40,40,45,255))
    # grill ridges
    for x in range(16, 36, 4):
        draw.line([x, 18, x, 40], fill=DARK, width=2)
    # handle
    draw.rounded_rectangle([22, 6, 28, 14], radius=2, fill=BROWN)

# 30. Double Boiler Pot
def draw_double_boiler(draw):
    # bottom pot
    draw.rounded_rectangle([10, 24, 40, 42], radius=4, fill=STEEL)
    # top pot nested inside
    draw.rounded_rectangle([8, 14, 42, 26], radius=4, fill=SILVER)
    # lid
    draw.ellipse([10, 8, 40, 16], fill=SILVER)
    draw.ellipse([21, 5, 29, 10], fill=DARK)
    # handles
    draw.line([2, 18, 8, 18], fill=DARK, width=3)
    draw.line([42, 18, 48, 18], fill=DARK, width=3)

# 31. Pressure Cooker
def draw_pressure_cooker(draw):
    draw.rounded_rectangle([10, 16, 40, 44], radius=4, fill=STEEL)
    # lid lock bar
    draw.rectangle([8, 14, 42, 18], fill=DARK)
    # steam valve knob
    draw.rectangle([21, 8, 29, 14], fill=DARK)
    draw.ellipse([23, 6, 27, 10], fill=RED)

# 32. Slow Cooker / Crockpot
def draw_slow_cooker(draw):
    # outer pot
    draw.rounded_rectangle([8, 18, 42, 44], radius=5, fill=RED)
    # glass lid
    draw.ellipse([10, 12, 40, 20], fill=GLASS)
    draw.ellipse([22, 8, 28, 14], fill=DARK)
    # dial knob
    draw.ellipse([22, 34, 28, 40], fill=DARK)

# 33. Air Fryer
def draw_air_fryer(draw):
    draw.rounded_rectangle([10, 10, 40, 44], radius=6, fill=DARK)
    # screen / display
    draw.rounded_rectangle([16, 14, 34, 22], radius=3, fill=BLACK)
    draw.ellipse([22, 16, 28, 20], fill=BLUE) # blue status indicator
    # drawer handle
    draw.rounded_rectangle([22, 30, 28, 38], radius=2, fill=STEEL)

# 34. Food Processor
def draw_food_processor(draw):
    # motor base
    draw.rounded_rectangle([12, 32, 38, 44], radius=3, fill=STEEL)
    # work bowl
    draw.rounded_rectangle([14, 16, 36, 32], radius=4, fill=GLASS)
    # central column & blade
    draw.line([25, 20, 25, 32], fill=DARK, width=3)
    draw.line([18, 28, 32, 28], fill=SILVER, width=2)
    # feed tube lid
    draw.rectangle([14, 10, 36, 16], fill=STEEL)
    draw.rectangle([16, 4, 24, 10], fill=GLASS)

# 35. Electric Hand Mixer
def draw_hand_mixer(draw):
    # body
    draw.rounded_rectangle([10, 12, 38, 26], radius=4, fill=WHITE)
    # handle loop
    draw.arc([16, 4, 32, 16], 180, 360, fill=DARK, width=4)
    # beaters
    draw.line([16, 26, 16, 38], fill=SILVER, width=2)
    draw.ellipse([13, 34, 19, 42], fill=SILVER)
    draw.line([30, 26, 30, 38], fill=SILVER, width=2)
    draw.ellipse([27, 34, 33, 42], fill=SILVER)

# 36. Stand Mixer
def draw_stand_mixer(draw):
    # heavy base and neck
    draw.polygon([(10, 42), (40, 42), (36, 14), (16, 14)], fill=RED)
    draw.rounded_rectangle([16, 10, 38, 18], radius=3, fill=RED)
    # steel bowl nested
    draw.ellipse([12, 26, 32, 42], fill=SILVER)
    draw.chord([12, 32, 32, 42], 0, 180, fill=STEEL)
    # attachment beater
    draw.line([28, 18, 28, 26], fill=STEEL, width=2)

# 37. Crepe Pan
def draw_crepe_pan(draw):
    # extremely flat edge pan
    draw.rectangle([6, 32, 44, 36], fill=DARK)
    # handle
    draw.rounded_rectangle([4, 26, 10, 32], radius=2, fill=BROWN)
    # thin yellow crepe cooking
    draw.rectangle([10, 30, 40, 33], fill=YELLOW)

# 38. Fondue Pot
def draw_fondue_pot(draw):
    # stand
    draw.line([16, 36, 12, 46], fill=DARK, width=3)
    draw.line([34, 36, 38, 46], fill=DARK, width=3)
    # burner fire
    draw.ellipse([22, 40, 28, 46], fill=ORANGE)
    # ceramic pot
    draw.ellipse([12, 18, 38, 38], fill=RED)
    draw.ellipse([14, 20, 36, 30], fill=YELLOW) # cheese level
    # fork sticking out
    draw.line([34, 10, 26, 24], fill=SILVER, width=1)

# 39. Sushi Rolling Mat
def draw_sushi_mat(draw):
    # bamboo slats
    for x in range(10, 42, 3):
        draw.line([x, 14, x, 38], fill=TAN, width=2)
    # tying string lines
    draw.line([8, 20, 42, 20], fill=BROWN, width=1)
    draw.line([8, 32, 42, 32], fill=BROWN, width=1)

# 40. Tea Cozy
def draw_tea_cozy(draw):
    # dome fabric cover over teapot
    draw.chord([10, 14, 40, 44], 180, 360, fill=BLUE)
    draw.chord([12, 16, 38, 42], 180, 360, fill=PINK)
    # loop tag on top
    draw.arc([22, 10, 28, 18], 180, 360, fill=BLUE, width=3)

# 41. Bread Lame (Scoring Tool)
def draw_bread_lame(draw):
    # thin wooden stick handle
    draw.line([6, 36, 30, 18], fill=BROWN, width=2)
    # curved razor blade at tip
    draw.rounded_rectangle([26, 10, 42, 22], radius=2, fill=SILVER)
    draw.line([30, 14, 38, 14], fill=STEEL, width=2)

# 42. Cherry Pitter
def draw_cherry_pitter(draw):
    # Y-pliers style
    draw.rounded_rectangle([4, 8, 22, 14], radius=3, fill=STEEL)
    draw.rounded_rectangle([4, 36, 22, 42], radius=3, fill=STEEL)
    # hinge
    draw.ellipse([18, 22, 26, 28], fill=DARK)
    # cup for cherry
    draw.ellipse([26, 24, 38, 36], fill=SILVER)
    # plunger pin
    draw.line([25, 14, 32, 26], fill=STEEL, width=2)

# 43. Butter Curler
def draw_butter_curler(draw):
    # wooden handle
    draw.rounded_rectangle([4, 28, 20, 36], radius=3, fill=BROWN)
    # hook metal wand
    draw.line([20, 32, 34, 32], fill=STEEL, width=2)
    # serrated curl hook at top
    draw.arc([30, 20, 42, 32], 180, 360, fill=SILVER, width=3)

# 44. Gravy Boat
def draw_gravy_boat(draw):
    # boat body
    draw.ellipse([8, 22, 42, 42], fill=WHITE)
    draw.ellipse([10, 24, 40, 40], fill=CREAM)
    # spout
    draw.polygon([(6, 24), (2, 16), (12, 20)], fill=WHITE)
    # handle
    draw.arc([32, 20, 46, 38], 300, 60, fill=WHITE, width=4)

# 45. Salt Pig
def draw_salt_pig(draw):
    # earthenware dome jar with open front
    draw.ellipse([12, 16, 38, 44], fill=TAN)
    draw.ellipse([14, 18, 36, 42], fill=CREAM)
    # open mouth showing white salt
    draw.ellipse([16, 24, 34, 38], fill=DARK)
    draw.chord([16, 28, 34, 38], 0, 180, fill=WHITE)

# 46. Pepper Mill (Grinder)
def draw_pepper_mill(draw):
    # tall wooden grinder
    draw.rounded_rectangle([18, 14, 32, 44], radius=4, fill=BROWN)
    draw.line([18, 24, 32, 24], fill=DARK, width=2)
    # silver crank knob on top
    draw.rectangle([22, 10, 28, 14], fill=SILVER)
    draw.ellipse([23, 7, 27, 11], fill=STEEL)

# 47. Cheese Board (Slate)
def draw_cheese_board(draw):
    # dark slate platter
    draw.rounded_rectangle([6, 20, 44, 44], radius=4, fill=DARK)
    # cheeses on board
    draw.polygon([(10, 32), (22, 32), (16, 22)], fill=YELLOW) # cheddar
    draw.rounded_rectangle([26, 26, 38, 36], radius=2, fill=CREAM) # brie

# 48. Knife Block (Wooden)
def draw_knife_block(draw):
    # angled wood block
    draw.polygon([(14, 18), (36, 10), (42, 42), (20, 42)], fill=TAN)
    # knife handles sticking out
    draw.rounded_rectangle([12, 8, 18, 18], radius=2, fill=BLACK)
    draw.rounded_rectangle([20, 6, 26, 16], radius=2, fill=BROWN)
    draw.rounded_rectangle([28, 4, 34, 14], radius=2, fill=RED)

# 49. Trivet (Cast Iron)
def draw_trivet_cast_iron(draw):
    draw.ellipse([8, 8, 42, 42], fill=DARK)
    # lattice scrollwork
    draw.ellipse([14, 14, 36, 36], fill=(0,0,0,0))
    draw.line([25, 8, 25, 42], fill=DARK, width=2)
    draw.line([8, 25, 42, 25], fill=DARK, width=2)

# 50. Matchbox
def draw_matchbox(draw):
    # slide box
    draw.rounded_rectangle([8, 16, 42, 34], radius=3, fill=BLUE)
    draw.rectangle([10, 18, 40, 32], fill=WHITE)
    # match tip sticking out
    draw.line([36, 25, 46, 25], fill=TAN, width=2)
    draw.ellipse([44, 23, 48, 27], fill=RED)

# Build all 50 items
items = [
    ("microwave", draw_microwave),
    ("coffee_maker", draw_coffee_maker),
    ("espresso_machine", draw_espresso_machine),
    ("tea_infuser", draw_tea_infuser),
    ("garbage_can", draw_garbage_can),
    ("paper_towel_holder", draw_paper_towel_holder),
    ("dish_soap", draw_dish_soap),
    ("steel_wool", draw_steel_wool),
    ("funnel", draw_funnel),
    ("ice_cube_tray", draw_ice_cube_tray),
    ("corkscrew", draw_corkscrew),
    ("nutcracker", draw_nutcracker),
    ("egg_timer", draw_egg_timer),
    ("garlic_peeler", draw_garlic_peeler),
    ("honey_dipper", draw_honey_dipper),
    ("oil_dispenser", draw_oil_dispenser),
    ("thermos", draw_thermos),
    ("bento_box", draw_bento_box),
    ("cake_stand", draw_cake_stand),
    ("cookie_cutter", draw_cookie_cutter),
    ("muffin_tin", draw_muffin_tin),
    ("baking_sheet", draw_baking_sheet),
    ("cooling_rack", draw_cooling_rack),
    ("piping_bag", draw_piping_bag),
    ("pastry_wheel", draw_pastry_wheel),
    ("egg_separator", draw_egg_separator),
    ("garlic_keeper", draw_garlic_keeper),
    ("trivet_silicone", draw_trivet_silicone),
    ("grill_pan", draw_grill_pan),
    ("double_boiler", draw_double_boiler),
    ("pressure_cooker", draw_pressure_cooker),
    ("slow_cooker", draw_slow_cooker),
    ("air_fryer", draw_air_fryer),
    ("food_processor", draw_food_processor),
    ("hand_mixer", draw_hand_mixer),
    ("stand_mixer", draw_stand_mixer),
    ("crepe_pan", draw_crepe_pan),
    ("fondue_pot", draw_fondue_pot),
    ("sushi_mat", draw_sushi_mat),
    ("tea_cozy", draw_tea_cozy),
    ("bread_lame", draw_bread_lame),
    ("cherry_pitter", draw_cherry_pitter),
    ("butter_curler", draw_butter_curler),
    ("gravy_boat", draw_gravy_boat),
    ("salt_pig", draw_salt_pig),
    ("pepper_mill", draw_pepper_mill),
    ("cheese_board", draw_cheese_board),
    ("knife_block", draw_knife_block),
    ("trivet_cast_iron", draw_trivet_cast_iron),
    ("matchbox", draw_matchbox)
]

print(f"Generating {len(items)} new kitchen sprites in '{OUTPUT_DIR}'...")
for name, func in items:
    create_sprite(name, func)
print("\nAll 50 new kitchen sprites generated successfully!")
