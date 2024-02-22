import pygame

class Item:
    def __init__(self,screen,tilesize,color,x,y):
        self.screen = screen
        self.tilesize = tilesize
        self.color = color
        self.x = x
        self.y = y


    def pos_item(self):
        pygame.draw.polygon(self.screen,self.color,[((self.x+0.5)*self.tilesize,(self.y)*self.tilesize),((self.x+1)*self.tilesize,(self.y+1)*self.tilesize),((self.x)*self.tilesize,(self.y+1)*self.tilesize)],2)
