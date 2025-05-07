import pydirectinput,time,pyautogui
from random import randint
time.sleep(2)
Sx,Sy= 900,400
Ex,Ey=600,300
Allkeys=['q','w','e','r']
SmallSleep,BigSleep=0.5,1
while True:
    pyautogui.moveTo(randint(Ex,Sx),randint(Ey,Sy))
    time.sleep(SmallSleep)
    pydirectinput.press('space')
    time.sleep(SmallSleep)
    for key in Allkeys:
            pydirectinput.press(key)
            time.sleep(0.5)
    time.sleep(BigSleep)

