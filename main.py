
from functions import *
from acceptgame import *

counter = 0
conf = 0.65

while True:
    goingdownPhoto = [f'goingDown{i}.png' for i in range(1,9)]
    inGame = CheckenterGame(conf)
    isAf0k = isAfk()
    if inGame or counter>=2:
        if not inGame:
            X,Y = goingDown()
            print('warning unknown')
        else:
            if inGame in goingdownPhoto :
                print("goingDown")
                X,Y = goingDown()
            else:
                print("GoingUP")
                X,Y = goingTop()
        pucheitem()
        lockScreen()
        Playing(X,Y)
        inGame = None
        counter = 0
        conf =0.6
    elif isAf0k:
        lockScreen()
        time.sleep(0.5)
        lockScreen()
        conf = 0.55
        counter+=1
    else:
        TryEnterGame()




