import pygame
class Box:
    def __init__(self,idx,x,y,width,bgColor,lineColor=(255,255,0)):
        """
        if the id is 1 it is a queen
        """
        self.id = idx

        self.rect = pygame.Rect(x,y,width,width)
        self.lineColor = lineColor
        #self.bgColor = self.assignBgColor()
        self.bgColor = bgColor

    def draw(self,screen,img):
        pygame.draw.rect(screen,self.bgColor,self.rect)
        #pygame.draw.rect(screen,self.lineColor,self.rect,1)
        if self.id == 1:
            pygame.draw.rect(screen,(20,200,200),self.rect,4)
            screen.blit(img, self.rect)

