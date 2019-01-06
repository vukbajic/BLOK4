from globalFunc import *
from message_print import *

def pause():
    checkPause = False
    while(checkPause is not True):
        gameDisplay.fill(WHITE)
        massage_to_screen("PAUSE, PRESS 'O' TO CONTUNUE OR 'H' TO GO ON HOME SCREEN", RED)
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    quit()
                if event.key == pygame.K_o:
                   checkPause = True
                if event.key == pygame.K_h:
                    global index
                    index = 0
                    start_screen()
            if event.type == pygame.QUIT:
                sys.exit(0)


