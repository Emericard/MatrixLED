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

    def calculate_days_to_xmas(self):
        """Calculates the number of days until next xmas"""
        now = datetime.datetime.now()
        year = now.year
        if now > datetime.datetime(year=year, month=12, day=25):
            # Account for the days after xmas of the remaining year
            year = year + 1
        delta = now - datetime.datetime(year=year, month=12, day=25)
        return abs(int(delta.days))
    
    def calculate_seconds(self):
        now = datetime.datetime.now()
        seconds_total = now.second
        hours = seconds_total // 3600
        minutes = (seconds_total - hours*3600) // 60
        seconds = seconds_total - hours*3600 - minutes*60
        return [hours, minutes, seconds]

    def countdown(self):
        chiffre = self.calculate_days_to_xmas()
        offscreen_canvas = self.matrix.CreateFrameCanvas()
        font = graphics.Font()
        seconds_total = self.calculate_seconds()
        font.LoadFont("../../../fonts/7x13.bdf")
        string = str(chiffre) + "d " + str(seconds_total[0]) + "h " + str(seconds_total[1]) + "min " + str(seconds_total[2]) + "s "
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
