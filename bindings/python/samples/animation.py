#!/usr/bin/python
import time
import sys

from imageViewer import display_image
from rgbmatrix import RGBMatrix, RGBMatrixOptions
from PIL import Image

frame = len(sys.argv) 


if len(sys.argv) < 3:
    sys.exit("Require an image argument")
else:
    folder_path = sys.argv[1]
    nb_frame = sys.argv[2]
    while(True): 
        for i in range(int(nb_frame)): 
            image_file = folder_path + "/frame_" + str(i) + ".gif"
            display_image(image_file)
            time.sleep(0.1)
try:
    print("Press CTRL-C to stop.")
    while True:
        time.sleep(100)
except KeyboardInterrupt:
    sys.exit(0)
