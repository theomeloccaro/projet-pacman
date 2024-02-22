import pygame
import random

class Alien:
    def __init__(self,screen,tilesize,color,x,y,largeur):
        self.screen=screen
        self.tilesize=tilesize
        self.color= color
        self.x=x
        self.y=y
        self.largeur=largeur

    def pos_alien(self):
        pygame.draw.circle(self.screen,self.color,((self.x+0.5)*self.tilesize,(self.y+0.5)*self.tilesize),self.tilesize/2,self.largeur)

    def mouv_alien(self,laby):
        directions_possibles = [(0, -1), (0, 1), (-1, 0), (1, 0)]
        directions_valides = []

        #test position valide
        for direction in directions_possibles:
            new_x, new_y = self.x + direction[0], self.y + direction[1]

            if not laby.hit_box(new_x, new_y):
                directions_valides.append(direction)

        # Choisir aléatoirement une direction valide pour se déplacer
        if directions_valides:
            direction = random.choice(directions_valides)
            self.x += direction[0]
            self.y += direction[1]
