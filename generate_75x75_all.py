import os
import glob
from PIL import Image
import numpy as np

def enhance_image(src_path, dest_path):
    try:
        img = Image.open(src_path).convert("RGBA")
        
        # 1. Resize to 75x75 using NEAREST to keep it pixel-perfect (no blur)
        img_75 = img.resize((75, 75), Image.Resampling.NEAREST)
        arr = np.array(img_75, dtype=np.int32)
        h, w, c = arr.shape
        
        # Extract alpha mask
        alpha = arr[:, :, 3]
        is_opaque = alpha > 128
        
        # 2. Generate Outline (1 pixel dark border around opaque areas)
        outline_mask = np.zeros((h, w), dtype=bool)
        for dy in [-1, 0, 1]:
            for dx in [-1, 0, 1]:
                if dy == 0 and dx == 0:
                    continue
                # Shift alpha
                shifted = np.roll(alpha, shift=(dy, dx), axis=(0, 1))
                outline_mask |= (~is_opaque) & (shifted > 128)
                
        # 3. Generate Bevel Shading (Highlights and Shadows)
        highlight_mask_1 = np.zeros((h, w), dtype=bool)
        highlight_mask_2 = np.zeros((h, w), dtype=bool)
        shadow_mask_1 = np.zeros((h, w), dtype=bool)
        shadow_mask_2 = np.zeros((h, w), dtype=bool)
        
        # Check 1-pixel neighborhood for Tier 1 highlights/shadows
        for dy, dx in [(-1, 0), (0, -1), (-1, -1)]:
            shifted = np.roll(alpha, shift=(dy, dx), axis=(0, 1))
            highlight_mask_1 |= is_opaque & (shifted <= 128)
            
        for dy, dx in [(1, 0), (0, 1), (1, 1)]:
            shifted = np.roll(alpha, shift=(dy, dx), axis=(0, 1))
            shadow_mask_1 |= is_opaque & (shifted <= 128)
            
        # Check 2-pixel neighborhood for Tier 2 highlights/shadows
        for dy, dx in [(-2, 0), (0, -2), (-2, -2)]:
            shifted = np.roll(alpha, shift=(dy, dx), axis=(0, 1))
            highlight_mask_2 |= is_opaque & (shifted <= 128) & (~highlight_mask_1)
            
        for dy, dx in [(2, 0), (0, 2), (2, 2)]:
            shifted = np.roll(alpha, shift=(dy, dx), axis=(0, 1))
            shadow_mask_2 |= is_opaque & (shifted <= 128) & (~shadow_mask_1)
            
        # 4. Apply colors
        out_arr = np.zeros((h, w, 4), dtype=np.uint8)
        
        # Base sprite drawing
        for y in range(h):
            for x in range(w):
                if is_opaque[y, x]:
                    r, g, b = arr[y, x, :3]
                    
                    # Apply shading
                    if highlight_mask_1[y, x]:
                        # Tier 1 highlight (+25% brightness)
                        r = min(255, int(r * 1.25))
                        g = min(255, int(g * 1.25))
                        b = min(255, int(b * 1.25))
                    elif highlight_mask_2[y, x]:
                        # Tier 2 highlight (+12% brightness)
                        r = min(255, int(r * 1.12))
                        g = min(255, int(g * 1.12))
                        b = min(255, int(b * 1.12))
                    elif shadow_mask_1[y, x]:
                        # Tier 1 shadow (-25% brightness)
                        r = max(0, int(r * 0.75))
                        g = max(0, int(g * 0.75))
                        b = max(0, int(b * 0.75))
                    elif shadow_mask_2[y, x]:
                        # Tier 2 shadow (-12% brightness)
                        r = max(0, int(r * 0.88))
                        g = max(0, int(g * 0.88))
                        b = max(0, int(b * 0.88))
                        
                    out_arr[y, x] = [r, g, b, 255]
                elif outline_mask[y, x]:
                    # Outline color (dark charcoal)
                    out_arr[y, x] = [25, 25, 30, 255]
                else:
                    # Transparent background
                    out_arr[y, x] = [0, 0, 0, 0]
                    
        # Create PIL image
        out_img = Image.fromarray(out_arr, "RGBA")
        
        # 5. Quantize to exactly 15 colors to guarantee 10-20 color range
        quantized = out_img.quantize(colors=15, method=Image.Quantize.FASTOCTREE, dither=Image.Dither.NONE)
        
        # Convert back to RGBA and check transparency
        final_rgba = quantized.convert("RGBA")
        
        # Ensure background pixels are fully transparent (0,0,0,0)
        final_arr = np.array(final_rgba)
        final_arr[final_arr[:, :, 3] < 128] = [0, 0, 0, 0]
        final_rgba = Image.fromarray(final_arr, "RGBA")
        
        # Save the 75x75 image
        final_rgba.save(dest_path)
        return True
    except Exception as e:
        print(f"Error processing {src_path}: {e}")
        return False

def main():
    print("Starting batch generation of pixel-perfect, cel-shaded outline sprites (75x75)...")
    
    # Process Animals
    animal_files = glob.glob("images/animals/*_50x50.png")
    print(f"Found {len(animal_files)} animal sprites.")
    success_animals = 0
    for f in sorted(animal_files):
        dest = f.replace("_50x50.png", "_75x75.png")
        if enhance_image(f, dest):
            success_animals += 1
            
    print(f"Successfully generated {success_animals}/{len(animal_files)} enhanced animal sprites.")
    
    # Process Fruits
    fruit_files = glob.glob("images/fruits/*_50x50.png")
    print(f"Found {len(fruit_files)} fruit sprites.")
    success_fruits = 0
    for f in sorted(fruit_files):
        dest = f.replace("_50x50.png", "_75x75.png")
        if enhance_image(f, dest):
            success_fruits += 1
            
    print(f"Successfully generated {success_fruits}/{len(fruit_files)} enhanced fruit sprites.")
    print("Done!")

if __name__ == "__main__":
    main()
