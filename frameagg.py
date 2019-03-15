from PIL import Image
import numpy as np
import math
from imagecreator import img
import os
from shutil import copyfile

os.chdir("frames_output")

fcount = 1
offset = 0

for h in range(3):
    
    for i in range(2):
        for j in range(2):
            for k in range(12):
                for l in range(2):
                    label = str(i) + "_" + str(j) + "_" + str(k) + "_" + str(l)
                    os.chdir(label)
                    
                    for m in range(3):
                        copyfile(str(m + 1 + offset ) + ".jpg", "../../agg_frames/" + str("{0:0=3d}".format(fcount)) + ".jpg")
                        fcount += 1
                    os.chdir("..")
    offset += 3

for i in range(2):
    for j in range(2):
        for k in range(12):
            for l in range(2):
                label = str(i) + "_" + str(j) + "_" + str(k) + "_" + str(l)
                os.chdir(label)
                
                
                copyfile(str(1 + offset) + ".jpg", "../../agg_frames/" + str(fcount) + ".jpg")
                fcount += 1
                os.chdir("..")