#!/usr/bin/python
import imageViewer
print("Image")
import sys
print("sys")
import runtext
print("runtext")
import time


try:
    print("Press CTRL-C to stop.")
    while True:
        time.sleep(100)
except KeyboardInterrupt:
    sys.exit(0)
