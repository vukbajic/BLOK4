from globals import *

class Weapon(pygame.sprite.Sprite):
    def __init__(self,x):
        self.image = pygame.image.load('images/arrow.png')
        self.rect = self.image.get_rect()
        self.isActive = True                    #oruzje je isActive kad je moguce pucati (ako je False, znaci da je 'pucanj' u toku)
        self.set_position(x)

    def set_position(self, x=DISPLAY_WIDTH / 2, y=DISPLAY_HEIGHT+480):
        self.rect.centerx, self.rect.bottom = x, y


