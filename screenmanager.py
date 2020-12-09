import cv2
import pyautogui
from screen_search import *
import os
import pytesseract
from utils import beep
import random

IMG_CHASSE_TRESOR = ".\\res\\CHASSE.png"
IMG_DEPART = ".\\res\\DEPART.png"
IMG_HINT = ".\\res\\HINT.png"
IMG_LEFT_ARROW = ".\\res\\LEFT_ARROW.png"
IMG_RIGHT_ARROW = ".\\res\\RIGHT_ARROW.png"
IMG_TOP_ARROW = ".\\res\\TOP_ARROW.png"
IMG_BOTTOM_ARROW = ".\\res\\BOTTOM_ARROW.png"
IMG_NEXT = ".\\res\\NEXT.png"
IMG_FIGHT = ".\\res\\FIGHT.png"
TMP_SCREENSHOT = ".\\res\\TMP.png"
TMP_IMG_MAIN_REGION = ".\\res\\TMP_MAIN_REGION.png"

RANDOM_RANGE = 150

def alttab():
    pyautogui.hotkey('alt','tab')

def click(pos):
    pyautogui.click(pos)

def takeScreenshot(region, path=TMP_SCREENSHOT):
    screenshot = pyautogui.screenshot(region=region)
    screenshot.save(path)

def locateOnScreen(img, region):
    return pyautogui.locateOnScreen(img, region=region, grayscale=True, confidence=0.8) 

def getMainRegion():
    pos = pyautogui.locateCenterOnScreen(IMG_CHASSE_TRESOR)
    if pos != None:
        left = pos[0] - 150
        top = pos[1] - 10
        width = 320
        heigth = pyautogui.size()[1] - top
        region = (left, top, width, heigth)
        takeScreenshot(region, TMP_IMG_MAIN_REGION)
        
        return region

def getPosFlag(main_region):
    pos = locateOnScreen(IMG_HINT, main_region)
    if pos != None:
        return pos

def getCurrentRegion(main_region, pos_hint):
    left = main_region[0]
    top = pos_hint[1] - 5
    width = main_region[2]
    height = 30

    region = (left, top, width, height)
    takeScreenshot(region)

    return region

def findDirection(region):
    if locateOnScreen(IMG_RIGHT_ARROW, region) != None:
        return 'right'
    if locateOnScreen(IMG_LEFT_ARROW, region) != None:
        return 'left'
    if locateOnScreen(IMG_TOP_ARROW, region) != None:
        return 'top'
    if locateOnScreen(IMG_BOTTOM_ARROW, region) != None:
        return 'bottom'

def getHint(pos_hint):
    left = int(pos_hint[0]) - 250
    top = pos_hint[1] -3
    width = 250
    height = 25
    region = (left, top, width, height)

    takeScreenshot(region)
    return imgToText(TMP_SCREENSHOT)

def imgToText(img):
    img = cv2.imread(img)
    img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    text = pytesseract.image_to_string(img,lang="fra")

    return text.strip().replace('.','')

def getRightPos():
    screen = pyautogui.size()
    return (screen.width * 0.9, (screen.height * 0.5) + random.randint(-RANDOM_RANGE,RANDOM_RANGE))
    

def getLeftPos():
    screen = pyautogui.size()
    return (screen.width * 0.1, (screen.height * 0.5) + random.randint(-RANDOM_RANGE,RANDOM_RANGE))

def getTopPos():
    screen = pyautogui.size()
    return ((screen.width * 0.5) + random.randint(-RANDOM_RANGE,RANDOM_RANGE), 31) 

def getBottomPos():
    screen = pyautogui.size()
    return ((screen.width * 0.5) + random.randint(0,RANDOM_RANGE), screen.height - 160)

def validFlag(pos):
    pyautogui.click(pos[0] + 12, pos[1] + 12)

def isTimeToFight(region):
    pos = locateOnScreen(IMG_FIGHT, region=region)
    if pos != None:
        return True
    return False

def goTonextStep(region):
    pos = locateOnScreen(IMG_NEXT, region=region)
    if pos != None:
        print("in")
        pyautogui.click(pos[0] + 5, pos[1] + 5)

def getBworkPos():
    screen = pyautogui.size()
    return (screen.width * 0.4, screen.height * 0.5)

def getDragoeufsToDesacrees():
    screen = pyautogui.size()
    return (screen.width * 0.2, screen.height * 0.5)
