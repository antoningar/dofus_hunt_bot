from utils import beep
import screenmanager
import apimanager
import movemanager
import uimanager
import keyboardmanager
import constantes

import time
import sys

def initNewHunt():
    return screenmanager.getMainRegion()

def isPosZaap(current_pos):
    return current_pos == constantes.POS_ZAAP

'''
    Permet d'aller chercher une nouvelle chasse au tresor
'''
def getNewHunt():
    main_region = initNewHunt()
    if main_region != None:
        print("getMainRegion")
        out = screenmanager.giveupHunt(main_region) 
        if out == -1:
            print("Attente nécesssaire")
            return

    screenmanager.doubleclick(constantes.POS_POPO)
    time.sleep(1)
    
    current_pos = constantes.POS_ZAAP
    movemanager.getHunt(current_pos)

def start():
    while True:
        choice = uimanager.current_menu()
        keyboardmanager.alttab()
        if choice == 'n':
            getNewHunt()
        elif choice == 's':
            startHunt()
        keyboardmanager.alttab()
            
    '''
    #getNewHunt(pos_popo)
    pos_flag = screenmanager.getPosFlag(main_region)
    current_pos = uimanager.getCurrentPos()
    screenmanager.alttab()

    pos_popo = screenmanager.getPosPopo()

    while True:
        if pos_flag == None:
            screenmanager.goTonextStep(main_region)
            time.sleep(1)
            if screenmanager.isTimeToFight(main_region):
                beep(4000)
                break
            pos_flag = screenmanager.getPosFlag(main_region)

        print(pos_flag)
        current_region = screenmanager.getCurrentRegion(main_region, pos_flag)
        direction = screenmanager.findDirection(current_region)
        hint_label = screenmanager.getHint(pos_flag)

        print(hint_label)
        print(direction)

        if hint_label == '':
            print("LABEL VIDE")
            hint_label = "Sac"

        if 'Phorreur' in hint_label:
            beep(1000)
            beep(1000)
            print("PHORREUR")
            current_pos = uimanager.getCurrentPos()
            screenmanager.alttab()
            pos_flag = screenmanager.getPosFlag(main_region)
            continue

        hint = apimanager.getNextPos(current_pos, direction, hint_label)

        print(hint)

        current_pos = movemanager.move(direction, hint['d'], current_pos)
        screenmanager.validFlag(pos_flag)        
        time.sleep(1)
        pos_flag = screenmanager.getPosFlag(main_region)
    '''