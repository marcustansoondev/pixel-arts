from PIL import Image
import numpy as np

data = np.zeros((50, 50, 4)).astype(float)
data[:, :, 3] = 255
alpha = data[:, :, 3].copy()
img = Image.fromarray(alpha, "L")
print(img.getpixel((0,0)))
