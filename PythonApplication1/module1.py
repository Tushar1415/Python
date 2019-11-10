#from PIL import Image
#import pytesseract
#import numpy as np

#img = Image.open(r"C:\Users\VISHAL\source\repos\PythonApplication1\PythonApplication1\Captcha1.png")
#data = np.array(img)

#converted = np.where(data == 255, 0, 255)

#img = Image.fromarray(converted.astype('uint8'))
#img.save('new_pic.png')

#pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
#print(pytesseract.image_to_string(Image.open(r"C:\Users\VISHAL\source\repos\PythonApplication1\PythonApplication1\test.jpg")))



#!/usr/bin/python
from PIL import Image
import cv2
import sys

img = Image.open(r"C:\Users\VISHAL\source\repos\PythonApplication1\PythonApplication1\Captcha1.png")

lower = np.array([128,128,128])  #-- Lower range --
upper = np.array([244,244,244])  #-- Upper range --
mask = cv2.inRange(img, lower, upper)
res = cv2.bitwise_and(img, img, mask= mask)  #-- Contains pixels having the gray color--
cv2.imshow('Result',res)
