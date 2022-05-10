from PIL import Image
import pytesseract
import os
pytesseract.pytesseract.tesseract_cmd = r'C:\Users\Indra\AppData\Local\Programs\Tesseract-OCR\tesseract.exe'

i = 1
for i in range(1, 9, 1):
    image = f'foto{i}.jpg'
    text = pytesseract.image_to_string(Image.open(image), lang="eng")
    print(text)
    print("start")

    #open text file
    text_file = open(f"foto{i}.txt", "w")
    
    #write string to file
    text_file.write(text)
    
    #close file
    text_file.close()