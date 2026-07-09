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
    # spokes
    draw.line([25, 28, 25, 42], fill=SILVER, width=1)
    draw.line([18, 35, 32, 35], fill=SILVER, width=1)
    # frame & pedal fork
    draw.line([25, 20, 25, 35], fill=BLUE, width=2)
    # pedals
    draw.rectangle([21, 33, 29, 36], fill=ORANGE)
    # seat
    draw.ellipse([20, 17, 30, 21], fill=BROWN)

# 2. Tandem Bicycle
def draw_tandem_bicycle(draw):
    draw.ellipse([6, 28, 18, 40], fill=(0,0,0,0), outline=BLACK, width=2)
    draw.ellipse([10, 32, 14, 36], fill=SILVER) # spoke hub
    draw.ellipse([32, 28, 44, 40], fill=(0,0,0,0), outline=BLACK, width=2)
    draw.ellipse([36, 32, 40, 36], fill=SILVER)
    # double diamond frame
    draw.line([(12, 34), (20, 20), (28, 34)], fill=RED, width=2)
    draw.line([(28, 34), (36, 20), (38, 34)], fill=RED, width=2)
    draw.line([(20, 20), (36, 20)], fill=RED, width=2)
    # gears
    draw.ellipse([25, 32, 29, 36], fill=STEEL)
    # seats & bars
    draw.ellipse([18, 18, 22, 21], fill=BROWN)
    draw.ellipse([34, 18, 38, 21], fill=BROWN)
    draw.line([(20, 20), (18, 16)], fill=STEEL, width=2)
    draw.line([(36, 20), (34, 16)], fill=STEEL, width=2)

# 3. Penny Farthing
def draw_penny_farthing(draw):
    draw.ellipse([6, 16, 32, 42], fill=(0,0,0,0), outline=BLACK, width=2) # big wheel
    draw.ellipse([17, 27, 21, 31], fill=SILVER) # big hub
    draw.ellipse([38, 34, 44, 40], fill=(0,0,0,0), outline=BLACK, width=2) # small wheel
    draw.ellipse([40, 36, 42, 38], fill=SILVER)
    # frame curve
    draw.arc([14, 12, 40, 36], 180, 270, fill=BLUE, width=2)
    draw.line([18, 16, 18, 28], fill=STEEL, width=2) # fork
    draw.ellipse([14, 10, 18, 13], fill=BROWN) # high seat
    # bars and bell
    draw.line([18, 16, 22, 12], fill=STEEL, width=2)
    draw.ellipse([22, 10, 24, 12], fill=YELLOW) # bell

# 4. Dirt Bike
def draw_dirt_bike(draw):
    draw.rectangle([10, 38, 38, 40], fill=GREY) # shadow
    # frame and engine
    draw.polygon([(20, 20), (28, 20), (30, 30), (16, 30)], fill=ORANGE)
    draw.rectangle([20, 26, 28, 32], fill=STEEL) # engine block
    # high mudguards and plate
    draw.line([(10, 24), (16, 28)], fill=ORANGE, width=3)
    draw.rectangle([18, 15, 23, 20], fill=WHITE) # plate
    # high tailpipe
    draw.line([(28, 26), (36, 22)], fill=SILVER, width=2)
    # wheels
    draw.ellipse([8, 28, 20, 40], fill=BLACK)
    draw.ellipse([12, 32, 16, 36], fill=SILVER)
    draw.ellipse([28, 28, 40, 40], fill=BLACK)
    draw.ellipse([32, 32, 36, 36], fill=SILVER)

# 5. Chopper Motorcycle
def draw_chopper_motorcycle(draw):
    # engine V twin
    draw.rectangle([20, 26, 28, 32], fill=STEEL)
    draw.line([(20, 28), (28, 32)], fill=SILVER, width=2)
    draw.line([(20, 32), (28, 28)], fill=SILVER, width=2)
    # long front fork
    draw.line([(14, 34), (32, 12)], fill=SILVER, width=2)
    # tank and seat
    draw.ellipse([22, 22, 30, 28], fill=BLACK) # tank
    draw.line([23, 23, 29, 23], fill=RED, width=2) # flame decal
    draw.rounded_rectangle([18, 26, 32, 34], radius=3, fill=BROWN) # seat
    # pipes
    draw.line([(26, 32), (38, 32)], fill=SILVER, width=2)
    # wheels
    draw.ellipse([8, 28, 20, 40], fill=BLACK) # front wheel
    draw.ellipse([12, 32, 16, 36], fill=SILVER)
    draw.ellipse([28, 24, 42, 38], fill=BLACK) # fat rear wheel
    draw.ellipse([32, 28, 38, 34], fill=SILVER)

# 6. Snowmobile
def draw_snowmobile(draw):
    draw.rounded_rectangle([16, 22, 40, 34], radius=4, fill=BLUE)
    draw.line([18, 25, 38, 25], fill=WHITE, width=2) # stripe
    draw.rectangle([18, 18, 24, 23], fill=LIGHTBLUE) # windshield
    # front ski runners
    draw.line([(16, 34), (6, 34), (4, 30)], fill=BLACK, width=2)
    draw.line([(14, 28), (10, 34)], fill=STEEL, width=2) # strut
    draw.rectangle([11, 30, 13, 33], fill=RED) # shock
    # rear tread drive
    draw.rectangle([24, 30, 38, 36], fill=BLACK)

# 7. ATV (Quad Bike)
def draw_atv(draw):
    draw.rounded_rectangle([12, 20, 38, 32], radius=4, fill=RED)
    draw.rectangle([14, 18, 36, 22], fill=BLACK) # cargo racks
    draw.rectangle([20, 26, 30, 32], fill=STEEL) # motor
    # Knobby wheels
    draw.ellipse([6, 24, 18, 36], fill=BLACK)
    draw.ellipse([10, 28, 14, 32], fill=SILVER)
    draw.ellipse([28, 24, 40, 36], fill=BLACK)
    draw.ellipse([32, 28, 36, 32], fill=SILVER)
    draw.line([(16, 20), (20, 12)], fill=STEEL, width=3) # handlebars

# 8. Dune Buggy
def draw_dune_buggy(draw):
    # open frame cage
    draw.rectangle([14, 18, 36, 32], fill=(0,0,0,0), outline=YELLOW, width=2)
    # interior
    draw.rectangle([22, 25, 28, 30], fill=RED) # seat
    # engine
    draw.rectangle([32, 24, 36, 30], fill=STEEL)
    draw.line([(36, 26), (40, 22)], fill=SILVER, width=2)
    # wheels
    draw.ellipse([8, 28, 18, 38], fill=BLACK)
    draw.ellipse([11, 31, 15, 35], fill=YELLOW)
    draw.ellipse([30, 26, 42, 38], fill=BLACK) # sand paddles rear
    draw.ellipse([34, 30, 38, 34], fill=YELLOW)

# 9. Ice Resurfacer
def draw_ice_resurfacer(draw):
    # blocky zamboni machine
    draw.rounded_rectangle([10, 16, 38, 38], radius=3, fill=WHITE)
    draw.rectangle([10, 28, 38, 38], fill=BLUE) # blue stripe
    draw.rectangle([26, 10, 34, 20], fill=BLUE) # driver cab
    draw.ellipse([28, 12, 30, 15], fill=BLACK) # wheel
    # conditioner board
    draw.rectangle([6, 34, 11, 38], fill=GREY)
    # wheels
    draw.ellipse([14, 32, 20, 38], fill=BLACK)
    draw.ellipse([16, 34, 18, 36], fill=SILVER)
    draw.ellipse([28, 32, 34, 38], fill=BLACK)
    draw.ellipse([29, 34, 33, 36], fill=SILVER)

# 10. Street Sweeper
def draw_street_sweeper(draw):
    draw.rounded_rectangle([10, 18, 38, 38], radius=2, fill=WHITE)
    draw.rectangle([12, 22, 20, 28], fill=LIGHTBLUE) # window
    draw.rectangle([26, 20, 36, 30], fill=GREEN) # hopper panel
    # sweeping brushes
    draw.ellipse([8, 34, 16, 40], fill=ORANGE)
    draw.line([(12, 34), (16, 30)], fill=STEEL, width=2)
    # beacon
    draw.ellipse([14, 14, 18, 18], fill=YELLOW)
    # wheels
    draw.ellipse([14, 32, 20, 38], fill=BLACK)
    draw.ellipse([28, 32, 34, 38], fill=BLACK)

# 11. Tow Truck
def draw_tow_truck(draw):
    draw.rectangle([6, 22, 18, 38], fill=BLUE) # cab
    draw.rectangle([8, 24, 14, 29], fill=LIGHTBLUE)
    draw.ellipse([12, 18, 16, 22], fill=YELLOW) # beacon
    # flatbed and towing crane arm at back
    draw.rectangle([18, 28, 44, 38], fill=GREY)
    draw.line([(28, 28), (40, 16)], fill=STEEL, width=3) # tow arm
    draw.line([(40, 16), (42, 24)], fill=SILVER, width=1) # cable
    draw.ellipse([41, 24, 43, 27], fill=SILVER) # hook
    # towed car silhouette
    draw.polygon([(40, 34), (46, 34), (44, 28)], fill=RED)
    # wheels
    draw.ellipse([10, 32, 16, 38], fill=BLACK)
    draw.ellipse([12, 34, 14, 36], fill=SILVER)
    draw.ellipse([32, 32, 38, 38], fill=BLACK)
    draw.ellipse([34, 34, 36, 36], fill=SILVER)

# 12. Tanker Truck
def draw_tank_truck(draw):
    draw.rectangle([6, 22, 16, 38], fill=RED) # cab
    draw.rectangle([6, 28, 16, 38], fill=BLACK) # grill
    # cylindrical steel liquid tank
    draw.rounded_rectangle([16, 18, 44, 38], radius=4, fill=SILVER)
    draw.rectangle([16, 28, 44, 38], fill=GREY) # tank bottom shade
    # orange hazard placard diamond
    draw.polygon([(28, 26), (32, 22), (36, 26), (32, 30)], fill=ORANGE)
    # wheels
    draw.ellipse([10, 32, 16, 38], fill=BLACK)
    draw.ellipse([24, 32, 30, 38], fill=BLACK)
    draw.ellipse([26, 34, 28, 36], fill=SILVER)
    draw.ellipse([34, 32, 40, 38], fill=BLACK)
    draw.ellipse([36, 34, 38, 36], fill=SILVER)

# 13. Car Transporter
def draw_car_transporter(draw):
    draw.rectangle([4, 24, 12, 38], fill=BLUE) # cab
    # double tier trailer displaying mini car
    draw.line([12, 26, 46, 26], fill=STEEL, width=2)
    draw.line([12, 34, 46, 34], fill=STEEL, width=2)
    # cars
    draw.rounded_rectangle([20, 20, 30, 25], radius=2, fill=RED) # red top car
    draw.rounded_rectangle([28, 28, 38, 33], radius=2, fill=YELLOW) # yellow bottom car
    # wheels
    draw.ellipse([14, 34, 18, 38], fill=BLACK)
    draw.ellipse([38, 34, 42, 38], fill=BLACK)

# 14. Logging Truck
def draw_logging_truck(draw):
    draw.rectangle([6, 22, 16, 38], fill=YELLOW) # cab
    draw.rectangle([8, 24, 14, 29], fill=LIGHTBLUE)
    # flatbed loaded with brown logs
    draw.rectangle([16, 30, 44, 38], fill=GREY)
    for y in [18, 22, 26]:
        draw.rounded_rectangle([18, y, 42, y+4], radius=1, fill=BROWN)
    # chains
    draw.line([(24, 18), (24, 30)], fill=BLACK, width=1)
    draw.line([(34, 18), (34, 30)], fill=BLACK, width=1)
    # wheels
    draw.ellipse([10, 32, 16, 38], fill=BLACK)
    draw.ellipse([30, 32, 36, 38], fill=BLACK)
    draw.ellipse([32, 34, 34, 36], fill=SILVER)

# 15. Armored Car
def draw_armored_car(draw):
    # secure green box van
    draw.rounded_rectangle([8, 18, 42, 38], radius=3, fill=DKGREEN)
    # rivets & panel lines
    for x in range(12, 42, 6):
        draw.ellipse([x, 20, x+1, 21], fill=GREY)
        draw.ellipse([x, 32, x+1, 33], fill=GREY)
    draw.rectangle([12, 22, 18, 25], fill=BLACK) # small window slit
    # wheels
    draw.ellipse([12, 34, 18, 40], fill=BLACK)
    draw.ellipse([14, 36, 16, 38], fill=DKGREEN)
    draw.ellipse([32, 34, 38, 40], fill=BLACK)
    draw.ellipse([34, 36, 36, 38], fill=DKGREEN)

# 16. Ice Cream Truck
def draw_ice_cream_truck(draw):
    draw.rounded_rectangle([8, 16, 42, 38], radius=3, fill=WHITE)
    draw.rectangle([20, 20, 30, 28], fill=PINK) # serving hatch pink awning
    draw.rectangle([21, 23, 29, 28], fill=LIGHTBLUE) # window
    # giant ice cream cone sign on roof
    draw.polygon([(22, 12), (28, 12), (25, 16)], fill=BROWN)
    draw.ellipse([22, 6, 28, 12], fill=PINK)
    # menu lights
    draw.ellipse([12, 20, 14, 22], fill=RED)
    draw.ellipse([15, 20, 17, 22], fill=YELLOW)
    draw.ellipse([18, 20, 20, 22], fill=BLUE)
    # wheels
    draw.ellipse([12, 34, 18, 40], fill=BLACK)
    draw.ellipse([14, 36, 16, 38], fill=PINK)
    draw.ellipse([32, 34, 38, 40], fill=BLACK)
    draw.ellipse([34, 36, 36, 38], fill=PINK)

# 17. Food Truck
def draw_food_truck(draw):
    draw.rounded_rectangle([8, 16, 42, 38], radius=3, fill=ORANGE)
    draw.rectangle([8, 26, 42, 38], fill=WHITE) # two tone paint
    draw.rectangle([20, 20, 34, 28], fill=BLACK) # serving hatch open
    draw.rectangle([22, 22, 32, 28], fill=YELLOW) # lit inside
    # taco icon
    draw.ellipse([25, 8, 31, 14], fill=BROWN)
    # wheels
    draw.ellipse([12, 34, 18, 40], fill=BLACK)
    draw.ellipse([14, 36, 16, 38], fill=SILVER)
    draw.ellipse([32, 34, 38, 40], fill=BLACK)
    draw.ellipse([34, 36, 36, 38], fill=SILVER)

# 18. Camper Van (RV)
def draw_camper_van(draw):
    # large white RV body
    draw.rounded_rectangle([6, 16, 44, 38], radius=4, fill=WHITE)
    draw.rectangle([10, 20, 16, 26], fill=LIGHTBLUE) # cab window
    draw.rectangle([22, 20, 38, 26], fill=LIGHTBLUE) # living area window
    # green stripe
    draw.line([6, 30, 44, 30], fill=GREEN, width=2)
    # ladder at back
    draw.line([42, 18, 42, 32], fill=STEEL, width=2)
    for ly in range(20, 32, 4):
        draw.line([41, ly, 43, ly], fill=STEEL, width=1)
    # wheels
    draw.ellipse([12, 34, 18, 40], fill=BLACK)
    draw.ellipse([14, 36, 16, 38], fill=SILVER)
    draw.ellipse([32, 34, 38, 40], fill=BLACK)
    draw.ellipse([34, 36, 36, 38], fill=SILVER)

# 19. Milk Float
def draw_milk_float(draw):
    # open sided white delivery cart
    draw.rectangle([8, 22, 16, 38], fill=WHITE) # cab
    draw.rectangle([10, 24, 14, 29], fill=LIGHTBLUE)
    # open shelves carrying white bottles
    draw.rectangle([16, 28, 42, 38], fill=GREY)
    for bx in [20, 26, 32, 38]:
        draw.rectangle([bx-1, 22, bx+1, 28], fill=WHITE) # bottles
        draw.rectangle([bx-1, 22, bx+1, 23], fill=RED) # caps
    # wheels
    draw.ellipse([10, 34, 16, 40], fill=BLACK)
    draw.ellipse([32, 34, 38, 40], fill=BLACK)

# 20. Electric Unicycle (OneWheel)
def draw_electric_unicycle(draw):
    # central wheel wrapped by deck
    draw.ellipse([20, 26, 30, 36], fill=BLACK)
    draw.ellipse([23, 29, 27, 33], fill=SILVER)
    # platform
    draw.line([12, 28, 38, 28], fill=BLUE, width=3)
    draw.line([12, 29, 38, 29], fill=STEEL, width=1)
    # LED
    draw.ellipse([13, 26, 15, 28], fill=WHITE)

# 21. Electric Scooter (Kick)
def draw_electric_scooter(draw):
    draw.line([16, 14, 16, 38], fill=BLACK, width=2) # steer pole
    draw.line([12, 14, 20, 14], fill=BLACK, width=2) # bar
    draw.line([16, 38, 36, 38], fill=GREY, width=3) # deck
    # lights
    draw.ellipse([17, 13, 19, 15], fill=WHITE) # headlight
    draw.ellipse([35, 36, 37, 38], fill=RED) # tail
    # wheels
    draw.ellipse([14, 36, 18, 40], fill=BLACK)
    draw.ellipse([34, 36, 38, 40], fill=BLACK)

# 22. Pulled Rickshaw
def draw_rickshaw(draw):
    # wooden carriage seat
    draw.rectangle([20, 22, 34, 32], fill=RED)
    draw.rectangle([20, 22, 34, 25], fill=BLACK) # trim
    draw.rectangle([14, 14, 34, 22], fill=YELLOW) # canopy hood
    # pull bars
    draw.line([(20, 30), (6, 34)], fill=BROWN, width=2)
    # large wooden wheels
    draw.ellipse([22, 28, 32, 38], fill=(0,0,0,0), outline=BROWN, width=2)

# 23. Horse Carriage
def draw_carriage(draw):
    # vintage luxury coach cabin
    draw.rounded_rectangle([18, 16, 42, 32], radius=4, fill=PURPLE)
    # gold trim windows
    draw.rectangle([24, 20, 36, 26], fill=RED) # seats inside
    draw.rectangle([24, 20, 36, 26], fill=(0,0,0,0), outline=YELLOW, width=2) # gold window frame
    # giant wooden wheels
    draw.ellipse([14, 28, 22, 36], fill=(0,0,0,0), outline=BROWN, width=2)
    draw.ellipse([36, 28, 44, 36], fill=(0,0,0,0), outline=BROWN, width=2)

# 24. Sleigh
def draw_sleigh(draw):
    # red curved carriage tub
    draw.polygon([(10, 20), (38, 20), (36, 32), (14, 32)], fill=RED)
    draw.line([10, 20, 38, 20], fill=YELLOW, width=2) # gold trim
    # cargo
    draw.rectangle([18, 15, 26, 20], fill=GREEN) # gifts
    draw.line([22, 13, 22, 20], fill=YELLOW, width=1)
    # curved runner skids below
    draw.arc([8, 28, 42, 38], 0, 180, fill=SILVER, width=2)
    draw.line([(8, 30), (6, 26)], fill=SILVER, width=2)

# 25. Dog Sled
def draw_dog_sled(draw):
    # wooden slatted sled
    draw.line([14, 34, 44, 34], fill=BROWN, width=3)
    draw.line([(44, 34), (46, 28)], fill=BROWN, width=2) # front curve
    # cargo bags
    draw.rounded_rectangle([20, 28, 36, 34], radius=2, fill=BLACK)
    # handlebar uprights
    draw.line([(16, 34), (16, 22)], fill=BROWN, width=2)
    draw.line([(16, 22), (20, 22)], fill=BROWN, width=2)
    # harness rope
    draw.line([(44, 34), (50, 32)], fill=STEEL, width=1)

# 26. Railroad Handcar
def draw_handcar(draw):
    # flat rolling platform on tracks
    draw.rectangle([10, 32, 40, 36], fill=BROWN)
    # seesaw pump lever in middle
    draw.line([25, 22, 25, 32], fill=STEEL, width=2)
    draw.line([20, 22, 30, 26], fill=BLACK, width=2) # lever crossbar
    # wheels on rail track
    draw.line([4, 40, 46, 40], fill=STEEL, width=1) # track rail
    draw.ellipse([14, 34, 20, 40], fill=DKGREY)
    draw.ellipse([30, 34, 36, 40], fill=DKGREY)

# 27. Trolley Bus
def draw_trolley_bus(draw):
    draw.rounded_rectangle([8, 16, 42, 38], radius=3, fill=BLUE)
    draw.rectangle([8, 16, 42, 20], fill=WHITE) # roof
    draw.rectangle([10, 22, 18, 28], fill=LIGHTBLUE) # windows
    draw.rectangle([22, 22, 30, 28], fill=LIGHTBLUE)
    # overhead wires contact poles
    draw.line([(20, 16), (10, 6)], fill=BLACK, width=2)
    draw.line([(24, 16), (14, 6)], fill=BLACK, width=2)
    # wheels
    draw.ellipse([12, 34, 18, 40], fill=BLACK)
    draw.ellipse([14, 36, 16, 38], fill=SILVER)
    draw.ellipse([32, 34, 38, 40], fill=BLACK)
    draw.ellipse([34, 36, 36, 38], fill=SILVER)

# 28. Steam Wagon
def draw_steam_wagon(draw):
    draw.rectangle([14, 22, 36, 38], fill=DKRED)
    # vertical boiler at front
    draw.rectangle([10, 16, 16, 34], fill=GREY)
    draw.rectangle([10, 22, 16, 24], fill=YELLOW) # brass trim
    # metal chimney tip
    draw.rectangle([12, 10, 14, 16], fill=BLACK)
    draw.ellipse([10, 4, 16, 10], fill=WHITE) # steam puff
    # wheels
    draw.ellipse([12, 32, 18, 38], fill=BLACK)
    draw.ellipse([14, 34, 16, 36], fill=SILVER)
    draw.ellipse([28, 32, 34, 38], fill=BLACK)
    draw.ellipse([29, 34, 33, 36], fill=SILVER)

# 29. Paddle Steamer
def draw_paddle_steamer(draw):
    draw.rectangle([6, 26, 44, 36], fill=WHITE) # hull
    draw.rectangle([6, 34, 44, 36], fill=DKBLUE) # bottom
    # paddle wheel
    draw.ellipse([34, 24, 46, 36], fill=(0,0,0,0), outline=RED, width=3)
    # water splash
    draw.ellipse([40, 32, 45, 35], fill=LIGHTBLUE)
    # steam chimneys
    draw.line([16, 12, 16, 26], fill=BLACK, width=2)
    draw.line([24, 12, 24, 26], fill=BLACK, width=2)

# 30. Rowboat
def draw_rowboat(draw):
    draw.chord([10, 22, 40, 36], 0, 180, fill=BROWN)
    draw.rectangle([15, 27, 35, 29], fill=BROWN) # bench seats
    # crossed oars
    draw.line([14, 18, 28, 34], fill=TAN, width=1)
    draw.line([36, 18, 22, 34], fill=TAN, width=1)
    # oar locks
    draw.ellipse([20, 25, 22, 27], fill=STEEL)
    draw.ellipse([28, 25, 30, 27], fill=STEEL)

# 31. Gondola Boat
def draw_gondola_boat(draw):
    # sleek curved Venetian boat black hull
    draw.arc([6, 12, 44, 36], 0, 180, fill=BLACK, width=3)
    # seat
    draw.rectangle([20, 28, 30, 31], fill=RED)
    # curved metal bow decoration
    draw.line([(6, 24), (4, 16)], fill=SILVER, width=2)
    draw.line([(4, 16), (2, 16)], fill=SILVER, width=2)

# 32. Canoe
def draw_canoe(draw):
    # long pointed double-ended boat
    draw.ellipse([6, 24, 44, 30], fill=RED)
    draw.ellipse([10, 25, 40, 29], fill=TAN) # inner wood frame
    draw.line([18, 27, 28, 27], fill=BROWN, width=1) # paddle lying inside

# 33. Jetfoil (Hydrofoil)
def draw_jetfoil(draw):
    draw.rounded_rectangle([10, 20, 40, 30], radius=2, fill=WHITE)
    # underwater wing foil legs
    draw.line([(14, 30), (14, 38)], fill=SILVER, width=2)
    draw.line([(36, 30), (36, 38)], fill=SILVER, width=2)
    # winglets
    draw.line([10, 38, 18, 38], fill=STEEL, width=2)
    draw.line([32, 38, 40, 38], fill=STEEL, width=2)
    # water spray
    draw.ellipse([14, 37, 18, 40], fill=LIGHTBLUE)
    draw.ellipse([32, 37, 36, 40], fill=LIGHTBLUE)

# 34. Catamaran
def draw_catamaran(draw):
    # twin parallel pontoons
    draw.rounded_rectangle([8, 30, 14, 36], radius=1, fill=WHITE)
    draw.rounded_rectangle([36, 30, 42, 36], radius=1, fill=WHITE)
    # bridge deck connecting them
    draw.rectangle([14, 26, 36, 32], fill=GREY)
    # sail mast
    draw.line([25, 8, 25, 26], fill=BLACK, width=2)
    draw.polygon([(25, 10), (16, 24), (25, 24)], fill=BLUE) # blue/white sail
    draw.polygon([(25, 12), (20, 24), (25, 24)], fill=WHITE)

# 35. Aircraft Carrier
def draw_aircraft_carrier(draw):
    # massive flat deck hull
    draw.polygon([(4, 26), (42, 26), (46, 22), (42, 18), (4, 18)], fill=DKGREY)
    draw.line([6, 20, 38, 20], fill=YELLOW, width=1) # deck runway markings
    # tiny tower island on side
    draw.rectangle([32, 12, 36, 18], fill=GREY)
    draw.rectangle([33, 9, 35, 12], fill=WHITE) # radar
    # miniature plane cross on deck
    draw.line([(18, 22), (22, 22)], fill=GREY, width=1)
    draw.line([(20, 20), (20, 24)], fill=GREY, width=1)

# 36. Tugboat
def draw_tugboat(draw):
    # stout red hull
    draw.chord([8, 22, 38, 40], 0, 180, fill=RED)
    # tires hanging on sides
    draw.ellipse([14, 30, 18, 34], fill=BLACK)
    draw.ellipse([28, 30, 32, 34], fill=BLACK)
    # fat pilot house
    draw.rounded_rectangle([16, 16, 30, 28], radius=2, fill=WHITE)
    draw.rectangle([18, 18, 22, 22], fill=LIGHTBLUE) # window
    # black smokestack with puff
    draw.rectangle([24, 10, 28, 16], fill=BLACK)

# 37. Barge
def draw_barge(draw):
    # flat cargo barge
    draw.rectangle([6, 28, 44, 38], fill=DKGREY)
    # sand stack heap & gravel stack
    draw.polygon([(10, 28), (22, 16), (34, 28)], fill=TAN) # sand
    draw.polygon([(24, 28), (34, 18), (42, 28)], fill=GREY) # gravel

# 38. Lifeboat
def draw_lifeboat(draw):
    # bright orange rescue boat
    draw.chord([8, 22, 42, 40], 0, 180, fill=ORANGE)
    draw.line([8, 25, 42, 25], fill=BLUE, width=2) # blue fender line
    draw.rounded_rectangle([16, 18, 34, 28], radius=2, fill=WHITE) # cabin
    draw.rectangle([20, 20, 26, 24], fill=LIGHTBLUE)

# 39. Pirate Ship (Galleon)
def draw_pirate_ship(draw):
    draw.chord([8, 22, 38, 40], 0, 180, fill=BROWN) # hull
    # raised castle decks
    draw.rectangle([8, 18, 14, 24], fill=BROWN)
    draw.rectangle([32, 18, 38, 24], fill=BROWN)
    # masts and black sails with white cross skull
    draw.line([22, 8, 22, 24], fill=BLACK, width=2)
    draw.rectangle([18, 10, 26, 18], fill=BLACK)
    # skull decal
    draw.ellipse([21, 13, 23, 15], fill=WHITE)
    # rigging lines
    draw.line([(10, 18), (18, 10)], fill=GREY, width=1)
    draw.line([(36, 18), (26, 10)], fill=GREY, width=1)

# 40. Hang Glider
def draw_hang_glider(draw):
    # triangular sail wing
    draw.polygon([(25, 12), (10, 28), (40, 28)], fill=YELLOW)
    draw.polygon([(25, 12), (20, 28), (30, 28)], fill=ORANGE) # stripes
    # pilot harness hanging below
    draw.line([(25, 20), (25, 34)], fill=BLACK, width=2)
    draw.ellipse([23, 34, 27, 38], fill=RED) # pilot in suit

# 41. Paraglider
def draw_paraglider(draw):
    # curved canopy wing
    draw.arc([10, 8, 40, 24], 180, 360, fill=RED, width=3)
    draw.arc([12, 10, 38, 24], 180, 360, fill=WHITE, width=2)
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
    draw.rounded_rectangle([20, 28, 30, 34], radius=2, fill=BLACK) # cart body
    # motor/propeller
    draw.rectangle([18, 24, 22, 28], fill=STEEL)
    draw.line([(16, 26), (16, 20)], fill=SILVER, width=1) # spinner
    draw.ellipse([22, 34, 28, 40], fill=BLACK) # wheel

# 43. Glider Plane (Sailplane)
def draw_glider_plane(draw):
    # long slender wings
    draw.ellipse([18, 22, 32, 26], fill=WHITE) # fuselage
    draw.ellipse([24, 23, 28, 25], fill=LIGHTBLUE) # canopy bubble
    draw.line([4, 24, 46, 24], fill=WHITE, width=2) # wingspan
    draw.line([4, 24, 8, 24], fill=RED, width=2) # wingtip markers
    draw.line([42, 24, 46, 24], fill=RED, width=2)

# 44. Seaplane (Floatplane)
def draw_seaplane(draw):
    # propeller plane body
    draw.ellipse([14, 18, 36, 26], fill=YELLOW)
    draw.line([(13, 22), (10, 22)], fill=BLACK, width=2) # nose engine
    draw.line([(10, 18), (10, 26)], fill=GREY, width=1) # prop
    # double pontoon floats underneath
    draw.line([18, 32, 32, 32], fill=STEEL, width=2)
    draw.line([(22, 26), (22, 32)], fill=BLACK, width=1)
    draw.line([(28, 26), (28, 32)], fill=BLACK, width=1)

# 45. Chinook Helicopter
def draw_chinook_helicopter(draw):
    # long tandem rotor helicopter fuselage
    draw.rounded_rectangle([10, 20, 40, 30], radius=3, fill=DKGREY)
    draw.rectangle([14, 22, 16, 24], fill=BLACK) # windows
    draw.rectangle([22, 22, 24, 24], fill=BLACK)
    # twin rotors at front/rear top
    draw.line([(14, 20), (14, 14)], fill=BLACK, width=2)
    draw.line([(6, 14), (22, 14)], fill=GREY, width=1)
    draw.line([(36, 20), (36, 14)], fill=BLACK, width=2)
    draw.line([(28, 14), (44, 14)], fill=GREY, width=1)

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
    draw.line([25, 14, 25, 34], fill=BLUE, width=1) # stripe decal
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
    draw.rectangle([20, 14, 30, 18], fill=GREY) # ascent stage
    draw.rectangle([24, 15, 26, 17], fill=BLACK) # window
    # landing gear legs
    for lx, rx in [(14, 8), (36, 42)]:
        draw.line([(lx, 28), (rx, 38)], fill=STEEL, width=2)
        draw.ellipse([rx-2, 38, rx+2, 42], fill=SILVER) # landing pads

# 49. Hand Truck (Dolly)
def draw_hand_truck(draw):
    # vertical metal L frame
    draw.line([20, 14, 20, 38], fill=SILVER, width=3)
    draw.line([20, 38, 30, 38], fill=SILVER, width=3) # nose plate
    # cargo load (boxes)
    draw.rectangle([22, 28, 34, 37], fill=RED)
    draw.rectangle([22, 18, 30, 28], fill=BLUE)
    # wheels
    draw.ellipse([16, 36, 22, 42], fill=BLACK)

# 50. Snowplow
def draw_snowplow(draw):
    draw.rectangle([14, 20, 38, 36], fill=ORANGE) # truck cab
    draw.rectangle([16, 24, 24, 30], fill=LIGHTBLUE)
    # massive front angled wedge plow blade pushing snow
    draw.line([(14, 36), (4, 30)], fill=SILVER, width=4)
    draw.ellipse([1, 26, 6, 31], fill=WHITE) # snow pile
    # wheels
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
