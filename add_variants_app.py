import sys

variants = [
    # T-Shirts
    ("tshirt_neon_green", "Neon Green T-Shirt", "Tops"),
    ("tshirt_sunset_orange", "Sunset Orange T-Shirt", "Tops"),
    ("tshirt_midnight_blue", "Midnight Blue T-Shirt", "Tops"),
    ("tshirt_cherry_blossom", "Cherry Blossom T-Shirt", "Tops"),
    ("tshirt_lemon_yellow", "Lemon Yellow T-Shirt", "Tops"),
    
    # Jeans
    ("jeans_faded_blue", "Faded Blue Jeans", "Bottoms"),
    ("jeans_charcoal_grey", "Charcoal Grey Jeans", "Bottoms"),
    ("jeans_olive_green", "Olive Green Jeans", "Bottoms"),
    ("jeans_crimson_red", "Crimson Red Jeans", "Bottoms"),
    ("jeans_acid_wash", "Acid Wash Jeans", "Bottoms"),
    
    # Hoodies
    ("hoodie_lavender", "Lavender Hoodie", "Tops"),
    ("hoodie_maroon", "Maroon Hoodie", "Tops"),
    ("hoodie_teal", "Teal Hoodie", "Tops"),
    ("hoodie_mustard", "Mustard Hoodie", "Tops"),
    ("hoodie_coral", "Coral Hoodie", "Tops"),
    
    # Sneakers
    ("sneakers_mint_choc", "Mint Choc Sneakers", "Footwear"),
    ("sneakers_retro_pink", "Retro Pink Sneakers", "Footwear"),
    ("sneakers_stealth_black", "Stealth Black Sneakers", "Footwear"),
    ("sneakers_golden_glow", "Golden Glow Sneakers", "Footwear"),
    ("sneakers_purple_haze", "Purple Haze Sneakers", "Footwear"),
    
    # Beanies
    ("beanie_candy_cane", "Candy Cane Beanie", "Accessories"),
    ("beanie_forest_elf", "Forest Elf Beanie", "Accessories"),
    ("beanie_ocean_wave", "Ocean Wave Beanie", "Accessories"),
    ("beanie_pumpkin_spice", "Pumpkin Spice Beanie", "Accessories"),
    ("beanie_plum_fairy", "Plum Fairy Beanie", "Accessories"),
    
    # Scarves
    ("scarf_bumblebee", "Bumblebee Scarf", "Accessories"),
    ("scarf_watermelon", "Watermelon Scarf", "Accessories"),
    ("scarf_starry_night", "Starry Night Scarf", "Accessories"),
    ("scarf_rainbow_dash", "Rainbow Dash Scarf", "Accessories"),
    ("scarf_coffee_bean", "Coffee Bean Scarf", "Accessories"),
    
    # Skirts
    ("skirt_bubblegum", "Bubblegum Skirt", "Bottoms"),
    ("skirt_emerald_city", "Emerald City Skirt", "Bottoms"),
    ("skirt_ruby_slipper", "Ruby Slipper Skirt", "Bottoms"),
    ("skirt_silver_lining", "Silver Lining Skirt", "Bottoms"),
    ("skirt_lilac_dream", "Lilac Dream Skirt", "Bottoms"),
    
    # Dresses
    ("dress_cinderella", "Cinderella Dress", "Dresses"),
    ("dress_belle", "Belle Dress", "Dresses"),
    ("dress_tinkerbell", "Tinkerbell Dress", "Dresses"),
    ("dress_aurora", "Aurora Dress", "Dresses"),
    ("dress_snow_white", "Snow White Dress", "Dresses"),
    
    # Sweaters
    ("sweater_ugly_xmas", "Ugly Xmas Sweater", "Tops"),
    ("sweater_cozy_cream", "Cozy Cream Sweater", "Tops"),
    ("sweater_neon_nights", "Neon Nights Sweater", "Tops"),
    ("sweater_candy_floss", "Candy Floss Sweater", "Tops"),
    ("sweater_autumn_leaf", "Autumn Leaf Sweater", "Tops"),
    
    # Socks
    ("socks_sporty_spice", "Sporty Spice Socks", "Footwear"),
    ("socks_zebra_stripe", "Zebra Stripe Socks", "Footwear"),
    ("socks_watermelon_sugar", "Watermelon Sugar Socks", "Footwear"),
    ("socks_galaxy_quest", "Galaxy Quest Socks", "Footwear"),
    ("socks_lucky_clover", "Lucky Clover Socks", "Footwear")
]

new_lines = []
for idx, (vid, name, vtype) in enumerate(variants):
    desc = f"A colorful {name.lower()} variant."
    ending = "," if idx < len(variants) - 1 else ""
    line = f'    {{ id: "{vid}", name: "{name}", filename: "images/clothing/{vid}_50x50.png", category: "clothing", type: "{vtype}", material: "Various", rarity: "★★★☆☆", description: "{desc}" }}{ending}'
    new_lines.append(line)

with open("app.js", "r") as f:
    content = f.read()

target = '    { id: "scrubs_hat", name: "Medical Scrub Cap", filename: "images/clothing/scrubs_hat_50x50.png", category: "clothing", type: "Accessories", material: "Cotton", rarity: "★★☆☆☆", description: "A clean teal medical scrub cap tied with back straps." }\n];'

replacement = '    { id: "scrubs_hat", name: "Medical Scrub Cap", filename: "images/clothing/scrubs_hat_50x50.png", category: "clothing", type: "Accessories", material: "Cotton", rarity: "★★☆☆☆", description: "A clean teal medical scrub cap tied with back straps." },\n' + "\n".join(new_lines) + '\n];'

if target in content:
    content = content.replace(target, replacement)
    with open("app.js", "w") as f:
        f.write(content)
    print("Success")
else:
    print("Target not found")
