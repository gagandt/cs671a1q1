from PIL import Image
import numpy as np

w, h = 28, 28
data = np.zeros((h, w, 3), dtype=np.uint8)
img = Image.fromarray(data, 'RGB')
img.save('my.png')
img.show()