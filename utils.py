import winsound

def beep(frequency):
    duration = 250
    winsound.Beep(frequency, duration)