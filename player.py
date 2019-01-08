from globals import *
from weapon import *
from globalFunc import  *
from messageBox import *
from pause import  *
#klasa lika, to sam sa neta uzeo
class Player(pygame.sprite.Sprite):
    def __init__(self, image_name='images/players/player.png'):
        self.image = pygame.image.load(image_name)          #dodajemo mu sliku
        self.rect = self.image.get_rect()                           #uzimamo koordinate i velicinu slike (x,y,visina,sirina)
        self.set_position()                                         #poziv funkcije koji ka po difoltu stavi na sredinu
        self.weapon = Weapon()
        self.life = LIFE


    def set_position(self, x=DISPLAY_WIDTH / 2, y=DISPLAY_HEIGHT):
        self.rect.centerx, self.rect.bottom = x, y



def moving(checkL, checkD, player):

    (x,y,z,g) = player.rect

    if checkL is True and x >= 10:
        player.rect = player.rect.move(-PLAYER_SPEED, 0)
        if player.weapon.isActive == True:
             player.weapon.rect = player.weapon.rect.move(-PLAYER_SPEED, 0)

    if checkD is True and x <= DISPLAY_WIDTH - 20:
        player.rect = player.rect.move(PLAYER_SPEED, 0)
        if player.weapon.isActive == True:
            player.weapon.rect = player.weapon.rect.move(PLAYER_SPEED, 0)

    #proveravam okvire lika
    #########################################################################
    life = '.'
    font = pygame.font.SysFont(None, 50)
    screen_text = font.render(life, True, BLACK)
    gameDisplay.blit(screen_text, [x, y-20])
    gameDisplay.blit(screen_text, [x + PLAYER_WIDTH, y + PLAYER_HIGHT-20])
    gameDisplay.blit(screen_text, [x + PLAYER_WIDTH, y-20])
    gameDisplay.blit(screen_text, [x, y + PLAYER_HIGHT-20])
    #########################################################################


#funkcija koja ga pokrece
def movePlayer(players, multiplay):
    checkD = False
    checkL = False
    checkD2 = False
    checkL2 = False
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            result = MessageBox("Exit", "Do you want to exit")
            if result is True:
                pygame.quit()
                sys.exit(0)


    keys = pygame.key.get_pressed()
    # moves hero with key presses

    if keys[pygame.K_LEFT]:
        checkL = True
    elif keys[pygame.K_RIGHT]:
        checkD = True
    elif keys[pygame.K_SPACE]:
        players[0].weapon.isActive = False
    elif keys[pygame.K_ESCAPE]:
        result = MessageBox("Exit", "Do you want to exit")
        if result is True:
            pygame.quit()
            sys.exit(0)
    elif keys[pygame.K_p]:
        pause()

    if keys[pygame.K_a]:
        checkL2 = True
    elif keys[pygame.K_d]:
        checkD2 = True
    elif keys[pygame.K_w]:
        if multiplay:
            players[1].weapon.isActive = False

    moving(checkL, checkD, players[0])
    if multiplay:
        moving(checkL2, checkD2, players[1])


def draw_player(player):
    gameDisplay.blit(player.weapon.image, player.weapon.rect)
    gameDisplay.blit(player.image, player.rect) #ovo je da nacrtamo lika
