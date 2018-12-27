import multiprocessing
import sys
import pygame
import os
from settings import *
from Oruzije import *
import testiranje
from multiprocessing import Process
import settings
from PyQt5.QtWidgets import  (QWidget, QApplication)
from PyQt5.QtGui import QPainter, QColor, QBrush
from PyQt5.QtCore import Qt

#pygame.init()

gameDisplay = pygame.display.set_mode((DISPLAYWIDTH, DISPLAYHEIGHT))
pygame.display.set_caption('Bubble trouble')
clock = pygame.time.Clock()

likImg = pygame.image.load('Small-mario2.png')

def lik(x,y):
    gameDisplay.blit(likImg, (x,y))

def whileLik(x, oruzije, y, x_change, gameDisplay):
    for event in pygame.event.get():
         if event.type == pygame.QUIT:
                pygame.quit()

         if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                x_change = -5
            elif event.key == pygame.K_RIGHT:
               x_change = 5
            elif event.key == pygame.K_ESCAPE:
                    crash = True
            elif event.key == pygame.K_SPACE:
               oruzije.update(x, gameDisplay)

         if event.type == pygame.KEYUP:
             if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                 x_change = 0
    print(x)
    print(x_change)
    if x <= DISPLAYWIDTH - lik_width and x >= 0:
        x += x_change
        if x < 0:
            x = 0
        elif x > DISPLAYWIDTH - lik_width:
            x = DISPLAYWIDTH - lik_width



    return x



def lik_Petlja():
    x = (DISPLAYWIDTH * 0.45)
    y = (DISPLAYHEIGHT * 0.8)


    x_change = 0
    crashed = False
    oruzije = Oruzije(5,10)
    lopte = testiranje.main(gameDisplay)
    gameDisplay.fill(white)
    lik(x, y)
    while not crashed:
        gameDisplay.fill(white)
        lik(x, y)
        x = whileLik(x, oruzije, y, x_change, gameDisplay)


        testiranje.whileLopta(lopte,gameDisplay,clock)



        pygame.display.update()


        clock.tick(60)


if __name__ == '__main__':
    pygame.init()

    #testiranje.main(gameDisplay)
    #processLik = Process(target=lik_Petlja())
    #processLik.start()
    lik_Petlja()
    pygame.quit()
    quit()

