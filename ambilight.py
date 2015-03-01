#!/usr/bin/python3.4

# Copyright (c) 2014 Lukas Seidel
# Version 0.1

import sys
from phue import Bridge

IP = '192.168.178.31'

b = Bridge(IP)

def connect():
    connected = False
    while connected == False:
        try:
            b.connect()
            connected = True
            print("Connected!")
        except:
            print("Please press the button on your bridge to connect!")
            connected = False

def calcColor(r, g, b):
    # converting RGB to xy
    r = r / 255.0
    g = g / 255.0
    b = b / 255.0
    colorsRGB = [r, g, b]
    colorsRGB = gammaCorrection(r, g, b)
    x = X / (X + Y + Z)
    y = Y / (X + Y + Z)
    colorsXY = [x, y]
    return colorsXY

def gammaCorrection(r, g, b):
    red = ((r + 0.055) / (1.0 + 0.055))**2.4 if (r > 0.04045) else (r / 12.92)
    green = ((g + 0.055) / (1.0 + 0.055))**2.4 if (g > 0.04045) else (g / 12.92)
    blue = ((b + 0.055) / (1.0 + 0.055))**2.4 if (b > 0.04045) else (b / 12.92)
    colors = [red, green, blue]
    return colors

def main():
    connect()
    b.set_light(1, 'on', True)
    lights = b.get_light_objects()
    lights[0].brightness = 254
    lights[0].xy = [1,1]

main()
