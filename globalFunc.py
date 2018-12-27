from player import *
from ball import *
import random


# napravimo novog igraca
player = Player()

#funkcija koja ga pokrece
def movePlayer():

    for event in pygame.event.get():
        print(event)
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                player.rect = player.rect.move(-PLAYER_SPEED, 0)
                #rect su koordinate slike. sastoji se od (x,y,visine,sirine)
                #move je ugradjena funkcija po kojoj se kreces po x i y osi
            elif event.key == pygame.K_RIGHT:
                player.rect = player.rect.move(PLAYER_SPEED, 0)

            elif event.key == pygame.K_ESCAPE:
                pygame.quit()

        if event.type == pygame.QUIT:
            pygame.quit()





def draw_player(player):
    gameDisplay.blit(player.image, player.rect) #ovo je da nacrtamo lika

def make_ball(num,corx,cory,direction):         #ovo je vasa funkcija koju sam podelio na tri funkcije
    """                                         #ovo je funkcija koja pravi lopte
    Function to make a new, random ball.
    """
    ball = Ball(num)
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
    ball_list.append(ball)
    return ball_list

def moveBall(ball_list):                        #samo ime kaze, lopte se krecu

    for ball in ball_list:
        # Move the ball's center
        ball.x += ball.change_x
        ball.y += ball.change_y

        print(ball.x)
        print(ball.y)
        # Bounce the ball if needed
        if ball.y > DISPLAY_HEIGHT - BALL_SIZE[ball.num] or ball.y < 75 * (ball.num + 1):
            ball.change_y *= -1
        if ball.x > DISPLAY_WIDTH - BALL_SIZE[ball.num] or ball.x < BALL_SIZE[ball.num]:
            ball.change_x *= -1


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
    print(xP1, yP1, xP2, xB1, yB1, xB2 )

    if yP1 <= yB1 and xP2 >= xB1:               #tu proveravam da li se ukrstaju koordinate lika i lopte
        if xP1 <= xB2:
            return False                        #ako se ukrstaju onda vraca false
    if yP1 <= yB1 and xP1 <= xB2:
        if xP2 >= xB1:
            return False

    return True                                 #ako se ne ukrstaju onda True


