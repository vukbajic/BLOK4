"""
 This example shows having multiple balls bouncing around the screen at the
 same time. You can hit the space bar to spawn more balls.

 Sample Python/Pygame Programs
 Simpson College Computer Science
 http://programarcadegames.com/
 http://simpson.edu/computer-science/
"""

import pygame
import random
from math import sin
import settings

# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)


BALL_SIZE = (50, 30, 15, 5)


class Ball:
    """
    Class to keep track of a ball's location and vector.
    """

    def __init__(self,number):
        self.x = 0
        self.y = 0
        self.change_x = sin(30)
        self.change_y = 0
        self.num = number
        self.new = True


def make_ball(num,corx,cory,direction):
    """
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


def main(screen):
    """
    This is our main program.
    """
  #  pygame.init()

    # Set the height and width of the screen
    #size = [SCREEN_WIDTH, SCREEN_HEIGHT]
    #screen = pygame.display.set_mode(size)

    #pygame.display.set_caption("Bouncing Balls")

    # Loop until the user clicks the close button.
    done = False

    # Used to manage how fast the screen updates
    clock = pygame.time.Clock()

    ball_list = []

    ball = make_ball(0,random.randrange(BALL_SIZE[0], settings.DISPLAYWIDTH - BALL_SIZE[0]),random.randrange(100, settings.DISPLAYHEIGHT - BALL_SIZE[0]), 1 )
    ball_list.append(ball)
    return ball_list

def whileLopta(ball_list, screen, clock):
   # for event in pygame.event.get():
   #     if event.type == pygame.QUIT:
     #       done = True
     #   elif event.type == pygame.KEYDOWN:
      #      # Space bar! Spawn a new ball.
      #      if event.key == pygame.K_SPACE:
      #          #  ball = make_ball()
                #  ball_list.append(ball)
       #         temp = ball_list[0]

      #          ball_list.remove(ball_list[0])

       #         if temp != 3:
       #             ball = make_ball(temp.num + 1, temp.x, temp.y, 1)
       #             ball_list.append(ball)
        #            ball = make_ball(temp.num + 1, temp.x, temp.y, -1)
        #            ball_list.append(ball)

    # --- Logic
    for ball in ball_list:
        # Move the ball's center
        ball.x += ball.change_x
        ball.y += ball.change_y

        if ball.new is not True and ball.num <= 3:
            # Bounce the ball if needed
            if ball.y > settings.DISPLAYHEIGHT - BALL_SIZE[ball.num] or ball.y < 75 * (ball.num + 1):
                ball.change_y *= -1
            if ball.x > settings.DISPLAYWIDTH - BALL_SIZE[ball.num] or ball.x < BALL_SIZE[ball.num]:
                ball.change_x *= -1

        # Kad loptica padne ispod svoje gornje granice onda moze da se proverava promena pravca
        if ball.y > 75 * (ball.num + 1):
            ball.new = False

    # --- Drawing
    # Set the screen background
    # screen.fill(WHITE)

    # Draw the balls
    for ball in ball_list:
        if ball.num <= 3:
            pygame.draw.circle(screen, BLACK, [ball.x, ball.y], BALL_SIZE[ball.num])

    # --- Wrap-up
    # Limit to 60 frames per second
    #clock.tick(60)

    # Go ahead and update the screen with what we've drawn.
    pygame.display.flip()
        # --- Event Processing


    # Close everything down
   # pygame.quit()

