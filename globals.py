import pygame
from math import sin


#sve ono sto nam treba a da bude globalno
DISPLAY_WIDTH = 800
DISPLAY_HEIGHT = 550
BLACK = (0,0,0)
WHITE = (255,255,255)
RED = (255, 0, 0)
GREEN = (0,255,0)
YELLOW = (255,255,0)
BALL_SIZE = (30, 15, 10, 5)
BALL_COLORS = (RED,GREEN,YELLOW,BLACK)
PLAYER_SPEED = 7
PLAYER_HIGHT = 37
PLAYER_WIDTH = 23
WEAPON_SPEED = 20
WEAPON_HEIGHT = 120
WEAPON_WIDTH = 8
LIFE = 3
NUMBERLIFES_FONT_SIZE = 50
FONT_SIZE = 30
TIME_PER_LEVEL = 50
bg1 = pygame.image.load("images/backgrounds/dock_background.jpg")
bg = pygame.image.load("images/backgrounds/background2.jpg")
bg_one_color = pygame.image.load("images/backgrounds/one_color_background.jpg")


gameDisplay = pygame.display.set_mode((DISPLAY_WIDTH, DISPLAY_HEIGHT))
pygame.display.set_caption('Bubble trouble')
gameDisplay.fill(WHITE)
a = pygame.image.load('images/icon.jpg')
pygame.display.set_icon(a)


clock = pygame.time.Clock()
screen_check = True

