#potrebne reference na spoljne biblioteke
from player import *
from ball import *
import random
import sys
import pygame
import  time
from globals import  *
from button import *
from message_print import *
from messageBox import *
from powers import *
from client import *
import socket,select,queue
import multiprocessing
import os

#logika za iscrtavanje i pomeranje igraca
#region player_logic
#check = False
def draw_player(player):                    #crta igraca i njegovo oruzije
    gameDisplay.blit(player.weapon.image, player.weapon.rect)
    gameDisplay.blit(player.image, player.rect) #ovo je da nacrtamo lika


#na osnovu kliknutog dugmeta pomera jednog ili drugog igraca levo ili desno
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

def weaponBack(player):
    player.weapon.rect = player.rect
    player.weapon.rect = player.weapon.rect.move(7, 0)
    player.weapon.isActive = True
    global checkSplit
    checkSplit = True

def lifeNumber(players, multiplay):
    life = players[0].life.__str__()
    font = pygame.font.SysFont(None, NUMBERLIFES_FONT_SIZE)
    screen_text = font.render(life, True, BLACK)
    gameDisplay.blit(screen_text, [30, 515])
    global online
    if multiplay or online:
        life1 = players[1].life.__str__()
        screen_text1 = font.render(life1, True, BLACK)
        gameDisplay.blit(screen_text1, [DISPLAY_WIDTH - 30, 515])

#endregion  #

#logika za iscrtavanje, pomeranje i deljenje lopte
#region ball_logic
def make_ball(num,corx,cory,direction):         #ovo je vasa funkcija koju sam podelio na tri funkcije

    global index

    ball = Ball(num, index, corx, cory)
    index+=1
    gameDisplay.blit(ball.image,[corx,cory])

    ball.change_x = direction
    ball.change_y = BALL_SPEED[num]

    return ball


def ballToList():                               #tu lopte kreiramo i ubacujemo u listu koju prosledjujemo funkciji
    ball_list = []                              #u kojoj se krecu
    global index
    index = 0

    global level_ball_size,level_ball_count

    for i  in range(0,level_ball_count):
        ball = make_ball(level_ball_size,350,350,1*-1^i)    #pravi loptu odredjene velicine
        ball.new = False
        ball_list.append(ball)

    return ball_list


def moveBall(ball_list):                        #samo ime kaze, lopte se krecu

    for ball in ball_list:
        # Move the ball's center
        ball.rect = ball.rect.move((ball.change_x*2), (ball.change_y *2))

        gameDisplay.blit(ball.image, ball.rect)

        if ball.new is not True and ball.num <= 3:
            if ball.num == 0:
                if ball.rect.top > DISPLAY_HEIGHT - ball.rect.height - 55 or ball.rect.top < 200:
                    ball.change_y *= -1
                if ball.rect.left > DISPLAY_WIDTH - ball.rect.width or ball.rect.left < ball.rect.width:
                    ball.change_x *= -1


            elif ball.num == 1:
                if ball.rect.top > DISPLAY_HEIGHT - ball.rect.height - 55 or ball.rect.top < 250:
                    ball.change_y *= -1
                if ball.rect.left > DISPLAY_WIDTH - ball.rect.width or ball.rect.left < ball.rect.width:
                    ball.change_x *= -1


            elif ball.num == 2:
                if ball.rect.top > DISPLAY_HEIGHT - ball.rect.height - 55 or ball.rect.top < 300:
                    ball.change_y *= -1
                if ball.rect.left > DISPLAY_WIDTH - ball.rect.width or ball.rect.left < ball.rect.width:
                    ball.change_x *= -1

            elif ball.num == 3:
                if ball.rect.top > DISPLAY_HEIGHT - ball.rect.height - 55 or ball.rect.top < 350:
                    ball.change_y *= -1
                if ball.rect.left > DISPLAY_WIDTH - ball.rect.width or ball.rect.left < ball.rect.width:
                    ball.change_x *= -1

        if ball.num <= 3 and ball.new is True:      #posle dve najvece loptice, nastavljaju tri,cetiri, pet najvecih loptica po nivou...
            if ball.num == 0:
                if ball.rect.top > 200:
                    ball.new = False
            elif ball.num == 1:
                if ball.rect.top > 250:
                    ball.new = False
            elif ball.num == 2:
                if ball.rect.top > 300:
                    ball.new = False
            elif ball.num == 3:
                if ball.rect.top > 350:
                    ball.new = False

    # Limit to 20 frames per second
    pygame.time.delay(20)

def ballSplit(ball, ball_list, player):             #brise lopticu iz liste i ubacuje dve manje

    player.score += 10
    ball_list.remove(ball_list[ball.index])

    for ball_temp in ball_list:
        if ball_temp.index > ball.index:
            ball_temp.index -= 1
    global index
    index -= 1

    if ball.num < 3:            #ako je pogodjena loptica najmanja, ne deli se, inace, deli na dve manje
        ball1 = make_ball(ball.num + 1, ball.rect.left, ball.rect.top, 1)
        ball_list.append(ball1)
        ball2 = make_ball(ball.num + 1, ball.rect.left, ball.rect.top, -1)
        ball_list.append(ball2)


    global multiplay,online
    if len(ball_list) == 0:             #ako nema nsita u lisiti, znaci da je nivo gotov
        nextLevel(multiplay,online)



#endregion

#obrada sudaranja loptice i igraca i loptica i oruzja
#region collision
def crash(xP, yP, ball_List):                           #funkcija proverava da li je doslo do sudara izmedju lopte i lika
    for ball in ball_List:
        xP1 = xP                                        #x koordinata lika
        yP1 = yP -20                                    #y koordinata lika
        xP2 = xP + PLAYER_WIDTH                         #x1 koordinata, do je njegova "desna" strana

        xB1 = ball.rect.left             #x koordinata lopte
        yB1 = ball.rect.bottom - (ball.rect.height /(2 / (ball.num+1)))                                #y koordinata
        xB2 = ball.rect.right         #x1 koordinata, desna strana lopte

        if yP1 <= yB1 and xP2 >= xB1:                   #tu proveravam da li se ukrstaju koordinate lika i lopte
            if xP1 <= xB2:
                return False                            #ako se ukrstaju onda vraca false
        if yP1 <= yB1 and xP1 <= xB2:
            if xP2 >= xB1:
                return False

    return True                                         #ako se ne ukrstaju onda True


def shot(player):
    (x, y, z, g) = player.weapon.rect

    if player.weapon.isActive == False:
        if y >= 40:
            player.weapon.rect = player.weapon.rect.move(0, -WEAPON_SPEED)
        else:
            player.weapon.isActive = True
            player.weapon.rect = player.rect
            player.weapon.rect = player.weapon.rect.move(7, 0)  #7 jer je tako uvek na sredini coveculjka

    (x, y, z, g) = player.weapon.rect
    return (x, y)


def hit(ball_list, player):     #proverava da li je lopta pogodjena

    for ball in ball_list:
        xW1 = player.weapon.rect.left
        yW1 = player.weapon.rect.top
        xW2 = player.weapon.rect.right

        xB1 = ball.rect.left             # x koordinata lopte
        yB1 = ball.rect.bottom - (ball.rect.height /(2 / (ball.num+1)))                                  # y koordinata
        xB2 = ball.rect.right

        global checkSplit
        checkSplit = False

        if yW1 <= yB1 and xW2 >= xB1:  # tu proveravam da li se ukrstaju koordinate lika i lopte
            if xW1 <= xB2:
                weaponBack(player)
                if(checkSplit):
                    ballSplit(ball, ball_list, player)
        elif yW1 <= yB1 and xW1 <= xB2:
            if xW2 >= xB1:
                weaponBack(player)
                if(checkSplit):
                    ballSplit(ball, ball_list, player)


#endregion

#petlje koje pokrecu igru
#region loops
def gameLoopSingePlayer(ball_List,players, multiplay):

    NoCrash = True
    gameOver = False

    global bg1, dock, TIME_PER_LEVEL, level, timer,level_ball_size,level_ball_count
    siljci = pygame.image.load("images/siljci.png")


    font = pygame.font.Font(None, 40)
    fontTimer = pygame.font.Font(None, 50)
    timer = TIME_PER_LEVEL
    dt = 0
    timeOut = False

    while NoCrash:



        gameDisplay.blit(level.background, (0, 0))  #crta pozadinu
        gameDisplay.blit(siljci, (0, -5))           # crta siljke

        # printovi su samo zbog lakseg dibaga
        draw_player(players[0])                     #crta igraca
        gameDisplay.blit(dock, (0, 500))            # crta dok
        lifeNumber(players, multiplay)              #ispisuje broj zivota igraca
        sc = font.render("Score  " + str(round(players[0].score)), True, BLACK) #ispisuje skor
        gameDisplay.blit(sc, (140, 520))

        # (x, y, c, d) = players[0].rect
        movePlayer(players, multiplay)          #octivaa pomeranje igraca
        shot(players[0])                        #proverava pucanje
        moveBall(ball_List)                     #pomera loptu
        hit(ball_List, players[0])              #proverava pogodak



        NoCrash = crash(players[0].rect.left, players[0].rect.top, ball_List)       #proverava da li je loptica pogodila igraca
        # ako dodje do sudara i lik ima jos zivota
        if not NoCrash and players[0].life > 1:
            if players[0].life == 2:
                massage_to_screen("1 life remaining!", RED, -50, size="medium")  # menjao
                massage_to_screen("Be careful next time!", BLACK, 50, size="small")  # menjao
            else:
                massage_to_screen(str(players[0].life - 1) + " lifes remaining!", RED, -50, size="medium")  # menjao
                massage_to_screen("Be careful next time or you lose!", BLACK, 50, size="small")  # menjao
            timer = TIME_PER_LEVEL
            pygame.display.update()
            pygame.time.delay(1000)
            # print(players[0].life)
            players[0].life -= 1
            NoCrash = True
            ball_List = ballToList()

        if timeOut and players[0].life > 0:         #ako je vreme isteklo....
            if players[0].life == 1:
                massage_to_screen("Time out!", RED, -50, size = "large")
                massage_to_screen("1 life remaining!", BLACK, 50, size="medium")  # menjao
            else:
                massage_to_screen("Time out!", RED, -50, size="large")
                massage_to_screen(str(players[0].life - 1) +  " lifes remaining!", BLACK, 50, size="medium")  # menjao

            timer = TIME_PER_LEVEL
            pygame.display.update()
            pygame.time.delay(1000)
            timeOut = False
            ball_List = ballToList()

        if not timeOut:
            gameOver = not NoCrash

        while gameOver == True:

            gameDisplay.blit(dock, (0, 500))
            gameDisplay.blit(level.background, (0, 0))
            massage_to_screen("Game over", RED, -50, size="large")  # menjao
            massage_to_screen("Press C to play again or ESC to quit", BLACK, 50, size="small")  # menjao

            timer = TIME_PER_LEVEL
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        NoCrash = False
                        gameOver = False
                    if event.key == pygame.QUIT:
                        NoCrash = False
                        gameOver = False
                    if event.key == pygame.K_c:
                        print('C')
                        NoCrash = True
                        gameOver = False
                        players[0].life = LIFE
                        level.number = 1;
                        level_ball_size = 3
                        level_ball_count = 1
                        players[0].score = 0
                        ball_List = ballToList()


        timer -= dt             #smanji vreme svaki sekund
        if timer <= 0:
            if (players[0].life - 1 == 0):
                timeOut = True
                gameOver = True
            else:
                timeOut = True

            players[0].life -= 1

        txt = fontTimer.render(str(round(timer)), True, BLACK)
        gameDisplay.blit(txt, (380, 510))

        dt = clock.tick(30) / 1000  # / 1000 to convert to seconds.

        lvl = font.render(("Level:  " + str(round(level.number))), True, BLACK)
        gameDisplay.blit(lvl, (360, 20))

        timerCheck = generateRandomPower(timer,players)
        if timerCheck:
            timer += 10

        pygame.display.update()

    pygame.quit()
    quit()


def gameLoopMultiPlayer(ball_List, players, multiplay):

    NoCrash1 = True
    NoCrash2 = True
    gameOver1 = False
    gameOver2 = False

    global bg1,dock,TIME_PER_LEVEL,level,timer

    siljci = pygame.image.load("images/siljci.png")

    font = pygame.font.Font(None, 40)
    fontTimer = pygame.font.Font(None, 50)
    timer = TIME_PER_LEVEL
    dt = 0
    timeOut = False

    while NoCrash1 and NoCrash2:


        gameDisplay.blit(level.background, (0, 0))
        gameDisplay.blit(siljci, (0, -5))

        # printovi su samo zbog lakseg dibaga
        draw_player(players[0])
        draw_player(players[1])

        gameDisplay.blit(dock, (0, 500))
        lifeNumber(players, multiplay)
        sc = font.render("Score  " + str(round(players[0].score)), True, BLACK)
        sc2 = font.render("Score  " + str(round(players[1].score)), True, BLACK)
        gameDisplay.blit(sc, (140, 520))
        gameDisplay.blit(sc2, (DISPLAY_WIDTH - 260, 520))

        #(x, y, c, d) = players[0].rect
        movePlayer(players, multiplay)
        shot(players[0])
        moveBall(ball_List)
        hit(ball_List, players[0])
        movePlayer(players, multiplay)
        shot(players[1])
        hit(ball_List, players[1])


        NoCrash1 = crash(players[0].rect.left, players[0].rect.top, ball_List)
        #ako dodje do sudara i lik ima jos zivota
        if not NoCrash1 and players[0].life >1:
            if players[0].life == 2:
                massage_to_screen("1 life remaining!", RED, -50, size="medium")  # menjao
                massage_to_screen("Be careful next time!", BLACK, 50, size="small")  # menjao
            else:
                massage_to_screen(str(players[0].life - 1) +  " lifes remaining!", RED, -50, size="medium")  # menjao
                massage_to_screen("Be careful next time or you lose!", BLACK, 50, size="small")  # menjao
            timer = TIME_PER_LEVEL
            pygame.display.update()
            pygame.time.delay(1000)
            #print(players[0].life)
            players[0].life -= 1
            NoCrash1 = True
            setStartPosition(players, -18)
            ball_List = ballToList()


        NoCrash2 = crash(players[1].rect.left, players[1].rect.top, ball_List)
        if not NoCrash2 and players[1].life > 1:
            if players[1].life == 3:
                if players[0].life == 2:
                    massage_to_screen(
                        "1 life remaining!", RED, -50, size="medium")  # menjao
                    massage_to_screen("Be careful next time!", BLACK, 50, size="small")  # menjao
                else:
                    massage_to_screen(str(players[1].life - 1)  + " lifes remaining!", RED, -50, size="medium")  # menjao
                    massage_to_screen("Be careful next time or you lose!", BLACK, 50, size="small")  # menjao
            pygame.display.update()
            timer = TIME_PER_LEVEL
            pygame.time.delay(1000)
            players[1].life -= 1
            NoCrash2 = True
            setStartPosition(players, -18)
            ball_List = ballToList()

        if timeOut and players[0].life > 0:
            if players[0].life == 2:
                massage_to_screen("Time out!", RED, -50, size="large")
                massage_to_screen("Two lifes remaining!", BLACK, 50, size="medium")  # menjao
            else:
                massage_to_screen("Time out!", RED, -50, size="large")
                massage_to_screen("One life remaining!", BLACK, 50, size="medium")  # menjao

            timer = TIME_PER_LEVEL
            pygame.display.update()
            pygame.time.delay(1000)
            timeOut = False
            setStartPosition(players, -18)
            ball_List = ballToList()


        if not timeOut:
            gameOver1 = not NoCrash1
            gameOver2 = not NoCrash2

        while gameOver1 or gameOver2:

            gameDisplay.blit(dock, (0, 500))
            gameDisplay.blit(level.background, (0, 0))
            massage_to_screen("Game over", RED, -50, size="large")  # menjao
            massage_to_screen("Press C to play again or ESC to quit", BLACK, 50, size="small")  # menjao

            timer = TIME_PER_LEVEL


            if players[0].life == players[1].life:
                 massage_to_screen_down("DRAW", RED)
            elif players[0].life < players[1].life:
                 massage_to_screen_down("PLAYER 2 WINS", RED)
            else:
                massage_to_screen_down("PLAYER 1 WINS", RED)

            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        NoCrash1 = False
                        gameOver1 = False
                        NoCrash2 = False
                        gameOver2 = False
                    if event.key == pygame.QUIT:
                        NoCrash1 = False
                        gameOver1 = False
                        NoCrash2 = False
                        gameOver2 = False
                    if event.key == pygame.K_c:
                        print('C')
                        NoCrash1 = True
                        NoCrash2 = True
                        gameOver1 = False
                        gameOver2 = False
                        players[0].life = LIFE
                        players[1].life = LIFE
                        level.number = 1
                        level_ball_size = 3
                        level_ball_count = 1
                        players[0].score = 0
                        players[1].score = 0
                        setStartPosition(players, -18)
                        ball_List = ballToList()


        timer -= dt
        if timer <= 0:
            if(players[0].life - 1 == 0):
                timeOut = True
                gameOver1 = True
            else:
                timeOut = True

            players[0].life -= 1


            if (players[1].life - 1 == 0):
                timeOut = True
                gameOver2 = True
            else:
                timeOut = True
            players[1].life -= 1


        txt = fontTimer.render(str(round(timer)), True, BLACK)
        gameDisplay.blit(txt, (380, 510))

        dt = clock.tick(30) / 1000  # / 1000 to convert to seconds.

        lvl = font.render(("Level:  " + str(round(level.number))), True, BLACK)
        gameDisplay.blit(lvl, (360, 20))

        timerCheck = generateRandomPower(timer, players)
        if timerCheck:
            timer += 10

        pygame.display.update()

    pygame.quit()
    quit()



def onlineGameLoop(ball_List, players,online,addr,port,playerNum):
    NoCrash1 = True
    NoCrash2 = True
    gameOver1 = False
    gameOver2 = False

    global bg1, dock, TIME_PER_LEVEL, level, timer

    siljci = pygame.image.load("images/siljci.png")

    font = pygame.font.Font(None, 40)
    fontTimer = pygame.font.Font(None, 50)
    timer = TIME_PER_LEVEL
    dt = 0
    timeOut = False

    soc = setUpConnection(playerNum, addr, port)

    while NoCrash1 and NoCrash2:

        ExcangeCoords(soc, players, playerNum)
        #pygame.display.update()


        gameDisplay.blit(level.background, (0, 0))
        gameDisplay.blit(siljci, (0, -5))

        draw_player(players[0])
        draw_player(players[1])

        gameDisplay.blit(dock, (0, 500))
        lifeNumber(players, multiplay)


        sc = font.render("Score  " + str(round(players[0].score)), True, BLACK)
        gameDisplay.blit(sc, (140, 520))

        sc2 = font.render("Score  " + str(round(players[1].score)), True, BLACK)
        gameDisplay.blit(sc2, (DISPLAY_WIDTH - 260, 520))

        # (x, y, c, d) = players[0].rect
        movePlayer(players, online)
        shot(players[0])
        moveBall(ball_List)
        hit(ball_List, players[0])
        movePlayer(players, online)
        shot(players[1])
        hit(ball_List, players[1])

        NoCrash1 = crash(players[0].rect.left, players[0].rect.top, ball_List)
        # ako dodje do sudara i lik ima jos zivota
        if not NoCrash1 and players[0].life > 1:
            if players[0].life == 2:
                massage_to_screen("1 life remaining!", RED, -50, size="medium")  # menjao
                massage_to_screen("Be careful next time!", BLACK, 50, size="small")  # menjao
            else:
                massage_to_screen(str(players[0].life - 1) + " lifes remaining!", RED, -50, size="medium")  # menjao
                massage_to_screen("Be careful next time or you lose!", BLACK, 50, size="small")  # menjao
            timer = TIME_PER_LEVEL
            pygame.display.update()
            pygame.time.delay(1000)
            # print(players[0].life)
            players[0].life -= 1
            NoCrash1 = True
            setStartPosition(players, -18)
            ball_List = ballToList()

        NoCrash2 = crash(players[1].rect.left, players[1].rect.top, ball_List)
        if not NoCrash2 and players[1].life > 1:
            if players[1].life == 3:
                if players[0].life == 2:
                    massage_to_screen(1 + " life remaining!", RED, -50, size="medium")  # menjao
                    massage_to_screen("Be careful next time!", BLACK, 50, size="small")  # menjao
                else:
                    massage_to_screen(str(players[1].life - 1) + " lifes remaining!", RED, -50, size="medium")  # menjao
                    massage_to_screen("Be careful next time or you lose!", BLACK, 50, size="small")  # menjao
            pygame.display.update()
            timer = TIME_PER_LEVEL
            pygame.time.delay(1000)
            players[1].life -= 1
            NoCrash2 = True
            setStartPosition(players, -18)
            ball_List = ballToList()

        if timeOut and players[0].life > 0:
            if players[0].life == 2:
                massage_to_screen("Time out!", RED, -50, size="large")
                massage_to_screen("Two lifes remaining!", BLACK, 50, size="medium")  # menjao
            else:
                massage_to_screen("Time out!", RED, -50, size="large")
                massage_to_screen("One life remaining!", BLACK, 50, size="medium")  # menjao

            timer = TIME_PER_LEVEL
            pygame.display.update()
            pygame.time.delay(1000)
            timeOut = False
            setStartPosition(players, -18)
            ball_List = ballToList()

        if not timeOut:
            gameOver1 = not NoCrash1
            gameOver2 = not NoCrash2

        while gameOver1 or gameOver2:

            global tournament
            if tournament is not True:
                gameDisplay.blit(dock, (0, 500))
                gameDisplay.blit(level.background, (0, 0))
                massage_to_screen("Game over", RED, -50, size="large")  # menjao
                massage_to_screen("Press C to play again or ESC to quit", BLACK, 50, size="small")  # menjao

                timer = TIME_PER_LEVEL

                if players[0].life == players[1].life:
                    massage_to_screen_down("DRAW", RED)
                elif players[0].life < players[1].life:
                    massage_to_screen_down("PLAYER 2 WINS", RED)
                else:
                    massage_to_screen_down("PLAYER 1 WINS", RED)

                pygame.display.update()

                for event in pygame.event.get():
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_ESCAPE:
                            NoCrash1 = False
                            gameOver1 = False
                            NoCrash2 = False
                            gameOver2 = False
                        if event.key == pygame.QUIT:
                            NoCrash1 = False
                            gameOver1 = False
                            NoCrash2 = False
                            gameOver2 = False
                        if event.key == pygame.K_c:
                            print('C')
                            NoCrash1 = True
                            NoCrash2 = True
                            gameOver1 = False
                            gameOver2 = False
                            players[0].life = LIFE
                            players[1].life = LIFE
                            level.number = 1
                            level_ball_size = 3
                            level_ball_count = 1
                            players[0].score = 0
                            players[1].score = 0
                            setStartPosition(players, -18)
                            ball_List = ballToList()
            else:
                if playerNum == 0 and gameOver2 or playerNum == 1 and gameOver1:
                    gameDisplay.blit(dock, (0, 500))
                    gameDisplay.blit(level.background, (0, 0))
                    massage_to_screen("You win", RED, -50, size="large")  # menjao

                    timer = TIME_PER_LEVEL

                    if players[0].life == players[1].life:
                        massage_to_screen_down("DRAW", RED)
                    elif players[0].life < players[1].life:
                        massage_to_screen_down("PLAYER 2 WINS", RED)
                    else:
                        massage_to_screen_down("PLAYER 1 WINS", RED)

                    pygame.display.update()
                    print("Winner")
                    startTournament()

                else:
                    gameDisplay.blit(dock, (0, 500))
                    gameDisplay.blit(level.background, (0, 0))
                    massage_to_screen("Game over", RED, -50, size="large")  # menjao
                    massage_to_screen("Press C to play again or ESC to quit", BLACK, 50, size="small")  # menjao

                    timer = TIME_PER_LEVEL

                    if players[0].life == players[1].life:
                        massage_to_screen_down("DRAW", RED)
                    elif players[0].life < players[1].life:
                        massage_to_screen_down("PLAYER 2 WINS", RED)
                    else:
                        massage_to_screen_down("PLAYER 1 WINS", RED)

                    pygame.display.update()

        timer -= dt
        if timer <= 0:
            if (players[0].life - 1 == 0):
                timeOut = True
                gameOver1 = True
            else:
                timeOut = True

            players[0].life -= 1

            if (players[1].life - 1 == 0):
                timeOut = True
                gameOver2 = True
            else:
                timeOut = True
            players[1].life -= 1

        txt = fontTimer.render(str(round(timer)), True, BLACK)
        gameDisplay.blit(txt, (380, 510))

        dt = clock.tick(30) / 1000  # / 1000 to convert to seconds.

        lvl = font.render(("Level:  " + str(round(level.number))), True, BLACK)
        gameDisplay.blit(lvl, (360, 20))

        timerCheck = generateRandomPower(timer, players)
        if timerCheck:
            timer += 10

        pygame.display.update()

    pygame.quit()
    quit()

#endregion

#pocetne funkcije
#region start
def start_screen():
    global nextlvl
    nextlvl = False

    global players, multiPlay, level_ball_size, level_ball_count, level
    level_ball_size = 3
    level_ball_count = 1
    level.number = 1


    bg = pygame.image.load("images/backgrounds/start_screen_background.jpg")

    while screen_check:
        gameDisplay.blit(bg, (0, 0))
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    result = MessageBox("Exit", "Do you want to exit")
                    if result is True:
                        pygame.quit()
                        sys.exit(0)
            if event.type == pygame.QUIT:
                result = MessageBox("Exit", "Do you want to exit")
                if result is True:
                    pygame.quit()
                    sys.exit(0)


        button("1 Player",630,20,140,50,YELLOW,RED,SinglePlayerAction)
        button("2 Players", 630, 85, 140, 50, YELLOW, RED,MultiPlayerAction)
        button("Tournamet", 630, 150, 140, 50, YELLOW, RED,startTournament)
        button("Online", 630, 215, 140, 50, YELLOW, RED,startOnline)


        pygame.display.update()



def startTournament():
    global enemyAddr, enemyPort
    global tournament
    if tournament:
        enemyAddr, enemyPort = connect("Winner")
    else:
        enemyAddr, enemyPort = connect("tournament")
    global players
    players = [Player()]
    players.append(Player('images/players/player2.png'))
    tournament= True
    OnlineAction()


def startOnline():
    global enemyAddr,enemyPort
    enemyAddr, enemyPort = connect("Online_game")
    global players
    players = [Player()]
    players.append(Player('images/players/player2.png'))
    OnlineAction()

def setStartPosition(players, x):
    i = 0
    for player in players:
        player.weapon.set_position((DISPLAY_WIDTH - PLAYER_WIDTH*1.5) * i + PLAYER_WIDTH*1.5, DISPLAY_HEIGHT + x)
        player.set_position((DISPLAY_WIDTH - PLAYER_WIDTH * 1.5) * i + PLAYER_WIDTH, DISPLAY_HEIGHT - 50)
        i += 1


def SinglePlayerAction():
    global nextlvl, players, multiPlay
    if nextlvl is not True:
        player = Player()
        players = [Player()]
        players.append(player)
    ball_List = ballToList()
    multiPlay = False
    gameLoopSingePlayer(ball_List, players, multiPlay)

def MultiPlayerAction():

    global multiplay,players

    multiplay = True

    global nextlvl
    if nextlvl is not True:
         players = [Player()]
         player2 = Player('images/players/player2.png')
         players.append(player2)

    i = 0
    if nextlvl:
        setStartPosition(players, -18)
    else:
        setStartPosition(players, 480)


    ball_List = ballToList()

    multiPlay = True
    gameLoopMultiPlayer(ball_List,players, multiPlay)



def OnlineAction():

    global online,enemyAddr,enemyPort
    online = True
    global players
    ball_List = ballToList()

    addr = socket.gethostbyname(socket.gethostname())  # vraca ip adresu racunaras
    #addr = '127.0.0.1'  # vraca ip adresu racunaras
    playerNum = compareAddrs(MY_ADDR,enemyAddr,enemyPort)

    onlineGameLoop(ball_List,players,online,enemyAddr,enemyPort,playerNum)

#endregion

#logika sa online-mode igrice
#region onlineGame
def setUpConnection(playerNum, addr, port): #vraca soket za komunijaciju sa protivniom
    if playerNum == 0:
        server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        # server.setblocking(0)
        server.bind((MY_ADDR, MY_PORT))
        server.listen(5)

        s, client_address = server.accept()

        return s
    else:
        client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client.connect((addr, int(port)))

        return client


def ExcangeCoords(s, players, playerNum):       #razmena koordinata igraca i loptica, kao i skora i broja zivota u online modu
    if playerNum == 0:
        data = s.recv(1024)
        my_decoded_str = data.decode()
        type(my_decoded_str)

        cords = my_decoded_str.split("+")

        players[1].rect.left = int(cords[0])
        players[1].score = int(cords[1])
        players[1].life = int(cords[2])
        players[1].weapon.rect.left = int(cords[3])
        players[1].weapon.rect.right = int(cords[4])
        players[1].weapon.rect.top = int(cords[5])

        asStr = str(players[playerNum].rect.left) + "+" + str(players[playerNum].score) + "+" + str(
            players[playerNum].life) + "+" + str(players[playerNum].weapon.rect.left) + "+" + str(
            players[playerNum].weapon.rect.right) + "+" + str(players[playerNum].weapon.rect.top)
        asbYte = str.encode(asStr)
        type(asbYte)
        s.sendall(asbYte)

    else:
        asStr = str(players[playerNum].rect.left) + "+" + str(players[playerNum].score) + "+" + str(
            players[playerNum].life) + "+" + str(players[playerNum].weapon.rect.left) + "+" + str(
            players[playerNum].weapon.rect.right) + "+" + str(
            players[playerNum].weapon.rect.top)
        asByte = str.encode(asStr)
        print(asStr + "POSLAJO")
        type(asByte)
        s.sendall(asByte)

        data1 = s.recv(1024)
        asStr1 = data1.decode()
        type(asStr1)
        print(asStr1 + " PRIMIJO")
        cords = asStr1.split("+")

        players[0].rect.left = int(cords[0])
        players[0].score = int(cords[1])
        players[0].life = int(cords[2])
        players[0].weapon.rect.left = int(cords[3])
        players[0].weapon.rect.right = int(cords[4])
        players[0].weapon.rect.top = int(cords[5])

    return players

def compareAddrs(addr1,addr2,enemyPort):                #odredjue redni broj igraca na osnovu adrese ili porta

    addrInt1 = int(re.sub('[.]', '', addr1))
    addrInt2 = int(re.sub('[.]', '', addr2))

    if addr1 == addr2:                      #sluzi samo za testiranje na isom racunaru(ako je adresa ista, igrac sa vecim portom je prvi i server u komunijaciji
        if MY_PORT > int(enemyPort):
            print("ISTE")
            return 0
        else:
            return 1
    elif addrInt1 > addrInt2:                #veca adresa - igrac 1
        print("0")
        return 0
    else:
        print("1")
        return 1



#endregion

#zajednicke metode
#region common
def pause():
    checkPause = False
    global bg_one_color
    while(checkPause is not True):
        gameDisplay.blit(bg_one_color, (0, 0))
        massage_to_screen("PAUSE, PRESS 'O' TO CONTUNUE OR 'H' TO GO ON HOME SCREEN", RED)
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    result = MessageBox("Exit", "Do you want to exit")
                    if result is True:
                        pygame.quit()
                        sys.exit(0)
                if event.key == pygame.K_o:
                   checkPause = True
                if event.key == pygame.K_h:
                    global index
                    index = 0
                    start_screen()
            if event.type == pygame.QUIT:
                result = MessageBox("Exit", "Do you want to exit")
                if result is True:
                    pygame.quit()
                    sys.exit(0)


def nextLevel(multiplay,online):
    global level
    global nextlvl,level_ball_count,level_ball_size,allowPower
    allowPower = True
    nextlvl = True
    level.ChangeBackgorund()
    level.number += 1
    ball_List = ballToList()

    gameDisplay.blit(bg_one_color, (0, 0))
    massage_to_screen(("Next level: " + str(level.number)),RED, 0, size = "medium")
    pygame.display.update()
    pygame.time.delay(1000)

    if level_ball_size > 0:
        if level_ball_count == 2:
            level_ball_size -= 1
            level_ball_count = 1
        else:
            level_ball_count = 2
    else:
        level_ball_count += 1

    global players
    if online is True:
        for player in players:
            weaponBack(player)
        OnlineAction()
    elif multiplay is True:

        for player in players:
            weaponBack(player)
        MultiPlayerAction()
    else:
        SinglePlayerAction()

#endregion
