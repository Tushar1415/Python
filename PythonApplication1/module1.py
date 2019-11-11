from PIL import Image
import pytesseract
import numpy as np 
import cv2

kernel = np.ones((2,2),np.uint8)
# load image
img = cv2.imread(r"C:\Users\VISHAL\source\repos\PythonApplication1\PythonApplication1\Captcha1.png")

# Convert BGR to HSV
hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

# define range of black color in HSV
lower_val = np.array([0,0,0])
upper_val = np.array([180,100,100])	#upper_val = np.array([179,100,125])[179,100,80]

# Threshold the HSV image to get only black colors
mask = cv2.inRange(hsv, lower_val, upper_val)

# Bitwise-AND mask and original image
res = cv2.bitwise_and(img,img, mask= mask)
# invert the mask to get black letters on white background
res2 = cv2.bitwise_not(mask)

# display image
#cv2.imshow("img", res)
#cv2.imshow("img2", res2)
#cv2.waitKey(0)
#cv2.destroyAllWindows()
cv2.imwrite(r"C:\Users\VISHAL\source\repos\PythonApplication1\PythonApplication1\Captcha1s.png",res2)

pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
print(pytesseract.image_to_string(Image.open(r"C:\Users\VISHAL\source\repos\PythonApplication1\PythonApplication1\Captcha1s.png")))

