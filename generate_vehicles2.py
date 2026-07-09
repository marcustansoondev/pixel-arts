import os
from PIL import Image, ImageDraw

OUTPUT_DIR = "images/vehicles"
os.makedirs(OUTPUT_DIR, exist_ok=True)

def create_sprite(name, draw_func):
    img = Image.new("RGBA", (50, 50), (255, 255, 255, 0))
    draw = ImageDraw.Draw(img)
    draw_func(draw)
    path = os.path.join(OUTPUT_DIR, f"{name}_50x50.png")
    img.save(path)
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
PINK      = (235, 130, 160, 255)
TAN       = (210, 180, 140, 255)

# 1. Unicycle
def draw_unicycle(draw):
    draw.ellipse([18, 28, 32, 42], fill=(0,0,0,0), outline=BLACK, width=2) # wheel
    # frame & pedal fork
    draw.line([25, 20, 25, 35], fill=BLUE, width=2)
    # seat
    draw.ellipse([20, 17, 30, 21], fill=BLACK)

# 2. Tandem Bicycle
def draw_tandem_bicycle(draw):
    draw.ellipse([6, 28, 18, 40], fill=(0,0,0,0), outline=BLACK, width=2)
    draw.ellipse([32, 28, 44, 40], fill=(0,0,0,0), outline=BLACK, width=2)
    # double diamond frame
    draw.line([(12, 34), (20, 20), (28, 34)], fill=RED, width=2)
    draw.line([(28, 34), (36, 20), (38, 34)], fill=RED, width=2)
    draw.line([(20, 20), (36, 20)], fill=RED, width=2)
    # seats
    draw.ellipse([18, 18, 22, 21], fill=BLACK)
    draw.ellipse([34, 18, 38, 21], fill=BLACK)

# 3. Penny Farthing
def draw_penny_farthing(draw):
    draw.ellipse([6, 16, 32, 42], fill=(0,0,0,0), outline=BLACK, width=2) # big wheel
    draw.ellipse([38, 34, 44, 40], fill=(0,0,0,0), outline=BLACK, width=2) # small wheel
    # frame curve
    draw.arc([14, 12, 40, 36], 180, 270, fill=BLUE, width=2)
    draw.ellipse([14, 10, 18, 13], fill=BLACK) # high seat

# 4. Dirt Bike
def draw_dirt_bike(draw):
    # sleek raised orange frame
    draw.polygon([(20, 20), (28, 20), (30, 30), (16, 30)], fill=ORANGE)
    # high mudguards
    draw.line([(10, 24), (16, 28)], fill=ORANGE, width=3)
    draw.ellipse([8, 28, 20, 40], fill=BLACK)
    draw.ellipse([28, 28, 40, 40], fill=BLACK)

# 5. Chopper Motorcycle
def draw_chopper_motorcycle(draw):
    # long angled front fork
    draw.line([(14, 34), (32, 12)], fill=SILVER, width=2)
    # low seat frame
    draw.rounded_rectangle([18, 26, 32, 34], radius=3, fill=BLACK)
    draw.ellipse([8, 28, 20, 40], fill=BLACK) # front wheel
    draw.ellipse([28, 24, 42, 38], fill=BLACK) # fat rear wheel

# 6. Snowmobile
def draw_snowmobile(draw):
    draw.rounded_rectangle([16, 22, 40, 34], radius=4, fill=BLUE)
    # front ski runners
    draw.line([(16, 34), (6, 34), (4, 30)], fill=STEEL, width=2)
    # rear tread drive
    draw.rectangle([24, 30, 38, 36], fill=BLACK)

# 7. ATV (Quad Bike)
def draw_atv(draw):
    draw.rounded_rectangle([12, 20, 38, 32], radius=4, fill=RED)
    # 4 big knobby tires
    draw.ellipse([8, 26, 18, 36], fill=BLACK)
    draw.ellipse([30, 26, 40, 36], fill=BLACK)
    draw.line([(16, 20), (20, 12)], fill=STEEL, width=3) # handlebars

# 8. Dune Buggy
def draw_dune_buggy(draw):
    # open frame cage
    draw.rectangle([14, 18, 36, 32], fill=(0,0,0,0), outline=YELLOW, width=2)
    # wheels
    draw.ellipse([8, 28, 18, 38], fill=BLACK)
    draw.ellipse([30, 28, 40, 38], fill=BLACK)

# 9. Ice Resurfacer
def draw_ice_resurfacer(draw):
    # blocky zamboni machine
    draw.rounded_rectangle([10, 16, 38, 38], radius=3, fill=WHITE)
    draw.rectangle([26, 10, 34, 20], fill=BLUE) # driver cab
    draw.ellipse([14, 32, 20, 38], fill=BLACK)
    draw.ellipse([28, 32, 34, 38], fill=BLACK)

# 10. Street Sweeper
def draw_street_sweeper(draw):
    draw.rounded_rectangle([10, 18, 38, 38], radius=2, fill=WHITE)
    draw.rectangle([12, 22, 20, 28], fill=LIGHTBLUE) # window
    # round sweeping brushes at bottom front
    draw.ellipse([8, 34, 16, 40], fill=ORANGE)
    draw.ellipse([14, 32, 20, 38], fill=BLACK)
    draw.ellipse([28, 32, 34, 38], fill=BLACK)

# 11. Tow Truck
def draw_tow_truck(draw):
    draw.rectangle([6, 22, 18, 38], fill=BLUE) # cab
    # flatbed and towing crane arm at back
    draw.rectangle([18, 28, 44, 38], fill=GREY)
    draw.line([(32, 28), (44, 16)], fill=STEEL, width=3) # tow arm
    draw.ellipse([10, 32, 16, 38], fill=BLACK)
    draw.ellipse([32, 32, 38, 38], fill=BLACK)

# 12. Tanker Truck
def draw_tank_truck(draw):
    draw.rectangle([6, 22, 16, 38], fill=RED) # cab
    # cylindrical steel liquid tank
    draw.rounded_rectangle([16, 18, 44, 38], radius=4, fill=SILVER)
    draw.ellipse([10, 32, 16, 38], fill=BLACK)
    draw.ellipse([24, 32, 30, 38], fill=BLACK)
    draw.ellipse([34, 32, 40, 38], fill=BLACK)

# 13. Car Transporter
def draw_car_transporter(draw):
    draw.rectangle([4, 24, 12, 38], fill=BLUE) # cab
    # double tier trailer displaying mini car
    draw.line([12, 26, 46, 26], fill=STEEL, width=2)
    draw.line([12, 34, 46, 34], fill=STEEL, width=2)
    # mini car
    draw.rounded_rectangle([20, 20, 30, 26], radius=2, fill=RED)
    draw.ellipse([14, 34, 18, 38], fill=BLACK)
    draw.ellipse([38, 34, 42, 38], fill=BLACK)

# 14. Logging Truck
def draw_logging_truck(draw):
    draw.rectangle([6, 22, 16, 38], fill=YELLOW) # cab
    # flatbed loaded with brown logs
    draw.rectangle([16, 30, 44, 38], fill=GREY)
    for y in [18, 22, 26]:
        draw.rounded_rectangle([18, y, 42, y+4], radius=1, fill=BROWN)
    draw.ellipse([10, 32, 16, 38], fill=BLACK)
    draw.ellipse([30, 32, 36, 38], fill=BLACK)

# 15. Armored Car
def draw_armored_car(draw):
    # secure green box van
    draw.rounded_rectangle([8, 18, 42, 38], radius=3, fill=DKGREEN)
    draw.rectangle([12, 22, 18, 26], fill=BLACK) # small window slit
    draw.ellipse([12, 34, 18, 40], fill=BLACK)
    draw.ellipse([32, 34, 38, 40], fill=BLACK)

# 16. Ice Cream Truck
def draw_ice_cream_truck(draw):
    draw.rounded_rectangle([8, 16, 42, 38], radius=3, fill=WHITE)
    draw.rectangle([20, 20, 30, 28], fill=LIGHTBLUE) # service window
    # giant ice cream cone sign on roof
    draw.polygon([(22, 12), (28, 12), (25, 16)], fill=BROWN)
    draw.ellipse([22, 6, 28, 12], fill=PINK)
    draw.ellipse([12, 34, 18, 40], fill=BLACK)
    draw.ellipse([32, 34, 38, 40], fill=BLACK)

# 17. Food Truck
def draw_food_truck(draw):
    draw.rounded_rectangle([8, 16, 42, 38], radius=3, fill=ORANGE)
    draw.rectangle([20, 20, 34, 28], fill=BLACK) # serving hatch hatch open
    draw.ellipse([12, 34, 18, 40], fill=BLACK)
    draw.ellipse([32, 34, 38, 40], fill=BLACK)

# 18. Camper Van (RV)
def draw_camper_van(draw):
    # large white RV body
    draw.rounded_rectangle([6, 16, 44, 38], radius=4, fill=WHITE)
    draw.rectangle([10, 20, 16, 26], fill=LIGHTBLUE) # cab window
    draw.rectangle([22, 20, 38, 26], fill=LIGHTBLUE) # living area window
    # brown stripe
    draw.line([6, 30, 44, 30], fill=BROWN, width=2)
    draw.ellipse([12, 34, 18, 40], fill=BLACK)
    draw.ellipse([32, 34, 38, 40], fill=BLACK)

# 19. Milk Float
def draw_milk_float(draw):
    # open sided white delivery cart
    draw.rectangle([8, 22, 16, 38], fill=WHITE) # cab
    # open shelves carrying white bottles
    draw.rectangle([16, 28, 42, 38], fill=GREY)
    for bx in [20, 26, 32, 38]:
        draw.rectangle([bx-1, 22, bx+1, 28], fill=WHITE)
    draw.ellipse([10, 34, 16, 40], fill=BLACK)
    draw.ellipse([32, 34, 38, 40], fill=BLACK)

# 20. Electric Unicycle (OneWheel)
def draw_electric_unicycle(draw):
    # central wheel wrapped by neon deck
    draw.ellipse([20, 26, 30, 36], fill=BLACK)
    draw.line([12, 28, 38, 28], fill=BLUE, width=3) # platform

# 21. Electric Scooter (Kick)
def draw_electric_scooter(draw):
    draw.line([16, 14, 16, 38], fill=BLACK, width=2) # steer pole
    draw.line([12, 14, 20, 14], fill=BLACK, width=2) # bar
    draw.line([16, 38, 36, 38], fill=GREY, width=3) # deck
    draw.ellipse([14, 36, 18, 40], fill=BLACK)
    draw.ellipse([34, 36, 38, 40], fill=BLACK)

# 22. Pulled Rickshaw
def draw_rickshaw(draw):
    # wooden carriage seat
    draw.rectangle([20, 22, 34, 32], fill=BROWN)
    draw.rectangle([14, 14, 34, 22], fill=YELLOW) # canopy hood
    # pull bars
    draw.line([(20, 30), (6, 34)], fill=BROWN, width=2)
    draw.ellipse([22, 28, 32, 38], fill=(0,0,0,0), outline=BLACK, width=2)

# 23. Horse Carriage
def draw_carriage(draw):
    # vintage luxury coach cabin
    draw.rounded_rectangle([18, 16, 42, 32], radius=4, fill=PURPLE)
    # gold trim windows
    draw.rectangle([24, 20, 36, 26], fill=(0,0,0,0), outline=YELLOW, width=2)
    # giant wooden wheels
    draw.ellipse([14, 28, 22, 36], fill=(0,0,0,0), outline=BROWN, width=2)
    draw.ellipse([36, 28, 44, 36], fill=(0,0,0,0), outline=BROWN, width=2)

# 24. Sleigh
def draw_sleigh(draw):
    # red curved carriage tub
    draw.polygon([(10, 20), (38, 20), (36, 32), (14, 32)], fill=RED)
    # curved runner skids below
    draw.arc([8, 28, 42, 38], 0, 180, fill=SILVER, width=2)
    draw.line([(8, 30), (6, 26)], fill=SILVER, width=2)

# 25. Dog Sled
def draw_dog_sled(draw):
    # wooden slatted sled
    draw.line([14, 34, 44, 34], fill=BROWN, width=3)
    draw.line([(44, 34), (46, 28)], fill=BROWN, width=2) # front curve
    # handlebar uprights
    draw.line([(16, 34), (16, 22)], fill=BROWN, width=2)
    draw.line([(16, 22), (20, 22)], fill=BROWN, width=2)

# 26. Railroad Handcar
def draw_handcar(draw):
    # flat rolling platform on tracks
    draw.rectangle([10, 32, 40, 36], fill=BROWN)
    # seesaw pump lever in middle
    draw.line([25, 22, 25, 32], fill=STEEL, width=2)
    draw.line([20, 22, 30, 26], fill=BLACK, width=2) # lever crossbar
    draw.ellipse([14, 34, 20, 40], fill=BLACK)
    draw.ellipse([30, 34, 36, 40], fill=BLACK)

# 27. Trolley Bus
def draw_trolley_bus(draw):
    draw.rounded_rectangle([8, 16, 42, 38], radius=3, fill=BLUE)
    # overhead wires contact poles
    draw.line([(20, 16), (10, 6)], fill=BLACK, width=2)
    draw.line([(24, 16), (14, 6)], fill=BLACK, width=2)
    draw.ellipse([12, 34, 18, 40], fill=BLACK)
    draw.ellipse([32, 34, 38, 40], fill=BLACK)

# 28. Steam Wagon
def draw_steam_wagon(draw):
    draw.rectangle([14, 22, 36, 38], fill=DKRED)
    # vertical boiler at front
    draw.rectangle([10, 16, 16, 34], fill=GREY)
    # metal chimney tip
    draw.rectangle([12, 10, 14, 16], fill=BLACK)
    draw.ellipse([12, 32, 18, 38], fill=BLACK)
    draw.ellipse([28, 32, 34, 38], fill=BLACK)

# 29. Paddle Steamer
def draw_paddle_steamer(draw):
    draw.rectangle([6, 26, 44, 36], fill=WHITE) # hull
    # Mississippi style paddle wheel at rear
    draw.ellipse([34, 24, 46, 36], fill=(0,0,0,0), outline=RED, width=3)
    # steam funnel chimneys
    draw.line([16, 12, 16, 26], fill=BLACK, width=2)
    draw.line([24, 12, 24, 26], fill=BLACK, width=2)

# 30. Rowboat
def draw_rowboat(draw):
    draw.chord([10, 22, 40, 36], 0, 180, fill=BROWN)
    # crossed oars
    draw.line([14, 18, 28, 34], fill=TAN, width=1)
    draw.line([36, 18, 22, 34], fill=TAN, width=1)

# 31. Gondola Boat
def draw_gondola_boat(draw):
    # sleek curved Venetian boat black hull
    draw.arc([6, 12, 44, 36], 0, 180, fill=BLACK, width=3)
    # curved metal bow decoration
    draw.line([(6, 24), (4, 16)], fill=SILVER, width=2)

# 32. Canoe
def draw_canoe(draw):
    # long pointed double-ended boat
    draw.ellipse([6, 24, 44, 30], fill=RED)
    draw.ellipse([10, 25, 40, 29], fill=TAN)

# 33. Jetfoil (Hydrofoil)
def draw_jetfoil(draw):
    draw.rounded_rectangle([10, 20, 40, 30], radius=2, fill=WHITE)
    # underwater wing foil legs
    draw.line([(14, 30), (14, 38)], fill=SILVER, width=2)
    draw.line([(36, 30), (36, 38)], fill=SILVER, width=2)
    # winglets
    draw.line([10, 38, 18, 38], fill=STEEL, width=2)
    draw.line([32, 38, 40, 38], fill=STEEL, width=2)

# 34. Catamaran
def draw_catamaran(draw):
    # twin parallel pontoons
    draw.rounded_rectangle([8, 30, 14, 36], radius=1, fill=WHITE)
    draw.rounded_rectangle([36, 30, 42, 36], radius=1, fill=WHITE)
    # bridge deck connecting them
    draw.rectangle([14, 26, 36, 32], fill=WHITE)
    # sail mast
    draw.line([25, 8, 25, 26], fill=BLACK, width=2)
    draw.polygon([(25, 10), (16, 24), (25, 24)], fill=WHITE)

# 35. Aircraft Carrier
def draw_aircraft_carrier(draw):
    # massive flat deck hull
    draw.polygon([(4, 26), (42, 26), (46, 22), (42, 18), (4, 18)], fill=DKGREY)
    # tiny tower island on side
    draw.rectangle([32, 12, 36, 18], fill=GREY)
    # miniature plane cross on deck
    draw.line([(18, 22), (22, 22)], fill=WHITE, width=1)
    draw.line([(20, 20), (20, 24)], fill=WHITE, width=1)

# 36. Tugboat
def draw_tugboat(draw):
    # stout red hull
    draw.chord([8, 22, 38, 40], 0, 180, fill=RED)
    # fat pilot house
    draw.rounded_rectangle([16, 16, 30, 28], radius=2, fill=WHITE)
    # black smokestack with puff
    draw.rectangle([22, 10, 26, 16], fill=BLACK)

# 37. Barge
def draw_barge(draw):
    # flat cargo barge carrying sand stack
    draw.rectangle([6, 28, 44, 38], fill=DKGREY)
    # sand stack heap
    draw.polygon([(12, 28), (25, 16), (38, 28)], fill=TAN)

# 38. Lifeboat
def draw_lifeboat(draw):
    # bright orange rescue boat
    draw.chord([8, 22, 42, 40], 0, 180, fill=ORANGE)
    draw.rounded_rectangle([16, 18, 34, 28], radius=2, fill=WHITE) # cabin

# 39. Pirate Ship (Galleon)
def draw_pirate_ship(draw):
    draw.chord([8, 22, 38, 40], 0, 180, fill=BROWN) # hull
    # raised castle decks
    draw.rectangle([8, 18, 14, 24], fill=BROWN)
    draw.rectangle([32, 18, 38, 24], fill=BROWN)
    # masts and black sails with white cross skull
    draw.line([22, 8, 22, 24], fill=BLACK, width=2)
    draw.rectangle([18, 10, 26, 18], fill=BLACK)
    draw.line([19, 14, 25, 14], fill=WHITE, width=1)
    draw.line([22, 11, 22, 17], fill=WHITE, width=1)

# 40. Hang Glider
def draw_hang_glider(draw):
    # triangular sail wing
    draw.polygon([(25, 12), (10, 28), (40, 28)], fill=YELLOW)
    # pilot harness hanging below
    draw.line([(25, 20), (25, 34)], fill=BLACK, width=2)
    draw.ellipse([23, 34, 27, 38], fill=RED)

# 41. Paraglider
def draw_paraglider(draw):
    # curved canopy wing
    draw.arc([10, 8, 40, 24], 180, 360, fill=RED, width=3)
    # lines converging to pilot
    draw.line([(10, 16), (25, 34)], fill=GREY, width=1)
    draw.line([(40, 16), (25, 34)], fill=GREY, width=1)
    draw.ellipse([23, 34, 27, 38], fill=BLUE)

# 42. Ultralight Airplane
def draw_ultralight_plane(draw):
    # open frame cockpit cart with high wing
    draw.line([10, 14, 40, 14], fill=BLUE, width=3) # wing
    # cart hanging down
    draw.line([(25, 14), (25, 32)], fill=STEEL, width=2)
    draw.rounded_rectangle([20, 28, 30, 34], radius=2, fill=WHITE)
    draw.ellipse([22, 34, 28, 40], fill=BLACK) # wheel

# 43. Glider Plane (Sailplane)
def draw_glider_plane(draw):
    # long slender wings
    draw.ellipse([18, 22, 32, 26], fill=WHITE) # fuselage
    draw.line([4, 24, 46, 24], fill=WHITE, width=2) # wingspan

# 44. Seaplane (Floatplane)
def draw_seaplane(draw):
    # propeller plane body
    draw.ellipse([14, 18, 36, 26], fill=YELLOW)
    # double pontoon floats underneath
    draw.line([18, 32, 32, 32], fill=STEEL, width=2)
    draw.line([(22, 26), (22, 32)], fill=BLACK, width=1)
    draw.line([(28, 26), (28, 32)], fill=BLACK, width=1)

# 45. Chinook Helicopter
def draw_chinook_helicopter(draw):
    # long tandem rotor helicopter fuselage
    draw.rounded_rectangle([10, 20, 40, 30], radius=3, fill=GREY)
    # twin rotors at front/rear top
    draw.line([(14, 20), (14, 14)], fill=BLACK, width=2)
    draw.line([(8, 14), (20, 14)], fill=DKGREY, width=1)
    draw.line([(36, 20), (36, 14)], fill=BLACK, width=2)
    draw.line([(30, 14), (42, 14)], fill=DKGREY, width=1)

# 46. Lunar Space Rover
def draw_space_rover(draw):
    # lunar rover frame with gold foil panels
    draw.rectangle([14, 24, 36, 34], fill=YELLOW)
    # satellite dish
    draw.arc([10, 10, 22, 22], 90, 270, fill=SILVER, width=2)
    # 4 mesh wheels
    draw.ellipse([10, 32, 18, 40], fill=(0,0,0,0), outline=GREY, width=2)
    draw.ellipse([32, 32, 40, 40], fill=(0,0,0,0), outline=GREY, width=2)

# 47. Space Rocket
def draw_space_rocket(draw):
    # vertical multi stage launcher rocket
    draw.rounded_rectangle([21, 10, 29, 38], radius=2, fill=WHITE)
    # nose cone
    draw.polygon([(21, 10), (29, 10), (25, 4)], fill=RED)
    # side booster thrusters
    draw.line([(20, 26), (20, 38)], fill=GREY, width=2)
    draw.line([(30, 26), (30, 38)], fill=GREY, width=2)
    # fiery exhaust tail
    draw.polygon([(23, 38), (27, 38), (25, 46)], fill=ORANGE)

# 48. Lunar Lander (Apollo Module)
def draw_lunar_lander(draw):
    # gold octagonal module body
    draw.polygon([(18, 18), (32, 18), (36, 28), (14, 28)], fill=YELLOW)
    # landing gear legs
    for lx, rx in [(14, 8), (36, 42)]:
        draw.line([(lx, 28), (rx, 38)], fill=STEEL, width=2)
        draw.ellipse([rx-2, 38, rx+2, 42], fill=SILVER) # landing pads

# 49. Hand Truck (Dolly)
def draw_hand_truck(draw):
    # vertical metal L frame
    draw.line([20, 14, 20, 38], fill=SILVER, width=3)
    draw.line([20, 38, 30, 38], fill=SILVER, width=3) # nose plate
    draw.ellipse([16, 36, 22, 42], fill=BLACK) # wheel

# 50. Snowplow
def draw_snowplow(draw):
    draw.rectangle([14, 20, 38, 36], fill=ORANGE) # truck cab
    draw.rectangle([16, 24, 24, 30], fill=LIGHTBLUE)
    # massive front angled wedge plow blade
    draw.line([(14, 36), (4, 30)], fill=SILVER, width=4)
    draw.ellipse([18, 32, 24, 38], fill=BLACK)
    draw.ellipse([30, 32, 36, 38], fill=BLACK)

# Build all 50 items
items = [
    ("unicycle", draw_unicycle),
    ("tandem_bicycle", draw_tandem_bicycle),
    ("penny_farthing", draw_penny_farthing),
    ("dirt_bike", draw_dirt_bike),
    ("chopper_motorcycle", draw_chopper_motorcycle),
    ("snowmobile", draw_snowmobile),
    ("atv", draw_atv),
    ("dune_buggy", draw_dune_buggy),
    ("ice_resurfacer", draw_ice_resurfacer),
    ("street_sweeper", draw_street_sweeper),
    ("tow_truck", draw_tow_truck),
    ("tank_truck", draw_tank_truck),
    ("car_transporter", draw_car_transporter),
    ("logging_truck", draw_logging_truck),
    ("armored_car", draw_armored_car),
    ("ice_cream_truck", draw_ice_cream_truck),
    ("food_truck", draw_food_truck),
    ("camper_van", draw_camper_van),
    ("milk_float", draw_milk_float),
    ("electric_unicycle", draw_electric_unicycle),
    ("electric_scooter", draw_electric_scooter),
    ("rickshaw", draw_rickshaw),
    ("carriage", draw_carriage),
    ("sleigh", draw_sleigh),
    ("dog_sled", draw_dog_sled),
    ("handcar", draw_handcar),
    ("trolley_bus", draw_trolley_bus),
    ("steam_wagon", draw_steam_wagon),
    ("paddle_steamer", draw_paddle_steamer),
    ("rowboat", draw_rowboat),
    ("gondola_boat", draw_gondola_boat),
    ("canoe", draw_canoe),
    ("jetfoil", draw_jetfoil),
    ("catamaran", draw_catamaran),
    ("aircraft_carrier", draw_aircraft_carrier),
    ("tugboat", draw_tugboat),
    ("barge", draw_barge),
    ("lifeboat", draw_lifeboat),
    ("pirate_ship", draw_pirate_ship),
    ("hang_glider", draw_hang_glider),
    ("paraglider", draw_paraglider),
    ("ultralight_plane", draw_ultralight_plane),
    ("glider_plane", draw_glider_plane),
    ("seaplane", draw_seaplane),
    ("chinook_helicopter", draw_chinook_helicopter),
    ("space_rover", draw_space_rover),
    ("space_rocket", draw_space_rocket),
    ("lunar_lander", draw_lunar_lander),
    ("hand_truck", draw_hand_truck),
    ("snowplow", draw_snowplow)
]

print(f"Generating {len(items)} new vehicle sprites in '{OUTPUT_DIR}'...")
for name, func in items:
    create_sprite(name, func)
print("\nAll 50 new vehicle sprites generated successfully!")
