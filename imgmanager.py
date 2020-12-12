import cv2
import pytesseract
import numpy as np

def transform(path):
    img = cv2.imread(path)
    ret, new_img = cv2.threshold(img, 127,255,cv2.THRESH_BINARY_INV)
    return new_img

def imgToText(path):
    tmp_save = ".\\res\\tmp_tesseract.png"
    img = transform(path)
    text = pytesseract.image_to_string(img,lang="fra")

    return text.strip().replace('.','')