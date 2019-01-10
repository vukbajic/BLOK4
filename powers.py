from globals import *

lifePowerImage = pygame.image.load("images/powers/heart.png")
clockPowerImage = pygame.image.load("images/powers/clock.png")
coinPowerImage = pygame.image.load("images/powers/coin.png")

class power():
    def __init__(self, image_name):
        self.image = pygame.image.load(image_name)  # dodajemo mu sliku
        self.rect = self.image.get_rect()  # uzimamo koordinate i velicinu slike (x,y,visina,sirina)
        self.set_position()  # poziv funkcije koji ka po difoltu stavi na sredinu

    def set_position(self, x=DISPLAY_WIDTH / 2, y=DISPLAY_HEIGHT - 50):
            self.rect.centerx, self.rect.bottom = x, y

def generatePowerList():
    powers = []
    power1 = power(lifePowerImage)
    power2 = power(clockPowerImage)
    power3 = power(coinPowerImage)
    powers.append(power1)
    powers.append(power2)
    powers.append(power3)

    return powers

def generateRandomPower():
    powers = generatePowerList()
    global timer,gameDisplay
    if timer % 10:
        index = random(0,2)
        currentPower = powers[index]
        gameDisplay.blit(currentPower.image, currentPower.rect)  # ovo je da nacrtamo lika

