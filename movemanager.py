import screenmanager
import time
import keyboardmanager

def getClickPos(direction, current_pos):
    if direction == 'right':
        if current_pos == [-2,8]:
            pos = screenmanager.getBworkPosOut()
        else:
            pos = screenmanager.getRightPos()
        current_pos = (current_pos[0] + 1, current_pos[1])

    if direction == 'left':
        if current_pos == [-1,8]:
            pos = screenmanager.getBworkPos()
        elif current_pos == [-7,26]:
            pos = screenmanager.getDragoeufsToDesacrees()
        elif current_pos == [4,-8]:
            pos = screenmanager.getLeftPos()
            current_pos = (current_pos[0], current_pos[1] - 1)    
        else:
            pos = screenmanager.getLeftPos()
        current_pos = (current_pos[0] - 1, current_pos[1])

    if direction == 'top':
        pos = screenmanager.getTopPos()
        current_pos = (current_pos[0], current_pos[1] - 1)

    if direction == 'bottom':
        pos = screenmanager.getBottomPos()
        current_pos = (current_pos[0], current_pos[1] + 1)

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
def getHunt(pos):
    pos = moveClassic('right', 2, pos)
    screenmanager.clickInsideMalleDoor()
    time.sleep(4)
    screenmanager.clickOnMalleSecondMap()
    time.sleep(4)
    screenmanager.clickOnNewMissions()
    screenmanager.clickOnLevelMission()
    screenmanager.getOut()
    time.sleep(4)
    screenmanager.getOut()
    time.sleep(4)
    keyboardmanager.goToHavreSac()
    time.sleep(1)
    

    
    
