import os
from PIL import Image, ImageDraw

OUTPUT_DIR = "images/vehicles"
os.makedirs(OUTPUT_DIR, exist_ok=True)

def enforce_max_colors(img, max_colors=9):
    pixels = list(img.getdata())
    unique_colors = set(pixels)
    if len(unique_colors) <= max_colors:
        return img
    
    alpha = img.split()[3]
    rgb = img.convert("RGB")
    
    quantized_rgb = rgb.quantize(colors=max_colors - 1, method=Image.Quantize.FASTOCTREE, dither=Image.Dither.NONE)
    quantized_rgb = quantized_rgb.convert("RGB")
    
    w, h = img.size
    new_data = []
    rgb_pixels = list(quantized_rgb.getdata())
    alpha_pixels = list(alpha.getdata())
    
    for i in range(len(rgb_pixels)):
        a = alpha_pixels[i]
        if a < 128:
            new_data.append((0, 0, 0, 0))
        else:
            new_data.append(rgb_pixels[i] + (255,))
            
    out_img = Image.new("RGBA", (w, h))
    out_img.putdata(new_data)
    return out_img

def create_sprite(name, draw_func):
    img = Image.new("RGBA", (50, 50), (255, 255, 255, 0))
    draw = ImageDraw.Draw(img)
    draw_func(draw)
    img = enforce_max_colors(img, max_colors=9)
    path = os.path.join(OUTPUT_DIR, f"{name}_50x50.png")
    img.save(path)

RED       = (210, 45, 45, 255)
DKRED     = (130, 20, 20, 255)
BLUE      = (50, 110, 210, 255)
DKBLUE    = (20, 50, 140, 255)
YELLOW    = (240, 200, 30, 255)
DKYELLOW  = (180, 150, 20, 255)
GREEN     = (50, 160, 60, 255)
DKGREEN   = (20, 90, 20, 255)
WHITE     = (245, 245, 245, 255)
BLACK     = (25, 25, 25, 255)
GREY      = (160, 160, 165, 255)
DKGREY    = (80, 80, 85, 255)
ORANGE    = (235, 110, 25, 255)
BROWN     = (130, 85, 45, 255)
DKBROWN   = (80, 50, 25, 255)
PURPLE    = (130, 60, 180, 255)
LIGHTBLUE = (170, 220, 250, 255)
STEEL     = (120, 125, 135, 255)
SILVER    = (180, 180, 190, 255)
TAN       = (210, 180, 140, 255)

def draw_wheel(draw, x, y, r, tire=BLACK, rim=SILVER, center=DKGREY):
    draw.ellipse([x-r, y-r, x+r, y+r], fill=tire)
    if r > 2:
        draw.ellipse([x-r+1, y-r+1, x+r-1, y+r-1], fill=rim)
        draw.ellipse([x-r+2, y-r+2, x+r-2, y+r-2], fill=center)
        if r > 4:
            draw.ellipse([x-1, y-1, x+1, y+1], fill=BLACK)

def draw_military_tank(draw):
    draw.rounded_rectangle([6, 30, 44, 40], radius=3, fill=DKGREY)
    draw.rectangle([10, 30, 40, 40], fill=BLACK)
    for i in range(8, 42, 6):
        draw.ellipse([i, 32, i+5, 37], fill=STEEL)
        draw.ellipse([i+1, 33, i+4, 36], fill=DKGREY)
    draw.polygon([(4, 30), (8, 22), (42, 22), (46, 30)], fill=DKGREEN)
    draw.polygon([(10, 22), (14, 18), (38, 18), (42, 22)], fill=GREEN)
    draw.polygon([(16, 18), (20, 22), (24, 22), (22, 18)], fill=BROWN)
    draw.polygon([(30, 18), (34, 22), (38, 22), (36, 18)], fill=DKGREEN)
    draw.rounded_rectangle([16, 12, 34, 18], radius=2, fill=GREEN)
    draw.rectangle([20, 10, 28, 12], fill=DKGREEN)
    draw.rectangle([34, 14, 48, 16], fill=STEEL)
    draw.rectangle([46, 13, 48, 17], fill=DKGREY)
    draw.rectangle([22, 8, 26, 10], fill=BLACK)

def draw_quadcopter(draw):
    draw.line([(8, 8), (42, 42)], fill=DKGREY, width=3)
    draw.line([(8, 42), (42, 8)], fill=DKGREY, width=3)
    for x, y in [(8,8), (42,42), (8,42), (42,8)]:
        draw.ellipse([x-6, y-6, x+6, y+6], fill=LIGHTBLUE, outline=BLUE)
        draw.ellipse([x-2, y-2, x+2, y+2], fill=STEEL)
    draw.ellipse([18, 18, 32, 32], fill=WHITE, outline=DKGREY)
    draw.ellipse([20, 20, 30, 30], fill=SILVER)
    draw.ellipse([22, 22, 28, 28], fill=BLACK)
    draw.ellipse([24, 24, 26, 26], fill=RED)

def draw_tricycle(draw):
    draw_wheel(draw, 12, 36, 5)
    draw_wheel(draw, 34, 36, 5)
    draw.line([(12, 36), (24, 26)], fill=RED, width=3)
    draw.line([(34, 36), (24, 26)], fill=RED, width=3)
    draw.line([(24, 26), (24, 18)], fill=STEEL, width=2)
    draw.rectangle([20, 16, 28, 20], fill=BLACK)
    draw.line([(24, 26), (40, 26)], fill=RED, width=3)
    draw.line([(40, 26), (40, 12)], fill=STEEL, width=2)
    draw.line([(36, 12), (44, 12)], fill=BLACK, width=2)
    draw.line([(40, 26), (40, 38)], fill=STEEL, width=2)
    draw_wheel(draw, 40, 38, 5)
    draw.line([(40, 38), (36, 34)], fill=BLACK, width=2)

def draw_amphibious_car(draw):
    draw.polygon([(4, 26), (10, 38), (40, 38), (46, 26)], fill=BLUE)
    draw.polygon([(4, 26), (10, 26), (14, 34), (8, 34)], fill=DKBLUE)
    draw.polygon([(8, 26), (12, 20), (38, 20), (42, 26)], fill=WHITE)
    draw.polygon([(14, 26), (18, 22), (32, 22), (36, 26)], fill=LIGHTBLUE)
    draw.line([(40, 34), (48, 30)], fill=STEEL, width=2)
    draw.ellipse([46, 28, 50, 32], fill=SILVER)
    draw.line([(4, 38), (46, 38)], fill=LIGHTBLUE, width=2)
    draw.ellipse([14, 30, 20, 36], fill=BLACK)
    draw.ellipse([30, 30, 36, 36], fill=BLACK)

def draw_hot_rod(draw):
    draw.rounded_rectangle([12, 26, 42, 34], radius=3, fill=RED)
    draw.polygon([(12, 26), (20, 20), (28, 20), (28, 26)], fill=WHITE)
    draw.polygon([(14, 26), (20, 22), (26, 22), (26, 26)], fill=LIGHTBLUE)
    draw.rectangle([6, 28, 18, 32], fill=SILVER)
    for i in range(8, 18, 3):
        draw.line([(i, 28), (i, 24)], fill=STEEL, width=2)
    draw.polygon([(20, 30), (26, 26), (24, 32), (30, 28), (28, 34)], fill=YELLOW)
    draw.polygon([(22, 30), (26, 28), (25, 32)], fill=ORANGE)
    draw_wheel(draw, 12, 34, 4)
    draw_wheel(draw, 38, 32, 8)

def draw_recumbent_bike(draw):
    draw.line([(10, 34), (40, 32)], fill=BLUE, width=3)
    draw.line([(40, 32), (36, 22)], fill=STEEL, width=2)
    draw.polygon([(16, 32), (22, 20), (28, 32)], fill=BROWN)
    draw.polygon([(18, 30), (22, 22), (26, 30)], fill=DKBROWN)
    draw.line([(24, 28), (16, 24)], fill=STEEL, width=2)
    draw_wheel(draw, 10, 34, 5)
    draw_wheel(draw, 40, 32, 5)
    draw.ellipse([38, 30, 42, 34], fill=GREY)
    draw.line([(40, 32), (44, 28)], fill=BLACK, width=2)

def draw_cargo_bike(draw):
    draw.rectangle([6, 20, 24, 36], fill=BROWN)
    draw.rectangle([8, 22, 22, 34], fill=DKBROWN)
    for i in range(10, 22, 4):
        draw.line([(i, 22), (i, 34)], fill=BROWN, width=1)
    draw.line([(24, 32), (40, 32)], fill=RED, width=3)
    draw.line([(36, 32), (36, 20)], fill=RED, width=3)
    draw.line([(32, 20), (40, 20)], fill=BLACK, width=2)
    draw.line([(32, 32), (32, 26)], fill=STEEL, width=2)
    draw.rectangle([30, 24, 34, 26], fill=BLACK)
    draw_wheel(draw, 14, 36, 6)
    draw_wheel(draw, 38, 32, 6)

def draw_electric_skateboard(draw):
    draw.rounded_rectangle([8, 24, 42, 28], radius=2, fill=DKBROWN)
    draw.rectangle([10, 24, 40, 26], fill=BLACK)
    draw.rectangle([16, 28, 34, 32], fill=DKGREY)
    draw.rectangle([18, 28, 32, 30], fill=BLACK)
    draw.line([(20, 30), (30, 30)], fill=GREEN, width=2)
    draw_wheel(draw, 14, 32, 4, tire=ORANGE, rim=WHITE, center=BLACK)
    draw_wheel(draw, 36, 32, 4, tire=ORANGE, rim=WHITE, center=BLACK)

def draw_solar_car(draw):
    draw.ellipse([6, 26, 44, 32], fill=SILVER)
    draw.ellipse([10, 24, 40, 28], fill=WHITE)
    draw.polygon([(14, 25), (20, 20), (30, 20), (36, 25)], fill=DKBLUE)
    draw.polygon([(16, 25), (22, 22), (28, 22), (34, 25)], fill=LIGHTBLUE)
    for i in range(12, 38, 4):
        draw.line([(i, 26), (i, 30)], fill=BLUE, width=1)
    draw.line([(10, 28), (40, 28)], fill=BLUE, width=1)
    draw_wheel(draw, 14, 32, 4)
    draw_wheel(draw, 36, 32, 4)

def draw_cable_ferry(draw):
    draw.line([(4, 36), (46, 36)], fill=BLUE, width=2)
    draw.polygon([(6, 28), (8, 34), (42, 34), (44, 28)], fill=GREY)
    draw.polygon([(8, 28), (10, 34), (40, 34), (42, 28)], fill=DKGREY)
    draw.rectangle([14, 20, 22, 28], fill=WHITE)
    draw.rectangle([16, 22, 20, 26], fill=LIGHTBLUE)
    draw.rectangle([28, 24, 38, 28], fill=RED)
    draw.rectangle([30, 22, 36, 24], fill=WHITE)
    draw.line([(4, 32), (46, 32)], fill=STEEL, width=1)

def draw_jetpack(draw):
    draw.rounded_rectangle([14, 10, 22, 32], radius=3, fill=SILVER)
    draw.rounded_rectangle([28, 10, 36, 32], radius=3, fill=SILVER)
    draw.rectangle([16, 12, 20, 24], fill=DKGREY)
    draw.rectangle([30, 12, 34, 24], fill=DKGREY)
    draw.line([(12, 18), (38, 18)], fill=BROWN, width=2)
    draw.line([(12, 26), (38, 26)], fill=BROWN, width=2)
    draw.rectangle([16, 32, 20, 36], fill=DKGREY)
    draw.rectangle([30, 32, 34, 36], fill=DKGREY)
    draw.polygon([(16, 36), (20, 36), (18, 46)], fill=ORANGE)
    draw.polygon([(17, 36), (19, 36), (18, 42)], fill=YELLOW)
    draw.polygon([(30, 36), (34, 36), (32, 46)], fill=ORANGE)
    draw.polygon([(31, 36), (33, 36), (32, 42)], fill=YELLOW)

def draw_flying_car(draw):
    draw.rounded_rectangle([8, 22, 42, 30], radius=4, fill=WHITE)
    draw.polygon([(14, 22), (20, 14), (30, 14), (36, 22)], fill=DKBLUE)
    draw.polygon([(16, 22), (22, 16), (28, 16), (34, 22)], fill=LIGHTBLUE)
    draw.polygon([(20, 26), (30, 26), (38, 34), (12, 34)], fill=SILVER)
    draw.polygon([(22, 26), (28, 26), (34, 32), (16, 32)], fill=DKGREY)
    draw.ellipse([6, 28, 14, 34], fill=DKGREY)
    draw.ellipse([8, 30, 12, 32], fill=LIGHTBLUE)
    draw.ellipse([36, 28, 44, 34], fill=DKGREY)
    draw.ellipse([38, 30, 42, 32], fill=LIGHTBLUE)

def draw_zeppelin(draw):
    draw.ellipse([4, 12, 46, 30], fill=SILVER)
    draw.ellipse([6, 14, 44, 28], fill=WHITE)
    draw.arc([4, 12, 46, 30], 90, 270, fill=GREY, width=2)
    draw.polygon([(6, 16), (2, 8), (12, 14)], fill=RED)
    draw.polygon([(6, 26), (2, 34), (12, 28)], fill=RED)
    draw.polygon([(4, 21), (0, 21), (8, 21)], fill=DKRED)
    draw.rounded_rectangle([18, 30, 32, 34], radius=2, fill=DKGREY)
    draw.rectangle([20, 30, 30, 32], fill=LIGHTBLUE)
    for i in range(20, 30, 3):
        draw.line([(i, 30), (i, 32)], fill=DKGREY, width=1)

def draw_ironclad(draw):
    draw.polygon([(4, 28), (46, 28), (40, 38), (10, 38)], fill=DKGREY)
    draw.polygon([(6, 28), (44, 28), (38, 36), (12, 36)], fill=GREY)
    draw.line([6, 32, 44, 32], fill=BLACK, width=2)
    draw.rectangle([22, 12, 28, 28], fill=BLACK)
    draw.rectangle([24, 14, 26, 28], fill=DKGREY)
    draw.ellipse([20, 6, 26, 12], fill=GREY)
    draw.ellipse([26, 4, 32, 10], fill=LIGHTBLUE)
    draw.ellipse([14, 24, 22, 28], fill=STEEL)
    draw.line([(10, 26), (14, 26)], fill=BLACK, width=2)

def draw_hydroplane(draw):
    draw.polygon([(6, 28), (14, 28), (12, 34), (8, 34)], fill=YELLOW)
    draw.polygon([(10, 24), (40, 24), (46, 28), (10, 28)], fill=YELLOW)
    draw.polygon([(10, 24), (38, 24), (44, 26), (10, 26)], fill=DKYELLOW)
    draw.polygon([(36, 24), (44, 12), (42, 24)], fill=RED)
    draw.polygon([(38, 24), (42, 16), (40, 24)], fill=DKRED)
    draw.polygon([(16, 24), (22, 18), (28, 18), (30, 24)], fill=WHITE)
    draw.polygon([(18, 24), (22, 20), (26, 20), (28, 24)], fill=LIGHTBLUE)
    draw.ellipse([12, 32, 20, 36], fill=WHITE)

def draw_bathyscaphe(draw):
    draw.rounded_rectangle([10, 8, 40, 20], radius=4, fill=YELLOW)
    draw.rounded_rectangle([12, 10, 38, 18], radius=2, fill=DKYELLOW)
    draw.ellipse([18, 20, 32, 34], fill=STEEL)
    draw.ellipse([20, 22, 30, 32], fill=DKGREY)
    draw.ellipse([22, 24, 28, 30], fill=LIGHTBLUE)
    draw.line([(25, 24), (28, 27)], fill=WHITE, width=2)
    draw.polygon([(30, 27), (44, 20), (44, 34)], fill=YELLOW)
    draw.ellipse([42, 22, 46, 32], fill=STEEL)

def draw_airboat(draw):
    draw.polygon([(4, 30), (40, 30), (46, 36), (10, 36)], fill=GREY)
    draw.polygon([(6, 30), (38, 30), (42, 34), (12, 34)], fill=SILVER)
    draw.ellipse([4, 12, 20, 30], fill=STEEL)
    draw.ellipse([6, 14, 18, 28], fill=DKGREY)
    draw.line([(12, 16), (12, 26)], fill=BLACK, width=2)
    draw.line([(8, 21), (16, 21)], fill=BLACK, width=2)
    draw.rectangle([24, 22, 32, 30], fill=BROWN)
    draw.rectangle([26, 24, 30, 30], fill=DKBROWN)

def draw_hoverbike(draw):
    draw.rounded_rectangle([12, 18, 38, 28], radius=4, fill=PURPLE)
    draw.polygon([(12, 18), (20, 14), (30, 14), (38, 18)], fill=WHITE)
    draw.polygon([(16, 18), (22, 16), (28, 16), (34, 18)], fill=LIGHTBLUE)
    draw.rectangle([22, 18, 28, 22], fill=BLACK)
    draw.ellipse([6, 24, 18, 32], fill=STEEL)
    draw.ellipse([8, 26, 16, 30], fill=LIGHTBLUE)
    draw.ellipse([32, 24, 44, 32], fill=STEEL)
    draw.ellipse([34, 26, 42, 30], fill=LIGHTBLUE)
    draw.line([(18, 28), (32, 28)], fill=DKGREY, width=3)

def draw_mobility_scooter(draw):
    draw.rectangle([12, 32, 36, 36], fill=GREY)
    draw.rectangle([22, 18, 32, 32], fill=RED)
    draw.rectangle([18, 26, 32, 30], fill=DKRED)
    draw.line([(16, 32), (16, 16)], fill=STEEL, width=2)
    draw.line([(12, 16), (20, 16)], fill=BLACK, width=2)
    draw.rectangle([10, 22, 16, 28], fill=BROWN)
    for i in range(10, 17, 2):
        draw.line([(i, 22), (i, 28)], fill=BLACK, width=1)
    draw_wheel(draw, 16, 36, 4)
    draw_wheel(draw, 32, 36, 4)

def draw_front_loader(draw):
    draw.rectangle([20, 18, 40, 36], fill=YELLOW)
    draw.rectangle([24, 12, 36, 18], fill=DKGREY)
    draw.rectangle([26, 14, 34, 18], fill=LIGHTBLUE)
    draw.line([(22, 24), (8, 28)], fill=DKGREY, width=4)
    draw.line([(22, 24), (8, 28)], fill=STEEL, width=2)
    draw.polygon([(2, 24), (12, 24), (10, 36), (4, 36)], fill=GREY)
    draw.polygon([(4, 26), (10, 26), (8, 34), (6, 34)], fill=DKGREY)
    draw_wheel(draw, 20, 32, 6)
    draw_wheel(draw, 36, 32, 6)

def draw_backhoe(draw):
    draw.rectangle([14, 18, 34, 34], fill=YELLOW)
    draw.rectangle([18, 10, 30, 18], fill=DKGREY)
    draw.rectangle([20, 12, 28, 18], fill=LIGHTBLUE)
    draw.polygon([(4, 24), (12, 24), (10, 34), (4, 34)], fill=GREY)
    draw.line([(34, 24), (42, 14), (46, 26)], fill=DKGREY, width=3)
    draw.polygon([(44, 26), (48, 28), (46, 32)], fill=GREY)
    draw_wheel(draw, 14, 32, 5)
    draw_wheel(draw, 28, 30, 7)

def draw_crane_truck(draw):
    draw.rectangle([6, 26, 16, 36], fill=ORANGE)
    draw.rectangle([10, 28, 14, 32], fill=LIGHTBLUE)
    draw.rectangle([16, 30, 44, 36], fill=DKGREY)
    draw.rectangle([22, 26, 30, 30], fill=BLACK)
    draw.line([(26, 26), (44, 8)], fill=YELLOW, width=4)
    draw.line([(44, 8), (44, 16)], fill=STEEL, width=1)
    draw.polygon([(42, 16), (46, 16), (44, 20)], fill=BLACK)
    draw_wheel(draw, 10, 36, 4)
    draw_wheel(draw, 24, 36, 4)
    draw_wheel(draw, 38, 36, 4)

def draw_concrete_pump(draw):
    draw.rectangle([6, 26, 16, 36], fill=RED)
    draw.rectangle([10, 28, 14, 32], fill=LIGHTBLUE)
    draw.rectangle([16, 28, 44, 36], fill=WHITE)
    draw.rectangle([18, 30, 42, 34], fill=SILVER)
    draw.line([(24, 28), (30, 12), (20, 6), (36, 6)], fill=RED, width=3)
    draw.line([(24, 28), (30, 12), (20, 6), (36, 6)], fill=STEEL, width=1)
    draw_wheel(draw, 10, 36, 4)
    draw_wheel(draw, 26, 36, 4)
    draw_wheel(draw, 38, 36, 4)

def draw_cherry_picker(draw):
    draw.rectangle([6, 26, 16, 36], fill=ORANGE)
    draw.rectangle([10, 28, 14, 32], fill=LIGHTBLUE)
    draw.rectangle([16, 32, 38, 36], fill=DKGREY)
    draw.line([(24, 32), (30, 18), (18, 12)], fill=STEEL, width=3)
    draw.rectangle([14, 6, 22, 12], fill=WHITE)
    draw.rectangle([16, 8, 20, 12], fill=SILVER)
    draw_wheel(draw, 10, 36, 4)
    draw_wheel(draw, 32, 36, 4)

def draw_snowcat(draw):
    draw.rectangle([14, 18, 40, 32], fill=RED)
    draw.rectangle([18, 20, 28, 26], fill=WHITE)
    draw.rectangle([20, 22, 26, 26], fill=LIGHTBLUE)
    draw.rounded_rectangle([12, 32, 42, 40], radius=3, fill=BLACK)
    draw.rectangle([16, 34, 38, 38], fill=DKGREY)
    for i in range(14, 40, 6):
        draw.ellipse([i, 34, i+4, 38], fill=STEEL)
    draw.line([(14, 34), (4, 30)], fill=SILVER, width=4)
    draw.polygon([(2, 26), (6, 26), (4, 36), (0, 36)], fill=YELLOW)

def draw_baggage_tug(draw):
    draw.rectangle([8, 22, 20, 36], fill=WHITE)
    draw.rectangle([10, 24, 16, 30], fill=LIGHTBLUE)
    draw.rectangle([20, 28, 30, 36], fill=GREY)
    draw.rectangle([32, 28, 42, 36], fill=GREY)
    draw.rectangle([22, 30, 28, 34], fill=BROWN)
    draw.rectangle([34, 30, 40, 34], fill=RED)
    draw.line([(20, 34), (22, 34)], fill=BLACK, width=2)
    draw.line([(30, 34), (32, 34)], fill=BLACK, width=2)
    draw_wheel(draw, 12, 36, 4)
    draw_wheel(draw, 25, 36, 4)
    draw_wheel(draw, 37, 36, 4)

def draw_pushback_tractor(draw):
    draw.rounded_rectangle([8, 28, 42, 36], radius=2, fill=WHITE)
    draw.rectangle([12, 30, 38, 36], fill=SILVER)
    draw.rectangle([14, 22, 24, 28], fill=DKGREY)
    draw.rectangle([16, 24, 22, 28], fill=LIGHTBLUE)
    draw_wheel(draw, 14, 32, 6)
    draw_wheel(draw, 36, 32, 6)

def draw_trencher(draw):
    draw.rectangle([14, 20, 34, 34], fill=ORANGE)
    draw.rectangle([18, 22, 26, 28], fill=LIGHTBLUE)
    draw.line([(34, 26), (46, 38)], fill=DKGREY, width=4)
    for i in range(36, 46, 3):
        draw.ellipse([i, i-8+26, i+2, i-6+26], fill=BLACK)
    draw.rounded_rectangle([10, 32, 36, 40], radius=3, fill=BLACK)
    draw.rectangle([14, 34, 32, 38], fill=STEEL)
    for i in range(12, 32, 5):
        draw.ellipse([i, 34, i+3, 37], fill=GREY)

def draw_mining_truck(draw):
    draw.polygon([(14, 16), (44, 16), (42, 30), (14, 30)], fill=YELLOW)
    draw.polygon([(16, 18), (42, 18), (40, 28), (16, 28)], fill=DKYELLOW)
    draw.rectangle([34, 10, 42, 16], fill=WHITE)
    draw.rectangle([36, 12, 40, 16], fill=LIGHTBLUE)
    draw.rectangle([14, 30, 42, 34], fill=DKGREY)
    draw_wheel(draw, 18, 32, 8)
    draw_wheel(draw, 36, 32, 8)

def draw_road_grader(draw):
    draw.line([(10, 32), (36, 24)], fill=YELLOW, width=4)
    draw.rectangle([30, 18, 44, 32], fill=YELLOW)
    draw.rectangle([32, 20, 38, 26], fill=LIGHTBLUE)
    draw.line([(22, 34), (28, 28)], fill=STEEL, width=4)
    draw.polygon([(18, 34), (26, 34), (24, 38), (16, 38)], fill=DKGREY)
    draw_wheel(draw, 10, 32, 5)
    draw_wheel(draw, 34, 32, 5)
    draw_wheel(draw, 42, 32, 5)

def draw_asphalt_paver(draw):
    draw.rectangle([12, 18, 36, 32], fill=DKGREY)
    draw.rectangle([16, 20, 32, 32], fill=GREY)
    draw.polygon([(36, 24), (46, 20), (46, 32), (36, 32)], fill=YELLOW)
    draw.rectangle([6, 30, 12, 36], fill=BLACK)
    draw.rectangle([8, 32, 10, 36], fill=STEEL)
    draw_wheel(draw, 18, 32, 4)
    draw_wheel(draw, 28, 32, 4)

def draw_combine_harvester(draw):
    draw.rectangle([16, 14, 40, 34], fill=GREEN)
    draw.rectangle([18, 16, 38, 34], fill=DKGREEN)
    draw.rectangle([28, 10, 38, 18], fill=WHITE)
    draw.rectangle([30, 12, 36, 18], fill=LIGHTBLUE)
    draw.ellipse([4, 24, 16, 36], fill=RED)
    for i in range(0, 360, 45):
        draw.arc([4, 24, 16, 36], i, i+20, fill=WHITE, width=1)
    draw.line([(16, 30), (10, 30)], fill=STEEL, width=3)
    draw.line([(20, 14), (10, 8)], fill=STEEL, width=2)
    draw_wheel(draw, 22, 32, 6)
    draw_wheel(draw, 36, 32, 4)

def draw_hay_baler(draw):
    draw.rectangle([10, 18, 30, 34], fill=RED)
    draw.rectangle([12, 20, 28, 34], fill=DKRED)
    draw.ellipse([30, 26, 42, 36], fill=YELLOW)
    draw.ellipse([32, 28, 40, 34], fill=DKYELLOW)
    for i in range(32, 40, 3):
        draw.line([(i, 28), (i, 34)], fill=BROWN, width=1)
    draw.line([(10, 28), (4, 28)], fill=BLACK, width=2)
    draw_wheel(draw, 18, 34, 5)

def draw_reach_stacker(draw):
    draw.rectangle([22, 24, 44, 36], fill=YELLOW)
    draw.rectangle([24, 26, 42, 36], fill=DKYELLOW)
    draw.rectangle([30, 18, 38, 24], fill=DKGREY)
    draw.rectangle([32, 20, 36, 24], fill=LIGHTBLUE)
    draw.line([(34, 26), (16, 10)], fill=BLACK, width=4)
    draw.line([(16, 10), (16, 20)], fill=STEEL, width=2)
    draw.rectangle([6, 14, 20, 24], fill=BLUE)
    draw.rectangle([8, 16, 18, 22], fill=DKBLUE)
    draw_wheel(draw, 26, 36, 4)
    draw_wheel(draw, 40, 36, 4)

def draw_maglev(draw):
    draw.rounded_rectangle([4, 18, 46, 32], radius=6, fill=WHITE)
    draw.rounded_rectangle([6, 20, 44, 32], radius=4, fill=SILVER)
    draw.line([6, 26, 44, 26], fill=BLUE, width=3)
    for i in range(12, 40, 6):
        draw.rectangle([i, 22, i+4, 25], fill=BLACK)
    draw.line([2, 34, 48, 34], fill=DKGREY, width=3)
    draw.line([2, 34, 48, 34], fill=GREY, width=1)

def draw_draisine(draw):
    draw.rectangle([8, 30, 42, 34], fill=DKGREY)
    draw.rectangle([10, 30, 40, 32], fill=STEEL)
    draw.rectangle([22, 22, 28, 30], fill=RED)
    draw.line([(14, 22), (36, 16)], fill=BROWN, width=2)
    draw.line([(14, 22), (36, 16)], fill=WHITE, width=1)
    draw.line([(25, 22), (25, 19)], fill=BLACK, width=2)
    draw_wheel(draw, 14, 34, 4)
    draw_wheel(draw, 36, 34, 4)
    draw.line([2, 38, 48, 38], fill=GREY, width=2)

def draw_subway_car(draw):
    draw.rectangle([4, 16, 46, 34], fill=SILVER)
    draw.rectangle([6, 18, 44, 34], fill=STEEL)
    draw.rectangle([10, 20, 16, 32], fill=DKGREY)
    draw.rectangle([22, 20, 28, 32], fill=DKGREY)
    draw.rectangle([34, 20, 40, 32], fill=DKGREY)
    draw.rectangle([11, 22, 15, 26], fill=LIGHTBLUE)
    draw.rectangle([23, 22, 27, 26], fill=LIGHTBLUE)
    draw.rectangle([35, 22, 39, 26], fill=LIGHTBLUE)
    draw_wheel(draw, 12, 36, 3)
    draw_wheel(draw, 38, 36, 3)

def draw_funicular(draw):
    draw.polygon([(8, 18), (38, 10), (38, 28), (8, 36)], fill=RED)
    draw.polygon([(10, 20), (36, 13), (36, 28), (10, 34)], fill=DKRED)
    draw.line([(2, 38), (48, 24)], fill=GREY, width=3)
    draw.polygon([(12, 22), (20, 20), (20, 28), (12, 30)], fill=LIGHTBLUE)
    draw.polygon([(24, 19), (32, 17), (32, 25), (24, 27)], fill=LIGHTBLUE)
    draw.ellipse([10, 34, 16, 40], fill=BLACK)
    draw.ellipse([30, 28, 36, 34], fill=BLACK)

def draw_cog_railway(draw):
    draw.polygon([(8, 22), (32, 14), (40, 14), (40, 34), (8, 34)], fill=GREEN)
    draw.polygon([(10, 24), (32, 16), (38, 16), (38, 34), (10, 34)], fill=DKGREEN)
    draw.line([(2, 36), (48, 36)], fill=DKGREY, width=3)
    draw.line([(2, 36), (48, 36)], fill=GREY, width=1)
    draw.ellipse([22, 32, 30, 40], fill=RED)
    draw.ellipse([24, 34, 28, 38], fill=BLACK)
    draw.rectangle([14, 24, 20, 28], fill=LIGHTBLUE)
    draw.rectangle([24, 20, 30, 28], fill=LIGHTBLUE)

def draw_outrigger_canoe(draw):
    draw.ellipse([4, 24, 46, 30], fill=BROWN)
    draw.ellipse([6, 26, 44, 28], fill=DKBROWN)
    draw.line([(18, 28), (18, 36)], fill=TAN, width=2)
    draw.line([(32, 28), (32, 36)], fill=TAN, width=2)
    draw.ellipse([10, 34, 40, 38], fill=TAN)
    draw.ellipse([12, 35, 38, 37], fill=BROWN)
    draw.polygon([(26, 24), (26, 6), (38, 20)], fill=WHITE)
    draw.line([(26, 24), (26, 6)], fill=BLACK, width=1)

def draw_banana_boat(draw):
    draw.ellipse([6, 26, 44, 34], fill=YELLOW)
    draw.ellipse([8, 28, 42, 32], fill=DKYELLOW)
    draw.line([(44, 30), (48, 26)], fill=WHITE, width=2)
    draw.ellipse([16, 22, 22, 28], fill=RED)
    draw.ellipse([26, 22, 32, 28], fill=BLUE)
    draw.ellipse([36, 22, 42, 28], fill=RED)
    draw.line([(14, 24), (16, 24)], fill=BLACK, width=2)
    draw.line([(24, 24), (26, 24)], fill=BLACK, width=2)
    draw.line([(34, 24), (36, 24)], fill=BLACK, width=2)

def draw_gondola_lift(draw):
    draw.rounded_rectangle([14, 18, 36, 38], radius=4, fill=RED)
    draw.rounded_rectangle([16, 20, 34, 38], radius=3, fill=DKRED)
    draw.rectangle([18, 22, 32, 30], fill=LIGHTBLUE)
    draw.polygon([(18, 22), (24, 22), (20, 30), (18, 30)], fill=WHITE)
    draw.line([(25, 18), (25, 6)], fill=STEEL, width=3)
    draw.line([(4, 10), (46, 2)], fill=BLACK, width=2)
    draw.ellipse([22, 4, 28, 10], fill=GREY)

def draw_flying_boat(draw):
    draw.ellipse([8, 20, 42, 28], fill=WHITE)
    draw.ellipse([10, 22, 40, 28], fill=SILVER)
    draw.polygon([(8, 24), (14, 20), (22, 20), (20, 24)], fill=LIGHTBLUE)
    draw.line([12, 14, 38, 14], fill=DKGREY, width=3)
    draw.line([12, 14, 38, 14], fill=GREY, width=1)
    draw.line([(16, 14), (16, 22)], fill=STEEL, width=2)
    draw.line([(34, 14), (34, 22)], fill=STEEL, width=2)
    draw.ellipse([18, 12, 24, 16], fill=BLACK)
    draw.ellipse([26, 12, 32, 16], fill=BLACK)

def draw_space_capsule(draw):
    draw.polygon([(18, 34), (32, 34), (25, 18)], fill=WHITE)
    draw.polygon([(20, 34), (30, 34), (25, 20)], fill=SILVER)
    draw.rectangle([16, 34, 34, 38], fill=DKGREY)
    draw.rectangle([18, 36, 32, 38], fill=BROWN)
    draw.line([(25, 18), (14, 6)], fill=GREY, width=1)
    draw.line([(25, 18), (25, 6)], fill=GREY, width=1)
    draw.line([(25, 18), (36, 6)], fill=GREY, width=1)
    draw.chord([10, 0, 18, 8], 180, 360, fill=ORANGE)
    draw.chord([21, 0, 29, 8], 180, 360, fill=WHITE)
    draw.chord([32, 0, 40, 8], 180, 360, fill=ORANGE)
    draw.ellipse([23, 26, 27, 30], fill=LIGHTBLUE)

def draw_asteroid_miner(draw):
    draw.rectangle([20, 18, 40, 32], fill=GREY)
    draw.rectangle([22, 20, 38, 30], fill=DKGREY)
    draw.polygon([(20, 18), (12, 22), (12, 28), (20, 32)], fill=WHITE)
    draw.polygon([(18, 20), (14, 23), (14, 27), (18, 30)], fill=LIGHTBLUE)
    draw.line([(40, 20), (46, 14)], fill=YELLOW, width=2)
    draw.line([(40, 30), (46, 36)], fill=YELLOW, width=2)
    draw.polygon([(4, 20), (8, 16), (12, 20), (10, 26), (6, 28)], fill=BROWN)
    draw.polygon([(40, 23), (40, 27), (48, 25)], fill=LIGHTBLUE)

def draw_amphibious_atv(draw):
    draw.rounded_rectangle([8, 20, 42, 32], radius=4, fill=DKGREEN)
    draw.rounded_rectangle([10, 22, 40, 32], radius=3, fill=GREEN)
    draw.rectangle([20, 16, 26, 20], fill=BLACK)
    draw.line([(32, 20), (36, 14)], fill=STEEL, width=2)
    draw.ellipse([34, 12, 38, 16], fill=BLACK)
    for i in range(10, 40, 10):
        draw_wheel(draw, i, 32, 4)

def draw_dragster(draw):
    draw.line([(6, 34), (34, 30)], fill=RED, width=4)
    draw.line([(6, 34), (34, 30)], fill=DKRED, width=2)
    draw.ellipse([26, 20, 42, 36], fill=BLACK)
    draw.ellipse([28, 22, 40, 34], fill=DKGREY)
    draw.ellipse([32, 26, 36, 30], fill=SILVER)
    draw_wheel(draw, 6, 34, 3)
    draw.rectangle([34, 14, 46, 20], fill=SILVER)
    draw.rectangle([36, 16, 44, 18], fill=DKGREY)
    draw.polygon([(46, 14), (46, 20), (50, 17)], fill=ORANGE)
    draw.polygon([(20, 26), (24, 22), (28, 26)], fill=WHITE)

def draw_mars_rover(draw):
    draw.rectangle([14, 22, 36, 30], fill=WHITE)
    draw.rectangle([16, 24, 34, 28], fill=SILVER)
    draw.line([(20, 22), (20, 10)], fill=STEEL, width=2)
    draw.rectangle([18, 8, 24, 12], fill=WHITE)
    draw.ellipse([20, 9, 22, 11], fill=BLACK)
    draw.polygon([(24, 22), (32, 18), (40, 18), (32, 22)], fill=DKBLUE)
    draw.line([(14, 30), (14, 34)], fill=BLACK, width=2)
    draw.line([(25, 30), (25, 34)], fill=BLACK, width=2)
    draw.line([(36, 30), (36, 34)], fill=BLACK, width=2)
    draw_wheel(draw, 14, 34, 4, tire=GREY, rim=DKGREY, center=BLACK)
    draw_wheel(draw, 25, 34, 4, tire=GREY, rim=DKGREY, center=BLACK)
    draw_wheel(draw, 36, 34, 4, tire=GREY, rim=DKGREY, center=BLACK)

def draw_diesel_locomotive(draw):
    draw.rectangle([6, 16, 44, 34], fill=BLUE)
    draw.rectangle([8, 18, 42, 34], fill=DKBLUE)
    draw.polygon([(6, 24), (16, 16), (16, 34)], fill=YELLOW)
    for i in range(6, 16, 3):
        draw.line([(i, 24), (i+4, 18)], fill=BLACK, width=1)
    draw.rectangle([18, 18, 24, 24], fill=BLACK)
    draw.rectangle([19, 19, 23, 23], fill=LIGHTBLUE)
    draw.line([2, 38, 48, 38], fill=GREY, width=3)
    draw_wheel(draw, 12, 36, 4)
    draw_wheel(draw, 20, 36, 4)
    draw_wheel(draw, 32, 36, 4)
    draw_wheel(draw, 40, 36, 4)

def draw_sidecar_motorcycle(draw):
    draw.line([(16, 30), (36, 30)], fill=GREEN, width=4)
    draw_wheel(draw, 14, 30, 5)
    draw_wheel(draw, 36, 30, 5)
    draw.line([(24, 30), (24, 20)], fill=STEEL, width=2)
    draw.rectangle([20, 18, 28, 22], fill=BLACK)
    draw.rounded_rectangle([18, 24, 34, 34], radius=3, fill=DKGREEN)
    draw.ellipse([24, 22, 32, 28], fill=BLACK)
    draw_wheel(draw, 26, 34, 4)

items = [
    ("military_tank", draw_military_tank),
    ("quadcopter", draw_quadcopter),
    ("tricycle", draw_tricycle),
    ("amphibious_car", draw_amphibious_car),
    ("hot_rod", draw_hot_rod),
    ("recumbent_bike", draw_recumbent_bike),
    ("cargo_bike", draw_cargo_bike),
    ("electric_skateboard", draw_electric_skateboard),
    ("solar_car", draw_solar_car),
    ("cable_ferry", draw_cable_ferry),
    ("jetpack", draw_jetpack),
    ("flying_car", draw_flying_car),
    ("zeppelin", draw_zeppelin),
    ("ironclad", draw_ironclad),
    ("hydroplane", draw_hydroplane),
    ("bathyscaphe", draw_bathyscaphe),
    ("airboat", draw_airboat),
    ("hoverbike", draw_hoverbike),
    ("mobility_scooter", draw_mobility_scooter),
    ("front_loader", draw_front_loader),
    ("backhoe", draw_backhoe),
    ("crane_truck", draw_crane_truck),
    ("concrete_pump", draw_concrete_pump),
    ("cherry_picker", draw_cherry_picker),
    ("snowcat", draw_snowcat),
    ("baggage_tug", draw_baggage_tug),
    ("pushback_tractor", draw_pushback_tractor),
    ("trencher", draw_trencher),
    ("mining_truck", draw_mining_truck),
    ("road_grader", draw_road_grader),
    ("asphalt_paver", draw_asphalt_paver),
    ("combine_harvester", draw_combine_harvester),
    ("hay_baler", draw_hay_baler),
    ("reach_stacker", draw_reach_stacker),
    ("maglev", draw_maglev),
    ("draisine", draw_draisine),
    ("subway_car", draw_subway_car),
    ("funicular", draw_funicular),
    ("cog_railway", draw_cog_railway),
    ("outrigger_canoe", draw_outrigger_canoe),
    ("banana_boat", draw_banana_boat),
    ("gondola_lift", draw_gondola_lift),
    ("flying_boat", draw_flying_boat),
    ("space_capsule", draw_space_capsule),
    ("asteroid_miner", draw_asteroid_miner),
    ("amphibious_atv", draw_amphibious_atv),
    ("dragster", draw_dragster),
    ("mars_rover", draw_mars_rover),
    ("diesel_locomotive", draw_diesel_locomotive),
    ("sidecar_motorcycle", draw_sidecar_motorcycle)
]

print(f"Generating {len(items)} heavily detailed vehicle sprites in '{OUTPUT_DIR}'...")
for name, func in items:
    create_sprite(name, func)
print("\nAll 50 new vehicle sprites generated successfully!")
