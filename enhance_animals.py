"""
enhance_animals.py
==================
Replaces low-quality / placeholder 50x50 animal sprites with
hand-crafted pixel art, then applies clean cell-shading to ALL
50x50 animal images. Every output has ≤ 10 unique colors (including
the transparent background) and zero dithering noise, making them
suitable for a kids' pixel-coloring game.

Animals REPLACED with proper unique art:
  armadillo, camel, capybara, chameleon, chimpanzee, crow, donkey,
  emu, falcon, ferret, iguana, lemur, moose, opossum, platypus,
  red_panda, walrus, weasel, ant, spider

Animals IMPROVED (wrong emoji was used previously):
  stingray, jellyfish, seahorse, starfish, cuttlefish, eel,
  gecko, komodo_dragon, salamander, toad, dragonfly, grasshopper,
  mantis, firefly, echidna, mole, mongoose, meerkat, anteater,
  pangolin, tapir, okapi, hyena, bandicoot, gopher, groundhog,
  prairie_dog, wombat, quokka, tasmanian_devil
"""

import os
from PIL import Image, ImageDraw
import numpy as np
import glob

OUTPUT_DIR = "images/animals"

# ---------------------------------------------------------------------------
# Palette helpers
# ---------------------------------------------------------------------------
T   = (0,   0,   0,   0)    # transparent
BK  = (25,  25,  25,  255)  # black outline
WH  = (245, 245, 245, 255)  # white/near-white
LGY = (200, 200, 200, 255)  # light grey
MGY = (160, 160, 160, 255)  # mid grey
DGY = (100, 100, 100, 255)  # dark grey

BRN = (160, 105, 55, 255)   # medium brown
DBRN= (110, 65,  25, 255)   # dark brown
LBRN= (210, 170, 120, 255)  # light brown / tan
ORNG= (235, 130, 40, 255)   # orange
YELL= (240, 210, 50, 255)   # yellow
RED  = (210, 60,  50, 255)  # red
PINK = (240, 175, 175, 255) # pink
GRN  = (80,  160, 70, 255)  # green
DGRN = (50,  110, 45, 255)  # dark green
LGRN = (160, 210, 130, 255) # light green
BLU  = (70,  120, 200, 255) # blue
LBLU = (160, 210, 250, 255) # light blue
PURP = (150, 90,  200, 255) # purple
CRMS = (180, 50,  80, 255)  # crimson
GOLD = (210, 175, 55, 255)  # gold
SKIN = (230, 195, 155, 255) # skin tone


def save_sprite(name, draw_fn, quantize=True):
    """Draw, optionally cell-shade, quantize, and save a 50x50 sprite."""
    img = Image.new("RGBA", (50, 50), T)
    d   = ImageDraw.Draw(img)
    draw_fn(d)

    if quantize:
        img = _quantize(img)

    path = os.path.join(OUTPUT_DIR, f"{name}_50x50.png")
    img.save(path)


def _quantize(img: Image.Image) -> Image.Image:
    """Flatten → quantize 9 colors (no dither) → restore alpha."""
    arr   = np.array(img.convert("RGBA"))
    alpha = arr[:, :, 3]
    mask  = alpha > 128

    # Outline: any transparent pixel next to an opaque pixel gets black
    h, w = mask.shape
    outline = np.zeros((h, w), bool)
    for dy, dx in [(-1,0),(1,0),(0,-1),(0,1)]:
        shifted = np.roll(np.roll(mask, dy, 0), dx, 1)
        if dy ==  1: shifted[0,  :] = False
        if dy == -1: shifted[-1, :] = False
        if dx ==  1: shifted[:,  0] = False
        if dx == -1: shifted[:, -1] = False
        outline |= (~mask) & shifted

    rgb = arr[:, :, :3].astype(float)
    rgb[outline] = [25, 25, 25]

    new_alpha = alpha.copy()
    new_alpha[outline] = 255

    flat = Image.new("RGB", (50, 50), (255, 255, 255))
    composed = Image.fromarray(
        np.dstack((rgb, new_alpha)).astype(np.uint8), "RGBA"
    )
    flat.paste(composed, mask=Image.fromarray(new_alpha, "L"))

    q     = flat.quantize(colors=9, method=Image.MEDIANCUT, dither=0)
    final = q.convert("RGBA")
    fa    = np.array(final)
    fa[:, :, 3] = new_alpha
    return Image.fromarray(fa, "RGBA")


# ===========================================================================
# New hand-crafted sprites (replace broken / placeholder animals)
# ===========================================================================

def draw_armadillo(d):
    # grey banded shell body
    d.ellipse([16,22,36,38], fill=DGY)
    d.ellipse([18,24,34,36], fill=MGY)
    # bands
    d.line([20,24,20,36], fill=DGY, width=1)
    d.line([25,23,25,37], fill=DGY, width=1)
    d.line([30,23,30,37], fill=DGY, width=1)
    # small head
    d.ellipse([12,21,22,29], fill=LBRN)
    d.ellipse([10,24,14,28], fill=LBRN)  # snout
    d.ellipse([13,22,15,24], fill=BK)    # eye
    # legs
    for x in [16,21,26,31]:
        d.rectangle([x,36,x+2,41], fill=LBRN)
    # tail
    d.line([36,33,44,38], fill=LBRN, width=3)

def draw_camel(d):
    # body
    d.ellipse([13,26,40,42], fill=LBRN)
    # two humps
    d.ellipse([14,16,25,30], fill=LBRN)
    d.ellipse([24,14,36,28], fill=LBRN)
    # neck
    d.rectangle([12,22,18,32], fill=LBRN)
    # head
    d.ellipse([5,18,18,28],  fill=LBRN)
    d.ellipse([4,22,10,27],  fill=LBRN) # snout
    d.ellipse([7,20,9,22],   fill=BK)   # eye
    # legs
    for x in [16,22,28,34]:
        d.rectangle([x,40,x+3,48], fill=BRN)
    # tail
    d.line([40,34,46,38], fill=BRN, width=2)

def draw_capybara(d):
    # large blocky body
    d.rounded_rectangle([12,26,42,42], radius=5, fill=BRN)
    # head
    d.rounded_rectangle([8,16,28,30], radius=4, fill=BRN)
    # snout area
    d.rounded_rectangle([6,21,16,28], radius=3, fill=LBRN)
    d.ellipse([7,22,10,25],  fill=BK)  # nostril
    d.ellipse([10,22,13,25], fill=BK)
    d.ellipse([14,17,17,20], fill=BK)  # eye
    # ears
    d.ellipse([22,14,26,18], fill=BRN)
    # legs
    for x in [14,20,28,34]:
        d.rectangle([x,40,x+3,48], fill=DBRN)

def draw_chameleon(d):
    # body (oval)
    d.ellipse([18,22,42,38], fill=GRN)
    d.ellipse([20,24,40,36], fill=LGRN)  # lighter belly
    # tail curling
    d.arc([36,32,50,46], start=220, end=360, fill=GRN, width=4)
    d.arc([40,38,50,48], start=160, end=280, fill=GRN, width=3)
    # neck + head
    d.polygon([(18,26),(8,20),(12,32)], fill=GRN)
    d.ellipse([4,16,20,28], fill=GRN)
    # big eye
    d.ellipse([6,17,13,24],  fill=WH)
    d.ellipse([8,19,11,22],  fill=BK)
    # legs
    d.line([22,36,18,44], fill=DGRN, width=3)
    d.line([30,37,27,45], fill=DGRN, width=3)
    d.line([34,36,37,44], fill=DGRN, width=3)

def draw_chimpanzee(d):
    # body
    d.ellipse([14,26,38,44], fill=DBRN)
    # face disc (lighter)
    d.ellipse([14,14,36,34], fill=BRN)
    d.ellipse([16,20,34,32], fill=SKIN)  # face
    # ears
    d.ellipse([10,18,17,25], fill=BRN)
    d.ellipse([33,18,40,25], fill=BRN)
    d.ellipse([11,20,15,24], fill=PINK)
    d.ellipse([35,20,39,24], fill=PINK)
    # eyes
    d.ellipse([19,21,22,24], fill=BK)
    d.ellipse([28,21,31,24], fill=BK)
    # nose/mouth
    d.ellipse([22,26,28,30], fill=SKIN)
    d.ellipse([23,27,25,29], fill=BK)
    d.ellipse([26,27,28,29], fill=BK)
    d.arc([21,28,29,33], start=0, end=180, fill=BK, width=1)
    # arms
    d.rectangle([8,30,16,42],  fill=DBRN)
    d.rectangle([34,30,42,42], fill=DBRN)

def draw_crow(d):
    # all-black bird, side view
    d.ellipse([18,18,38,34], fill=DGY)   # body
    d.ellipse([12,14,26,26], fill=DGY)   # head
    # wing highlight
    d.ellipse([20,20,36,32], fill=BK)
    d.line([20,26,36,28], fill=DGY, width=1)  # wing feather
    # beak
    d.polygon([(12,18),(6,20),(12,22)], fill=DGY)
    # eye
    d.ellipse([14,16,17,19], fill=WH)
    d.ellipse([15,17,16,18], fill=BK)
    # tail
    d.polygon([(36,28),(46,30),(36,34)], fill=DGY)
    # legs
    d.line([26,33,24,40], fill=DGY, width=2)
    d.line([30,33,30,40], fill=DGY, width=2)
    d.line([24,40,20,42], fill=DGY, width=1)
    d.line([24,40,26,42], fill=DGY, width=1)

def draw_donkey(d):
    # grey body
    d.ellipse([14,26,42,44], fill=MGY)
    # neck + head
    d.rectangle([12,16,22,30], fill=MGY)
    d.ellipse([6,12,24,28],    fill=MGY)
    # long ears
    d.rectangle([8,6,12,18],   fill=MGY)
    d.rectangle([8,6,12,16],   fill=PINK)
    d.rectangle([14,4,18,16],  fill=MGY)
    d.rectangle([14,4,18,14],  fill=PINK)
    # face/muzzle
    d.ellipse([6,18,18,26],    fill=LBRN)
    d.ellipse([8,19,10,21],    fill=BK)  # eye
    d.ellipse([8,23,11,26],    fill=BK)  # nostril
    # legs
    for x in [16,22,30,36]:
        d.rectangle([x,42,x+3,49], fill=DGY)
    # tail
    d.line([42,34,48,38], fill=DBRN, width=2)
    d.line([48,38,46,43], fill=DBRN, width=2)

def draw_emu(d):
    # brown feathery body
    d.ellipse([16,24,42,46], fill=DBRN)
    # long neck
    d.rectangle([14,10,22,28], fill=BRN)
    # small head
    d.ellipse([10,6,24,18],    fill=BRN)
    # beak
    d.polygon([(10,10),(4,12),(10,14)], fill=DGY)
    # eye
    d.ellipse([12,8,15,11],    fill=ORNG)
    d.ellipse([13,9,14,10],    fill=BK)
    # wings (small vestigial)
    d.ellipse([12,24,20,32],   fill=BRN)
    # legs (very long)
    d.rectangle([22,44,26,50], fill=DGY)
    d.rectangle([30,44,34,50], fill=DGY)
    # feet
    d.line([22,50,18,50], fill=DGY, width=2)
    d.line([22,50,24,50], fill=DGY, width=2)
    d.line([30,50,26,50], fill=DGY, width=2)
    d.line([30,50,32,50], fill=DGY, width=2)

def draw_falcon(d):
    # brown back, white/cream chest
    d.ellipse([16,20,38,42], fill=BRN)
    d.ellipse([18,24,36,42], fill=LBRN)  # chest
    # head
    d.ellipse([14,10,34,26], fill=DBRN)
    # cheek patch
    d.rectangle([14,18,20,24], fill=DBRN)
    d.ellipse([16,11,20,15],   fill=BK)   # eye
    # hooked beak
    d.polygon([(14,16),(6,17),(10,20)],  fill=YELL)
    # wings
    d.polygon([(16,26),(6,40),(26,36)],  fill=BRN)
    d.polygon([(38,26),(46,40),(28,36)], fill=BRN)
    # tail
    d.polygon([(18,40),(32,40),(25,48)], fill=DBRN)
    # talons
    d.line([22,42,18,48], fill=YELL, width=2)
    d.line([28,42,28,48], fill=YELL, width=2)

def draw_ferret(d):
    # long thin body
    d.ellipse([10,24,44,38], fill=LBRN)
    d.ellipse([12,26,42,36], fill=WH)    # lighter belly
    # head
    d.ellipse([6,16,24,30],  fill=LBRN)
    # mask
    d.ellipse([6,18,14,26],  fill=BRN)
    d.ellipse([14,18,22,24], fill=BRN)
    # eyes
    d.ellipse([8,19,11,22],  fill=BK)
    d.ellipse([16,19,19,22], fill=BK)
    # nose
    d.ellipse([9,24,12,26],  fill=PINK)
    # ears
    d.ellipse([16,14,20,18], fill=LBRN)
    d.ellipse([22,13,26,17], fill=LBRN)
    # legs
    for x in [14,20,30,36]:
        d.rectangle([x,36,x+3,42], fill=BRN)
    # long tail
    d.line([44,32,50,28], fill=BRN, width=4)

def draw_iguana(d):
    # green scaly body
    d.ellipse([16,24,42,40], fill=GRN)
    # dorsal spines
    for x in range(18, 40, 3):
        d.polygon([(x,24),(x+1,18),(x+2,24)], fill=DGRN)
    # tail
    d.polygon([(40,30),(50,36),(40,38)], fill=GRN)
    # head
    d.polygon([(16,28),(6,22),(10,34)], fill=GRN)
    d.ellipse([4,20,18,32], fill=GRN)
    d.ellipse([5,22,12,28], fill=LGRN)  # dewlap
    # eye
    d.ellipse([6,22,9,25],  fill=YELL)
    d.ellipse([7,23,8,24],  fill=BK)
    # legs
    d.line([22,38,18,46], fill=DGRN, width=3)
    d.line([30,39,28,47], fill=DGRN, width=3)
    d.line([34,38,38,46], fill=DGRN, width=3)

def draw_lemur(d):
    # white/black ringed tail curling up
    for i in range(6):
        c = BK if i%2==0 else WH
        d.arc([32+i,8+i,50-i,30-i], start=0, end=300, fill=c, width=3)
    # grey body
    d.ellipse([10,26,36,44], fill=MGY)
    # white belly
    d.ellipse([14,30,32,42], fill=WH)
    # head
    d.ellipse([10,14,30,30], fill=MGY)
    # black eye patches
    d.ellipse([11,17,18,23], fill=BK)
    d.ellipse([22,17,29,23], fill=BK)
    # white inner
    d.ellipse([13,19,16,22], fill=WH)
    d.ellipse([24,19,27,22], fill=WH)
    d.ellipse([14,20,15,21], fill=BK)
    d.ellipse([25,20,26,21], fill=BK)
    # ears
    d.ellipse([8,12,14,18],  fill=MGY)
    d.ellipse([26,12,32,18], fill=MGY)

def draw_moose(d):
    # brown body
    d.ellipse([14,28,42,46], fill=DBRN)
    # neck
    d.rectangle([14,18,22,32], fill=DBRN)
    # head
    d.ellipse([8,14,26,28],   fill=BRN)
    # big snout/muzzle
    d.ellipse([6,20,18,30],   fill=LBRN)
    d.ellipse([7,23,10,26],   fill=BK)  # nostril
    d.ellipse([8,16,11,19],   fill=BK)  # eye
    # antlers (palmate)
    d.polygon([(14,14),(6,4),(10,14)],  fill=DBRN)
    d.line([8,6,4,10],  fill=DBRN, width=2)
    d.line([8,6,6,2],   fill=DBRN, width=2)
    d.polygon([(18,14),(26,4),(22,14)], fill=DBRN)
    d.line([24,6,28,10], fill=DBRN, width=2)
    d.line([24,6,26,2],  fill=DBRN, width=2)
    # legs
    for x in [16,22,30,36]:
        d.rectangle([x,44,x+3,50], fill=DBRN)

def draw_opossum(d):
    # grey body
    d.ellipse([14,26,40,44], fill=MGY)
    # white belly
    d.ellipse([18,30,36,42], fill=WH)
    # head (pointed)
    d.polygon([(14,30),(32,30),(24,14)], fill=WH)
    d.ellipse([12,22,32,34],            fill=WH)
    # pink nose
    d.ellipse([20,22,24,26], fill=PINK)
    # eyes
    d.ellipse([14,24,18,28], fill=BK)
    d.ellipse([26,24,30,28], fill=BK)
    # ears
    d.ellipse([10,18,17,25], fill=PINK)
    d.ellipse([27,18,34,25], fill=PINK)
    # prehensile tail (curly)
    d.arc([36,26,50,40], start=40, end=270, fill=PINK, width=3)
    # legs
    for x in [16,22,28,34]:
        d.rectangle([x,42,x+3,48], fill=MGY)

def draw_platypus(d):
    # brown body
    d.ellipse([12,24,42,40], fill=BRN)
    # tail (flat paddle)
    d.ellipse([36,34,50,44], fill=DBRN)
    # head
    d.ellipse([6,20,24,32],  fill=BRN)
    # duck bill
    d.ellipse([2,22,14,30],  fill=DGY)
    # eye
    d.ellipse([10,22,13,25], fill=BK)
    # legs
    for x in [16,22,28,34]:
        d.rectangle([x,38,x+3,44], fill=DBRN)
    # webbed feet
    d.ellipse([14,42,20,46], fill=DBRN)
    d.ellipse([26,42,32,46], fill=DBRN)

def draw_red_panda(d):
    # rusty-red body
    d.ellipse([14,26,40,44], fill=ORNG)
    # darker back
    d.ellipse([16,26,38,36], fill=RED)
    # white belly
    d.ellipse([18,34,36,44], fill=WH)
    # head
    d.ellipse([12,14,34,30], fill=ORNG)
    # white ear tips
    d.ellipse([12,12,18,18], fill=WH)
    d.ellipse([28,12,34,18], fill=WH)
    d.ellipse([13,13,17,17], fill=BRN)
    d.ellipse([29,13,33,17], fill=BRN)
    # white face markings
    d.ellipse([14,20,20,26], fill=WH)
    d.ellipse([26,20,32,26], fill=WH)
    # eyes
    d.ellipse([15,21,19,25], fill=BK)
    d.ellipse([27,21,31,25], fill=BK)
    # red eye rings
    d.ellipse([14,20,18,24], outline=RED, width=1)
    d.ellipse([28,20,32,24], outline=RED, width=1)
    # nose
    d.ellipse([21,24,25,27], fill=BK)
    # ringed tail
    for i, c in enumerate([ORNG,DBRN,ORNG,DBRN,ORNG]):
        d.arc([36,28+i*3, 50, 44+i*3], start=200, end=340, fill=c, width=3)

def draw_walrus(d):
    # large grey body
    d.ellipse([10,22,44,48], fill=MGY)
    d.ellipse([12,26,42,48], fill=LGY)  # lighter belly
    # head
    d.ellipse([10,12,36,30], fill=MGY)
    # muzzle with whisker pad
    d.ellipse([10,22,30,34], fill=LGY)
    # tusks
    d.polygon([(14,32),(10,46),(16,46)], fill=WH)
    d.polygon([(22,32),(20,46),(26,46)], fill=WH)
    # eyes
    d.ellipse([22,14,26,18], fill=BK)
    # flippers
    d.ellipse([6,36,16,48],  fill=DGY)
    d.ellipse([38,36,48,48], fill=DGY)

def draw_weasel(d):
    # long slim body
    d.ellipse([8,24,46,38],  fill=BRN)
    d.ellipse([12,26,42,36], fill=LBRN) # belly
    # head
    d.ellipse([4,18,20,30],  fill=BRN)
    # white chin
    d.ellipse([6,24,18,30],  fill=WH)
    # eyes
    d.ellipse([6,19,9,22],   fill=BK)
    d.ellipse([10,19,13,22], fill=BK)
    # nose
    d.ellipse([5,24,8,26],   fill=PINK)
    # ears
    d.ellipse([12,16,16,20], fill=BRN)
    d.ellipse([16,15,20,19], fill=BRN)
    # legs
    for x in [14,20,30,36]:
        d.rectangle([x,36,x+2,42], fill=BRN)
    # tail
    d.line([46,32,50,26], fill=DBRN, width=4)

def draw_ant(d):
    # 3-segment body
    d.ellipse([23,36,31,44], fill=BK)  # abdomen
    d.ellipse([23,28,31,37], fill=BK)  # thorax
    d.ellipse([21,20,29,30], fill=BK)  # head
    # antennae
    d.line([24,20,18,12], fill=BK, width=1)
    d.line([18,12,15,10], fill=BK, width=1)
    d.line([26,20,30,12], fill=BK, width=1)
    d.line([30,12,33,10], fill=BK, width=1)
    d.ellipse([14,9,16,11], fill=BK)
    d.ellipse([32,9,34,11], fill=BK)
    # eyes
    d.ellipse([22,22,24,24], fill=RED)
    d.ellipse([26,22,28,24], fill=RED)
    # 6 legs
    d.line([24,31,16,26], fill=BK, width=2)
    d.line([24,32,16,32], fill=BK, width=2)
    d.line([24,34,16,38], fill=BK, width=2)
    d.line([30,31,38,26], fill=BK, width=2)
    d.line([30,32,38,32], fill=BK, width=2)
    d.line([30,34,38,38], fill=BK, width=2)

def draw_spider(d):
    # dark round body (two parts)
    d.ellipse([20,28,34,42], fill=DGY)  # abdomen
    d.ellipse([22,20,32,30], fill=BK)   # cephalothorax
    # eyes (row of 4)
    for ex in [23,26,29,32]:
        d.ellipse([ex,21,ex+2,23], fill=RED)
    # 8 legs (4 per side)
    legs_l = [(20,25,10,18),(20,26,8,24),(20,28,8,30),(20,30,10,36)]
    legs_r = [(32,25,44,18),(32,26,46,24),(32,28,46,30),(32,30,44,36)]
    for x1,y1,x2,y2 in legs_l:
        d.line([x1,y1,x2,y2], fill=BK, width=2)
    for x1,y1,x2,y2 in legs_r:
        d.line([x1,y1,x2,y2], fill=BK, width=2)
    # abdomen pattern
    d.ellipse([22,31,32,40], fill=MGY)
    d.ellipse([24,33,30,38], fill=DGY)


# ---------------------------------------------------------------------------
# Improved sprites for animals that had wrong emoji previously
# ---------------------------------------------------------------------------

def draw_stingray(d):
    d.polygon([(25,12),(8,30),(25,40),(42,30)], fill=DGY)
    d.ellipse([20,22,30,32], fill=MGY)
    d.ellipse([22,24,25,27], fill=BK)  # eye
    d.line([25,40,25,50], fill=DGY, width=3)  # tail
    d.line([25,50,22,48], fill=DGY, width=1)
    d.ellipse([23,44,27,48], fill=BK)  # stinger

def draw_jellyfish(d):
    # bell
    d.ellipse([12,10,38,30], fill=(200,140,220,255))
    d.ellipse([14,12,36,28], fill=(230,190,250,255))  # highlight
    # tentacles
    for x in [14,18,22,26,30,34]:
        d.arc([x,26,x+4,46], start=0, end=180, fill=(180,100,200,255), width=2)
    # eyes
    d.ellipse([19,16,22,19], fill=BK)
    d.ellipse([28,16,31,19], fill=BK)

def draw_seahorse(d):
    # head + snout
    d.ellipse([18,8,32,22], fill=ORNG)
    d.line([18,14,10,18],   fill=ORNG, width=4)  # snout
    d.ellipse([20,10,23,13], fill=BK)             # eye
    # body curling
    d.arc([16,18,34,40], start=270, end=90,  fill=YELL, width=6)
    d.arc([20,34,38,46], start=90,  end=270, fill=ORNG, width=6)
    d.ellipse([26,44,36,50], fill=ORNG)           # tail curl
    # dorsal fin
    d.polygon([(32,12),(40,10),(34,20)], fill=YELL)

def draw_starfish(d):
    cx, cy = 25, 26
    pts = []
    import math
    for i in range(5):
        a = math.radians(i*72 - 90)
        pts.append((int(cx+18*math.cos(a)), int(cy+18*math.sin(a))))
        a2 = math.radians(i*72 + 36 - 90)
        pts.append((int(cx+8*math.cos(a2)), int(cy+8*math.sin(a2))))
    d.polygon(pts, fill=ORNG)
    d.ellipse([22,23,28,29], fill=YELL)  # center disk
    d.ellipse([23,24,27,28], fill=ORNG)

def draw_cuttlefish(d):
    d.ellipse([12,16,40,38], fill=(120,160,200,255))
    # stripes
    for y in [20,25,30]:
        d.line([14,y,38,y], fill=(80,120,180,255), width=2)
    # fins along sides
    d.ellipse([8,18,16,36],  fill=(100,140,190,255))
    d.ellipse([36,18,44,36], fill=(100,140,190,255))
    # eyes
    d.ellipse([17,20,23,26], fill=WH)
    d.ellipse([19,22,21,24], fill=BK)
    d.ellipse([29,20,35,26], fill=WH)
    d.ellipse([31,22,33,24], fill=BK)
    # tentacles
    for x in [16,20,24,28,32,36]:
        d.line([x,38,x-2,48], fill=(80,120,180,255), width=2)

def draw_eel(d):
    # wavy snake-like body
    d.arc([10,10,30,30], start=90,  end=270, fill=DGRN, width=8)
    d.arc([20,20,40,40], start=270, end=90,  fill=DGRN, width=8)
    d.arc([10,30,30,50], start=90,  end=270, fill=DGRN, width=8)
    # head
    d.ellipse([8,8,22,20], fill=GRN)
    d.ellipse([9,10,13,14], fill=BK)  # eye
    d.polygon([(8,16),(2,18),(8,20)], fill=LGRN)  # mouth

def draw_gecko(d):
    # small green lizard, top-down view
    d.ellipse([18,22,34,40], fill=LGRN)          # body
    d.ellipse([20,24,32,38], fill=GRN)
    # tail
    d.polygon([(26,40),(22,50),(30,50)], fill=LGRN)
    # head
    d.ellipse([16,14,36,26], fill=LGRN)
    d.ellipse([18,15,22,19], fill=BK)             # eye L
    d.ellipse([30,15,34,19], fill=BK)             # eye R
    # 4 legs with toe pads
    d.line([20,26,10,22], fill=GRN, width=3)
    d.line([32,26,42,22], fill=GRN, width=3)
    d.line([20,36,10,42], fill=GRN, width=3)
    d.line([32,36,42,42], fill=GRN, width=3)
    for tx,ty in [(8,20),(44,20),(8,42),(44,42)]:
        d.ellipse([tx-2,ty-2,tx+2,ty+2], fill=LGRN)

def draw_komodo_dragon(d):
    d.ellipse([14,24,44,42], fill=DGY)            # body
    d.ellipse([16,28,42,40], fill=MGY)
    # tail
    d.polygon([(42,30),(50,34),(42,38)], fill=DGY)
    # head
    d.polygon([(14,30),(4,26),(6,36)], fill=DGY)
    d.ellipse([2,24,16,36], fill=DGY)
    d.ellipse([4,27,8,31],  fill=YELL)            # eye
    d.ellipse([5,28,7,30],  fill=BK)
    # tongue
    d.line([2,31,0,29], fill=RED, width=1)
    d.line([0,29,0,27], fill=RED, width=1)
    # legs
    d.line([20,40,16,48], fill=DGY, width=3)
    d.line([28,41,26,49], fill=DGY, width=3)
    d.line([34,40,36,48], fill=DGY, width=3)

def draw_salamander(d):
    d.ellipse([16,22,38,38], fill=ORNG)           # body
    d.ellipse([18,24,36,36], fill=YELL)           # belly
    # black spots
    for x,y in [(20,24),(28,25),(24,30),(32,30),(22,33)]:
        d.ellipse([x,y,x+3,y+3], fill=BK)
    # tail
    d.polygon([(36,28),(48,24),(36,34)], fill=ORNG)
    # head
    d.ellipse([8,18,24,30], fill=ORNG)
    d.ellipse([10,20,14,24], fill=BK)             # eye
    # legs
    d.line([20,36,14,44], fill=ORNG, width=3)
    d.line([28,37,26,45], fill=ORNG, width=3)
    d.line([32,36,36,44], fill=ORNG, width=3)

def draw_toad(d):
    d.ellipse([12,22,40,42], fill=(90,130,70,255))  # body (warty green)
    d.ellipse([14,26,38,42], fill=(120,160,90,255)) # belly
    # bumps
    for x,y in [(16,24),(24,23),(32,24),(20,28),(30,28)]:
        d.ellipse([x,y,x+3,y+3], fill=(70,100,55,255))
    # head
    d.ellipse([12,14,40,28], fill=(90,130,70,255))
    # big eyes on top
    d.ellipse([13,13,21,21], fill=YELL)
    d.ellipse([31,13,39,21], fill=YELL)
    d.ellipse([15,15,19,19], fill=(50,30,20,255))
    d.ellipse([33,15,37,19], fill=(50,30,20,255))
    # mouth
    d.arc([16,22,36,32], start=0, end=180, fill=BK, width=2)
    # legs
    d.polygon([(12,36),(2,44),(14,46)],  fill=(80,120,60,255))
    d.polygon([(40,36),(50,44),(38,46)], fill=(80,120,60,255))

def draw_dragonfly(d):
    # body
    d.line([25,12,25,42], fill=(60,120,200,255), width=4)  # abdomen
    d.ellipse([22,10,28,18], fill=LGRN)                    # thorax
    # 4 wings
    d.ellipse([4,12,24,24],  fill=(200,230,255,180))
    d.ellipse([4,22,24,34],  fill=(200,230,255,180))
    d.ellipse([26,12,46,24], fill=(200,230,255,180))
    d.ellipse([26,22,46,34], fill=(200,230,255,180))
    # head + big eyes
    d.ellipse([20,6,30,14],  fill=LGRN)
    d.ellipse([18,6,24,12],  fill=BLU)   # eye L
    d.ellipse([26,6,32,12],  fill=BLU)   # eye R
    # abdo segments
    for y in range(20,42,4):
        d.line([23,y,27,y], fill=(40,80,160,255), width=1)

def draw_grasshopper(d):
    d.ellipse([18,26,40,42], fill=GRN)   # body
    d.ellipse([20,28,38,40], fill=LGRN)  # belly
    # head
    d.ellipse([8,20,24,32],  fill=GRN)
    d.ellipse([8,22,12,26],  fill=BK)    # eye
    # antennae
    d.line([14,20,6,10],  fill=DGRN, width=1)
    d.line([18,20,14,10], fill=DGRN, width=1)
    # big hind legs
    d.polygon([(22,36),(10,28),(14,42)], fill=DGRN)
    d.polygon([(36,36),(48,28),(44,42)], fill=DGRN)
    # forelegs
    d.line([20,32,12,38], fill=DGRN, width=2)
    d.line([30,32,24,38], fill=DGRN, width=2)
    d.line([32,32,40,38], fill=DGRN, width=2)
    # wings
    d.ellipse([24,22,40,36], fill=(200,240,200,160))

def draw_mantis(d):
    d.rectangle([22,22,28,42], fill=GRN)  # abdomen
    d.ellipse([20,14,30,24],   fill=LGRN) # thorax
    # raptorial forelegs
    d.polygon([(20,18),(10,10),(12,22)], fill=GRN)
    d.polygon([(30,18),(40,10),(38,22)], fill=GRN)
    d.line([10,10,6,16],  fill=DGRN, width=2)
    d.line([40,10,44,16], fill=DGRN, width=2)
    # head
    d.ellipse([19,8,31,18],  fill=GRN)
    # big compound eyes
    d.ellipse([18,8,24,14],  fill=YELL)
    d.ellipse([26,8,32,14],  fill=YELL)
    d.ellipse([19,9,23,13],  fill=BK)
    d.ellipse([27,9,31,13],  fill=BK)
    # antennae
    d.line([22,8,16,2], fill=DGRN, width=1)
    d.line([28,8,34,2], fill=DGRN, width=1)
    # wings
    d.ellipse([18,24,32,40], fill=(160,220,160,140))

def draw_firefly(d):
    d.ellipse([18,20,34,38], fill=DBRN)  # body
    d.ellipse([20,30,32,40], fill=YELL)  # glowing abdomen
    # glow effect (lighter halo)
    d.ellipse([16,28,36,44], fill=(255,255,100,60))
    d.ellipse([14,26,38,46], fill=(255,255,100,30))
    # head
    d.ellipse([18,12,32,24], fill=DBRN)
    d.ellipse([20,14,24,18], fill=BK)   # eye L
    d.ellipse([28,14,32,18], fill=BK)   # eye R
    # wings
    d.ellipse([6,18,22,34],  fill=(180,220,255,120))
    d.ellipse([30,18,46,34], fill=(180,220,255,120))
    # antennae
    d.line([22,12,16,6], fill=DBRN, width=1)
    d.line([28,12,34,6], fill=DBRN, width=1)

def draw_echidna(d):
    # dark body with spines
    d.ellipse([12,22,42,44], fill=DBRN)
    d.ellipse([14,24,40,42], fill=BRN)
    # spines (top)
    for x in range(14,42,3):
        d.polygon([(x,24),(x+1,16),(x+2,24)], fill=LGY)
    # head + long snout
    d.ellipse([6,26,24,38], fill=BRN)
    d.line([6,32,0,32],     fill=BRN, width=3)
    # eye
    d.ellipse([10,27,13,30], fill=BK)
    # legs
    for x in [16,22,28,34]:
        d.rectangle([x,42,x+2,48], fill=DBRN)

def draw_mole(d):
    d.ellipse([12,22,40,44], fill=DGY)    # body
    d.ellipse([14,26,38,42], fill=MGY)   # lighter belly
    # big digging hands
    d.ellipse([8,30,18,40],  fill=SKIN)
    d.ellipse([34,30,44,40], fill=SKIN)
    # finger lines
    for dx in [10,12,14]:
        d.line([dx,30,dx-2,26], fill=LBRN, width=1)
    for dx in [36,38,40]:
        d.line([dx,30,dx+2,26], fill=LBRN, width=1)
    # tiny head
    d.ellipse([16,18,32,30], fill=DGY)
    # pink snout
    d.ellipse([20,24,28,30], fill=PINK)
    # tiny eyes (nearly buried)
    d.ellipse([17,20,19,22], fill=BK)
    d.ellipse([29,20,31,22], fill=BK)

def draw_mongoose(d):
    d.ellipse([10,26,42,42], fill=BRN)   # body
    d.ellipse([12,28,40,40], fill=LBRN)  # belly
    # head
    d.ellipse([6,18,26,32],  fill=BRN)
    d.ellipse([6,22,16,30],  fill=LBRN)  # muzzle
    d.ellipse([8,20,11,23],  fill=BK)    # eye
    d.ellipse([8,27,11,30],  fill=BK)    # nose
    # ears
    d.ellipse([18,16,22,20], fill=BRN)
    d.ellipse([22,15,26,19], fill=BRN)
    # banded tail
    for i, c in enumerate([BRN,DBRN,BRN,DBRN,BRN]):
        d.rectangle([38+i*2, 30, 40+i*2, 38], fill=c)
    # legs
    for x in [14,20,28,34]:
        d.rectangle([x,40,x+3,46], fill=BRN)

def draw_meerkat(d):
    # upright stance
    d.ellipse([18,28,34,46], fill=LBRN)  # body
    d.ellipse([20,30,32,44], fill=YELL)  # cream belly
    # neck
    d.rectangle([21,22,31,30], fill=LBRN)
    # head
    d.ellipse([16,14,36,28],   fill=LBRN)
    # dark eye rings
    d.ellipse([17,17,23,23],   fill=DBRN)
    d.ellipse([29,17,35,23],   fill=DBRN)
    d.ellipse([18,18,22,22],   fill=WH)
    d.ellipse([30,18,34,22],   fill=WH)
    d.ellipse([19,19,21,21],   fill=BK)
    d.ellipse([31,19,33,21],   fill=BK)
    # ears
    d.ellipse([14,12,18,17],   fill=BRN)
    d.ellipse([34,12,38,17],   fill=BRN)
    # arms (held out)
    d.rectangle([12,30,20,36], fill=LBRN)
    d.rectangle([32,30,40,36], fill=LBRN)
    # legs
    d.rectangle([20,44,24,50], fill=BRN)
    d.rectangle([28,44,32,50], fill=BRN)

def draw_anteater(d):
    # elongated grey body
    d.ellipse([14,24,44,42], fill=MGY)
    d.ellipse([16,28,42,40], fill=LGY)
    # very long snout
    d.polygon([(14,30),(0,26),(0,34)], fill=MGY)
    # head
    d.ellipse([10,22,26,34], fill=MGY)
    d.ellipse([10,28,14,32], fill=BK)   # nostril
    d.ellipse([16,23,19,26], fill=BK)   # eye
    # bushy tail
    d.ellipse([40,24,50,42], fill=DGY)
    d.ellipse([42,26,50,40], fill=MGY)
    # legs
    for x in [18,24,32,38]:
        d.rectangle([x,40,x+3,47], fill=DGY)
    # claws
    for x in [18,22,32,36]:
        d.line([x,47,x-2,50], fill=BK, width=1)

def draw_pangolin(d):
    # scaled armoured body
    d.ellipse([14,22,42,42], fill=BRN)
    # scales (overlapping brown rectangles)
    for row, y in enumerate(range(24, 42, 4)):
        for col in range(5):
            x = 14 + col*6 + (row%2)*3
            d.polygon([(x,y),(x+6,y),(x+4,y+4),(x+2,y+4)], fill=DBRN)
    # head (pointed)
    d.polygon([(14,28),(4,24),(6,34)], fill=BRN)
    d.ellipse([2,22,16,32], fill=BRN)
    d.ellipse([4,24,8,28],  fill=BK)   # eye
    # curling tail
    d.arc([34,32,50,48], start=180, end=360, fill=DBRN, width=6)

def draw_tapir(d):
    # big black body
    d.ellipse([12,26,44,46], fill=BK)
    d.ellipse([14,30,42,44], fill=DGY)  # lighter mid-section
    # head with flexible snout
    d.ellipse([6,18,26,34],  fill=DGY)
    d.polygon([(6,24),(0,20),(0,30)], fill=DGY)  # snout
    d.ellipse([8,20,12,24],  fill=BK)   # eye
    # ears
    d.ellipse([16,14,22,20], fill=DGY)
    d.ellipse([22,13,28,19], fill=DGY)
    # legs
    for x in [16,22,30,36]:
        d.rectangle([x,44,x+3,50], fill=BK)

def draw_okapi(d):
    # body like a small giraffe - reddish-brown
    d.ellipse([14,28,42,46], fill=(160,80,40,255))
    # zebra stripes on rump+legs
    d.ellipse([30,32,42,46], fill=WH)
    for y in [32,36,40,44]:
        d.line([30,y,42,y], fill=BK, width=2)
    # neck
    d.rectangle([14,16,22,32], fill=(160,80,40,255))
    # head (like giraffe)
    d.ellipse([8,10,24,24],   fill=(160,80,40,255))
    # ossicones (short horns)
    d.line([16,10,14,4], fill=BRN, width=2)
    d.line([20,10,22,4], fill=BRN, width=2)
    d.ellipse([13,3,16,6], fill=BRN)
    d.ellipse([21,3,24,6], fill=BRN)
    # eye
    d.ellipse([10,13,14,17], fill=BK)
    # snout
    d.ellipse([8,18,16,24],   fill=LBRN)
    # legs
    for x in [16,22,30,36]:
        d.rectangle([x,44,x+3,50], fill=(140,70,30,255))

def draw_hyena(d):
    # spotted brown body
    d.ellipse([12,26,42,44], fill=BRN)
    d.ellipse([14,28,40,42], fill=LBRN)
    # spots
    for x,y in [(16,28),(24,27),(32,28),(20,34),(30,34),(22,40),(34,40)]:
        d.ellipse([x,y,x+3,y+3], fill=DBRN)
    # sloped back (hind lower)
    d.polygon([(30,26),(42,28),(42,36),(30,32)], fill=BRN)
    # head
    d.ellipse([6,18,28,32],  fill=BRN)
    d.ellipse([6,22,18,30],  fill=LBRN)   # muzzle
    d.ellipse([8,20,11,23],  fill=BK)     # eye
    d.ellipse([8,27,12,30],  fill=BK)     # nose
    # ears (pointed)
    d.polygon([(16,18),(12,10),(20,18)],  fill=BRN)
    d.polygon([(22,18),(18,10),(26,18)],  fill=BRN)
    # mane
    d.rectangle([20,18,30,28], fill=DBRN)
    # legs
    for x in [14,20,28,34]:
        d.rectangle([x,42,x+3,49], fill=BRN)

def draw_bandicoot(d):
    # grey-brown body
    d.ellipse([14,24,40,44], fill=BRN)
    d.ellipse([16,28,38,42], fill=LBRN)  # belly
    # long pointed head
    d.polygon([(14,30),(0,24),(4,36)],  fill=BRN)
    d.ellipse([2,22,18,34], fill=BRN)
    # long nose
    d.ellipse([2,27,8,31],  fill=PINK)
    d.ellipse([4,28,6,30],  fill=BK)    # nostril
    # eye
    d.ellipse([8,24,12,28], fill=BK)
    # big ears
    d.ellipse([12,14,20,24], fill=BRN)
    d.ellipse([18,13,26,23], fill=BRN)
    # hind legs (large)
    d.rectangle([28,40,34,50], fill=DBRN)
    d.rectangle([34,40,40,50], fill=DBRN)
    # forelegs
    d.rectangle([16,40,20,46], fill=BRN)
    # tail
    d.line([40,36,50,32], fill=DBRN, width=3)

def draw_gopher(d):
    # chubby brown body
    d.ellipse([12,24,40,46], fill=BRN)
    d.ellipse([14,28,38,44], fill=LBRN)  # belly
    # head
    d.ellipse([10,16,32,30], fill=BRN)
    # cheek pouches
    d.ellipse([6,20,16,28],  fill=LBRN)
    d.ellipse([26,20,36,28], fill=LBRN)
    # eyes
    d.ellipse([12,18,15,21], fill=BK)
    d.ellipse([22,18,25,21], fill=BK)
    # nose
    d.ellipse([17,22,21,25], fill=PINK)
    # ears (small)
    d.ellipse([20,14,24,18], fill=BRN)
    # big teeth
    d.rectangle([17,26,19,30], fill=WH)
    d.rectangle([20,26,22,30], fill=WH)
    # forelegs with claws
    d.rectangle([14,40,18,46], fill=BRN)
    d.rectangle([26,40,30,46], fill=BRN)
    d.line([14,46,12,48], fill=BK, width=1)
    d.line([16,46,14,48], fill=BK, width=1)

def draw_groundhog(d):
    # brown chunky body
    d.ellipse([12,24,40,46], fill=DBRN)
    d.ellipse([14,28,38,44], fill=BRN)
    # head
    d.ellipse([10,14,32,28], fill=DBRN)
    d.ellipse([10,20,22,28], fill=LBRN)  # face
    d.ellipse([10,22,14,26], fill=BK)    # eye
    # nose
    d.ellipse([10,24,14,27], fill=PINK)
    # ears
    d.ellipse([20,12,26,18], fill=DBRN)
    d.ellipse([26,11,32,17], fill=DBRN)
    # forelegs (upright pose)
    d.rectangle([12,34,16,44], fill=DBRN)
    d.rectangle([30,34,34,44], fill=DBRN)
    # hind legs
    d.rectangle([16,42,22,50], fill=BRN)
    d.rectangle([26,42,32,50], fill=BRN)

def draw_prairie_dog(d):
    # light brown body
    d.ellipse([14,26,38,46], fill=LBRN)
    d.ellipse([16,30,36,44], fill=(240,210,170,255))  # belly
    # head
    d.ellipse([14,14,36,28],  fill=LBRN)
    d.ellipse([16,20,24,28],  fill=(240,210,170,255)) # muzzle
    d.ellipse([16,22,20,26],  fill=BK)  # eye L
    d.ellipse([26,14,30,18],  fill=BK)  # eye R
    # nose
    d.ellipse([18,25,22,28],  fill=PINK)
    # ears
    d.ellipse([14,12,18,18],  fill=BRN)
    d.ellipse([32,12,36,18],  fill=BRN)
    # upright forelegs
    d.rectangle([12,32,16,42], fill=BRN)
    d.rectangle([36,32,40,42], fill=BRN)
    # hind legs
    d.rectangle([18,44,22,50], fill=LBRN)
    d.rectangle([30,44,34,50], fill=LBRN)
    # short tail
    d.line([36,36,42,32], fill=BRN, width=3)

def draw_wombat(d):
    # chunky grey bear-like body
    d.ellipse([10,26,42,48], fill=DGY)
    d.ellipse([12,30,40,46], fill=MGY)  # belly
    # big broad head
    d.ellipse([10,14,36,30], fill=DGY)
    d.ellipse([10,20,24,30], fill=MGY)  # face
    # small ears
    d.ellipse([12,12,18,18], fill=DGY)
    d.ellipse([28,12,34,18], fill=DGY)
    # eyes
    d.ellipse([14,18,17,21], fill=BK)
    d.ellipse([22,18,25,21], fill=BK)
    # broad flat nose
    d.ellipse([14,24,24,28], fill=BK)
    # legs (short and strong)
    for x in [12,18,28,34]:
        d.rectangle([x,46,x+4,50], fill=DBRN)

def draw_quokka(d):
    # small round happy marsupial
    d.ellipse([14,26,38,46], fill=BRN)
    d.ellipse([16,30,36,44], fill=LBRN)  # belly
    # head
    d.ellipse([14,14,36,28], fill=BRN)
    d.ellipse([16,20,24,28], fill=LBRN)  # muzzle
    # big ears
    d.ellipse([10,10,18,20], fill=BRN)
    d.ellipse([11,11,17,18], fill=PINK)
    d.ellipse([32,10,40,20], fill=BRN)
    d.ellipse([33,11,39,18], fill=PINK)
    # eyes (big + friendly)
    d.ellipse([16,16,22,22], fill=BK)
    d.ellipse([28,16,34,22], fill=BK)
    d.ellipse([17,17,19,19], fill=WH)  # glint
    d.ellipse([29,17,31,19], fill=WH)
    # smile
    d.arc([18,22,32,30], start=10, end=170, fill=BK, width=1)
    # short legs
    for x in [18,28]:
        d.rectangle([x,44,x+4,50], fill=BRN)
    # tail
    d.line([38,38,46,36], fill=BRN, width=3)

def draw_tasmanian_devil(d):
    # black stocky body
    d.ellipse([12,26,40,46], fill=BK)
    d.ellipse([14,28,38,44], fill=DGY)  # belly
    # white chest patches
    d.ellipse([18,32,30,42], fill=WH)
    # big head
    d.ellipse([10,14,36,30], fill=BK)
    d.ellipse([10,22,24,30], fill=DGY)   # muzzle
    # ears
    d.ellipse([10,10,16,18], fill=RED)
    d.ellipse([28,10,34,18], fill=RED)
    # eyes
    d.ellipse([12,16,16,20], fill=BK)
    d.ellipse([24,16,28,20], fill=BK)
    d.ellipse([13,17,15,19], fill=RED)
    d.ellipse([25,17,27,19], fill=RED)
    # angry open mouth
    d.arc([12,24,28,32], start=0, end=180, fill=RED, width=3)
    d.ellipse([14,26,18,30], fill=WH)
    d.ellipse([20,26,24,30], fill=WH)
    # legs
    for x in [14,20,28,34]:
        d.rectangle([x,44,x+3,50], fill=BK)


# ---------------------------------------------------------------------------
# Main entry point
# ---------------------------------------------------------------------------

REPLACEMENTS = {
    # Blank / identical placeholders
    "armadillo":    draw_armadillo,
    "camel":        draw_camel,
    "capybara":     draw_capybara,
    "chameleon":    draw_chameleon,
    "chimpanzee":   draw_chimpanzee,
    "crow":         draw_crow,
    "donkey":       draw_donkey,
    "emu":          draw_emu,
    "falcon":       draw_falcon,
    "ferret":       draw_ferret,
    "iguana":       draw_iguana,
    "lemur":        draw_lemur,
    "moose":        draw_moose,
    "opossum":      draw_opossum,
    "platypus":     draw_platypus,
    "red_panda":    draw_red_panda,
    "walrus":       draw_walrus,
    "weasel":       draw_weasel,
    "ant":          draw_ant,
    "spider":       draw_spider,
    # Wrong emoji used previously
    "stingray":         draw_stingray,
    "jellyfish":        draw_jellyfish,
    "seahorse":         draw_seahorse,
    "starfish":         draw_starfish,
    "cuttlefish":       draw_cuttlefish,
    "eel":              draw_eel,
    "gecko":            draw_gecko,
    "komodo_dragon":    draw_komodo_dragon,
    "salamander":       draw_salamander,
    "toad":             draw_toad,
    "dragonfly":        draw_dragonfly,
    "grasshopper":      draw_grasshopper,
    "mantis":           draw_mantis,
    "firefly":          draw_firefly,
    "echidna":          draw_echidna,
    "mole":             draw_mole,
    "mongoose":         draw_mongoose,
    "meerkat":          draw_meerkat,
    "anteater":         draw_anteater,
    "pangolin":         draw_pangolin,
    "tapir":            draw_tapir,
    "okapi":            draw_okapi,
    "hyena":            draw_hyena,
    "bandicoot":        draw_bandicoot,
    "gopher":           draw_gopher,
    "groundhog":        draw_groundhog,
    "prairie_dog":      draw_prairie_dog,
    "wombat":           draw_wombat,
    "quokka":           draw_quokka,
    "tasmanian_devil":  draw_tasmanian_devil,
}


def apply_outline_and_quantize(filepath):
    """Apply clean black outline + quantize to ≤9 colors (no dither)."""
    try:
        img = Image.open(filepath).convert("RGBA")
        img = _quantize(img)
        img.save(filepath)
    except Exception as e:
        print(f"  Error processing {filepath}: {e}")


def main():
    os.makedirs(OUTPUT_DIR, exist_ok=True)

    # 1. Redraw all replacement animals
    print("Step 1/2 — Drawing replacement sprites…")
    for name, fn in REPLACEMENTS.items():
        save_sprite(name, fn, quantize=True)
        print(f"  ✓  {name}")

    # 2. Apply outline + quantize to EVERY 50x50 animal image
    all_files = sorted(glob.glob(os.path.join(OUTPUT_DIR, "*_50x50.png")))
    print(f"\nStep 2/2 — Applying clean outline + quantize to {len(all_files)} 50×50 images…")
    for f in all_files:
        apply_outline_and_quantize(f)

    # 3. Report final color counts for new sprites
    print("\nColor count verification (replacement sprites):")
    for name in REPLACEMENTS:
        f = os.path.join(OUTPUT_DIR, f"{name}_50x50.png")
        img = Image.open(f).convert("RGBA")
        arr = np.array(img)
        mask = arr[:, :, 3] > 128
        colors = set(map(tuple, arr[mask][:, :3]))
        print(f"  {name:25s}: {len(colors):2d} colors")

    print("\nDone — all 50×50 animal sprites enhanced. ≤ 10 colors each.")


if __name__ == "__main__":
    main()
