from globalFunc import *


pygame.init()

ball_List = ballToList()

NoCrash = True
while NoCrash:
    gameDisplay.fill(WHITE)
    #printovi su samo zbog lakseg dibaga
    draw_player(player)
    print(player.rect)
    (x,y,c,d) = player.rect
    movePlayer()
    (x1,y1) = moveBall(ball_List)
    print(x,y,x1,y1)
    print(NoCrash)
    NoCrash = crash(x,y,x1,y1)
    print(NoCrash)
    pygame.display.update()
    clock.tick(100)

pygame.quit()
quit()