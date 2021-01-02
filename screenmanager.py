import pyautogui
import os
import random
from screen_search import *
from utils import beep
from imgmanager import imgToText
import constantes

RANDOM_RANGE = 150

def click(pos):
    pyautogui.click(pos)

def doubleclick(pos):
    moveMouse(pos)
    pyautogui.click(clicks=2, interval=0.25)

def takeScreenshot(region, path=constantes.TMP_SCREENSHOT):
    screenshot = pyautogui.screenshot(region=region)
    screenshot.save(path)

def locateOnScreen(img, region=None):
    return pyautogui.locateOnScreen(img, region=region, grayscale=True, confidence=0.8) 

def moveMouse(pos):
    pyautogui.moveTo(pos)

def getCurrentPos():
    pos = (15,68,84,31)
    takeScreenshot(pos)
    coord = imgToText(constantes.TMP_SCREENSHOT,True).split(',')[:2]

    x = int(coord[0])
    y = int(coord[1].replace('|',''))

    #EXCEPTIONS
    x = -77 if x == -717 else x

    print("pos : ")
    print([x,y])
    return [x,y]

def getMainRegion():
    pos = pyautogui.locateCenterOnScreen(constantes.IMG_CHASSE_TRESOR)
    if pos != None:
        left = pos[0] - 150
        top = pos[1] - 10
        width = 320
        heigth = pyautogui.size()[1] - top
        region = (left, top, width, heigth)
        takeScreenshot(region, constantes.TMP_IMG_MAIN_REGION)
        
        return region

def getPosFlag(main_region):
    pos = locateOnScreen(constantes.IMG_HINT, main_region)
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
    if locateOnScreen(constantes.IMG_RIGHT_ARROW, region) != None:
        return 'right'
    if locateOnScreen(constantes.IMG_LEFT_ARROW, region) != None:
        return 'left'
    if locateOnScreen(constantes.IMG_TOP_ARROW, region) != None:
        return 'top'
    if locateOnScreen(constantes.IMG_BOTTOM_ARROW, region) != None:
        return 'bottom'

def getHint(pos_hint):
    left = int(pos_hint[0]) - 250
    top = pos_hint[1] -3
    width = 250
    height = 25
    region = (left, top, width, height)

    takeScreenshot(region)
    return imgToText(constantes.TMP_SCREENSHOT,False)

def validFlag(pos):
    pyautogui.click(pos[0] + 12, pos[1] + 12)

def isTimeToFight(region):
    pos = locateOnScreen(constantes.IMG_FIGHT, region=region)
    if pos != None:
        return True
    return False

def goTonextStep(region):
    pos = locateOnScreen(constantes.IMG_NEXT, region=region)
    if pos != None:
        print("in")
        pyautogui.click(pos[0] + 5, pos[1] + 5)

def getPosPopo():
    screen = pyautogui.size()
    left = screen.width * 0.2
    top = screen.height * 0.85
    width = screen.width * 0.63 
    height = screen.height * 0.1
    region = (int(left), int(top), int(width), int(height))

    pos = pyautogui.locateCenterOnScreen(constantes.IMG_POPO, region=region)
    return pos

def giveupHunt(region):
    pos = (region[0] + region[2] - 20, region[1] + 40)
    click(pos)
    time.sleep(0.5)
    pos = pyautogui.locateCenterOnScreen(constantes.IMG_CANCEL_VALIDATION)
    pyautogui.click(pos)
    time.sleep(0.5)
    if locateOnScreen(constantes.IMG_CHASSE_TRESOR) != None:
        return -1

def clickInsideMalleDoor():
    screen = pyautogui.size()
    pos = (screen.width * 0.5, screen.height * 0.5)
    pyautogui.click(pos)

def clickOnMalleSecondMap():
    screen = pyautogui.size()
    pos = (screen.width * 0.74, screen.height * 0.44)
    pyautogui.click(pos)

def clickOnNewMissions():
    screen = pyautogui.size()
    pos = (screen.width * 0.55, screen.height * 0.45)
    pyautogui.click(pos)

def clickOnLevelMission():
    screen = pyautogui.size()
    pos = (screen.width * 0.6, screen.height * 0.48)
    pyautogui.click(pos)

def getOut():
    screen = pyautogui.size()
    pos = (screen.width * 0.19, screen.height * 0.77)
    pyautogui.click(pos)

#----------Deplacements----------#

def getRightPos():
    screen = pyautogui.size()
    return [screen.width * 0.9, (screen.height * 0.5) + random.randint(-RANDOM_RANGE,RANDOM_RANGE)]
    
def getLeftPos():
    screen = pyautogui.size()
    return [screen.width * 0.1, (screen.height * 0.5) + random.randint(-RANDOM_RANGE,RANDOM_RANGE)]

def getTopPos():
    screen = pyautogui.size()
    return [(screen.width * 0.5) + random.randint(-RANDOM_RANGE,RANDOM_RANGE), 31]

def getBottomPos():
    screen = pyautogui.size()
    return [(screen.width * 0.5) + random.randint(0,RANDOM_RANGE), screen.height - 160]
 
'''
    Exception lors des déplacements sur la map
'''

def getBworkPos():
    screen = pyautogui.size()
    return [screen.width * 0.4, screen.height * 0.5]

def getDragoeufsToDesacrees():
    screen = pyautogui.size()
    return [screen.width * 0.2, screen.height * 0.5]

def getDesacreesToDragoeuf():
    screen = pyautogui.size()
    return [screen.width * 0.75, screen.height * 0.75]

def getBworkPosOut():
    screen = pyautogui.size()
    return [screen.width * 0.60, screen.height * 0.4]

def getLeftPosMadrestam(pos):
    if pos == [8,4]:
        screen = pyautogui.size()
        return [screen.width * 0.1, (screen.height * 0.6) + random.randint(0,RANDOM_RANGE)]
    elif pos == [13,-1]:
        screen = pyautogui.size()
        return [screen.width * 0.1, (screen.height * 0.1)]

def getPosGoToCalanques():
    screen = pyautogui.size()
    return [screen.width * 0.75, screen.height * 0.15]

def getHighRightPos():
    screen = pyautogui.size()
    return [screen.width * 0.9, screen.height * 0.1]
  