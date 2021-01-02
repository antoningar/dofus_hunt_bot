import screenmanager
import time
import keyboardmanager
import constantes

def getClickPos(direction, current_pos=['0','0']):
    if direction == 'right':
        if current_pos == [-2,8]:
            pos = screenmanager.getBworkPosOut()
            current_pos = [current_pos[0] + 1, current_pos[1]]
        elif current_pos == [7,-27]:
            pos = screenmanager.getPosGoToCalanques()
            current_pos = [current_pos[0] + 1, current_pos[1]]
        elif current_pos == [-81,-37]:
            pos = screenmanager.getRightPos()
            current_pos = [current_pos[0] + 1, current_pos[1]-1]
        elif current_pos == [-8,26]:
            pos = screenmanager.getDesacreesToDragoeuf()
            current_pos = [current_pos[0] + 1, current_pos[1]]
        elif current_pos == [-20,42]:
            pos = screenmanager.getHighRightPos()
            current_pos = [current_pos[0] + 1, current_pos[1]]
        else:
            pos = screenmanager.getRightPos()
            current_pos = [current_pos[0] + 1, current_pos[1]]

    if direction == 'left':
        if current_pos == [-1,8]:
            pos = screenmanager.getBworkPos()
            current_pos = [current_pos[0] - 1, current_pos[1]]
        elif current_pos == [-7,26]:
            pos = screenmanager.getDragoeufsToDesacrees()
            current_pos = [current_pos[0] - 1, current_pos[1]]
        elif current_pos == [4,-8]:
            pos = screenmanager.getLeftPos()
            current_pos = [current_pos[0], current_pos[1] - 1]
        elif current_pos == [8,-4] or current_pos == [13,-1] :
            pos = screenmanager.getLeftPosMadrestam(current_pos)
            current_pos = [current_pos[0] - 1, current_pos[1]]      
        else:
            pos = screenmanager.getLeftPos()
            current_pos = [current_pos[0] - 1, current_pos[1]]

    if direction == 'top':
        pos = screenmanager.getTopPos()
        current_pos = [current_pos[0], current_pos[1] - 1]

    if direction == 'bottom':
        pos = screenmanager.getBottomPos()
        current_pos = [current_pos[0], current_pos[1] + 1]

    return pos, current_pos

def move(direction, length, pos):
    while length != 0:
        click_pos, pos = getClickPos(direction, pos)
        length = length - 1
        screenmanager.click(click_pos)
        while screenmanager.getCurrentPos() != pos:
            time.sleep(1)
    return pos
    
def moveClassic(direction, length, pos):
    while length != 0:
        click_pos, pos = getClickPos(direction, pos)
        length = length - 1
        screenmanager.click(click_pos)
        time.sleep(5)
    return pos

def waitUntilImgPop(img):
    while not screenmanager.locateOnScreen(img):
        time.sleep(1)

def goToMalle():
    click_pos, pos = getClickPos('right')
    screenmanager.click(click_pos)
    waitUntilImgPop(constantes.IMG_MALLE_FIRST)

    screenmanager.click(click_pos)
    waitUntilImgPop(constantes.IMG_MALLE_SECOND)

def goToTakeHunt():
    screenmanager.clickInsideMalleDoor()
    waitUntilImgPop(constantes.IMG_INSIDE_MALLE_COULOIR)

    screenmanager.clickOnMalleSecondMap()
    waitUntilImgPop(constantes.IMG_INSIDE_MALLE_SALLE)

def takeHunt():
    screenmanager.clickOnNewMissions()
    screenmanager.clickOnLevelMission()

def getOut():
    screenmanager.getOut()
    waitUntilImgPop(constantes.IMG_INSIDE_MALLE_COULOIR)
    
    screenmanager.getOut()
    waitUntilImgPop(constantes.IMG_MALLE_SECOND)
    
    keyboardmanager.goToHavreSac()

'''
    A l'appel de cette fonction on est au zaap champs de cania
    donc on doit : 
        2 cases à droite
        rentrer dans la masion
        avancer
        clicker sur le coffre
        clicker sur le lvl
        sortir de la maison
'''
def getHunt():
    goToMalle()
    goToTakeHunt()
    takeHunt()
    getOut()
    

    
    
