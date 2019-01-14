from globalFunc import *
from globals import *


def text_objects(text, color, size):
        smallfont = pygame.font.SysFont("comicsansms", 25)      #definisane velicine teksta koji se ispisuje kao i font
        mediumfont = pygame.font.SysFont("comicsansms", 50)
        largefont = pygame.font.SysFont("comicsansms", 80)

        if size == "small":
            textSurface = smallfont.render(text, True, color)
        elif size == "large":
            textSurface = largefont.render(text, True, color)
        elif size == "medium":
            textSurface = mediumfont.render(text, True, color)
        return textSurface, textSurface.get_rect()

def massage_to_screen(msg, color, y_displace=0, size="small"):  # ispisuje  poruku na ekranu

        textSurf, textRect = text_objects(msg, color, size)
        textRect.center = (DISPLAY_WIDTH / 2), (DISPLAY_HEIGHT / 2) + y_displace
        gameDisplay.blit(textSurf, textRect)


def massage_to_screen_down(msg, color, y_displace=0, size="small"):

    textSurf, textRect = text_objects(msg, color, size)
    textRect.center = (DISPLAY_WIDTH / 2), (DISPLAY_HEIGHT / 4) + y_displace
    gameDisplay.blit(textSurf, textRect)