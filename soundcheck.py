import winsound

def fanfare():
    winsound.Beep(523, 75)
    winsound.Beep(698, 75)
    winsound.Beep(880, 75)
    winsound.Beep(1046, 150)
    winsound.Beep(880, 75)
    winsound.Beep(1046, 200)

fanfare()