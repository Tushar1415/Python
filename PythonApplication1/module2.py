from PIL import Image
import pytesseract
import numpy as np 
import cv2

kernel = np.ones((2,2),np.uint8)

string_path = "D:\\Captcha1\\Captcha"
i = 100
while i < 10972:
	string_path1 = string_path + str(i) + ".png"
	img = cv2.imread(string_path1)
	hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
	lower_val = np.array([0,0,0])
	upper_val = np.array([180,100,100])	#upper_val = np.array([179,100,125])
	mask = cv2.inRange(hsv, lower_val, upper_val)
	res = cv2.bitwise_and(img,img, mask= mask)
	res2 = cv2.bitwise_not(mask)
	string_path2 = string_path + str(i) + "s.png"
	cv2.imwrite(string_path2,res2)
	#pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
	#print(pytesseract.image_to_string(Image.open(string_path2)))
	i += 1





