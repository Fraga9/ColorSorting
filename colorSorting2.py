import random
from colorthief import ColorThief
import matplotlib.pyplot as plt
import colorsys 
import webcolors
from colorir import *

##colours_lenght = 1000
##colours = []
##for i in range(1, colours_lenght):
##    colours.append(
##        [
##            random.random(),
##            random.random(),
##            random.random()      
##        ]  
##    )

colors = [random_color() for _ in range(1000)]
print(colors[1])
colors.sort(key=hue_sort_key())  # This is where the magic happens


