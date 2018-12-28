from player import *
from ball import *
import random


# napravimo novog igraca
player = Player()
check = False
def moving(checkL, checkD):

    (x,y,z,g) = player.weapon.rect

    #print(x,y,z,g)
    if checkL is True and x >= 0:
        player.rect = player.rect.move(-PLAYER_SPEED, 0)
        player.weapon.rect = player.weapon.rect.move(-PLAYER_SPEED, 0)

    if checkD is True and x <= DISPLAY_WIDTH - z:
        player.rect = player.rect.move(PLAYER_SPEED, 0)
        player.weapon.rect = player.weapon.rect.move(PLAYER_SPEED, 0)


#funkcija koja ga pokrece
def movePlayer():
    checkD = False
    checkL = False
    for event in pygame.event.get():

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT or event.key == ord('a'):
                checkL = True
                #rect su koordinate slike. sastoji se od (x,y,visine,sirine)
                #move je ugradjena funkcija po kojoj se kreces po x i y osi
            elif event.key == pygame.K_RIGHT or event.key == ord('d'):
                checkD = True



        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == ord('a'):
                checkL = False
            if event.key == pygame.K_RIGHT or event.key == ord('d'):
                checkD = False


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


    return (checkL, checkD)



def draw_player(player):
    gameDisplay.blit(player.weapon.image, player.weapon.rect)
    gameDisplay.blit(player.image, player.rect) #ovo je da nacrtamo lika


def make_ball(num,corx,cory,direction):         #ovo je vasa funkcija koju sam podelio na tri funkcije
    """                                         #ovo je funkcija koja pravi lopte
    Function to make a new, random ball.
    """
    ball = Ball(num)
    ball.index += 1
    # Starting position of the ball.
    # Take into account the ball size so we don't spawn on the edge.
    ball.x = corx
    ball.y = cory

    # Speed and direction of rectangle

    ball.change_x = direction
    ball.change_y = 3

    return ball

def ballToList():                               #tu lopte kreiramo i ubacujemo u listu koju prosledjujemo funkciji
    ball_list = []                              #u kojoj se krecu

    ball = make_ball(0, random.randrange(BALL_SIZE[0], DISPLAY_WIDTH - BALL_SIZE[0]),
                     random.randrange(100, DISPLAY_HEIGHT - BALL_SIZE[0]), 1)
    ball.new = False
    ball_list.append(ball)
    return ball_list

def moveBall(ball_list):                        #samo ime kaze, lopte se krecu

    for ball in ball_list:
        # Move the ball's center
        ball.x += ball.change_x
        ball.y += ball.change_y


        if ball.new is not True and ball.num <= 3:
        # Bounce the ball if needed
            if ball.y > DISPLAY_HEIGHT - BALL_SIZE[ball.num] or ball.y < 75 * (ball.num + 1):
                ball.change_y *= -1
            if ball.x > DISPLAY_WIDTH - BALL_SIZE[ball.num] or ball.x < BALL_SIZE[ball.num]:
                ball.change_x *= -1

        if ball.y > 75 * ball.num + 1:
            ball.new = False

    # Draw the balls
    for ball in ball_list:
        pygame.draw.circle(gameDisplay, BLACK, [ball.x, ball.y], BALL_SIZE[ball.num])

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
            player.weapon.rect = player.weapon.rect.move(0, DISPLAY_HEIGHT)

    (x, y, z, g) = player.weapon.rect
    return (x, y)


def hit(xW, yW, ball_list,playes):
    xW1 = xW
    yW1 = yW
    xW2 = xW + WEAPON_WIDTH

    for p in ball_list:
        print(p)

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

    print('broj je',ball.num,'a index',ball.index)

    if ball.num < 3:
        ball1 = make_ball(ball.num + 1, ball.x, ball.y, 1)
        ball_list.append(ball1)
        ball2 = make_ball(ball.num + 1, ball.x, ball.y, -1)
        ball_list.append(ball2)

   # else:
        #pygame.quit()

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
        hit(xW, yW, ball_List, player)

        NoCrash = crash(x, y, x1, y1)
        if not NoCrash and player.life >1:
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