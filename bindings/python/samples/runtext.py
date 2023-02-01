#!/usr/bin/env python
# Display a runtext with double-buffering.
from samplebase import SampleBase
from rgbmatrix import graphics

import time


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
        iteration = 0
        sens = 1
        while True:
            offscreen_canvas.Clear()
            iteration += sens
            if iteration == 31 or iteration == 0:
                sens = -sens
            len = graphics.DrawText(offscreen_canvas, font, pos, 10, colors[iteration], my_text)
            pos -= 1
            if (pos + len < 16):
                pos = offscreen_canvas.width

            time.sleep(0.05)
            offscreen_canvas = self.matrix.SwapOnVSync(offscreen_canvas)

        print(offscreen_canvas)


# Main function
if __name__ == "__main__":
    run_text = RunText()
    if (not run_text.process()):
        run_text.print_help()
