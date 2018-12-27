import pygame
import settings
from settings import *


class Oruzije(pygame.sprite.Sprite):

    def __init__(self, x = 0, y = 0):
        self.is_active = False
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('arrow2.png')
        self.rect = self.image.get_rect(centerx = x, top = y)

    def update(self, x, gameDisplay):
        gameDisplay.blit(self.image, (x, DISPLAYHEIGHT- lik_high))
        y = DISPLAYHEIGHT
        while y > 100:
            gameDisplay.blit(self.image, (x, y-lik_high))
            y-= 1
            print(y)
            pygame.time.wait(1)
            pygame.display.update()

