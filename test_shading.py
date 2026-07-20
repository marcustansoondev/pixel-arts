import numpy as np
from PIL import Image, ImageDraw

def draw_test_burger():
    img = Image.new("RGBA", (50, 50), (0, 0, 0, 0))
    d = ImageDraw.Draw(img)
    # Bottom bun
    d.ellipse([10, 35, 40, 45], fill=(220, 170, 110))
    # Patty
    d.ellipse([10, 30, 40, 40], fill=(100, 50, 20))
    # Cheese
    d.polygon([(10, 33), (20, 38), (30, 33), (40, 38), (35, 28), (15, 28)], fill=(255, 200, 50))
    # Lettuce
    d.ellipse([8, 25, 42, 33], fill=(50, 200, 50))
    # Top bun
    d.chord([10, 15, 40, 35], start=180, end=0, fill=(220, 170, 110))
    # Sesame seeds
    d.point([20, 20], fill=(255, 255, 200))
    d.point([30, 22], fill=(255, 255, 200))
    d.point([25, 18], fill=(255, 255, 200))
    return img

def apply_shading(arr, mask):
    h, w, _ = arr.shape
    shaded = arr.copy().astype(float)
    
    for y in range(h):
        for x in range(w):
            if not mask[y, x]: continue
            
            color = arr[y, x]
            
            # Global lighting gradient (subtle)
            # x_ratio = x / w
            # y_ratio = y / h
            # factor = 1.0 - 0.2 * (x_ratio + y_ratio)
            # base = color * factor
            base = color.astype(float)
            
            # Bevel edges
            top_diff = (y == 0) or np.any(arr[y-1, x] != color)
            left_diff = (x == 0) or np.any(arr[y, x-1] != color)
            bottom_diff = (y == h-1) or np.any(arr[y+1, x] != color)
            right_diff = (x == w-1) or np.any(arr[y, x+1] != color)
            
            if top_diff and left_diff:
                base += 60 # Strong highlight
            elif top_diff or left_diff:
                base += 30 # Mild highlight
            elif bottom_diff and right_diff:
                base -= 60 # Strong shadow
            elif bottom_diff or right_diff:
                base -= 30 # Mild shadow
                
            shaded[y, x] = np.clip(base, 0, 255)
            
    return shaded

def _apply_outline_and_quantize(img: Image.Image) -> Image.Image:
    arr   = np.array(img.convert("RGBA"))
    alpha = arr[:, :, 3]
    mask  = alpha > 128

    h, w = mask.shape
    outline = np.zeros((h, w), bool)
    for dy, dx in [(-1,0),(1,0),(0,-1),(0,1)]:
        shifted = np.roll(np.roll(mask, dy, 0), dx, 1)
        if dy ==  1: shifted[0,  :] = False
        if dy == -1: shifted[-1, :] = False
        if dx ==  1: shifted[:,  0] = False
        if dx == -1: shifted[:, -1] = False
        outline |= (~mask) & shifted

    rgb = arr[:, :, :3].copy()
    
    # 1. APPLY BEVEL SHADING TO OPAQUE AREAS BEFORE OUTLINE
    rgb = apply_shading(rgb, mask)

    # 2. APPLY OUTLINE
    rgb[outline] = [25, 25, 30] # Dark charcoal outline

    new_alpha = alpha.copy()
    new_alpha[outline] = 255

    # Paste onto white background
    flat = Image.new("RGB", (50, 50), (255, 255, 255))
    composed = Image.fromarray(
        np.dstack((rgb, new_alpha)).astype(np.uint8), "RGBA"
    )
    flat.paste(composed, mask=Image.fromarray(new_alpha, "L"))

    # Quantize to 9 colors
    q = flat.quantize(colors=9, method=Image.MEDIANCUT, dither=0)
    final = q.convert("RGBA")
    
    final_arr = np.array(final)
    final_arr[new_alpha < 128] = [0, 0, 0, 0]
    
    return Image.fromarray(final_arr, "RGBA")

if __name__ == "__main__":
    img = draw_test_burger()
    img.save("test_burger_raw.png")
    out = _apply_outline_and_quantize(img)
    out.save("test_burger_shaded.png")
    print("Done")
