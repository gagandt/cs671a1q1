from PIL import Image
import numpy as np
import math
from imagecreator import img
import os
import shutil

if not os.path.exists("frames_output"):
    os.makedirs("frames_output")

os.chdir("output")

for i in range(2):
    for j in range(2):
        for k in range(12):
            for l in range(2):
                label = str(i) + "_" + str(j) + "_" + str(k) + "_" + str(l)
                os.chdir(label)
                label1 = label
                label += "_"
                
                m = 1
                f = 1                
                while m < 900:
                    img_h_stack = [None] * 3
                    for n in range(3):
                        list_im = [label + str(m) + ".jpg", label + str(m+1*10) + ".jpg", label + str(m+2*10) + ".jpg"]
                        imgs    = [ PIL.Image.open(i) for i in list_im ]
                        imgs_comb = np.hstack( (np.asarray( i) for i in imgs ))
                        img_h_stack[n] = PIL.Image.fromarray(imgs_comb)
                        
                        m += 30
                    
                    imgs = [img_h_stack[0], img_h_stack[1], img_h_stack[2]]
                    imgs_comb = np.vstack( (np.asarray( i ) for i in imgs ) )
                    imgs_comb = PIL.Image.fromarray( imgs_comb)
                    
                    os.chdir("../../frames_output")
                    if not os.path.exists(label1):
                        os.makedirs(label1)
                    os.chdir(label1)
                    
                    imgs_comb.save( str(f)+'.jpg' )
                    f += 1
                    
                    os.chdir("../../output/"+label1)
                
                os.chdir("..")
                                    
                