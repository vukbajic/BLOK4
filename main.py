from globalFunc import *
import time
from multiprocessing import  Process

#pocetak programa
pygame.init()
ball_List = ballToList()
NoCrash = True
gameOver = False
gameLoop(ball_List, NoCrash, gameOver)



