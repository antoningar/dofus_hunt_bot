from utils import beep
import screenmanager
import apimanager
import movemanager
import uimanager
import keyboardmanager
import constantes
import huntmanager

import time
import sys

def isPosZaap(current_pos):
    return current_pos == constantes.POS_ZAAP

'''
    Permet d'aller chercher une nouvelle chasse au tresor
'''
def getNewHunt():
    main_region = screenmanager.getMainRegion()
    if main_region != None:
        out = screenmanager.giveupHunt(main_region) 
        if out == -1:
            print("Attente nécesssaire")
            return

    #screenmanager.doubleclick(constantes.POS_POPO)
    time.sleep(1)
    
    current_pos = constantes.POS_ZAAP
    movemanager.getHunt(current_pos)

def initHunt():
    main_region = screenmanager.getMainRegion()
    pos_flag = screenmanager.getPosFlag(main_region)
    current_pos = screenmanager.getCurrentPos()
    
    return pos_flag, current_pos, main_region

def startHunt():
    pos_flag, current_pos, main_region = initHunt()
    huntmanager.start(pos_flag, current_pos, main_region)

def start():
    while True:
        choice = uimanager.current_menu()
        keyboardmanager.alttab()
        if choice == 'n':
            getNewHunt()
        elif choice == 's':
            startHunt()