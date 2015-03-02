#!/usr/bin/python3.4

# Copyright (c) 2014 Lukas Seidel
# Version 0.1

import sys, os
from PIL import Image
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


def processImage():
    os.system("import -window root screen.png")
    # open the image
    img = Image.open("screen.png")

    # grab width and height
    width, height = img.size

    # make a list of all pixels in the image
    pixels = img.load()
    data = []
    for x in range(width):
        for y in range(height):
            cpixel = pixels[x, y]
            data.append(cpixel)
    r = 0
    g = 0
    b = 0
    counter = 0
    # loop through all pixels
    # if alpha value is greater than 200/255, add it to the average
    # (note: could also use criteria like, if not a black pixel or not a white pixel...)
    for x in range(len(data)):
        try:
            if int(data[x][3]) >= 200:
                r += int(data[x][0])
                g += int(data[x][1])
                b += int(data[x][2])
        except:
            r += int(data[x][0])
            g += int(data[x][1])
            b += int(data[x][2])

        counter += 1

    # compute average RGB values
    rAvg = r/counter
    gAvg = g/counter
    bAvg = b/counter
    avgColor = [rAvg, gAvg, bAvg]
    os.system("rm screen.png")
    # print(str(avgColor[0]) + " " + str(avgColor[1]) + " " + str(avgColor[2]))
    return avgColor


def calcColor(r, g, b):
    # converting RGB to xy
    red = r / 255.0
    green = g / 255.0
    blue = b / 255.0
    colorsRGB = gammaCorrection(red, green, blue)
    red = colorsRGB[0]
    green = colorsRGB[1]
    blue = colorsRGB[2]
    X = red * 0.649926 + green * 0.103455 + blue * 0.197109
    Y = red * 0.234327 + green * 0.743075 + blue * 0.022598
    Z = red * 0.0000000 + green * 0.053077 + blue * 1.035763
    xF = X / (X + Y + Z)
    yF = Y / (X + Y + Z)
    colorsXY = [xF, yF, Y]
    return colorsXY


def gammaCorrection(r, g, b):
    # simple Gamma Correction to match onscreen-colors
    red = ((r + 0.055) / (1.0 + 0.055))**2.4 if (r > 0.04045) else (r / 12.92)
    green = ((g + 0.055) / (1.0 + 0.055))**2.4 if (g > 0.04045) else (g / 12.92)
    blue = ((b + 0.055) / (1.0 + 0.055))**2.4 if (b > 0.04045) else (b / 12.92)
    colors = [red, green, blue]
    return colors


def main():
    connect()

    while True:
        try:
            avgColor = processImage()
            colors = calcColor(avgColor[0], avgColor[1], avgColor[2])
            b.set_light(1, 'on', True)
            lights = b.get_light_objects()
            # lights[0].brightness = int(colors[2])
            lights[0].brightness = 200
            lights[0].xy = [colors[0],colors[1]]
        except:
            lights[0].brightness = 200

main()

