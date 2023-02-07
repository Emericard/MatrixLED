#!/usr/bin/python
import sys
print("sys")
from runtext import RunText
from countdown import Countdown
import time

runtext = RunText()
countdown = Countdown()

try:
    print("Press CTRL-C to stop.")
    while True:
        time.sleep(100)
except KeyboardInterrupt:
    sys.exit(0)
