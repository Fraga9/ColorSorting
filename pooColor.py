from colorthief import ColorThief
import matplotlib.pyplot as plt
import colorsys 
import webcolors
from colorir import *

#Crea una clase de objeto tipo cover que tenga como atributos color, valoracion y rgb
class Cover:
    def __init__(self, nombre, rgb, color, distance, hex):
        self.nombre = nombre
        self.rgb = rgb
        self.color = color
        self.distance = distance
        self.hex = hex

def closest_color(rgb):
    differences = {}
    for color_hex, color_name in webcolors.CSS3_HEX_TO_NAMES.items():
        r, g, b = webcolors.hex_to_rgb(color_hex)
        differences[sum([(r - rgb[0]) ** 2, 
                         (g - rgb[1]) ** 2, 
                         (b - rgb[2]) ** 2])] = color_name
    return differences[min(differences.keys())]

#Crea una lista de objetos tipo cover
Covers = ["AhiVamos.png", "AmorAmarillo.png", "Artaud.png", "Bocanada.png", "CancionAnimal.png", "Dynamo.png", 
          "FuerzaNatural.png", "Grace.png","HatfulOfHollow.png", "Humbug.png", "NadaPersonal.png","SaturdayNightWrist.png",
          "SiempreEsHoy.png", "Signos.png", "TheBlackParade.png", "TheQueenIsDead.png", "TheSmiths.png", "Utopia.png"]



CoverList = []
for i in range(len(Covers)):
    ct = ColorThief(Covers[i])
    rgb = (ct.get_color(quality = 1000))
    hex = f"#{rgb[0]:02x}{rgb[1]:02x}{rgb[2]:02x}"
    distance = simplified_dist("#ffffff", hex)
    try:
        cname = webcolors.rgb_to_name(rgb)
    except ValueError:
        cname = closest_color(rgb)
    CoverList.append(Cover(Covers[i], rgb, cname, distance, hex))



#Color sort
#CoverList.sort(key=lambda cover: colorsys.rgb_to_hsv(*cover.rgb))

#for i in range(len(CoverList)):
    #print(CoverList[i].nombre, CoverList[i].color, CoverList[i].rgb)
    

#print(CoverList[10].distance)   
#print(CoverList[10].nombre)

rgbArray = []

#quickSort
def quick_sort(arr):
    if len(arr) <= 1:
        return arr

    pivot = arr[len(arr) // 2].distance
    left = [cover for cover in arr if cover.distance < pivot]
    middle = [cover for cover in arr if cover.distance == pivot]
    right = [cover for cover in arr if cover.distance > pivot]

    return quick_sort(left) + middle + quick_sort(right)

CoverOrdenada = quick_sort(CoverList)


for i in range(len(CoverOrdenada)):
    rgbArray.append(CoverOrdenada[i].rgb)
    
    
print(CoverOrdenada[1].nombre)
    
plt.imshow([rgbArray])
plt.show()