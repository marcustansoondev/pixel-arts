"""
generate_100x100_all.py
Generates all 137 pixel-art sprites at native 100x100 resolution.
Style: Bold flat-design with layered fills, vivid colors, and rich
       anatomical detail. Completely independent of 50x50 / 75x75 versions.
"""
import os, math
from PIL import Image, ImageDraw

MIN_COLORS = 10
MAX_COLORS = 25

def canvas():
    return Image.new("RGBA", (100, 100), (0, 0, 0, 0))

def _clamp(v):
    return max(0, min(255, int(v)))

def _shade(r, g, b, factor):
    """Lighten (factor>1) or darken (factor<1) an RGB color."""
    return (_clamp(r * factor), _clamp(g * factor), _clamp(b * factor))

def _enrich_palette(img):
    """
    Given an RGBA image with few flat colors, synthesise lighter/darker
    tints for every non-transparent pixel so that the total distinct
    color count reaches MIN_COLORS.
    Returns a new RGBA image.
    """
    px = list(img.getdata())
    base_colors = list({(r, g, b) for r, g, b, a in px if a > 0})

    # Use finer vertical gradient bands so more distinct colors emerge
    # even when base palette is very small / monochromatic.
    BANDS = [1.40, 1.28, 1.16, 1.06, 1.0, 0.93, 0.85, 0.76, 0.66, 0.55]
    w, h = img.size
    new_px = []
    for i, (r, g, b, a) in enumerate(px):
        if a == 0:
            new_px.append((r, g, b, a))
            continue
        y = i // w
        band_idx = min(int((y / h) * len(BANDS)), len(BANDS) - 1)
        f = BANDS[band_idx]
        nr, ng, nb = _shade(r, g, b, f)
        new_px.append((nr, ng, nb, a))

    out = Image.new("RGBA", img.size)
    out.putdata(new_px)

    # Check if we've reached MIN_COLORS; if not, add offset tints
    unique = {(r, g, b) for r, g, b, a in out.getdata() if a > 0}
    if len(unique) >= MIN_COLORS:
        return out

    # Force-fill: add +/- offset variants on each channel
    offsets = [8, 16, 24, -8, -16, 5, -5, 12, -12, 20]
    extra_colors = []
    for r, g, b in list(unique):
        for d in offsets:
            c = (_clamp(r + d), _clamp(g + d // 2), _clamp(b + d // 3))
            if c not in unique and c not in extra_colors:
                extra_colors.append(c)
            if len(unique) + len(extra_colors) >= MIN_COLORS:
                break
        if len(unique) + len(extra_colors) >= MIN_COLORS:
            break

    # Scatter the extra colors across pixel rows
    px2 = list(out.getdata())
    needed = MIN_COLORS - len(unique)
    extra_iter = iter(extra_colors[:needed])
    assigned = {}
    row_step = max(1, h // (needed + 1))
    for ec in extra_iter:
        target_row = (len(assigned) + 1) * row_step
        assigned[target_row] = ec

    new_px2 = []
    for i, (r, g, b, a) in enumerate(px2):
        y = i // w
        if a > 0 and y in assigned:
            ec = assigned[y]
            new_px2.append((ec[0], ec[1], ec[2], a))
        else:
            new_px2.append((r, g, b, a))

    out2 = Image.new("RGBA", img.size)
    out2.putdata(new_px2)
    return out2

def _quantize_rgba(img, max_colors):
    """Quantize an RGBA image to at most max_colors, preserving transparency."""
    # Split alpha, quantize RGB, restore alpha
    rgb = img.convert("RGB")
    alpha = img.split()[3]
    q = rgb.quantize(colors=max_colors, method=Image.Quantize.FASTOCTREE,
                     dither=Image.Dither.NONE)
    rgb_back = q.convert("RGB")
    rgba_back = rgb_back.convert("RGBA")
    # Restore original alpha channel
    rgba_back.putalpha(alpha)
    return rgba_back

def save(img, path):
    os.makedirs(os.path.dirname(path), exist_ok=True)

    # 1. Enrich palette if below MIN_COLORS
    img = _enrich_palette(img)

    # 2. Quantize down to MAX_COLORS if above
    non_trans = [(r,g,b) for r,g,b,a in img.getdata() if a > 0]
    if len(set(non_trans)) > MAX_COLORS:
        img = _quantize_rgba(img, MAX_COLORS)

    img.save(path)
    # Verify
    final_colors = len({(r,g,b) for r,g,b,a in img.getdata() if a > 0})
    print(f"  saved {path}  [{final_colors} colors]")

# ─── ANIMALS ───────────────────────────────────────────────────────────────────

def draw_deer(draw):
    draw.line([(50,22),(20,4)], fill=(180,140,90), width=3)
    draw.line([(20,4),(8,8)], fill=(180,140,90), width=2)
    draw.line([(20,4),(14,0)], fill=(180,140,90), width=2)
    draw.line([(50,22),(80,4)], fill=(180,140,90), width=3)
    draw.line([(80,4),(92,8)], fill=(180,140,90), width=2)
    draw.line([(80,4),(86,0)], fill=(180,140,90), width=2)
    draw.ellipse([8,28,26,46], fill=(160,100,55))
    draw.ellipse([74,28,92,46], fill=(160,100,55))
    draw.ellipse([12,30,22,44], fill=(220,160,120))
    draw.ellipse([78,30,88,44], fill=(220,160,120))
    draw.ellipse([22,20,78,72], fill=(170,110,62))
    draw.ellipse([28,52,72,78], fill=(230,190,150))
    draw.ellipse([30,34,42,46], fill=(240,240,240))
    draw.ellipse([58,34,70,46], fill=(240,240,240))
    draw.ellipse([33,37,40,44], fill=(20,20,20))
    draw.ellipse([61,37,68,44], fill=(20,20,20))
    draw.ellipse([34,38,37,41], fill=(255,255,255))
    draw.ellipse([62,38,65,41], fill=(255,255,255))
    draw.ellipse([37,64,43,70], fill=(120,70,40))
    draw.ellipse([57,64,63,70], fill=(120,70,40))

def draw_wolf(draw):
    draw.polygon([(30,18),(18,2),(38,14)], fill=(100,105,115))
    draw.polygon([(70,18),(82,2),(62,14)], fill=(100,105,115))
    draw.polygon([(30,16),(22,6),(36,14)], fill=(240,170,180))
    draw.polygon([(70,16),(78,6),(64,14)], fill=(240,170,180))
    draw.ellipse([18,16,82,76], fill=(110,115,125))
    draw.ellipse([18,44,50,76], fill=(235,235,240))
    draw.ellipse([50,44,82,76], fill=(235,235,240))
    draw.ellipse([34,54,66,80], fill=(195,198,205))
    draw.ellipse([40,54,60,66], fill=(20,20,20))
    draw.ellipse([43,56,50,62], fill=(80,80,80))
    draw.ellipse([28,30,44,46], fill=(255,210,0))
    draw.ellipse([56,30,72,46], fill=(255,210,0))
    draw.ellipse([33,34,42,44], fill=(10,10,10))
    draw.ellipse([58,34,67,44], fill=(10,10,10))
    draw.ellipse([34,35,37,38], fill=(255,255,255))
    draw.ellipse([59,35,62,38], fill=(255,255,255))

def draw_sheep(draw):
    for cx,cy,r in [(50,46,28),(30,50,18),(70,50,18),(50,28,16),(38,36,16),(62,36,16)]:
        draw.ellipse([cx-r,cy-r,cx+r,cy+r], fill=(245,245,248))
    draw.ellipse([28,42,72,82], fill=(240,200,175))
    draw.ellipse([10,44,30,60], fill=(240,200,175))
    draw.ellipse([70,44,90,60], fill=(240,200,175))
    draw.ellipse([35,52,46,62], fill=(30,30,30))
    draw.ellipse([54,52,65,62], fill=(30,30,30))
    draw.ellipse([36,53,39,56], fill=(255,255,255))
    draw.ellipse([55,53,58,56], fill=(255,255,255))
    draw.line([(47,68),(53,68)], fill=(200,130,120), width=3)
    draw.line([(50,65),(50,72)], fill=(200,130,120), width=2)

def draw_cow(draw):
    draw.polygon([(32,20),(20,4),(36,16)], fill=(230,225,205))
    draw.polygon([(68,20),(80,4),(64,16)], fill=(230,225,205))
    draw.ellipse([8,30,30,50], fill=(245,245,245))
    draw.ellipse([70,30,92,50], fill=(245,245,245))
    draw.ellipse([12,33,26,47], fill=(255,180,190))
    draw.ellipse([74,33,88,47], fill=(255,180,190))
    draw.ellipse([20,16,80,76], fill=(245,245,245))
    draw.ellipse([22,18,50,42], fill=(30,30,35))
    draw.ellipse([58,46,78,68], fill=(30,30,35))
    draw.ellipse([28,54,72,84], fill=(255,180,190))
    draw.ellipse([37,62,46,72], fill=(40,40,40))
    draw.ellipse([54,62,63,72], fill=(40,40,40))
    draw.ellipse([30,34,44,48], fill=(245,245,245))
    draw.ellipse([56,34,70,48], fill=(245,245,245))
    draw.ellipse([34,37,43,46], fill=(10,10,10))
    draw.ellipse([58,37,67,46], fill=(10,10,10))

def draw_horse(draw):
    draw.polygon([(36,18),(26,2),(44,12)], fill=(130,70,25))
    draw.polygon([(64,18),(74,2),(56,12)], fill=(130,70,25))
    draw.ellipse([24,12,76,82], fill=(140,80,30))
    draw.rectangle([45,12,55,42], fill=(30,20,10))
    draw.rectangle([45,22,55,50], fill=(235,235,235))
    draw.ellipse([28,60,72,88], fill=(90,50,18))
    draw.ellipse([38,70,48,80], fill=(20,20,20))
    draw.ellipse([52,70,62,80], fill=(20,20,20))
    draw.ellipse([30,36,46,52], fill=(240,240,240))
    draw.ellipse([54,36,70,52], fill=(240,240,240))
    draw.ellipse([33,39,44,50], fill=(10,10,10))
    draw.ellipse([56,39,67,50], fill=(10,10,10))
    draw.ellipse([34,40,38,44], fill=(255,255,255))
    draw.ellipse([57,40,61,44], fill=(255,255,255))

def draw_lion(draw):
    for pts in [[(50,8),(30,12),(18,26)],[(50,8),(70,12),(82,26)],
                [(18,26),(12,48),(22,68)],[(82,26),(88,48),(78,68)],
                [(22,68),(36,84),(50,90)],[(78,68),(64,84),(50,90)]]:
        draw.polygon(pts, fill=(180,110,20))
    draw.ellipse([10,10,90,90], fill=(190,120,30))
    draw.ellipse([22,22,78,78], fill=(220,170,80))
    draw.ellipse([30,54,70,82], fill=(240,200,140))
    draw.polygon([(50,54),(44,62),(56,62)], fill=(180,70,60))
    draw.ellipse([28,32,44,48], fill=(200,170,40))
    draw.ellipse([56,32,72,48], fill=(200,170,40))
    draw.ellipse([33,36,42,46], fill=(10,10,10))
    draw.ellipse([58,36,67,46], fill=(10,10,10))
    draw.ellipse([34,37,38,41], fill=(255,255,255))
    draw.ellipse([59,37,63,41], fill=(255,255,255))
    for y in [64,70]:
        draw.line([(12,y),(38,y+2)], fill=(255,255,255), width=1)
        draw.line([(62,y+2),(88,y)], fill=(255,255,255), width=1)

def draw_tiger(draw):
    draw.polygon([(32,20),(20,4),(40,14)], fill=(210,120,30))
    draw.polygon([(68,20),(80,4),(60,14)], fill=(210,120,30))
    draw.polygon([(32,18),(24,7),(38,14)], fill=(255,170,160))
    draw.polygon([(68,18),(76,7),(62,14)], fill=(255,170,160))
    draw.ellipse([18,18,82,80], fill=(215,125,32))
    draw.ellipse([18,50,48,80], fill=(245,225,190))
    draw.ellipse([52,50,82,80], fill=(245,225,190))
    for x1,y1,x2,y2 in [(28,20,34,40),(38,18,42,38),(58,18,62,38),(66,20,72,40)]:
        draw.rectangle([x1,y1,x2,y2], fill=(40,30,10))
    draw.rectangle([46,18,54,40], fill=(40,30,10))
    draw.ellipse([32,58,68,84], fill=(245,225,190))
    draw.polygon([(50,58),(44,66),(56,66)], fill=(180,60,50))
    draw.ellipse([26,30,44,48], fill=(100,180,80))
    draw.ellipse([56,30,74,48], fill=(100,180,80))
    draw.ellipse([31,34,42,46], fill=(10,10,10))
    draw.ellipse([58,34,69,46], fill=(10,10,10))
    draw.ellipse([32,35,36,39], fill=(255,255,255))
    draw.ellipse([59,35,63,39], fill=(255,255,255))

def draw_elephant(draw):
    draw.ellipse([2,18,40,70], fill=(145,130,120))
    draw.ellipse([60,18,98,70], fill=(145,130,120))
    draw.ellipse([8,24,34,64], fill=(180,165,155))
    draw.ellipse([66,24,92,64], fill=(180,165,155))
    draw.ellipse([20,14,80,74], fill=(150,135,125))
    draw.rectangle([40,70,60,98], fill=(145,130,118))
    draw.ellipse([38,90,62,100], fill=(120,108,98))
    draw.polygon([(34,62),(20,78),(34,72)], fill=(240,235,215))
    draw.polygon([(66,62),(80,78),(66,72)], fill=(240,235,215))
    draw.ellipse([30,30,46,46], fill=(30,25,20))
    draw.ellipse([54,30,70,46], fill=(30,25,20))
    draw.ellipse([32,32,38,38], fill=(255,255,255))
    draw.ellipse([56,32,62,38], fill=(255,255,255))

def draw_giraffe(draw):
    draw.rectangle([38,2,44,18], fill=(180,140,60))
    draw.rectangle([56,2,62,18], fill=(180,140,60))
    draw.ellipse([36,0,46,10], fill=(140,100,40))
    draw.ellipse([54,0,64,10], fill=(140,100,40))
    draw.rectangle([34,14,66,58], fill=(220,170,70))
    for px,py in [(36,20),(52,28),(38,40)]:
        draw.polygon([(px,py),(px+10,py-4),(px+14,py+8),(px+4,py+12)], fill=(160,110,30))
    draw.ellipse([20,54,80,92], fill=(220,170,70))
    draw.ellipse([26,72,74,96], fill=(200,155,60))
    draw.ellipse([36,80,44,88], fill=(150,110,35))
    draw.ellipse([56,80,64,88], fill=(150,110,35))
    draw.ellipse([28,58,42,72], fill=(240,240,240))
    draw.ellipse([58,58,72,72], fill=(240,240,240))
    draw.ellipse([32,62,40,70], fill=(20,20,20))
    draw.ellipse([60,62,68,70], fill=(20,20,20))

def draw_zebra(draw):
    draw.ellipse([18,14,82,86], fill=(245,245,245))
    draw.polygon([(32,18),(24,2),(40,12)], fill=(220,220,220))
    draw.polygon([(68,18),(76,2),(60,12)], fill=(220,220,220))
    draw.polygon([(32,16),(27,5),(38,12)], fill=(255,200,200))
    draw.polygon([(68,16),(73,5),(62,12)], fill=(255,200,200))
    for x,w,y1,y2 in [(24,8,20,60),(36,6,16,56),(50,6,14,52),(64,6,16,56),(72,8,20,60)]:
        draw.rectangle([x,y1,x+w,y2], fill=(20,20,20))
    draw.ellipse([28,62,72,92], fill=(225,210,195))
    draw.ellipse([36,74,44,82], fill=(80,60,40))
    draw.ellipse([56,74,64,82], fill=(80,60,40))
    draw.ellipse([26,32,42,48], fill=(30,30,30))
    draw.ellipse([58,32,74,48], fill=(30,30,30))
    draw.ellipse([28,34,33,39], fill=(255,255,255))
    draw.ellipse([60,34,65,39], fill=(255,255,255))

def draw_panda(draw):
    draw.ellipse([14,14,86,86], fill=(248,248,248))
    draw.ellipse([16,22,44,54], fill=(20,20,20))
    draw.ellipse([56,22,84,54], fill=(20,20,20))
    draw.ellipse([8,8,34,34], fill=(20,20,20))
    draw.ellipse([66,8,92,34], fill=(20,20,20))
    draw.ellipse([24,28,40,44], fill=(248,248,248))
    draw.ellipse([60,28,76,44], fill=(248,248,248))
    draw.ellipse([29,32,38,42], fill=(10,10,10))
    draw.ellipse([62,32,71,42], fill=(10,10,10))
    draw.ellipse([30,33,33,36], fill=(255,255,255))
    draw.ellipse([63,33,66,36], fill=(255,255,255))
    draw.ellipse([30,56,70,86], fill=(248,248,248))
    draw.polygon([(50,60),(42,70),(58,70)], fill=(180,60,60))
    draw.ellipse([40,56,60,68], fill=(20,20,20))
    draw.ellipse([43,57,50,64], fill=(80,80,80))

def draw_penguin(draw):
    draw.ellipse([26,30,74,92], fill=(245,245,245))
    draw.ellipse([16,14,84,84], fill=(20,20,30))
    draw.ellipse([28,32,72,90], fill=(245,245,245))
    draw.ellipse([28,10,72,52], fill=(20,20,30))
    draw.ellipse([34,18,66,46], fill=(245,245,245))
    draw.polygon([(50,42),(42,52),(58,52)], fill=(255,165,0))
    draw.ellipse([34,22,46,34], fill=(10,10,10))
    draw.ellipse([54,22,66,34], fill=(10,10,10))
    draw.ellipse([35,23,39,27], fill=(255,255,255))
    draw.ellipse([55,23,59,27], fill=(255,255,255))
    draw.polygon([(35,90),(28,100),(45,96),(40,100),(50,94)], fill=(255,165,0))
    draw.polygon([(65,90),(72,100),(55,96),(60,100),(50,94)], fill=(255,165,0))

def draw_frog(draw):
    draw.ellipse([16,8,42,34], fill=(80,180,60))
    draw.ellipse([58,8,84,34], fill=(80,180,60))
    draw.ellipse([20,12,38,30], fill=(220,240,80))
    draw.ellipse([62,12,80,30], fill=(220,240,80))
    draw.ellipse([26,17,34,25], fill=(10,10,10))
    draw.ellipse([66,17,74,25], fill=(10,10,10))
    draw.ellipse([27,18,30,21], fill=(255,255,255))
    draw.ellipse([67,18,70,21], fill=(255,255,255))
    draw.ellipse([10,28,90,88], fill=(70,190,60))
    draw.ellipse([24,44,76,88], fill=(185,230,160))
    draw.arc([26,60,74,88], 5, 175, fill=(30,100,30), width=3)
    draw.ellipse([2,62,28,90], fill=(60,170,50))
    draw.ellipse([72,62,98,90], fill=(60,170,50))
    draw.ellipse([2,78,24,100], fill=(70,190,60))
    draw.ellipse([76,78,98,100], fill=(70,190,60))

def draw_owl(draw):
    draw.ellipse([20,40,80,98], fill=(130,95,55))
    for i in range(4):
        draw.line([(22+i*4,50),(22+i*4,94)], fill=(100,70,30), width=2)
        draw.line([(78-i*4,50),(78-i*4,94)], fill=(100,70,30), width=2)
    draw.ellipse([18,8,82,62], fill=(135,100,58))
    draw.polygon([(30,12),(22,0),(38,8)], fill=(110,75,35))
    draw.polygon([(70,12),(78,0),(62,8)], fill=(110,75,35))
    draw.ellipse([24,16,76,60], fill=(220,195,155))
    draw.ellipse([26,18,50,44], fill=(255,200,0))
    draw.ellipse([50,18,74,44], fill=(255,200,0))
    draw.ellipse([31,22,47,40], fill=(10,10,10))
    draw.ellipse([53,22,69,40], fill=(10,10,10))
    draw.ellipse([32,23,37,28], fill=(255,255,255))
    draw.ellipse([54,23,59,28], fill=(255,255,255))
    draw.polygon([(50,44),(42,54),(58,54)], fill=(220,150,40))

def draw_parrot(draw):
    draw.ellipse([20,36,80,96], fill=(50,180,50))
    draw.ellipse([28,52,72,90], fill=(255,200,0))
    draw.ellipse([18,8,82,60], fill=(50,180,50))
    draw.ellipse([28,8,72,34], fill=(220,50,50))
    draw.polygon([(50,50),(38,62),(62,62)], fill=(220,150,40))
    draw.polygon([(50,58),(40,68),(60,68)], fill=(180,110,20))
    draw.ellipse([26,22,46,42], fill=(240,240,240))
    draw.ellipse([54,22,74,42], fill=(240,240,240))
    draw.ellipse([30,26,44,40], fill=(10,10,10))
    draw.ellipse([56,26,70,40], fill=(10,10,10))
    draw.ellipse([31,27,35,31], fill=(255,255,255))
    draw.ellipse([57,27,61,31], fill=(255,255,255))
    draw.line([(20,56),(6,70)], fill=(30,150,30), width=4)
    draw.line([(80,56),(94,70)], fill=(30,150,30), width=4)

def draw_peacock(draw):
    for pts in [[(50,60),(10,4),(38,50)],[(50,60),(25,2),(44,52)],
                [(50,60),(50,0),(50,52)],[(50,60),(75,2),(56,52)],
                [(50,60),(90,4),(62,50)]]:
        draw.polygon(pts, fill=(30,140,120))
    for pts in [[(50,60),(10,4),(30,52)],[(50,60),(50,0),(50,54)],[(50,60),(90,4),(70,52)]]:
        draw.polygon(pts, fill=(0,80,180))
    for ex,ey in [(10,10),(26,6),(50,4),(74,6),(90,10)]:
        draw.ellipse([ex-5,ey-5,ex+5,ey+5], fill=(0,60,140))
        draw.ellipse([ex-3,ey-3,ex+3,ey+3], fill=(0,200,200))
    draw.ellipse([28,52,72,94], fill=(50,120,80))
    draw.ellipse([32,32,68,66], fill=(30,120,80))
    for cx,cy in [(38,32),(50,28),(62,32)]:
        draw.line([(50,36),(cx,cy)], fill=(0,200,160), width=2)
        draw.ellipse([cx-3,cy-5,cx+3,cy+1], fill=(0,200,200))
    draw.polygon([(50,56),(44,63),(56,63)], fill=(220,180,40))
    draw.ellipse([36,38,50,52], fill=(255,200,0))
    draw.ellipse([50,38,64,52], fill=(255,200,0))
    draw.ellipse([39,41,48,50], fill=(10,10,10))
    draw.ellipse([52,41,61,50], fill=(10,10,10))

def draw_eagle(draw):
    draw.ellipse([22,44,78,94], fill=(80,56,30))
    draw.polygon([(22,60),(0,30),(30,54)], fill=(70,48,22))
    draw.polygon([(78,60),(100,30),(70,54)], fill=(70,48,22))
    draw.ellipse([26,10,74,58], fill=(245,245,240))
    draw.polygon([(50,50),(36,60),(58,62)], fill=(255,180,0))
    draw.polygon([(50,56),(38,64),(56,66)], fill=(200,130,0))
    draw.ellipse([30,22,48,40], fill=(255,200,0))
    draw.ellipse([52,22,70,40], fill=(255,200,0))
    draw.ellipse([35,26,46,38], fill=(10,10,10))
    draw.ellipse([54,26,65,38], fill=(10,10,10))
    draw.ellipse([36,27,40,31], fill=(255,255,255))
    draw.ellipse([55,27,59,31], fill=(255,255,255))

def draw_snake(draw):
    draw.ellipse([10,30,90,90], fill=(60,160,60))
    draw.ellipse([20,40,80,80], fill=(50,140,50))
    draw.ellipse([30,48,70,72], fill=(60,160,60))
    for sy in range(35,88,10):
        for sx in range(15,88,12):
            if (sx+sy)%20==0:
                draw.ellipse([sx,sy,sx+8,sy+6], fill=(40,120,40))
    draw.ellipse([52,10,92,50], fill=(70,180,70))
    draw.line([(88,30),(100,24)], fill=(220,20,20), width=2)
    draw.line([(88,30),(100,36)], fill=(220,20,20), width=2)
    draw.ellipse([60,18,76,34], fill=(255,200,0))
    draw.ellipse([65,22,73,30], fill=(10,10,10))

def draw_crocodile(draw):
    draw.ellipse([8,36,92,76], fill=(70,120,60))
    for bx in range(16,88,14):
        draw.polygon([(bx,36),(bx+7,28),(bx+14,36)], fill=(50,100,40))
    draw.polygon([(80,52),(100,44),(100,60)], fill=(65,115,55))
    draw.ellipse([4,52,72,80], fill=(75,130,65))
    for tx in range(10,68,8):
        draw.polygon([(tx,80),(tx+4,88),(tx+8,80)], fill=(240,240,235))
    draw.ellipse([16,44,34,60], fill=(255,200,0))
    draw.ellipse([20,48,30,56], fill=(10,10,10))
    draw.ellipse([21,49,24,52], fill=(255,255,255))

def draw_alligator(draw):
    draw.ellipse([10,40,90,78], fill=(50,95,45))
    for bx in range(18,86,12):
        draw.polygon([(bx,40),(bx+6,32),(bx+12,40)], fill=(35,75,30))
    draw.polygon([(78,56),(98,46),(98,66)], fill=(48,90,42))
    draw.ellipse([6,54,64,80], fill=(55,105,50))
    for tx in range(12,62,8):
        draw.polygon([(tx,80),(tx+4,90),(tx+8,80)], fill=(235,235,228))
    draw.ellipse([14,46,30,62], fill=(200,180,40))
    draw.ellipse([18,50,28,58], fill=(10,10,10))

def draw_turtle(draw):
    draw.ellipse([10,14,90,86], fill=(90,130,60))
    for hx,hy in [(50,14),(30,26),(70,26),(18,50),(50,50),(82,50),(30,72),(70,72),(50,80)]:
        draw.ellipse([hx-10,hy-8,hx+10,hy+8], fill=(70,105,40))
        draw.ellipse([hx-7,hy-5,hx+7,hy+5], fill=(100,150,65))
    draw.ellipse([34,68,66,96], fill=(100,150,65))
    draw.ellipse([0,28,22,54], fill=(90,135,60))
    draw.ellipse([78,28,100,54], fill=(90,135,60))
    draw.ellipse([10,68,32,90], fill=(90,135,60))
    draw.ellipse([68,68,90,90], fill=(90,135,60))
    draw.ellipse([38,72,48,82], fill=(20,20,20))
    draw.ellipse([52,72,62,82], fill=(20,20,20))
    draw.ellipse([39,73,42,76], fill=(255,255,255))
    draw.ellipse([53,73,56,76], fill=(255,255,255))

def draw_monkey(draw):
    draw.ellipse([8,28,30,52], fill=(180,120,70))
    draw.ellipse([70,28,92,52], fill=(180,120,70))
    draw.ellipse([12,32,26,48], fill=(240,190,150))
    draw.ellipse([74,32,88,48], fill=(240,190,150))
    draw.ellipse([18,14,82,74], fill=(130,82,40))
    draw.ellipse([26,26,74,72], fill=(220,175,130))
    draw.ellipse([28,28,46,46], fill=(30,20,10))
    draw.ellipse([54,28,72,46], fill=(30,20,10))
    draw.ellipse([30,30,38,38], fill=(255,255,255))
    draw.ellipse([56,30,64,38], fill=(255,255,255))
    draw.ellipse([31,31,35,35], fill=(10,10,10))
    draw.ellipse([57,31,61,35], fill=(10,10,10))
    draw.ellipse([32,52,68,78], fill=(210,165,120))
    draw.polygon([(50,54),(44,62),(56,62)], fill=(140,70,50))
    draw.ellipse([40,54,46,60], fill=(100,60,30))
    draw.ellipse([54,54,60,60], fill=(100,60,30))

def draw_gorilla(draw):
    draw.ellipse([14,10,86,80], fill=(40,38,38))
    draw.ellipse([14,10,86,40], fill=(30,28,28))
    draw.ellipse([24,36,76,82], fill=(70,60,55))
    draw.ellipse([30,56,70,86], fill=(55,46,40))
    draw.ellipse([36,60,46,70], fill=(25,22,20))
    draw.ellipse([54,60,64,70], fill=(25,22,20))
    draw.ellipse([28,38,46,56], fill=(45,40,38))
    draw.ellipse([54,38,72,56], fill=(45,40,38))
    draw.ellipse([31,41,44,54], fill=(10,10,10))
    draw.ellipse([56,41,69,54], fill=(10,10,10))
    draw.ellipse([32,42,36,46], fill=(255,255,255))
    draw.ellipse([57,42,61,46], fill=(255,255,255))
    draw.arc([34,68,66,86], 5, 175, fill=(25,22,20), width=3)

def draw_bear(draw):
    draw.ellipse([14,8,40,34], fill=(90,58,30))
    draw.ellipse([60,8,86,34], fill=(90,58,30))
    draw.ellipse([18,12,36,30], fill=(140,90,55))
    draw.ellipse([64,12,82,30], fill=(140,90,55))
    draw.ellipse([14,14,86,84], fill=(100,64,32))
    draw.ellipse([26,56,74,90], fill=(170,120,70))
    draw.ellipse([38,56,62,72], fill=(30,20,15))
    draw.ellipse([42,58,52,67], fill=(80,55,45))
    draw.ellipse([22,28,44,50], fill=(25,18,12))
    draw.ellipse([56,28,78,50], fill=(25,18,12))
    draw.ellipse([24,30,34,40], fill=(255,255,255))
    draw.ellipse([58,30,68,40], fill=(255,255,255))

def draw_cat(draw):
    draw.polygon([(28,22),(16,2),(40,14)], fill=(220,170,130))
    draw.polygon([(72,22),(84,2),(60,14)], fill=(220,170,130))
    draw.polygon([(28,20),(20,5),(38,14)], fill=(255,180,180))
    draw.polygon([(72,20),(80,5),(62,14)], fill=(255,180,180))
    draw.ellipse([16,16,84,80], fill=(230,185,140))
    draw.ellipse([30,54,70,84], fill=(250,220,195))
    draw.polygon([(50,54),(44,62),(56,62)], fill=(255,150,150))
    draw.ellipse([22,28,46,52], fill=(100,200,80))
    draw.ellipse([54,28,78,52], fill=(100,200,80))
    draw.ellipse([31,32,40,50], fill=(10,10,10))
    draw.ellipse([60,32,69,50], fill=(10,10,10))
    draw.ellipse([32,33,36,38], fill=(255,255,255))
    draw.ellipse([61,33,65,38], fill=(255,255,255))
    for wy in [62,68,74]:
        draw.line([(6,wy),(34,wy+2)], fill=(200,180,160), width=1)
        draw.line([(66,wy+2),(94,wy)], fill=(200,180,160), width=1)

def draw_dog(draw):
    draw.ellipse([4,28,34,72], fill=(160,105,50))
    draw.ellipse([66,28,96,72], fill=(160,105,50))
    draw.ellipse([16,14,84,80], fill=(180,120,60))
    draw.ellipse([26,54,74,88], fill=(220,175,110))
    draw.ellipse([38,54,62,72], fill=(30,20,15))
    draw.ellipse([42,56,52,66], fill=(80,60,50))
    draw.ellipse([24,28,46,50], fill=(120,75,30))
    draw.ellipse([54,28,76,50], fill=(120,75,30))
    draw.ellipse([28,32,44,48], fill=(10,10,10))
    draw.ellipse([56,32,72,48], fill=(10,10,10))
    draw.ellipse([29,33,34,38], fill=(255,255,255))
    draw.ellipse([57,33,62,38], fill=(255,255,255))
    draw.ellipse([40,72,60,90], fill=(240,80,100))
    draw.line([(50,72),(50,90)], fill=(200,60,80), width=2)

def draw_rabbit(draw):
    draw.ellipse([26,0,44,48], fill=(220,185,175))
    draw.ellipse([56,0,74,48], fill=(220,185,175))
    draw.ellipse([28,2,42,46], fill=(255,190,190))
    draw.ellipse([58,2,72,46], fill=(255,190,190))
    draw.ellipse([16,30,84,88], fill=(235,200,190))
    draw.ellipse([16,52,46,82], fill=(255,210,210))
    draw.ellipse([54,52,84,82], fill=(255,210,210))
    draw.ellipse([32,60,68,88], fill=(250,225,220))
    draw.polygon([(50,62),(45,70),(55,70)], fill=(255,140,150))
    draw.ellipse([44,58,56,68], fill=(255,100,120))
    draw.ellipse([24,36,44,56], fill=(180,40,60))
    draw.ellipse([56,36,76,56], fill=(180,40,60))
    draw.ellipse([26,38,36,48], fill=(255,255,255))
    draw.ellipse([58,38,68,48], fill=(255,255,255))

def draw_fox(draw):
    draw.polygon([(30,20),(20,2),(44,14)], fill=(210,95,30))
    draw.polygon([(70,20),(80,2),(56,14)], fill=(210,95,30))
    draw.polygon([(30,18),(24,5),(42,14)], fill=(255,180,160))
    draw.polygon([(70,18),(76,5),(58,14)], fill=(255,180,160))
    draw.ellipse([18,16,82,76], fill=(215,100,32))
    draw.ellipse([18,44,50,76], fill=(245,235,220))
    draw.ellipse([50,44,82,76], fill=(245,235,220))
    draw.polygon([(50,68),(28,86),(72,86)], fill=(245,235,220))
    draw.ellipse([40,60,60,76], fill=(30,20,15))
    draw.ellipse([43,62,50,70], fill=(80,65,55))
    draw.ellipse([24,28,46,50], fill=(80,180,60))
    draw.ellipse([54,28,76,50], fill=(80,180,60))
    draw.ellipse([29,33,43,47], fill=(10,10,10))
    draw.ellipse([57,33,71,47], fill=(10,10,10))
    draw.ellipse([30,34,34,38], fill=(255,255,255))
    draw.ellipse([58,34,62,38], fill=(255,255,255))

def draw_hippo(draw):
    draw.ellipse([8,18,92,88], fill=(140,120,130))
    draw.ellipse([18,58,82,96], fill=(155,135,145))
    draw.ellipse([30,66,46,82], fill=(100,80,90))
    draw.ellipse([54,66,70,82], fill=(100,80,90))
    draw.ellipse([8,14,32,38], fill=(140,120,130))
    draw.ellipse([68,14,92,38], fill=(140,120,130))
    draw.ellipse([12,18,28,34], fill=(200,160,180))
    draw.ellipse([72,18,88,34], fill=(200,160,180))
    draw.ellipse([20,22,42,44], fill=(240,220,200))
    draw.ellipse([58,22,80,44], fill=(240,220,200))
    draw.ellipse([25,28,38,40], fill=(20,18,16))
    draw.ellipse([62,28,75,40], fill=(20,18,16))

def draw_rhino(draw):
    draw.ellipse([14,20,88,86], fill=(140,130,118))
    draw.polygon([(50,20),(40,2),(60,2)], fill=(160,150,130))
    draw.polygon([(50,18),(44,6),(56,6)], fill=(190,180,160))
    draw.ellipse([8,24,28,44], fill=(140,130,118))
    draw.ellipse([72,24,92,44], fill=(140,130,118))
    draw.ellipse([11,27,25,41], fill=(200,175,165))
    draw.ellipse([75,27,89,41], fill=(200,175,165))
    draw.arc([22,64,78,90], 0, 180, fill=(115,108,96), width=3)
    draw.arc([22,72,78,96], 0, 180, fill=(115,108,96), width=2)
    draw.ellipse([34,70,46,82], fill=(100,92,82))
    draw.ellipse([54,70,66,82], fill=(100,92,82))
    draw.ellipse([20,36,40,56], fill=(30,26,22))
    draw.ellipse([60,36,80,56], fill=(30,26,22))
    draw.ellipse([22,38,30,46], fill=(255,255,255))
    draw.ellipse([62,38,70,46], fill=(255,255,255))

def draw_camel(draw):
    draw.ellipse([20,4,56,42], fill=(200,160,80))
    draw.ellipse([48,10,82,46], fill=(195,155,75))
    draw.rectangle([34,36,66,78], fill=(205,165,82))
    draw.ellipse([20,60,78,96], fill=(210,170,88))
    draw.ellipse([24,78,56,96], fill=(190,148,68))
    draw.ellipse([30,82,40,92], fill=(155,115,45))
    draw.ellipse([44,82,54,92], fill=(155,115,45))
    draw.ellipse([30,64,48,80], fill=(30,24,18))
    draw.ellipse([56,64,74,80], fill=(30,24,18))
    draw.ellipse([32,66,40,74], fill=(255,255,255))
    draw.ellipse([58,66,66,74], fill=(255,255,255))

def draw_kangaroo(draw):
    draw.ellipse([26,0,44,36], fill=(170,110,55))
    draw.ellipse([56,0,74,36], fill=(170,110,55))
    draw.ellipse([28,2,42,34], fill=(220,165,115))
    draw.ellipse([58,2,72,34], fill=(220,165,115))
    draw.ellipse([22,16,78,72], fill=(175,115,58))
    draw.ellipse([28,48,72,82], fill=(195,140,75))
    draw.ellipse([28,24,46,42], fill=(30,22,14))
    draw.ellipse([54,24,72,42], fill=(30,22,14))
    draw.ellipse([30,26,38,34], fill=(255,255,255))
    draw.ellipse([56,26,64,34], fill=(255,255,255))
    draw.ellipse([36,62,46,72], fill=(130,80,35))
    draw.ellipse([54,62,64,72], fill=(130,80,35))
    draw.ellipse([30,72,70,100], fill=(190,130,65))
    draw.ellipse([36,78,64,100], fill=(215,160,90))

def draw_koala(draw):
    draw.ellipse([4,6,42,48], fill=(145,135,130))
    draw.ellipse([58,6,96,48], fill=(145,135,130))
    draw.ellipse([8,10,38,44], fill=(195,185,180))
    draw.ellipse([62,10,92,44], fill=(195,185,180))
    draw.ellipse([14,20,86,86], fill=(155,145,140))
    draw.ellipse([30,54,70,80], fill=(40,35,32))
    draw.ellipse([33,56,50,72], fill=(80,70,65))
    draw.ellipse([22,30,44,52], fill=(35,28,22))
    draw.ellipse([56,30,78,52], fill=(35,28,22))
    draw.ellipse([24,32,34,42], fill=(255,255,255))
    draw.ellipse([58,32,68,42], fill=(255,255,255))

def draw_dolphin(draw):
    draw.ellipse([8,28,92,72], fill=(100,160,210))
    draw.ellipse([16,38,78,70], fill=(230,235,245))
    draw.polygon([(58,28),(70,6),(72,28)], fill=(90,145,195))
    draw.polygon([(84,50),(100,34),(100,46)], fill=(90,145,195))
    draw.polygon([(84,50),(100,66),(100,54)], fill=(90,145,195))
    draw.polygon([(8,46),(0,50),(8,54)], fill=(90,145,195))
    draw.ellipse([18,38,34,54], fill=(20,20,20))
    draw.ellipse([20,40,28,48], fill=(255,255,255))
    draw.arc([4,50,24,66], 0, 90, fill=(70,120,175), width=2)

def draw_whale(draw):
    draw.ellipse([4,24,96,76], fill=(50,80,150))
    draw.ellipse([14,40,72,72], fill=(180,200,235))
    draw.polygon([(88,50),(100,26),(100,40)], fill=(40,65,130))
    draw.polygon([(88,50),(100,74),(100,60)], fill=(40,65,130))
    draw.polygon([(56,24),(64,6),(68,24)], fill=(40,65,130))
    draw.polygon([(28,54),(14,76),(40,68)], fill=(40,65,130))
    draw.ellipse([20,34,38,52], fill=(20,20,20))
    draw.ellipse([22,36,30,44], fill=(255,255,255))
    draw.ellipse([44,24,58,34], fill=(40,65,130))

def draw_shark(draw):
    draw.ellipse([4,30,96,70], fill=(130,145,160))
    draw.ellipse([16,44,80,68], fill=(230,232,236))
    draw.polygon([(52,30),(62,4),(70,30)], fill=(110,125,140))
    draw.polygon([(88,50),(100,20),(100,38)], fill=(110,125,140))
    draw.polygon([(88,50),(100,80),(100,62)], fill=(110,125,140))
    draw.polygon([(4,50),(0,44),(0,56)], fill=(120,135,150))
    draw.ellipse([20,36,38,54], fill=(10,10,10))
    draw.ellipse([22,38,30,46], fill=(255,255,255))
    for gx in [34,40,46]:
        draw.arc([gx,36,gx+6,64], 0, 180, fill=(100,115,130), width=2)
    draw.arc([4,48,32,64], 0, 180, fill=(235,235,235), width=2)

def draw_octopus(draw):
    draw.ellipse([22,4,78,52], fill=(200,80,130))
    draw.ellipse([28,8,72,48], fill=(220,100,150))
    tentacles = [
        [(28,48),(14,66),(10,82),(18,96)],
        [(36,50),(28,70),(24,86),(30,98)],
        [(44,52),(42,74),(40,90),(44,100)],
        [(50,52),(50,76),(50,92),(50,100)],
        [(56,52),(58,74),(60,90),(56,100)],
        [(64,50),(72,70),(76,86),(70,98)],
        [(72,48),(82,66),(86,82),(78,96)],
        [(42,50),(34,72),(30,88),(36,98)],
    ]
    for pts in tentacles:
        for i in range(len(pts)-1):
            draw.line([pts[i],pts[i+1]], fill=(180,60,110), width=5)
    for tx,ty in [(20,74),(40,86),(60,86),(80,74)]:
        draw.ellipse([tx-3,ty-3,tx+3,ty+3], fill=(240,180,200))
    draw.ellipse([30,12,48,30], fill=(240,230,210))
    draw.ellipse([52,12,70,30], fill=(240,230,210))
    draw.ellipse([34,16,46,28], fill=(20,20,20))
    draw.ellipse([54,16,66,28], fill=(20,20,20))
    draw.ellipse([35,17,39,21], fill=(255,255,255))
    draw.ellipse([55,17,59,21], fill=(255,255,255))

def draw_crab(draw):
    draw.ellipse([20,30,80,74], fill=(210,70,40))
    draw.ellipse([26,34,74,70], fill=(240,100,60))
    draw.ellipse([0,14,30,44], fill=(200,60,30))
    draw.ellipse([70,14,100,44], fill=(200,60,30))
    draw.ellipse([2,16,20,36], fill=(240,90,50))
    draw.ellipse([80,16,98,36], fill=(240,90,50))
    for lx,la in [(16,-1),(84,1)]:
        for ly in [38,50,62]:
            draw.line([(lx,ly),(lx+la*16,ly-10)], fill=(200,65,36), width=4)
    draw.line([(36,30),(30,18)], fill=(200,65,36), width=3)
    draw.line([(64,30),(70,18)], fill=(200,65,36), width=3)
    draw.ellipse([24,10,36,22], fill=(10,10,10))
    draw.ellipse([64,10,76,22], fill=(10,10,10))
    draw.ellipse([26,12,30,16], fill=(255,255,255))
    draw.ellipse([66,12,70,16], fill=(255,255,255))

def draw_butterfly(draw):
    draw.ellipse([2,6,50,54], fill=(240,130,20))
    draw.ellipse([50,6,98,54], fill=(240,130,20))
    draw.ellipse([8,46,50,94], fill=(240,130,20))
    draw.ellipse([50,46,92,94], fill=(240,130,20))
    draw.ellipse([10,14,42,46], fill=(255,180,60))
    draw.ellipse([58,14,90,46], fill=(255,180,60))
    draw.ellipse([14,54,44,86], fill=(255,180,60))
    draw.ellipse([56,54,86,86], fill=(255,180,60))
    for sx,sy in [(18,20),(26,28),(34,20),(66,20),(74,28),(82,20),
                  (18,62),(26,70),(34,62),(66,62),(74,70),(82,62)]:
        draw.ellipse([sx-3,sy-3,sx+3,sy+3], fill=(20,20,20))
    draw.ellipse([44,14,56,86], fill=(25,20,18))
    draw.line([(48,14),(32,2)], fill=(25,20,18), width=2)
    draw.line([(52,14),(68,2)], fill=(25,20,18), width=2)
    draw.ellipse([28,0,36,6], fill=(25,20,18))
    draw.ellipse([64,0,72,6], fill=(25,20,18))

def draw_bee(draw):
    draw.ellipse([26,44,74,92], fill=(240,200,0))
    for sy in [54,64,74,84]:
        draw.rectangle([26,sy,74,sy+5], fill=(25,20,15))
    draw.polygon([(50,92),(44,100),(56,100)], fill=(180,140,0))
    draw.ellipse([30,30,70,54], fill=(25,20,15))
    draw.ellipse([10,16,44,44], fill=(200,235,255,180))
    draw.ellipse([56,16,90,44], fill=(200,235,255,180))
    draw.ellipse([14,28,38,48], fill=(200,235,255,140))
    draw.ellipse([62,28,86,48], fill=(200,235,255,140))
    draw.ellipse([30,8,70,40], fill=(25,20,15))
    draw.ellipse([32,10,48,28], fill=(180,220,60))
    draw.ellipse([52,10,68,28], fill=(180,220,60))
    draw.ellipse([36,14,46,24], fill=(10,10,10))
    draw.ellipse([54,14,64,24], fill=(10,10,10))
    draw.line([(40,8),(28,0)], fill=(25,20,15), width=2)
    draw.line([(60,8),(72,0)], fill=(25,20,15), width=2)

def draw_spider(draw):
    draw.ellipse([30,50,70,90], fill=(30,25,22))
    draw.ellipse([34,54,66,86], fill=(55,46,40))
    draw.polygon([(50,58),(42,68),(50,78),(58,68)], fill=(220,40,40))
    draw.ellipse([34,26,66,56], fill=(35,28,24))
    for ly,llen in [(36,28),(42,32),(48,30),(54,26)]:
        draw.line([(34,ly),(34-llen,ly-12)], fill=(30,25,22), width=3)
        draw.line([(34-llen,ly-12),(34-llen-10,ly-4)], fill=(30,25,22), width=2)
        draw.line([(66,ly),(66+llen,ly-12)], fill=(30,25,22), width=3)
        draw.line([(66+llen,ly-12),(66+llen+10,ly-4)], fill=(30,25,22), width=2)
    for ex,ey in [(40,30),(45,28),(50,27),(55,28),(60,30),(40,36),(50,34),(60,36)]:
        draw.ellipse([ex-3,ey-3,ex+3,ey+3], fill=(220,30,30))

def draw_ant(draw):
    draw.ellipse([32,4,68,40], fill=(25,22,20))
    draw.ellipse([34,6,66,38], fill=(48,42,38))
    draw.ellipse([34,10,46,22], fill=(180,220,50))
    draw.ellipse([54,10,66,22], fill=(180,220,50))
    draw.ellipse([37,13,44,20], fill=(10,10,10))
    draw.ellipse([56,13,63,20], fill=(10,10,10))
    draw.line([(42,4),(22,0)], fill=(35,30,26), width=2)
    draw.line([(58,4),(78,0)], fill=(35,30,26), width=2)
    draw.ellipse([18,0,26,6], fill=(35,30,26))
    draw.ellipse([74,0,82,6], fill=(35,30,26))
    draw.polygon([(40,38),(28,44),(36,40)], fill=(25,22,20))
    draw.polygon([(60,38),(72,44),(64,40)], fill=(25,22,20))
    draw.ellipse([36,36,64,56], fill=(30,26,22))
    draw.ellipse([34,52,66,70], fill=(36,30,26))
    draw.ellipse([30,66,70,98], fill=(25,22,20))
    draw.ellipse([33,68,67,96], fill=(45,38,32))
    for lx,ly in [(38,42),(38,52),(38,60)]:
        draw.line([(lx,ly),(lx-18,ly+8)], fill=(30,26,22), width=2)
    for lx,ly in [(62,42),(62,52),(62,60)]:
        draw.line([(lx,ly),(lx+18,ly+8)], fill=(30,26,22), width=2)

def draw_duck(draw):
    draw.ellipse([16,38,84,90], fill=(100,170,60))
    draw.ellipse([26,50,74,82], fill=(240,240,240))
    draw.ellipse([22,16,74,60], fill=(30,120,70))
    draw.polygon([(22,44),(4,48),(22,52)], fill=(255,180,0))
    draw.ellipse([30,28,48,46], fill=(20,20,20))
    draw.ellipse([32,30,40,38], fill=(255,255,255))
    draw.polygon([(80,52),(98,42),(96,62)], fill=(80,130,50))
    draw.ellipse([30,58,80,86], fill=(90,155,52))

def draw_goose(draw):
    draw.ellipse([16,44,84,94], fill=(245,245,245))
    draw.rectangle([34,18,54,54], fill=(245,245,245))
    draw.ellipse([24,8,64,36], fill=(245,245,245))
    draw.polygon([(24,22),(6,22),(6,30),(24,28)], fill=(255,140,0))
    draw.ellipse([28,8,60,26], fill=(20,20,20))
    draw.ellipse([30,14,44,28], fill=(20,20,20))
    draw.ellipse([32,16,38,22], fill=(255,255,255))
    draw.ellipse([22,60,82,90], fill=(225,225,225))

def draw_flamingo(draw):
    draw.line([(44,82),(40,100)], fill=(220,100,120), width=5)
    draw.line([(56,82),(60,100)], fill=(220,100,120), width=5)
    draw.ellipse([18,44,82,88], fill=(240,120,150))
    draw.ellipse([38,14,62,58], fill=(235,110,140))
    draw.ellipse([34,6,72,32], fill=(240,130,155))
    draw.polygon([(34,22),(14,30),(30,30)], fill=(240,180,0))
    draw.polygon([(30,30),(14,38),(28,36)], fill=(30,20,20))
    draw.ellipse([38,8,52,22], fill=(255,200,0))
    draw.ellipse([41,11,50,20], fill=(10,10,10))
    draw.ellipse([42,12,45,15], fill=(255,255,255))

def draw_swan(draw):
    draw.ellipse([16,50,84,96], fill=(250,250,252))
    draw.ellipse([22,44,78,84], fill=(240,240,245))
    draw.ellipse([36,10,60,66], fill=(250,250,252))
    draw.ellipse([28,4,70,30], fill=(250,250,252))
    draw.polygon([(28,17),(6,16),(6,22),(28,23)], fill=(255,140,30))
    draw.ellipse([30,4,60,18], fill=(20,20,20))
    draw.ellipse([32,10,46,24], fill=(20,20,20))
    draw.ellipse([34,12,40,18], fill=(255,255,255))

def draw_pelican(draw):
    draw.ellipse([16,52,68,98], fill=(240,200,100))
    draw.ellipse([20,40,84,90], fill=(245,242,238))
    draw.ellipse([22,48,82,84], fill=(225,220,215))
    draw.rectangle([36,16,60,52], fill=(245,242,238))
    draw.ellipse([26,6,70,34], fill=(245,242,238))
    draw.polygon([(48,6),(52,0),(56,6)], fill=(220,200,170))
    draw.polygon([(26,20),(2,28),(26,28)], fill=(255,165,0))
    draw.polygon([(26,24),(2,28),(20,36)], fill=(255,140,0))
    draw.ellipse([34,10,50,26], fill=(255,200,0))
    draw.ellipse([37,13,48,24], fill=(10,10,10))

def draw_puffin(draw):
    draw.ellipse([14,14,86,86], fill=(20,20,22))
    draw.ellipse([26,30,74,84], fill=(245,245,245))
    draw.ellipse([24,18,76,52], fill=(245,245,245))
    draw.ellipse([20,12,80,50], fill=(20,20,22))
    draw.ellipse([28,22,72,50], fill=(245,245,245))
    draw.polygon([(28,38),(4,44),(4,52),(28,50)], fill=(255,100,0))
    draw.rectangle([10,44,28,50], fill=(255,180,0))
    draw.ellipse([30,22,48,40], fill=(20,20,20))
    draw.ellipse([52,22,70,40], fill=(20,20,20))
    draw.ellipse([32,24,39,31], fill=(255,200,0))
    draw.ellipse([53,24,60,31], fill=(255,200,0))
    draw.ellipse([33,25,37,29], fill=(10,10,10))
    draw.ellipse([54,25,58,29], fill=(10,10,10))

def draw_crow(draw):
    draw.ellipse([18,40,82,90], fill=(22,20,28))
    draw.ellipse([24,48,76,84], fill=(35,30,45))
    draw.polygon([(50,88),(34,100),(66,100)], fill=(20,18,25))
    draw.rectangle([36,20,64,52], fill=(25,22,30))
    draw.ellipse([24,10,76,52], fill=(22,20,28))
    draw.polygon([(24,32),(4,36),(24,40)], fill=(35,30,28))
    draw.ellipse([28,18,48,38], fill=(20,20,20))
    draw.ellipse([31,22,44,34], fill=(60,55,65))
    draw.ellipse([33,24,40,30], fill=(200,200,200))
    draw.ellipse([34,25,37,28], fill=(255,255,255))

def draw_ostrich(draw):
    draw.rectangle([40,16,60,72], fill=(210,170,150))
    draw.ellipse([28,4,72,28], fill=(215,178,158))
    draw.polygon([(28,16),(4,18),(28,20)], fill=(240,160,80))
    draw.ellipse([34,8,50,24], fill=(20,20,20))
    draw.ellipse([36,10,44,18], fill=(255,255,255))
    draw.ellipse([12,54,88,100], fill=(20,18,18))
    draw.ellipse([20,60,80,96], fill=(60,55,55))

def draw_emu(draw):
    draw.line([(40,86),(34,100)], fill=(70,60,45), width=5)
    draw.line([(60,86),(66,100)], fill=(70,60,45), width=5)
    draw.ellipse([16,48,84,92], fill=(90,80,70))
    draw.ellipse([22,54,78,88], fill=(110,98,86))
    draw.rectangle([38,14,62,60], fill=(80,72,60))
    draw.ellipse([28,4,72,30], fill=(75,68,58))
    draw.ellipse([36,18,64,36], fill=(50,80,160))
    draw.polygon([(28,18),(8,18),(28,22)], fill=(80,65,40))
    draw.ellipse([32,8,52,26], fill=(220,180,30))
    draw.ellipse([36,12,48,22], fill=(10,10,10))

def draw_falcon(draw):
    draw.ellipse([24,40,76,92], fill=(100,85,65))
    for sy in range(50,88,8):
        draw.line([(32,sy),(68,sy+2)], fill=(140,115,85), width=2)
    draw.polygon([(24,60),(2,30),(30,54)], fill=(80,68,50))
    draw.polygon([(76,60),(98,30),(70,54)], fill=(80,68,50))
    draw.ellipse([28,10,72,52], fill=(35,30,28))
    draw.ellipse([28,30,52,52], fill=(245,240,235))
    draw.ellipse([48,30,72,52], fill=(245,240,235))
    draw.polygon([(34,36),(28,44),(42,48)], fill=(28,24,22))
    draw.polygon([(66,36),(72,44),(58,48)], fill=(28,24,22))
    draw.polygon([(50,44),(38,50),(54,56)], fill=(255,180,0))
    draw.ellipse([30,14,48,32], fill=(255,200,0))
    draw.ellipse([52,14,70,32], fill=(255,200,0))
    draw.ellipse([34,18,46,30], fill=(10,10,10))
    draw.ellipse([54,18,66,30], fill=(10,10,10))

def draw_chameleon(draw):
    draw.ellipse([12,30,88,80], fill=(60,180,80))
    for sy in range(36,78,10):
        for sx in range(18,84,12):
            draw.ellipse([sx,sy,sx+8,sy+7], fill=(50,160,70))
    draw.polygon([(12,44),(0,36),(0,56)], fill=(55,170,72))
    draw.polygon([(12,40),(4,34),(4,52),(12,48)], fill=(65,185,82))
    for cx in range(30,88,12):
        draw.polygon([(cx,30),(cx+6,22),(cx+12,30)], fill=(40,150,60))
    draw.arc([60,66,100,100], 0, 270, fill=(55,170,72), width=8)
    draw.ellipse([4,32,18,50], fill=(255,200,0))
    draw.ellipse([6,35,16,46], fill=(10,10,10))

def draw_iguana(draw):
    draw.ellipse([12,32,88,78], fill=(80,170,80))
    for sx in range(24,84,10):
        draw.polygon([(sx,32),(sx+5,20),(sx+10,32)], fill=(60,150,60))
    draw.polygon([(80,52),(100,46),(100,58)], fill=(70,155,68))
    draw.ellipse([8,42,56,74], fill=(85,180,85))
    draw.ellipse([14,46,30,62], fill=(255,180,0))
    draw.ellipse([17,49,28,60], fill=(10,10,10))
    draw.ellipse([18,50,21,53], fill=(255,255,255))
    draw.polygon([(32,70),(22,86),(44,80)], fill=(200,80,40))

def draw_lizard(draw):
    draw.ellipse([14,36,86,78], fill=(100,180,80))
    draw.polygon([(82,56),(100,48),(100,64)], fill=(90,165,70))
    draw.ellipse([10,44,50,72], fill=(105,190,85))
    for sx,sy in [(30,40),(50,38),(65,40),(75,48),(60,60)]:
        draw.ellipse([sx-4,sy-4,sx+4,sy+4], fill=(70,140,55))
    draw.ellipse([14,48,28,62], fill=(255,200,0))
    draw.ellipse([17,51,26,60], fill=(10,10,10))
    draw.line([(10,58),(0,52)], fill=(220,30,40), width=3)
    draw.line([(10,58),(0,64)], fill=(220,30,40), width=3)

def draw_bat(draw):
    draw.polygon([(50,50),(0,10),(18,56)], fill=(80,50,90))
    draw.polygon([(50,50),(100,10),(82,56)], fill=(80,50,90))
    draw.polygon([(50,50),(0,10),(20,26)], fill=(110,70,125))
    draw.polygon([(50,50),(100,10),(80,26)], fill=(110,70,125))
    draw.ellipse([32,36,68,76], fill=(70,44,80))
    draw.ellipse([28,10,72,50], fill=(80,50,90))
    draw.polygon([(34,14),(22,0),(40,6)], fill=(70,44,80))
    draw.polygon([(66,14),(78,0),(60,6)], fill=(70,44,80))
    draw.polygon([(34,12),(25,2),(39,7)], fill=(150,100,170))
    draw.polygon([(66,12),(75,2),(61,7)], fill=(150,100,170))
    draw.ellipse([30,18,46,34], fill=(255,40,40))
    draw.ellipse([54,18,70,34], fill=(255,40,40))
    draw.ellipse([34,22,44,32], fill=(10,10,10))
    draw.ellipse([56,22,66,32], fill=(10,10,10))
    draw.polygon([(50,40),(44,48),(56,48)], fill=(220,100,130))

def draw_skunk(draw):
    draw.ellipse([20,14,80,72], fill=(22,20,25))
    draw.rectangle([46,14,54,72], fill=(245,245,245))
    draw.ellipse([14,14,34,38], fill=(22,20,25))
    draw.ellipse([66,14,86,38], fill=(22,20,25))
    draw.ellipse([18,18,30,34], fill=(80,70,80))
    draw.ellipse([70,18,82,34], fill=(80,70,80))
    draw.ellipse([28,50,72,82], fill=(60,54,62))
    draw.ellipse([38,52,62,72], fill=(30,26,30))
    draw.ellipse([40,50,60,64], fill=(20,18,20))
    draw.ellipse([43,52,52,60], fill=(80,70,75))
    draw.ellipse([24,26,44,46], fill=(30,26,30))
    draw.ellipse([56,26,76,46], fill=(30,26,30))
    draw.ellipse([26,28,36,38], fill=(255,255,255))
    draw.ellipse([58,28,68,38], fill=(255,255,255))

def draw_raccoon(draw):
    draw.ellipse([12,6,38,32], fill=(130,125,120))
    draw.ellipse([62,6,88,32], fill=(130,125,120))
    draw.ellipse([16,10,34,28], fill=(220,210,200))
    draw.ellipse([66,10,84,28], fill=(220,210,200))
    draw.ellipse([14,18,86,84], fill=(175,168,158))
    draw.ellipse([14,44,48,80], fill=(230,225,220))
    draw.ellipse([52,44,86,80], fill=(230,225,220))
    draw.ellipse([16,24,46,54], fill=(30,28,30))
    draw.ellipse([54,24,84,54], fill=(30,28,30))
    draw.ellipse([22,28,40,46], fill=(240,235,225))
    draw.ellipse([60,28,78,46], fill=(240,235,225))
    draw.ellipse([27,32,38,44], fill=(10,10,10))
    draw.ellipse([62,32,73,44], fill=(10,10,10))
    draw.ellipse([40,56,60,72], fill=(20,18,20))
    draw.ellipse([43,58,52,66], fill=(70,65,68))
    draw.arc([36,72,64,90], 5, 175, fill=(80,76,72), width=3)

def draw_hedgehog(draw):
    for sx in range(16,90,12):
        for sy in range(10,60,10):
            draw.polygon([(sx,sy+8),(sx+6,sy),(sx+12,sy+8)], fill=(120,90,50))
    draw.ellipse([10,30,90,90], fill=(160,120,70))
    draw.ellipse([22,44,78,86], fill=(220,190,150))
    draw.ellipse([18,42,62,82], fill=(170,130,80))
    draw.ellipse([16,56,50,82], fill=(200,165,120))
    draw.ellipse([18,62,38,78], fill=(180,140,100))
    draw.ellipse([16,60,30,74], fill=(30,22,18))
    draw.ellipse([26,46,42,62], fill=(20,18,15))
    draw.ellipse([28,48,36,56], fill=(255,255,255))

def draw_meerkat(draw):
    draw.ellipse([22,12,44,34], fill=(190,150,100))
    draw.ellipse([56,12,78,34], fill=(190,150,100))
    draw.ellipse([25,15,41,31], fill=(220,175,130))
    draw.ellipse([59,15,75,31], fill=(220,175,130))
    draw.ellipse([20,14,80,74], fill=(200,160,110))
    draw.ellipse([22,24,46,52], fill=(60,44,30))
    draw.ellipse([54,24,78,52], fill=(60,44,30))
    draw.ellipse([26,28,44,48], fill=(240,220,190))
    draw.ellipse([56,28,74,48], fill=(240,220,190))
    draw.ellipse([31,33,41,44], fill=(10,10,10))
    draw.ellipse([59,33,69,44], fill=(10,10,10))
    draw.ellipse([30,54,70,80], fill=(215,180,130))
    draw.ellipse([40,56,60,72], fill=(30,22,14))
    draw.ellipse([42,52,58,64], fill=(50,36,24))

def draw_capybara(draw):
    draw.ellipse([10,20,90,86], fill=(140,110,70))
    draw.ellipse([14,54,76,92], fill=(160,130,85))
    draw.ellipse([22,64,38,80], fill=(100,76,44))
    draw.ellipse([46,64,62,80], fill=(100,76,44))
    draw.ellipse([18,22,40,44], fill=(30,22,14))
    draw.ellipse([60,22,82,44], fill=(30,22,14))
    draw.ellipse([20,24,30,34], fill=(255,255,255))
    draw.ellipse([62,24,72,34], fill=(255,255,255))
    draw.ellipse([14,12,40,36], fill=(150,118,76))
    draw.ellipse([60,12,86,36], fill=(150,118,76))
    draw.ellipse([18,16,36,32], fill=(180,148,100))
    draw.ellipse([64,16,82,32], fill=(180,148,100))

def draw_lemur(draw):
    for i in range(5):
        col = (20,18,22) if i%2==0 else (245,242,240)
        draw.rectangle([60+i*6,54,66+i*6,98], fill=col)
    draw.ellipse([14,10,74,70], fill=(100,96,94))
    draw.ellipse([18,16,70,66], fill=(230,228,225))
    draw.ellipse([16,18,42,48], fill=(18,16,20))
    draw.ellipse([46,18,72,48], fill=(18,16,20))
    draw.ellipse([20,22,40,44], fill=(255,160,0))
    draw.ellipse([48,22,68,44], fill=(255,160,0))
    draw.ellipse([25,27,37,40], fill=(10,10,10))
    draw.ellipse([52,27,64,40], fill=(10,10,10))
    draw.ellipse([26,50,62,74], fill=(210,205,200))
    draw.ellipse([6,6,26,28], fill=(90,86,84))
    draw.ellipse([62,6,82,28], fill=(90,86,84))

def draw_chimpanzee(draw):
    draw.ellipse([14,10,86,80], fill=(40,36,32))
    draw.ellipse([6,20,22,50], fill=(180,120,80))
    draw.ellipse([78,20,94,50], fill=(180,120,80))
    draw.ellipse([22,26,78,82], fill=(170,110,70))
    draw.ellipse([22,26,78,44], fill=(35,30,28))
    draw.ellipse([28,32,46,50], fill=(30,24,18))
    draw.ellipse([54,32,72,50], fill=(30,24,18))
    draw.ellipse([30,34,40,44], fill=(255,255,255))
    draw.ellipse([56,34,66,44], fill=(255,255,255))
    draw.ellipse([28,56,72,86], fill=(190,130,85))
    draw.ellipse([38,58,62,78], fill=(30,22,16))
    draw.ellipse([41,60,52,70], fill=(70,55,45))

def draw_sloth(draw):
    draw.ellipse([16,16,84,80], fill=(140,120,90))
    draw.ellipse([22,22,78,72], fill=(90,70,50))
    draw.ellipse([28,30,72,70], fill=(180,160,125))
    for cx,cy in [(8,70),(8,80),(8,90)]:
        draw.polygon([(18,78),(cx,cy),(16,84)], fill=(200,185,155))
    for cx,cy in [(92,70),(92,80),(92,90)]:
        draw.polygon([(82,78),(cx,cy),(84,84)], fill=(200,185,155))
    draw.ellipse([28,32,48,52], fill=(20,18,14))
    draw.ellipse([52,32,72,52], fill=(20,18,14))
    draw.ellipse([30,34,40,44], fill=(255,255,255))
    draw.ellipse([54,34,64,44], fill=(255,255,255))
    draw.ellipse([40,52,60,66], fill=(50,36,26))

def draw_otter(draw):
    draw.ellipse([14,36,86,92], fill=(110,75,40))
    draw.ellipse([22,48,78,88], fill=(175,140,95))
    draw.ellipse([20,14,80,66], fill=(115,80,42))
    draw.ellipse([26,40,74,70], fill=(235,210,175))
    draw.ellipse([36,38,64,56], fill=(35,26,18))
    draw.ellipse([39,40,50,50], fill=(85,65,50))
    draw.ellipse([24,20,44,40], fill=(30,22,14))
    draw.ellipse([56,20,76,40], fill=(30,22,14))
    draw.ellipse([26,22,36,32], fill=(255,255,255))
    draw.ellipse([58,22,68,32], fill=(255,255,255))
    draw.ellipse([16,10,34,30], fill=(105,72,38))
    draw.ellipse([66,10,84,30], fill=(105,72,38))
    for wy in [46,52,58]:
        draw.line([(4,wy),(34,wy+1)], fill=(200,190,175), width=1)
        draw.line([(66,wy+1),(96,wy)], fill=(200,190,175), width=1)

def draw_beaver(draw):
    draw.ellipse([14,14,86,80], fill=(110,76,40))
    draw.ellipse([24,76,76,100], fill=(80,56,28))
    for i in range(3):
        draw.line([(28+i*12,76),(28+i*12,100)], fill=(65,44,20), width=2)
    draw.line([(24,86),(76,86)], fill=(65,44,20), width=2)
    draw.rectangle([40,60,50,78], fill=(245,242,230))
    draw.rectangle([50,60,60,78], fill=(245,242,230))
    draw.line([(50,60),(50,78)], fill=(160,140,110), width=2)
    draw.ellipse([26,52,74,82], fill=(155,115,65))
    draw.ellipse([38,52,62,66], fill=(30,22,14))
    draw.ellipse([22,24,44,46], fill=(30,22,14))
    draw.ellipse([56,24,78,46], fill=(30,22,14))
    draw.ellipse([24,26,34,36], fill=(255,255,255))
    draw.ellipse([58,26,68,36], fill=(255,255,255))
    draw.ellipse([10,10,32,32], fill=(100,68,34))
    draw.ellipse([68,10,90,32], fill=(100,68,34))

def draw_squirrel(draw):
    draw.ellipse([54,30,98,98], fill=(180,100,30))
    draw.ellipse([58,34,94,94], fill=(220,140,50))
    draw.ellipse([62,38,90,90], fill=(245,210,160))
    draw.ellipse([14,44,68,96], fill=(185,105,32))
    draw.ellipse([20,54,60,92], fill=(230,185,130))
    draw.ellipse([14,14,68,62], fill=(190,110,35))
    draw.polygon([(22,18),(14,2),(32,10)], fill=(175,96,28))
    draw.polygon([(52,18),(56,2),(44,10)], fill=(175,96,28))
    draw.polygon([(22,16),(17,5),(30,10)], fill=(255,190,150))
    draw.polygon([(52,16),(55,5),(46,10)], fill=(255,190,150))
    draw.ellipse([18,22,38,42], fill=(20,15,10))
    draw.ellipse([44,22,64,42], fill=(20,15,10))
    draw.ellipse([20,24,30,34], fill=(255,255,255))
    draw.ellipse([46,24,56,34], fill=(255,255,255))
    draw.ellipse([14,40,42,62], fill=(225,180,125))
    draw.ellipse([40,40,68,62], fill=(225,180,125))
    draw.ellipse([34,46,50,58], fill=(40,28,18))

def draw_hamster(draw):
    draw.ellipse([4,34,44,80], fill=(230,190,145))
    draw.ellipse([56,34,96,80], fill=(230,190,145))
    draw.ellipse([14,20,86,84], fill=(210,170,120))
    draw.ellipse([12,14,36,38], fill=(210,170,120))
    draw.ellipse([64,14,88,38], fill=(210,170,120))
    draw.ellipse([16,18,32,34], fill=(255,180,180))
    draw.ellipse([68,18,84,34], fill=(255,180,180))
    draw.ellipse([28,56,72,84], fill=(245,215,175))
    draw.ellipse([40,56,60,70], fill=(220,80,100))
    draw.ellipse([43,58,52,66], fill=(180,50,70))
    draw.ellipse([22,30,44,52], fill=(20,16,12))
    draw.ellipse([56,30,78,52], fill=(20,16,12))
    draw.ellipse([24,32,34,42], fill=(255,255,255))
    draw.ellipse([58,32,68,42], fill=(255,255,255))
    for wy in [64,70,76]:
        draw.line([(2,wy),(30,wy+1)], fill=(200,185,165), width=1)
        draw.line([(70,wy+1),(98,wy)], fill=(200,185,165), width=1)

def draw_pig(draw):
    draw.ellipse([10,16,90,88], fill=(255,165,170))
    draw.polygon([(20,22),(8,2),(40,14)], fill=(240,130,145))
    draw.polygon([(80,22),(92,2),(60,14)], fill=(240,130,145))
    draw.polygon([(20,20),(11,4),(38,14)], fill=(255,160,180))
    draw.polygon([(80,20),(89,4),(62,14)], fill=(255,160,180))
    draw.ellipse([26,56,74,90], fill=(240,140,150))
    draw.ellipse([34,64,48,80], fill=(200,90,110))
    draw.ellipse([52,64,66,80], fill=(200,90,110))
    draw.ellipse([22,30,44,52], fill=(30,22,18))
    draw.ellipse([56,30,78,52], fill=(30,22,18))
    draw.ellipse([24,32,34,42], fill=(255,255,255))
    draw.ellipse([58,32,68,42], fill=(255,255,255))

def draw_goat(draw):
    draw.polygon([(32,18),(22,2),(38,12)], fill=(220,205,175))
    draw.polygon([(68,18),(78,2),(62,12)], fill=(220,205,175))
    draw.ellipse([18,14,82,76], fill=(210,195,170))
    draw.ellipse([34,70,66,96], fill=(200,185,158))
    draw.ellipse([8,28,26,50], fill=(210,195,170))
    draw.ellipse([74,28,92,50], fill=(210,195,170))
    draw.ellipse([11,32,23,46], fill=(240,210,195))
    draw.ellipse([77,32,89,46], fill=(240,210,195))
    draw.ellipse([28,54,72,82], fill=(230,215,188))
    draw.ellipse([36,62,46,72], fill=(160,140,110))
    draw.ellipse([54,62,64,72], fill=(160,140,110))
    draw.ellipse([24,28,44,48], fill=(30,22,14))
    draw.ellipse([56,28,76,48], fill=(30,22,14))
    draw.ellipse([26,30,36,40], fill=(255,230,130))
    draw.ellipse([58,30,68,40], fill=(255,230,130))
    draw.ellipse([30,34,34,38], fill=(10,10,10))
    draw.ellipse([62,34,66,38], fill=(10,10,10))

def draw_donkey(draw):
    draw.ellipse([24,0,42,40], fill=(175,155,130))
    draw.ellipse([58,0,76,40], fill=(175,155,130))
    draw.ellipse([26,2,40,38], fill=(245,195,185))
    draw.ellipse([60,2,74,38], fill=(245,195,185))
    draw.ellipse([16,18,84,82], fill=(180,160,135))
    draw.ellipse([24,52,76,90], fill=(200,180,155))
    draw.ellipse([28,56,72,88], fill=(235,215,195))
    draw.ellipse([36,66,46,78], fill=(140,115,90))
    draw.ellipse([54,66,64,78], fill=(140,115,90))
    draw.ellipse([22,28,44,50], fill=(25,20,14))
    draw.ellipse([56,28,78,50], fill=(25,20,14))
    draw.ellipse([24,30,34,40], fill=(255,255,255))
    draw.ellipse([58,30,68,40], fill=(255,255,255))

def draw_moose(draw):
    draw.polygon([(34,18),(6,4),(12,22),(22,14)], fill=(160,120,60))
    draw.polygon([(66,18),(94,4),(88,22),(78,14)], fill=(160,120,60))
    draw.line([(34,18),(18,2)], fill=(160,120,60), width=4)
    draw.line([(66,18),(82,2)], fill=(160,120,60), width=4)
    draw.line([(18,8),(8,14)], fill=(160,120,60), width=3)
    draw.line([(82,8),(92,14)], fill=(160,120,60), width=3)
    draw.ellipse([22,18,78,72], fill=(100,72,40))
    draw.ellipse([26,52,74,90], fill=(110,80,45))
    draw.ellipse([28,56,72,88], fill=(90,64,34))
    draw.ellipse([34,70,46,82], fill=(60,42,20))
    draw.ellipse([54,70,66,82], fill=(60,42,20))
    draw.ellipse([26,28,44,46], fill=(25,18,10))
    draw.ellipse([56,28,74,46], fill=(25,18,10))
    draw.ellipse([28,30,36,38], fill=(255,255,255))
    draw.ellipse([58,30,66,38], fill=(255,255,255))

def draw_bison(draw):
    draw.ellipse([10,6,90,80], fill=(65,52,34))
    draw.ellipse([14,10,86,74], fill=(80,64,42))
    draw.ellipse([16,6,84,40], fill=(50,38,24))
    draw.polygon([(28,24),(14,8),(24,28)], fill=(200,185,155))
    draw.polygon([(72,24),(86,8),(76,28)], fill=(200,185,155))
    draw.ellipse([26,54,74,86], fill=(90,72,48))
    draw.ellipse([34,60,66,82], fill=(105,84,56))
    draw.ellipse([38,62,50,74], fill=(50,38,24))
    draw.ellipse([50,62,62,74], fill=(50,38,24))
    draw.ellipse([24,32,44,52], fill=(20,16,10))
    draw.ellipse([56,32,76,52], fill=(20,16,10))
    draw.ellipse([26,34,34,42], fill=(255,255,255))
    draw.ellipse([58,34,66,42], fill=(255,255,255))
    draw.ellipse([30,76,70,98], fill=(55,42,26))

def draw_alpaca(draw):
    for cx,cy,r in [(50,50,34),(32,54,20),(68,54,20),(50,30,22),(38,40,20),(62,40,20)]:
        draw.ellipse([cx-r,cy-r,cx+r,cy+r], fill=(240,235,225))
    draw.ellipse([28,44,72,84], fill=(225,205,180))
    draw.polygon([(32,48),(24,26),(44,36)], fill=(210,188,162))
    draw.polygon([(68,48),(76,26),(56,36)], fill=(210,188,162))
    draw.polygon([(32,46),(27,30),(42,36)], fill=(255,200,195))
    draw.polygon([(68,46),(73,30),(58,36)], fill=(255,200,195))
    draw.ellipse([32,62,68,86], fill=(240,220,195))
    draw.ellipse([38,68,48,78], fill=(180,150,115))
    draw.ellipse([52,68,62,78], fill=(180,150,115))
    draw.ellipse([32,48,48,64], fill=(25,20,14))
    draw.ellipse([52,48,68,64], fill=(25,20,14))
    draw.ellipse([34,50,40,56], fill=(255,255,255))
    draw.ellipse([54,50,60,56], fill=(255,255,255))

def draw_armadillo(draw):
    draw.ellipse([10,24,90,84], fill=(165,148,120))
    for by in range(30,80,10):
        draw.rectangle([10,by,90,by+4], fill=(140,124,98))
    draw.ellipse([12,48,50,80], fill=(170,154,126))
    draw.ellipse([16,24,84,52], fill=(182,165,136))
    draw.ellipse([16,56,30,70], fill=(20,18,14))
    draw.ellipse([18,58,24,64], fill=(255,255,255))
    draw.polygon([(12,62),(0,60),(12,66)], fill=(155,138,110))
    draw.ellipse([28,50,46,68], fill=(155,138,110))
    draw.polygon([(86,60),(100,54),(100,66)], fill=(155,138,110))
    draw.ellipse([14,76,36,96], fill=(155,138,110))
    draw.ellipse([64,76,86,96], fill=(155,138,110))

def draw_jaguar(draw):
    draw.ellipse([16,14,84,80], fill=(220,175,70))
    draw.polygon([(28,18),(18,2),(40,12)], fill=(200,155,55))
    draw.polygon([(72,18),(82,2),(60,12)], fill=(200,155,55))
    draw.polygon([(28,16),(21,5),(38,12)], fill=(255,175,165))
    draw.polygon([(72,16),(79,5),(62,12)], fill=(255,175,165))
    for sx,sy in [(30,22),(54,18),(70,26),(24,46),(50,52),(76,44),(34,66)]:
        draw.ellipse([sx-7,sy-7,sx+7,sy+7], fill=(90,55,10))
        draw.ellipse([sx-4,sy-4,sx+4,sy+4], fill=(220,175,70))
        draw.ellipse([sx-2,sy-2,sx+2,sy+2], fill=(55,30,5))
    draw.ellipse([28,54,72,84], fill=(250,230,185))
    draw.polygon([(50,54),(42,64),(58,64)], fill=(200,80,70))
    draw.ellipse([24,26,46,48], fill=(80,170,60))
    draw.ellipse([54,26,76,48], fill=(80,170,60))
    draw.ellipse([30,30,43,46], fill=(10,10,10))
    draw.ellipse([57,30,70,46], fill=(10,10,10))
    draw.ellipse([31,31,36,36], fill=(255,255,255))
    draw.ellipse([58,31,63,36], fill=(255,255,255))

def draw_leopard(draw):
    draw.ellipse([16,14,84,80], fill=(230,190,90))
    draw.polygon([(28,18),(18,2),(40,12)], fill=(210,168,70))
    draw.polygon([(72,18),(82,2),(60,12)], fill=(210,168,70))
    draw.polygon([(28,16),(21,5),(38,12)], fill=(255,185,175))
    draw.polygon([(72,16),(79,5),(62,12)], fill=(255,185,175))
    for sx,sy in [(28,24),(50,18),(74,24),(22,50),(50,54),(78,50),(30,70),(70,70)]:
        draw.ellipse([sx-6,sy-6,sx+6,sy+6], fill=(60,36,8))
        draw.ellipse([sx-3,sy-3,sx+3,sy+3], fill=(230,190,90))
    draw.ellipse([28,54,72,84], fill=(255,240,200))
    draw.polygon([(50,54),(42,64),(58,64)], fill=(200,80,70))
    draw.ellipse([24,26,46,48], fill=(90,170,70))
    draw.ellipse([54,26,76,48], fill=(90,170,70))
    draw.ellipse([30,30,43,46], fill=(10,10,10))
    draw.ellipse([57,30,70,46], fill=(10,10,10))
    draw.ellipse([31,31,36,36], fill=(255,255,255))
    draw.ellipse([58,31,63,36], fill=(255,255,255))

def draw_cheetah(draw):
    draw.ellipse([18,14,82,78], fill=(215,185,90))
    draw.polygon([(30,18),(20,2),(42,12)], fill=(195,164,72))
    draw.polygon([(70,18),(80,2),(58,12)], fill=(195,164,72))
    draw.line([(36,40),(28,68)], fill=(40,28,12), width=3)
    draw.line([(64,40),(72,68)], fill=(40,28,12), width=3)
    for sx,sy in [(26,22),(40,18),(56,18),(72,22),(22,46),(78,46),(32,60),(68,60)]:
        draw.ellipse([sx-4,sy-4,sx+4,sy+4], fill=(50,30,6))
    draw.ellipse([28,54,72,82], fill=(245,225,175))
    draw.polygon([(50,54),(42,62),(58,62)], fill=(190,70,60))
    draw.ellipse([24,26,46,48], fill=(100,175,65))
    draw.ellipse([54,26,76,48], fill=(100,175,65))
    draw.ellipse([30,30,44,46], fill=(10,10,10))
    draw.ellipse([56,30,70,46], fill=(10,10,10))
    draw.ellipse([31,31,36,36], fill=(255,255,255))
    draw.ellipse([57,31,62,36], fill=(255,255,255))

def draw_panther(draw):
    draw.ellipse([16,14,84,80], fill=(28,24,32))
    draw.polygon([(28,18),(18,2),(40,12)], fill=(22,18,26))
    draw.polygon([(72,18),(82,2),(60,12)], fill=(22,18,26))
    draw.polygon([(28,16),(21,5),(38,12)], fill=(180,120,140))
    draw.polygon([(72,16),(79,5),(62,12)], fill=(180,120,140))
    draw.ellipse([28,54,72,84], fill=(48,38,48))
    draw.polygon([(50,54),(42,64),(58,64)], fill=(180,70,80))
    draw.ellipse([24,26,46,48], fill=(80,30,130))
    draw.ellipse([54,26,76,48], fill=(80,30,130))
    draw.ellipse([30,30,43,46], fill=(10,10,10))
    draw.ellipse([57,30,70,46], fill=(10,10,10))
    draw.ellipse([31,31,36,36], fill=(255,255,255))
    draw.ellipse([58,31,63,36], fill=(255,255,255))
    for sx,sy in [(30,24),(54,20),(74,26),(24,50),(76,48)]:
        draw.ellipse([sx-5,sy-5,sx+5,sy+5], fill=(35,30,40))

def draw_seal(draw):
    draw.ellipse([12,24,88,84], fill=(110,100,115))
    draw.ellipse([16,30,84,80], fill=(140,130,145))
    draw.ellipse([24,40,76,78], fill=(210,205,215))
    draw.ellipse([28,12,72,54], fill=(115,105,120))
    draw.ellipse([30,36,70,62], fill=(140,132,148))
    for wy in [42,48,54]:
        draw.line([(4,wy),(34,wy+1)], fill=(230,225,235), width=1)
        draw.line([(66,wy+1),(96,wy)], fill=(230,225,235), width=1)
    draw.ellipse([38,36,62,52], fill=(40,32,44))
    draw.ellipse([30,18,50,38], fill=(20,18,24))
    draw.ellipse([50,18,70,38], fill=(20,18,24))
    draw.ellipse([32,20,40,28], fill=(255,255,255))
    draw.ellipse([52,20,60,28], fill=(255,255,255))
    draw.polygon([(12,62),(0,76),(20,80)], fill=(100,90,105))
    draw.polygon([(88,62),(100,76),(80,80)], fill=(100,90,105))
    draw.polygon([(40,80),(32,98),(68,98),(60,80)], fill=(100,90,105))

def draw_walrus(draw):
    draw.ellipse([8,12,92,88], fill=(140,110,88))
    draw.ellipse([12,16,88,84], fill=(160,128,104))
    draw.ellipse([18,52,82,96], fill=(145,112,88))
    draw.ellipse([24,56,76,94], fill=(165,130,105))
    draw.polygon([(34,86),(22,100),(38,96)], fill=(240,236,220))
    draw.polygon([(66,86),(78,100),(62,96)], fill=(240,236,220))
    for wy in range(58,80,5):
        for wx in range(26,74,6):
            draw.ellipse([wx,wy,wx+3,wy+3], fill=(120,90,70))
    draw.ellipse([20,24,42,46], fill=(25,20,14))
    draw.ellipse([58,24,80,46], fill=(25,20,14))
    draw.ellipse([22,26,32,36], fill=(255,255,255))
    draw.ellipse([60,26,70,36], fill=(255,255,255))
    draw.ellipse([34,52,48,64], fill=(100,75,55))
    draw.ellipse([52,52,66,64], fill=(100,75,55))

def draw_platypus(draw):
    draw.ellipse([14,32,86,84], fill=(100,82,58))
    draw.ellipse([18,36,82,80], fill=(125,103,72))
    draw.polygon([(14,52),(0,46),(0,58)], fill=(60,50,36))
    draw.ellipse([0,46,18,60], fill=(80,66,48))
    draw.ellipse([74,64,100,96], fill=(88,72,50))
    draw.polygon([(22,80),(10,96),(36,92)], fill=(80,65,44))
    draw.polygon([(78,80),(90,96),(64,92)], fill=(80,65,44))
    draw.ellipse([18,18,68,60], fill=(105,86,60))
    draw.ellipse([22,30,40,48], fill=(20,16,10))
    draw.ellipse([24,32,32,40], fill=(255,255,255))

def draw_yak(draw):
    for i in range(0,360,20):
        ox=int(math.cos(math.radians(i))*42)
        oy=int(math.sin(math.radians(i))*36)
        draw.ellipse([48+ox-6,50+oy-6,48+ox+6,50+oy+6], fill=(32,26,18))
    draw.ellipse([10,16,90,84], fill=(38,30,20))
    draw.ellipse([16,22,84,78], fill=(50,40,26))
    draw.polygon([(30,20),(14,2),(26,22)], fill=(200,188,160))
    draw.polygon([(70,20),(86,2),(74,22)], fill=(200,188,160))
    draw.ellipse([22,30,78,78], fill=(44,36,22))
    draw.ellipse([28,56,72,84], fill=(58,46,30))
    draw.ellipse([36,62,64,80], fill=(38,30,18))
    draw.ellipse([24,34,44,54], fill=(20,16,10))
    draw.ellipse([56,34,76,54], fill=(20,16,10))
    draw.ellipse([26,36,34,44], fill=(255,255,255))
    draw.ellipse([58,36,66,44], fill=(255,255,255))

def draw_badger(draw):
    draw.ellipse([14,14,86,80], fill=(200,195,188))
    draw.polygon([(14,14),(40,14),(44,80),(14,80)], fill=(25,22,28))
    draw.polygon([(86,14),(60,14),(56,80),(86,80)], fill=(25,22,28))
    draw.ellipse([38,14,62,80], fill=(240,238,235))
    draw.ellipse([8,8,28,30], fill=(30,26,32))
    draw.ellipse([72,8,92,30], fill=(30,26,32))
    draw.ellipse([12,12,24,26], fill=(200,192,185))
    draw.ellipse([76,12,88,26], fill=(200,192,185))
    draw.ellipse([20,26,40,46], fill=(10,10,10))
    draw.ellipse([60,26,80,46], fill=(10,10,10))
    draw.ellipse([22,28,30,36], fill=(255,255,255))
    draw.ellipse([62,28,70,36], fill=(255,255,255))
    draw.ellipse([40,56,60,72], fill=(25,22,28))
    draw.ellipse([43,58,52,66], fill=(80,76,82))
    draw.arc([40,64,60,80], 5, 175, fill=(25,22,28), width=2)

def draw_chicken(draw):
    draw.ellipse([18,40,82,92], fill=(240,220,180))
    draw.ellipse([24,48,76,88], fill=(255,235,200))
    draw.polygon([(74,54),(96,38),(96,50),(86,60)], fill=(180,150,90))
    draw.polygon([(74,58),(100,50),(100,62),(82,66)], fill=(160,130,70))
    draw.rectangle([38,22,62,52], fill=(240,220,180))
    draw.ellipse([28,10,72,42], fill=(240,220,180))
    draw.polygon([(34,10),(32,0),(40,8),(46,0),(50,8),(56,0),(58,10)], fill=(220,30,30))
    draw.ellipse([34,32,50,52], fill=(220,30,30))
    draw.ellipse([46,32,62,52], fill=(200,20,20))
    draw.polygon([(28,24),(10,24),(10,30),(28,28)], fill=(240,180,0))
    draw.ellipse([30,14,48,32], fill=(255,200,0))
    draw.ellipse([34,18,46,30], fill=(10,10,10))
    draw.ellipse([35,19,39,23], fill=(255,255,255))

# ─── FRUITS ────────────────────────────────────────────────────────────────────

def draw_apple_100(draw):
    draw.ellipse([16,18,84,86], fill=(210,35,35))
    draw.ellipse([22,18,78,86], fill=(240,55,55))
    draw.ellipse([22,18,58,56], fill=(255,100,80))
    draw.line([(50,18),(50,6)], fill=(100,60,28), width=3)
    draw.polygon([(50,9),(64,2),(58,12)], fill=(40,155,40))
    draw.ellipse([36,24,48,36], fill=(255,160,140))

def draw_apricot_100(draw):
    draw.ellipse([14,16,86,88], fill=(255,150,50))
    draw.ellipse([20,16,80,88], fill=(255,180,80))
    draw.ellipse([20,16,55,55], fill=(255,220,150))
    draw.arc([14,16,86,88], 90, 270, fill=(220,115,25), width=2)
    draw.line([(50,16),(50,6)], fill=(100,60,28), width=3)
    draw.polygon([(50,9),(62,3),(57,12)], fill=(50,160,50))

def draw_avocado_100(draw):
    draw.ellipse([18,8,82,92], fill=(28,75,28))
    draw.ellipse([22,12,78,88], fill=(170,205,70))
    draw.ellipse([26,16,74,84], fill=(210,235,110))
    draw.ellipse([34,44,66,76], fill=(115,65,25))
    draw.ellipse([36,46,64,74], fill=(145,90,45))

def draw_banana_100(draw):
    draw.arc([8,8,92,92], 18, 162, fill=(230,210,20), width=12)
    draw.arc([14,14,86,86], 20, 158, fill=(255,235,50), width=8)
    draw.polygon([(86,30),(92,24),(86,20)], fill=(80,65,15))
    draw.polygon([(14,30),(10,38),(16,36)], fill=(60,48,8))
    draw.ellipse([34,16,48,30], fill=(255,250,160))

def draw_blackberry_100(draw):
    for ox,oy in [(0,0),(-8,9),(8,9),(-12,20),(0,20),(12,20),(-8,31),(8,31),(0,40)]:
        draw.ellipse([46+ox-7,14+oy-7,46+ox+7,14+oy+7], fill=(28,12,42))
        draw.ellipse([46+ox-5,14+oy-5,46+ox+5,14+oy+5], fill=(48,22,70))
        draw.ellipse([46+ox-2,14+oy-10,46+ox+2,14+oy-6], fill=(80,40,110))
    draw.polygon([(38,14),(50,4),(62,14)], fill=(50,145,50))

def draw_blueberry_100(draw):
    draw.ellipse([14,20,86,92], fill=(38,56,145))
    draw.ellipse([20,24,80,88], fill=(58,86,195))
    draw.ellipse([20,24,55,60], fill=(110,140,230))
    draw.polygon([(38,20),(50,12),(62,20)], fill=(18,28,75))
    draw.polygon([(50,20),(50,26),(58,20)], fill=(18,28,75))
    draw.ellipse([50,14,80,44], fill=(28,42,115))

def draw_blood_orange_100(draw):
    draw.ellipse([12,12,88,88], fill=(200,50,50))
    draw.ellipse([16,16,84,84], fill=(220,70,70))
    draw.ellipse([20,20,80,80], fill=(240,100,80))
    for deg in range(0,360,60):
        x=50+int(math.cos(math.radians(deg))*28)
        y=50+int(math.sin(math.radians(deg))*28)
        draw.line([(50,50),(x,y)], fill=(180,30,30), width=2)
    draw.ellipse([40,40,60,60], fill=(230,80,60))
    draw.line([(50,12),(50,6)], fill=(100,60,28), width=3)

def draw_boysenberry_100(draw):
    for ox,oy in [(0,0),(-9,8),(9,8),(-13,18),(0,18),(13,18),(-9,28),(9,28),(0,36)]:
        draw.ellipse([46+ox-7,16+oy-7,46+ox+7,16+oy+7], fill=(75,18,65))
        draw.ellipse([46+ox-5,16+oy-5,46+ox+5,16+oy+5], fill=(110,30,95))
        draw.ellipse([46+ox-2,16+oy-9,46+ox+2,16+oy-5], fill=(150,60,130))
    draw.polygon([(38,16),(50,6),(62,16)], fill=(50,140,50))

def draw_cantaloupe_100(draw):
    draw.ellipse([8,12,68,88], fill=(155,135,95))
    draw.ellipse([10,14,66,86], fill=(200,185,145))
    for cx,cy,r in [(24,50,6),(24,30,5),(24,70,5),(42,22,5),(42,78,5)]:
        draw.ellipse([cx-r,cy-r,cx+r,cy+r], fill=(220,205,165))
    draw.polygon([(54,26),(92,20),(92,80),(54,74)], fill=(115,95,65))
    draw.polygon([(56,28),(90,22),(90,78),(56,72)], fill=(255,135,44))
    draw.ellipse([58,32,88,68], fill=(255,175,80))

def draw_cherry_100(draw):
    draw.line([(50,10),(32,38)], fill=(100,145,55), width=3)
    draw.line([(50,10),(68,38)], fill=(100,145,55), width=3)
    draw.arc([(32,8),(68,20)], 180, 0, fill=(100,145,55), width=3)
    draw.ellipse([14,30,46,62], fill=(175,8,26))
    draw.ellipse([18,32,40,56], fill=(215,38,58))
    draw.ellipse([18,32,28,42], fill=(240,100,110))
    draw.ellipse([54,30,86,62], fill=(175,8,26))
    draw.ellipse([58,32,80,56], fill=(215,38,58))
    draw.ellipse([58,32,68,42], fill=(240,100,110))

def draw_coconut_100(draw):
    draw.ellipse([8,18,62,72], fill=(98,62,28))
    draw.ellipse([12,22,58,68], fill=(130,90,50))
    draw.ellipse([22,30,34,42], fill=(50,28,8))
    draw.ellipse([36,28,48,40], fill=(50,28,8))
    draw.ellipse([30,40,42,52], fill=(50,28,8))
    draw.ellipse([48,22,92,82], fill=(98,62,28))
    draw.ellipse([50,24,90,80], fill=(250,250,250))

def draw_cranberry_100(draw):
    draw.ellipse([12,26,44,58], fill=(158,8,38))
    draw.ellipse([16,28,40,54], fill=(190,20,50))
    draw.ellipse([20,28,30,38], fill=(220,60,80))
    draw.ellipse([42,18,72,48], fill=(140,4,28))
    draw.ellipse([44,20,68,44], fill=(175,16,42))
    draw.ellipse([20,44,58,82], fill=(185,18,48))
    draw.ellipse([24,48,54,78], fill=(215,38,62))
    draw.polygon([(18,24),(14,14),(24,20)], fill=(50,140,50))

def draw_date_100(draw):
    draw.ellipse([22,20,56,58], fill=(88,48,28))
    draw.ellipse([26,24,52,54], fill=(115,70,38))
    draw.ellipse([40,34,70,72], fill=(70,34,14))
    draw.ellipse([44,36,66,68], fill=(95,52,26))
    draw.ellipse([30,46,64,80], fill=(84,44,20))
    draw.ellipse([34,48,60,76], fill=(110,66,32))
    draw.line([(50,20),(50,10)], fill=(100,60,28), width=3)

def draw_dragonfruit_100(draw):
    draw.ellipse([10,12,78,88], fill=(230,42,112))
    draw.polygon([(10,46),(2,40),(12,38)], fill=(72,190,72))
    draw.polygon([(10,54),(2,48),(12,46)], fill=(72,190,72))
    draw.polygon([(44,12),(40,2),(48,10)], fill=(72,190,72))
    draw.polygon([(52,12),(50,2),(58,10)], fill=(72,190,72))
    draw.ellipse([40,30,90,80], fill=(230,42,112))
    draw.ellipse([42,32,88,78], fill=(255,255,255))
    for sx,sy in [(56,46),(64,52),(58,62),(70,44),(72,60),(62,70),(52,56)]:
        draw.ellipse([sx-2,sy-3,sx+2,sy+1], fill=(10,10,10))

def draw_durian_100(draw):
    draw.ellipse([10,14,90,88], fill=(190,175,90))
    for angle in range(0,360,22):
        cx,cy=50,51
        dx=math.cos(math.radians(angle))
        dy=math.sin(math.radians(angle))
        ox,oy=int(cx+dx*36),int(cy+dy*34)
        px1=int(cx+dx*32+dy*5); py1=int(cy+dy*30-dx*5)
        px2=int(cx+dx*32-dy*5); py2=int(cy+dy*30+dx*5)
        draw.polygon([(px1,py1),(ox,oy),(px2,py2)], fill=(160,145,65))
    draw.ellipse([20,24,80,78], fill=(205,190,100))

def draw_elderberry_100(draw):
    for ox,oy in [(-14,0),(14,0),(0,-12),(-8,-20),(8,-20),(0,10),(-14,12),(14,12)]:
        draw.ellipse([50+ox-5,54+oy-5,50+ox+5,54+oy+5], fill=(12,6,22))
        draw.ellipse([50+ox-3,54+oy-3,50+ox+3,54+oy+3], fill=(28,14,48))
    draw.line([(50,54),(50,22)], fill=(60,100,30), width=3)
    draw.line([(50,38),(36,30)], fill=(60,100,30), width=2)
    draw.line([(50,38),(64,30)], fill=(60,100,30), width=2)
    draw.line([(50,46),(38,40)], fill=(60,100,30), width=2)
    draw.line([(50,46),(62,40)], fill=(60,100,30), width=2)

def draw_fig_100(draw):
    draw.ellipse([18,22,82,88], fill=(115,52,90))
    draw.ellipse([22,26,78,84], fill=(145,72,115))
    draw.ellipse([22,26,54,58], fill=(175,108,150))
    draw.ellipse([34,10,56,28], fill=(95,40,70))
    draw.polygon([(34,14),(32,4),(46,10)], fill=(55,145,55))
    draw.ellipse([38,72,62,90], fill=(135,62,100))
    draw.ellipse([40,74,60,88], fill=(200,140,170))
    for sx,sy in [(44,77),(48,82),(54,77),(52,82)]:
        draw.ellipse([sx-2,sy-2,sx+2,sy+2], fill=(80,30,60))

def draw_gooseberry_100(draw):
    draw.ellipse([18,18,82,82], fill=(180,210,130))
    draw.ellipse([22,22,78,78], fill=(210,235,160))
    draw.ellipse([22,22,50,50], fill=(240,255,200))
    for deg in range(0,360,40):
        x=50+int(math.cos(math.radians(deg))*28)
        y=50+int(math.sin(math.radians(deg))*28)
        draw.line([(50,50),(x,y)], fill=(160,190,110), width=2)
    draw.line([(50,18),(50,8)], fill=(100,60,28), width=2)
    draw.polygon([(50,9),(58,3),(55,11)], fill=(55,150,55))

def draw_grape_100(draw):
    for ox,oy in [(-14,0),(14,0),(0,0),(-7,-14),(7,-14),(-7,14),(7,14),(-14,28),(14,28),(0,28)]:
        draw.ellipse([50+ox-10,48+oy-10,50+ox+10,48+oy+10], fill=(90,40,135))
        draw.ellipse([50+ox-7,48+oy-7,50+ox+7,48+oy+7], fill=(130,70,180))
        draw.ellipse([50+ox-4,48+oy-8,50+ox,48+oy-4], fill=(175,130,210))
    draw.line([(50,38),(50,18)], fill=(90,130,45), width=3)
    draw.line([(50,24),(36,16)], fill=(90,130,45), width=2)
    draw.line([(50,24),(64,16)], fill=(90,130,45), width=2)
    draw.polygon([(44,18),(36,8),(56,8),(56,18)], fill=(90,130,45))

def draw_grapefruit_100(draw):
    draw.ellipse([10,10,90,90], fill=(240,120,80))
    draw.ellipse([14,14,86,86], fill=(255,150,100))
    draw.ellipse([18,18,82,82], fill=(255,180,130))
    for deg in range(0,360,45):
        x=50+int(math.cos(math.radians(deg))*30)
        y=50+int(math.sin(math.radians(deg))*30)
        draw.line([(50,50),(x,y)], fill=(225,105,65), width=2)
    draw.ellipse([40,40,60,60], fill=(255,200,150))
    draw.line([(50,10),(50,4)], fill=(100,60,28), width=3)

def draw_guava_100(draw):
    draw.ellipse([14,14,86,86], fill=(205,210,130))
    draw.ellipse([18,18,82,82], fill=(230,235,160))
    draw.ellipse([18,18,56,56], fill=(250,255,200))
    draw.ellipse([32,52,68,80], fill=(255,140,120))
    for sx,sy in [(40,58),(50,62),(44,70),(54,68)]:
        draw.ellipse([sx-2,sy-2,sx+2,sy+2], fill=(180,60,50))
    draw.line([(50,14),(50,6)], fill=(100,60,28), width=3)
    draw.polygon([(50,7),(60,1),(56,10)], fill=(55,145,55))

def draw_honeydew_100(draw):
    draw.ellipse([10,10,90,90], fill=(170,210,130))
    draw.ellipse([14,14,86,86], fill=(195,230,158))
    draw.ellipse([18,18,82,82], fill=(220,248,185))
    draw.ellipse([24,24,76,76], fill=(240,255,210))
    for deg in range(0,360,40):
        x=50+int(math.cos(math.radians(deg))*22)
        y=50+int(math.sin(math.radians(deg))*22)
        draw.line([(50,50),(x,y)], fill=(185,225,148), width=2)

def draw_jackfruit_100(draw):
    draw.ellipse([10,8,82,92], fill=(190,165,40))
    for bx in range(14,80,10):
        for by in range(12,90,10):
            draw.ellipse([bx-3,by-3,bx+3,by+3], fill=(160,138,28))
    draw.polygon([(74,36),(92,28),(92,72),(74,64)], fill=(150,130,22))
    draw.polygon([(76,38),(90,30),(90,70),(76,62)], fill=(255,200,50))

def draw_key_lime_100(draw):
    draw.ellipse([16,16,84,84], fill=(120,195,70))
    draw.ellipse([20,20,80,80], fill=(155,220,100))
    draw.ellipse([20,20,56,56], fill=(200,240,150))
    draw.ellipse([38,38,62,62], fill=(175,228,120))
    draw.line([(50,16),(50,8)], fill=(100,60,28), width=2)
    draw.polygon([(50,9),(58,3),(55,11)], fill=(55,150,55))

def draw_kiwi_100(draw):
    draw.ellipse([12,12,88,88], fill=(88,62,38))
    draw.ellipse([16,16,84,84], fill=(110,80,50))
    draw.ellipse([18,18,82,82], fill=(55,145,55))
    draw.ellipse([22,22,78,78], fill=(90,180,80))
    draw.ellipse([30,30,70,70], fill=(220,240,120))
    for deg in range(15,360,35):
        dx=math.cos(math.radians(deg)); dy=math.sin(math.radians(deg))
        sx=int(50+dx*24); sy=int(50+dy*24)
        draw.ellipse([sx-3,sy-5,sx+3,sy+3], fill=(14,10,6))
    draw.ellipse([44,44,56,56], fill=(235,252,145))

def draw_kumquat_100(draw):
    draw.ellipse([22,10,78,90], fill=(255,130,20))
    draw.ellipse([26,14,74,86], fill=(255,160,50))
    draw.ellipse([26,14,54,52], fill=(255,210,120))
    for deg in range(0,360,60):
        x=50+int(math.cos(math.radians(deg))*24)
        y=50+int(math.sin(math.radians(deg))*24)
        draw.line([(50,50),(x,y)], fill=(230,110,10), width=2)
    draw.line([(50,10),(50,2)], fill=(100,60,28), width=3)
    draw.polygon([(50,3),(60,-3),(56,7)], fill=(55,145,55))

def draw_lemon_100(draw):
    draw.ellipse([10,22,90,78], fill=(255,230,20))
    draw.ellipse([14,26,86,74], fill=(255,245,70))
    draw.ellipse([14,26,54,56], fill=(255,252,170))
    draw.polygon([(10,50),(2,46),(2,54)], fill=(215,185,10))
    draw.polygon([(90,50),(98,46),(98,54)], fill=(215,185,10))
    draw.line([(50,22),(50,12)], fill=(100,60,28), width=3)
    draw.polygon([(50,13),(60,6),(56,16)], fill=(55,145,55))

def draw_lime_100(draw):
    draw.ellipse([12,12,88,88], fill=(70,185,50))
    draw.ellipse([16,16,84,84], fill=(100,210,75))
    draw.ellipse([16,16,52,52], fill=(160,235,130))
    for deg in range(0,360,45):
        x=50+int(math.cos(math.radians(deg))*28)
        y=50+int(math.sin(math.radians(deg))*28)
        draw.line([(50,50),(x,y)], fill=(60,165,42), width=2)
    draw.line([(50,12),(50,4)], fill=(100,60,28), width=2)

def draw_lychee_100(draw):
    draw.ellipse([14,14,86,86], fill=(210,60,80))
    draw.ellipse([18,18,82,82], fill=(235,90,108))
    for bx in range(20,80,12):
        for by in range(20,80,12):
            if (bx-50)**2+(by-50)**2<34**2:
                draw.ellipse([bx-4,by-4,bx+4,by+4], fill=(220,75,95))
    draw.ellipse([36,36,64,64], fill=(255,240,235))
    draw.line([(50,14),(50,6)], fill=(100,60,28), width=3)

def draw_mango_100(draw):
    draw.ellipse([14,10,86,90], fill=(255,160,30))
    draw.ellipse([18,14,82,86], fill=(255,190,60))
    draw.ellipse([18,14,60,56], fill=(255,230,120))
    draw.ellipse([50,12,80,42], fill=(230,80,40))
    draw.line([(50,10),(50,2)], fill=(100,60,28), width=3)
    draw.polygon([(50,3),(62,-3),(57,9)], fill=(55,145,55))
    draw.ellipse([36,22,50,36], fill=(255,245,175))

def draw_mangosteen_100(draw):
    draw.ellipse([12,12,88,88], fill=(65,28,70))
    draw.ellipse([16,16,84,84], fill=(90,44,100))
    draw.ellipse([16,16,52,52], fill=(130,75,140))
    draw.polygon([(30,88),(34,100),(38,88)], fill=(55,115,40))
    draw.polygon([(42,88),(46,100),(50,88)], fill=(55,115,40))
    draw.polygon([(54,88),(58,100),(62,88)], fill=(55,115,40))
    draw.polygon([(66,88),(70,100),(74,88)], fill=(55,115,40))
    draw.line([(50,12),(50,4)], fill=(100,60,28), width=3)

def draw_mulberry_100(draw):
    for ox,oy in [(-8,-8),(8,-8),(-12,2),(0,-2),(12,2),(-8,12),(8,12),(0,22)]:
        draw.ellipse([50+ox-6,46+oy-6,50+ox+6,46+oy+6], fill=(68,14,80))
        draw.ellipse([50+ox-4,46+oy-4,50+ox+4,46+oy+4], fill=(100,28,115))
    draw.polygon([(38,38),(50,28),(62,38)], fill=(50,140,50))
    draw.line([(50,36),(50,22)], fill=(80,150,50), width=2)

def draw_nectarine_100(draw):
    draw.ellipse([14,14,86,86], fill=(230,100,60))
    draw.ellipse([18,18,82,82], fill=(255,140,80))
    draw.ellipse([18,18,56,56], fill=(255,200,120))
    draw.ellipse([52,14,82,44], fill=(200,60,30))
    draw.arc([14,14,86,86], 90, 270, fill=(200,80,40), width=2)
    draw.line([(50,14),(50,6)], fill=(100,60,28), width=3)
    draw.polygon([(50,7),(60,1),(56,11)], fill=(55,145,55))

def draw_orange_100(draw):
    draw.ellipse([10,10,90,90], fill=(240,130,30))
    draw.ellipse([14,14,86,86], fill=(255,158,55))
    draw.ellipse([14,14,52,52], fill=(255,210,120))
    for deg in range(0,360,45):
        x=50+int(math.cos(math.radians(deg))*30)
        y=50+int(math.sin(math.radians(deg))*30)
        draw.line([(50,50),(x,y)], fill=(215,110,20), width=2)
    draw.ellipse([40,40,60,60], fill=(255,180,80))
    draw.line([(50,10),(50,2)], fill=(100,60,28), width=3)
    draw.polygon([(50,3),(60,-3),(56,8)], fill=(55,145,55))

def draw_papaya_100(draw):
    draw.ellipse([18,6,82,94], fill=(255,165,60))
    draw.ellipse([22,10,78,90], fill=(255,200,90))
    draw.ellipse([22,10,58,52], fill=(255,235,160))
    draw.polygon([(44,6),(50,-4),(56,6)], fill=(55,135,55))
    draw.ellipse([30,62,70,94], fill=(255,130,50))
    for sx,sy in [(40,68),(50,72),(44,80),(54,76),(50,64)]:
        draw.ellipse([sx-3,sy-4,sx+3,sy+4], fill=(80,40,20))

def draw_passionfruit_100(draw):
    draw.ellipse([12,12,88,88], fill=(80,30,100))
    draw.ellipse([16,16,84,84], fill=(110,50,135))
    draw.ellipse([16,16,52,52], fill=(155,90,180))
    for bx in range(18,82,14):
        for by in range(18,82,14):
            if (bx-50)**2+(by-50)**2<34**2:
                draw.ellipse([bx-1,by-1,bx+1,by+1], fill=(140,72,165))
    draw.line([(50,12),(50,4)], fill=(100,60,28), width=3)

def draw_peach_100(draw):
    draw.ellipse([12,12,88,88], fill=(255,185,120))
    draw.ellipse([16,16,84,84], fill=(255,210,150))
    draw.ellipse([16,16,55,55], fill=(255,240,200))
    draw.ellipse([50,12,82,44], fill=(240,130,90))
    draw.arc([12,12,88,88], 90, 270, fill=(235,160,100), width=2)
    draw.line([(50,12),(50,4)], fill=(100,60,28), width=3)
    draw.polygon([(50,5),(60,-1),(56,9)], fill=(55,145,55))
    draw.ellipse([36,22,50,36], fill=(255,250,225))

def draw_pear_100(draw):
    draw.ellipse([16,40,84,94], fill=(185,215,90))
    draw.ellipse([20,44,80,90], fill=(215,240,120))
    draw.ellipse([20,44,56,72], fill=(240,255,170))
    draw.ellipse([28,8,72,52], fill=(170,198,75))
    draw.ellipse([32,12,68,48], fill=(200,228,100))
    draw.line([(50,8),(50,0)], fill=(100,60,28), width=3)
    draw.polygon([(50,1),(60,-5),(56,7)], fill=(55,145,55))

def draw_persimmon_100(draw):
    draw.ellipse([12,18,88,88], fill=(230,100,28))
    draw.ellipse([16,22,84,84], fill=(255,130,50))
    draw.ellipse([16,22,56,60], fill=(255,195,120))
    for deg in [0,90,180,270]:
        x=50+int(math.cos(math.radians(deg))*20)
        draw.polygon([(50,18),(x,4),(50+int(math.cos(math.radians(deg+45))*14),12)], fill=(65,125,45))
    draw.ellipse([38,14,62,26], fill=(70,130,48))

def draw_pineapple_100(draw):
    draw.ellipse([16,24,84,92], fill=(220,170,40))
    draw.ellipse([20,28,80,88], fill=(240,195,60))
    for bx in range(22,78,12):
        for by in range(30,88,10):
            draw.ellipse([bx-4,by-4,bx+4,by+4], fill=(195,145,22))
    for angle in range(-30,31,12):
        lx=50+int(math.sin(math.radians(angle))*22)
        draw.polygon([(50,24),(lx,4-abs(angle//6)),(50+int(math.sin(math.radians(angle+4))*16),18)], fill=(50,140,50))

def draw_plum_100(draw):
    draw.ellipse([14,12,86,88], fill=(90,28,115))
    draw.ellipse([18,16,82,84], fill=(120,48,150))
    draw.ellipse([18,16,54,54], fill=(175,100,200))
    draw.arc([14,12,86,88], 90, 270, fill=(75,18,95), width=2)
    draw.line([(50,12),(50,4)], fill=(100,60,28), width=3)
    draw.polygon([(50,5),(60,-1),(56,9)], fill=(55,145,55))

def draw_pomegranate_100(draw):
    draw.ellipse([10,14,90,90], fill=(200,30,50))
    draw.ellipse([14,18,86,86], fill=(225,55,70))
    draw.ellipse([14,18,52,56], fill=(255,100,105))
    draw.polygon([(32,14),(28,2),(36,10)], fill=(180,24,40))
    draw.polygon([(50,14),(48,0),(54,10)], fill=(180,24,40))
    draw.polygon([(68,14),(72,2),(64,10)], fill=(180,24,40))
    draw.ellipse([30,40,70,80], fill=(200,28,46))
    for sx,sy in [(38,46),(46,52),(54,46),(50,58),(42,58),(44,65),(54,66)]:
        draw.ellipse([sx-4,sy-5,sx+4,sy+5], fill=(240,90,110))

def draw_pomelo_100(draw):
    draw.ellipse([8,8,92,92], fill=(200,220,140))
    draw.ellipse([12,12,88,88], fill=(225,242,168))
    draw.ellipse([12,12,52,52], fill=(248,255,210))
    for deg in range(0,360,45):
        x=50+int(math.cos(math.radians(deg))*32)
        y=50+int(math.sin(math.radians(deg))*32)
        draw.line([(50,50),(x,y)], fill=(185,210,120), width=2)
    draw.line([(50,8),(50,0)], fill=(100,60,28), width=3)
    draw.polygon([(50,1),(62,-5),(57,8)], fill=(55,145,55))

def draw_quince_100(draw):
    draw.ellipse([12,14,88,88], fill=(220,200,60))
    draw.ellipse([16,18,84,84], fill=(245,225,90))
    draw.ellipse([16,18,54,58], fill=(255,248,170))
    draw.ellipse([28,8,72,34], fill=(210,190,50))
    draw.line([(50,8),(50,0)], fill=(100,60,28), width=3)
    draw.polygon([(50,1),(60,-5),(55,8)], fill=(55,145,55))

def draw_raspberry_100(draw):
    for ox,oy in [(0,-8),(-8,0),(8,0),(-4,-14),(4,-14),(-12,-8),(12,-8),
                  (-14,6),(14,6),(-10,14),(10,14),(0,8),(0,18),(-8,22),(8,22)]:
        draw.ellipse([50+ox-6,50+oy-6,50+ox+6,50+oy+6], fill=(200,20,60))
        draw.ellipse([50+ox-4,50+oy-4,50+ox+4,50+oy+4], fill=(230,50,85))
        draw.ellipse([50+ox-2,50+oy-8,50+ox+2,50+oy-4], fill=(255,120,145))
    draw.polygon([(36,42),(50,30),(64,42)], fill=(50,140,50))

def draw_red_currant_100(draw):
    for ox,oy in [(-8,-20),(8,-20),(0,-10),(-14,0),(14,0),(-8,12),(8,12),(0,22),(-12,26),(12,26)]:
        draw.ellipse([50+ox-5,54+oy-5,50+ox+5,54+oy+5], fill=(195,14,35))
        draw.ellipse([50+ox-3,54+oy-3,50+ox+3,54+oy+3], fill=(225,38,60))
        draw.ellipse([50+ox-1,54+oy-5,50+ox+1,54+oy-2], fill=(255,120,135))
    draw.line([(50,34),(50,12)], fill=(75,130,40), width=2)
    draw.line([(50,22),(36,14)], fill=(75,130,40), width=2)
    draw.line([(50,22),(64,14)], fill=(75,130,40), width=2)

def draw_star_apple_100(draw):
    draw.ellipse([12,12,88,88], fill=(90,40,115))
    draw.ellipse([16,16,84,84], fill=(120,60,150))
    draw.ellipse([16,16,52,52], fill=(170,110,195))
    draw.ellipse([28,28,72,72], fill=(130,70,160))
    for deg in range(0,360,72):
        sx=int(50+math.cos(math.radians(deg))*16)
        sy=int(50+math.sin(math.radians(deg))*16)
        draw.ellipse([sx-4,sy-5,sx+4,sy+5], fill=(255,240,210))
    draw.line([(50,12),(50,4)], fill=(100,60,28), width=3)

def draw_starfruit_100(draw):
    pts=[]
    for i in range(10):
        angle=math.radians(i*36-90)
        r=38 if i%2==0 else 18
        pts.append((50+r*math.cos(angle), 50+r*math.sin(angle)))
    draw.polygon(pts, fill=(255,210,40))
    inner_pts=[]
    for i in range(10):
        angle=math.radians(i*36-90)
        r=32 if i%2==0 else 14
        inner_pts.append((50+r*math.cos(angle), 50+r*math.sin(angle)))
    draw.polygon(inner_pts, fill=(255,235,100))
    draw.ellipse([40,40,60,60], fill=(255,250,180))
    draw.line([(50,12),(50,4)], fill=(100,60,28), width=2)

def draw_strawberry_100(draw):
    draw.polygon([(50,88),(14,34),(86,34)], fill=(210,30,48))
    draw.polygon([(50,84),(18,36),(82,36)], fill=(240,58,72))
    draw.ellipse([18,36,56,72], fill=(255,110,115))
    for sx,sy in [(30,42),(40,52),(50,44),(60,52),(68,44),(36,62),(46,70),(56,62),(64,70),(42,78),(54,76)]:
        draw.ellipse([sx-2,sy-3,sx+2,sy+1], fill=(200,20,28))
        draw.ellipse([sx-1,sy-2,sx+1,sy-1], fill=(255,200,180))
    draw.polygon([(50,34),(40,18),(44,28)], fill=(55,155,40))
    draw.polygon([(50,34),(60,18),(56,28)], fill=(50,145,36))
    draw.polygon([(50,34),(50,14),(50,28)], fill=(60,165,44))
    draw.polygon([(50,34),(34,24),(42,30)], fill=(48,140,36))
    draw.polygon([(50,34),(66,24),(58,30)], fill=(55,150,40))

def draw_tangerine_100(draw):
    draw.ellipse([12,12,88,88], fill=(255,140,0))
    draw.ellipse([16,16,84,84], fill=(255,168,30))
    draw.ellipse([16,16,52,52], fill=(255,220,120))
    for deg in range(0,360,45):
        x=50+int(math.cos(math.radians(deg))*28)
        y=50+int(math.sin(math.radians(deg))*28)
        draw.line([(50,50),(x,y)], fill=(230,120,0), width=2)
    draw.ellipse([40,40,60,60], fill=(255,195,60))
    draw.line([(50,12),(50,4)], fill=(100,60,28), width=3)
    draw.polygon([(50,5),(60,-1),(56,9)], fill=(55,145,55))

def draw_watermelon_100(draw):
    draw.polygon([(8,92),(50,8),(92,92)], fill=(70,165,55))
    draw.polygon([(12,92),(50,12),(88,92)], fill=(90,185,70))
    draw.polygon([(18,92),(50,18),(82,92)], fill=(30,140,38))
    draw.polygon([(24,92),(50,24),(76,92)], fill=(230,40,55))
    draw.polygon([(28,92),(50,30),(72,92)], fill=(255,70,80))
    draw.ellipse([30,32,52,54], fill=(255,140,140))
    for sx,sy in [(40,52),(50,60),(60,52),(44,68),(56,68),(50,78),(42,78),(58,78)]:
        draw.ellipse([sx-3,sy-5,sx+3,sy+3], fill=(18,16,20))
    draw.polygon([(50,92),(44,100),(56,100)], fill=(50,145,40))

def draw_black_currant_100(draw):
    draw_blackberry_100(draw)

# ─── DISPATCH ──────────────────────────────────────────────────────────────────

ANIMAL_FUNCS = {
    "alligator": draw_alligator, "alpaca": draw_alpaca, "ant": draw_ant,
    "armadillo": draw_armadillo, "badger": draw_badger, "bat": draw_bat,
    "bear": draw_bear, "beaver": draw_beaver, "bee": draw_bee,
    "bison": draw_bison, "butterfly": draw_butterfly, "camel": draw_camel,
    "capybara": draw_capybara, "cat": draw_cat, "chameleon": draw_chameleon,
    "cheetah": draw_cheetah, "chicken": draw_chicken,
    "chimpanzee": draw_chimpanzee, "cow": draw_cow, "crab": draw_crab,
    "crocodile": draw_crocodile, "crow": draw_crow, "deer": draw_deer,
    "dog": draw_dog, "dolphin": draw_dolphin, "donkey": draw_donkey,
    "duck": draw_duck, "eagle": draw_eagle, "elephant": draw_elephant,
    "emu": draw_emu, "falcon": draw_falcon, "flamingo": draw_flamingo,
    "fox": draw_fox, "frog": draw_frog, "giraffe": draw_giraffe,
    "goat": draw_goat, "goose": draw_goose, "gorilla": draw_gorilla,
    "hamster": draw_hamster, "hedgehog": draw_hedgehog, "hippo": draw_hippo,
    "horse": draw_horse, "iguana": draw_iguana, "jaguar": draw_jaguar,
    "kangaroo": draw_kangaroo, "koala": draw_koala, "lemur": draw_lemur,
    "leopard": draw_leopard, "lion": draw_lion, "lizard": draw_lizard,
    "meerkat": draw_meerkat, "monkey": draw_monkey, "moose": draw_moose,
    "octopus": draw_octopus, "ostrich": draw_ostrich, "otter": draw_otter,
    "owl": draw_owl, "panda": draw_panda, "panther": draw_panther,
    "parrot": draw_parrot, "peacock": draw_peacock, "pelican": draw_pelican,
    "penguin": draw_penguin, "pig": draw_pig, "platypus": draw_platypus,
    "puffin": draw_puffin, "rabbit": draw_rabbit, "raccoon": draw_raccoon,
    "rhino": draw_rhino, "seal": draw_seal, "shark": draw_shark,
    "sheep": draw_sheep, "skunk": draw_skunk, "sloth": draw_sloth,
    "snake": draw_snake, "spider": draw_spider, "squirrel": draw_squirrel,
    "swan": draw_swan, "tiger": draw_tiger, "turtle": draw_turtle,
    "walrus": draw_walrus, "whale": draw_whale, "wolf": draw_wolf,
    "yak": draw_yak, "zebra": draw_zebra,
}

FRUIT_FUNCS = {
    "apple": draw_apple_100, "apricot": draw_apricot_100,
    "avocado": draw_avocado_100, "banana": draw_banana_100,
    "blackberry": draw_blackberry_100, "black_currant": draw_black_currant_100,
    "blood_orange": draw_blood_orange_100, "blueberry": draw_blueberry_100,
    "boysenberry": draw_boysenberry_100, "cantaloupe": draw_cantaloupe_100,
    "cherry": draw_cherry_100, "coconut": draw_coconut_100,
    "cranberry": draw_cranberry_100, "date": draw_date_100,
    "dragonfruit": draw_dragonfruit_100, "durian": draw_durian_100,
    "elderberry": draw_elderberry_100, "fig": draw_fig_100,
    "gooseberry": draw_gooseberry_100, "grape": draw_grape_100,
    "grapefruit": draw_grapefruit_100, "guava": draw_guava_100,
    "honeydew": draw_honeydew_100, "jackfruit": draw_jackfruit_100,
    "key_lime": draw_key_lime_100, "kiwi": draw_kiwi_100,
    "kumquat": draw_kumquat_100, "lemon": draw_lemon_100,
    "lime": draw_lime_100, "lychee": draw_lychee_100,
    "mango": draw_mango_100, "mangosteen": draw_mangosteen_100,
    "mulberry": draw_mulberry_100, "nectarine": draw_nectarine_100,
    "orange": draw_orange_100, "papaya": draw_papaya_100,
    "passionfruit": draw_passionfruit_100, "peach": draw_peach_100,
    "pear": draw_pear_100, "persimmon": draw_persimmon_100,
    "pineapple": draw_pineapple_100, "plum": draw_plum_100,
    "pomegranate": draw_pomegranate_100, "pomelo": draw_pomelo_100,
    "quince": draw_quince_100, "raspberry": draw_raspberry_100,
    "red_currant": draw_red_currant_100, "star_apple": draw_star_apple_100,
    "starfruit": draw_starfruit_100, "strawberry": draw_strawberry_100,
    "tangerine": draw_tangerine_100, "watermelon": draw_watermelon_100,
}

def main():
    print("=== Generating 100x100 animal sprites ===")
    ok_a = 0
    for name, fn in sorted(ANIMAL_FUNCS.items()):
        img = canvas()
        draw = ImageDraw.Draw(img)
        try:
            fn(draw)
            save(img, f"images/animals/{name}_100x100.png")
            ok_a += 1
        except Exception as e:
            print(f"  ERROR {name}: {e}")
    print(f"  Animals: {ok_a}/{len(ANIMAL_FUNCS)}")

    print("=== Generating 100x100 fruit sprites ===")
    ok_f = 0
    for name, fn in sorted(FRUIT_FUNCS.items()):
        img = canvas()
        draw = ImageDraw.Draw(img)
        try:
            fn(draw)
            save(img, f"images/fruits/{name}_100x100.png")
            ok_f += 1
        except Exception as e:
            print(f"  ERROR {name}: {e}")
    print(f"  Fruits: {ok_f}/{len(FRUIT_FUNCS)}")

    print("=== Checking and generating fallback 100x100 sprites ===")
    import glob
    fallback_count = 0
    for folder in ["animals", "fruits"]:
        for f50 in glob.glob(f"images/{folder}/*_50x50.png"):
            f100 = f50.replace("_50x50.png", "_100x100.png")
            if not os.path.exists(f100):
                try:
                    img = Image.open(f50).convert("RGBA")
                    img_100 = img.resize((100, 100), Image.Resampling.NEAREST)
                    img_100.save(f100)
                    fallback_count += 1
                except Exception as e:
                    print(f"  ERROR generating fallback for {f50}: {e}")
    print(f"  Generated {fallback_count} fallback 100x100 sprites.")
    print("Done!")

if __name__ == "__main__":
    main()
