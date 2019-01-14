import pygame
from level import *
from math import sin


#sve ono sto nam treba a da bude globalno
MAIN_SERVER_ADDR = '192.168.100.214'
MY_PORT = 502
MY_ADDR = '192.168.100.214'
DISPLAY_WIDTH = 800
DISPLAY_HEIGHT = 550
BLACK = (0,0,0)
WHITE = (255,255,255)
RED = (255, 0, 0)
GREEN = (0,255,0)
YELLOW = (255,255,0)
BALL_SIZE = (5, 10, 15, 30)
BALL_SPEED = (3, 3.5, 4, 4.5)
BALL_COLORS = (RED,GREEN,YELLOW,BLACK)
PLAYER_SPEED = 5
PLAYER_HIGHT = 37
PLAYER_WIDTH = 23
WEAPON_SPEED = 20
WEAPON_HEIGHT = 120
WEAPON_WIDTH = 8
LIFE = 3
NUMBERLIFES_FONT_SIZE = 50
FONT_SIZE = 30
TIME_PER_LEVEL = 50
dock = pygame.image.load("images/backgrounds/dock_background.jpg")

level = level()
timer = TIME_PER_LEVEL
multiplay = False
level_ball_size = 3
level_ball_count = 1
players = []
allowPower = True
start_time = 0
currentPower = None
global online
online = False

global tournament
tournament= False
bg_one_color = pygame.image.load("images/backgrounds/one_color_background.jpg")


gameDisplay = pygame.display.set_mode((DISPLAY_WIDTH, DISPLAY_HEIGHT))
pygame.display.set_caption('Bubble trouble')
gameDisplay.fill(WHITE)
a = pygame.image.load('images/icon.jpg')
pygame.display.set_icon(a)


clock = pygame.time.Clock()
screen_check = True

