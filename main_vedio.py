from PIL import Image
import numpy as np
import math
from imagecreator import img
import os

os.chdir("agg_frames/")

import cv2
import os

os.system("ffmpeg -framerate 2 -pattern_type glob -i '*.jpg' video.mp4")