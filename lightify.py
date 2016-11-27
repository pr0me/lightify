#!/usr/bin/python3.5

# Copyright (c) 2014 Lukas Seidel
# Version 1.1

# import timeit
import os
import sys
import time
from PIL import Image
from phue import Bridge
import analysis as a
import numpy as np

# insert IP of your Hue bridge here
IP = '192.168.0.101'


def est_connection():
    connected = False
    while connected == False:
        try:
            b = Bridge(IP)
            b.connect()
            connected = True
            print("Connection established.")
            return b
        except:
            print("ERROR: Please press the button on your bridge to connect!")
            connected = False

def main():
    sleep = 0.8
    id = "root"
    if len(sys.argv) > 1:
        if sys.argv[1] == "-h":
            print("usage: lightify.py [-h] [-sleep seconds] [-id ID]\n")
            print("sleep: Define the waiting time between consecutive updates.\n"
                  "   Default is 1 second.\n   Example input: 2 , 0.5")
            print("id: Define the id of the window to receive the screenshot from."
                  "Use 'xwininfo' to identify the window.\n"
                  "   If not set, whole desktop is captured.")
            return 0
        else:
            c = 0
            for arg in sys.argv:
                if arg == "-sleep":
                    sleep = int(sys.argv[c + 1])
                if arg == "-id":
                    id = str(sys.argv[c + 1])
                c += 1

    b = est_connection()
    b.set_light(1, 'on', True)
    lights = b.get_light_objects('id')
    lights[1].brightness = 218
    curr_colors = [0, 0]

    while True:
        time.sleep(sleep)
        os.system("import -window %s -resize 640 screen.png"%id)
        avg_color = a.process_image()
        last_colors = curr_colors
        curr_colors = a.calc_color(avg_color[0], avg_color[1], avg_color[2])
        if (curr_colors[0] > last_colors[0] + 0.018 or curr_colors[0] < last_colors[0] - 0.018 or
                curr_colors[1] > last_colors[1] + 0.018 or curr_colors[1] < last_colors[1] - 0.018):
            lights[1].xy = [curr_colors[0], curr_colors[1]]
            print("switched colors")
        print("tick")

    return 0

# t = timeit.Timer(main)
# print(t.repeat(10, 1))

if __name__ == "__main__":
    main()
