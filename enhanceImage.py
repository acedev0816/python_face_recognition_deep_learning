from PIL import Image
from PIL import ImageEnhance
from PIL import ImageFilter
import os
import cv2


def adjust_brightness(input_image,factor):
	enhancer_object = ImageEnhance.Brightness(input_image)
	out = enhancer_object.enhance(factor)
	return out
def adjust_contrast(input_image,factor):
	enhancer_object = ImageEnhance.Contrast(input_image)
	out = enhancer_object.enhance(factor)
	return out
def adjust_sharpness(input_image,factor):
	enhancer_object = ImageEnhance.Sharpness(input_image)
	out = enhancer_object.enhance(factor)
	return out
def main():
	index = 1
	while True:
		path = ".\\output\\Person" + str(index) +"\\image2.jpg"
		if not os.path.exists(path):
			break
		image = Image.open(path)
		cv_image = cv2.imread(path)
		cv2.imshow('orgin'+str(index),cv_image)
		image_bright = adjust_brightness(image,1.7)
		image_shape = adjust_sharpness(image,1.7)
		image_contrast = adjust_contrast(image_shape,1.7)

		

		directpath = ".\\output\\adjust"
		if not os.path.exists(directpath):
			print("make " + directpath)
			os.makedirs(directpath)

		savepath = directpath +"\\Person" + str(index) +".jpg"
		image_contrast.save(savepath)
		cv_image = cv2.imread(savepath)
		cv2.imshow('enhance' + str(index),cv_image)
		index += 1

if __name__ == '__main__':
	main()
	while True:
		k = cv2.waitKey(10)
		if k == ord('q'):
			break
	cv2.destroyAllWindows()