#!/usr/bin/python3.4

# Copyright (c) 2014 Lukas Seidel
# Version 0.1

import sys
from gi.repository import Gtk
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
    X = r * 0.649926 + g * 0.103455 + b * 0.197109
    Y = r * 0.234327 + g * 0.743075 + b * 0.022598
    Z = r * 0.0000000 + g * 0.053077 + b * 1.035763
    colorsRGB = gammaCorrection(X, Y, Z)
    xF = X / (X + Y + Z)
    yF = Y / (X + Y + Z)
    colorsXY = [xF, yF, Y]
    return colorsXY

def getImage():


def gammaCorrection(r, g, b):
    # simple Gamma Correction to match onscreen-colors
    red = ((r + 0.055) / (1.0 + 0.055))**2.4 if (r > 0.04045) else (r / 12.92)
    green = ((g + 0.055) / (1.0 + 0.055))**2.4 if (g > 0.04045) else (g / 12.92)
    blue = ((b + 0.055) / (1.0 + 0.055))**2.4 if (b > 0.04045) else (b / 12.92)
    colors = [red, green, blue]
    return colors

def main():
    connect()
    colors = calcColor(0, 0, 128)
    b.set_light(1, 'on', True)
    lights = b.get_light_objects()
    lights[0].brightness = colors[2]
    lights[0].xy = [colors[0],colors[1]]

# main()
getImage()
