from PIL import Image
import pytesseract
print(pytesseract.image_to_string(Image.open('C:\\Users\\VISHAL\\source\repos\\PythonApplication1\\PythonApplication1\\Captcha1.png')))