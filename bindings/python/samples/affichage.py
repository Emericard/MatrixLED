#!/usr/bin/python
import sys
print("sys")
from runtext import RunText
from countdown import Countdown
from samplebase import SampleBase
import time

runtext = RunText()
countdown = Countdown()
matrix = SampleBase()
offscreen_canvas = matrix.matrix.CreateFrameCanvas()
while True :
    offscreen_canvas.Clear()
    runtext_print = runtext.run()
    countdown_print = countdown.run()
    offscreen_canvas = matrix.matrix.SwapOnVSync(offscreen_canvas)

try:
    print("Press CTRL-C to stop.")
    while True:
        time.sleep(100)
except KeyboardInterrupt:
    sys.exit(0)
