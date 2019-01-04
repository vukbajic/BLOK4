from player import *
from ball import *
import random
import sys
import pygame
import  time
from globals import  *
from button import *



# napravimo novog igraca
player = Player()
check = False
def moving(checkL, checkD):

    (x,y,z,g) = player.weapon.rect

    #print(x,y,z,g)
    if checkL is True and x >= 10:
        player.rect = player.rect.move(-PLAYER_SPEED, 0)
        if player.weapon.isActive == True:
             player.weapon.rect = player.weapon.rect.move(-PLAYER_SPEED, 0)

    if checkD is True and x <= DISPLAY_WIDTH - 20:
        player.rect = player.rect.move(PLAYER_SPEED, 0)
        if player.weapon.isActive == True:
            player.weapon.rect = player.weapon.rect.move(PLAYER_SPEED, 0)



#funkcija koja ga pokrece
def movePlayer():
    checkD = False
    checkL = False
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit(0)


    keys = pygame.key.get_pressed()
    # moves hero with key presses

    if keys[pygame.K_LEFT]:
        checkL = True
    elif keys[pygame.K_RIGHT]:
        checkD = True
    elif keys[pygame.K_SPACE]:
        player.weapon.isActive = False
    elif keys[pygame.K_ESCAPE]:
        pygame.quit()
    elif keys[pygame.K_p]:
        pause()


    return (checkL, checkD)


def draw_player(player):
    gameDisplay.blit(player.weapon.image, player.weapon.rect)
    gameDisplay.blit(player.image, player.rect) #ovo je da nacrtamo lika


def make_ball(num,corx,cory,direction):         #ovo je vasa funkcija koju sam podelio na tri funkcije
    """                                         #ovo je funkcija koja pravi lopte
    Function to make a new, random ball.
    """
    global index
    ball = Ball(num,index)
    index =   index + 1


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
                if ball.y > DISPLAY_HEIGHT - BALL_SIZE[ball.num] or ball.y < 200:
                    ball.change_y *= -1
                if ball.x > DISPLAY_WIDTH - BALL_SIZE[ball.num] or ball.x < BALL_SIZE[ball.num]:
                    ball.change_x *= -1


            elif ball.num == 1:
                if ball.y > DISPLAY_HEIGHT - BALL_SIZE[ball.num] or ball.y < 250:
                    ball.change_y *= -1
                if ball.x > DISPLAY_WIDTH - BALL_SIZE[ball.num] or ball.x < BALL_SIZE[ball.num]:
                    ball.change_x *= -1


            elif ball.num == 2:
                if ball.y > DISPLAY_HEIGHT - BALL_SIZE[ball.num] or ball.y < 300:
                    ball.change_y *= -1
                if ball.x > DISPLAY_WIDTH - BALL_SIZE[ball.num] or ball.x < BALL_SIZE[ball.num]:
                    ball.change_x *= -1

            elif ball.num == 3:
                if ball.y > DISPLAY_HEIGHT - BALL_SIZE[ball.num] or ball.y < 350:
                    ball.change_y *= -1
                if ball.x > DISPLAY_WIDTH - BALL_SIZE[ball.num] or ball.x < BALL_SIZE[ball.num]:
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
        pygame.draw.circle(gameDisplay, BALL_COLORS[ball.num], [ball.x, ball.y], BALL_SIZE[ball.num])

    # --- Wrap-up
    # Limit to 60 frames per second
    pygame.time.delay(20)
    return (ball.x, ball.y)
    # Go ahead and update the screen with what we've drawn.
    #pygame.display.flip()


def crash(xP, yP, xB, yB):                      #funkcija proverava da li je doslo do sudara izmedju lopte i lika
    xP1 = xP                                    #x koordinata lika
    yP1 = yP                                    #y koordinata lika
    xP2 = xP + PLAYER_WIDTH                     #x1 koordinata, do je njegova "desna" strana

    xB1 = xB                                    #x koordinata lopte
    yB1 = yB + BALL_SIZE[0]                     #y koordinata + velicina lopte (donja strana lopte)
    xB2 = xB + BALL_SIZE[0]                     #x1 koordinata, desna strana lopte
                                                #tu cemo morati jos da nadogradimo da radi i za manje lopte

    if yP1 <= yB1 and xP2 >= xB1:               #tu proveravam da li se ukrstaju koordinate lika i lopte
        if xP1 <= xB2:
            return False                        #ako se ukrstaju onda vraca false
    if yP1 <= yB1 and xP1 <= xB2:
        if xP2 >= xB1:
            return False

    return True                                 #ako se ne ukrstaju onda True


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


def hit(xW, yW, ball_list):
    xW1 = xW
    yW1 = yW
    xW2 = xW + WEAPON_WIDTH

    for ball in ball_list:
        print("index: ",ball.index)

    for ball in ball_list:
        xB1 = ball.x
        yB1 = ball.y + BALL_SIZE[ball.num]
        xB2 = ball.x + BALL_SIZE[ball.num]

        if yW1 <= yB1 and xW2 >= xB1:  # tu proveravam da li se ukrstaju koordinate lika i lopte
            if xW1 <= xB2:
                ballSplit(ball, ball_list)

                # ako se ukrstaju onda vraca false
        elif yW1 <= yB1 and xW1 <= xB2:
            if xW2 >= xB1:
                ballSplit(ball, ball_list)


def ballSplit(ball, ball_list):
    player.weapon.rect = player.weapon.rect.move(0, DISPLAY_HEIGHT)
    player.weapon.isActive = True
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


def massage_to_screen(msg,color):
    font = pygame.font.SysFont(None, FONT_SIZE)
    screen_text = font.render(msg, True, color)
    gameDisplay.blit(screen_text, [DISPLAY_WIDTH/4, DISPLAY_HEIGHT/4])


def lifeNumber(life):
    font = pygame.font.SysFont(None,NUMBERLIFES_FONT_SIZE)
    screen_text = font.render(life,True,BLACK)
    gameDisplay.blit(screen_text, [50,50])


def gameLoop(ball_List, NoCrash, gameOver):

    while NoCrash:

        gameDisplay.fill(WHITE)
        lifeNumber(player.life.__str__())
        # printovi su samo zbog lakseg dibaga
        draw_player(player)

        (x, y, c, d) = player.rect
        (check1, check2) = movePlayer()
        moving(check1, check2)
        (xW, yW) = shot(player)
        (x1, y1) = moveBall(ball_List)
        hit(xW, yW, ball_List)

        NoCrash = crash(x, y, x1, y1)
        if not NoCrash and player.life >1:
            if player.life == 3:
                massage_to_screen("Oooops, be ceraful, two lifes remaining", RED)
            else:
                massage_to_screen("Oooops, be ceraful, one life remaining", RED)
            pygame.display.update()
            pygame.time.delay(1000)
            print(player.life)
            player.life -=1
            NoCrash = True
            ball_List = ballToList()



        gameOver = not NoCrash
        while gameOver == True:

            gameDisplay.fill(WHITE)
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
                        player.life = LIFE
                        ball_List = ballToList()




        pygame.display.update()
        clock.tick(30)

    pygame.quit()
    quit()


def pause():
    checkPause = False
    while(checkPause is not True):
        gameDisplay.fill(WHITE)
        massage_to_screen("PAUSE, PRESS 'O' TO CONTUNUE", RED)
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    quit()
                if event.key == pygame.K_o:
                   checkPause = True
            if event.type == pygame.QUIT:
                sys.exit(0)

def start_screen():

    bg = pygame.image.load("start_screen_background.jpg")

    while screen_check:
        gameDisplay.blit(bg, (0, 0))
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    quit()
            if event.type == pygame.QUIT:
                sys.exit(0)


        button("1 Player",630,20,140,50,YELLOW,RED,SinglePlayerAction)
        button("2 Players", 630, 85, 140, 50, YELLOW, RED)
        button("Tournamet", 630, 150, 140, 50, YELLOW, RED)
        button("Options", 630, 215, 140, 50, YELLOW, RED)


        pygame.display.update()

def SinglePlayerAction():
    ball_List = ballToList()
    NoCrash = True
    gameOver = False
    gameLoop(ball_List, NoCrash, gameOver)





