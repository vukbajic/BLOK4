import pygame
from math import sin
#sve ono sto nam treba a da bude globalno
DISPLAY_WIDTH = 800
DISPLAY_HEIGHT = 500
BLACK = (0,0,0)
WHITE = (255,255,255)
RED = (255, 0, 0)
BALL_SIZE = (30, 15, 10, 5)
PLAYER_SPEED = 10
PLAYER_HIGHT = 73
PLAYER_WIDTH = 58
WEAPON_SPEED = 20
WEAPON_HEIGHT = 120
WEAPON_WIDTH = 8
BALL_INDEX = -1
LIFE = 3
NUMBERLIFES_FONT_SIZE = 50
FONT_SIZE = 30

gameDisplay = pygame.display.set_mode((DISPLAY_WIDTH, DISPLAY_HEIGHT))
pygame.display.set_caption('Bubble trouble')
gameDisplay.fill(WHITE)

clock = pygame.time.Clock()
