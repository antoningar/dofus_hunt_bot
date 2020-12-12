def getCurrentPos():
    pos = input('POSITION ACTUELLE :')
    return pos.split(',')

def current_menu():
    print("n pour prendre une nouvelle chasse")
    print("s pour commencer la chasse")
    return input('>>')