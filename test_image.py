from PIL import Image
import numpy as np

img = Image.open('images/clothing/tshirt_50x50.png')
data = np.array(img)
unique_colors = np.unique(data.reshape(-1, 4), axis=0)
print(f"Colors ({len(unique_colors)}):")
for c in unique_colors:
    print(c)
