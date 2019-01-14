from globals import *
import random

#pozadine
bg1 = pygame.image.load("images/backgrounds/background1.jpg")
bg2 = pygame.image.load("images/backgrounds/background2.jpg")
bg3 = pygame.image.load("images/backgrounds/background3.jpg")
bg4 = pygame.image.load("images/backgrounds/background4.jpg")
bg5 = pygame.image.load("images/backgrounds/background5.jpg")

#lista pozadina
bgs = []
bgs.append(bg1)
bgs.append(bg2)
bgs.append(bg3)
bgs.append(bg4)
bgs.append(bg5)


class level:
    def __init__(self):
        self.number = 1
        self.background = random.choice(bgs)
        #self.balls
        #self.SetBalls()

    #def SetBalls(self,previousLevel):

    def ChangeBackgorund(self):
        self.background = random.choice(bgs)    #pozadina se bira slucajnim izborom na pocetku svakog nivoa
