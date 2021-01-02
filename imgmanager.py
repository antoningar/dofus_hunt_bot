import cv2
import pytesseract
import numpy as np

TMP_PATH = ".\\res\\tmp_tesseract.png"

def transform(img, isPos):
    img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    if isPos:
        ret, new_img = cv2.threshold(img, 127,255,cv2.THRESH_BINARY_INV)
    else:
        ret, new_img = cv2.threshold(img, 127,255,cv2.THRESH_BINARY)
    return new_img

def imgToText(path, isPos):
    img = cv2.imread(path)
    img = transform(img, isPos)
    cv2.imwrite(TMP_PATH, img)
    text = pytesseract.image_to_string(img,lang="fra")

    return text.strip().replace('.','')