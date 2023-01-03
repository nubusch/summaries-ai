import numpy as np
import pytesseract
from PIL import ImageEnhance, Image, ImageShow
import cv2
import fitz

img = Image.open(r'outfile.png')


#img = ImageEnhance.Brightness(img).enhance(0.5)
img = ImageEnhance.Contrast(img).enhance(3)
img = ImageEnhance.Sharpness(img).enhance(3)

ImageShow.show(img)

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract'

text = pytesseract.image_to_string(img)

# Displaying the extracted text
print(text[:-1])



