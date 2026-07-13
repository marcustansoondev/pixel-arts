import os
from PIL import Image, ImageDraw
import numpy as np

OUTPUT_DIR = "images/vehicles"
os.makedirs(OUTPUT_DIR, exist_ok=True)

# Colors
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
DBROWN    = (80, 50, 25, 255)
PURPLE    = (130, 60, 180, 255)
LIGHTBLUE = (170, 220, 250, 255)
STEEL     = (120, 125, 135, 255)
SILVER    = (190, 190, 195, 255)
GOLD      = (215, 175, 45, 255)
SAND      = (220, 200, 160, 255)
TEAL      = (40, 160, 160, 255)
PINK      = (240, 140, 160, 255)

def _quantize_no_outline(img: Image.Image) -> Image.Image:
    arr = np.array(img.convert("RGBA"))
    alpha = arr[:, :, 3]
    new_alpha = alpha.copy()

    flat = Image.new("RGB", (50, 50), (255, 255, 255))
    composed = Image.fromarray(
        np.dstack((arr[:, :, :3], new_alpha)).astype(np.uint8), "RGBA"
    )
    flat.paste(composed, mask=Image.fromarray(new_alpha, "L"))

    q = flat.quantize(colors=9, method=Image.MEDIANCUT, dither=0)
    final = q.convert("RGBA")
    fa = np.array(final)
    fa[:, :, 3] = new_alpha
    return Image.fromarray(fa, "RGBA")

def create_sprite(name, draw_func):
    img = Image.new("RGBA", (50, 50), (255, 255, 255, 0))
    draw = ImageDraw.Draw(img)
    draw_func(draw)
    img = _quantize_no_outline(img)
    path = os.path.join(OUTPUT_DIR, f"{name}_50x50.png")
    img.save(path)

def draw_wheels(draw, w1_cx, w2_cx, cy=36, r=5, color=BLACK, hub_color=SILVER):
    draw.ellipse([w1_cx - r, cy - r, w1_cx + r, cy + r], fill=color)
    draw.ellipse([w1_cx - r/2.5, cy - r/2.5, w1_cx + r/2.5, cy + r/2.5], fill=hub_color)
    draw.ellipse([w2_cx - r, cy - r, w2_cx + r, cy + r], fill=color)
    draw.ellipse([w2_cx - r/2.5, cy - r/2.5, w2_cx + r/2.5, cy + r/2.5], fill=hub_color)

# Expanded generic helper for cars to add more detail consistently
def draw_detailed_car(draw, color, stripe, cabin_pts, body_box, whl1, whl2):
    # shadow/chassis
    draw.rectangle([body_box[0]+1, body_box[3]-1, body_box[2]-1, body_box[3]+1], fill=DKGREY)
    # roof / pillars
    draw.polygon(cabin_pts, fill=STEEL)
    # shrink cabin for window
    win = [(x, y+1) if y < 20 else (x+1 if x < 25 else x-1, y) for (x, y) in cabin_pts]
    draw.polygon(win, fill=LIGHTBLUE)
    # body
    draw.rounded_rectangle(body_box, radius=3, fill=color)
    # stripe
    if stripe:
        draw.rectangle([body_box[0], body_box[1]+4, body_box[2], body_box[1]+6], fill=stripe)
    # B-pillar
    cx = (cabin_pts[1][0] + cabin_pts[2][0]) // 2
    draw.line([cx, cabin_pts[1][1], cx, cabin_pts[0][1]], fill=STEEL, width=2)
    # Headlight / taillight
    draw.rectangle([body_box[0], body_box[1]+2, body_box[0]+3, body_box[1]+5], fill=SILVER)
    draw.rectangle([body_box[2]-3, body_box[1]+2, body_box[2], body_box[1]+5], fill=ORANGE)
    # door handles
    draw.rectangle([cx-4, body_box[1]+2, cx-2, body_box[1]+3], fill=SILVER)
    draw.rectangle([cx+2, body_box[1]+2, cx+4, body_box[1]+3], fill=SILVER)
    draw_wheels(draw, whl1, whl2)

def draw_coupe(d):
    draw_detailed_car(d, RED, DKRED, [(16, 24), (20, 16), (30, 16), (34, 24)], [9, 24, 41, 36], 15, 33)

def draw_hatchback(d):
    draw_detailed_car(d, GREEN, DKGREEN, [(12, 24), (16, 16), (32, 16), (38, 24)], [8, 24, 38, 36], 14, 32)

def draw_muscle_car(d):
    draw_detailed_car(d, BLACK, ORANGE, [(14, 22), (18, 16), (30, 16), (34, 22)], [8, 22, 42, 34], 14, 36)
    # extra scoop
    d.rectangle([34, 21, 38, 23], fill=GREY)

def draw_station_wagon(d):
    draw_detailed_car(d, BROWN, DBROWN, [(12, 22), (12, 16), (38, 16), (38, 22)], [8, 22, 42, 34], 14, 36)
    d.line([25, 16, 25, 22], fill=STEEL, width=2)

def draw_crossover_car(d):
    draw_detailed_car(d, GREY, DKGREY, [(14, 20), (18, 14), (32, 14), (36, 20)], [8, 20, 42, 34], 15, 35)

def draw_kei_truck(d):
    d.rectangle([10, 34, 40, 36], fill=DKGREY)
    d.rectangle([10, 18, 22, 34], fill=WHITE) # Cab
    d.rectangle([12, 20, 20, 26], fill=LIGHTBLUE) # window
    d.rectangle([15, 20, 17, 26], fill=STEEL) # pillar
    d.rectangle([22, 26, 40, 34], fill=STEEL) # bed
    d.rectangle([10, 28, 12, 30], fill=SILVER) # light
    d.rectangle([38, 28, 40, 30], fill=RED) # light
    draw_wheels(d, 15, 33)

def draw_panel_van(d):
    d.rectangle([10, 34, 40, 36], fill=DKGREY)
    d.rounded_rectangle([8, 18, 42, 34], radius=3, fill=WHITE)
    d.rectangle([8, 25, 42, 27], fill=BLUE)
    d.rectangle([10, 20, 18, 26], fill=LIGHTBLUE)
    d.rectangle([18, 20, 20, 26], fill=STEEL)
    d.rectangle([8, 28, 10, 31], fill=SILVER)
    d.rectangle([40, 28, 42, 31], fill=RED)
    draw_wheels(d, 15, 35)

def draw_step_van(d):
    d.rectangle([8, 34, 42, 36], fill=DKGREY)
    d.rectangle([8, 14, 38, 34], fill=YELLOW)
    d.rectangle([8, 24, 38, 26], fill=DKGREY)
    d.rectangle([10, 16, 18, 24], fill=LIGHTBLUE)
    d.rectangle([8, 28, 10, 30], fill=SILVER)
    draw_wheels(d, 14, 32)

def draw_flatbed_truck(d):
    d.rectangle([8, 34, 42, 36], fill=DKGREY)
    d.rectangle([8, 18, 20, 34], fill=RED)
    d.rectangle([10, 20, 18, 26], fill=LIGHTBLUE)
    d.rectangle([14, 20, 16, 26], fill=STEEL)
    d.rectangle([20, 28, 42, 34], fill=STEEL)
    # cargo tie downs
    for x in range(22, 42, 5):
        d.line([x, 28, x, 34], fill=DKGREY, width=1)
    draw_wheels(d, 14, 34, cy=35)

def draw_box_truck(d):
    d.rectangle([8, 34, 42, 36], fill=DKGREY)
    d.rectangle([8, 20, 18, 34], fill=WHITE)
    d.rectangle([10, 22, 16, 27], fill=LIGHTBLUE)
    d.rectangle([18, 14, 42, 34], fill=SILVER)
    d.rectangle([18, 24, 42, 26], fill=GREY)
    draw_wheels(d, 13, 34)

def draw_flatbed_tow_truck(d):
    d.rectangle([8, 34, 42, 36], fill=DKGREY)
    d.rectangle([8, 18, 18, 34], fill=BLUE)
    d.rectangle([9, 20, 15, 26], fill=LIGHTBLUE)
    d.polygon([(18, 30), (42, 24), (42, 34), (18, 34)], fill=STEEL)
    # winch
    d.rectangle([18, 26, 22, 30], fill=BLACK)
    draw_wheels(d, 13, 34)

def draw_kei_car(d):
    draw_detailed_car(d, TEAL, STEEL, [(16, 22), (18, 16), (32, 16), (34, 22)], [12, 22, 38, 34], 17, 33)

def draw_moped(d):
    d.line([14, 34, 36, 34], fill=BLACK, width=2)
    d.line([25, 22, 25, 34], fill=BLACK, width=2)
    d.rectangle([20, 24, 28, 28], fill=RED)
    d.rectangle([20, 20, 24, 24], fill=BLACK) # Seat
    d.ellipse([14, 20, 18, 24], fill=SILVER) # headlight
    draw_wheels(d, 14, 36, cy=35, r=4)

def draw_cruiser_motorcycle(d):
    d.line([14, 32, 36, 32], fill=SILVER, width=2)
    d.line([16, 20, 20, 32], fill=SILVER, width=2) # fork
    d.rectangle([18, 22, 28, 26], fill=BLACK) # tank
    d.rectangle([28, 22, 32, 25], fill=BROWN) # seat
    d.ellipse([12, 18, 16, 22], fill=SILVER) # light
    draw_wheels(d, 14, 36, cy=34, r=6)

def draw_touring_motorcycle(d):
    d.rectangle([12, 20, 38, 32], fill=ORANGE)
    d.rectangle([12, 14, 20, 20], fill=LIGHTBLUE) # windshield
    d.rectangle([24, 20, 30, 24], fill=BLACK) # seat
    d.rectangle([34, 22, 38, 28], fill=RED) # panniers
    draw_wheels(d, 16, 34, cy=34, r=6)

def draw_scrambler_motorcycle(d):
    d.line([12, 32, 38, 32], fill=STEEL, width=2)
    d.rectangle([18, 20, 26, 24], fill=GREEN) # tank
    d.rectangle([26, 20, 32, 23], fill=BROWN) # seat
    d.ellipse([10, 18, 14, 22], fill=SILVER)
    draw_wheels(d, 14, 36, cy=34, r=6, color=BLACK, hub_color=GREY)

def draw_cafe_racer(d):
    d.line([12, 32, 38, 32], fill=BLACK, width=2)
    d.rectangle([18, 22, 28, 25], fill=WHITE)
    d.rectangle([28, 22, 32, 24], fill=BLACK)
    d.ellipse([32, 22, 36, 26], fill=WHITE) # cowl
    d.ellipse([10, 20, 14, 24], fill=SILVER)
    draw_wheels(d, 14, 36, cy=34, r=6)

def draw_recumbent_trike(d):
    d.line([12, 34, 38, 34], fill=STEEL, width=2)
    d.polygon([(18, 24), (32, 30), (32, 34), (18, 34)], fill=BLUE)
    d.ellipse([12 - 3, 34 - 3, 12 + 3, 34 + 3], outline=BLACK, width=2)
    d.ellipse([36 - 3, 34 - 3, 36 + 3, 34 + 3], outline=BLACK, width=2)
    d.ellipse([25 - 3, 34 - 3, 25 + 3, 34 + 3], outline=BLACK, width=2)

def draw_ebike(d):
    d.line([14, 32, 36, 32], fill=BLACK, width=2)
    d.rectangle([22, 26, 28, 30], fill=STEEL) # battery
    d.line([14, 22, 18, 32], fill=BLACK, width=2)
    d.line([28, 22, 25, 32], fill=BLACK, width=2)
    draw_wheels(d, 14, 36, cy=32, r=5)

def draw_smart_car(d):
    draw_detailed_car(d, PURPLE, PINK, [(16, 20), (20, 14), (30, 14), (34, 20)], [12, 20, 38, 34], 17, 33)

def draw_electric_cargo_van(d):
    d.rectangle([10, 34, 40, 36], fill=DKGREY)
    d.rounded_rectangle([8, 16, 42, 34], radius=4, fill=WHITE)
    d.rectangle([10, 18, 18, 24], fill=LIGHTBLUE)
    d.rectangle([20, 20, 38, 28], fill=GREEN) # Eco stripe
    d.rectangle([22, 22, 36, 26], fill=DKGREEN) # Eco detail
    d.rectangle([8, 28, 10, 30], fill=SILVER)
    draw_wheels(d, 15, 35)

def draw_street_flusher(d):
    d.rectangle([8, 34, 42, 36], fill=DKGREY)
    d.rectangle([8, 20, 18, 34], fill=YELLOW)
    d.rectangle([10, 22, 16, 26], fill=LIGHTBLUE)
    d.rectangle([18, 16, 42, 34], fill=STEEL)
    d.rectangle([20, 18, 40, 22], fill=GREY)
    d.line([6, 34, 12, 34], fill=WHITE, width=2)
    d.line([2, 36, 8, 36], fill=WHITE, width=2) # Water spray
    draw_wheels(d, 13, 34)

def draw_vacuum_truck(d):
    d.rectangle([8, 34, 42, 36], fill=DKGREY)
    d.rectangle([8, 20, 18, 34], fill=GREY)
    d.rectangle([10, 22, 16, 26], fill=LIGHTBLUE)
    d.rectangle([18, 16, 40, 34], fill=STEEL)
    d.arc([22, 10, 36, 30], start=0, end=180, fill=DKGREY, width=3) # Hose
    draw_wheels(d, 13, 34)

def draw_salt_spreader(d):
    d.rectangle([8, 34, 42, 36], fill=DKGREY)
    d.rectangle([8, 20, 18, 34], fill=ORANGE)
    d.rectangle([10, 22, 16, 26], fill=LIGHTBLUE)
    d.rectangle([18, 18, 38, 34], fill=STEEL)
    d.polygon([(18,18), (38,18), (34,34), (22,34)], fill=GREY) # hopper shape
    d.rectangle([38, 28, 44, 34], fill=YELLOW) # spreader
    # salt pixels
    d.point([(42,36), (44,35), (46,37), (40,36)], fill=WHITE)
    draw_wheels(d, 13, 33)

def draw_airport_fire_tender(d):
    d.rectangle([6, 34, 44, 36], fill=DKGREY)
    d.rectangle([6, 16, 44, 34], fill=RED)
    d.rectangle([6, 24, 44, 26], fill=SILVER) # stripe
    d.rectangle([8, 18, 20, 24], fill=LIGHTBLUE)
    d.line([14, 16, 26, 12], fill=SILVER, width=2) # roof water cannon
    d.point([(28,10), (30,8), (32,10)], fill=LIGHTBLUE) # water drops
    draw_wheels(d, 12, 38, cy=34, r=6)

def draw_riot_control_truck(d):
    d.rectangle([6, 34, 44, 36], fill=DKGREY)
    d.rectangle([6, 18, 44, 34], fill=DKBLUE)
    d.rectangle([10, 20, 18, 25], fill=STEEL) # armored window
    d.line([12, 20, 18, 25], fill=DKGREY, width=1) # mesh
    d.line([12, 25, 18, 20], fill=DKGREY, width=1)
    d.line([12, 18, 22, 14], fill=BLACK, width=3) # cannon
    draw_wheels(d, 12, 38, cy=34, r=6)

def draw_military_jeep(d):
    d.rectangle([8, 34, 42, 36], fill=DKGREY)
    d.rectangle([6, 22, 42, 34], fill=DKGREEN)
    d.line([14, 22, 14, 14], fill=BLACK, width=2) # windshield frame
    d.rectangle([16, 14, 18, 22], fill=LIGHTBLUE) # glass
    d.ellipse([6, 24, 8, 28], fill=SILVER) # light
    d.rectangle([34, 22, 40, 28], fill=GREEN) # jerry can
    draw_wheels(d, 12, 36, cy=35)

def draw_humvee(d):
    d.rectangle([6, 34, 44, 36], fill=DKGREY)
    d.rounded_rectangle([6, 20, 44, 34], radius=2, fill=SAND)
    d.rectangle([12, 22, 20, 26], fill=BLACK)
    d.rectangle([22, 22, 30, 26], fill=BLACK)
    d.rectangle([34, 16, 38, 20], fill=BLACK) # roof turret
    draw_wheels(d, 12, 38, cy=34, r=6)

def draw_half_track(d):
    d.rectangle([6, 34, 44, 36], fill=DKGREY)
    d.rectangle([6, 18, 22, 34], fill=DKGREEN) # cab
    d.rectangle([10, 20, 16, 26], fill=LIGHTBLUE) # window
    d.rectangle([22, 22, 44, 34], fill=DKGREEN) # bed
    d.rectangle([24, 30, 42, 38], fill=BLACK) # track
    d.ellipse([26, 32, 30, 36], fill=GREY) # wheels in track
    d.ellipse([36, 32, 40, 36], fill=GREY)
    d.ellipse([10, 31, 18, 39], fill=BLACK) # front wheel
    d.ellipse([12, 33, 16, 37], fill=GREY) # front hub

def draw_self_propelled_howitzer(d):
    d.rectangle([6, 24, 44, 36], fill=DKGREEN)
    d.rectangle([18, 16, 34, 24], fill=DKGREEN) # turret
    d.line([18, 18, 2, 18], fill=BLACK, width=4) # barrel
    d.line([4, 16, 4, 20], fill=GREY, width=2) # muzzle brake
    d.rounded_rectangle([6, 32, 44, 38], radius=2, fill=BLACK)
    for x in range(8, 40, 6):
        d.ellipse([x, 33, x+4, 37], fill=GREY)

def draw_armored_combat_vehicle(d):
    d.rectangle([6, 20, 44, 32], fill=DKGREEN)
    d.polygon([(10, 20), (14, 14), (36, 14), (40, 20)], fill=DKGREEN) # slope
    d.line([25, 16, 35, 16], fill=BLACK, width=3) # gun
    d.rectangle([12, 22, 16, 26], fill=BLACK) # vision block
    draw_wheels(d, 12, 38, cy=32, r=5)

def draw_tracked_infantry_carrier(d):
    d.rectangle([6, 20, 44, 34], fill=DKGREEN)
    d.rectangle([10, 16, 32, 20], fill=GREEN)
    d.line([28, 16, 36, 14], fill=BLACK, width=2) # MG
    d.rounded_rectangle([6, 32, 44, 38], radius=2, fill=BLACK)
    for x in range(8, 40, 6):
        d.ellipse([x, 33, x+4, 37], fill=GREY)

def draw_utility_atv(d):
    d.rectangle([10, 34, 40, 36], fill=DKGREY)
    d.rectangle([10, 22, 38, 30], fill=RED)
    d.rectangle([20, 18, 28, 22], fill=BLACK) # handlebars/seat
    d.rectangle([10, 22, 14, 26], fill=SILVER) # rack
    d.rectangle([34, 22, 38, 26], fill=SILVER) # rack
    draw_wheels(d, 14, 34, cy=32, r=6)

def draw_beach_buggy(d):
    d.rectangle([8, 34, 42, 36], fill=DKGREY)
    d.polygon([(8, 28), (14, 22), (36, 22), (42, 28), (42, 34), (8, 34)], fill=PINK)
    d.rectangle([18, 22, 22, 28], fill=WHITE) # seat
    d.line([14, 22, 20, 16], fill=BLACK, width=2) # steering wheel
    draw_wheels(d, 14, 36, cy=34, r=6)

def draw_sand_rail(d):
    d.rectangle([8, 34, 42, 36], fill=DKGREY)
    d.line([12, 34, 18, 20], fill=STEEL, width=2)
    d.line([18, 20, 32, 20], fill=STEEL, width=2)
    d.line([32, 20, 38, 34], fill=STEEL, width=2)
    d.rectangle([20, 26, 26, 32], fill=RED) # seat
    d.ellipse([34, 28, 38, 32], fill=GREY) # engine block
    draw_wheels(d, 14, 36, cy=34, r=6)

def draw_crawler_tractor(d):
    d.rectangle([8, 16, 34, 34], fill=YELLOW)
    d.rectangle([12, 10, 22, 16], fill=ORANGE) # Cab
    d.rectangle([14, 12, 20, 16], fill=LIGHTBLUE) # window
    d.rectangle([28, 12, 30, 16], fill=BLACK) # exhaust
    d.rounded_rectangle([6, 30, 38, 37], radius=2, fill=BLACK)
    for x in range(8, 34, 5):
        d.ellipse([x, 32, x+3, 35], fill=GREY)

def draw_supersonic_transport(d):
    d.line([4, 25, 46, 25], fill=WHITE, width=4)
    d.polygon([(4, 25), (10, 23), (10, 27)], fill=WHITE)
    d.polygon([(20, 25), (36, 18), (36, 32)], fill=WHITE)
    d.polygon([(36, 25), (42, 14), (42, 25)], fill=WHITE)
    d.line([12, 24, 30, 24], fill=LIGHTBLUE, width=1) # windows
    d.line([46, 24, 48, 26], fill=ORANGE, width=1) # thrust

def draw_cargo_aircraft(d):
    d.rounded_rectangle([8, 20, 42, 30], radius=4, fill=GREY)
    d.line([12, 25, 36, 25], fill=DKGREY, width=8) # wings span
    d.polygon([(36, 20), (42, 12), (42, 20)], fill=GREY)
    d.rectangle([10, 22, 14, 26], fill=LIGHTBLUE) # cockpit
    d.rectangle([14, 24, 36, 26], fill=DKGREY) # stripe

def draw_propeller_airliner(d):
    d.rounded_rectangle([10, 22, 40, 28], radius=3, fill=WHITE)
    d.line([18, 25, 32, 25], fill=SILVER, width=4) # wing
    d.line([20, 20, 20, 30], fill=BLACK, width=1)
    d.line([30, 20, 30, 30], fill=BLACK, width=1)
    d.line([14, 24, 34, 24], fill=LIGHTBLUE, width=1) # windows
    d.polygon([(34, 22), (40, 16), (40, 22)], fill=RED) # tail

def draw_trimotor_plane(d):
    d.rectangle([10, 20, 38, 28], fill=SILVER)
    d.line([8, 20, 8, 28], fill=BLACK, width=2) # front prop
    d.line([22, 16, 22, 32], fill=BLACK, width=2) # wing props
    d.line([12, 22, 16, 26], fill=LIGHTBLUE, width=2) # cockpit
    d.rectangle([10, 26, 36, 27], fill=BLUE) # trim

def draw_flying_wing_glider(d):
    d.polygon([(4, 25), (25, 12), (46, 25), (25, 20)], fill=WHITE)
    d.polygon([(4, 25), (25, 14), (46, 25), (25, 20)], fill=SILVER) # shadow
    d.ellipse([22, 18, 28, 24], fill=LIGHTBLUE) # canopy

def draw_tiltwing_aircraft(d):
    d.rectangle([10, 22, 40, 28], fill=GREY)
    d.line([25, 12, 25, 38], fill=STEEL, width=6) # tilted wing
    d.ellipse([22, 10, 28, 14], fill=BLACK) # props
    d.ellipse([22, 36, 28, 40], fill=BLACK)
    d.rectangle([12, 24, 16, 26], fill=LIGHTBLUE)

def draw_tailsitter_aircraft(d):
    d.polygon([(25, 6), (20, 40), (30, 40)], fill=WHITE)
    d.polygon([(16, 30), (25, 30), (25, 40)], fill=RED)
    d.polygon([(34, 30), (25, 30), (25, 40)], fill=RED)
    d.ellipse([22, 20, 28, 26], fill=LIGHTBLUE) # cockpit
    d.line([20, 4, 30, 4], fill=BLACK, width=2) # prop

def draw_rocket_plane(d):
    d.polygon([(4, 25), (42, 20), (42, 30)], fill=BLACK)
    d.line([42, 25, 48, 25], fill=ORANGE, width=4) # flame
    d.line([44, 25, 48, 25], fill=YELLOW, width=2) # flame core
    d.polygon([(12, 25), (24, 23), (24, 27)], fill=LIGHTBLUE) # canopy
    d.line([4, 25, 42, 25], fill=STEEL, width=1) # panel line

def draw_microlight_trike(d):
    d.polygon([(14, 12), (36, 12), (25, 20)], fill=YELLOW)
    d.polygon([(14, 12), (36, 12), (25, 16)], fill=ORANGE) # detail
    d.line([25, 20, 25, 32], fill=BLACK, width=2)
    d.rectangle([23, 28, 27, 32], fill=RED) # seat
    draw_wheels(d, 20, 30, cy=34, r=3)

def draw_solar_airplane(d):
    d.line([2, 25, 48, 25], fill=BLUE, width=5) # wings
    d.line([4, 25, 46, 25], fill=LIGHTBLUE, width=1) # solar grid
    d.rectangle([18, 22, 32, 28], fill=WHITE) # fuselage
    d.rectangle([20, 24, 24, 26], fill=BLACK) # canopy

def draw_weather_balloon(d):
    d.ellipse([14, 4, 36, 26], fill=WHITE)
    d.ellipse([18, 6, 24, 12], fill=SILVER) # highlight
    d.line([20, 26, 22, 38], fill=BLACK, width=1)
    d.line([30, 26, 28, 38], fill=BLACK, width=1)
    d.rectangle([21, 38, 29, 44], fill=RED) # instrument box
    d.rectangle([23, 40, 27, 42], fill=LIGHTBLUE)

def draw_skycrane_helicopter(d):
    d.line([8, 20, 42, 20], fill=ORANGE, width=4)
    d.rectangle([6, 18, 14, 26], fill=ORANGE)
    d.rectangle([8, 20, 12, 24], fill=LIGHTBLUE) # cockpit
    d.rectangle([18, 24, 34, 36], fill=GREEN) # cargo
    d.rectangle([20, 26, 32, 34], fill=DKGREEN) # container doors
    d.line([10, 12, 38, 12], fill=DKGREY, width=2) # rotor
    d.line([24, 12, 24, 20], fill=STEEL, width=2) # mast

def draw_octocopter_drone(d):
    d.rectangle([20, 20, 30, 30], fill=BLACK)
    d.ellipse([22, 22, 28, 28], fill=BLUE) # core light
    d.line([12, 12, 38, 38], fill=STEEL, width=2)
    d.line([12, 38, 38, 12], fill=STEEL, width=2)
    for cx, cy in [(12, 12), (38, 38), (12, 38), (38, 12)]:
        d.ellipse([cx-5, cy-5, cx+5, cy+5], outline=RED, width=2)

def draw_vtol_jet(d):
    d.polygon([(6, 25), (42, 20), (42, 30)], fill=STEEL)
    d.polygon([(14, 25), (22, 23), (22, 27)], fill=LIGHTBLUE) # canopy
    d.rectangle([20, 28, 24, 34], fill=RED) # thrust nozzle
    d.rectangle([28, 28, 32, 34], fill=RED)
    d.line([22, 34, 22, 38], fill=ORANGE, width=2) # flame
    d.line([30, 34, 30, 38], fill=ORANGE, width=2)

def draw_paramotor(d):
    d.arc([10, 8, 40, 24], start=180, end=360, fill=RED, width=4)
    d.arc([12, 10, 38, 24], start=180, end=360, fill=YELLOW, width=2) # stripe
    d.line([25, 20, 25, 34], fill=BLACK, width=1)
    d.ellipse([22, 30, 28, 36], fill=STEEL)
    d.ellipse([24, 32, 26, 34], fill=BLACK) # engine

# Boat helper
def draw_boat(d, hull_pts, hull_color, cabin_box, cabin_color, props=None):
    d.polygon(hull_pts, fill=hull_color)
    d.line([hull_pts[0][0], hull_pts[0][1], hull_pts[1][0], hull_pts[1][1]], fill=WHITE, width=1) # waterline
    if cabin_box:
        d.rectangle(cabin_box, fill=cabin_color)
        # portholes / windows
        for x in range(cabin_box[0]+2, cabin_box[2]-2, 4):
            d.rectangle([x, cabin_box[1]+2, x+2, cabin_box[1]+4], fill=LIGHTBLUE)

def draw_battleship(d):
    draw_boat(d, [(4, 28), (42, 28), (46, 34), (4, 34)], GREY, [14, 20, 32, 28], DKGREY)
    d.rectangle([10, 24, 14, 28], fill=BLACK) # turret 1
    d.line([12, 26, 2, 26], fill=BLACK, width=2)
    d.rectangle([32, 24, 36, 28], fill=BLACK) # turret 2
    d.line([34, 26, 44, 26], fill=BLACK, width=2)
    d.line([22, 14, 22, 20], fill=BLACK, width=1) # mast

def draw_destroyer_warship(d):
    draw_boat(d, [(6, 28), (40, 28), (44, 34), (6, 34)], STEEL, [16, 22, 28, 28], GREY)
    d.line([22, 22, 22, 16], fill=BLACK, width=2) # radar mast
    d.point([(21, 16), (23, 16)], fill=RED) # radar dish
    d.rectangle([10, 25, 14, 28], fill=BLACK) # gun
    d.line([12, 26, 6, 26], fill=BLACK, width=1)

def draw_frigate_warship(d):
    draw_boat(d, [(6, 28), (42, 28), (44, 34), (6, 34)], STEEL, [18, 20, 30, 28], GREY)
    d.polygon([(30, 28), (34, 28), (34, 24)], fill=GREY) # helipad

def draw_corvette_warship(d):
    draw_boat(d, [(8, 28), (38, 28), (40, 34), (8, 34)], STEEL, [18, 24, 28, 28], GREY)
    d.rectangle([12, 26, 16, 28], fill=BLACK)

def draw_cruiser_warship(d):
    draw_boat(d, [(4, 28), (44, 28), (46, 34), (4, 34)], STEEL, [14, 20, 34, 28], GREY)
    d.rectangle([20, 14, 24, 20], fill=DKGREY) # smokestack

def draw_minesweeper_boat(d):
    draw_boat(d, [(8, 28), (38, 28), (40, 34), (8, 34)], BROWN, [16, 22, 28, 28], WHITE)
    d.line([38, 28, 42, 34], fill=BLACK, width=1) # sweeping gear

def draw_torpedo_boat(d):
    draw_boat(d, [(8, 28), (40, 28), (42, 34), (8, 34)], DKGREY, [16, 24, 24, 28], GREY)
    d.rectangle([26, 25, 34, 28], fill=BLACK) # torpedo tubes
    d.ellipse([26, 26, 28, 28], fill=RED)

def draw_patrol_boat(d):
    draw_boat(d, [(8, 26), (38, 26), (40, 34), (8, 34)], GREY, [14, 20, 24, 26], WHITE)
    d.rectangle([14, 20, 24, 22], fill=BLUE) # roof
    d.rectangle([10, 24, 12, 26], fill=BLACK) # small gun

def draw_midget_sub(d):
    d.ellipse([12, 22, 38, 32], fill=DKBLUE)
    d.ellipse([14, 24, 36, 30], fill=STEEL) # highlight
    d.rectangle([22, 16, 26, 22], fill=DKBLUE) # sail
    d.line([24, 16, 24, 12], fill=BLACK, width=1) # periscope
    d.ellipse([36, 25, 40, 29], fill=GREY) # prop

def draw_deep_sea_rov(d):
    d.rectangle([14, 18, 36, 34], fill=YELLOW)
    d.rectangle([16, 20, 34, 32], fill=ORANGE) # inner
    d.ellipse([18, 22, 26, 30], fill=LIGHTBLUE) # camera lens
    d.line([14, 28, 6, 34], fill=STEEL, width=2) # arm 1
    d.line([14, 24, 6, 20], fill=STEEL, width=2) # arm 2
    d.ellipse([34, 22, 38, 26], fill=BLACK)
    d.ellipse([34, 26, 38, 30], fill=BLACK)

def draw_oceanographic_vessel(d):
    draw_boat(d, [(6, 28), (42, 28), (44, 36), (6, 36)], BLUE, [10, 20, 26, 28], WHITE)
    d.line([36, 28, 40, 18], fill=YELLOW, width=2)
    d.line([40, 18, 42, 28], fill=YELLOW, width=2)
    d.ellipse([38, 22, 42, 26], fill=RED) # submarine hanging

def draw_icebreaker_ship(d):
    draw_boat(d, [(4, 26), (40, 26), (44, 36), (4, 36)], RED, [12, 18, 28, 26], WHITE)
    d.polygon([(4, 26), (12, 26), (8, 36)], fill=DKRED) # reinforced bow
    d.rectangle([20, 12, 24, 18], fill=BLACK) # smokestack

def draw_cable_layer(d):
    draw_boat(d, [(6, 28), (42, 28), (44, 36), (6, 36)], DKGREY, [12, 20, 28, 28], WHITE)
    d.ellipse([32, 22, 40, 30], fill=ORANGE) # drum
    d.ellipse([34, 24, 38, 28], fill=DKGREY) # inner drum

def draw_dredger_ship(d):
    draw_boat(d, [(6, 28), (42, 28), (44, 36), (6, 36)], STEEL, [24, 20, 34, 28], WHITE)
    d.line([10, 28, 2, 40], fill=YELLOW, width=4) # excavator arm
    d.polygon([(2, 40), (6, 44), (8, 40)], fill=BLACK) # bucket

def draw_roro_ferry(d):
    draw_boat(d, [(6, 30), (44, 30), (44, 36), (6, 36)], BLUE, [6, 20, 44, 30], WHITE)
    d.rectangle([6, 20, 44, 24], fill=LIGHTBLUE) # windows
    d.polygon([(4, 30), (8, 30), (6, 36)], fill=GREY) # open bow ramp

def draw_houseboat(d):
    draw_boat(d, [(8, 28), (42, 28), (42, 34), (8, 34)], BROWN, [12, 16, 36, 28], WHITE)
    d.rectangle([12, 16, 36, 18], fill=RED) # roof
    d.rectangle([16, 20, 22, 26], fill=LIGHTBLUE) # big window
    d.rectangle([26, 20, 32, 26], fill=LIGHTBLUE) # big window

def draw_canal_narrowboat(d):
    draw_boat(d, [(4, 28), (46, 28), (46, 34), (4, 34)], BLACK, [6, 22, 42, 28], RED)
    d.rectangle([6, 22, 42, 24], fill=YELLOW) # trim
    d.line([12, 22, 12, 16], fill=BLACK, width=2) # chimney
    d.ellipse([10, 14, 14, 16], fill=GREY) # smoke

def draw_cabin_cruiser(d):
    draw_boat(d, [(8, 26), (40, 26), (42, 34), (8, 34)], WHITE, None, None)
    d.line([8, 26, 40, 26], fill=BLUE, width=2) # stripe
    d.polygon([(14, 26), (20, 18), (32, 18), (36, 26)], fill=LIGHTBLUE) # windshield
    d.polygon([(16, 26), (21, 20), (31, 20), (34, 26)], fill=STEEL) # glass highlight

def draw_runabout_boat(d):
    draw_boat(d, [(8, 28), (40, 28), (42, 34), (8, 34)], BROWN, None, None)
    d.rectangle([12, 24, 24, 28], fill=WHITE) # seats
    d.rectangle([14, 24, 22, 28], fill=RED) # red leather
    d.line([10, 24, 12, 28], fill=SILVER, width=1) # windshield

def draw_outboard_motorboat(d):
    draw_boat(d, [(10, 28), (38, 28), (40, 34), (10, 34)], SILVER, None, None)
    d.rectangle([10, 28, 38, 30], fill=BLUE) # trim
    d.rectangle([6, 26, 10, 34], fill=BLACK) # outboard motor
    d.ellipse([6, 26, 10, 30], fill=RED) # motor cover

def draw_puffer_boat(d):
    draw_boat(d, [(8, 26), (38, 26), (40, 34), (8, 34)], BLACK, [16, 22, 24, 26], BROWN)
    d.rectangle([16, 22, 24, 24], fill=WHITE) # roof
    d.line([20, 22, 20, 12], fill=BLACK, width=3) # smokestack
    d.ellipse([18, 8, 24, 12], fill=GREY) # smoke

def draw_jon_boat(d):
    draw_boat(d, [(8, 28), (40, 28), (38, 34), (10, 34)], DKGREEN, None, None)
    d.rectangle([14, 28, 18, 30], fill=BROWN) # bench 1
    d.rectangle([30, 28, 34, 30], fill=BROWN) # bench 2

def draw_pontoon_boat(d):
    d.line([8, 32, 42, 32], fill=SILVER, width=4) # pontoons
    d.line([12, 32, 12, 22], fill=BLACK, width=2)
    d.line([38, 32, 38, 22], fill=BLACK, width=2)
    d.rectangle([12, 26, 38, 30], fill=WHITE) # fencing
    d.rectangle([14, 20, 34, 22], fill=BLUE) # canopy
    d.rectangle([16, 28, 22, 32], fill=RED) # seats

def draw_jetboat(d):
    draw_boat(d, [(8, 26), (38, 26), (40, 34), (8, 34)], RED, None, None)
    d.polygon([(16, 26), (22, 20), (30, 20), (32, 26)], fill=BLACK) # windshield
    d.line([6, 32, 2, 32], fill=WHITE, width=3) # water spray
    d.line([8, 30, 4, 30], fill=LIGHTBLUE, width=2)

def draw_inflatable_rib(d):
    d.ellipse([8, 28, 42, 34], fill=GREY) # inflatable tube
    d.ellipse([10, 29, 40, 33], fill=DKGREY) # shading
    d.rectangle([14, 22, 22, 28], fill=WHITE) # console
    d.rectangle([16, 24, 20, 26], fill=BLACK) # screen

def draw_coracle(d):
    d.ellipse([14, 22, 36, 38], fill=BROWN)
    d.ellipse([16, 24, 34, 36], fill=DBROWN) # woven texture
    d.line([14, 30, 36, 30], fill=BROWN, width=2) # woven texture
    d.line([25, 22, 25, 38], fill=BROWN, width=2) # woven texture

def draw_pirogue(d):
    d.polygon([(6, 30), (44, 30), (40, 34), (10, 34)], fill=BROWN)
    d.line([10, 32, 40, 32], fill=DBROWN, width=1) # wood grain

def draw_dragon_boat(d):
    d.rectangle([6, 30, 44, 34], fill=RED)
    d.line([6, 32, 44, 32], fill=GOLD, width=1) # scale pattern
    d.polygon([(44, 30), (48, 24), (46, 34)], fill=ORANGE) # dragon head
    d.ellipse([45, 26, 47, 28], fill=BLACK) # eye

def draw_swan_pedal_boat(d):
    d.rectangle([12, 30, 38, 34], fill=WHITE)
    d.arc([8, 14, 20, 32], start=180, end=360, fill=WHITE, width=4)
    d.polygon([(8, 16), (4, 18), (8, 20)], fill=ORANGE) # beak
    d.ellipse([10, 16, 12, 18], fill=BLACK) # eye

def draw_bumper_boat(d):
    d.ellipse([14, 22, 36, 38], fill=BLACK)
    d.ellipse([18, 24, 32, 36], fill=YELLOW)
    d.ellipse([22, 28, 28, 32], fill=BLUE) # seat
    d.line([25, 24, 25, 28], fill=BLACK, width=2) # steering column

def draw_water_taxi(d):
    draw_boat(d, [(8, 28), (42, 28), (42, 34), (8, 34)], YELLOW, [14, 20, 36, 28], WHITE)
    d.rectangle([14, 20, 36, 22], fill=BLACK) # roof checker pattern
    # windows
    for x in range(16, 34, 6):
        d.rectangle([x, 24, x+4, 28], fill=LIGHTBLUE)

def draw_electric_locomotive(d):
    d.rectangle([6, 18, 44, 34], fill=RED)
    d.rectangle([6, 26, 44, 28], fill=YELLOW) # stripe
    d.line([18, 18, 22, 10], fill=BLACK, width=2) # pantograph
    d.line([22, 10, 26, 18], fill=BLACK, width=2)
    d.line([20, 10, 24, 10], fill=SILVER, width=2) # wire contact
    d.rectangle([8, 20, 12, 24], fill=LIGHTBLUE) # window
    draw_wheels(d, 12, 38, cy=34, r=4)
    draw_wheels(d, 20, 30, cy=34, r=4)

def draw_coal_train(d):
    d.rectangle([8, 24, 42, 34], fill=DKGREY)
    d.ellipse([12, 16, 38, 26], fill=BLACK) # coal pile
    d.ellipse([14, 14, 30, 24], fill=BLACK) # coal bump
    draw_wheels(d, 12, 38, cy=34, r=4)

def draw_boxcar_train(d):
    d.rectangle([6, 18, 44, 34], fill=BROWN)
    d.rectangle([20, 20, 30, 32], fill=DBROWN) # sliding door
    d.line([25, 20, 25, 32], fill=BLACK, width=1) # door seam
    d.rectangle([28, 24, 30, 28], fill=SILVER) # lock
    draw_wheels(d, 12, 38, cy=34, r=4)

def draw_caboose(d):
    d.rectangle([6, 18, 44, 34], fill=RED)
    d.rectangle([18, 10, 32, 18], fill=RED) # cupola
    d.rectangle([20, 12, 24, 16], fill=LIGHTBLUE) # cupola window
    d.rectangle([26, 12, 30, 16], fill=LIGHTBLUE) # cupola window
    d.rectangle([10, 22, 14, 28], fill=LIGHTBLUE) # side window
    d.rectangle([36, 22, 40, 28], fill=LIGHTBLUE) # side window
    draw_wheels(d, 12, 38, cy=34, r=4)

def draw_dining_car(d):
    d.rectangle([6, 18, 44, 34], fill=SILVER)
    d.rectangle([6, 20, 44, 22], fill=BLUE) # trim
    for x in range(10, 40, 6):
        d.rectangle([x, 24, x+4, 28], fill=LIGHTBLUE) # big windows
        d.ellipse([x+1, 25, x+3, 27], fill=WHITE) # plates on tables
    draw_wheels(d, 12, 38, cy=34, r=4)

def draw_sleeping_car(d):
    d.rectangle([6, 18, 44, 34], fill=DKBLUE)
    d.rectangle([6, 18, 44, 20], fill=SILVER) # roof
    for x in range(10, 40, 6):
        d.rectangle([x, 22, x+3, 25], fill=LIGHTBLUE) # upper berth
        d.rectangle([x, 28, x+3, 31], fill=LIGHTBLUE) # lower berth
    draw_wheels(d, 12, 38, cy=34, r=4)

def draw_intermodal_well_car(d):
    d.rectangle([6, 28, 44, 34], fill=STEEL)
    d.rectangle([10, 16, 40, 28], fill=RED) # shipping container
    d.rectangle([10, 16, 40, 18], fill=DKRED) # container roof
    # corrugation
    for x in range(12, 38, 4):
        d.line([x, 18, x, 28], fill=DKRED, width=1)
    draw_wheels(d, 12, 38, cy=34, r=4)

def draw_railway_crane(d):
    d.rectangle([6, 26, 44, 34], fill=YELLOW)
    d.rectangle([10, 20, 20, 26], fill=YELLOW) # cab
    d.rectangle([12, 22, 16, 26], fill=LIGHTBLUE) # cab window
    d.line([18, 22, 40, 10], fill=BLACK, width=3) # crane boom
    d.line([40, 10, 40, 16], fill=STEEL, width=1) # cable
    d.polygon([(38, 16), (42, 16), (40, 20)], fill=BLACK) # hook
    draw_wheels(d, 12, 38, cy=34, r=4)

def draw_track_maintenance_car(d):
    d.rectangle([6, 20, 44, 34], fill=YELLOW)
    d.rectangle([14, 22, 36, 28], fill=DKGREY) # machinery
    d.line([25, 28, 25, 34], fill=STEEL, width=2) # tamper tool
    d.rectangle([8, 22, 12, 26], fill=LIGHTBLUE) # cab window
    draw_wheels(d, 12, 38, cy=34, r=4)

def draw_galloping_goose(d):
    d.rectangle([6, 20, 20, 34], fill=SILVER) # Car front
    d.rectangle([20, 16, 44, 34], fill=BROWN) # Bus back
    d.rectangle([10, 22, 16, 26], fill=LIGHTBLUE) # front window
    for x in range(22, 40, 6):
        d.rectangle([x, 20, x+4, 26], fill=LIGHTBLUE) # back windows
    draw_wheels(d, 12, 38, cy=34, r=4)

def draw_high_rail_truck(d):
    d.rectangle([8, 20, 38, 34], fill=WHITE)
    d.rectangle([10, 22, 16, 26], fill=LIGHTBLUE) # window
    d.rectangle([18, 22, 38, 26], fill=ORANGE) # utility body
    d.ellipse([10, 34, 14, 38], fill=SILVER) # secondary wheels
    d.ellipse([34, 34, 38, 38], fill=SILVER)
    draw_wheels(d, 13, 33, cy=33)

def draw_space_probe(d):
    d.ellipse([18, 18, 32, 32], fill=SILVER)
    d.ellipse([20, 20, 30, 30], fill=GOLD) # foil
    d.arc([10, 10, 40, 40], start=45, end=135, fill=WHITE, width=3) # dish
    d.line([25, 18, 25, 6], fill=STEEL, width=2) # antenna
    d.ellipse([23, 4, 27, 8], fill=RED) # sensor

def draw_ion_spacecraft(d):
    d.rectangle([14, 20, 36, 30], fill=WHITE)
    d.line([14, 25, 2, 25], fill=LIGHTBLUE, width=4) # ion exhaust
    d.line([14, 25, 8, 25], fill=BLUE, width=2)
    # solar panels
    d.rectangle([20, 8, 30, 20], fill=DKBLUE)
    d.rectangle([20, 30, 30, 42], fill=DKBLUE)
    # panel grid
    d.line([25, 8, 25, 42], fill=STEEL, width=1)
    d.line([20, 14, 30, 14], fill=STEEL, width=1)
    d.line([20, 36, 30, 36], fill=STEEL, width=1)

def draw_orbital_lander(d):
    d.polygon([(14, 24), (36, 24), (30, 14), (20, 14)], fill=GOLD)
    d.ellipse([22, 16, 28, 22], fill=BLACK) # window
    d.line([16, 24, 10, 38], fill=SILVER, width=2) # leg
    d.line([34, 24, 40, 38], fill=SILVER, width=2) # leg
    d.ellipse([6, 36, 14, 40], fill=GREY) # footpad
    d.ellipse([36, 36, 44, 40], fill=GREY) # footpad

def draw_reusable_booster(d):
    d.rectangle([20, 8, 30, 40], fill=WHITE)
    d.rectangle([20, 14, 30, 18], fill=BLACK) # logo/grid
    d.line([20, 34, 14, 42], fill=DKGREY, width=2) # landing leg
    d.line([30, 34, 36, 42], fill=DKGREY, width=2) # landing leg
    d.line([22, 40, 28, 40], fill=ORANGE, width=3) # engine nozzle

def draw_rocket_lander(d):
    d.polygon([(14, 34), (36, 34), (25, 14)], fill=SILVER)
    d.polygon([(16, 34), (34, 34), (25, 16)], fill=WHITE)
    d.line([25, 34, 25, 46], fill=ORANGE, width=4) # engine fire
    d.line([25, 34, 25, 42], fill=YELLOW, width=2) # inner fire
    d.ellipse([23, 24, 27, 28], fill=LIGHTBLUE) # porthole

def draw_lunar_atv(d):
    d.rectangle([12, 24, 38, 34], fill=WHITE)
    d.rectangle([14, 20, 22, 24], fill=GOLD) # seats
    d.line([30, 24, 34, 14], fill=STEEL, width=1) # antenna
    d.ellipse([32, 12, 36, 16], fill=BLACK) # dish
    draw_wheels(d, 15, 35, cy=34, r=5, color=GREY, hub_color=STEEL)

def draw_vintage_fire_engine(d):
    draw_detailed_car(d, RED, DKRED, [(16, 24), (20, 16), (30, 16), (34, 24)], [8, 24, 40, 36], 14, 34)
    d.ellipse([14, 16, 18, 20], fill=GOLD) # bell
    d.rectangle([34, 24, 38, 34], fill=BROWN) # wooden ladder
    for y in range(26, 34, 3):
        d.line([34, y, 38, y], fill=DBROWN, width=1) # ladder rungs

NEW_VEHICLES = {
    "coupe": draw_coupe,
    "hatchback": draw_hatchback,
    "muscle_car": draw_muscle_car,
    "station_wagon": draw_station_wagon,
    "crossover_car": draw_crossover_car,
    "kei_truck": draw_kei_truck,
    "panel_van": draw_panel_van,
    "step_van": draw_step_van,
    "flatbed_truck": draw_flatbed_truck,
    "box_truck": draw_box_truck,
    "flatbed_tow_truck": draw_flatbed_tow_truck,
    "kei_car": draw_kei_car,
    "moped": draw_moped,
    "cruiser_motorcycle": draw_cruiser_motorcycle,
    "touring_motorcycle": draw_touring_motorcycle,
    "scrambler_motorcycle": draw_scrambler_motorcycle,
    "cafe_racer": draw_cafe_racer,
    "recumbent_trike": draw_recumbent_trike,
    "ebike": draw_ebike,
    "smart_car": draw_smart_car,
    "electric_cargo_van": draw_electric_cargo_van,
    "street_flusher": draw_street_flusher,
    "vacuum_truck": draw_vacuum_truck,
    "salt_spreader": draw_salt_spreader,
    "airport_fire_tender": draw_airport_fire_tender,
    "riot_control_truck": draw_riot_control_truck,
    "military_jeep": draw_military_jeep,
    "humvee": draw_humvee,
    "half_track": draw_half_track,
    "self_propelled_howitzer": draw_self_propelled_howitzer,
    "armored_combat_vehicle": draw_armored_combat_vehicle,
    "tracked_infantry_carrier": draw_tracked_infantry_carrier,
    "utility_atv": draw_utility_atv,
    "beach_buggy": draw_beach_buggy,
    "sand_rail": draw_sand_rail,
    "crawler_tractor": draw_crawler_tractor,
    "supersonic_transport": draw_supersonic_transport,
    "cargo_aircraft": draw_cargo_aircraft,
    "propeller_airliner": draw_propeller_airliner,
    "trimotor_plane": draw_trimotor_plane,
    "flying_wing_glider": draw_flying_wing_glider,
    "tiltwing_aircraft": draw_tiltwing_aircraft,
    "tailsitter_aircraft": draw_tailsitter_aircraft,
    "rocket_plane": draw_rocket_plane,
    "microlight_trike": draw_microlight_trike,
    "solar_airplane": draw_solar_airplane,
    "weather_balloon": draw_weather_balloon,
    "skycrane_helicopter": draw_skycrane_helicopter,
    "octocopter_drone": draw_octocopter_drone,
    "vtol_jet": draw_vtol_jet,
    "paramotor": draw_paramotor,
    "battleship": draw_battleship,
    "destroyer_warship": draw_destroyer_warship,
    "frigate_warship": draw_frigate_warship,
    "corvette_warship": draw_corvette_warship,
    "cruiser_warship": draw_cruiser_warship,
    "minesweeper_boat": draw_minesweeper_boat,
    "torpedo_boat": draw_torpedo_boat,
    "patrol_boat": draw_patrol_boat,
    "midget_sub": draw_midget_sub,
    "deep_sea_rov": draw_deep_sea_rov,
    "oceanographic_vessel": draw_oceanographic_vessel,
    "icebreaker_ship": draw_icebreaker_ship,
    "cable_layer": draw_cable_layer,
    "dredger_ship": draw_dredger_ship,
    "roro_ferry": draw_roro_ferry,
    "houseboat": draw_houseboat,
    "canal_narrowboat": draw_canal_narrowboat,
    "cabin_cruiser": draw_cabin_cruiser,
    "runabout_boat": draw_runabout_boat,
    "outboard_motorboat": draw_outboard_motorboat,
    "puffer_boat": draw_puffer_boat,
    "jon_boat": draw_jon_boat,
    "pontoon_boat": draw_pontoon_boat,
    "jetboat": draw_jetboat,
    "inflatable_rib": draw_inflatable_rib,
    "coracle": draw_coracle,
    "pirogue": draw_pirogue,
    "dragon_boat": draw_dragon_boat,
    "swan_pedal_boat": draw_swan_pedal_boat,
    "bumper_boat": draw_bumper_boat,
    "water_taxi": draw_water_taxi,
    "electric_locomotive": draw_electric_locomotive,
    "coal_train": draw_coal_train,
    "boxcar_train": draw_boxcar_train,
    "caboose": draw_caboose,
    "dining_car": draw_dining_car,
    "sleeping_car": draw_sleeping_car,
    "intermodal_well_car": draw_intermodal_well_car,
    "railway_crane": draw_railway_crane,
    "track_maintenance_car": draw_track_maintenance_car,
    "galloping_goose": draw_galloping_goose,
    "high_rail_truck": draw_high_rail_truck,
    "space_probe": draw_space_probe,
    "ion_spacecraft": draw_ion_spacecraft,
    "orbital_lander": draw_orbital_lander,
    "reusable_booster": draw_reusable_booster,
    "rocket_lander": draw_rocket_lander,
    "lunar_atv": draw_lunar_atv,
    "vintage_fire_engine": draw_vintage_fire_engine
}

if __name__ == "__main__":
    print(f"Generating {len(NEW_VEHICLES)} enhanced vehicles...")
    for idx, (name, fn) in enumerate(NEW_VEHICLES.items()):
        create_sprite(name, fn)
    print("Done generating enhanced vehicles.")
