import sys

variants = [
    # Sedan
    ("sedan_neon", "Neon Sedan", "Cars"),
    ("sedan_midnight", "Midnight Sedan", "Cars"),
    ("sedan_cherry", "Cherry Sedan", "Cars"),
    ("sedan_lemon", "Lemon Sedan", "Cars"),
    ("sedan_purple", "Purple Sedan", "Cars"),
    
    # Sports Car
    ("sports_car_mint", "Mint Sports Car", "Cars"),
    ("sports_car_gold", "Gold Sports Car", "Cars"),
    ("sports_car_stealth", "Stealth Sports Car", "Cars"),
    ("sports_car_magenta", "Magenta Sports Car", "Cars"),
    ("sports_car_cyan", "Cyan Sports Car", "Cars"),
    
    # Pickup Truck
    ("pickup_sunset", "Sunset Pickup", "Trucks"),
    ("pickup_navy", "Navy Pickup", "Trucks"),
    ("pickup_forest", "Forest Pickup", "Trucks"),
    ("pickup_crimson", "Crimson Pickup", "Trucks"),
    ("pickup_silver", "Silver Pickup", "Trucks"),
    
    # SUV
    ("suv_lavender", "Lavender SUV", "Cars"),
    ("suv_teal", "Teal SUV", "Cars"),
    ("suv_maroon", "Maroon SUV", "Cars"),
    ("suv_mustard", "Mustard SUV", "Cars"),
    ("suv_coral", "Coral SUV", "Cars"),
    
    # Minivan
    ("minivan_sky", "Sky Minivan", "Cars"),
    ("minivan_rose", "Rose Minivan", "Cars"),
    ("minivan_mint", "Mint Minivan", "Cars"),
    ("minivan_sand", "Sand Minivan", "Cars"),
    ("minivan_plum", "Plum Minivan", "Cars"),
    
    # Convertible
    ("convertible_candy", "Candy Convertible", "Cars"),
    ("convertible_ocean", "Ocean Convertible", "Cars"),
    ("convertible_lime", "Lime Convertible", "Cars"),
    ("convertible_grape", "Grape Convertible", "Cars"),
    ("convertible_pearl", "Pearl Convertible", "Cars"),
    
    # Motorcycle
    ("motorcycle_flame", "Flame Motorcycle", "Bikes"),
    ("motorcycle_ghost", "Ghost Motorcycle", "Bikes"),
    ("motorcycle_ninja", "Ninja Motorcycle", "Bikes"),
    ("motorcycle_phantom", "Phantom Motorcycle", "Bikes"),
    ("motorcycle_cobalt", "Cobalt Motorcycle", "Bikes"),
    
    # Scooter
    ("scooter_peach", "Peach Scooter", "Bikes"),
    ("scooter_aqua", "Aqua Scooter", "Bikes"),
    ("scooter_ruby", "Ruby Scooter", "Bikes"),
    ("scooter_lemon", "Lemon Scooter", "Bikes"),
    ("scooter_olive", "Olive Scooter", "Bikes"),
    
    # Race Car
    ("race_car_toxic", "Toxic Race Car", "Cars"),
    ("race_car_blizzard", "Blizzard Race Car", "Cars"),
    ("race_car_inferno", "Inferno Race Car", "Cars"),
    ("race_car_midnight", "Midnight Race Car", "Cars"),
    ("race_car_bubblegum", "Bubblegum Race Car", "Cars"),
    
    # Hot Air Balloon
    ("balloon_rainbow", "Rainbow Hot Air Balloon", "Air"),
    ("balloon_sunset", "Sunset Hot Air Balloon", "Air"),
    ("balloon_ocean", "Ocean Hot Air Balloon", "Air"),
    ("balloon_forest", "Forest Hot Air Balloon", "Air"),
    ("balloon_galaxy", "Galaxy Hot Air Balloon", "Air")
]

new_lines = []
for idx, (vid, name, vtype) in enumerate(variants):
    desc = f"A colorful {name.lower()} variant."
    ending = "," if idx < len(variants) - 1 else ""
    line = f'    {{ id: "{vid}", name: "{name}", filename: "images/vehicles/{vid}_50x50.png", category: "vehicles", type: "{vtype}", material: "Various", rarity: "★★★☆☆", description: "{desc}" }}{ending}'
    new_lines.append(line)

with open("app.js", "r") as f:
    content = f.read()

# find the last element in vehicles
target = '    { id: "steam_yacht", name: "Luxury Steam Yacht", filename: "images/vehicles/steam_yacht_50x50.png", category: "vehicles", type: "Water", material: "Coal / Steam", rarity: "★★★★★", description: "An elegant late 19th-century pleasure yacht powered by a steam boiler." }\n];'

replacement = '    { id: "steam_yacht", name: "Luxury Steam Yacht", filename: "images/vehicles/steam_yacht_50x50.png", category: "vehicles", type: "Water", material: "Coal / Steam", rarity: "★★★★★", description: "An elegant late 19th-century pleasure yacht powered by a steam boiler." },\n' + "\n".join(new_lines) + '\n];'

if target in content:
    content = content.replace(target, replacement)
    with open("app.js", "w") as f:
        f.write(content)
    print("Success")
else:
    print("Target not found")
