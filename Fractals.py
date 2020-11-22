#Optimisation
import math
from PIL import Image

# creates a julia set
# width, height are for the size of the image
# max_count defines the maximum itteration per pixel
# zoom, dx, dy defines if we zoom in and the displacement of the center
# cR, cX variables to change shapes
def createJuliaSet(width=1280, height=800, max_count=100, zoom=1.2, dx=0, dy=0, cR=-0.8, cX=0.156):
	color_gradient = [[100,100,200], [50,50,180], [200, 50, 128], [255, 230, 0], [0,0,0]] #our default gradient for coloring

	#initialize new image with pixel map
	new_image = Image.new("RGB", (width, height), "black")
	pixels = new_image.load()

	for y in range(0, height):
		for x in range(0, width):
			# Zn + 1 = Zn**2 + C => (zR+zX)**2 + (cR + cX)
			zR = (1 / zoom) * ((x - dx) - (width/2.0))*(4.0/width) #real number is on x axis
			zX = (1 / zoom) * ((y - dy) - (height/2.0))*(4.0/width) #because it's an imaginery number
			
			#iterate through each pixel
			count = 0
			while (count < max_count) and ((zR**2+zX**2) < 4):
				count += 1
				new_zR = (zR * zR) - (zX * zX) + cR
				zX = 2 * zR * zX + cX
				zR = new_zR
			
			#color the pixel appropriately
			n = math.sin(float(count)/max_count) * float(len(color_gradient) - 1)
			n1 = int(math.floor(n))
			n1 = int(math.floor(n))
			n2 = int(math.ceil(n))
			color = []
			for m in range(3):
				c = int(color_gradient[n1][m] * (n - n1) + color_gradient[n2][m] * (n2 - n))
				color.append(c)
			pixels[x, y] = tuple(color)

	name = "JuliaSet.png"
	new_image.save(name, "PNG")		
	new_image.show()


# creates a mandelbrot set
# width, height are for the size of the image
# max_count defines the maximum itteration per pixel
# zoom, dx, dy defines if we zoom in and the displacement of the center
def createMandelBrot(width=1280, height=800, max_count=100, zoom=1.0, dx=0, dy=0):
	#initialize new image with pixel map
	new_image = Image.new("RGB", (width, height), "black")
	pixels = new_image.load()

	for y in range(0, height):
		for x in range(0, width):
			# Zn + 1 = Zn**2 + C => (zR+zX)**2 + (cR + cX)
			cR = (1 / zoom) * ((x - dx) - (width/2.0))*(4.0/width) #real number is on x axis
			cX = (1 / zoom) * ((y - dy) - (height/2.0))*(4.0/width) #because it's an imaginery number
			zR = 0
			zX = 0

			count = 0
			while (count < max_count) and ((zR**2+zX**2) < 4):
				count += 1
				new_zR = (zR * zR) - (zX * zX) + cR
				zX = 2 * zR * zX + cX
				zR = new_zR
			
			if count == max_count:
				# it's outside so black
				pixels[x, y] = (0,0,0)
			else:
				# the colors are chosen based on these function
				r = math.cos(count) * 255
				g = math.sin(count) * 255
				b = math.tan(count) * 255
				pixels[x, y] = (int(r), int(g), int(b))		

	name = "MandelBrot.png"
	new_image.save(name, "PNG")	
	new_image.show()

if __name__ == "__main__":
  #createMandelBrot()
  #createJuliaSet()
