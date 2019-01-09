from globals import *

class Weapon(pygame.sprite.Sprite):
    def __init__(self):
        self.image = pygame.image.load('images/arrow.png')
        self.rect = self.image.get_rect()
        self.isActive = True
        self.set_position()

    def set_position(self, x=DISPLAY_WIDTH / 2, y=DISPLAY_HEIGHT+480):
        self.rect.centerx, self.rect.bottom = x, y


