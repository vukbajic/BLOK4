from globals import *
#klasa lika, to sam sa neta uzeo
class Player(pygame.sprite.Sprite):
    def __init__(self):
        self.image = pygame.image.load('Small-mario2.png')          #dodajemo mu sliku
        self.rect = self.image.get_rect()                           #uzimamo koordinate i velicinu slike (x,y,visina,sirina)
        self.set_position()                                         #poziv funkcije koji ka po difoltu stavi na sredinu

    def set_position(self, x=DISPLAY_WIDTH / 2, y=DISPLAY_HEIGHT):
        self.rect.centerx, self.rect.bottom = x, y
