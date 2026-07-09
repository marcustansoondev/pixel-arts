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

# 1. Sedan (Blue Car)
def draw_sedan(draw):
    draw.rounded_rectangle([10, 22, 40, 36], radius=4, fill=BLUE)
    draw.polygon([(14, 22), (18, 14), (32, 14), (36, 22)], fill=LIGHTBLUE) # cabin
    draw.ellipse([14, 32, 22, 40], fill=BLACK) # front wheel
    draw.ellipse([28, 32, 36, 40], fill=BLACK) # rear wheel

# 2. Sports Car (Red)
def draw_sports_car(draw):
    draw.polygon([(8, 26), (12, 18), (34, 18), (42, 26), (42, 34), (8, 34)], fill=RED)
    draw.polygon([(14, 24), (20, 16), (30, 16), (34, 24)], fill=BLACK) # windshield
    draw.ellipse([12, 30, 20, 38], fill=BLACK)
    draw.ellipse([30, 30, 38, 38], fill=BLACK)

# 3. Pickup Truck (Green)
def draw_pickup_truck(draw):
    draw.rounded_rectangle([8, 22, 42, 36], radius=2, fill=GREEN)
    draw.rectangle([10, 14, 24, 22], fill=LIGHTBLUE) # cab window
    draw.rectangle([25, 20, 40, 24], fill=(0,0,0,0)) # flatbed cut
    draw.ellipse([12, 32, 20, 40], fill=BLACK)
    draw.ellipse([30, 32, 38, 40], fill=BLACK)

# 4. SUV (Grey)
def draw_suv(draw):
    draw.rounded_rectangle([8, 18, 42, 36], radius=4, fill=GREY)
    # windows
    draw.rectangle([12, 14, 38, 22], fill=BLACK)
    draw.ellipse([12, 32, 20, 40], fill=BLACK)
    draw.ellipse([30, 32, 38, 40], fill=BLACK)

# 5. Minivan (White)
def draw_minivan(draw):
    draw.rounded_rectangle([8, 18, 42, 36], radius=4, fill=WHITE)
    draw.rectangle([12, 14, 36, 22], fill=LIGHTBLUE)
    draw.ellipse([12, 32, 20, 40], fill=BLACK)
    draw.ellipse([30, 32, 38, 40], fill=BLACK)

# 6. Convertible (Yellow)
def draw_convertible(draw):
    draw.rounded_rectangle([8, 24, 42, 36], radius=3, fill=YELLOW)
    # open cabin (windshield only)
    draw.line([(18, 24), (22, 16)], fill=LIGHTBLUE, width=3)
    draw.ellipse([12, 32, 20, 40], fill=BLACK)
    draw.ellipse([30, 32, 38, 40], fill=BLACK)

# 7. Limousine (Black)
def draw_limousine(draw):
    draw.rounded_rectangle([4, 22, 46, 36], radius=2, fill=BLACK)
    draw.rectangle([10, 16, 40, 22], fill=GREY) # long window strip
    draw.ellipse([8, 32, 16, 40], fill=DKGREY)
    draw.ellipse([34, 32, 42, 40], fill=DKGREY)

# 8. Formula 1 Race Car (Red/White)
def draw_race_car(draw):
    # low chassis
    draw.rectangle([6, 28, 44, 36], fill=RED)
    draw.rectangle([40, 24, 44, 32], fill=WHITE) # spoiler
    # cockpit driver helmet
    draw.ellipse([22, 22, 28, 28], fill=YELLOW)
    draw.ellipse([10, 28, 18, 36], fill=BLACK)
    draw.ellipse([32, 28, 40, 36], fill=BLACK)

# 9. Monster Truck
def draw_monster_truck(draw):
    # high small green body
    draw.rounded_rectangle([14, 10, 36, 22], radius=3, fill=GREEN)
    # suspension struts
    draw.line([(18, 22), (14, 34)], fill=STEEL, width=4)
    draw.line([(32, 22), (36, 34)], fill=STEEL, width=4)
    # giant wheels
    draw.ellipse([8, 26, 22, 40], fill=BLACK)
    draw.ellipse([28, 26, 42, 40], fill=BLACK)

# 10. Fire Truck
def draw_fire_truck(draw):
    draw.rectangle([8, 18, 42, 38], fill=RED)
    # white cab section
    draw.rectangle([8, 18, 18, 28], fill=WHITE)
    draw.rectangle([10, 20, 16, 26], fill=LIGHTBLUE)
    # ladder on top
    draw.line([14, 14, 38, 14], fill=GREY, width=2)
    for lx in range(18, 38, 4):
        draw.line([lx, 12, lx, 16], fill=GREY, width=1)
    draw.ellipse([12, 34, 18, 40], fill=BLACK)
    draw.ellipse([32, 34, 38, 40], fill=BLACK)

# 11. Police Car
def draw_police_car(draw):
    draw.rounded_rectangle([10, 22, 40, 36], radius=3, fill=BLACK)
    draw.rectangle([16, 22, 32, 30], fill=WHITE) # white doors
    draw.polygon([(14, 22), (18, 16), (32, 16), (36, 22)], fill=LIGHTBLUE)
    # flashing lights
    draw.rectangle([22, 12, 25, 16], fill=RED)
    draw.rectangle([25, 12, 28, 16], fill=BLUE)
    draw.ellipse([14, 32, 22, 40], fill=BLACK)
    draw.ellipse([28, 32, 36, 40], fill=BLACK)

# 12. Ambulance
def draw_ambulance(draw):
    draw.rounded_rectangle([8, 16, 42, 38], radius=3, fill=WHITE)
    draw.rectangle([10, 20, 18, 26], fill=LIGHTBLUE)
    # red cross
    draw.rectangle([24, 22, 32, 28], fill=RED)
    draw.rectangle([27, 19, 29, 31], fill=RED)
    # flashing beacon
    draw.ellipse([14, 12, 18, 16], fill=RED)
    draw.ellipse([12, 34, 18, 40], fill=BLACK)
    draw.ellipse([32, 34, 38, 40], fill=BLACK)

# 13. School Bus
def draw_school_bus(draw):
    draw.rounded_rectangle([6, 16, 44, 38], radius=2, fill=YELLOW)
    # black stripes and windows
    for wx in range(12, 40, 6):
        draw.rectangle([wx, 20, wx+4, 26], fill=BLACK)
    draw.line([6, 30, 44, 30], fill=BLACK, width=2)
    draw.ellipse([12, 34, 18, 40], fill=BLACK)
    draw.ellipse([32, 34, 38, 40], fill=BLACK)

# 14. Double Decker Bus
def draw_double_decker_bus(draw):
    draw.rounded_rectangle([8, 12, 42, 38], radius=3, fill=RED)
    # top row windows
    for wx in range(12, 40, 6):
        draw.rectangle([wx, 16, wx+4, 20], fill=LIGHTBLUE)
    # bottom row windows
    for wx in range(12, 40, 6):
        draw.rectangle([wx, 24, wx+4, 28], fill=LIGHTBLUE)
    draw.ellipse([12, 34, 18, 40], fill=BLACK)
    draw.ellipse([32, 34, 38, 40], fill=BLACK)

# 15. Garbage Truck
def draw_garbage_truck(draw):
    draw.rectangle([8, 20, 22, 38], fill=WHITE) # cab
    draw.rectangle([10, 24, 16, 30], fill=LIGHTBLUE)
    # large green container rear
    draw.rounded_rectangle([22, 16, 42, 38], radius=4, fill=GREEN)
    draw.ellipse([14, 34, 20, 40], fill=BLACK)
    draw.ellipse([32, 34, 38, 40], fill=BLACK)

# 16. Cement Mixer
def draw_cement_mixer(draw):
    draw.rectangle([6, 22, 20, 38], fill=YELLOW) # cab
    # rotating steel drum
    draw.ellipse([20, 16, 40, 34], fill=GREY)
    draw.arc([20, 16, 40, 34], 0, 360, fill=DKGREY, width=2)
    draw.ellipse([12, 34, 18, 40], fill=BLACK)
    draw.ellipse([30, 34, 36, 40], fill=BLACK)

# 17. Dump Truck
def draw_dump_truck(draw):
    draw.rectangle([6, 22, 18, 38], fill=YELLOW) # cab
    # large yellow bed filled with dirt/grey rocks
    draw.polygon([(18, 22), (40, 16), (44, 32), (18, 32)], fill=ORANGE)
    draw.chord([20, 10, 38, 22], 180, 360, fill=GREY) # load
    draw.ellipse([12, 32, 18, 38], fill=BLACK)
    draw.ellipse([32, 32, 38, 38], fill=BLACK)

# 18. Tractor
def draw_tractor(draw):
    # green engine body
    draw.rectangle([10, 24, 26, 38], fill=GREEN)
    # driver seat and roll bar
    draw.line([(28, 24), (28, 14)], fill=BLACK, width=2)
    draw.rectangle([24, 14, 32, 24], fill=YELLOW) # canopy
    # small front wheel, large rear wheel
    draw.ellipse([12, 34, 18, 40], fill=BLACK)
    draw.ellipse([26, 26, 42, 42], fill=BLACK)

# 19. Forklift
def draw_forklift(draw):
    # yellow cabin cage
    draw.rectangle([16, 20, 32, 38], fill=YELLOW)
    draw.rectangle([20, 14, 28, 24], fill=(0,0,0,0), outline=BLACK, width=2) # cage
    # front fork lift prongs
    draw.line([(10, 36), (6, 36)], fill=STEEL, width=3)
    draw.line([(10, 24), (10, 38)], fill=STEEL, width=3)
    draw.ellipse([14, 34, 20, 40], fill=BLACK)
    draw.ellipse([26, 34, 32, 40], fill=BLACK)

# 20. Bulldozer
def draw_bulldozer(draw):
    draw.rectangle([16, 20, 36, 38], fill=YELLOW)
    # front large metal blade plate
    draw.polygon([(12, 28), (4, 38), (14, 38)], fill=SILVER)
    # continuous treads (caterpillar tracks)
    draw.rounded_rectangle([14, 32, 38, 42], radius=4, fill=BLACK)

# 21. Excavator
def draw_excavator(draw):
    draw.rectangle([16, 24, 34, 36], fill=YELLOW) # cab
    # long segmented crane arm and bucket shovel
    draw.line([(26, 24), (26, 12)], fill=STEEL, width=4)
    draw.line([(26, 12), (16, 8)], fill=STEEL, width=3)
    draw.polygon([(16, 8), (12, 14), (18, 14)], fill=ORANGE) # scoop
    draw.rounded_rectangle([14, 32, 36, 40], radius=3, fill=BLACK) # tracks

# 22. Steamroller
def draw_steamroller(draw):
    draw.rectangle([18, 20, 36, 38], fill=GREEN) # body
    # giant metal front roller drum
    draw.ellipse([6, 26, 22, 42], fill=GREY)
    draw.ellipse([9, 29, 19, 39], fill=SILVER)
    draw.ellipse([28, 30, 36, 38], fill=BLACK) # smaller back tire

# 23. Golf Cart
def draw_golf_cart(draw):
    draw.rounded_rectangle([12, 24, 38, 38], radius=2, fill=WHITE)
    # windshield poles & canopy roof
    draw.line([(16, 24), (18, 14)], fill=BLACK, width=2)
    draw.line([(32, 24), (30, 14)], fill=BLACK, width=2)
    draw.rectangle([16, 12, 34, 16], fill=WHITE)
    draw.ellipse([14, 34, 20, 40], fill=BLACK)
    draw.ellipse([30, 34, 36, 40], fill=BLACK)

# 24. Go-Kart
def draw_gokart(draw):
    # low tube frame bumpers
    draw.rectangle([8, 30, 42, 36], fill=BLACK)
    # seat and driver body block
    draw.rectangle([20, 22, 28, 32], fill=RED)
    draw.ellipse([22, 16, 28, 22], fill=YELLOW) # helmet
    draw.ellipse([10, 28, 16, 34], fill=BLACK)
    draw.ellipse([32, 28, 38, 34], fill=BLACK)

# 25. Bicycle
def draw_bicycle(draw):
    # diamond frame
    draw.polygon([(16, 34), (25, 20), (34, 34)], fill=(0,0,0,0), outline=BLUE, width=2)
    draw.line([(25, 20), (14, 20)], fill=BLUE, width=2) # handlebars
    # two wheels
    draw.ellipse([8, 28, 20, 40], fill=(0,0,0,0), outline=BLACK, width=2)
    draw.ellipse([28, 28, 40, 40], fill=(0,0,0,0), outline=BLACK, width=2)

# 26. Motorcycle
def draw_motorcycle(draw):
    # sleek red frame & gas tank
    draw.ellipse([18, 22, 32, 30], fill=RED)
    draw.line([(28, 22), (16, 34)], fill=STEEL, width=3)
    draw.ellipse([10, 28, 22, 40], fill=BLACK)
    draw.ellipse([28, 28, 40, 40], fill=BLACK)

# 27. Vespa Scooter
def draw_scooter(draw):
    draw.chord([12, 20, 24, 38], 0, 180, fill=LIGHTBLUE) # front shield
    draw.rounded_rectangle([20, 26, 38, 36], radius=4, fill=LIGHTBLUE)
    draw.ellipse([14, 32, 20, 38], fill=BLACK)
    draw.ellipse([30, 32, 36, 38], fill=BLACK)

# 28. Segway
def draw_segway(draw):
    # platform base
    draw.rectangle([18, 38, 32, 42], fill=GREY)
    # upright steering handle pole
    draw.line([25, 14, 25, 38], fill=STEEL, width=2)
    draw.line([20, 14, 30, 14], fill=BLACK, width=2) # handle
    # left/right wheels side by side
    draw.ellipse([14, 34, 20, 44], fill=BLACK)
    draw.ellipse([30, 34, 36, 44], fill=BLACK)

# 29. Auto Rickshaw / Tuk Tuk
def draw_tuk_tuk(draw):
    # yellow cabin hood, three wheels
    draw.rounded_rectangle([12, 16, 38, 36], radius=4, fill=YELLOW)
    draw.rectangle([12, 20, 24, 28], fill=LIGHTBLUE) # front window
    draw.ellipse([14, 32, 19, 37], fill=BLACK) # front wheel
    draw.ellipse([30, 32, 36, 37], fill=BLACK) # rear wheel

# 30. Hovercraft
def draw_hovercraft(draw):
    # black rubber air skirt at bottom
    draw.rounded_rectangle([8, 30, 42, 38], radius=4, fill=BLACK)
    draw.ellipse([12, 18, 38, 32], fill=WHITE) # body
    # giant rear fan propellers
    draw.ellipse([30, 12, 38, 22], fill=GREY)

# 31. Speed Boat
def draw_speed_boat(draw):
    # wedge hull cutting water
    draw.polygon([(4, 30), (36, 30), (44, 20), (36, 18), (4, 18)], fill=RED)
    # glass windshield
    draw.polygon([(26, 20), (32, 20), (30, 14), (24, 14)], fill=LIGHTBLUE)

# 32. Sailboat
def draw_sailboat(draw):
    draw.chord([10, 26, 40, 42], 0, 180, fill=BROWN) # wooden hull
    # tall mast
    draw.line([25, 6, 25, 30], fill=BLACK, width=2)
    # white triangular sails
    draw.polygon([(25, 8), (14, 24), (25, 24)], fill=WHITE)
    draw.polygon([(25, 10), (34, 24), (25, 24)], fill=WHITE)

# 33. Submarine
def draw_submarine(draw):
    draw.ellipse([10, 20, 40, 34], fill=YELLOW)
    # tower structure
    draw.rectangle([22, 12, 28, 20], fill=YELLOW)
    # L periscope line
    draw.line([(25, 12), (25, 6), (28, 6)], fill=GREY, width=2)

# 34. Cruise Ship
def draw_cruise_ship(draw):
    # giant white hull
    draw.rounded_rectangle([4, 22, 46, 38], radius=2, fill=WHITE)
    draw.rectangle([4, 32, 46, 38], fill=DKBLUE) # bottom hull strip
    # cabins tiers
    draw.rectangle([10, 16, 40, 22], fill=WHITE)
    # tiny window port holes
    for px in range(12, 42, 6):
        draw.ellipse([px, 25, px+2, 27], fill=BLACK)

# 35. Jet Ski
def draw_jet_ski(draw):
    # tiny speed boat wedge
    draw.polygon([(8, 32), (32, 32), (40, 24), (32, 24)], fill=ORANGE)
    draw.rectangle([20, 20, 28, 26], fill=BLACK) # seat handlebars

# 36. Kayak
def draw_kayak(draw):
    # long slender double pointed canoe
    draw.ellipse([4, 22, 46, 28], fill=ORANGE)
    # center paddle crossed
    draw.line([20, 12, 30, 36], fill=BROWN, width=2)

# 37. Cargo Container Ship
def draw_cargo_ship(draw):
    # red container hull
    draw.rectangle([6, 28, 44, 38], fill=DKRED)
    # stacked colorful cargo boxes
    draw.rectangle([10, 18, 18, 28], fill=BLUE)
    draw.rectangle([18, 22, 26, 28], fill=YELLOW)
    draw.rectangle([26, 18, 34, 28], fill=GREEN)
    draw.rectangle([34, 22, 40, 28], fill=ORANGE)

# 38. Helicopter
def draw_helicopter(draw):
    # round cabin
    draw.ellipse([14, 18, 34, 32], fill=BLUE)
    draw.ellipse([26, 20, 32, 26], fill=LIGHTBLUE) # window
    # tail boom & rotor
    draw.line([(14, 25), (4, 22)], fill=BLUE, width=3)
    draw.line([(4, 18), (4, 26)], fill=BLACK, width=1)
    # landing skids
    draw.line([(18, 32), (18, 36)], fill=BLACK, width=2)
    draw.line([(30, 32), (30, 36)], fill=BLACK, width=2)
    draw.line([(14, 36), (34, 36)], fill=GREY, width=2)

# 39. Biplane
def draw_biplane(draw):
    # fuselage propeller plane
    draw.ellipse([10, 20, 40, 28], fill=RED)
    # double parallel wing layers
    draw.line([20, 12, 36, 12], fill=WHITE, width=2)
    draw.line([20, 32, 36, 32], fill=WHITE, width=2)
    # struts
    draw.line([(24, 12), (24, 32)], fill=BLACK, width=1)
    draw.line([(32, 12), (32, 32)], fill=BLACK, width=1)

# 40. Fighter Jet
def draw_jet_fighter(draw):
    # sleek grey delta wings shape
    draw.polygon([(25, 4), (16, 32), (25, 42), (34, 32)], fill=GREY)
    draw.polygon([(22, 28), (28, 28), (25, 20)], fill=LIGHTBLUE) # canopy cockpit
    # wingtip red rockets
    draw.rectangle([14, 30, 16, 36], fill=RED)
    draw.rectangle([34, 30, 36, 36], fill=RED)

# 41. Hot Air Balloon
def draw_hot_air_balloon(draw):
    # striped teardrop balloon
    draw.ellipse([14, 6, 36, 30], fill=RED)
    draw.chord([18, 16, 32, 32], 0, 180, fill=YELLOW)
    # hanging basket
    draw.rectangle([22, 36, 28, 42], fill=BROWN)
    draw.line([(22, 32), (22, 36)], fill=BLACK, width=1)
    draw.line([(28, 32), (28, 36)], fill=BLACK, width=1)

# 42. Blimp / Airship
def draw_blimp(draw):
    # oval balloon
    draw.ellipse([6, 12, 44, 28], fill=GREY)
    draw.line([6, 20, 44, 20], fill=BLUE, width=3) # stripe
    # tiny gondola below
    draw.rectangle([20, 28, 30, 32], fill=WHITE)

# 43. Passenger Airliner
def draw_passenger_plane(draw):
    # long fuselage tube
    draw.ellipse([4, 22, 46, 28], fill=WHITE)
    # sweeping back wings
    draw.polygon([(20, 24), (28, 24), (12, 38)], fill=GREY)
    draw.polygon([(20, 24), (28, 24), (38, 10)], fill=GREY)

# 44. Space Shuttle
def draw_space_shuttle(draw):
    # white triangular wings and dark nose
    draw.polygon([(25, 4), (12, 36), (38, 36)], fill=WHITE)
    draw.polygon([(22, 4), (28, 4), (25, 10)], fill=BLACK) # cockpit nose
    # booster exhausts
    draw.rectangle([20, 36, 23, 40], fill=ORANGE)
    draw.rectangle([27, 36, 30, 40], fill=ORANGE)

# 45. Steam Locomotive Train
def draw_train_locomotive(draw):
    draw.rectangle([10, 22, 36, 38], fill=BLACK)
    # vertical smoke stack chimney
    draw.rectangle([14, 12, 18, 22], fill=BLACK)
    # red driver cab at rear
    draw.rectangle([30, 16, 42, 38], fill=RED)
    draw.ellipse([14, 34, 22, 42], fill=GREY)
    draw.ellipse([26, 32, 38, 44], fill=GREY)

# 46. Bullet Train
def draw_bullet_train(draw):
    # sleek streamlined bullet nose
    draw.polygon([(4, 28), (20, 28), (26, 36), (4, 36)], fill=WHITE)
    draw.rectangle([20, 24, 46, 36], fill=WHITE)
    # blue stripe
    draw.line([4, 32, 46, 32], fill=BLUE, width=2)
    # front cockpit window slope
    draw.polygon([(6, 28), (14, 28), (18, 31), (6, 31)], fill=BLACK)

# 47. Electric Tram Streetcar
def draw_tram(draw):
    # square streetcar trolley box
    draw.rounded_rectangle([8, 16, 42, 38], radius=2, fill=GREEN)
    # window grid
    for wx in range(12, 40, 6):
        draw.rectangle([wx, 20, wx+4, 26], fill=LIGHTBLUE)
    # overhead pantograph connector rod
    draw.line([25, 16, 25, 8], fill=BLACK, width=2)
    draw.line([20, 8, 30, 8], fill=BLACK, width=2)

# 48. Cable Car
def draw_cable_car(draw):
    draw.rounded_rectangle([8, 16, 42, 38], radius=2, fill=BROWN)
    # yellow frame trims
    draw.rectangle([8, 16, 42, 20], fill=YELLOW)
    # open sides with posts
    for px in range(12, 40, 8):
        draw.line([px, 20, px, 30], fill=YELLOW, width=2)
    draw.ellipse([14, 36, 20, 42], fill=BLACK)
    draw.ellipse([30, 36, 36, 42], fill=BLACK)

# 49. Monorail
def draw_monorail(draw):
    # capsule wrapping train car
    draw.rounded_rectangle([6, 18, 44, 32], radius=4, fill=WHITE)
    draw.rectangle([10, 22, 40, 26], fill=BLACK) # continuous black window
    # straddling concrete beam track line underneath
    draw.line([4, 32, 46, 32], fill=GREY, width=3)

# 50. Hoverboard
def draw_hoverboard(draw):
    # sleek neon deck
    draw.rounded_rectangle([8, 22, 42, 28], radius=2, fill=PURPLE)
    # neon light rings underneath
    draw.ellipse([12, 28, 20, 32], fill=BLUE)
    draw.ellipse([30, 28, 38, 32], fill=BLUE)

# Build all 50 items
items = [
    ("sedan", draw_sedan),
    ("sports_car", draw_sports_car),
    ("pickup_truck", draw_pickup_truck),
    ("suv", draw_suv),
    ("minivan", draw_minivan),
    ("convertible", draw_convertible),
    ("limousine", draw_limousine),
    ("race_car", draw_race_car),
    ("monster_truck", draw_monster_truck),
    ("fire_truck", draw_fire_truck),
    ("police_car", draw_police_car),
    ("ambulance", draw_ambulance),
    ("school_bus", draw_school_bus),
    ("double_decker_bus", draw_double_decker_bus),
    ("garbage_truck", draw_garbage_truck),
    ("cement_mixer", draw_cement_mixer),
    ("dump_truck", draw_dump_truck),
    ("tractor", draw_tractor),
    ("forklift", draw_forklift),
    ("bulldozer", draw_bulldozer),
    ("excavator", draw_excavator),
    ("steamroller", draw_steamroller),
    ("golf_cart", draw_golf_cart),
    ("gokart", draw_gokart),
    ("bicycle", draw_bicycle),
    ("motorcycle", draw_motorcycle),
    ("scooter", draw_scooter),
    ("segway", draw_segway),
    ("tuk_tuk", draw_tuk_tuk),
    ("hovercraft", draw_hovercraft),
    ("speed_boat", draw_speed_boat),
    ("sailboat", draw_sailboat),
    ("submarine", draw_submarine),
    ("cruise_ship", draw_cruise_ship),
    ("jet_ski", draw_jet_ski),
    ("kayak", draw_kayak),
    ("cargo_ship", draw_cargo_ship),
    ("helicopter", draw_helicopter),
    ("biplane", draw_biplane),
    ("jet_fighter", draw_jet_fighter),
    ("hot_air_balloon", draw_hot_air_balloon),
    ("blimp", draw_blimp),
    ("passenger_plane", draw_passenger_plane),
    ("space_shuttle", draw_space_shuttle),
    ("train_locomotive", draw_train_locomotive),
    ("bullet_train", draw_bullet_train),
    ("tram", draw_tram),
    ("cable_car", draw_cable_car),
    ("monorail", draw_monorail),
    ("hoverboard", draw_hoverboard)
]

print(f"Generating {len(items)} new vehicle sprites in '{OUTPUT_DIR}'...")
for name, func in items:
    create_sprite(name, func)
print("\nAll 50 new vehicle sprites generated successfully!")
