from functions import *
from acceptgame import *

while True:
    goingdownPhoto = ['goingDown.png','goingDown2.png','goingDown3.png','goingDown4.png','goingDown5.png','goingDown6.png']
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




