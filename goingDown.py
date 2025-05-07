import pydirectinput,time,pyautogui
from random import randint
time.sleep(2)
X = (300,800)
Y = (400,800)
Allkeys=['q','w','e','r']
SmallSleep,BigSleep=0.5,1
while True:
    pyautogui.moveTo(randint(X[0],X[1]),randint(Y[0],Y[1]))
    time.sleep(SmallSleep)
    pydirectinput.press('space')
    time.sleep(SmallSleep)
    for key in Allkeys:
            pydirectinput.press(key)
            time.sleep(0.5)
    time.sleep(BigSleep)
