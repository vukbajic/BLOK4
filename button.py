import pygame
from globals import *
from globalFunc import *


#msg - titl dugmeta
#x - pozicija na x osi
#y - pozicija na y osi
#w - sirina dugmeta
#h - duzina dugmeta
#ic - boja dugmeta
#ac - boja dugmeta kad mis predje preko njega
#action - funckija koja se izvrsava kada je dugme pritisnuto
#primer
#button("1 Player", 630, 20, 140, 50, YELLOW, RED, SinglePlayerAction)

def button(msg,x,y,w,h,ic,ac,action=None):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    if x+w > mouse[0] > x and y+h > mouse[1] > y:
        pygame.draw.rect(gameDisplay, ac,(x,y,w,h))
        if click[0] == 1 and action != None:
            action()
    else:
        pygame.draw.rect(gameDisplay, ic,(x,y,w,h))

    smallText = pygame.font.Font("freesansbold.ttf",20)
    textSurf, textRect = text_objects(msg, smallText)
    textRect.center = ( (x+(w/2)), (y+(h/2)) )
    gameDisplay.blit(textSurf, textRect)


def text_objects(text, font):
    textSurface = font.render(text, True, BLACK)
    return textSurface, textSurface.get_rect()
