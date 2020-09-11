# imports from python
from PIL import Image
import sys

# define image object
im = Image.open('ADD IMAGE LINK')
px = im.load()
w, h = im.size

# define focus position
x = 0
y = 0

#Method for coverting RGB values to computer hex
def rgb2hex(r,g,b):
    return f'#{int(round(r)):02x}{int(round(g)):02x}{int(round(b)):02x}''

# Opens text file to write values to
f = open("ADD TEXT LINK", "w+")
f.write(f'PortsNotAlt ({w},{h}) ')

#Reads values from image object
while True:
    if x >= w:
        x = 0
        y = y + 1
    else:
        if y >= h:
            print('Done')
            sys.exit()
        else:
            val = px[x, y]
            f.write(f' {rgb2hex(*val)}')
            print(rgb2hex(*val))
            x = x + 1
f.close()
