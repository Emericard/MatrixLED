#!/usr/bin/env python
# Display a runtext with double-buffering.
from samplebase import SampleBase
from rgbmatrix import graphics, RGBMatrix, RGBMatrixOptions
import sys
import time
from math import ceil, floor
import datetime
from PIL import Image

deadlines = [
    ["CTS, DCPI", datetime.datetime(year=2023, month=2, day=17) ];
    ["ESF AIR", datetime.datetime(year=2023, month=3, day=3) ];
    ["IAD, SE3D, SES", datetime.datetime(year=2023, month=3, day=17) ];
    ["ESF, ASF", datetime.datetime(year=2023, month=3, day=31) ];
    ["SESA", datetime.datetime(year=2023, month=4, day=14) ]
]


class Countdown(SampleBase):
    def __init__(self, *args, **kwargs):
        super(Countdown, self).__init__(*args, **kwargs)
        self.parser.add_argument("-t", "--runtext", help="The text to scroll on the RGB LED panel", default="Hello world!")
        self.parser.add_argument("-i", "--gifPath", help="The gpath to the gif to display", default="Images/PizzaParrot")
        self.parser.add_argument("-n", "--nb_frames", help="Thenumber of frames of the gif to display", default=10)

    def calculate_delta(self, i):
        """Calculates the number of days until next xmas"""
        now = datetime.datetime.now()
        deadline = deadlines[i][1]
        delta = deadline - now
        days = delta.days
        hours = delta.seconds // 3600
        minutes = (delta.seconds -3600*hours) // 60
        seconds = delta.seconds -3600*hours - 60*minutes
        return [days, hours, minutes, seconds]        
    
    def countdown(self,canvas, x = 20, y = 20) :
        font = graphics.Font()
        canvas.brightness = 40
        font.LoadFont("../../../fonts/7x13.bdf")
        delta = self.calculate_delta()
        string = ""
        for i in range(len(graphics[:,1])):
            delta = self.calculate_delta(i)
            string += deadlines[i][0] + " : " + str(delta[0]) + "d " + str(delta[1]) + "h "
        #string += str(delta[0]) + "d " + str(delta[1]) + "h " + str(delta[2]) + "min " + str(delta[3]) + "s "
        #len = graphics.DrawText(canvas, font, x, y, graphics.Color(255,255,255), string)
        return string
  
    def runtext(self, canvas, pos, length, text = "Coucou!"):
        font = graphics.Font()
        canvas.brightness = 100
        font.LoadFont("../../../fonts/7x13.bdf")
        #my_text = self.args.runtext
        colors = [graphics.Color(171, 71, 188),
graphics.Color(174, 76, 182),
graphics.Color(176, 82, 176),
graphics.Color(179, 87, 170),
graphics.Color(182, 92, 164),
graphics.Color(185, 97, 158),
graphics.Color(187, 103, 152),
graphics.Color(190, 108, 146),
graphics.Color(193, 113, 139),
graphics.Color(195, 118, 133),
graphics.Color(198, 124, 127),
graphics.Color(201, 129, 121),
graphics.Color(204, 134, 115),
graphics.Color(206, 139, 109),
graphics.Color(209, 145, 103),
graphics.Color(212, 150, 97),
graphics.Color(214, 155, 91),
graphics.Color(217, 160, 85),
graphics.Color(220, 166, 79),
graphics.Color(222, 171, 73),
graphics.Color(225, 176, 67),
graphics.Color(228, 181, 61),
graphics.Color(231, 187, 55),
graphics.Color(233, 192, 49),
graphics.Color(236, 197, 42),
graphics.Color(239, 202, 36),
graphics.Color(241, 208, 30),
graphics.Color(244, 213, 24),
graphics.Color(247, 218, 18),
graphics.Color(250, 223, 12),
graphics.Color(252, 229, 6),
graphics.Color(255, 234, 0)]
        now = datetime.datetime.now()
        pos -= 1 
        if pos + length == 0:
            pos = canvas.width
        lenght = graphics.DrawText(canvas, font, pos, 10, colors[ceil(31*now.second/60)], text)
        #for i in range(10):
        #    lenght= graphics.DrawLine(canvas, 0, i, 20, i, graphics.Color(0,0,0))
        return pos, lenght


    def set_image(self, canvas, frame):
        canvas.brightness = 60
        folder_path = self.args.gifPath
        nb_frame = self.args.nb_frames
        frame += 1
        if frame >= nb_frame:
            frame = 0
        image_file = folder_path + "/frame_" + str(frame) + ".gif"
        im = Image.open(image_file)
        rgbImage = im.convert ('RGB')
        [width, height] = im.size
        for i in range(width):
            for j in range(height):
                colors = rgbImage.getpixel((i,j))
                test = canvas.SetPixel(i, j, colors[0], colors[1],colors[2])
        return frame

    def run(self):
        offscreen_canvas = self.matrix.CreateFrameCanvas()
        pos = offscreen_canvas.width
        length = 0
        frame = 0
        while True :
            offscreen_canvas.Clear()
            text = self.countdown(offscreen_canvas, 30,20)
            pos, length = self.runtext(offscreen_canvas, pos, length, text)
            frame = self.set_image(offscreen_canvas, frame)
            time.sleep(0.03)
            offscreen_canvas = self.matrix.SwapOnVSync(offscreen_canvas)
    
    
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