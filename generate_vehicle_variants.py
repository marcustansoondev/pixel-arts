import os
from PIL import Image, ImageDraw

OUTPUT_DIR = "images/vehicles"
os.makedirs(OUTPUT_DIR, exist_ok=True)

def create_sprite(name, draw_func):
    base_img = Image.new("RGBA", (50, 50), (255, 255, 255, 0))
    draw = ImageDraw.Draw(base_img)
    draw_func(draw)
    
    r, g, b, a = base_img.split()
    shadow_mask = a.point(lambda p: 255 if p > 128 else 0)
    
    combined = Image.new("RGBA", (50, 50), (255, 255, 255, 0))
    shadow_color = Image.new("RGBA", (50, 50), (30, 30, 35, 255))
    combined.paste(shadow_color, (2, 2), mask=shadow_mask)
    
    combined = Image.alpha_composite(combined, base_img)
    
    gloss = Image.new("RGBA", (50, 50), (0, 0, 0, 0))
    gloss_draw = ImageDraw.Draw(gloss)
    gloss_draw.polygon([(0, 0), (35, 0), (0, 35)], fill=(255, 255, 255, 45))
    gloss_draw.polygon([(50, 25), (50, 50), (25, 50)], fill=(0, 0, 0, 45))
    gloss_masked = Image.new("RGBA", (50, 50), (0, 0, 0, 0))
    gloss_masked.paste(gloss, (0, 0), mask=shadow_mask)
    combined = Image.alpha_composite(combined, gloss_masked)
    
    flat = Image.new("RGB", (50, 50), (255, 255, 255))
    comb_a = combined.split()[3].point(lambda p: 255 if p > 128 else 0)
    flat.paste(combined, mask=comb_a)
    
    q = flat.quantize(colors=8, method=Image.MEDIANCUT)
    final = q.convert("RGBA")
    
    data = final.getdata()
    alpha_data = comb_a.getdata()
    new_data = []
    for i in range(len(data)):
        if alpha_data[i] == 0:
            new_data.append((0, 0, 0, 0))
        else:
            new_data.append((data[i][0], data[i][1], data[i][2], 255))
    final.putdata(new_data)
    
    path = os.path.join(OUTPUT_DIR, f"{name}_50x50.png")
    final.save(path)
    print(f"Saved: {path}")

def make_sedan(base_c, dark_c, win_c):
    def draw(d):
        d.rectangle([12, 38, 38, 40], fill=(80,80,85,255)) 
        d.rounded_rectangle([10, 22, 40, 36], radius=4, fill=base_c)
        d.rectangle([10, 29, 40, 36], fill=dark_c)
        d.polygon([(14, 22), (18, 14), (32, 14), (36, 22)], fill=win_c)
        d.polygon([(20, 15), (23, 15), (17, 22), (14, 22)], fill=(245,245,245,255)) 
        d.line([8, 30, 10, 30], fill=(180,180,190,255), width=2)
        d.line([40, 30, 42, 30], fill=(180,180,190,255), width=2)
        d.rectangle([10, 25, 12, 28], fill=(240,200,30,255)) 
        d.rectangle([38, 25, 40, 28], fill=(210,45,45,255)) 
        d.ellipse([14, 32, 22, 40], fill=(25,25,25,255))
        d.ellipse([16, 34, 20, 38], fill=(180,180,190,255))
        d.ellipse([28, 32, 36, 40], fill=(25,25,25,255))
        d.ellipse([30, 34, 34, 38], fill=(180,180,190,255))
    return draw

def make_sports_car(base_c, dark_c, stripe_c):
    def draw(d):
        d.rectangle([10, 36, 40, 38], fill=(80,80,85,255)) 
        d.polygon([(8, 26), (12, 18), (34, 18), (42, 26), (42, 34), (8, 34)], fill=base_c)
        d.rectangle([8, 30, 42, 34], fill=dark_c)
        d.polygon([(14, 24), (20, 16), (30, 16), (34, 24)], fill=(25,25,25,255)) 
        d.line([(18, 22), (24, 17)], fill=(170,220,250,255), width=1)
        d.line([(38, 20), (38, 15)], fill=(25,25,25,255), width=2)
        d.rectangle([(36, 14), (43, 16)], fill=stripe_c)
        d.rectangle([8, 26, 10, 29], fill=(240,200,30,255)) 
        d.rectangle([41, 26, 43, 29], fill=(235,110,25,255))
        d.ellipse([12, 30, 20, 38], fill=(25,25,25,255))
        d.ellipse([14, 32, 18, 36], fill=(180,180,190,255))
        d.ellipse([30, 30, 38, 38], fill=(25,25,25,255))
        d.ellipse([32, 32, 36, 36], fill=(180,180,190,255))
    return draw

def make_pickup(base_c, dark_c):
    def draw(d):
        d.rectangle([10, 38, 40, 40], fill=(80,80,85,255))
        d.rounded_rectangle([8, 22, 42, 36], radius=2, fill=base_c)
        d.rectangle([8, 29, 42, 36], fill=dark_c)
        d.rectangle([10, 14, 24, 22], fill=base_c)
        d.rectangle([12, 15, 22, 21], fill=(170,220,250,255))
        d.line([(14, 15), (18, 20)], fill=(245,245,245,255), width=1)
        d.rectangle([25, 20, 40, 24], fill=(0,0,0,0))
        d.rounded_rectangle([26, 17, 39, 21], radius=1, fill=(130,85,45,255))
        d.rounded_rectangle([29, 13, 37, 17], radius=1, fill=(130,85,45,255))
        d.line([6, 31, 8, 31], fill=(180,180,190,255), width=2)
        d.rectangle([8, 24, 9, 27], fill=(240,200,30,255))
        d.rectangle([41, 24, 42, 27], fill=(210,45,45,255))
        d.ellipse([12, 32, 20, 40], fill=(25,25,25,255))
        d.ellipse([14, 34, 18, 38], fill=(180,180,190,255))
        d.ellipse([30, 32, 38, 40], fill=(25,25,25,255))
        d.ellipse([32, 34, 36, 38], fill=(180,180,190,255))
    return draw

def make_suv(base_c, dark_c):
    def draw(d):
        d.rectangle([10, 38, 40, 40], fill=(80,80,85,255))
        d.rounded_rectangle([8, 18, 42, 36], radius=4, fill=base_c)
        d.rectangle([8, 27, 42, 36], fill=dark_c)
        d.rectangle([12, 14, 38, 22], fill=(25,25,25,255))
        d.line([(14, 14), (20, 21)], fill=(170,220,250,255), width=1)
        d.line([(26, 14), (32, 21)], fill=(170,220,250,255), width=1)
        d.line([12, 16, 38, 16], fill=(25,25,25,255), width=2)
        d.rectangle([8, 22, 10, 26], fill=(180,180,190,255))
        d.rectangle([8, 20, 9, 22], fill=(240,200,30,255))
        d.ellipse([12, 32, 20, 40], fill=(25,25,25,255))
        d.ellipse([14, 34, 18, 38], fill=base_c)
        d.ellipse([30, 32, 38, 40], fill=(25,25,25,255))
        d.ellipse([32, 34, 36, 38], fill=base_c)
    return draw

def make_minivan(base_c, dark_c):
    def draw(d):
        d.rectangle([10, 38, 40, 40], fill=(80,80,85,255))
        d.rounded_rectangle([8, 18, 42, 36], radius=4, fill=base_c)
        d.rectangle([8, 28, 42, 36], fill=dark_c)
        d.rectangle([12, 14, 36, 22], fill=(170,220,250,255))
        d.line([(18, 14), (18, 22)], fill=(25,25,25,255), width=2)
        d.line([(28, 14), (28, 22)], fill=(25,25,25,255), width=2)
        d.line([20, 26, 38, 26], fill=(80,80,85,255), width=1)
        d.rectangle([8, 23, 9, 26], fill=(240,200,30,255))
        d.rectangle([41, 23, 42, 26], fill=(210,45,45,255))
        d.ellipse([12, 32, 20, 40], fill=(25,25,25,255))
        d.ellipse([14, 34, 18, 38], fill=(180,180,190,255))
        d.ellipse([30, 32, 38, 40], fill=(25,25,25,255))
        d.ellipse([32, 34, 36, 38], fill=(180,180,190,255))
    return draw

def make_convertible(base_c, dark_c, seat_c):
    def draw(d):
        d.rectangle([10, 38, 40, 40], fill=(80,80,85,255))
        d.rounded_rectangle([8, 24, 42, 36], radius=3, fill=base_c)
        d.rectangle([8, 30, 42, 36], fill=dark_c)
        d.rectangle([18, 20, 32, 24], fill=seat_c)
        d.ellipse([26, 18, 30, 22], fill=(130,85,45,255))
        d.line([(16, 24), (20, 16)], fill=(180,180,190,255), width=2)
        d.line([(17, 24), (20, 18)], fill=(170,220,250,255), width=1)
        d.ellipse([12, 32, 20, 40], fill=(25,25,25,255))
        d.ellipse([14, 34, 18, 38], fill=(180,180,190,255))
        d.ellipse([30, 32, 38, 40], fill=(25,25,25,255))
        d.ellipse([32, 34, 36, 38], fill=(180,180,190,255))
    return draw

def make_motorcycle(base_c):
    def draw(d):
        d.ellipse([18, 22, 32, 30], fill=base_c)
        d.line([19, 23, 29, 23], fill=(245,245,245,255), width=2)
        d.rectangle([20, 29, 28, 35], fill=(120,125,135,255))
        d.line([(28, 32), (38, 32)], fill=(180,180,190,255), width=2)
        d.line([(28, 22), (16, 34)], fill=(120,125,135,255), width=3)
        d.ellipse([10, 28, 22, 40], fill=(25,25,25,255))
        d.ellipse([14, 32, 18, 36], fill=(180,180,190,255))
        d.ellipse([28, 28, 40, 40], fill=(25,25,25,255))
        d.ellipse([32, 32, 36, 36], fill=(180,180,190,255))
    return draw

def make_scooter(base_c, seat_c):
    def draw(d):
        d.chord([12, 20, 24, 38], 0, 180, fill=base_c)
        d.rounded_rectangle([20, 26, 38, 36], radius=4, fill=base_c)
        d.rectangle([24, 24, 32, 27], fill=seat_c)
        d.ellipse([12, 20, 16, 24], fill=(245,245,245,255))
        d.ellipse([14, 32, 20, 38], fill=(25,25,25,255))
        d.ellipse([16, 34, 18, 36], fill=(180,180,190,255))
        d.ellipse([30, 32, 36, 38], fill=(25,25,25,255))
        d.ellipse([32, 34, 34, 36], fill=(180,180,190,255))
    return draw

def make_race_car(base_c, dark_c, wing_c):
    def draw(d):
        d.rectangle([8, 36, 42, 38], fill=(80,80,85,255))
        d.rectangle([6, 28, 44, 36], fill=base_c)
        d.rectangle([6, 32, 44, 36], fill=dark_c)
        d.rectangle([4, 32, 9, 35], fill=wing_c)
        d.rectangle([40, 20, 44, 28], fill=wing_c)
        d.rectangle([43, 18, 45, 30], fill=(25,25,25,255))
        d.ellipse([22, 20, 28, 26], fill=(240,200,30,255))
        d.rectangle([24, 21, 28, 23], fill=(25,25,25,255))
        d.ellipse([10, 28, 18, 36], fill=(25,25,25,255))
        d.ellipse([12, 30, 16, 34], fill=(240,200,30,255))
        d.ellipse([32, 28, 40, 36], fill=(25,25,25,255))
        d.ellipse([34, 30, 38, 34], fill=(240,200,30,255))
    return draw

def make_hot_air_balloon(base_c, stripe_c):
    def draw(d):
        d.ellipse([14, 6, 36, 30], fill=base_c)
        d.chord([18, 16, 32, 32], 0, 180, fill=stripe_c)
        d.ellipse([22, 8, 28, 28], fill=(25,25,25,255))
        d.polygon([(23, 33), (27, 33), (25, 30)], fill=(235,110,25,255))
        d.rectangle([22, 36, 28, 42], fill=(130,85,45,255))
        d.line([(22, 30), (22, 36)], fill=(25,25,25,255), width=1)
        d.line([(28, 30), (28, 36)], fill=(25,25,25,255), width=1)
    return draw

if __name__ == "__main__":
    variants = [
        # Sedan
        ("sedan_neon", make_sedan((57,255,20,255), (0,100,0,255), (170,220,250,255))),
        ("sedan_midnight", make_sedan((25,25,112,255), (0,0,50,255), (170,220,250,255))),
        ("sedan_cherry", make_sedan((255,183,197,255), (255,20,147,255), (170,220,250,255))),
        ("sedan_lemon", make_sedan((255,250,205,255), (255,215,0,255), (170,220,250,255))),
        ("sedan_purple", make_sedan((147,112,219,255), (138,43,226,255), (170,220,250,255))),
        
        # Sports Car
        ("sports_car_mint", make_sports_car((152,255,152,255), (34,139,34,255), (255,255,255,255))),
        ("sports_car_gold", make_sports_car((255,215,0,255), (218,165,32,255), (0,0,0,255))),
        ("sports_car_stealth", make_sports_car((40,40,40,255), (20,20,20,255), (80,80,80,255))),
        ("sports_car_magenta", make_sports_car((255,0,255,255), (139,0,139,255), (255,255,255,255))),
        ("sports_car_cyan", make_sports_car((0,255,255,255), (0,139,139,255), (0,0,0,255))),
        
        # Pickup Truck
        ("pickup_sunset", make_pickup((255,100,0,255), (139,0,0,255))),
        ("pickup_navy", make_pickup((0,0,128,255), (0,0,80,255))),
        ("pickup_forest", make_pickup((34,139,34,255), (0,100,0,255))),
        ("pickup_crimson", make_pickup((220,20,60,255), (139,0,0,255))),
        ("pickup_silver", make_pickup((192,192,192,255), (128,128,128,255))),
        
        # SUV
        ("suv_lavender", make_suv((230,230,250,255), (216,191,216,255))),
        ("suv_teal", make_suv((0,128,128,255), (0,100,100,255))),
        ("suv_maroon", make_suv((128,0,0,255), (100,0,0,255))),
        ("suv_mustard", make_suv((255,219,88,255), (218,165,32,255))),
        ("suv_coral", make_suv((255,127,80,255), (205,92,92,255))),
        
        # Minivan
        ("minivan_sky", make_minivan((135,206,235,255), (70,130,180,255))),
        ("minivan_rose", make_minivan((255,228,225,255), (255,182,193,255))),
        ("minivan_mint", make_minivan((189,252,201,255), (60,179,113,255))),
        ("minivan_sand", make_minivan((244,164,96,255), (210,105,30,255))),
        ("minivan_plum", make_minivan((221,160,221,255), (128,0,128,255))),
        
        # Convertible
        ("convertible_candy", make_convertible((255,0,0,255), (139,0,0,255), (255,255,255,255))),
        ("convertible_ocean", make_convertible((0,119,190,255), (0,0,128,255), (245,245,220,255))),
        ("convertible_lime", make_convertible((50,205,50,255), (34,139,34,255), (0,0,0,255))),
        ("convertible_grape", make_convertible((128,0,128,255), (75,0,130,255), (255,192,203,255))),
        ("convertible_pearl", make_convertible((255,250,240,255), (211,211,211,255), (139,69,19,255))),
        
        # Motorcycle
        ("motorcycle_flame", make_motorcycle((255,69,0,255))),
        ("motorcycle_ghost", make_motorcycle((248,248,255,255))),
        ("motorcycle_ninja", make_motorcycle((0,255,0,255))),
        ("motorcycle_phantom", make_motorcycle((0,0,0,255))),
        ("motorcycle_cobalt", make_motorcycle((61,89,171,255))),
        
        # Scooter
        ("scooter_peach", make_scooter((255,218,185,255), (160,82,45,255))),
        ("scooter_aqua", make_scooter((0,255,255,255), (0,0,0,255))),
        ("scooter_ruby", make_scooter((224,17,95,255), (255,255,255,255))),
        ("scooter_lemon", make_scooter((255,250,205,255), (139,69,19,255))),
        ("scooter_olive", make_scooter((128,128,0,255), (0,0,0,255))),
        
        # Race Car
        ("race_car_toxic", make_race_car((57,255,20,255), (0,100,0,255), (0,0,0,255))),
        ("race_car_blizzard", make_race_car((255,255,255,255), (192,192,192,255), (0,0,255,255))),
        ("race_car_inferno", make_race_car((255,0,0,255), (139,0,0,255), (255,215,0,255))),
        ("race_car_midnight", make_race_car((25,25,112,255), (0,0,50,255), (255,255,255,255))),
        ("race_car_bubblegum", make_race_car((255,192,203,255), (255,105,180,255), (255,255,255,255))),
        
        # Hot Air Balloon
        ("balloon_rainbow", make_hot_air_balloon((255,0,0,255), (255,255,0,255))),
        ("balloon_sunset", make_hot_air_balloon((255,140,0,255), (255,69,0,255))),
        ("balloon_ocean", make_hot_air_balloon((0,0,255,255), (0,255,255,255))),
        ("balloon_forest", make_hot_air_balloon((34,139,34,255), (173,255,47,255))),
        ("balloon_galaxy", make_hot_air_balloon((75,0,130,255), (238,130,238,255)))
    ]
    
    for name, func in variants:
        create_sprite(name, func)
