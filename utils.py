import winsound

DURATION = 250

def beep(frequency):
    winsound.Beep(frequency, DURATION)

def beepFight():
    beep(4000)

def beepPhorreur():
    beep(1000)
    beep(1000)