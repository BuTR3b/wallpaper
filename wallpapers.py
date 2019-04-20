from PIL import Image, ImageDraw
import random
from os import system

system("cls")

print("================================")
print("Enter size of figures(1 - min, 100 - max)\n")
size = int(input(">> "))
print("================================")

img = Image.new('RGB', (240, 400))
Drawer = ImageDraw.Draw(img)

for i in range(1280):
	for j in range(720):

		x0 = random.randint(1, 720)
		y0 = random.randint(1, 1280)
		x1 = x0 + size
		y1 = y0 + size

		red = random.randint(0, 255)
		green = random.randint(0, 255)
		blue = random.randint(0, 255)

		Drawer.point((i, j), (red, green, blue))

		figure = random.choice(["polygon", "line", "rect", "ellipse"])
		if (figure == "polygon"):
			Drawer.polygon([x0, y0, x1, y1], (red, green, blue), (red, green, blue))
		elif (figure == "line"):
			Drawer.line([x0, y0, x1, y1], (red, green, blue), 1)
		elif (figure == "rect"):
			Drawer.rectangle([x0, y0, x1, y1], (red, green, blue), (red, green, blue))
		else:
			Drawer.ellipse([x0, y0, x1, y1], (red, green, blue), (red, green, blue))

img.save("pic.png")
