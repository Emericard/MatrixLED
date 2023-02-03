#!/usr/bin/env python
# Display a runtext with double-buffering.
from samplebase import SampleBase
from rgbmatrix import graphics
import sys
import time
import datetime


class Countdown(SampleBase):
    def __init__(self, *args, **kwargs):
        super(Countdown, self).__init__(*args, **kwargs)

    def calculate_delta(self):
        """Calculates the number of days until next xmas"""
        now = datetime.datetime.now()
        deadline = datetime.datetime(year=2023, month=12, day=25)
        delta = deadline - now
        return [int(delta.days), int(delta.hour), int(delta.minute), int(delta.second)]

    def countdown(self):
        offscreen_canvas = self.matrix.CreateFrameCanvas()
        font = graphics.Font()
        delta = self.calculate_delta()
        font.LoadFont("../../../fonts/7x13.bdf")
        string = str(delta[0]) + "d " + str(delta[1]) + "h " + str(delta[2]) + "min " + str(delta[3]) + "s "
        len = graphics.DrawText(offscreen_canvas, font, 10, 10, graphics.Color(255,255,255), string)

        offscreen_canvas = self.matrix.SwapOnVSync(offscreen_canvas)
    
    def run(self):
        while True :
            self.countdown()


# Main function
if __name__ == "__main__":
    countdown = Countdown()
    if (not countdown.process()):
        countdown.print_help()


try:
    print("Press CTRL-C to stop.")
    while True:
        time.sleep(100)
except KeyboardInterrupt:
    sys.exit(0)
