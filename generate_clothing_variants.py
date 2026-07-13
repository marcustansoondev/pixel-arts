import os
from PIL import Image, ImageDraw

OUTPUT_DIR = "images/clothing"
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

# Shape Drawing Factory Functions
def make_tshirt(base_c, accent_c):
    def draw(d):
        d.rectangle([14, 15, 36, 42], fill=base_c)
        d.rectangle([10, 15, 14, 25], fill=base_c)
        d.rectangle([36, 15, 40, 25], fill=base_c)
        d.polygon([(22, 15), (28, 15), (25, 18)], fill=accent_c)
        d.rectangle([10, 24, 14, 25], fill=accent_c)
        d.rectangle([36, 24, 40, 25], fill=accent_c)
        d.rectangle([14, 41, 36, 42], fill=accent_c)
    return draw

def make_jeans(base_c, dark_c, btn_c):
    def draw(d):
        d.rectangle([15, 12, 35, 44], fill=base_c)
        d.rectangle([24, 22, 26, 44], fill=(0,0,0,0))
        d.rectangle([15, 12, 35, 15], fill=dark_c)
        d.rectangle([18, 16, 21, 20], fill=dark_c)
        d.rectangle([29, 16, 32, 20], fill=dark_c)
        d.ellipse([24, 13, 26, 15], fill=btn_c)
    return draw

def make_hoodie(base_c, pocket_c, str_c):
    def draw(d):
        d.rectangle([14, 16, 36, 44], fill=base_c)
        d.rectangle([9, 18, 14, 38], fill=base_c)
        d.rectangle([36, 18, 41, 38], fill=base_c)
        d.rounded_rectangle([18, 8, 32, 17], radius=3, fill=base_c)
        d.rectangle([19, 32, 31, 38], fill=pocket_c)
        d.line([22, 16, 22, 22], fill=str_c, width=1)
        d.line([28, 16, 28, 22], fill=str_c, width=1)
    return draw

def make_sneakers(base_c, sole_c, lace_c):
    def draw(d):
        d.rounded_rectangle([8, 26, 24, 38], radius=2, fill=base_c)
        d.rectangle([8, 36, 24, 38], fill=sole_c)
        d.polygon([(18, 26), (24, 26), (24, 35)], fill=sole_c)
        d.line([14, 28, 18, 28], fill=lace_c)
        
        d.rounded_rectangle([26, 26, 42, 38], radius=2, fill=base_c)
        d.rectangle([26, 36, 42, 38], fill=sole_c)
        d.polygon([(26, 26), (32, 26), (26, 35)], fill=sole_c)
        d.line([32, 28, 36, 28], fill=lace_c)
    return draw

def make_beanie(base_c, brim_c, pom_c):
    def draw(d):
        d.ellipse([14, 13, 36, 38], fill=base_c)
        d.rectangle([12, 30, 38, 38], fill=brim_c)
        d.ellipse([22, 7, 28, 13], fill=pom_c)
    return draw

def make_scarf(base_c, str1_c, str2_c):
    def draw(d):
        d.rounded_rectangle([14, 15, 36, 25], radius=2, fill=base_c)
        d.rectangle([16, 25, 22, 42], fill=base_c)
        d.rectangle([26, 25, 31, 38], fill=base_c)
        for y in [18, 22]:
            d.line([14, y, 36, y], fill=str1_c, width=1)
        for y in [28, 34, 40]:
            d.line([16, y, 22, y], fill=str2_c, width=1)
    return draw

def make_skirt(base_c, pleat_c):
    def draw(d):
        d.polygon([(18, 18), (32, 18), (40, 42), (10, 42)], fill=base_c)
        for x in range(14, 38, 4):
            d.line([x, 18, x*1.1 - 2, 42], fill=pleat_c, width=1)
    return draw

def make_dress(base_c, sparkle_c):
    def draw(d):
        d.polygon([(18, 14), (32, 14), (28, 24), (22, 24)], fill=base_c)
        d.polygon([(22, 24), (28, 24), (42, 46), (8, 46)], fill=base_c)
        d.ellipse([20, 18, 21, 19], fill=sparkle_c)
        d.ellipse([30, 28, 31, 29], fill=sparkle_c)
        d.ellipse([15, 40, 16, 41], fill=sparkle_c)
    return draw

def make_sweater(base_c, str_c, pat_c):
    def draw(d):
        d.rectangle([13, 14, 37, 43], fill=base_c)
        d.rectangle([8, 16, 13, 38], fill=base_c)
        d.rectangle([37, 16, 42, 38], fill=base_c)
        d.line([13, 24, 37, 24], fill=str_c, width=1)
        d.line([13, 28, 37, 28], fill=str_c, width=1)
        for x in range(15, 36, 5):
            d.line([x, 24, x+2, 28], fill=pat_c, width=1)
    return draw

def make_socks(base_c, str1_c, str2_c):
    def draw(d):
        d.rectangle([13, 15, 20, 34], fill=base_c)
        d.rectangle([13, 31, 25, 36], fill=base_c)
        d.rectangle([13, 15, 20, 17], fill=str1_c)
        d.rectangle([13, 19, 20, 21], fill=str2_c)
        
        d.rectangle([28, 15, 35, 34], fill=base_c)
        d.rectangle([28, 31, 40, 36], fill=base_c)
        d.rectangle([28, 15, 35, 17], fill=str1_c)
        d.rectangle([28, 19, 35, 21], fill=str2_c)
    return draw

if __name__ == "__main__":
    variants = [
        # T-Shirts
        ("tshirt_neon_green", make_tshirt((57,255,20,255), (255,255,255,255))),
        ("tshirt_sunset_orange", make_tshirt((255,100,0,255), (0,0,0,255))),
        ("tshirt_midnight_blue", make_tshirt((25,25,112,255), (173,216,230,255))),
        ("tshirt_cherry_blossom", make_tshirt((255,183,197,255), (255,20,147,255))),
        ("tshirt_lemon_yellow", make_tshirt((255,250,205,255), (255,215,0,255))),
        
        # Jeans
        ("jeans_faded_blue", make_jeans((135,206,235,255), (100,149,237,255), (218,165,32,255))),
        ("jeans_charcoal_grey", make_jeans((54,69,79,255), (40,40,40,255), (192,192,192,255))),
        ("jeans_olive_green", make_jeans((85,107,47,255), (107,142,35,255), (205,133,63,255))),
        ("jeans_crimson_red", make_jeans((220,20,60,255), (139,0,0,255), (255,215,0,255))),
        ("jeans_acid_wash", make_jeans((224,255,255,255), (175,238,238,255), (169,169,169,255))),
        
        # Hoodies
        ("hoodie_lavender", make_hoodie((230,230,250,255), (216,191,216,255), (255,255,255,255))),
        ("hoodie_maroon", make_hoodie((128,0,0,255), (100,0,0,255), (192,192,192,255))),
        ("hoodie_teal", make_hoodie((0,128,128,255), (0,100,100,255), (0,255,255,255))),
        ("hoodie_mustard", make_hoodie((255,219,88,255), (218,165,32,255), (139,69,19,255))),
        ("hoodie_coral", make_hoodie((255,127,80,255), (205,92,92,255), (255,228,225,255))),
        
        # Sneakers
        ("sneakers_mint_choc", make_sneakers((152,255,152,255), (101,67,33,255), (255,255,255,255))),
        ("sneakers_retro_pink", make_sneakers((255,105,180,255), (0,255,255,255), (255,255,0,255))),
        ("sneakers_stealth_black", make_sneakers((40,40,40,255), (20,20,20,255), (80,80,80,255))),
        ("sneakers_golden_glow", make_sneakers((255,215,0,255), (255,255,255,255), (218,165,32,255))),
        ("sneakers_purple_haze", make_sneakers((147,112,219,255), (138,43,226,255), (230,230,250,255))),
        
        # Beanies
        ("beanie_candy_cane", make_beanie((255,0,0,255), (255,255,255,255), (255,255,255,255))),
        ("beanie_forest_elf", make_beanie((34,139,34,255), (0,100,0,255), (173,255,47,255))),
        ("beanie_ocean_wave", make_beanie((0,119,190,255), (0,191,255,255), (224,255,255,255))),
        ("beanie_pumpkin_spice", make_beanie((210,105,30,255), (139,69,19,255), (255,140,0,255))),
        ("beanie_plum_fairy", make_beanie((221,160,221,255), (128,0,128,255), (255,192,203,255))),
        
        # Scarves
        ("scarf_bumblebee", make_scarf((255,215,0,255), (0,0,0,255), (0,0,0,255))),
        ("scarf_watermelon", make_scarf((252,108,133,255), (34,139,34,255), (0,0,0,255))),
        ("scarf_starry_night", make_scarf((0,0,128,255), (255,215,0,255), (255,255,255,255))),
        ("scarf_rainbow_dash", make_scarf((0,191,255,255), (255,0,0,255), (255,255,0,255))),
        ("scarf_coffee_bean", make_scarf((111,78,55,255), (210,180,140,255), (245,222,179,255))),
        
        # Skirts
        ("skirt_bubblegum", make_skirt((255,192,203,255), (255,105,180,255))),
        ("skirt_emerald_city", make_skirt((80,200,120,255), (46,139,87,255))),
        ("skirt_ruby_slipper", make_skirt((224,17,95,255), (139,0,0,255))),
        ("skirt_silver_lining", make_skirt((192,192,192,255), (105,105,105,255))),
        ("skirt_lilac_dream", make_skirt((200,162,200,255), (147,112,219,255))),
        
        # Dresses
        ("dress_cinderella", make_dress((173,216,230,255), (255,255,255,255))),
        ("dress_belle", make_dress((255,215,0,255), (255,255,255,255))),
        ("dress_tinkerbell", make_dress((154,205,50,255), (255,255,255,255))),
        ("dress_aurora", make_dress((255,182,193,255), (255,20,147,255))),
        ("dress_snow_white", make_dress((255,250,250,255), (255,0,0,255))),
        
        # Sweaters
        ("sweater_ugly_xmas", make_sweater((0,128,0,255), (255,0,0,255), (255,255,255,255))),
        ("sweater_cozy_cream", make_sweater((255,253,208,255), (210,180,140,255), (139,69,19,255))),
        ("sweater_neon_nights", make_sweater((0,0,0,255), (57,255,20,255), (255,0,255,255))),
        ("sweater_candy_floss", make_sweater((255,182,193,255), (173,216,230,255), (255,255,255,255))),
        ("sweater_autumn_leaf", make_sweater((210,105,30,255), (255,140,0,255), (139,69,19,255))),
        
        # Socks
        ("socks_sporty_spice", make_socks((255,255,255,255), (0,0,255,255), (255,0,0,255))),
        ("socks_zebra_stripe", make_socks((255,255,255,255), (0,0,0,255), (0,0,0,255))),
        ("socks_watermelon_sugar", make_socks((255,182,193,255), (50,205,50,255), (220,20,60,255))),
        ("socks_galaxy_quest", make_socks((75,0,130,255), (255,20,147,255), (0,191,255,255))),
        ("socks_lucky_clover", make_socks((0,255,127,255), (34,139,34,255), (255,215,0,255)))
    ]
    
    for name, func in variants:
        create_sprite(name, func)
