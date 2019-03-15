from PIL import Image
import numpy as np
import math
from imagecreator import img
import os

if not os.path.exists("output"):
    os.makedirs("output")
    
os.chdir("output")

length = [7, 15]
width = [1, 3]
color = [[255, 0, 0], [0, 0, 255]]

for i in range(2):
    for j in range(2):
        for k in range(12):
            for l in range(2):
                label = str(i) + "_" + str(j) + "_" + str(k) + "_" + str(l)
                
                data = img(label, length[i], width[j], math.pi/12 * k, color[l])
                data.create()


