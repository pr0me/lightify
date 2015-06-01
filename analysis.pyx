#!/usr/bin/python3.4

import timeit
import sys, os
from PIL import Image

def processImage():
    os.system("import -window root screen.png")
    img = Image.open("screen.png")
    width, height = img.size

    # make a list of all pixels in the image
    pixels = img.load()
    cdef list data
    data = []
    for x in range(width):
        for y in range(height):
            cpixel = pixels[x, y]
            data.append(cpixel)

    cdef int r
    cdef int g
    cdef int b
    cdef int counter
    r = 0
    g = 0
    b = 0
    counter = 0
    i = 0
    # loop through pixels
    # if alpha value is greater than 200/255, add it to the average
    while x < len(data):
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
        x += (counter % 2) + 1

    # compute average RGB values
    cdef double rAvg
    cdef double gAvg
    cdef double bAvg
    rAvg = r/counter
    gAvg = g/counter
    bAvg = b/counter
    cdef list avgColor
    avgColor = [rAvg, gAvg, bAvg]

    return avgColor

def calcColor(r, g, b):
    # converting RGB to xy
    cdef double red
    cdef double green
    cdef double blue
    red = r / 255.0
    green = g / 255.0
    blue = b / 255.0
    cdef list colorsRGB
    colorsRGB = gammaCorrection(red, green, blue)
    red = colorsRGB[0]
    green = colorsRGB[1]
    blue = colorsRGB[2]

    cdef double X
    cdef double Y
    cdef double Z
    cdef double xF
    cdef double yF
    X = red * 0.649926 + green * 0.103455 + blue * 0.197109
    Y = red * 0.234327 + green * 0.743075 + blue * 0.022598
    Z = red * 0.0000000 + green * 0.053077 + blue * 1.035763
    xF = X / (X + Y + Z)
    yF = Y / (X + Y + Z)
    cdef list colorsXY
    colorsXY = [xF, yF, Y]
    return colorsXY

def gammaCorrection(r, g, b):
    # simple Gamma Correction to match onscreen-colors
    cdef double red
    cdef double green
    cdef double blue
    red = ((r + 0.055) / (1.0 + 0.055))**2.4 if (r > 0.04045) else (r / 12.92)
    green = ((g + 0.055) / (1.0 + 0.055))**2.4 if (g > 0.04045) else (g / 12.92)
    blue = ((b + 0.055) / (1.0 + 0.055))**2.4 if (b > 0.04045) else (b / 12.92)
    cdef list colors
    colors = [red, green, blue]
    return colors

def main1():
    cdef list avgColor
    avgColor = processImage()
    colors = calcColor(avgColor[0], avgColor[1], avgColor[2])
    # print(avgColor)
    # print(colors)

# t = timeit.Timer(main1)
# print(t.repeat(10, 1))
