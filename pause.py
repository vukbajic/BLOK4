from globalFunc import *
from message_print import *
from globals import *
from messageBox import *

def pause():
    checkPause = False
    bg = pygame.image.load("images/backgrounds/one_color_background.jpg")
    while(checkPause is not True):
        gameDisplay.blit(bg, (0, 0))
        massage_to_screen("PAUSE, PRESS 'O' TO CONTUNUE OR 'H' TO GO ON HOME SCREEN", RED)
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    result = MessageBox("Exit", "Do you want to exit")
                    if result is True:
                        pygame.quit()
                        sys.exit(0)
                if event.key == pygame.K_o:
                   checkPause = True
                if event.key == pygame.K_h:
                    global index
                    index = 0
                    start_screen()
            if event.type == pygame.QUIT:
                result = MessageBox("Exit", "Do you want to exit")
                if result is True:
                    pygame.quit()
                    sys.exit(0)


