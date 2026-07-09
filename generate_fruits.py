import os
from PIL import Image, ImageDraw

def create_sprite(filename, draw_func):
    img = Image.new("RGBA", (50, 50), (255, 255, 255, 0))
    draw = ImageDraw.Draw(img)
    draw_func(draw)
    img.save(filename)

# ── PALETTE (reused across functions; max 10 per sprite) ─────────────────────

# 1. APPLE – red body, dark-red shading, light highlight, stem, leaf, dark shadow
def draw_apple(draw):
    # body
    draw.ellipse([10, 14, 40, 44], fill=(210, 40, 40, 255))
    # shading (darker left half)
    draw.ellipse([10, 14, 24, 44], fill=(160, 20, 20, 255))
    # midtone join
    draw.ellipse([14, 16, 36, 42], fill=(220, 50, 50, 255))
    # highlight
    draw.ellipse([18, 17, 26, 27], fill=(255, 130, 120, 255))
    # top cleft
    draw.line([(25, 14), (25, 17)], fill=(140, 20, 20, 255), width=2)
    # stem
    draw.line([(25, 14), (25, 7)], fill=(100, 60, 25, 255), width=2)
    # leaf
    draw.polygon([(25, 9), (34, 4), (30, 11)], fill=(40, 155, 40, 255))
    draw.line([(25, 9), (30, 6)], fill=(25, 100, 25, 255), width=1)
    # bottom shadow
    draw.ellipse([14, 38, 36, 46], fill=(140, 20, 20, 255))

# 2. APRICOT
def draw_apricot(draw):
    draw.ellipse([10, 14, 40, 44], fill=(255, 155, 55, 255))
    draw.ellipse([10, 14, 25, 44], fill=(210, 110, 25, 255))   # shading
    draw.ellipse([14, 16, 36, 42], fill=(255, 175, 75, 255))
    draw.ellipse([17, 17, 27, 29], fill=(255, 220, 160, 255))  # highlight
    # crease line
    draw.line([(25, 14), (25, 44)], fill=(200, 100, 30, 255), width=1)
    # stem
    draw.line([(25, 14), (25, 7)], fill=(100, 60, 25, 255), width=2)
    draw.polygon([(25, 9), (31, 5), (28, 12)], fill=(50, 155, 50, 255))

# 3. AVOCADO
def draw_avocado(draw):
    # outer pear shape – dark green skin
    draw.ellipse([12, 10, 38, 46], fill=(30, 80, 25, 255))
    # lighter mid-section
    draw.ellipse([14, 12, 36, 44], fill=(60, 120, 40, 255))
    # pale flesh ring
    draw.ellipse([16, 16, 34, 42], fill=(190, 225, 90, 255))
    # yellow-green inner flesh
    draw.ellipse([18, 20, 32, 40], fill=(230, 248, 130, 255))
    # large brown seed
    draw.ellipse([20, 24, 30, 36], fill=(120, 68, 28, 255))
    draw.ellipse([22, 26, 28, 34], fill=(155, 100, 50, 255))   # seed highlight
    # stem nub
    draw.rectangle([23, 8, 27, 12], fill=(100, 60, 25, 255))

# 4. BANANA
def draw_banana(draw):
    # outer curved shape
    draw.arc([8, 8, 46, 46], 20, 165, fill=(240, 210, 25, 255), width=8)
    # inner lighter arc
    draw.arc([12, 12, 42, 42], 25, 158, fill=(255, 240, 80, 255), width=4)
    # ribs along curve
    draw.arc([15, 15, 39, 39], 40, 140, fill=(205, 175, 10, 255), width=1)
    # tip ends
    draw.polygon([(42, 22), (47, 18), (43, 15)], fill=(80, 65, 12, 255))
    draw.polygon([(10, 22), (6, 26), (11, 30)], fill=(65, 50, 8, 255))
    # shading on inner side
    draw.arc([10, 10, 44, 44], 20, 165, fill=(190, 155, 5, 255), width=2)

# 5. BLACKBERRY
def draw_blackberry(draw):
    # aggregate drupelets
    drupes = [(0,0),(-4,4),(4,4),(-6,10),(0,10),(6,10),(-4,16),(4,16),(0,20)]
    for ox, oy in drupes:
        draw.ellipse([22+ox, 14+oy, 28+ox, 20+oy], fill=(25, 10, 40, 255))
        draw.ellipse([23+ox, 15+oy, 26+ox, 18+oy], fill=(65, 30, 90, 255))
        draw.ellipse([23+ox, 15+oy, 25+ox, 17+oy], fill=(110, 60, 130, 255))
    # green sepals
    draw.polygon([(20, 14), (25, 8),  (28, 13)], fill=(40, 140, 40, 255))
    draw.polygon([(25, 13),(29,  8),  (32, 14)], fill=(30, 110, 30, 255))
    # stem
    draw.line([(25, 9), (25, 5)], fill=(80, 50, 20, 255), width=1)

# 6. BLUEBERRY
def draw_blueberry(draw):
    draw.ellipse([11, 16, 38, 44], fill=(38, 56, 145, 255))
    draw.ellipse([14, 19, 35, 41], fill=(58, 86, 195, 255))
    draw.ellipse([17, 20, 29, 32], fill=(110, 145, 230, 255))  # highlight
    # crown star at top
    draw.polygon([(21, 16), (25, 12), (29, 16)], fill=(20, 28, 80, 255))
    draw.polygon([(25, 16), (25, 20), (29, 16)], fill=(20, 28, 80, 255))
    # second berry
    draw.ellipse([24, 10, 44, 30], fill=(30, 44, 120, 255))
    draw.ellipse([27, 13, 41, 27], fill=(50, 72, 165, 255))
    draw.ellipse([29, 14, 36, 21], fill=(90, 120, 200, 255))
    draw.polygon([(32, 10), (37, 7), (38, 12)], fill=(18, 26, 70, 255))

# 7. CANTALOUPE
def draw_cantaloupe(draw):
    # whole melon half (left)
    draw.ellipse([5, 10, 34, 44], fill=(155, 135, 90, 255))
    draw.ellipse([7, 12, 32, 42], fill=(200, 180, 140, 255))
    # net pattern
    for y in range(14, 42, 5):
        draw.line([(9, y), (30, y)], fill=(175, 150, 110, 255), width=1)
    for x in range(10, 32, 5):
        draw.line([(x, 13), (x, 41)], fill=(175, 150, 110, 255), width=1)
    # cross-section showing orange flesh (right)
    draw.ellipse([28, 16, 46, 40], fill=(120, 90, 55, 255))
    draw.ellipse([30, 18, 44, 38], fill=(255, 138, 45, 255))
    draw.ellipse([33, 21, 41, 35], fill=(255, 180, 90, 255))
    # seed cavity
    draw.ellipse([35, 25, 39, 31], fill=(200, 100, 30, 255))

# 8. CHERRY
def draw_cherry(draw):
    # stems
    draw.line([(25, 6), (17, 24)], fill=(80, 130, 40, 255), width=2)
    draw.line([(25, 6), (33, 24)], fill=(80, 130, 40, 255), width=2)
    draw.arc([(17, 4), (33, 14)], 190, 350, fill=(80, 130, 40, 255), width=2)
    # left cherry body
    draw.ellipse([9, 22, 25, 38], fill=(170, 8, 25, 255))
    draw.ellipse([11, 24, 23, 36], fill=(210, 35, 55, 255))
    draw.ellipse([12, 24, 17, 29], fill=(255, 110, 120, 255))  # highlight
    # right cherry body
    draw.ellipse([25, 22, 41, 38], fill=(170, 8, 25, 255))
    draw.ellipse([27, 24, 39, 36], fill=(210, 35, 55, 255))
    draw.ellipse([28, 24, 33, 29], fill=(255, 110, 120, 255))  # highlight

# 9. COCONUT
def draw_coconut(draw):
    # whole coconut half-shell (left)
    draw.ellipse([5, 14, 33, 42], fill=(95, 60, 25, 255))
    draw.ellipse([7, 16, 31, 40], fill=(130, 88, 44, 255))
    # three eyes
    draw.ellipse([13, 22, 16, 25], fill=(50, 28, 8, 255))
    draw.ellipse([19, 22, 22, 25], fill=(50, 28, 8, 255))
    draw.ellipse([16, 27, 19, 30], fill=(50, 28, 8, 255))
    # halved coconut (right) showing white flesh
    draw.ellipse([23, 18, 46, 44], fill=(95, 60, 25, 255))
    draw.ellipse([25, 20, 44, 42], fill=(245, 242, 230, 255))
    draw.ellipse([28, 23, 41, 39], fill=(245, 242, 230, 255))
    # hollow center (water cavity)
    draw.ellipse([31, 27, 38, 35], fill=(210, 235, 255, 255))

# 10. CRANBERRY
def draw_cranberry(draw):
    # three berries clustered
    draw.ellipse([7, 22, 24, 38], fill=(155, 8, 35, 255))
    draw.ellipse([9, 24, 22, 36], fill=(195, 20, 50, 255))
    draw.ellipse([11, 24, 17, 30], fill=(240, 80, 100, 255))  # highlight
    draw.ellipse([20, 16, 36, 32], fill=(140, 5, 28, 255))
    draw.ellipse([22, 18, 34, 30], fill=(185, 16, 45, 255))
    draw.ellipse([23, 18, 28, 23], fill=(240, 80, 100, 255))
    draw.ellipse([16, 28, 36, 46], fill=(175, 15, 42, 255))
    draw.ellipse([18, 30, 34, 44], fill=(215, 35, 60, 255))
    draw.ellipse([19, 30, 25, 36], fill=(240, 80, 100, 255))
    # green sepals
    draw.polygon([(12, 22), (8, 16), (16, 20)], fill=(45, 135, 45, 255))

# 11. DATE
def draw_date(draw):
    # three dates clustered on a stem
    draw.line([(25, 6), (15, 16)], fill=(90, 55, 20, 255), width=2)
    draw.line([(25, 6), (25, 16)], fill=(90, 55, 20, 255), width=2)
    draw.line([(25, 6), (35, 14)], fill=(90, 55, 20, 255), width=2)
    # date 1 (left)
    draw.rounded_rectangle([10, 14, 20, 34], radius=4, fill=(85, 44, 18, 255))
    draw.rounded_rectangle([11, 15, 19, 28], radius=3, fill=(115, 66, 30, 255))
    draw.ellipse([12, 15, 16, 20], fill=(155, 100, 52, 255))
    # date 2 (center)
    draw.rounded_rectangle([20, 14, 30, 38], radius=4, fill=(70, 33, 12, 255))
    draw.rounded_rectangle([21, 15, 29, 30], radius=3, fill=(100, 55, 24, 255))
    draw.ellipse([22, 15, 26, 21], fill=(140, 85, 42, 255))
    # date 3 (right)
    draw.rounded_rectangle([30, 12, 40, 32], radius=4, fill=(80, 40, 15, 255))
    draw.rounded_rectangle([31, 13, 39, 25], radius=3, fill=(110, 62, 27, 255))
    draw.ellipse([32, 13, 36, 19], fill=(145, 92, 46, 255))

# 12. DRAGONFRUIT
def draw_dragonfruit(draw):
    # main body – vivid pink oval
    draw.ellipse([8, 10, 42, 44], fill=(230, 40, 110, 255))
    draw.ellipse([10, 12, 40, 42], fill=(245, 65, 130, 255))
    # scale flaps around perimeter
    for (sx, sy, ex, ey) in [
        (8,24,2,18),(8,24,2,30),(42,24,48,18),(42,24,48,30),
        (18,10,14,4),(28,10,24,4),(18,44,14,50),(28,44,24,50)
    ]:
        draw.polygon([(sx,sy),(ex,ey-3),(ex+4,ey+3)], fill=(60, 180, 60, 255))
    # white flesh cross-section (right half)
    draw.ellipse([20, 18, 44, 42], fill=(230, 40, 110, 255))
    draw.ellipse([22, 20, 42, 40], fill=(250, 250, 250, 255))
    # seeds scattered in flesh
    for (px, py) in [(28,26),(32,24),(36,28),(30,33),(34,35),(38,32),(26,32)]:
        draw.ellipse([px-1, py-1, px+1, py+1], fill=(20, 15, 20, 255))

# 13. DURIAN
def draw_durian(draw):
    # body
    draw.ellipse([8, 12, 42, 44], fill=(125, 138, 48, 255))
    draw.ellipse([10, 14, 40, 42], fill=(155, 168, 65, 255))
    # spines all around
    spine_pts = [
        (25,12),(18,13),(32,13),(12,20),(38,20),(10,28),(40,28),
        (13,36),(37,36),(20,42),(30,42),(25,44)
    ]
    for sx, sy in spine_pts:
        dx, dy = sx-25, sy-28
        draw.polygon([(sx,sy),(sx-3+dy//6,sy-4-abs(dx)//4),(sx+3-dy//6,sy-4-abs(dx)//4)],
                     fill=(90, 105, 28, 255))
    # flesh hint at bottom opening
    draw.ellipse([19, 38, 31, 46], fill=(255, 225, 130, 255))
    # stem
    draw.line([(25, 12), (25, 5)], fill=(88, 58, 18, 255), width=3)

# 14. FIG
def draw_fig(draw):
    # pear/teardrop body
    draw.ellipse([14, 8, 36, 32], fill=(90, 45, 95, 255))   # top narrow
    draw.ellipse([10, 22, 40, 46], fill=(110, 55, 115, 255)) # bottom wide
    draw.ellipse([12, 24, 38, 44], fill=(130, 70, 135, 255)) # lighter
    # highlight
    draw.ellipse([14, 26, 22, 36], fill=(175, 110, 180, 255))
    # stem
    draw.line([(25, 8), (25, 3)], fill=(80, 50, 18, 255), width=2)
    # eye / ostiole at bottom
    draw.ellipse([21, 41, 29, 46], fill=(80, 35, 85, 255))
    draw.ellipse([23, 42, 27, 45], fill=(210, 145, 165, 255))
    # cross-section seeds hint
    draw.ellipse([19, 36, 23, 40], fill=(195, 110, 140, 255))
    draw.ellipse([26, 35, 30, 39], fill=(195, 110, 140, 255))

# 15. GRAPE
def draw_grape(draw):
    offsets = [(21,14),(29,14),(17,20),(25,20),(33,20),(21,26),(29,26),(17,32),(25,32),(21,38)]
    for gx, gy in offsets:
        draw.ellipse([gx, gy, gx+8, gy+8],   fill=(100, 45, 132, 255))
        draw.ellipse([gx+1, gy+1, gx+7, gy+7], fill=(130, 68, 172, 255))
        draw.ellipse([gx+1, gy+1, gx+4, gy+4], fill=(175, 120, 205, 255))  # highlight
    # stem & tendril
    draw.line([(25, 6), (25, 14)], fill=(90, 130, 40, 255), width=2)
    draw.arc([(22, 4), (30, 10)], 0, 360, fill=(90, 130, 40, 255), width=1)

# 16. GRAPEFRUIT
def draw_grapefruit(draw):
    # whole fruit (left)
    draw.ellipse([4, 10, 36, 44], fill=(240, 172, 50, 255))
    draw.ellipse([6, 12, 34, 42], fill=(255, 195, 75, 255))
    draw.ellipse([14, 18, 28, 34], fill=(255, 220, 130, 255))  # specular
    # cross-section (right) – pink flesh
    draw.ellipse([26, 20, 48, 44], fill=(230, 80, 50, 255))
    draw.ellipse([28, 22, 46, 42], fill=(250, 120, 90, 255))
    # segment lines
    draw.line([(37, 22), (37, 42)], fill=(255, 255, 255, 255), width=1)
    draw.line([(28, 32), (46, 32)], fill=(255, 255, 255, 255), width=1)
    draw.line([(29, 24), (45, 40)], fill=(255, 255, 255, 255), width=1)
    draw.line([(29, 40), (45, 24)], fill=(255, 255, 255, 255), width=1)

# 17. GUAVA
def draw_guava(draw):
    # whole fruit body
    draw.ellipse([6, 12, 36, 42], fill=(110, 175, 72, 255))
    draw.ellipse([8, 14, 34, 40], fill=(145, 205, 100, 255))
    draw.ellipse([10, 15, 24, 30], fill=(185, 230, 145, 255))   # highlight
    # crown tip at top-right
    draw.line([(33, 12), (33, 8)], fill=(70, 125, 40, 255), width=2)
    draw.ellipse([30, 7, 36, 11], fill=(70, 125, 40, 255))
    # cross-section (right) – pink flesh
    draw.ellipse([28, 20, 46, 42], fill=(110, 175, 72, 255))
    draw.ellipse([30, 22, 44, 40], fill=(240, 115, 125, 255))
    draw.ellipse([33, 25, 41, 37], fill=(255, 165, 172, 255))
    # seeds
    for (px, py) in [(34,28),(38,32),(36,36)]:
        draw.ellipse([px-1, py-1, px+1, py+1], fill=(180, 60, 50, 255))

# 18. HONEYDEW
def draw_honeydew(draw):
    # whole melon (left)
    draw.ellipse([4, 10, 36, 44], fill=(200, 228, 165, 255))
    draw.ellipse([6, 12, 34, 42], fill=(220, 245, 190, 255))
    draw.ellipse([10, 15, 26, 32], fill=(240, 255, 215, 255))  # highlight
    # cross-section (right) – pale green flesh
    draw.ellipse([27, 18, 47, 42], fill=(180, 220, 145, 255))
    draw.ellipse([29, 20, 45, 40], fill=(155, 210, 120, 255))
    # seed cavity
    draw.ellipse([33, 25, 41, 35], fill=(210, 240, 175, 255))
    draw.ellipse([35, 27, 39, 33], fill=(230, 248, 200, 255))
    # seeds
    for (px, py) in [(34,27),(38,28),(36,31)]:
        draw.ellipse([px, py, px+2, py+3], fill=(190, 170, 80, 255))

# 19. JACKFRUIT
def draw_jackfruit(draw):
    # large bumpy green body
    draw.ellipse([8, 10, 42, 46], fill=(95, 115, 38, 255))
    draw.ellipse([10, 12, 40, 44], fill=(120, 145, 55, 255))
    # hexagonal bumps grid
    for x in range(13, 40, 6):
        for y in range(14, 44, 6):
            draw.ellipse([x-2, y-2, x+2, y+2], fill=(80, 100, 30, 255))
            draw.ellipse([x-1, y-1, x+1, y+1], fill=(145, 172, 68, 255))
    # stem
    draw.line([(25, 10), (25, 4)], fill=(85, 55, 18, 255), width=3)
    # exposed pod/flesh highlight
    draw.ellipse([29, 22, 38, 32], fill=(255, 215, 70, 255))

# 20. KIWI
def draw_kiwi(draw):
    # whole kiwi (left) – fuzzy brown skin
    draw.ellipse([5, 14, 30, 40], fill=(100, 72, 40, 255))
    draw.ellipse([7, 16, 28, 38], fill=(125, 90, 52, 255))
    # fuzz marks
    for (px, py) in [(10,20),(14,17),(20,16),(24,19),(26,26),(22,32),(15,34),(9,30)]:
        draw.line([(px, py), (px+2, py-2)], fill=(80, 55, 28, 255), width=1)
    # cross-section (right) – green flesh
    draw.ellipse([22, 18, 46, 44], fill=(100, 72, 40, 255))
    draw.ellipse([24, 20, 44, 42], fill=(65, 170, 50, 255))
    draw.ellipse([27, 23, 41, 39], fill=(200, 238, 110, 255))
    draw.ellipse([32, 28, 36, 33], fill=(240, 252, 185, 255))  # core
    # seeds radiating from core
    for (px, py) in [(28,24),(32,22),(36,24),(39,28),(39,33),(36,37),(32,39),(28,37),(26,32)]:
        draw.ellipse([px-1, py-1, px+1, py+1], fill=(20, 18, 14, 255))

# 21. KUMQUAT
def draw_kumquat(draw):
    # two kumquats
    draw.ellipse([6, 22, 23, 40], fill=(250, 132, 12, 255))
    draw.ellipse([8, 24, 21, 38], fill=(255, 168, 55, 255))
    draw.ellipse([9, 24, 15, 31], fill=(255, 215, 130, 255))
    draw.ellipse([28, 16, 46, 36], fill=(245, 122, 8, 255))
    draw.ellipse([30, 18, 44, 34], fill=(255, 158, 48, 255))
    draw.ellipse([31, 18, 37, 25], fill=(255, 210, 125, 255))
    # stems & leaves
    draw.line([(14, 22), (14, 17)], fill=(85, 55, 18, 255), width=1)
    draw.line([(37, 16), (37, 11)], fill=(85, 55, 18, 255), width=1)
    draw.polygon([(14, 18), (20, 13), (16, 10)], fill=(40, 145, 40, 255))
    draw.polygon([(37, 12), (43, 7), (39, 5)], fill=(40, 145, 40, 255))

# 22. LEMON
def draw_lemon(draw):
    # body – bright yellow oblong
    draw.ellipse([8, 16, 42, 40], fill=(245, 218, 32, 255))
    draw.ellipse([10, 18, 40, 38], fill=(255, 242, 80, 255))
    # highlight top-left
    draw.ellipse([13, 19, 26, 30], fill=(255, 252, 175, 255))
    # nipple tips
    draw.ellipse([6, 23, 11, 29], fill=(220, 195, 20, 255))
    draw.ellipse([39, 23, 44, 29], fill=(220, 195, 20, 255))
    # stem
    draw.line([(25, 16), (25, 10)], fill=(85, 55, 18, 255), width=2)
    draw.polygon([(25, 11), (32, 6), (28, 13)], fill=(45, 145, 45, 255))

# 23. LIME
def draw_lime(draw):
    draw.ellipse([8, 16, 42, 40], fill=(28, 145, 38, 255))
    draw.ellipse([10, 18, 40, 38], fill=(55, 190, 68, 255))
    draw.ellipse([13, 19, 26, 30], fill=(110, 225, 115, 255))   # highlight
    # nipple tips
    draw.ellipse([6, 23, 11, 29], fill=(22, 115, 30, 255))
    draw.ellipse([39, 23, 44, 29], fill=(22, 115, 30, 255))
    # stem
    draw.line([(25, 16), (25, 10)], fill=(85, 55, 18, 255), width=2)
    draw.polygon([(25, 11), (32, 6), (28, 13)], fill=(25, 110, 30, 255))

# 24. LYCHEE
def draw_lychee(draw):
    # red bumpy skin (left fruit)
    draw.ellipse([5, 18, 28, 42], fill=(195, 35, 55, 255))
    draw.ellipse([7, 20, 26, 40], fill=(220, 55, 75, 255))
    # bumps on skin
    for (px, py) in [(10,22),(16,20),(22,22),(8,30),(14,28),(20,30),(11,36),(17,35)]:
        draw.ellipse([px, py, px+3, py+3], fill=(170, 20, 40, 255))
    # peeled fruit (right) – white translucent flesh
    draw.ellipse([22, 14, 46, 40], fill=(195, 35, 55, 255))
    draw.ellipse([24, 16, 44, 38], fill=(245, 242, 248, 255))
    draw.ellipse([27, 19, 41, 35], fill=(255, 252, 255, 255))
    # dark seed showing through
    draw.ellipse([31, 23, 38, 32], fill=(110, 68, 38, 255))
    draw.ellipse([33, 25, 36, 30], fill=(145, 98, 58, 255))

# 25. MANGO
def draw_mango(draw):
    # body – kidney shape
    draw.ellipse([10, 14, 40, 44], fill=(230, 168, 38, 255))
    # red blush on top
    draw.ellipse([10, 14, 32, 30], fill=(215, 68, 38, 255))
    # yellow-green tip area
    draw.ellipse([26, 30, 40, 44], fill=(110, 188, 45, 255))
    # lighter golden highlight
    draw.ellipse([15, 16, 28, 30], fill=(255, 225, 120, 255))
    # stem
    draw.line([(25, 14), (25, 7)], fill=(95, 60, 22, 255), width=2)
    draw.polygon([(25, 8), (33, 3), (29, 11)], fill=(38, 145, 38, 255))

# 26. MULBERRY
def draw_mulberry(draw):
    drupes = [(0,0),(-3,3),(3,3),(-4,8),(0,8),(4,8),(-4,13),(0,13),(4,13),(-3,18),(3,18),(0,22)]
    for ox, oy in drupes:
        draw.ellipse([22+ox, 12+oy, 28+ox, 18+oy], fill=(22, 8, 35, 255))
        draw.ellipse([23+ox, 13+oy, 27+ox, 17+oy], fill=(60, 20, 80, 255))
        draw.ellipse([23+ox, 13+oy, 25+ox, 15+oy], fill=(105, 55, 125, 255))
    # sepals
    draw.polygon([(21, 12), (25, 6), (28, 11)], fill=(48, 138, 48, 255))
    draw.line([(25, 7), (25, 3)], fill=(80, 50, 18, 255), width=1)

# 27. NECTARINE
def draw_nectarine(draw):
    draw.ellipse([10, 14, 40, 44], fill=(242, 168, 35, 255))
    # deep red blush on left
    draw.ellipse([10, 14, 28, 38], fill=(218, 38, 38, 255))
    # mid-join
    draw.ellipse([14, 16, 36, 42], fill=(248, 185, 60, 255))
    # highlight
    draw.ellipse([17, 17, 26, 27], fill=(255, 235, 160, 255))
    # crease line
    draw.line([(25, 14), (25, 44)], fill=(200, 95, 28, 255), width=1)
    # stem
    draw.line([(25, 14), (25, 7)], fill=(95, 60, 22, 255), width=2)

# 28. ORANGE
def draw_orange(draw):
    draw.ellipse([10, 14, 40, 44], fill=(242, 122, 25, 255))
    draw.ellipse([12, 16, 38, 42], fill=(255, 148, 48, 255))
    # peel texture lines
    for i in range(3):
        draw.arc([12+i*2, 16+i*2, 38-i*2, 42-i*2], 200, 330, fill=(218, 102, 12, 255), width=1)
    # highlight
    draw.ellipse([15, 17, 26, 28], fill=(255, 210, 120, 255))
    # stem
    draw.line([(25, 14), (25, 7)], fill=(88, 55, 18, 255), width=2)
    draw.polygon([(25, 8), (32, 3), (29, 11)], fill=(45, 148, 45, 255))

# 29. PAPAYA
def draw_papaya(draw):
    # elongated body
    draw.polygon([(25, 10), (12, 30), (14, 46), (36, 46), (38, 30)], fill=(232, 152, 38, 255))
    draw.ellipse([12, 26, 38, 46], fill=(232, 152, 38, 255))
    # orange blush
    draw.ellipse([14, 12, 36, 42], fill=(245, 125, 35, 255))
    # highlight
    draw.ellipse([16, 14, 24, 28], fill=(255, 200, 120, 255))
    # cross section seeds
    draw.ellipse([20, 32, 30, 42], fill=(35, 28, 28, 255))
    for (px, py) in [(22,34),(26,33),(28,37),(24,40)]:
        draw.ellipse([px-1, py-1, px+1, py+1], fill=(20, 15, 15, 255))
    # stem
    draw.line([(25, 10), (25, 4)], fill=(88, 55, 18, 255), width=2)

# 30. PASSIONFRUIT
def draw_passionfruit(draw):
    # dark purple wrinkled skin
    draw.ellipse([6, 14, 44, 46], fill=(75, 35, 78, 255))
    draw.ellipse([8, 16, 42, 44], fill=(95, 50, 98, 255))
    # wrinkle marks
    for (x1,y1,x2,y2) in [(12,20,10,26),(38,20,40,26),(10,34,12,40),(38,34,36,40),(20,16,18,20),(30,16,32,20)]:
        draw.line([(x1,y1),(x2,y2)], fill=(60, 28, 62, 255), width=1)
    # cross-section (right half) yellow arils
    draw.ellipse([24, 18, 47, 43], fill=(75, 35, 78, 255))
    draw.ellipse([26, 20, 45, 41], fill=(235, 200, 45, 255))
    draw.ellipse([28, 22, 43, 39], fill=(248, 220, 70, 255))
    # arils and seeds
    for (px, py) in [(30,26),(35,24),(39,28),(31,33),(36,35),(40,33)]:
        draw.ellipse([px-2, py-2, px+2, py+2], fill=(38, 48, 8, 255))
        draw.ellipse([px-1, py-1, px+1, py+1], fill=(55, 68, 12, 255))

# 31. PEACH
def draw_peach(draw):
    draw.ellipse([10, 14, 40, 44], fill=(255, 168, 102, 255))
    # rosy blush left side
    draw.ellipse([10, 14, 28, 38], fill=(238, 75, 85, 255))
    # midtone
    draw.ellipse([14, 16, 36, 42], fill=(255, 185, 118, 255))
    # highlight
    draw.ellipse([17, 17, 26, 27], fill=(255, 235, 195, 255))
    # crease
    draw.line([(25, 14), (25, 44)], fill=(205, 95, 78, 255), width=1)
    # stem
    draw.line([(25, 14), (25, 7)], fill=(95, 60, 22, 255), width=2)
    draw.polygon([(25, 8), (32, 3), (28, 12)], fill=(65, 158, 60, 255))

# 32. PEAR
def draw_pear(draw):
    # bottom bulb
    draw.ellipse([11, 26, 39, 46], fill=(148, 188, 55, 255))
    draw.ellipse([13, 28, 37, 44], fill=(175, 215, 78, 255))
    # top narrow section
    draw.ellipse([16, 12, 34, 34], fill=(148, 188, 55, 255))
    draw.ellipse([18, 14, 32, 32], fill=(175, 215, 78, 255))
    # highlight
    draw.ellipse([19, 15, 27, 27], fill=(220, 248, 138, 255))
    # yellow blush patch
    draw.ellipse([26, 32, 36, 42], fill=(238, 228, 55, 255))
    # stem
    draw.line([(25, 12), (25, 5)], fill=(95, 60, 22, 255), width=2)
    draw.polygon([(25, 6), (31, 2), (28, 9)], fill=(48, 140, 48, 255))

# 33. PERSIMMON
def draw_persimmon(draw):
    # squat round orange fruit
    draw.ellipse([10, 16, 40, 44], fill=(252, 105, 18, 255))
    draw.ellipse([12, 18, 38, 42], fill=(255, 138, 48, 255))
    draw.ellipse([14, 18, 26, 30], fill=(255, 200, 130, 255))  # highlight
    # four-pointed calyx/crown
    draw.polygon([(17, 16), (22, 11), (25, 16)], fill=(65, 108, 38, 255))
    draw.polygon([(25, 16), (30, 11), (33, 16)], fill=(55, 95, 32, 255))
    draw.polygon([(20, 14), (25, 10), (30, 14)], fill=(72, 118, 42, 255))
    draw.polygon([(25, 16), (25, 11), (28, 15)], fill=(58, 102, 36, 255))
    draw.ellipse([23, 13, 27, 17], fill=(80, 52, 18, 255))    # stem nub

# 34. PINEAPPLE
def draw_pineapple(draw):
    # body
    draw.ellipse([14, 20, 36, 46], fill=(225, 168, 38, 255))
    # diamond scale grid
    for y in range(22, 46, 5):
        for x in range(15, 36, 5):
            draw.polygon([(x+2,y),(x+5,y+2),(x+2,y+5),(x-1,y+2)], fill=(185, 128, 18, 255))
    # crown leaves
    for (fx, lean) in [(17,-3),(20,-2),(23,-1),(25,0),(27,1),(30,2),(33,3)]:
        draw.line([(fx, 20), (fx+lean, 5)], fill=(38, 138, 45, 255), width=2)
    draw.polygon([(19, 20),(25, 4),(31, 20)], fill=(45, 155, 52, 255))

# 35. PLUM
def draw_plum(draw):
    draw.ellipse([10, 14, 40, 44], fill=(85, 38, 105, 255))
    draw.ellipse([10, 14, 26, 38], fill=(62, 18, 82, 255))     # shading
    draw.ellipse([14, 16, 36, 42], fill=(108, 52, 130, 255))
    draw.ellipse([16, 17, 25, 28], fill=(160, 105, 185, 255))  # highlight
    # waxy bloom line
    draw.line([(25, 14), (25, 44)], fill=(62, 18, 82, 255), width=1)
    # stem
    draw.line([(25, 14), (25, 7)], fill=(95, 60, 22, 255), width=2)

# 36. POMEGRANATE
def draw_pomegranate(draw):
    draw.ellipse([10, 14, 40, 44], fill=(192, 28, 42, 255))
    draw.ellipse([12, 16, 38, 42], fill=(218, 48, 62, 255))
    draw.ellipse([14, 16, 24, 28], fill=(255, 112, 118, 255))  # highlight
    # crown spikes
    draw.polygon([(20, 14), (18, 7), (24, 13)], fill=(185, 24, 38, 255))
    draw.polygon([(25, 14), (25, 6), (28, 13)], fill=(170, 18, 32, 255))
    draw.polygon([(30, 14), (32, 7), (26, 13)], fill=(185, 24, 38, 255))
    # cross-section arils
    draw.ellipse([24, 26, 44, 46], fill=(192, 28, 42, 255))
    draw.ellipse([26, 28, 42, 44], fill=(248, 215, 175, 255))
    for (px, py) in [(30,31),(35,30),(39,33),(31,37),(36,37)]:
        draw.ellipse([px-2, py-2, px+2, py+2], fill=(215, 8, 32, 255))
        draw.ellipse([px-1, py-1, px+1, py+1], fill=(245, 90, 105, 255))

# 37. POMELO
def draw_pomelo(draw):
    # large thick-skinned fruit
    draw.ellipse([5, 10, 45, 46], fill=(205, 220, 75, 255))
    draw.ellipse([7, 12, 43, 44], fill=(228, 242, 108, 255))
    draw.ellipse([10, 14, 32, 36], fill=(245, 255, 165, 255))  # highlight
    # hint of white pith thickness
    draw.ellipse([14, 18, 36, 40], fill=(248, 255, 210, 255))
    draw.ellipse([17, 21, 33, 37], fill=(235, 242, 178, 255))
    # stem
    draw.line([(25, 10), (25, 4)], fill=(88, 55, 18, 255), width=2)

# 38. QUINCE
def draw_quince(draw):
    # lumpy pear/apple shape
    draw.ellipse([12, 8, 36, 34], fill=(228, 208, 48, 255))
    draw.ellipse([10, 24, 40, 46], fill=(232, 212, 52, 255))
    draw.ellipse([12, 26, 38, 44], fill=(245, 230, 85, 255))
    draw.ellipse([14, 14, 24, 24], fill=(255, 248, 165, 255))  # highlight
    # fuzz marks on skin
    for (px, py) in [(18,12),(28,10),(32,18),(14,30),(36,32),(22,40)]:
        draw.line([(px, py), (px+2, py-2)], fill=(195, 175, 30, 255), width=1)
    # stem
    draw.line([(25, 8), (25, 2)], fill=(88, 55, 18, 255), width=2)

# 39. RASPBERRY
def draw_raspberry(draw):
    drupes = [(0,0),(-3,3),(3,3),(-5,7),(0,7),(5,7),(-4,12),(4,12),(-2,17),(2,17),(0,21)]
    for ox, oy in drupes:
        draw.ellipse([22+ox, 14+oy, 28+ox, 20+oy], fill=(222, 38, 80, 255))
        draw.ellipse([23+ox, 15+oy, 27+ox, 19+oy], fill=(248, 72, 112, 255))
        draw.ellipse([23+ox, 15+oy, 25+ox, 17+oy], fill=(255, 155, 175, 255))
    # sepals
    draw.polygon([(19, 14), (25, 8), (30, 13)], fill=(42, 148, 42, 255))
    draw.polygon([(25, 13),(30,8),(33,14)], fill=(35, 118, 35, 255))
    draw.line([(25, 8), (25, 4)], fill=(78, 48, 18, 255), width=1)

# 40. STARFRUIT
def draw_starfruit(draw):
    # 5-pointed star cross-section
    draw.polygon([(25,8),(29,19),(40,19),(31,26),(34,37),(25,30),(16,37),(19,26),(10,19),(21,19)],
                 fill=(238, 215, 25, 255))
    # inner lighter star
    draw.polygon([(25,12),(28,20),(37,20),(30,25),(33,34),(25,28),(17,34),(20,25),(13,20),(22,20)],
                 fill=(252, 238, 78, 255))
    # rib shading lines
    draw.line([(25, 8), (25, 30)],  fill=(198, 175, 8, 255), width=1)
    draw.line([(10, 19), (40, 19)], fill=(198, 175, 8, 255), width=1)
    draw.line([(16, 37), (34, 19)], fill=(198, 175, 8, 255), width=1)
    draw.line([(34, 37), (16, 19)], fill=(198, 175, 8, 255), width=1)
    # stem end
    draw.line([(25, 8), (25, 4)],   fill=(88, 55, 18, 255), width=2)

# 41. STRAWBERRY
def draw_strawberry(draw):
    # body
    draw.polygon([(25, 46), (11, 22), (18, 14), (32, 14), (39, 22)], fill=(215, 28, 28, 255))
    draw.ellipse([11, 14, 39, 36], fill=(215, 28, 28, 255))
    draw.ellipse([13, 16, 37, 34], fill=(238, 55, 55, 255))
    # highlight
    draw.ellipse([15, 17, 23, 28], fill=(255, 120, 115, 255))
    # green calyx leaves
    draw.polygon([(16, 14), (25, 22), (34, 14)], fill=(45, 145, 45, 255))
    draw.polygon([(12, 14), (25, 8),  (38, 14)], fill=(35, 118, 35, 255))
    draw.polygon([(19, 12), (25, 6),  (31, 12)], fill=(52, 158, 52, 255))
    # seeds (achenes)
    seeds = [(17,22),(23,20),(29,22),(35,22),(15,29),(21,28),(27,29),(33,28),(19,36),(25,35),(31,36),(24,43)]
    for sx, sy in seeds:
        draw.ellipse([sx-1, sy-1, sx+1, sy+2], fill=(238, 238, 95, 255))

# 42. TANGERINE
def draw_tangerine(draw):
    draw.ellipse([8, 16, 42, 44], fill=(240, 115, 18, 255))
    draw.ellipse([10, 18, 40, 42], fill=(255, 142, 42, 255))
    draw.ellipse([12, 18, 28, 32], fill=(255, 205, 115, 255))  # highlight
    # easy-peel segment seam lines hinting
    for a in [30, 90, 150, 210, 270, 330]:
        import math
        x = int(25 + 14 * math.cos(math.radians(a)))
        y = int(30 + 12 * math.sin(math.radians(a)))
        draw.line([(25, 30), (x, y)], fill=(215, 95, 10, 255), width=1)
    # stem & leaf
    draw.line([(25, 16), (25, 9)], fill=(88, 55, 18, 255), width=2)
    draw.polygon([(25, 10), (33, 5), (28, 12)], fill=(45, 142, 45, 255))

# 43. WATERMELON
def draw_watermelon(draw):
    # slice shape
    draw.polygon([(5, 44), (25, 8), (45, 44)], fill=(38, 118, 45, 255))
    # white rind ring
    draw.polygon([(8, 44), (25, 12), (42, 44)], fill=(248, 248, 248, 255))
    # red flesh
    draw.polygon([(11, 44), (25, 16), (39, 44)], fill=(230, 40, 45, 255))
    draw.polygon([(13, 44), (25, 20), (37, 44)], fill=(248, 68, 72, 255))
    # highlight on flesh
    draw.polygon([(15, 44), (22, 24), (28, 44)], fill=(255, 125, 118, 255))
    # seeds
    for (px, py) in [(22,32),(28,30),(32,36),(18,36),(25,40),(30,43)]:
        draw.ellipse([px-2, py-1, px+2, py+3], fill=(18, 15, 18, 255))
    # green stripe on rind
    draw.line([(5, 44), (25, 8)],  fill=(28, 88, 32, 255), width=2)
    draw.line([(45, 44), (25, 8)], fill=(28, 88, 32, 255), width=2)

# 44. STAR APPLE
def draw_star_apple(draw):
    # round dark purple body
    draw.ellipse([7, 12, 43, 46], fill=(72, 44, 95, 255))
    draw.ellipse([9, 14, 41, 44], fill=(95, 62, 120, 255))
    draw.ellipse([11, 15, 25, 30], fill=(138, 95, 162, 255))   # highlight
    # cross-section star pattern (right)
    draw.ellipse([25, 18, 47, 42], fill=(72, 44, 95, 255))
    draw.ellipse([27, 20, 45, 40], fill=(240, 238, 242, 255))  # white flesh
    # star segments (5 lobes)
    import math
    for i in range(5):
        a = math.radians(i * 72 - 90)
        sx = int(36 + 8 * math.cos(a))
        sy = int(30 + 8 * math.sin(a))
        draw.line([(36, 30), (sx, sy)], fill=(118, 75, 142, 255), width=2)
    draw.ellipse([33, 27, 39, 33], fill=(118, 75, 142, 255))   # center

# 45. BOYSENBERRY
def draw_boysenberry(draw):
    drupes = [(0,0),(-3,3),(3,3),(-5,7),(0,7),(5,7),(-4,12),(4,12),(-2,17),(2,17),(0,21)]
    for ox, oy in drupes:
        draw.ellipse([22+ox, 14+oy, 28+ox, 20+oy], fill=(92, 22, 55, 255))
        draw.ellipse([23+ox, 15+oy, 27+ox, 19+oy], fill=(125, 42, 85, 255))
        draw.ellipse([23+ox, 15+oy, 25+ox, 17+oy], fill=(175, 88, 130, 255))
    draw.polygon([(19, 14), (25, 8), (30, 13)], fill=(42, 138, 42, 255))
    draw.polygon([(25, 13),(29, 8),(33,14)],    fill=(35, 112, 35, 255))
    draw.line([(25, 8), (25, 4)], fill=(75, 46, 16, 255), width=1)

# 46. ELDERBERRY
def draw_elderberry(draw):
    # branching stem with clusters
    draw.line([(25, 8), (14, 22)], fill=(148, 35, 45, 255), width=2)
    draw.line([(25, 8), (25, 22)], fill=(148, 35, 45, 255), width=2)
    draw.line([(25, 8), (36, 22)], fill=(148, 35, 45, 255), width=2)
    draw.line([(14, 22), (10, 32)], fill=(148, 35, 45, 255), width=1)
    draw.line([(14, 22), (18, 32)], fill=(148, 35, 45, 255), width=1)
    draw.line([(36, 22), (32, 32)], fill=(148, 35, 45, 255), width=1)
    draw.line([(36, 22), (40, 32)], fill=(148, 35, 45, 255), width=1)
    # berries
    for (bx, by) in [(10,30),(15,33),(19,30),(22,34),(25,30),(29,34),(32,30),(37,33),(41,30)]:
        draw.ellipse([bx-3, by-3, bx+3, by+3], fill=(12, 8, 18, 255))
        draw.ellipse([bx-2, by-2, bx, by],      fill=(55, 38, 72, 255))
    # leaf pair
    draw.polygon([(16, 8), (8, 2), (12, 10)],  fill=(38, 128, 38, 255))
    draw.polygon([(34, 8), (42, 2), (38, 10)], fill=(38, 128, 38, 255))

# 47. GOOSEBERRY
def draw_gooseberry(draw):
    # translucent green veined berry
    draw.ellipse([10, 14, 40, 44], fill=(132, 202, 102, 255))
    draw.ellipse([12, 16, 38, 42], fill=(165, 228, 135, 255))
    draw.ellipse([14, 17, 26, 30], fill=(205, 248, 178, 255))  # highlight
    # vein lines (distinctive gooseberry feature)
    draw.line([(25, 14), (25, 44)], fill=(100, 168, 72, 255), width=1)
    draw.line([(11, 29), (39, 29)], fill=(100, 168, 72, 255), width=1)
    draw.line([(14, 18), (36, 40)], fill=(100, 168, 72, 255), width=1)
    draw.line([(36, 18), (14, 40)], fill=(100, 168, 72, 255), width=1)
    # tiny stem end and flower remnant
    draw.line([(25, 44), (25, 47)], fill=(88, 55, 18, 255), width=1)
    draw.ellipse([23, 47, 27, 50],  fill=(80, 148, 58, 255))
    draw.line([(25, 14), (25, 10)], fill=(88, 55, 18, 255), width=1)

# 48. KEY LIME
def draw_key_lime(draw):
    # small round yellow-green
    draw.ellipse([12, 16, 38, 42], fill=(175, 205, 45, 255))
    draw.ellipse([14, 18, 36, 40], fill=(205, 232, 78, 255))
    draw.ellipse([15, 18, 25, 28], fill=(235, 252, 148, 255))  # highlight
    # small nipple tips
    draw.ellipse([8, 24, 13, 30],  fill=(155, 182, 32, 255))
    draw.ellipse([37, 24, 42, 30], fill=(155, 182, 32, 255))
    # stem
    draw.line([(25, 16), (25, 10)], fill=(88, 55, 18, 255), width=2)
    draw.polygon([(25, 11), (30, 6), (27, 13)], fill=(38, 128, 38, 255))

# 49. BLOOD ORANGE
def draw_blood_orange(draw):
    # whole fruit
    draw.ellipse([5, 10, 38, 44], fill=(228, 95, 25, 255))
    draw.ellipse([7, 12, 36, 42], fill=(248, 118, 48, 255))
    draw.ellipse([9, 13, 22, 26], fill=(255, 188, 115, 255))   # highlight
    # cross-section – deep crimson flesh
    draw.ellipse([26, 18, 48, 42], fill=(218, 80, 18, 255))
    draw.ellipse([28, 20, 46, 40], fill=(172, 8, 28, 255))
    draw.ellipse([30, 22, 44, 38], fill=(198, 22, 42, 255))
    # segment lines
    draw.line([(37, 20), (37, 40)], fill=(255, 255, 255, 255), width=1)
    draw.line([(28, 30), (46, 30)], fill=(255, 255, 255, 255), width=1)
    draw.line([(30, 22), (44, 38)], fill=(255, 255, 255, 255), width=1)
    draw.line([(30, 38), (44, 22)], fill=(255, 255, 255, 255), width=1)

# 50. RED CURRANT
def draw_red_currant(draw):
    # stem & branches
    draw.line([(25, 6), (16, 38)], fill=(108, 145, 68, 255), width=1)
    draw.line([(16, 38), (12, 46)], fill=(108, 145, 68, 255), width=1)
    # berries on stem
    for (bx, by) in [(18,14),(24,18),(14,24),(20,28),(11,34),(17,38),(10,43)]:
        draw.ellipse([bx-4, by-4, bx+4, by+4], fill=(228, 38, 48, 255))
        draw.ellipse([bx-3, by-3, bx+3, by+3], fill=(248, 68, 78, 255))
        draw.ellipse([bx-2, by-2, bx,   by  ], fill=(255, 135, 125, 255))  # highlight
        draw.ellipse([bx-1, by+2, bx+1, by+4], fill=(18, 12, 12, 255))     # calyx dot

# 51. BLACK CURRANT
def draw_black_currant(draw):
    draw.line([(25, 6), (16, 38)], fill=(108, 145, 68, 255), width=1)
    draw.line([(16, 38), (12, 46)], fill=(108, 145, 68, 255), width=1)
    for (bx, by) in [(18,14),(24,18),(14,24),(20,28),(11,34),(17,38),(10,43)]:
        draw.ellipse([bx-4, by-4, bx+4, by+4], fill=(22, 10, 32, 255))
        draw.ellipse([bx-3, by-3, bx+3, by+3], fill=(55, 28, 72, 255))
        draw.ellipse([bx-2, by-2, bx,   by  ], fill=(92, 55, 115, 255))   # highlight
        draw.ellipse([bx-1, by+2, bx+1, by+4], fill=(12, 8, 8, 255))

# 52. MANGOSTEEN
def draw_mangosteen(draw):
    # dark purple globose body
    draw.ellipse([9, 16, 41, 46], fill=(55, 26, 55, 255))
    draw.ellipse([11, 18, 39, 44], fill=(80, 42, 82, 255))
    draw.ellipse([13, 19, 24, 30], fill=(122, 78, 125, 255))   # highlight
    # green crown/calyx at top (4 petals)
    for pts in [[(20,16),(15,10),(22,14)], [(25,14),(20,8),(28,12)],
                [(30,16),(35,10),(28,14)], [(25,14),(30,8),(24,12)]]:
        draw.polygon(pts, fill=(55, 118, 38, 255))
    draw.ellipse([22, 12, 28, 17], fill=(78, 52, 18, 255))     # stem nub
    # cross-section (right half) white garlic-like segments
    draw.ellipse([25, 20, 47, 44], fill=(55, 26, 55, 255))
    draw.ellipse([27, 22, 45, 42], fill=(235, 228, 215, 255))
    # segment lines
    draw.line([(36, 22), (36, 42)], fill=(195, 185, 170, 255), width=1)
    draw.line([(27, 32), (45, 32)], fill=(195, 185, 170, 255), width=1)

# ─── DISPATCH ─────────────────────────────────────────────────────────────────

fruits_to_generate = [
    ("apple", draw_apple), ("apricot", draw_apricot), ("avocado", draw_avocado),
    ("banana", draw_banana), ("blackberry", draw_blackberry), ("blueberry", draw_blueberry),
    ("cantaloupe", draw_cantaloupe), ("cherry", draw_cherry), ("coconut", draw_coconut),
    ("cranberry", draw_cranberry), ("date", draw_date), ("dragonfruit", draw_dragonfruit),
    ("durian", draw_durian), ("fig", draw_fig), ("grape", draw_grape),
    ("grapefruit", draw_grapefruit), ("guava", draw_guava), ("honeydew", draw_honeydew),
    ("jackfruit", draw_jackfruit), ("kiwi", draw_kiwi), ("kumquat", draw_kumquat),
    ("lemon", draw_lemon), ("lime", draw_lime), ("lychee", draw_lychee),
    ("mango", draw_mango), ("mulberry", draw_mulberry), ("nectarine", draw_nectarine),
    ("orange", draw_orange), ("papaya", draw_papaya), ("passionfruit", draw_passionfruit),
    ("peach", draw_peach), ("pear", draw_pear), ("persimmon", draw_persimmon),
    ("pineapple", draw_pineapple), ("plum", draw_plum), ("pomegranate", draw_pomegranate),
    ("pomelo", draw_pomelo), ("quince", draw_quince), ("raspberry", draw_raspberry),
    ("starfruit", draw_starfruit), ("strawberry", draw_strawberry), ("tangerine", draw_tangerine),
    ("watermelon", draw_watermelon), ("star_apple", draw_star_apple),
    ("boysenberry", draw_boysenberry), ("elderberry", draw_elderberry),
    ("gooseberry", draw_gooseberry), ("key_lime", draw_key_lime),
    ("blood_orange", draw_blood_orange), ("red_currant", draw_red_currant),
    ("black_currant", draw_black_currant), ("mangosteen", draw_mangosteen),
]

def main():
    out_dir = "images/fruits"
    os.makedirs(out_dir, exist_ok=True)
    for name, func in fruits_to_generate:
        path = os.path.join(out_dir, f"{name}_50x50.png")
        create_sprite(path, func)
        print(f"Generated {path}")

if __name__ == "__main__":
    main()
