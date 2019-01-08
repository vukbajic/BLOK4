from globals import *
#klasa lopte, to sam kopirao sa vaseg koda
class Ball:
    def __init__(self,number,index, image_name='images/players/player.png'):
        self.x = 0
        self.y = 0
        self.change_x = sin(30)
        self.change_y = 0
        self.num = number
        self.new = True
        self.index = index
        self.image = pygame.image.load(image_name)
        self.rect = self.image.get_rect()






