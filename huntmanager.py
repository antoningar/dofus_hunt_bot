import screenmanager
import movemanager
import keyboardmanager
import apimanager
import uimanager
import utils

import time

def start(pos_flag, current_pos, main_region):
    while True:
        if pos_flag == None:
            screenmanager.goTonextStep(main_region)
            time.sleep(1)
            if screenmanager.isTimeToFight(main_region):
                utils.beepFight()
                break
            pos_flag = screenmanager.getPosFlag(main_region)

        current_region = screenmanager.getCurrentRegion(main_region, pos_flag)
        direction = screenmanager.findDirection(current_region)
        hint_label = screenmanager.getHint(pos_flag)
        
        print("hint label de base")
        print(hint_label)

        #BUGS HIHI
        if hint_label == '':
            print("BUG LABEL VIDE")
            hint_label = "Sac"

        if hint_label == 'Souche quine repousse pas':
            print("BUG LABEL SOUCHE")
            hint_label = 'Souche qui ne repousse pas'

        if 'Raflot' in hint_label:
            print('BUG LABEL RAFIOT')
            hint_label = hint_label.replace('Raflot','Rafiot')
        
        if '\'Bijoutiers\"' in hint_label:
            print('BUG LABEL PANNEAU BIJOUTIER')
            hint_label = hint_label.replace('\'Bijoutiers\"','\"Bijoutiers\"')

        if 'Geuf' in hint_label:
            print('BUG LABEL GEUF')
            hint_label = hint_label.replace('Geuf','Oeuf')

        if 'Carbac' in hint_label:
            print('BUG LABEL Carbac')
            hint_label = hint_label.replace('Carbac','Corbac')

        if "Forgerons”" in hint_label:
            print('BUG LABEL Forgerons')
            hint_label = "Panneau \"Forgerons\""

        if "Bûcherons”" in hint_label or "Sculpteurs”" in hint_label:
            print('BUG LABEL BUCHERONS')
            hint_label = hint_label.replace("”",'"')

        if "Charette" in hint_label:
            print('BUG LABEL Charette')
            hint_label = hint_label.replace("Charette",'Charrette')

        if "Pamme" in hint_label:
            print('BUG LABEL Pamme')
            hint_label = hint_label.replace("Pamme",'Pomme')

        if "\'Bricoleurs" in hint_label:
            print('BUG LABEL BRICO')
            hint_label = hint_label.replace("\'Bricoleurs","\"Bricoleurs")

        if "Aveniurier" in hint_label:
            print('BUG LABEL AVENTURIER GELE')
            hint_label = hint_label.replace("Aveniurier","Aventurier")

        if "Pant" in hint_label:
            print('BUG LABEL PONT')
            hint_label = hint_label.replace("Pant","Pont")

        if "£Eolienne" in hint_label:
            print('BUG LABEL £Eolienne')
            hint_label = hint_label.replace("£",'')

        if "£olienne" in hint_label:
            print('BUG LABEL £olienne')
            hint_label = hint_label.replace("£",'E')

        if "GOssements" in hint_label:
            print('BUG LABEL GOssements')
            hint_label = hint_label.replace("G",'')

        if "Caisses empilées cachées par dl" in hint_label:
            print('BUG LABEL Caisses empilées cachées par dl')
            hint_label = hint_label[:-1]

        if "Dua d'étoiles de mer" in hint_label:
            print('BUG LABEL Dua d\'étoiles de mer')
            hint_label = hint_label.replace("Dua",'Duo')

        if "©bjet" in hint_label:
            print('BUG LABEL ©bjet')
            hint_label = hint_label.replace("©bjet",'Objet')

        if "perie" in hint_label:
            print('BUG LABEL perie')
            hint_label = hint_label.replace("perie",'perle')

        if "Squeletie" in hint_label:
            print('BUG LABEL Squeletie')
            hint_label = hint_label.replace("Squeletie",'Squelette')

        if "£chelle" in hint_label:
            print('BUG LABEL £chelle')
            hint_label = hint_label.replace("£chelle",'Echelle')

        if "£tendoir" in hint_label:
            print('BUG LABEL £tendoir')
            hint_label = hint_label.replace("£tendoir",'Etendoir')

        if "£tendoir" in hint_label:
            print('BUG LABEL £tendoir')
            hint_label = hint_label.replace("£tendoir",'Etendoir')

        if "Tailleurs”" in hint_label:
            print('BUG LABEL Tailleurs”')
            hint_label = hint_label.replace("Tailleurs”",'Tailleurs\"')

        if "Gutil" in hint_label:
            print('BUG LABEL Gutil')
            hint_label = hint_label.replace("Gutil",'Outil')

        if "…" in hint_label:
            print('BUG LABEL …')
            hint_label = hint_label.replace("…",'').strip()

        if "Poni" in hint_label:
            print('BUG LABEL Poni')
            hint_label = hint_label.replace("Poni",'Pont').strip()

        if "Ôssements" in hint_label:
            print('BUG LABEL Ôssements')
            hint_label = hint_label.replace("Ôssements",'Ossements').strip()

        if "Gssements" in hint_label:
            print('BUG LABEL Gssements')
            hint_label = hint_label.replace("Gssements",'Ossements').strip()

        if "maladorante" in hint_label:
            print('BUG LABEL maladorante')
            hint_label = hint_label.replace("maladorante",'malodorante').strip()

        if "Charretie" in hint_label:
            print('BUG LABEL Charretie')
            hint_label = hint_label.replace("Charretie",'Charrette')

        if "Charretie" in hint_label:
            print('BUG LABEL Charretie')
            hint_label = hint_label.replace("Charretie",'Charrette')

        if "Enirée" in hint_label:
            print('BUG LABEL Enirée')
            hint_label = hint_label.replace("Enirée",'Entrée')

        #FIN BUGS HIHI

        if 'Phorreur' in hint_label:
            utils.beepPhorreur()
            print("PHORREUR")
            return

        hint = apimanager.getNextPos(current_pos, direction, hint_label)
        
        print(direction)
        print(hint_label)
        print(hint)
        print(current_pos)

        current_pos = movemanager.move(direction, hint['d'], current_pos)
        
        screenmanager.validFlag(pos_flag)        
        time.sleep(1)
        pos_flag = screenmanager.getPosFlag(main_region)
