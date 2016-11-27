#!/usr/bin/python3.5
# Version 1.1

import os
import sys
import numpy as np
from PIL import Image
import matplotlib.pylab as plt


def process_image():
    img = Image.open("screen.png")
    width, height = img.size

    # make a list of all pixels in the image
    data = np.array(img.getdata())

    r_avg = np.mean(data[:, 0])
    g_avg = np.mean(data[:, 1])
    b_avg = np.mean(data[:, 2])

    avg_color = [r_avg, g_avg, b_avg]
    print(avg_color)

    return avg_color


def gamma_correction(r, g, b):
    # simple Gamma Correction to match onscreen-colors
    red = ((r + 0.055) / (1.0 + 0.055))**2.4 if (r > 0.04045) else (r / 12.92)
    green = ((g + 0.055) / (1.0 + 0.055))**2.4 if (g > 0.04045) else (g / 12.92)
    blue = ((b + 0.055) / (1.0 + 0.055))**2.4 if (b > 0.04045) else (b / 12.92)
    colors = [red, green, blue]
    return colors


def calc_color(r, g, b):
    # converting RGB to HUE
    red = r / 255.0
    green = g / 255.0
    blue = b / 255.0
    colors_rgb = gamma_correction(red, green, blue)
    red = colors_rgb[0]
    green = colors_rgb[1]
    blue = colors_rgb[2]

    X = red * 0.649926 + green * 0.103455 + blue * 0.197109
    Y = red * 0.234327 + green * 0.743075 + blue * 0.022598
    Z = red * 0.0000000 + green * 0.053077 + blue * 1.035763
    xF = X / (X + Y + Z)
    yF = Y / (X + Y + Z)
    colors_xy = [xF, yF, Y]
    return colors_xy


def main():
    avg_color = process_image()
    colors = calc_color(avg_color[0], avg_color[1], avg_color[2])
    # print(avg_color)
    # print(colors)
