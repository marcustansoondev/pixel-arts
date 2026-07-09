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
    draw.rectangle([12, 38, 38, 40], fill=DKGREY) # underbody shadow
    draw.rounded_rectangle([10, 22, 40, 36], radius=4, fill=BLUE)
    draw.rectangle([10, 29, 40, 36], fill=DKBLUE) # shading
    draw.polygon([(14, 22), (18, 14), (32, 14), (36, 22)], fill=LIGHTBLUE) # cabin
    draw.polygon([(20, 15), (23, 15), (17, 22), (14, 22)], fill=WHITE) # window highlight
    # bumpers
    draw.line([8, 30, 10, 30], fill=SILVER, width=2)
    draw.line([40, 30, 42, 30], fill=SILVER, width=2)
    # lights
    draw.rectangle([10, 25, 12, 28], fill=YELLOW) # headlight
    draw.rectangle([38, 25, 40, 28], fill=RED) # taillight
    # wheels
    draw.ellipse([14, 32, 22, 40], fill=BLACK)
    draw.ellipse([16, 34, 20, 38], fill=SILVER)
    draw.ellipse([28, 32, 36, 40], fill=BLACK)
    draw.ellipse([30, 34, 34, 38], fill=SILVER)

# 2. Sports Car (Red)
def draw_sports_car(draw):
    draw.rectangle([10, 36, 40, 38], fill=DKGREY) # shadow
    draw.polygon([(8, 26), (12, 18), (34, 18), (42, 26), (42, 34), (8, 34)], fill=RED)
    draw.rectangle([8, 30, 42, 34], fill=DKRED) # shading
    draw.polygon([(14, 24), (20, 16), (30, 16), (34, 24)], fill=BLACK) # windshield
    draw.line([(18, 22), (24, 17)], fill=LIGHTBLUE, width=1) # windshield highlight
    # spoiler
    draw.line([(38, 20), (38, 15)], fill=BLACK, width=2)
    draw.rectangle([(36, 14), (43, 16)], fill=DKRED)
    # lights
    draw.rectangle([8, 26, 10, 29], fill=YELLOW) # headlight
    draw.rectangle([41, 26, 43, 29], fill=ORANGE) # taillight
    # wheels
    draw.ellipse([12, 30, 20, 38], fill=BLACK)
    draw.ellipse([14, 32, 18, 36], fill=SILVER)
    draw.ellipse([30, 30, 38, 38], fill=BLACK)
    draw.ellipse([32, 32, 36, 36], fill=SILVER)

# 3. Pickup Truck (Green)
def draw_pickup_truck(draw):
    draw.rectangle([10, 38, 40, 40], fill=DKGREY) # shadow
    draw.rounded_rectangle([8, 22, 42, 36], radius=2, fill=GREEN)
    draw.rectangle([8, 29, 42, 36], fill=DKGREEN) # body shading
    draw.rectangle([10, 14, 24, 22], fill=GREEN) # cab upper frame
    draw.rectangle([12, 15, 22, 21], fill=LIGHTBLUE) # cab window
    draw.line([(14, 15), (18, 20)], fill=WHITE, width=1) # window shine
    draw.rectangle([25, 20, 40, 24], fill=(0,0,0,0)) # flatbed cut
    # cargo (logs)
    draw.rounded_rectangle([26, 17, 39, 21], radius=1, fill=BROWN)
    draw.rounded_rectangle([29, 13, 37, 17], radius=1, fill=BROWN)
    # bumper and lights
    draw.line([6, 31, 8, 31], fill=SILVER, width=2)
    draw.rectangle([8, 24, 9, 27], fill=YELLOW)
    draw.rectangle([41, 24, 42, 27], fill=RED)
    # wheels
    draw.ellipse([12, 32, 20, 40], fill=BLACK)
    draw.ellipse([14, 34, 18, 38], fill=SILVER)
    draw.ellipse([30, 32, 38, 40], fill=BLACK)
    draw.ellipse([32, 34, 36, 38], fill=SILVER)

# 4. SUV (Grey)
def draw_suv(draw):
    draw.rectangle([10, 38, 40, 40], fill=DKGREY) # shadow
    draw.rounded_rectangle([8, 18, 42, 36], radius=4, fill=GREY)
    draw.rectangle([8, 27, 42, 36], fill=DKGREY) # shading
    draw.rectangle([12, 14, 38, 22], fill=BLACK) # windows strip
    draw.line([(14, 14), (20, 21)], fill=LIGHTBLUE, width=1)
    draw.line([(26, 14), (32, 21)], fill=LIGHTBLUE, width=1)
    # roof rack
    draw.line([12, 16, 38, 16], fill=BLACK, width=2)
    # front grille and lights
    draw.rectangle([8, 22, 10, 26], fill=SILVER)
    draw.rectangle([8, 20, 9, 22], fill=YELLOW)
    # wheels
    draw.ellipse([12, 32, 20, 40], fill=BLACK)
    draw.ellipse([14, 34, 18, 38], fill=GREY)
    draw.ellipse([30, 32, 38, 40], fill=BLACK)
    draw.ellipse([32, 34, 36, 38], fill=GREY)

# 5. Minivan (White)
def draw_minivan(draw):
    draw.rectangle([10, 38, 40, 40], fill=DKGREY) # shadow
    draw.rounded_rectangle([8, 18, 42, 36], radius=4, fill=WHITE)
    draw.rectangle([8, 28, 42, 36], fill=GREY) # shading
    draw.rectangle([12, 14, 36, 22], fill=LIGHTBLUE) # windows
    draw.line([(18, 14), (18, 22)], fill=BLACK, width=2) # window pillar
    draw.line([(28, 14), (28, 22)], fill=BLACK, width=2)
    # details
    draw.line([20, 26, 38, 26], fill=DKGREY, width=1) # door guide
    draw.rectangle([8, 23, 9, 26], fill=YELLOW)
    draw.rectangle([41, 23, 42, 26], fill=RED)
    # wheels
    draw.ellipse([12, 32, 20, 40], fill=BLACK)
    draw.ellipse([14, 34, 18, 38], fill=SILVER)
    draw.ellipse([30, 32, 38, 40], fill=BLACK)
    draw.ellipse([32, 34, 36, 38], fill=SILVER)

# 6. Convertible (Yellow)
def draw_convertible(draw):
    draw.rectangle([10, 38, 40, 40], fill=DKGREY) # shadow
    draw.rounded_rectangle([8, 24, 42, 36], radius=3, fill=YELLOW)
    draw.rectangle([8, 30, 42, 36], fill=ORANGE) # lower shade
    # open cabin
    draw.rectangle([18, 20, 32, 24], fill=RED) # red seats
    draw.ellipse([26, 18, 30, 22], fill=BROWN) # steering wheel
    draw.line([(16, 24), (20, 16)], fill=SILVER, width=2) # windshield frame
    draw.line([(17, 24), (20, 18)], fill=LIGHTBLUE, width=1) # windshield glass
    # lights
    draw.rectangle([8, 26, 9, 29], fill=YELLOW)
    draw.rectangle([41, 26, 42, 29], fill=RED)
    # wheels
    draw.ellipse([12, 32, 20, 40], fill=BLACK)
    draw.ellipse([14, 34, 18, 38], fill=SILVER)
    draw.ellipse([30, 32, 38, 40], fill=BLACK)
    draw.ellipse([32, 34, 36, 38], fill=SILVER)

# 7. Limousine (Black)
def draw_limousine(draw):
    draw.rectangle([6, 38, 44, 40], fill=DKGREY) # shadow
    draw.rounded_rectangle([4, 22, 46, 36], radius=2, fill=BLACK)
    draw.line([5, 24, 45, 24], fill=DKGREY, width=1) # specular line
    draw.rectangle([10, 16, 40, 22], fill=GREY) # long window strip
    draw.line([(18, 16), (18, 22)], fill=BLACK, width=2)
    draw.line([(28, 16), (28, 22)], fill=BLACK, width=2)
    # luxury silver trims
    draw.rectangle([4, 26, 6, 30], fill=SILVER) # grille
    draw.rectangle([16, 24, 18, 26], fill=SILVER) # handles
    draw.rectangle([26, 24, 28, 26], fill=SILVER)
    # lights
    draw.rectangle([4, 23, 5, 25], fill=YELLOW)
    draw.rectangle([45, 23, 46, 25], fill=RED)
    # wheels
    draw.ellipse([8, 32, 16, 40], fill=BLACK)
    draw.ellipse([10, 34, 14, 38], fill=SILVER)
    draw.ellipse([34, 32, 42, 40], fill=BLACK)
    draw.ellipse([36, 34, 40, 38], fill=SILVER)

# 8. Formula 1 Race Car (Red/White)
def draw_race_car(draw):
    draw.rectangle([8, 36, 42, 38], fill=DKGREY) # shadow
    # low chassis
    draw.rectangle([6, 28, 44, 36], fill=RED)
    draw.rectangle([6, 32, 44, 36], fill=DKRED) # shadow underpod
    # wings
    draw.rectangle([4, 32, 9, 35], fill=WHITE) # front wing
    draw.rectangle([40, 20, 44, 28], fill=WHITE) # rear wing
    draw.rectangle([43, 18, 45, 30], fill=BLACK) # wing endplate
    # cockpit driver helmet
    draw.ellipse([22, 20, 28, 26], fill=YELLOW)
    draw.rectangle([24, 21, 28, 23], fill=BLACK) # visor
    # wheels
    draw.ellipse([10, 28, 18, 36], fill=BLACK)
    draw.ellipse([12, 30, 16, 34], fill=YELLOW)
    draw.ellipse([32, 28, 40, 36], fill=BLACK)
    draw.ellipse([34, 30, 38, 34], fill=YELLOW)

# 9. Monster Truck
def draw_monster_truck(draw):
    # body (green truck cab)
    draw.rounded_rectangle([14, 10, 36, 22], radius=3, fill=GREEN)
    draw.polygon([(18, 14), (26, 14), (22, 18)], fill=YELLOW) # flame decal
    draw.rectangle([14, 12, 18, 16], fill=LIGHTBLUE) # window
    # roll cage
    draw.line([(26, 10), (32, 10), (34, 14)], fill=BLACK, width=2)
    draw.ellipse([28, 8, 30, 10], fill=YELLOW) # roof spotlights
    draw.ellipse([31, 8, 33, 10], fill=YELLOW)
    # suspension struts & springs
    draw.line([(18, 22), (14, 34)], fill=STEEL, width=3)
    draw.line([(32, 22), (36, 34)], fill=STEEL, width=3)
    draw.line([(17, 26), (19, 29)], fill=DKGREY, width=2) # spring coils
    draw.line([(31, 26), (33, 29)], fill=DKGREY, width=2)
    # giant wheels
    draw.ellipse([6, 24, 22, 40], fill=BLACK)
    draw.ellipse([10, 28, 18, 36], fill=SILVER) # chrome rim
    draw.ellipse([28, 24, 44, 40], fill=BLACK)
    draw.ellipse([32, 28, 40, 36], fill=SILVER)

# 10. Fire Truck
def draw_fire_truck(draw):
    draw.rectangle([8, 18, 42, 38], fill=RED)
    draw.rectangle([8, 30, 42, 38], fill=DKRED) # shading
    # white cab section
    draw.rectangle([8, 18, 18, 28], fill=WHITE)
    draw.rectangle([10, 20, 16, 26], fill=LIGHTBLUE)
    # ladder on top
    draw.line([14, 14, 38, 14], fill=STEEL, width=2)
    for lx in range(18, 38, 4):
        draw.line([lx, 12, lx, 16], fill=STEEL, width=1)
    # equipment
    draw.ellipse([24, 26, 30, 32], fill=YELLOW) # hose reel
    draw.rectangle([34, 24, 39, 28], fill=SILVER) # control panel
    # emergency lights
    draw.rectangle([13, 15, 15, 18], fill=BLUE)
    draw.rectangle([15, 15, 17, 18], fill=RED)
    # wheels
    draw.ellipse([12, 34, 18, 40], fill=BLACK)
    draw.ellipse([14, 36, 16, 38], fill=SILVER)
    draw.ellipse([32, 34, 38, 40], fill=BLACK)
    draw.ellipse([34, 36, 36, 38], fill=SILVER)

# 11. Police Car
def draw_police_car(draw):
    draw.rectangle([10, 38, 40, 40], fill=DKGREY) # shadow
    draw.rounded_rectangle([10, 22, 40, 36], radius=3, fill=BLACK)
    draw.rectangle([16, 22, 32, 30], fill=WHITE) # white doors
    draw.polygon([(14, 22), (18, 16), (32, 16), (36, 22)], fill=LIGHTBLUE)
    draw.line([(20, 17), (24, 21)], fill=WHITE, width=1) # window shine
    # flashing lights
    draw.rectangle([22, 12, 25, 16], fill=RED)
    draw.rectangle([25, 12, 28, 16], fill=BLUE)
    # bullbar
    draw.line([7, 28, 9, 28], fill=STEEL, width=2)
    draw.line([7, 26, 7, 32], fill=STEEL, width=2)
    # wheels
    draw.ellipse([14, 32, 22, 40], fill=BLACK)
    draw.ellipse([16, 34, 20, 38], fill=SILVER)
    draw.ellipse([28, 32, 36, 40], fill=BLACK)
    draw.ellipse([30, 34, 34, 38], fill=SILVER)

# 12. Ambulance
def draw_ambulance(draw):
    draw.rectangle([8, 38, 42, 40], fill=DKGREY) # shadow
    draw.rounded_rectangle([8, 16, 42, 38], radius=3, fill=WHITE)
    draw.rectangle([8, 28, 42, 30], fill=RED) # stripe
    draw.rectangle([10, 20, 18, 26], fill=LIGHTBLUE) # cab window
    # red cross
    draw.rectangle([25, 21, 31, 25], fill=RED)
    draw.rectangle([27, 19, 29, 27], fill=RED)
    # flashing beacon
    draw.ellipse([14, 12, 18, 16], fill=RED)
    # wheels
    draw.ellipse([12, 34, 18, 40], fill=BLACK)
    draw.ellipse([14, 36, 16, 38], fill=SILVER)
    draw.ellipse([32, 34, 38, 40], fill=BLACK)
    draw.ellipse([34, 36, 36, 38], fill=SILVER)

# 13. School Bus
def draw_school_bus(draw):
    draw.rounded_rectangle([6, 16, 44, 38], radius=2, fill=YELLOW)
    draw.rectangle([6, 30, 44, 38], fill=ORANGE) # lower shadow
    # black stripes and windows
    for wx in range(12, 40, 6):
        draw.rectangle([wx, 20, wx+4, 26], fill=LIGHTBLUE)
    draw.line([6, 28, 44, 28], fill=BLACK, width=2) # black stripe
    draw.line([6, 32, 44, 32], fill=BLACK, width=1)
    # stop sign
    draw.ellipse([8, 24, 12, 28], fill=RED)
    # warning lights
    draw.ellipse([8, 14, 10, 16], fill=RED)
    draw.ellipse([40, 14, 42, 16], fill=RED)
    # wheels
    draw.ellipse([12, 34, 18, 40], fill=BLACK)
    draw.ellipse([14, 36, 16, 38], fill=GREY)
    draw.ellipse([32, 34, 38, 40], fill=BLACK)
    draw.ellipse([34, 36, 36, 38], fill=GREY)

# 14. Double Decker Bus
def draw_double_decker_bus(draw):
    draw.rounded_rectangle([8, 12, 42, 38], radius=3, fill=RED)
    draw.rectangle([8, 28, 42, 38], fill=DKRED) # shading
    # top row windows
    for wx in range(12, 40, 6):
        draw.rectangle([wx, 16, wx+4, 20], fill=LIGHTBLUE)
    # bottom row windows
    for wx in range(12, 40, 6):
        draw.rectangle([wx, 24, wx+4, 28], fill=LIGHTBLUE)
    # destination display
    draw.rectangle([8, 13, 14, 15], fill=BLACK)
    draw.rectangle([9, 14, 13, 15], fill=YELLOW)
    # wheels
    draw.ellipse([12, 34, 18, 40], fill=BLACK)
    draw.ellipse([14, 36, 16, 38], fill=SILVER)
    draw.ellipse([32, 34, 38, 40], fill=BLACK)
    draw.ellipse([34, 36, 36, 38], fill=SILVER)

# 15. Garbage Truck
def draw_garbage_truck(draw):
    draw.rectangle([8, 20, 22, 38], fill=WHITE) # cab
    draw.rectangle([8, 30, 22, 38], fill=GREY) # cab shadow
    draw.rectangle([10, 24, 16, 30], fill=LIGHTBLUE)
    # large green container rear
    draw.rounded_rectangle([22, 16, 42, 38], radius=4, fill=GREEN)
    draw.rectangle([22, 28, 42, 38], fill=DKGREEN) # shadow
    # rib details
    for rx in range(25, 41, 5):
        draw.line([rx, 18, rx, 36], fill=GREEN, width=1)
    # loading arm
    draw.line([(8, 32), (6, 26), (12, 24)], fill=STEEL, width=2)
    # wheels
    draw.ellipse([14, 34, 20, 40], fill=BLACK)
    draw.ellipse([16, 36, 18, 38], fill=GREY)
    draw.ellipse([32, 34, 38, 40], fill=BLACK)
    draw.ellipse([34, 36, 36, 38], fill=GREY)

# 16. Cement Mixer
def draw_cement_mixer(draw):
    draw.rectangle([6, 22, 20, 38], fill=YELLOW) # cab
    draw.rectangle([6, 30, 20, 38], fill=ORANGE) # bumper/shadow
    draw.rectangle([8, 24, 14, 29], fill=LIGHTBLUE) # window
    # rotating steel drum
    draw.ellipse([20, 16, 40, 34], fill=GREY)
    draw.arc([20, 16, 40, 34], 0, 360, fill=DKGREY, width=2)
    # spiral stripe
    draw.line([(24, 18), (36, 32)], fill=WHITE, width=3)
    # discharge chute
    draw.line([(40, 28), (44, 34)], fill=STEEL, width=3)
    # wheels
    draw.ellipse([12, 34, 18, 40], fill=BLACK)
    draw.ellipse([14, 36, 16, 38], fill=SILVER)
    draw.ellipse([30, 34, 36, 40], fill=BLACK)
    draw.ellipse([32, 36, 34, 38], fill=SILVER)

# 17. Dump Truck
def draw_dump_truck(draw):
    draw.rectangle([6, 22, 18, 38], fill=YELLOW) # cab
    draw.rectangle([8, 24, 14, 29], fill=LIGHTBLUE)
    # large orange bed filled with dirt/grey rocks
    draw.polygon([(18, 22), (40, 16), (44, 32), (18, 32)], fill=ORANGE)
    # rock load
    draw.ellipse([20, 12, 26, 18], fill=GREY)
    draw.ellipse([25, 10, 32, 17], fill=DKGREY)
    draw.ellipse([30, 11, 38, 18], fill=GREY)
    # wheels
    draw.ellipse([12, 32, 18, 38], fill=BLACK)
    draw.ellipse([14, 34, 16, 36], fill=GREY)
    draw.ellipse([32, 32, 38, 38], fill=BLACK)
    draw.ellipse([34, 34, 36, 36], fill=GREY)

# 18. Tractor
def draw_tractor(draw):
    # green engine body
    draw.rectangle([10, 24, 26, 38], fill=GREEN)
    draw.rectangle([10, 30, 26, 38], fill=DKGREEN) # shadow
    # exhaust chimney
    draw.line([(14, 24), (14, 14)], fill=BLACK, width=2)
    draw.line([(14, 14), (16, 12)], fill=BLACK, width=2)
    # canopy
    draw.line([(28, 24), (28, 16)], fill=STEEL, width=2)
    draw.line([(20, 24), (20, 16)], fill=STEEL, width=1)
    draw.rectangle([18, 14, 32, 16], fill=YELLOW)
    # small front wheel, large rear wheel
    draw.ellipse([12, 34, 18, 40], fill=BLACK)
    draw.ellipse([14, 36, 16, 38], fill=YELLOW)
    draw.ellipse([24, 22, 42, 40], fill=BLACK)
    draw.ellipse([29, 27, 37, 35], fill=YELLOW)

# 19. Forklift
def draw_forklift(draw):
    # yellow cabin cage
    draw.rectangle([16, 20, 32, 38], fill=YELLOW)
    draw.rectangle([16, 28, 32, 38], fill=ORANGE) # lower shade
    draw.rectangle([20, 14, 28, 24], fill=(0,0,0,0), outline=BLACK, width=2) # cage
    # mast
    draw.line([(12, 14), (12, 38)], fill=BLACK, width=3)
    # front fork lift prongs carrying pallet
    draw.line([(12, 32), (6, 32)], fill=STEEL, width=3)
    draw.line([(12, 36), (6, 36)], fill=STEEL, width=3)
    draw.rectangle([2, 30, 5, 38], fill=BROWN) # box payload
    # wheels
    draw.ellipse([14, 34, 20, 40], fill=BLACK)
    draw.ellipse([16, 36, 18, 38], fill=SILVER)
    draw.ellipse([26, 34, 32, 40], fill=BLACK)
    draw.ellipse([28, 36, 30, 38], fill=SILVER)

# 20. Bulldozer
def draw_bulldozer(draw):
    draw.rectangle([16, 20, 36, 38], fill=YELLOW)
    draw.rectangle([16, 29, 36, 38], fill=BLACK) # engine grill / shadow
    # exhaust
    draw.line([(22, 20), (22, 12)], fill=BLACK, width=2)
    # front large metal blade plate
    draw.polygon([(14, 28), (4, 38), (14, 38)], fill=SILVER)
    draw.line([(16, 30), (10, 34)], fill=STEEL, width=2) # piston arm
    # continuous treads (caterpillar tracks)
    draw.rounded_rectangle([14, 32, 38, 42], radius=4, fill=BLACK)
    draw.ellipse([18, 35, 22, 39], fill=GREY)
    draw.ellipse([30, 35, 34, 39], fill=GREY)

# 21. Excavator
def draw_excavator(draw):
    draw.rectangle([16, 24, 34, 36], fill=YELLOW) # cab
    draw.rectangle([16, 30, 34, 36], fill=GREY) # turntable
    # long segmented crane arm and bucket shovel
    draw.line([(26, 24), (26, 12)], fill=STEEL, width=3)
    draw.line([(26, 12), (16, 8)], fill=STEEL, width=3)
    draw.line([(24, 18), (20, 10)], fill=SILVER, width=1) # hydraulic cylinder
    draw.polygon([(16, 8), (12, 14), (18, 14)], fill=ORANGE) # scoop
    draw.rounded_rectangle([14, 32, 36, 40], radius=3, fill=BLACK) # tracks

# 22. Steamroller
def draw_steamroller(draw):
    draw.rectangle([18, 20, 36, 38], fill=GREEN) # body
    # giant metal front roller drum
    draw.ellipse([6, 24, 22, 40], fill=GREY)
    draw.ellipse([9, 27, 19, 37], fill=SILVER)
    # canopy
    draw.line([(24, 20), (24, 12)], fill=BLACK, width=2)
    draw.rectangle([20, 12, 32, 14], fill=BLACK)
    # rear wheel
    draw.ellipse([28, 30, 36, 38], fill=BLACK) # smaller back tire
    draw.ellipse([30, 32, 34, 36], fill=YELLOW)

# 23. Golf Cart
def draw_golf_cart(draw):
    draw.rounded_rectangle([12, 24, 38, 38], radius=2, fill=GREEN)
    # interior
    draw.rectangle([20, 20, 24, 28], fill=BLACK) # steering wheel & seat
    # windshield poles & canopy roof
    draw.line([(16, 24), (18, 14)], fill=STEEL, width=2)
    draw.line([(32, 24), (30, 14)], fill=STEEL, width=2)
    draw.rectangle([14, 12, 34, 16], fill=WHITE)
    # clubs
    draw.rectangle([34, 24, 38, 32], fill=BROWN) # bag
    draw.line([(36, 24), (38, 18)], fill=SILVER, width=2)
    # wheels
    draw.ellipse([14, 34, 20, 40], fill=BLACK)
    draw.ellipse([16, 36, 18, 38], fill=SILVER)
    draw.ellipse([30, 34, 36, 40], fill=BLACK)
    draw.ellipse([32, 36, 34, 38], fill=SILVER)

# 24. Go-Kart
def draw_gokart(draw):
    # low tube frame bumpers
    draw.rectangle([8, 30, 42, 36], fill=BLUE)
    # seat and driver body block
    draw.rectangle([20, 22, 28, 32], fill=RED)
    draw.ellipse([22, 16, 28, 22], fill=YELLOW) # helmet
    draw.rectangle([24, 17, 28, 19], fill=BLACK) # visor
    # engine details
    draw.rectangle([30, 24, 34, 30], fill=STEEL)
    draw.line([(34, 26), (38, 22)], fill=SILVER, width=2) # tailpipe
    # wheels
    draw.ellipse([10, 28, 16, 34], fill=BLACK)
    draw.ellipse([32, 28, 38, 34], fill=BLACK)

# 25. Bicycle
def draw_bicycle(draw):
    # diamond frame
    draw.polygon([(16, 34), (25, 20), (34, 34)], fill=(0,0,0,0), outline=BLUE, width=2)
    draw.line([(25, 20), (14, 20)], fill=STEEL, width=2) # handlebars
    draw.rectangle([23, 18, 27, 20], fill=BROWN) # seat
    # two wheels
    draw.ellipse([8, 28, 20, 40], fill=(0,0,0,0), outline=BLACK, width=2)
    draw.ellipse([12, 32, 16, 36], fill=SILVER) # spoke hub
    draw.ellipse([28, 28, 40, 40], fill=(0,0,0,0), outline=BLACK, width=2)
    draw.ellipse([32, 32, 36, 36], fill=SILVER)

# 26. Motorcycle
def draw_motorcycle(draw):
    # sleek red frame & gas tank
    draw.ellipse([18, 22, 32, 30], fill=RED)
    draw.line([19, 23, 29, 23], fill=WHITE, width=2) # tank trim
    # engine block
    draw.rectangle([20, 29, 28, 35], fill=STEEL)
    draw.line([(28, 32), (38, 32)], fill=SILVER, width=2) # tailpipe
    # forks and wheels
    draw.line([(28, 22), (16, 34)], fill=STEEL, width=3)
    draw.ellipse([10, 28, 22, 40], fill=BLACK)
    draw.ellipse([14, 32, 18, 36], fill=SILVER)
    draw.ellipse([28, 28, 40, 40], fill=BLACK)
    draw.ellipse([32, 32, 36, 36], fill=SILVER)

# 27. Vespa Scooter
def draw_scooter(draw):
    draw.chord([12, 20, 24, 38], 0, 180, fill=LIGHTBLUE) # front shield
    draw.rounded_rectangle([20, 26, 38, 36], radius=4, fill=LIGHTBLUE)
    draw.rectangle([24, 24, 32, 27], fill=BROWN) # seat
    draw.ellipse([12, 20, 16, 24], fill=WHITE) # headlight
    # wheels
    draw.ellipse([14, 32, 20, 38], fill=BLACK)
    draw.ellipse([16, 34, 18, 36], fill=SILVER)
    draw.ellipse([30, 32, 36, 38], fill=BLACK)
    draw.ellipse([32, 34, 34, 36], fill=SILVER)

# 28. Segway
def draw_segway(draw):
    # platform base
    draw.rectangle([18, 38, 32, 42], fill=GREY)
    draw.line([20, 38, 30, 38], fill=DKGREY, width=2) # foot grip
    # upright steering handle pole
    draw.line([25, 14, 25, 38], fill=STEEL, width=2)
    draw.line([20, 14, 30, 14], fill=BLACK, width=2) # handle
    # left/right wheels side by side
    draw.ellipse([14, 34, 20, 44], fill=BLACK)
    draw.ellipse([16, 36, 18, 42], fill=SILVER)
    draw.ellipse([30, 34, 36, 44], fill=BLACK)
    draw.ellipse([32, 36, 34, 42], fill=SILVER)

# 29. Auto Rickshaw / Tuk Tuk
def draw_tuk_tuk(draw):
    # yellow cabin hood, three wheels
    draw.rounded_rectangle([12, 16, 38, 36], radius=4, fill=YELLOW)
    draw.rectangle([12, 26, 38, 36], fill=GREEN) # lower green section
    draw.rectangle([12, 20, 24, 28], fill=LIGHTBLUE) # front window
    draw.rectangle([26, 22, 34, 28], fill=BROWN) # passenger seat
    # front wheel
    draw.ellipse([14, 32, 19, 37], fill=BLACK)
    # rear wheel
    draw.ellipse([30, 32, 36, 37], fill=BLACK)

# 30. Hovercraft
def draw_hovercraft(draw):
    # black rubber air skirt at bottom
    draw.rounded_rectangle([8, 30, 42, 38], radius=4, fill=BLACK)
    draw.ellipse([12, 18, 38, 32], fill=WHITE) # body
    draw.line([16, 24, 34, 24], fill=RED, width=2) # red stripe
    # giant rear fan propellers
    draw.ellipse([30, 12, 38, 22], fill=GREY)
    draw.ellipse([32, 14, 36, 20], fill=BLACK)

# 31. Speed Boat
def draw_speed_boat(draw):
    # wedge hull cutting water
    draw.polygon([(4, 30), (36, 30), (44, 20), (36, 18), (4, 18)], fill=RED)
    draw.polygon([(4, 24), (36, 24), (40, 20), (36, 18), (4, 18)], fill=WHITE) # lower hull
    # glass windshield
    draw.polygon([(26, 20), (32, 20), (30, 14), (24, 14)], fill=LIGHTBLUE)
    # outboard motor
    draw.rectangle([2, 22, 5, 28], fill=BLACK)
    draw.ellipse([1, 28, 3, 31], fill=WHITE) # spray

# 32. Sailboat
def draw_sailboat(draw):
    draw.chord([10, 26, 40, 42], 0, 180, fill=BROWN) # wooden hull
    draw.line([10, 28, 40, 28], fill=WHITE, width=1) # waterline
    # tall mast
    draw.line([25, 6, 25, 30], fill=BLACK, width=2)
    # white triangular sails with red stripe
    draw.polygon([(25, 8), (14, 24), (25, 24)], fill=WHITE)
    draw.polygon([(25, 10), (34, 24), (25, 24)], fill=WHITE)
    draw.polygon([(25, 14), (32, 24), (25, 24)], fill=RED)

# 33. Submarine
def draw_submarine(draw):
    draw.ellipse([10, 20, 40, 34], fill=YELLOW)
    draw.ellipse([14, 22, 36, 32], fill=ORANGE) # shading panel
    # tower structure
    draw.rectangle([22, 12, 28, 20], fill=YELLOW)
    # L periscope line
    draw.line([(25, 12), (25, 6), (28, 6)], fill=GREY, width=2)
    # port holes
    draw.ellipse([16, 25, 19, 28], fill=LIGHTBLUE)
    draw.ellipse([24, 25, 27, 28], fill=LIGHTBLUE)
    # propeller
    draw.line([(10, 27), (8, 24)], fill=SILVER, width=2)
    draw.line([(10, 27), (8, 30)], fill=SILVER, width=2)

# 34. Cruise Ship
def draw_cruise_ship(draw):
    # giant white hull
    draw.rounded_rectangle([4, 22, 46, 38], radius=2, fill=WHITE)
    draw.rectangle([4, 30, 46, 36], fill=DKBLUE) # bottom hull strip
    draw.rectangle([4, 36, 46, 38], fill=RED) # red waterline
    # cabins tiers
    draw.rectangle([10, 16, 40, 22], fill=WHITE)
    draw.rectangle([14, 12, 36, 16], fill=WHITE)
    # tiny window port holes
    for px in range(12, 42, 6):
        draw.ellipse([px, 25, px+2, 27], fill=YELLOW)
    # funnels
    draw.rectangle([20, 8, 24, 12], fill=RED)
    draw.rectangle([20, 6, 24, 8], fill=BLACK)

# 35. Jet Ski
def draw_jet_ski(draw):
    # tiny speed boat wedge
    draw.polygon([(8, 32), (32, 32), (40, 24), (32, 24)], fill=ORANGE)
    draw.polygon([(8, 28), (32, 28), (36, 24), (32, 24)], fill=WHITE)
    draw.rectangle([20, 20, 28, 24], fill=BLACK) # seat handlebars
    # splash
    draw.ellipse([4, 30, 7, 33], fill=LIGHTBLUE)
    draw.ellipse([2, 32, 5, 35], fill=WHITE)

# 36. Kayak
def draw_kayak(draw):
    # long slender double pointed canoe
    draw.ellipse([4, 22, 46, 28], fill=ORANGE)
    draw.ellipse([20, 23, 30, 27], fill=BLACK) # cockpit
    # center paddle crossed
    draw.line([20, 12, 30, 36], fill=BROWN, width=2)
    draw.rectangle([19, 10, 21, 14], fill=SILVER) # blades
    draw.rectangle([29, 34, 31, 38], fill=SILVER)

# 37. Cargo Container Ship
def draw_cargo_ship(draw):
    # red container hull
    draw.rectangle([6, 28, 44, 38], fill=DKRED)
    draw.rectangle([6, 36, 44, 38], fill=BLACK) # bottom
    # stacked colorful cargo boxes
    draw.rectangle([10, 18, 18, 28], fill=BLUE)
    draw.rectangle([18, 22, 26, 28], fill=YELLOW)
    draw.rectangle([26, 18, 34, 28], fill=GREEN)
    draw.rectangle([34, 22, 40, 28], fill=ORANGE)
    # superstructure
    draw.rectangle([38, 18, 44, 28], fill=WHITE)
    draw.rectangle([40, 16, 43, 18], fill=WHITE) # bridge

# 38. Helicopter
def draw_helicopter(draw):
    # round cabin
    draw.ellipse([14, 18, 34, 32], fill=BLUE)
    draw.ellipse([16, 20, 32, 30], fill=DKBLUE) # shading
    draw.ellipse([26, 20, 32, 26], fill=LIGHTBLUE) # window
    draw.line([(28, 20), (32, 24)], fill=WHITE, width=1) # shine
    # tail boom & rotor
    draw.line([(14, 25), (4, 22)], fill=BLUE, width=3)
    draw.line([(4, 18), (4, 26)], fill=BLACK, width=1)
    # landing skids
    draw.line([(18, 32), (18, 36)], fill=STEEL, width=2)
    draw.line([(30, 32), (30, 36)], fill=STEEL, width=2)
    draw.line([(14, 36), (36, 36)], fill=GREY, width=2)
    # main rotor
    draw.line([(24, 18), (24, 14)], fill=STEEL, width=2)
    draw.line([(12, 14), (36, 14)], fill=GREY, width=2)

# 39. Biplane
def draw_biplane(draw):
    # fuselage propeller plane
    draw.ellipse([10, 20, 40, 28], fill=RED)
    draw.ellipse([10, 20, 15, 28], fill=YELLOW) # engine cowl
    # double parallel wing layers
    draw.line([20, 12, 36, 12], fill=WHITE, width=2)
    draw.line([20, 32, 36, 32], fill=WHITE, width=2)
    # struts
    draw.line([(24, 12), (24, 32)], fill=BLACK, width=1)
    draw.line([(32, 12), (32, 32)], fill=BLACK, width=1)
    # propeller spinner
    draw.line([(9, 18), (9, 30)], fill=GREY, width=1)
    draw.ellipse([8, 22, 10, 26], fill=SILVER)

# 40. Fighter Jet
def draw_jet_fighter(draw):
    # sleek grey delta wings shape
    draw.polygon([(25, 4), (16, 32), (25, 42), (34, 32)], fill=GREY)
    draw.polygon([(25, 12), (18, 32), (25, 40), (32, 32)], fill=DKGREY) # camo patterns
    draw.polygon([(22, 28), (28, 28), (25, 20)], fill=ORANGE) # gold canopy
    # wingtip rockets
    draw.rectangle([14, 30, 16, 36], fill=WHITE)
    draw.rectangle([14, 30, 16, 32], fill=RED)
    draw.rectangle([34, 30, 36, 36], fill=WHITE)
    draw.rectangle([34, 30, 36, 32], fill=RED)
    # exhaust flames
    draw.polygon([(23, 42), (27, 42), (25, 48)], fill=RED)

# 41. Hot Air Balloon
def draw_hot_air_balloon(draw):
    # striped teardrop balloon
    draw.ellipse([14, 6, 36, 30], fill=RED)
    draw.chord([18, 16, 32, 32], 0, 180, fill=YELLOW)
    draw.ellipse([22, 8, 28, 28], fill=BLUE) # vertical stripe
    # burner fire
    draw.polygon([(23, 33), (27, 33), (25, 30)], fill=ORANGE)
    # hanging basket
    draw.rectangle([22, 36, 28, 42], fill=BROWN)
    draw.line([(22, 30), (22, 36)], fill=BLACK, width=1)
    draw.line([(28, 30), (28, 36)], fill=BLACK, width=1)

# 42. Blimp / Airship
def draw_blimp(draw):
    # oval balloon
    draw.ellipse([6, 12, 44, 28], fill=GREY)
    draw.line([6, 20, 44, 20], fill=RED, width=3) # stripe
    # tail fins
    draw.polygon([(6, 16), (2, 10), (10, 16)], fill=RED)
    draw.polygon([(6, 24), (2, 30), (10, 24)], fill=RED)
    # tiny gondola below
    draw.rectangle([20, 28, 30, 32], fill=WHITE)
    draw.ellipse([28, 29, 31, 31], fill=BLACK) # prop

# 43. Passenger Airliner
def draw_passenger_plane(draw):
    # long fuselage tube
    draw.ellipse([4, 22, 46, 28], fill=WHITE)
    draw.line([6, 25, 44, 25], fill=BLUE, width=1) # cheatline
    # sweeping back wings
    draw.polygon([(20, 24), (28, 24), (12, 38)], fill=GREY)
    draw.polygon([(20, 24), (28, 24), (38, 10)], fill=GREY)
    # engines
    draw.rectangle([22, 28, 26, 32], fill=DKGREY)
    draw.rectangle([22, 18, 26, 22], fill=DKGREY)

# 44. Space Shuttle
def draw_space_shuttle(draw):
    # white wings and body
    draw.polygon([(25, 4), (12, 36), (38, 36)], fill=WHITE)
    draw.polygon([(22, 4), (28, 4), (25, 10)], fill=BLACK) # heat shield nose
    draw.polygon([(20, 32), (30, 32), (25, 14)], fill=WHITE) # fuselage
    draw.line([(12, 34), (38, 34)], fill=BLACK, width=2) # wing edges
    # booster exhausts
    draw.rectangle([19, 36, 22, 40], fill=ORANGE)
    draw.rectangle([28, 36, 31, 40], fill=ORANGE)
    draw.polygon([(20, 40), (30, 40), (25, 46)], fill=YELLOW)

# 45. Steam Locomotive Train
def draw_train_locomotive(draw):
    # boiler
    draw.rectangle([10, 22, 32, 38], fill=BLACK)
    draw.line([14, 22, 14, 38], fill=YELLOW, width=1) # bands
    draw.line([22, 22, 22, 38], fill=YELLOW, width=1)
    # chimney stack
    draw.rectangle([14, 14, 18, 22], fill=BLACK)
    # steam cloud
    draw.ellipse([10, 6, 16, 12], fill=GREY)
    draw.ellipse([6, 2, 12, 8], fill=WHITE)
    # red driver cab at rear
    draw.rectangle([30, 16, 42, 38], fill=RED)
    draw.rectangle([32, 20, 38, 26], fill=YELLOW) # cab window
    # wheels with connecting rod
    draw.ellipse([12, 34, 20, 42], fill=RED)
    draw.ellipse([24, 32, 36, 44], fill=RED)
    draw.line([(16, 38), (30, 38)], fill=SILVER, width=2)

# 46. Bullet Train
def draw_bullet_train(draw):
    # sleek streamlined bullet nose
    draw.polygon([(4, 28), (20, 28), (26, 36), (4, 36)], fill=WHITE)
    draw.rectangle([20, 24, 46, 36], fill=WHITE)
    # blue stripe
    draw.line([4, 32, 46, 32], fill=BLUE, width=2)
    # front cockpit window slope
    draw.polygon([(6, 28), (14, 28), (18, 31), (6, 31)], fill=BLACK)
    # roof pantograph
    draw.line([(34, 24), (36, 20), (40, 20)], fill=GREY, width=2)

# 47. Electric Tram Streetcar
def draw_tram(draw):
    draw.rounded_rectangle([8, 16, 42, 38], radius=2, fill=GREEN)
    draw.rectangle([8, 16, 42, 20], fill=WHITE) # roof
    # window grid
    for wx in range(12, 40, 6):
        draw.rectangle([wx, 22, wx+4, 28], fill=LIGHTBLUE)
    # pantograph rod
    draw.line([25, 16, 22, 10], fill=STEEL, width=2)
    draw.line([22, 10, 28, 10], fill=BLACK, width=2)
    # lights
    draw.ellipse([10, 32, 12, 34], fill=YELLOW)

# 48. Cable Car
def draw_cable_car(draw):
    draw.rounded_rectangle([8, 16, 42, 38], radius=2, fill=BROWN)
    draw.rectangle([8, 28, 42, 38], fill=RED) # lower section
    # open sides with posts
    for px in range(12, 40, 8):
        draw.line([px, 20, px, 30], fill=YELLOW, width=2)
    # white roof
    draw.rectangle([6, 14, 44, 17], fill=WHITE)
    # wheels
    draw.ellipse([14, 36, 20, 42], fill=BLACK)
    draw.ellipse([30, 36, 36, 42], fill=BLACK)

# 49. Monorail
def draw_monorail(draw):
    # capsule wrapping train car
    draw.rounded_rectangle([6, 18, 44, 32], radius=4, fill=WHITE)
    draw.rectangle([10, 22, 40, 26], fill=BLACK) # windows
    draw.line([6, 29, 44, 29], fill=BLUE, width=1) # accent stripe
    # straddling concrete beam track line underneath
    draw.line([4, 32, 46, 32], fill=GREY, width=3)

# 50. Hoverboard
def draw_hoverboard(draw):
    # sleek neon deck
    draw.rounded_rectangle([8, 22, 42, 28], radius=2, fill=PURPLE)
    draw.line([12, 25, 38, 25], fill=ORANGE, width=1) # stripe decal
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
