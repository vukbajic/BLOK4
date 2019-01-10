from globalFunc import *
from globals import *


#def massage_to_screen(msg,color):
 #   font = pygame.font.SysFont(None, FONT_SIZE)
  #  screen_text = font.render(msg, True, color)
 #   gameDisplay.blit(screen_text, [DISPLAY_WIDTH/8, DISPLAY_HEIGHT/4])


#def massage_to_screen_down(msg,color):
 #   font = pygame.font.SysFont(None, FONT_SIZE)
  #  screen_text = font.render(msg, True, color)
  #  gameDisplay.blit(screen_text, [DISPLAY_WIDTH/8, DISPLAY_HEIGHT/2])

def text_objects(text, color, size):  # menjao
        smallfont = pygame.font.SysFont("comicsansms", 25)
        mediumfont = pygame.font.SysFont("comicsansms", 50)
        largefont = pygame.font.SysFont("comicsansms", 80)

        if size == "small":  # menjao
            # font = pygame.font.SysFont(None, FONT_SIZE)
            textSurface = smallfont.render(text, True, color)
        elif size == "large":  # menjao
            # font = pygame.font.SysFont(None, FONT_SIZE)
            textSurface = largefont.render(text, True, color)
        elif size == "medium":  # menjao
            # font = pygame.font.SysFont(None, FONT_SIZE)
            textSurface = mediumfont.render(text, True, color)
        return textSurface, textSurface.get_rect()

def massage_to_screen(msg, color, y_displace=0, size="small"):  # menjao

        textSurf, textRect = text_objects(msg, color, size)
        textRect.center = (DISPLAY_WIDTH / 2), (DISPLAY_HEIGHT / 2) + y_displace
        gameDisplay.blit(textSurf, textRect)


def massage_to_screen_down(msg, color, y_displace=0, size="small"):  # menjao

    textSurf, textRect = text_objects(msg, color, size)
    textRect.center = (DISPLAY_WIDTH / 2), (DISPLAY_HEIGHT / 4) + y_displace
    gameDisplay.blit(textSurf, textRect)