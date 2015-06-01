#!/usr/bin/python3.4

# Copyright (c) 2014 Lukas Seidel
# Version 0.1

import sys, os
from PIL import Image
from phue import Bridge
import analysisC

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

def main():
    connect()
    b.set_light(1, 'on', True)
    lights[0].brightness = 200
    currColors = [0, 0]

    while True:
        try:
            os.system("import -window root screen.png")
            avgColor = processImage()
            lastColors = currColors
            currColors = calcColor(avgColor[0], avgColor[1], avgColor[2])
            if (currColors[0] > lastColors[0] + 0.01 or currColors[0] < lastColors[0] - 0.01 or
                currColors[1] > lastColors[1] + 0.01 or currColors[1] < lastColors[1] - 0.01):
               lights = b.get_light_objects()
               lights[0].xy = [currColors[0],currColors[1]]
        except:
            lights = b.get_light_objects()
            lights[0].brightness = 200

main()
