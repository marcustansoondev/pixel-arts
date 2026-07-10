import os
import glob
from PIL import Image, ImageFilter
import numpy as np

def enhance_image(filepath):
    try:
        img = Image.open(filepath).convert("RGBA")
    except Exception as e:
        print(f"Failed to open {filepath}: {e}")
        return
        
    data = np.array(img)
    alpha = data[:, :, 3]
    mask = alpha > 0
    
    if not np.any(mask):
        return
        
    # Create a height map by blurring the alpha channel
    alpha_img = Image.fromarray(alpha)
    # The blurred alpha acts like a height dome: high in the middle, low at the edges
    height_img = alpha_img.filter(ImageFilter.GaussianBlur(radius=3))
    height_map = np.array(height_img).astype(float)
    
    # Scale height map to a reasonable Z depth
    height_map = (height_map / 255.0) * 15.0 
    
    # Calculate gradients (dz/dy, dz/dx)
    dy, dx = np.gradient(height_map)
    
    # Define light direction: coming from top-left, pointing down-right
    # (lx, ly, lz)
    lx, ly, lz = -1.0, -1.0, 1.5
    light_len = np.sqrt(lx**2 + ly**2 + lz**2)
    lx, ly, lz = lx/light_len, ly/light_len, lz/light_len
    
    h, w = data.shape[:2]
    
    # We will compute ambient + diffuse lighting
    ambient = 0.5
    
    for y in range(h):
        for x in range(w):
            if mask[y, x]:
                # Surface normal vector (nx, ny, nz)
                # Since z = height_map(x,y), normal is (-dz/dx, -dz/dy, 1)
                nx = -dx[y, x]
                ny = -dy[y, x]
                nz = 1.0
                
                # Normalize normal vector
                n_len = np.sqrt(nx**2 + ny**2 + nz**2)
                nx, ny, nz = nx/n_len, ny/n_len, nz/n_len
                
                # Diffuse lighting (dot product of normal and light vector)
                diffuse = max(0.0, nx*lx + ny*ly + nz*lz)
                
                # Specular lighting (optional, makes it look glossy)
                # View vector is straight down (0, 0, 1)
                # Reflection vector R = 2*(N dot L)*N - L
                dot_nl = nx*lx + ny*ly + nz*lz
                if dot_nl > 0:
                    rx = 2 * dot_nl * nx - lx
                    ry = 2 * dot_nl * ny - ly
                    rz = 2 * dot_nl * nz - lz
                    specular = max(0.0, rz) ** 10  # shininess
                else:
                    specular = 0.0
                
                # Final light factor
                light_factor = ambient + (diffuse * 0.7)
                
                for c in range(3):
                    val = data[y, x, c] * light_factor + (specular * 80)
                    data[y, x, c] = min(255, max(0, int(val)))

    enhanced_img = Image.fromarray(data, "RGBA")
    
    # Quantize cleanly
    rgb_img = Image.new("RGB", enhanced_img.size, (255, 255, 255))
    rgb_img.paste(enhanced_img, mask=alpha_img)
    
    # 9 colors + 1 transparent = 10 colors. No dithering.
    quantized = rgb_img.quantize(colors=9, method=Image.MEDIANCUT, dither=Image.NONE)
    
    final_img = quantized.convert("RGBA")
    final_data = np.array(final_img)
    
    # Restore transparency
    final_data[:, :, 3] = alpha
    
    Image.fromarray(final_data, "RGBA").save(filepath)
    print(f"Enhanced (3D Volume) {filepath}")

def main():
    files = glob.glob("images/animals/*_50x50.png")
    for f in files:
        enhance_image(f)
    print(f"Enhanced {len(files)} images with smooth 3D lighting.")

if __name__ == "__main__":
    main()
