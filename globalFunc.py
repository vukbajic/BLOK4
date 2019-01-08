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


check = False


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




def make_ball(num,corx,cory,direction):         #ovo je vasa funkcija koju sam podelio na tri funkcije
    """                                         #ovo je funkcija koja pravi lopte
    Function to make a new, random ball.
    """
    global index
    #img = pygame.image.load('images/players/player.png')
    ball = Ball(num, index, 'images/players/player.png')
    index+=1


    # Starting position of the ball.
    # Take into account the ball size so we don't spawn on the edge.
    ball.x = corx
    ball.y = cory

    # Speed and direction of rectangle

    ball.change_x = direction
    ball.change_y = 4

    return ball


def ballToList():                               #tu lopte kreiramo i ubacujemo u listu koju prosledjujemo funkciji
    ball_list = []                              #u kojoj se krecu
    global index
    index = 0
    ball = make_ball(0,150,250,1)
    ball.new = False
    ball_list.append(ball)
    return ball_list


def moveBall(ball_list):                        #samo ime kaze, lopte se krecu

    for ball in ball_list:
        # Move the ball's center
        ball.x += ball.change_x * 2
        ball.y += ball.change_y * 2

        if ball.new is not True and ball.num <= 3:
            if ball.num == 0:
                if ball.y > DISPLAY_HEIGHT - BALL_SIZE[ball.num] - 55 or ball.y < 200:
                    ball.change_y *= -1
                if ball.x > DISPLAY_WIDTH - BALL_SIZE[ball.num] or ball.x < BALL_SIZE[ball.num]:
                    ball.change_x *= -1


            elif ball.num == 1:
                if ball.y > DISPLAY_HEIGHT - BALL_SIZE[ball.num] - 55 or ball.y < 250:
                    ball.change_y *= -1
                if ball.x > DISPLAY_WIDTH - BALL_SIZE[ball.num] or ball.x < BALL_SIZE[ball.num]:
                    ball.change_x *= -1


            elif ball.num == 2:
                if ball.y > DISPLAY_HEIGHT - BALL_SIZE[ball.num] - 55 or ball.y < 300:
                    ball.change_y *= -1
                if ball.x > DISPLAY_WIDTH - BALL_SIZE[ball.num] or ball.x < BALL_SIZE[ball.num]:
                    ball.change_x *= -1

            elif ball.num == 3:
                if ball.y > DISPLAY_HEIGHT - BALL_SIZE[ball.num] - 55 or ball.y < 350:
                    ball.change_y *= -1
                if ball.x > DISPLAY_WIDTH - BALL_SIZE[ball.num]  or ball.x < BALL_SIZE[ball.num]:
                    ball.change_x *= -1

        if ball.num <= 3 and ball.new is True:
            if ball.num == 0:
                if ball.y > 200:
                    ball.new = False
            elif ball.num == 1:
                if ball.y > 250:
                    ball.new = False
            elif ball.num == 2:
                if ball.y > 300:
                    ball.new = False
            elif ball.num == 3:
                if ball.y > 350:
                    ball.new = False

    # Draw the balls
    for ball in ball_list:
       # pygame.draw.circle(gameDisplay, BALL_COLORS[ball.num], [ball.x, ball.y], BALL_SIZE[ball.num])
        img = pygame.image.load('images/balls/ball.png')
        img = pygame.transform.scale(img, (50, 50))
        rect = img.get_rect()
        rect = rect.move((ball.x, ball.y))

        x = ball.x - 29
        y = ball.y - 23
        #images/balls/ball.png
       # rect = ball.get_rect()
        #proveravam okvire lopte. ovako sam uspeo da nastimam okvir samo prve, velike lopte..
        #mislim da bi bilo bolje da umesto sto crtamo loptu da ubacimo sliku njenu, tu se lakse prate okviri
        ###############################################################################################################
        life = '.'
        font = pygame.font.SysFont(None, 50)
        screen_text = font.render(life, True, BLACK)

       # x = ball.x
       # y = ball.y
        gameDisplay.blit(img,(x,y))

        gameDisplay.blit(screen_text, [ball.x - (BALL_SIZE[ball.num] ), ball.y-BALL_SIZE[ball.num]*1.5]) #levo gore
        gameDisplay.blit(screen_text, [ball.x + BALL_SIZE[ball.num] / 2, ball.y]) #desno dole
        gameDisplay.blit(screen_text, [ball.x + BALL_SIZE[ball.num] / 2, ball.y -BALL_SIZE[ball.num]*1.5]) #desno gore
        gameDisplay.blit(screen_text, [ball.x - (BALL_SIZE[ball.num] ), ball.y]) #LEVO DOLE
        #gameDisplay.bilt(img, )

        ###############################################################################################################

    # Limit to 20 frames per second
    pygame.time.delay(20)


def crash(xP, yP, ball_List):                           #funkcija proverava da li je doslo do sudara izmedju lopte i lika
    for ball in ball_List:
        xP1 = xP                                        #x koordinata lika
        yP1 = yP -20                                    #y koordinata lika
        xP2 = xP + PLAYER_WIDTH                         #x1 koordinata, do je njegova "desna" strana

        xB1 = ball.x - BALL_SIZE[ball.num]              #x koordinata lopte
        yB1 = ball.y                                    #y koordinata
        xB2 = ball.x + BALL_SIZE[ball.num] / 2          #x1 koordinata, desna strana lopte

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


def hit(xW, yW, ball_list, player):
    xW1 = xW
    yW1 = yW
    xW2 = xW + WEAPON_WIDTH

    for ball in ball_list:
        xB1 = ball.x - BALL_SIZE[ball.num]              # x koordinata lopte
        yB1 = ball.y                                    # y koordinata
        xB2 = ball.x + BALL_SIZE[ball.num] / 2

        global checkSplit
        checkSplit = False

        if yW1 <= yB1 and xW2 >= xB1:  # tu proveravam da li se ukrstaju koordinate lika i lopte
            if xW1 <= xB2:
                weaponBack(player)
                if(checkSplit):
                    print(xW, yW, ball.x, ball.y)
                    ballSplit(ball, ball_list, player)
        elif yW1 <= yB1 and xW1 <= xB2:
            if xW2 >= xB1:
                weaponBack(player)
                if(checkSplit):
                    print(xW, yW, ball.x, ball.y)
                    ballSplit(ball, ball_list, player)

def weaponBack(player):
    player.weapon.rect = player.rect
    player.weapon.rect = player.weapon.rect.move(7, 0)
    player.weapon.isActive = True
    global checkSplit
    checkSplit = True


def ballSplit(ball, ball_list, player):

    player.score += 10
    ball_list.remove(ball_list[ball.index])

    for ball_temp in ball_list:
        if ball_temp.index > ball.index:
            ball_temp.index -= 1
    global index
    index -= 1

    if ball.num < 3:
        ball1 = make_ball(ball.num + 1, ball.x, ball.y, 1)
        ball_list.append(ball1)
        ball2 = make_ball(ball.num + 1, ball.x, ball.y, -1)
        ball_list.append(ball2)





def lifeNumber(players, multiplay):
    life = players[0].life.__str__()
    font = pygame.font.SysFont(None,NUMBERLIFES_FONT_SIZE)
    screen_text = font.render(life,True,BLACK)
    gameDisplay.blit(screen_text, [30,515])
    if multiplay:
        life1 = players[1].life.__str__()
        screen_text1 = font.render(life1, True, BLACK)
        gameDisplay.blit(screen_text1, [DISPLAY_WIDTH-30, 515])



def gameLoop(ball_List, NoCrash, gameOver, players, multiplay):

    global bg,bg1
    siljci = pygame.image.load("images/siljci.png")

    font = pygame.font.Font(None, 40)
    timer = 50
    dt = 0


    while NoCrash:

        gameDisplay.blit(bg1, (0, 500))
        gameDisplay.blit(bg, (0, 0))
        gameDisplay.blit(siljci, (0, -5))
        lifeNumber(players, multiplay)
        # printovi su samo zbog lakseg dibaga
        draw_player(players[0])
        sc = font.render(str(round(players[0].score, 0)), True, BLACK)
        gameDisplay.blit(sc, (200, 520))


        if multiplay:
            draw_player(players[1])
            sc2 = font.render(str(round(players[1].score, 0)), True, BLACK)
            gameDisplay.blit(sc2, (DISPLAY_WIDTH-200, 520))

        (x, y, c, d) = players[0].rect
        movePlayer(players, multiplay)
        (xW, yW) = shot(players[0])
        moveBall(ball_List)
        hit(xW, yW, ball_List, players[0])

        if multiplay:
            (x2, y2, c2, d2) = players[1].rect
            movePlayer(players, multiplay)
            (xW2, yW2) = shot(players[1])
            hit(xW2, yW2, ball_List, players[1])


        NoCrash = crash(x, y, ball_List)
        if not NoCrash and players[0].life >1:
            if players[0].life == 3:
                massage_to_screen("Oooops, be ceraful, two lifes remaining", RED)
            else:
                massage_to_screen("Oooops, be ceraful, one life remaining", RED)
            pygame.display.update()
            pygame.time.delay(1000)
            print(players[0].life)
            players[0].life -= 1
            NoCrash = True
            ball_List = ballToList()

        if multiplay:
            NoCrash = crash(x2, y2, ball_List)
            if not NoCrash and players[0].life > 1:
                if players[1].life == 3:
                    massage_to_screen("Oooops, be ceraful, two lifes remaining", RED)
                else:
                    massage_to_screen("Oooops, be ceraful, one life remaining", RED)
                pygame.display.update()
                pygame.time.delay(1000)
                print(players[1].life)
                players[1].life -= 1
                NoCrash = True
                ball_List = ballToList()



        gameOver = not NoCrash
        while gameOver == True:

            gameDisplay.blit(bg1, (0, 500))
            gameDisplay.blit(bg, (0, 0))
            massage_to_screen("Game over, press C to play again or ESC to quit", RED)
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
                        if multiplay:
                            players[1].life = LIFE
                        ball_List = ballToList()

        timer -= dt
        if timer <= 0:
            players[0].life -= 1

            if multiplay is True:
                players[1].life -= 1

            massage_to_screen("Time out, you can do it faster",RED)
            pygame.display.update()
            pygame.time.delay(2000)
            timer = 50




        txt = font.render(str(round(timer, 0)), True, BLACK)
        gameDisplay.blit(txt, (380, 520))
        pygame.display.flip()
        dt = clock.tick(30) / 1000  # / 1000 to convert to seconds.

        pygame.display.update()
        #clock.tick(30)

    pygame.quit()
    quit()





def start_screen():

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
        button("Tournamet", 630, 150, 140, 50, YELLOW, RED)
        button("Options", 630, 215, 140, 50, YELLOW, RED)


        pygame.display.update()

def SinglePlayerAction():
    player = Player()
    players = [Player()]
    players.append(player)
    ball_List = ballToList()
    NoCrash = True
    gameOver = False
    multiPlay = False
    gameLoop(ball_List, NoCrash, gameOver, players, multiPlay)

def MultiPlayerAction():
    players = [Player()]
    player2 = Player('images/players/player2.png')
    players.append(player2)
    i = 0
    for player in players:
        player.set_position(DISPLAY_WIDTH/3 * (i+1), DISPLAY_HEIGHT - 50)
        i+=1

    ball_List = ballToList()
    NoCrash = True
    gameOver = False
    multiPlay = True
    gameLoop(ball_List, NoCrash, gameOver, players, multiPlay)


