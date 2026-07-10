import os
import glob
from PIL import Image, ImageEnhance, ImageFilter, ImageDraw, ImageOps
import numpy as np

def enhance_image(filepath):
    # Load image and ensure RGBA
    img = Image.open(filepath).convert("RGBA")
    data = np.array(img)
    
    # Extract alpha channel
    alpha = data[:, :, 3]
    
    # Mask of non-transparent pixels
    mask = alpha > 0
    
    if not np.any(mask):
        return
        
    # Get bounding box of the non-transparent area
    y_indices, x_indices = np.where(mask)
    if len(x_indices) == 0:
        return
        
    min_x, max_x = np.min(x_indices), np.max(x_indices)
    min_y, max_y = np.min(y_indices), np.max(y_indices)
    
    # Create a shadow/highlight gradient based on y coordinate (top-down lighting)
    h, w = data.shape[:2]
    
    # Let's add simple shading
    for y in range(h):
        for x in range(w):
            if mask[y, x]:
                # simple lighting based on normalized y position in the object
                rel_y = (y - min_y) / max((max_y - min_y), 1)
                
                # top is brighter, bottom is darker
                light_factor = 1.2 - (rel_y * 0.4) 
                
                # add some noise for texture
                noise = np.random.uniform(0.95, 1.05)
                
                factor = light_factor * noise
                
                for c in range(3):
                    val = int(data[y, x, c] * factor)
                    data[y, x, c] = min(255, max(0, val))
                    
    # Recreate image
    enhanced_img = Image.fromarray(data, "RGBA")
    
    # Extract alpha to apply later
    alpha_img = enhanced_img.split()[3]
    
    # Convert RGB to P mode with max 10 colors (quantize)
    # PIL's quantize works best on RGB, so convert to RGB first (with white bg)
    rgb_img = Image.new("RGB", enhanced_img.size, (255, 255, 255))
    rgb_img.paste(enhanced_img, mask=alpha_img)
    
    # Quantize to 9 colors (leaving 1 for transparent)
    quantized = rgb_img.quantize(colors=9, method=Image.MEDIANCUT)
    
    # Convert back to RGBA and re-apply alpha
    final_img = quantized.convert("RGBA")
    final_data = np.array(final_img)
    
    # Restore transparency
    final_data[:, :, 3] = alpha
    
    # Save back
    Image.fromarray(final_data, "RGBA").save(filepath)
    print(f"Enhanced {filepath}")

def main():
    files = glob.glob("images/kitchen/*_50x50.png")
    for f in files:
        enhance_image(f)
    print(f"Enhanced {len(files)} images.")

if __name__ == "__main__":
    main()
