from colorthief import ColorThief
import matplotlib.pyplot as plt
import colorsys 
import webcolors

"""
ct = ColorThief("Dynamo.jpg")
dominant_color = (ct.get_color(quality=1))
##plt.imshow([dominant_color])
##plt.show()

palette = ct.get_palette(color_count=6)
plt.imshow([palette])
print(palette[0])
plt.show()

for color in palette:
    print(color)
    print(f"#{color[0]:02x}{color[1]:02x}{color[2]:02x}")
    print(colorsys.rgb_to_hsv(color[0], color[1], color[2]))
    print(colorsys.rgb_to_hls(color[0], color[1], color[2]))

"""
#print(webcolors.CSS21_HEX_TO_NAMES.items())





def closest_color(rgb):
    differences = {}
    for color_hex, color_name in webcolors.CSS3_HEX_TO_NAMES.items():
        r, g, b = webcolors.hex_to_rgb(color_hex)
        differences[sum([(r - rgb[0]) ** 2, 
                         (g - rgb[1]) ** 2, 
                         (b - rgb[2]) ** 2])] = color_name
    return differences[min(differences.keys())]

Covers = ["AhiVamos.png", "AmorAmarillo.png", "Artaud.png", "Bocanada.png", "CancionAnimal.png", "Dynamo.png", 
          "FuerzaNatural.png", "Grace.png", "Humbug.png", "NadaPersonal.png", "SiempreEsHoy.png", "Signos.png", "TheQueenIsDead.png", 
          "Utopia.png"]
lista = []
for i in range(len(Covers)):
    print(Covers[i])
    ct = ColorThief(Covers[i])
    color = (ct.get_color(quality=1000))
    print(color)
    lista.append(color)
    #palette = ct.get_palette(color_count=3, quality = 100)
    #plt.imshow([palette])
    #print(palette[0])
    #plt.show()
    try:
        cname = webcolors.rgb_to_name(color)
        print(f"The color is exactly {cname}")
    except ValueError:
        cname = closest_color(color)
        print(f"The closest color is {cname}")
    #plt.imshow([[color]])	
    #plt.show()

print(lista[1])
plt.imshow([lista])
plt.show()




"""
ct = ColorThief("Bocanada.png")
color = (ct.get_color(quality=100))
print(color)
palette = ct.get_palette(color_count=3, quality = 100)
plt.imshow([palette])
print(palette[0])
plt.show()


try:
    cname = webcolors.rgb_to_name(color)
    print(f"The color is exactly {cname}")
except ValueError:
    cname = closest_color(color)
    print(f"The closest color is {cname}")
    

plt.imshow([[color]])	
plt.show()
"""