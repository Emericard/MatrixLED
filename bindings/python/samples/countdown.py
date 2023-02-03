#!/usr/bin/env python
# Display a runtext with double-buffering.
from samplebase import SampleBase
from rgbmatrix import graphics, RGBMatrix, RGBMatrixOptions

import time
import datetime


class Countdown(SampleBase):
    def __init__(self, *args, **kwargs):
        super(Countdown, self).__init__(*args, **kwargs)

    def calculate_days_to_xmas():
        """Calculates the number of days until next xmas"""
        now = datetime.datetime.now()
        year = now.year
        if now > datetime.datetime(year=year, month=12, day=25):
            # Account for the days after xmas of the remaining year
            year = year + 1
        delta = now - datetime.datetime(year=year, month=12, day=25)
        return abs(int(delta.days))


    def affichage_countdown(self):
        chiffre = self.calculate_days_to_xmas()
        options = RGBMatrixOptions()
        matrice = RGBMatrix(options = options)
        offscreen_canvas = matrice.matrix.CreateFrameCanvas()
        font = graphics.Font()
        font.LoadFont("../../../fonts/7x13.bdf")
        len = graphics.DrawText(offscreen_canvas, font, 10, 10, graphics.Color(255,255,255), chiffre)

        offscreen_canvas = matrix.SwapOnVSync(offscreen_canvas)



# Main function
if __name__ == "__main__":
    countdown = Countdown()
    countdown.affichage.countdown()
    if (not countdown.process()):
        countdown.print_help()


try:
    print("Press CTRL-C to stop.")
    while True:
        time.sleep(100)
except KeyboardInterrupt:
    sys.exit(0)
