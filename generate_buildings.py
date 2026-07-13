import os
import random
from PIL import Image, ImageDraw, ImageFont
import numpy as np
from enhance_weather import enhance_weather_image

OUTPUT_DIR = "images/buildings"
os.makedirs(OUTPUT_DIR, exist_ok=True)

base_types = [
    "Skyscraper", "House", "Shop", "Tower", "Station", 
    "Factory", "Museum", "Library", "Bank", "Castle", 
    "Barn", "Lighthouse", "Hospital", "School", "Restaurant", 
    "Hotel", "Cafe", "Gym", "Clinic", "Theater"
]

styles = [
    "Modern", "Rustic", "Gothic", "Cyberpunk", "Abandoned", 
    "Neon", "Minimalist", "Classic", "Futuristic", "Tropical"
]

js_objects = []

def get_style_colors(style):
    if style == "Modern":
        return {"wall": (220, 220, 220), "roof": (150, 150, 150), "window": (100, 200, 255), "accent": (50, 50, 50)}
    elif style == "Rustic":
        return {"wall": (139, 69, 19), "roof": (85, 107, 47), "window": (205, 133, 63), "accent": (101, 67, 33)}
    elif style == "Gothic":
        return {"wall": (80, 80, 80), "roof": (40, 40, 40), "window": (148, 0, 211), "accent": (0, 0, 0)}
    elif style == "Cyberpunk":
        return {"wall": (20, 20, 60), "roof": (10, 10, 30), "window": (255, 20, 147), "accent": (0, 255, 255)}
    elif style == "Abandoned":
        return {"wall": (100, 110, 90), "roof": (70, 75, 60), "window": (30, 30, 30), "accent": (50, 60, 40)}
    elif style == "Neon":
        return {"wall": (10, 10, 10), "roof": (0, 0, 0), "window": (57, 255, 20), "accent": (255, 0, 255)}
    elif style == "Minimalist":
        return {"wall": (255, 255, 255), "roof": (255, 255, 255), "window": (200, 200, 200), "accent": (255, 140, 0)}
    elif style == "Classic":
        return {"wall": (178, 34, 34), "roof": (105, 105, 105), "window": (255, 228, 196), "accent": (245, 245, 220)}
    elif style == "Futuristic":
        return {"wall": (192, 192, 192), "roof": (211, 211, 211), "window": (0, 255, 255), "accent": (255, 255, 255)}
    elif style == "Tropical":
        return {"wall": (255, 255, 153), "roof": (34, 139, 34), "window": (173, 216, 230), "accent": (255, 105, 180)}
    return {"wall": (200, 200, 200), "roof": (100, 100, 100), "window": (150, 150, 255), "accent": (50, 50, 50)}

def draw_building(draw, btype, colors):
    w, r, win, a = colors["wall"], colors["roof"], colors["window"], colors["accent"]
    
    if btype == "Skyscraper":
        draw.rectangle([15, 5, 35, 45], fill=w)
        for y in range(10, 45, 5):
            for x in (17, 23, 29):
                draw.rectangle([x, y, x+3, y+3], fill=win)
    elif btype == "House":
        draw.rectangle([10, 25, 40, 45], fill=w)
        draw.polygon([5, 25, 25, 10, 45, 25], fill=r)
        draw.rectangle([15, 30, 22, 37], fill=win)
        draw.rectangle([28, 30, 35, 37], fill=win)
        draw.rectangle([22, 35, 28, 45], fill=a) # door
    elif btype == "Shop":
        draw.rectangle([5, 20, 45, 45], fill=w)
        draw.rectangle([5, 20, 45, 25], fill=a) # awning
        draw.rectangle([10, 30, 25, 40], fill=win) # display window
        draw.rectangle([32, 30, 40, 45], fill=r) # door
    elif btype == "Tower":
        draw.rectangle([20, 15, 30, 45], fill=w)
        draw.polygon([15, 15, 25, 0, 35, 15], fill=r)
        draw.rectangle([23, 20, 27, 25], fill=win)
        draw.rectangle([23, 30, 27, 35], fill=win)
    elif btype == "Station":
        draw.rectangle([5, 30, 45, 45], fill=w)
        draw.chord([5, 15, 45, 45], start=180, end=0, fill=r)
        draw.rectangle([20, 35, 30, 45], fill=win) # big entrance
    elif btype == "Factory":
        draw.rectangle([5, 30, 45, 45], fill=w)
        draw.polygon([5,30, 15,20, 15,30], fill=r)
        draw.polygon([15,30, 25,20, 25,30], fill=r)
        draw.polygon([25,30, 35,20, 35,30], fill=r)
        draw.polygon([35,30, 45,20, 45,30], fill=r)
        draw.rectangle([38, 10, 42, 25], fill=a) # smokestack
    elif btype == "Museum":
        draw.rectangle([10, 25, 40, 45], fill=w)
        draw.polygon([5, 25, 25, 15, 45, 25], fill=r)
        for x in range(12, 40, 6):
            draw.rectangle([x, 25, x+2, 45], fill=a) # pillars
    elif btype == "Library":
        draw.rectangle([10, 15, 40, 45], fill=w)
        draw.rectangle([10, 15, 40, 20], fill=r)
        for y in (25, 35):
            for x in (12, 20, 28, 36):
                draw.rectangle([x, y, x+3, y+5], fill=win)
    elif btype == "Bank":
        draw.rectangle([10, 20, 40, 45], fill=w)
        draw.rectangle([5, 15, 45, 20], fill=r) # thick roof
        draw.rectangle([5, 40, 45, 45], fill=r) # thick base
        for x in (12, 22, 32):
            draw.rectangle([x, 20, x+4, 40], fill=win) # large windows/pillars
    elif btype == "Castle":
        draw.rectangle([10, 20, 40, 45], fill=w)
        # crenellations
        for x in range(10, 40, 6):
            draw.rectangle([x, 15, x+3, 20], fill=w)
        draw.chord([20, 30, 30, 50], start=180, end=0, fill=a) # arched door
    elif btype == "Barn":
        draw.rectangle([10, 25, 40, 45], fill=w)
        draw.polygon([5, 25, 15, 10, 35, 10, 45, 25], fill=r)
        draw.rectangle([20, 30, 30, 45], fill=a)
        draw.line([20,30, 30,45], fill=w, width=2)
        draw.line([30,30, 20,45], fill=w, width=2)
    elif btype == "Lighthouse":
        draw.polygon([20, 10, 30, 10, 35, 45, 15, 45], fill=w)
        draw.rectangle([22, 5, 28, 10], fill=win) # light
        draw.polygon([18, 5, 25, 0, 32, 5], fill=r)
    elif btype == "Hospital":
        draw.rectangle([10, 20, 40, 45], fill=w)
        draw.rectangle([20, 5, 30, 20], fill=w)
        draw.rectangle([22, 10, 28, 12], fill=a) # cross horizontal
        draw.rectangle([24, 8, 26, 14], fill=a) # cross vertical
        draw.rectangle([15, 25, 20, 30], fill=win)
        draw.rectangle([30, 25, 35, 30], fill=win)
    elif btype == "School":
        draw.rectangle([5, 25, 45, 45], fill=w)
        draw.rectangle([20, 15, 30, 25], fill=w)
        draw.polygon([18, 15, 25, 5, 32, 15], fill=r) # bell tower
        draw.ellipse([23, 18, 27, 22], fill=win) # clock
        for x in (8, 14, 32, 38):
            draw.rectangle([x, 30, x+4, 35], fill=win)
    elif btype == "Restaurant":
        draw.rectangle([10, 25, 40, 45], fill=w)
        draw.rectangle([8, 20, 42, 25], fill=r) # flat awning
        draw.rectangle([15, 30, 35, 40], fill=win) # large panoramic window
        draw.rectangle([20, 10, 30, 15], fill=a) # sign on roof
    elif btype == "Hotel":
        draw.rectangle([15, 10, 35, 45], fill=w)
        draw.rectangle([10, 40, 40, 45], fill=r) # lobby
        for y in (15, 22, 29):
            draw.rectangle([12, y, 38, y+3], fill=a) # balconies
    elif btype == "Cafe":
        draw.rectangle([15, 25, 35, 45], fill=w)
        draw.polygon([10, 25, 25, 15, 40, 25], fill=r)
        draw.chord([20, 18, 30, 28], start=0, end=180, fill=a) # cup symbol
        draw.rectangle([20, 32, 30, 45], fill=win) # door
    elif btype == "Gym":
        draw.rectangle([5, 25, 45, 45], fill=w)
        # dumbbell symbol
        draw.ellipse([20, 15, 24, 19], fill=a)
        draw.ellipse([26, 15, 30, 19], fill=a)
        draw.line([24, 17, 26, 17], fill=a, width=2)
        draw.rectangle([10, 30, 40, 35], fill=win) # long window
    elif btype == "Clinic":
        draw.rectangle([15, 20, 35, 45], fill=w)
        draw.polygon([10, 20, 25, 10, 40, 20], fill=r)
        draw.rectangle([22, 25, 28, 27], fill=a) # cross h
        draw.rectangle([24, 23, 26, 29], fill=a) # cross v
    elif btype == "Theater":
        draw.rectangle([10, 15, 40, 45], fill=w)
        draw.rectangle([15, 20, 35, 30], fill=a) # marquee
        draw.rectangle([12, 10, 20, 15], fill=r) # side decor
        draw.rectangle([30, 10, 38, 15], fill=r) # side decor
        draw.rectangle([20, 35, 30, 45], fill=win) # doors

idx = 1
for style in styles:
    for btype in base_types:
        img = Image.new("RGBA", (50, 50), (0, 0, 0, 0))
        draw = ImageDraw.Draw(img)
        
        colors = get_style_colors(style)
        draw_building(draw, btype, colors)
        
        name = f"{style} {btype}"
        file_name = f"building_{idx:03d}_{style.lower()}_{btype.lower()}_50x50.png"
        filepath = os.path.join(OUTPUT_DIR, file_name)
        img.save(filepath)
        
        # Apply the kid-friendly enhancement (thick black outline, max 10 solid colors)
        enhance_weather_image(filepath)
        
        desc = f"A {style.lower()} styled {btype.lower()}."
        js_objects.append(f'    {{ id: "building_{idx}", name: "{name}", filename: "images/buildings/{file_name}", category: "buildings", type: "{btype}", material: "{style}", rarity: "★☆☆☆☆", description: "{desc}" }},')
        idx += 1

with open("buildings_app.js", "w") as f:
    f.write("\n".join(js_objects))

print(f"Generated {idx-1} unique building variants successfully and saved JS data.")
