import requests
import json

PATH_HINTS = ".\\res\\my_list_hints.txt"

def getLabelFromId(id):
    with open(PATH_HINTS, 'r', encoding='utf-8') as f:
        for line in f.readlines():
            values = line.strip().replace('\"','').replace(',','').split(':')
            current_id = int(values[0])
            current_label = values[1].strip().replace('\\','\"')
            
            if current_id == id:
                return current_label

def getHintFromJson(j, hint_label):
    for hint in j['hints']:
        if getLabelFromId(hint['n']) == hint_label:
            return hint

def getNextPos(current_pos, direction, hint_label):
    url = ("https://dofus-map.com/huntTool/getData.php?x=%s&y=%s&direction=%s&world=0&language=fr" % (int(current_pos[0]), int(current_pos[1]), direction))
    r = requests.get(url)
    response_json = r.json()
    hint = getHintFromJson(response_json, hint_label)
    return hint