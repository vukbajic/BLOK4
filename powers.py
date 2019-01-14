from globals import *
from random import randint
from math import fmod

lifePowerImage = "images/powers/heart.png"
clockPowerImage = "images/powers/clock.png"
coinPowerImage = "images/powers/coin.png"

class power():
    def __init__(self, image_name):
        self.image = pygame.image.load(image_name)  # dodajemo mu sliku
        self.rect = self.image.get_rect()  # uzimamo koordinate i velicinu slike (x,y,visina,sirina)
        self.name = ""
        self.set_position()  # poziv funkcije koji ka po difoltu stavi na sredinu

    def set_position(self, x=500, y=500):
            self.rect.centerx, self.rect.bottom = x, y

def generatePowerList():        #generise neki od bonusa po verovatnoci 1:1:2
    powers = []
    power1 = power(lifePowerImage)
    power1.name = "life"
    power2 = power(clockPowerImage)
    power2.name = "time"
    power3 = power(coinPowerImage)
    power3.name = "score"
    power4 = power(coinPowerImage)
    power4.name = "score"
    powers.append(power1)
    powers.append(power2)
    powers.append(power3)
    powers.append(power4)

    return powers

def generateRandomPower(timer,players):     #na svakih 10 sekindu na slcuajnom mestu definise "slucajan" bonus
    powers = generatePowerList()
    global gameDisplay,allowPower,start_time,currentPower,TIME_PER_LEVEL
    timer = int(timer)
    timerCheck = False

   # mod = randint(15,20)
    if allowPower:
        if timer % 10 == 0 and timer != 0 and timer != TIME_PER_LEVEL and timer != start_time:
            start_time = timer
            index = randint(0,3)
            currentPower = powers[index]
            randX = randint(25,775)
            currentPower.set_position(randX,500)
            allowPower = False

    else:
        gameDisplay.blit(currentPower.image, currentPower.rect)  # iscrtava bonus na ekran
        allowPower = False
        if start_time - int(timer) >= 4:
            allowPower = True
        check,player = checkCoordinates(currentPower,players)
        if check:
             timerCheck = applayPower(currentPower,player,timer)

    return  timerCheck


def checkCoordinates(currentPower,players): #proverava da li je neki od likova "sakupio" bonus

    global  start_time

    for player in players:
        xPlayerLeft = player.rect.left
        xPlayerRight = player.rect.right

        xPowerLeft = currentPower.rect.left
        xPowerRight = currentPower.rect.right

        if xPlayerLeft <= xPowerLeft and xPlayerRight >= xPowerLeft:
            if xPowerLeft <= xPowerRight:
                start_time = 0
                return True,player

        if xPlayerLeft <= xPowerLeft and xPlayerLeft <= xPowerRight:
            if xPowerRight <= xPowerLeft:
                start_time = 0
                return True,player

    return False,None

def applayPower(power,player,timer):        #u slucaju "sakupljanja", primenjuje bonus na igraca
    global allowPower
    allowPower = True
    if power.name == "life":
        player.life += 1
    elif power.name == "time":
        return True
    elif power.name == "score":
        player.score += 50

    return False

