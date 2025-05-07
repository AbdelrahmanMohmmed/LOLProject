import pyautogui, time, pyscreeze


CONFIDENCE_LEVEL = 0.7
SEARCH_INTERVAL = 0.5

def TryEnterGame():
    print('trying Enter Game')
    arr = ['findMatch.png', 'accept.png','playAgain.png','continue.png','party.png','confirm.png']
    accept_button_location=None
    for photo in arr:
        try:
            accept_button_location = pyscreeze.locateOnScreen(
                f"images/{photo}", confidence=CONFIDENCE_LEVEL)
            if accept_button_location:
                print(f"Detected {photo} at: {accept_button_location}")
                accept_button_center = pyautogui.center(accept_button_location)
                pyautogui.click(accept_button_center)
        except Exception as e:
            time.sleep(0.1)

def CheckenterGame():
    accept_button_location = None
    arr2 = ['goingTop.png','goingTop2.png','goingTop3.png','goingTop4.png','goingDown5.png','goingDown6.png','goingDown.png','goingDown2.png','goingDown3.png','goingDown4.png']
    for photo in arr2:
        try:
            accept_button_location = pyscreeze.locateOnScreen(
                f"images/{photo}", confidence=CONFIDENCE_LEVEL)
            if accept_button_location:
                print("IN GAME !!")
                return photo
        except Exception as e:
            print("not in game")
            time.sleep(0.1)

def CheckWinGame():
    accept_button_location = None
    arr2 = ['ok.png','continue.png']
    for photo in arr2:
        try:
            accept_button_location = pyscreeze.locateOnScreen(
                f"images/{photo}", confidence=CONFIDENCE_LEVEL)
            if accept_button_location:
                accept_button_center = pyautogui.center(accept_button_location)
                pyautogui.click(accept_button_center)
                print("WON")
                return True
        except Exception as e:
            time.sleep(0.3)
    return False
if __name__ == '__main__':
    time.sleep(2)
    while True:
        TryEnterGame()
        time.sleep(SEARCH_INTERVAL)