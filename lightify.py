#!/usr/bin/python3.4

# Copyright (c) 2014 Lukas Seidel
# Version 0.1

# import timeit
import sys, os
from PIL import Image
from phue import Bridge
import analysis as a

# insert IP of your Hue bridge here
IP = '192.168.178.45'

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
    lights = b.get_light_objects()
    lights[0].brightness = 218
    currColors = [0, 0]
    i = 0

    while True:
        os.system("import -window root screen.png")
        avgColor = a.processImage()
        lastColors = currColors
        currColors = a.calcColor(avgColor[0], avgColor[1], avgColor[2])
        if (currColors[0] > lastColors[0] + 0.018 or currColors[0] < lastColors[0] - 0.018 or
            currColors[1] > lastColors[1] + 0.018 or currColors[1] < lastColors[1] - 0.018):
               lights[0].xy = [currColors[0],currColors[1]]
               print("switched colors")
        print("UPDATE")

# t = timeit.Timer(main)
# print(t.repeat(10, 1))
main()
