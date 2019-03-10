from PIL import Image
import numpy as np
import math
from imagecreator import img
import os

os.chdir("test")

import PIL

list_im = ['0_0_0_0_1.png','0_0_0_0_2.png', '0_0_0_0_3.png']
imgs    = [ PIL.Image.open(i) for i in list_im ]

imgs_comb = np.hstack( (np.asarray( i) for i in imgs ) )

# save that beautiful picture
imgs_comb1 = PIL.Image.fromarray( imgs_comb)
#imgs_comb.save( 'Trifecta1.jpg' )    

list_im = ['0_0_0_0_4.png','0_0_0_0_6.png', '0_0_0_0_9.png']
imgs    = [ PIL.Image.open(i) for i in list_im ]
# pick the image which is the smallest, and resize the others to match it (can be arbitrary image shape here)
imgs_comb = np.hstack( (np.asarray( i ) for i in imgs ) )

# save that beautiful picture
imgs_comb2 = PIL.Image.fromarray( imgs_comb)
#imgs_comb.save( 'Trifecta2.jpg' ) 

list_im = ['0_0_0_0_5.png','0_0_0_0_7.png', '0_0_0_0_8.png']
imgs    = [ PIL.Image.open(i) for i in list_im ]
# pick the image which is the smallest, and resize the others to match it (can be arbitrary image shape here)
imgs_comb = np.hstack( (np.asarray( i ) for i in imgs ) )

# save that beautiful picture
imgs_comb3 = PIL.Image.fromarray( imgs_comb)
#imgs_comb.save( 'Trifecta3.jpg' ) 

imgs = [imgs_comb1, imgs_comb2, imgs_comb3]
#imgs    = [ PIL.Image.open(i) for i in list_im ]

# for a vertical stacking it is simple: use vstack
imgs_comb = np.vstack( (np.asarray( i ) for i in imgs ) )
imgs_comb = PIL.Image.fromarray( imgs_comb)
imgs_comb.save( 'Tl.jpg' )