from globalFunc import *
from globals import *


def massage_to_screen(msg,color):
    font = pygame.font.SysFont(None, FONT_SIZE)
    screen_text = font.render(msg, True, color)
    gameDisplay.blit(screen_text, [DISPLAY_WIDTH/8, DISPLAY_HEIGHT/4])