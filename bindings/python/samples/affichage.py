#!/usr/bin/python
import imageViewer
import sys
import runtext
import time

run = runtext.runtextfct()
try:
    print("Press CTRL-C to stop.")
    while True:
        time.sleep(100)
except KeyboardInterrupt:
    sys.exit(0)
