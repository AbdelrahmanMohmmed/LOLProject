import pydirectinput,time,pyautogui
from random import randint
from  acceptgame import CheckWinGame
def pucheitem():
    pydirectinput.press('p')
    pyautogui.moveTo(600,600)
    pyautogui.rightClick()
    pydirectinput.press('enter')
    pydirectinput.press('esc')

def lockScreen():
    pydirectinput.press('y')

def goingDown():
    X = (300, 800)
    Y = (400, 800)
    return X,Y
def goingTop():
    X = (600,900)
    Y = (300,400)
    return X,Y

def Playing(X,Y):
    Allkeys = ['q', 'w', 'e', 'r']
    SmallSleep, BigSleep = 0.5, 1
    while True:
        pyautogui.moveTo(randint(X[0], X[1]), randint(Y[0], Y[1]))
        time.sleep(SmallSleep)
        pydirectinput.press('space')
        time.sleep(SmallSleep)
        for key in Allkeys:
            pydirectinput.press(key)
            time.sleep(0.5)
        pydirectinput.keyDown('ctrl')
        for key in Allkeys:
            pydirectinput.press(key)
        pydirectinput.keyUp('ctrl')
        time.sleep(BigSleep)
        if CheckWinGame():
            break