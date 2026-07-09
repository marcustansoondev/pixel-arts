import os
from PIL import Image, ImageDraw

OUTPUT_DIR = "images/animals"
os.makedirs(OUTPUT_DIR, exist_ok=True)

def create_sprite(name, draw_func):
    img = Image.new("RGBA", (50, 50), (255, 255, 255, 0))
    draw = ImageDraw.Draw(img)
    draw_func(draw)
    path = os.path.join(OUTPUT_DIR, f"{name}_50x50.png")
    img.save(path)
    print(f"  Saved: {path}")

# Color constants
RED       = (210, 50, 50, 255)
DKRED     = (130, 20, 20, 255)
LIGHTRED  = (255, 100, 100, 255)
ORANGE    = (240, 110, 30, 255)
YELLOW    = (230, 190, 40, 255)
GREEN     = (50, 150, 50, 255)
DKGREEN   = (20, 90, 20, 255)
BLUE      = (50, 110, 200, 255)
DKBLUE    = (20, 50, 130, 255)
BROWN     = (130, 90, 50, 255)
DKBROWN   = (80, 50, 25, 255)
CREAM     = (240, 220, 180, 255)
TAN       = (190, 150, 100, 255)
WHITE     = (245, 245, 245, 255)
BLACK     = (25, 25, 25, 255)
GREY      = (160, 160, 165, 255)
DKGREY    = (80, 80, 85, 255)
PINK      = (240, 150, 170, 255)
DARK      = (50, 50, 55, 255)
GLASS     = (180, 215, 240, 200)

# 1. Red Panda
def draw_red_panda(draw):
    draw.ellipse([12, 16, 38, 38], fill=ORANGE)
    draw.ellipse([14, 18, 36, 36], fill=DKRED)
    # ears
    draw.polygon([(14, 16), (10, 10), (20, 14)], fill=WHITE)
    draw.polygon([(36, 16), (40, 10), (30, 14)], fill=WHITE)
    # white muzzle/cheeks
    draw.ellipse([20, 26, 30, 34], fill=WHITE)
    draw.ellipse([23, 28, 27, 32], fill=BLACK)

# 2. Wombat
def draw_wombat(draw):
    # stout brown bear-like marsupial
    draw.ellipse([10, 14, 40, 40], fill=BROWN)
    draw.ellipse([12, 16, 38, 38], fill=TAN)
    # small nose and ears
    draw.ellipse([22, 24, 28, 30], fill=BLACK)
    draw.polygon([(14, 16), (12, 10), (20, 14)], fill=BROWN)
    draw.polygon([(36, 16), (38, 10), (30, 14)], fill=BROWN)

# 3. Echidna
def draw_echidna(draw):
    draw.ellipse([14, 16, 38, 38], fill=BROWN)
    # beak
    draw.line([(25, 30), (10, 30)], fill=BLACK, width=3)
    # spines
    for sx, sy in [(16, 12), (24, 10), (32, 12), (38, 18), (38, 26), (34, 34), (20, 34)]:
        draw.line([(25, 25), (sx, sy)], fill=TAN, width=2)

# 4. Quokka
def draw_quokka(draw):
    # smiling small brown wallaby
    draw.ellipse([12, 14, 38, 38], fill=BROWN)
    draw.ellipse([14, 16, 36, 36], fill=TAN)
    # smile
    draw.arc([20, 24, 30, 32], 0, 180, fill=BLACK, width=2)
    # black nose
    draw.ellipse([23, 22, 27, 26], fill=BLACK)
    # ears
    draw.ellipse([12, 10, 18, 16], fill=BROWN)
    draw.ellipse([32, 10, 38, 16], fill=BROWN)

# 5. Tasmanian Devil
def draw_tasmanian_devil(draw):
    draw.ellipse([12, 14, 38, 40], fill=BLACK)
    # pink ears
    draw.polygon([(14, 16), (10, 10), (20, 14)], fill=PINK)
    draw.polygon([(36, 16), (40, 10), (30, 14)], fill=PINK)
    # white chest stripe
    draw.arc([16, 26, 34, 38], 0, 180, fill=WHITE, width=3)

# 6. Anteater
def draw_anteater(draw):
    # long snout and bushy tail
    draw.ellipse([18, 16, 38, 36], fill=GREY)
    # long tubular snout
    draw.line([(24, 28), (6, 28)], fill=DKGREY, width=4)
    # black stripe
    draw.line([(18, 24), (32, 34)], fill=BLACK, width=4)

# 7. Pangolin
def draw_pangolin(draw):
    # scaly rolled animal
    draw.ellipse([12, 16, 38, 38], fill=DKBROWN)
    # overlapping scale arcs
    for y in range(18, 36, 4):
        draw.arc([14, y, 36, y+6], 0, 180, fill=TAN, width=2)

# 8. Tapir
def draw_tapir(draw):
    # black front/back, white middle, short trunk
    draw.ellipse([10, 16, 24, 38], fill=BLACK) # head/front
    draw.ellipse([22, 16, 36, 38], fill=WHITE) # middle
    draw.ellipse([34, 16, 42, 38], fill=BLACK) # back
    # short flexible proboscis snout
    draw.line([(14, 28), (6, 32)], fill=DKGREY, width=4)

# 9. Okapi
def draw_okapi(draw):
    # brown body, striped legs
    draw.ellipse([14, 14, 36, 36], fill=DKBROWN)
    # striped rear
    draw.rectangle([32, 22, 38, 36], fill=WHITE)
    for y in range(24, 36, 3):
        draw.line([32, y, 38, y], fill=BLACK, width=1)
    # giraffe-like head
    draw.line([(18, 18), (14, 8)], fill=DKBROWN, width=4)
    draw.ellipse([12, 6, 16, 10], fill=CREAM)

# 10. Hyena
def draw_hyena(draw):
    # spotted brown dog-like predator
    draw.ellipse([12, 14, 38, 38], fill=TAN)
    # spots
    for sx, sy in [(16, 20), (32, 22), (20, 30), (30, 32), (25, 26)]:
        draw.ellipse([sx-1, sy-1, sx+1, sy+1], fill=DKBROWN)
    # ears
    draw.ellipse([13, 10, 19, 16], fill=DKBROWN)
    draw.ellipse([31, 10, 37, 16], fill=DKBROWN)

# 11. Mongoose
def draw_mongoose(draw):
    # slender brown mammal
    draw.rounded_rectangle([10, 20, 42, 32], radius=4, fill=BROWN)
    draw.ellipse([8, 18, 16, 26], fill=TAN) # head
    draw.line([(40, 26), (48, 20)], fill=BROWN, width=3) # tail

# 12. Weasel
def draw_weasel(draw):
    # long slender reddish-brown body with white belly
    draw.rounded_rectangle([8, 20, 42, 28], radius=3, fill=BROWN)
    draw.rounded_rectangle([10, 25, 36, 29], radius=1, fill=WHITE)
    draw.ellipse([6, 18, 12, 24], fill=BROWN) # head

# 13. Ferret
def draw_ferret(draw):
    # mask on face
    draw.rounded_rectangle([10, 20, 40, 30], radius=4, fill=CREAM)
    draw.ellipse([8, 16, 16, 24], fill=WHITE) # head
    # black mask
    draw.line([9, 20, 15, 20], fill=BLACK, width=2)

# 14. Mole
def draw_mole(draw):
    # cylindrical dark grey body, pink nose/claws
    draw.ellipse([12, 16, 38, 36], fill=DKGREY)
    draw.ellipse([10, 24, 14, 28], fill=PINK) # nose
    # claws
    draw.line([(14, 32), (10, 36)], fill=WHITE, width=2)
    draw.line([(34, 32), (38, 36)], fill=WHITE, width=2)

# 15. Opossum
def draw_opossum(draw):
    # grey body, white face, pink tail
    draw.ellipse([14, 16, 38, 36], fill=GREY)
    draw.polygon([(16, 26), (8, 26), (18, 32)], fill=WHITE) # face
    draw.ellipse([8, 25, 11, 28], fill=PINK) # nose
    draw.line([(36, 28), (48, 34)], fill=PINK, width=2) # tail

# 16. Bandicoot
def draw_bandicoot(draw):
    # brown marsupial with pointed snout and stripes
    draw.ellipse([14, 16, 38, 36], fill=BROWN)
    draw.polygon([(16, 26), (8, 26), (18, 32)], fill=TAN) # face
    # stripes on back
    for x in range(28, 38, 3):
        draw.line([x, 16, x, 36], fill=WHITE, width=1)

# 17. Porcupine
def draw_porcupine(draw):
    draw.ellipse([14, 16, 38, 38], fill=DKBROWN)
    # quill spines
    for sx, sy in [(12, 12), (18, 8), (26, 8), (34, 10), (40, 16), (42, 24), (40, 32)]:
        draw.line([(25, 25), (sx, sy)], fill=WHITE, width=2)

# 18. Gopher
def draw_gopher(draw):
    # small brown rodent with buck teeth
    draw.ellipse([14, 16, 36, 38], fill=BROWN)
    draw.ellipse([21, 24, 29, 32], fill=CREAM)
    # buck teeth
    draw.rectangle([23, 31, 25, 34], fill=WHITE)
    draw.rectangle([25, 31, 27, 34], fill=WHITE)

# 19. Groundhog
def draw_groundhog(draw):
    # fat brown woodchuck
    draw.ellipse([10, 14, 40, 40], fill=DKBROWN)
    draw.ellipse([12, 16, 38, 38], fill=BROWN)
    draw.ellipse([22, 24, 28, 30], fill=BLACK)

# 20. Chipmunk
def draw_chipmunk(draw):
    # stripes on back
    draw.ellipse([14, 16, 36, 38], fill=TAN)
    # stripes
    draw.line([(20, 16), (20, 38)], fill=BLACK, width=1)
    draw.line([(22, 16), (22, 38)], fill=WHITE, width=1)
    draw.line([(24, 16), (24, 38)], fill=BLACK, width=1)

# 21. Prairie Dog
def draw_prairie_dog(draw):
    # standing tan rodent
    draw.rounded_rectangle([16, 12, 34, 44], radius=6, fill=CREAM)
    draw.rounded_rectangle([18, 14, 32, 42], radius=5, fill=TAN)
    draw.ellipse([23, 18, 27, 22], fill=BLACK)

# 22. Narwhal
def draw_narwhal(draw):
    # grey whale with long tusk
    draw.ellipse([14, 20, 42, 34], fill=GREY)
    draw.ellipse([18, 22, 38, 32], fill=WHITE)
    # tusk
    draw.line([(14, 27), (2, 27)], fill=WHITE, width=2)

# 23. Manatee
def draw_manatee(draw):
    # fat grey sea cow
    draw.ellipse([10, 14, 40, 36], fill=GREY)
    # paddle tail
    draw.ellipse([34, 20, 44, 30], fill=GREY)

# 24. Dugong
def draw_dugong(draw):
    draw.ellipse([10, 14, 40, 36], fill=GREY)
    # fluked tail (whale-like)
    draw.polygon([(36, 25), (46, 18), (44, 32)], fill=GREY)

# 25. Sea Lion
def draw_sea_lion(draw):
    # brown marine mammal with flippers
    draw.ellipse([12, 16, 38, 36], fill=BROWN)
    # front flippers
    draw.polygon([(16, 32), (10, 42), (20, 36)], fill=BROWN)
    draw.polygon([(34, 32), (40, 42), (30, 36)], fill=BROWN)

# 26. Orca (Killer Whale)
def draw_orca(draw):
    # black and white whale
    draw.ellipse([10, 16, 40, 36], fill=BLACK)
    draw.ellipse([16, 26, 34, 36], fill=WHITE) # white belly
    # eye patch
    draw.ellipse([16, 20, 20, 23], fill=WHITE)
    # dorsal fin
    draw.polygon([(25, 16), (25, 6), (32, 16)], fill=BLACK)

# 27. Beluga
def draw_beluga(draw):
    # pure white melon-headed whale
    draw.ellipse([12, 16, 38, 36], fill=WHITE)
    draw.ellipse([14, 18, 36, 34], fill=(240, 240, 240, 255))
    # melon forehead
    draw.ellipse([14, 18, 22, 26], fill=WHITE)

# 28. Manta Ray
def draw_manta_ray(draw):
    # large diamond wings
    draw.polygon([(25, 8), (4, 25), (25, 42), (46, 25)], fill=DKGREY)
    # cephalic horns
    draw.rectangle([20, 6, 22, 10], fill=BLACK)
    draw.rectangle([28, 6, 30, 10], fill=BLACK)

# 29. Stingray
def draw_stingray(draw):
    # diamond body with long tail whip
    draw.polygon([(25, 12), (8, 28), (25, 40), (42, 28)], fill=GREY)
    draw.line([(25, 40), (25, 48)], fill=DARK, width=2)

# 30. Seahorse
def draw_seahorse(draw):
    # curved body
    draw.arc([16, 12, 34, 38], 90, 270, fill=YELLOW, width=4)
    # snout
    draw.line([(18, 16), (10, 16)], fill=YELLOW, width=3)
    # tail curl
    draw.ellipse([26, 32, 34, 40], fill=YELLOW)

# 31. Jellyfish
def draw_jellyfish(draw):
    # dome cap
    draw.chord([12, 10, 38, 34], 180, 360, fill=PINK)
    draw.ellipse([12, 20, 38, 26], fill=PINK)
    # tentacles
    for tx in [16, 22, 28, 34]:
        draw.line([tx, 24, tx, 44], fill=PINK, width=1)

# 32. Starfish
def draw_starfish(draw):
    draw.polygon([(25, 8), (29, 20), (40, 20), (31, 28), (35, 40), (25, 32), (15, 40), (19, 28), (10, 20), (21, 20)], fill=ORANGE)
    draw.ellipse([23, 23, 27, 27], fill=YELLOW)

# 33. Lobster
def draw_lobster(draw):
    draw.rounded_rectangle([18, 18, 32, 40], radius=4, fill=RED)
    # claws
    draw.arc([8, 10, 22, 26], 180, 360, fill=RED, width=4)
    draw.arc([28, 10, 42, 26], 180, 360, fill=RED, width=4)
    # tail fan
    draw.polygon([(25, 40), (18, 46), (32, 46)], fill=DKRED)

# 34. Shrimp
def draw_shrimp(draw):
    # curved pink crustacean
    draw.arc([12, 12, 38, 38], 0, 180, fill=PINK, width=4)
    # antennae
    draw.line([(36, 25), (46, 20)], fill=PINK, width=1)
    draw.line([(36, 25), (46, 30)], fill=PINK, width=1)

# 35. Squid
def draw_squid(draw):
    # arrow head
    draw.polygon([(25, 8), (16, 24), (34, 24)], fill=DKRED)
    draw.rectangle([18, 24, 32, 34], fill=RED)
    # tentacles
    for tx in range(18, 34, 3):
        draw.line([tx, 34, tx-2, 46], fill=RED, width=1)

# 36. Cuttlefish
def draw_cuttlefish(draw):
    # oval body with fringe fin
    draw.ellipse([14, 14, 36, 38], fill=TAN)
    # fin edge
    draw.arc([12, 12, 38, 40], 0, 360, fill=WHITE, width=1)
    # eyes
    draw.ellipse([18, 18, 22, 22], fill=BLACK)
    draw.ellipse([28, 18, 32, 22], fill=BLACK)

# 37. Eel
def draw_eel(draw):
    # ribbon body snake-like fish
    draw.arc([10, 10, 40, 40], 40, 220, fill=DKGREEN, width=4)
    # head
    draw.ellipse([8, 22, 14, 28], fill=GREEN)

# 38. Gecko
def draw_gecko(draw):
    # small bright green lizard with pads on toes
    draw.line([(25, 10), (25, 40)], fill=GREEN, width=3)
    # feet
    for fx, fy in [(18, 16), (32, 16), (18, 32), (32, 32)]:
        draw.ellipse([fx-2, fy-2, fx+2, fy+2], fill=YELLOW)

# 39. Komodo Dragon
def draw_komodo_dragon(draw):
    # giant grey-brown lizard
    draw.ellipse([12, 18, 38, 36], fill=DKGREY)
    # long neck & head
    draw.line([(14, 26), (6, 22)], fill=DKGREY, width=5)
    # yellow tongue
    draw.line([(6, 22), (2, 22)], fill=YELLOW, width=2)

# 40. Salamander
def draw_salamander(draw):
    # black body with bright yellow spots
    draw.line([(25, 10), (25, 40)], fill=BLACK, width=4)
    # spots
    for sx, sy in [(25, 16), (25, 24), (25, 32)]:
        draw.point((sx, sy), fill=YELLOW)
        draw.point((sx+1, sy), fill=YELLOW)

# 41. Toad
def draw_toad(draw):
    # bumpy brown squat amphibian
    draw.ellipse([12, 16, 38, 38], fill=BROWN)
    # bumps
    for bx, by in [(16, 20), (32, 22), (20, 28), (30, 30)]:
        draw.ellipse([bx-1, by-1, bx+1, by+1], fill=DKBROWN)

# 42. Scorpion
def draw_scorpion(draw):
    # segmented tail curved up
    draw.rounded_rectangle([18, 20, 32, 36], radius=4, fill=DARK)
    # tail hook
    draw.arc([16, 8, 34, 24], 90, 270, fill=DARK, width=3)
    draw.ellipse([14, 8, 18, 12], fill=RED) # stinger
    # claws
    draw.line([(18, 24), (10, 18)], fill=DARK, width=2)
    draw.line([(32, 24), (40, 18)], fill=DARK, width=2)

# 43. Centipede
def draw_centipede(draw):
    # long orange segmented body with legs
    draw.line([(25, 8), (25, 42)], fill=ORANGE, width=3)
    # legs
    for y in range(12, 40, 4):
        draw.line([22, y, 28, y], fill=YELLOW, width=1)

# 44. Snail
def draw_snail(draw):
    # brown coiled shell, grey body
    draw.ellipse([14, 14, 38, 34], fill=BROWN)
    draw.arc([14, 14, 38, 34], 0, 360, fill=DKBROWN, width=2) # coil line
    # body crawling at bottom
    draw.rounded_rectangle([8, 32, 42, 38], radius=2, fill=GREY)
    # tentacles
    draw.line([(10, 32), (6, 26)], fill=GREY, width=2)

# 45. Ladybug
def draw_ladybug(draw):
    draw.ellipse([14, 14, 36, 38], fill=RED)
    draw.line([(25, 14), (25, 38)], fill=BLACK, width=2) # wings divider
    # head
    draw.ellipse([21, 10, 29, 16], fill=BLACK)
    # spots
    for sx, sy in [(18, 20), (32, 20), (18, 30), (32, 30)]:
         draw.ellipse([sx-2, sy-2, sx+2, sy+2], fill=BLACK)

# 46. Dragonfly
def draw_dragonfly(draw):
    # blue body, double wings
    draw.line([(25, 8), (25, 42)], fill=BLUE, width=2)
    # wings
    draw.ellipse([8, 16, 42, 20], fill=GLASS)
    draw.ellipse([10, 22, 40, 26], fill=GLASS)

# 47. Grasshopper
def draw_grasshopper(draw):
    # green insect with long back legs
    draw.rounded_rectangle([18, 16, 32, 38], radius=4, fill=GREEN)
    # long legs
    draw.line([(18, 28), (10, 16)], fill=DKGREEN, width=3)
    draw.line([(10, 16), (14, 42)], fill=DKGREEN, width=2)
    draw.line([(32, 28), (40, 16)], fill=DKGREEN, width=3)
    draw.line([(40, 16), (36, 42)], fill=DKGREEN, width=2)

# 48. Praying Mantis
def draw_mantis(draw):
    # green elongated head/thorax and folded front claws
    draw.line([(25, 10), (25, 38)], fill=GREEN, width=3)
    # folded claws
    draw.polygon([(25, 16), (18, 22), (25, 26)], fill=DKGREEN)
    draw.polygon([(25, 16), (32, 22), (25, 26)], fill=DKGREEN)

# 49. Beetle
def draw_beetle(draw):
    # shiny green scarab
    draw.ellipse([14, 16, 36, 40], fill=DKGREEN)
    draw.ellipse([16, 18, 34, 38], fill=GREEN)
    # head
    draw.ellipse([21, 11, 29, 17], fill=BLACK)
    # horn
    draw.line([(25, 11), (25, 6)], fill=BLACK, width=2)

# 50. Firefly
def draw_firefly(draw):
    # brown beetle, glowing yellow tail
    draw.ellipse([14, 14, 36, 32], fill=DARK)
    # head
    draw.ellipse([21, 10, 29, 15], fill=BLACK)
    # glowing tail
    draw.ellipse([20, 30, 30, 42], fill=YELLOW)
    draw.ellipse([22, 32, 28, 40], fill=WHITE)

# Build all 50 items
items = [
    ("red_panda", draw_red_panda),
    ("wombat", draw_wombat),
    ("echidna", draw_echidna),
    ("quokka", draw_quokka),
    ("tasmanian_devil", draw_tasmanian_devil),
    ("anteater", draw_anteater),
    ("pangolin", draw_pangolin),
    ("tapir", draw_tapir),
    ("okapi", draw_okapi),
    ("hyena", draw_hyena),
    ("mongoose", draw_mongoose),
    ("weasel", draw_weasel),
    ("ferret", draw_ferret),
    ("mole", draw_mole),
    ("opossum", draw_opossum),
    ("bandicoot", draw_bandicoot),
    ("porcupine", draw_porcupine),
    ("gopher", draw_gopher),
    ("groundhog", draw_groundhog),
    ("chipmunk", draw_chipmunk),
    ("prairie_dog", draw_prairie_dog),
    ("narwhal", draw_narwhal),
    ("manatee", draw_manatee),
    ("dugong", draw_dugong),
    ("sea_lion", draw_sea_lion),
    ("orca", draw_orca),
    ("beluga", draw_beluga),
    ("manta_ray", draw_manta_ray),
    ("stingray", draw_stingray),
    ("seahorse", draw_seahorse),
    ("jellyfish", draw_jellyfish),
    ("starfish", draw_starfish),
    ("lobster", draw_lobster),
    ("shrimp", draw_shrimp),
    ("squid", draw_squid),
    ("cuttlefish", draw_cuttlefish),
    ("eel", draw_eel),
    ("gecko", draw_gecko),
    ("komodo_dragon", draw_komodo_dragon),
    ("salamander", draw_salamander),
    ("toad", draw_toad),
    ("scorpion", draw_scorpion),
    ("centipede", draw_centipede),
    ("snail", draw_snail),
    ("ladybug", draw_ladybug),
    ("dragonfly", draw_dragonfly),
    ("grasshopper", draw_grasshopper),
    ("mantis", draw_mantis),
    ("beetle", draw_beetle),
    ("firefly", draw_firefly)
]

print(f"Generating {len(items)} new animal sprites in '{OUTPUT_DIR}'...")
for name, func in items:
    create_sprite(name, func)
print("\nAll 50 new animal sprites generated successfully!")
