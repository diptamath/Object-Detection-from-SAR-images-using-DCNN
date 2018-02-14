import json
from PIL import Image
import numpy as np
from math import pow
from pyradar.core.equalizers import naive_equalize_image
from pyradar.core.sar import save_image

input = json.load(open("train.json",'r'))
#print(input[0]["id"])
count=0
ImageArray = []
id = []
inclination = []
is_Iceberg = []
minVal=1000000
for value in input:
	#print(value["id"])
	
	id.append(value["id"])
	inclination.append(value["inc_angle"])
	is_Iceberg.append(value["is_iceberg"])
	Matrix = np.zeros(shape=(3,75,75))
	x=0
	for pixel in value["band_1"]:
		# each pixel value can be stored in a 2-D array using the formula
		# pixel x can be stored in (i,j) defined as:
		# i = x/75 and j = x%75
		val = pow(10,(pixel/10))
		if pixel < minVal:
			minVal=pixel
		Matrix[0][int(x/75)][x%75]=val
		Matrix[2][int(x/75)][x%75]=val
		x+=1
	#print(x)
	
	x=0
	for pixel in value["band_2"]:
		# each pixel value can be stored in a 2-D array using the formula
		# pixel x can be stored in (i,j) defined as:
		# i = x/75 and j = x%75
		if pixel < minVal:
			minVal=pixel
		Matrix[1][int(x/75)][x%75]=val
		Matrix[2][int(x/75)][x%75]/=val
		x+=1
	#print(x)
	
	ImageArray.append(Matrix)
	count+=1
print(len(ImageArray))
print(ImageArray[0][0][0][2])
print(minVal)
c=1
'''
#img = Image.fromarray(np.uint8(ImageArray[0]))
#img.save('myimg.jpeg')
image = ImageArray[0][1]
# get actual range
input_range = image.min(), image.max()
# set new range
output_range = 0, 255
# equalize image
image_eq = naive_equalize_image(image, input_range, output_range)
# save image in current directory
save_image(".", "image_sar", image_eq)
'''

for image in ImageArray:
	# Creates PIL image
	image=image[2]
	#img = Image.fromarray(image)
	#img.save("converted/input_"+str(c)+".png")
	# get actual range
	input_range = image.min(), image.max()
	# set new range
	output_range = 0, 255
	# equalize image
	image_eq = naive_equalize_image(image, input_range, output_range)
	
	# save image in current directory
	if is_Iceberg[c-1]:
		save_image("./iceberg", "image_sar_"+str(c), image_eq)
	else:
		save_image("./ship", "image_sar_"+str(c), image_eq)
	#img = Image.fromarray(image[1], 'L')
	#img.save("converted/inputBand2_"+str(c)+".png")
	c+=1
