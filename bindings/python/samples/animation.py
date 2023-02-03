#!/usr/bin/python
import time
import sys

from imageViewer import display_image
from rgbmatrix import RGBMatrix, RGBMatrixOptions
from PIL import Image

frame = len(sys.arg) 

if len(sys.argv) < 2:
    sys.exit("Require an image argument")
else:
    for i in range(frame): 
        image_file = sys.argv[i+1]

display_image(image_file)


try:
    print("Press CTRL-C to stop.")
    while True:
        time.sleep(100)
except KeyboardInterrupt:
    sys.exit(0)
