#!/usr/bin/env python

import pysimpledmx


class Spot:
    """
    Control some generic brand 5 channel LED moving head spotlight

    Channels:
    1: Pan (540 degrees)
    2: Tilt (270 degrees)
    3: Dimmer/Strobe
    4: Color Macro
    5: Gobo
    """

    def __init__(self, serial_port, channel):
        self.dmx = pysimpledmx.DMXConnection(serial_port)
        self.channel = channel

    def blackout(self):
        for i in range(5):
            self.dmx.clear(self.channel + i)
        self.dmx.render()

    def pan(self, value, send_now=False):
        self.dmx.setChannel(self.channel, value)
        if send_now:
            self.dmx.render()

    def tilt(self, value, send_now=False):
        self.dmx.setChannel(self.channel + 1, value)
        if send_now:
            self.dmx.render()

    def dimmer(self, value, send_now=False):
        self.dmx.setChannel(self.channel + 2, value)
        if send_now:
            self.dmx.render()

    def color_macro(self, value, send_now=False):
        self.dmx.setChannel(self.channel + 3, value)
        if send_now:
            self.dmx.render()

    def gobo(self, value, send_now=False):
        self.dmx.setChannel(self.channel + 4, value)
        if send_now:
            self.dmx.render()

    def send(self):
        self.dmx.render()

if __name__ == "__main__":
    import time
    import random
    spot = Spot("/dev/ttyUSB0", 1)
    spot.pan(random.randint(0, 255))
    spot.tilt(random.randint(0, 255))
    spot.dimmer(random.randint(0, 255))
    spot.color_macro(random.randint(0, 255))
    spot.gobo(random.randint(0, 255))
    spot.send()
    time.sleep(5)
    spot.blackout()
