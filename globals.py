import pygame
from math import sin
#sve ono sto nam treba a da bude globalno
DISPLAY_WIDTH = 800
DISPLAY_HEIGHT = 600
BLACK = (0,0,0)
WHITE = (255,255,255)
RED = (255, 0, 0)
BALL_SIZE = (50, 30, 15, 5)
PLAYER_SPEED = 5
PLAYER_HIGHT = 73
PLAYER_WIDTH = 58
FONT_SIZE = 30
NUMBERLIFES_FONT_SIZE = 50
LIFE = 3

gameDisplay = pygame.display.set_mode((DISPLAY_WIDTH, DISPLAY_HEIGHT))
pygame.display.set_caption('Bubble trouble')
gameDisplay.fill(WHITE)

clock = pygame.time.Clock()
