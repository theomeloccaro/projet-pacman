import pygame

class Grid:
    def __init__(self, x,y, tilesize):
        self.x = x
        self.y = y
        self.tilesize = tilesize

    def set_color(self, v):
        self.color = v

    def draw(self, screen):
        for i in range(1,self.x):
            pygame.draw.line(screen,self.color, (self.tilesize*i, 0), (self.tilesize*i, self.tilesize*self.y) )
        for i in range(0,self.y):
            pygame.draw.line(screen, self.color, (0, self.tilesize*i), (self.tilesize*self.x, self.tilesize*i) )
        

    def arriver(self,x,y):
        return x==19 and y==8