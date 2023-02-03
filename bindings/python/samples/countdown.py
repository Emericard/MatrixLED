#!/usr/bin/env python
# Display a runtext with double-buffering.
from samplebase import SampleBase
from rgbmatrix import graphics

import time
import datetime

class RunText(SampleBase):
    def __init__(self, *args, **kwargs):
        super(RunText, self).__init__(*args, **kwargs)
        self.parser.add_argument("-t", "--text", help="The text to scroll on the RGB LED panel", default="Hello world!")

    def run(self):
        offscreen_canvas = self.matrix.CreateFrameCanvas()
        font = graphics.Font()
        font.LoadFont("../../../fonts/7x13.bdf")
        color = graphics.Color(255,0,0)
        print(color)
        pos = offscreen_canvas.width
        my_text = self.args.text



def calculate_days_to_xmas():
        """Calculates the number of days until next xmas"""
        now = datetime.datetime.now()
        year = now.year
        if now > datetime.datetime(year=year, month=12, day=25):
            # Account for the days after xmas of the remaining year
            year = year + 1
        delta = now - datetime.datetime(year=year, month=12, day=25)
        return abs(int(delta.days))


def affichage_countdown():
    chiffre = calculate_days_to_xmas()
    offscreen_canvas = SampleBase.matrix.CreateFrameCanvas()
    font = graphics.Font()
    font.LoadFont("../../../fonts/7x13.bdf")
    len = graphics.DrawText(offscreen_canvas, font, 10, 10, graphics.Color(255,255,255), chiffre)

    offscreen_canvas = matrix.SwapOnVSync(offscreen_canvas)




# Main function
affichage_countdown()

try:
    print("Press CTRL-C to stop.")
    while True:
        time.sleep(100)
except KeyboardInterrupt:
    sys.exit(0)
