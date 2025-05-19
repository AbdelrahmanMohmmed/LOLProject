from functions import *
from acceptgame import *

while True:
    goingdownPhoto = [f'goingDown{i}.png' for i in range(1,9)]
    inGame = CheckenterGame()
    if inGame:
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
    else:
        TryEnterGame()




