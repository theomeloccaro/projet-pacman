import pygame

class Item:
    def __init__(self,screen,tilesize,color,x,y):
        self.screen = screen
        self.tilesize = tilesize
        self.color = color
        self.x = x
        self.y = y


    def pos_item(self):
        pygame.draw.circle(self.screen,self.color,[self.tilesize*(self.x+1-0.5),self.tilesize*(self.y+1-0.5)],self.tilesize/2,2)