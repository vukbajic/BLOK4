from globals import *
#klasa lopte, to sam kopirao sa vaseg koda
class Ball:
    def __init__(self,number,index, x, y, image_name='images/balls/ball.png'):
        self.x = 0
        self.y = 0
        self.change_x = sin(30)
        self.change_y = 0
        self.num = number
        self.new = True
        self.index = index
        self.image = pygame.image.load(image_name)
        self.image = pygame.transform.scale(self.image,(int(round(50/(self.num+1),0)),int (round(50/(self.num+1),0))))
        self.rect = self.image.get_rect()
        self.set_position(x, y)
        print(self.rect, x, y)


    def set_position(self,x, y):
        self.rect.topleft = (x,y)






