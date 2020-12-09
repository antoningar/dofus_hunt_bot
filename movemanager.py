import screenmanager
import time

def getClickPos(direction, current_pos):
    if direction == 'right':
        pos = screenmanager.getRightPos()
        current_pos = (str(int(current_pos[0]) + 1), current_pos[1])

    if direction == 'left':
        if current_pos == ['-1','8']:
            pos = screenmanager.getBworkPos()
        elif current_pos == ['-7','26']:
            pos = screenmanager.getDragoeufsToDesacrees()
        else:
            pos = screenmanager.getLeftPos()
        current_pos = (str(int(current_pos[0]) - 1), current_pos[1])

    if direction == 'top':
        pos = screenmanager.getTopPos()
        current_pos = (current_pos[0], str(int(current_pos[1]) - 1))

    if direction == 'bottom':
        pos = screenmanager.getBottomPos()
        current_pos = (current_pos[0], str(int(current_pos[1]) + 1))

    return pos, current_pos

def move(direction, length, pos):
    while length != 0:
        click_pos, pos = getClickPos(direction, pos)
        length = length - 1
        screenmanager.click(click_pos)
        time.sleep(6.5)
    return pos