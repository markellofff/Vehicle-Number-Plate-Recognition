import pytesseract
from database import *
from PIL import Image

img = Image.open("italic_test.png")

# the below command is to redirect the tesseract to see the path
# if you are on windows
# pytesseract.pytesseract.tesseract_cmd = "C:\\Program Files (x86)\\Tesseract-OCR\\tesseract.exe"

# if you are on linux
pytesseract.pytesseract.tesseract_cmd = "/usr/bin/tesseract"

result = pytesseract.image_to_string(img)
print("Text extracted by the OCR : ", result)
vehicle_no = result
'''
 search() is the user defined function for searching the Name and Address from the database module.
'''
search(vehicle_no)
