from weapon import *
#klasa lika

class Player(pygame.sprite.Sprite):
    def __init__(self, image_name='images/players/player.png'):
        self.image = pygame.image.load(image_name)                  #dodajemo mu sliku
        self.rect = self.image.get_rect()                           #uzimamo koordinate i velicinu slike (x,y,visina,sirina)
        self.set_position()                                         #poziv funkcije koji ka po difoltu stavi na sredinu
        self.weapon = Weapon(self.rect.left)
        self.life = LIFE
        self.score = 0


    def set_position(self, x=DISPLAY_WIDTH - 780 , y=DISPLAY_HEIGHT - 50):
        self.rect.centerx, self.rect.bottom = x, y
