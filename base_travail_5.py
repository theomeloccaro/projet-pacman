# Example file showing a circle moving on screen
import pygame 
import random
from labyrinthe import Labyrinthe
from grid import Grid
from utils import Pos
from IO import InputHandler
from item import Item
from alien import Alien
from chargeur import ConfigLoader
import configparser
import time
import sys

# pygame setup
pygame.init()
param={}
loader=ConfigLoader("conf.ini")

param["Version"]=loader.get_value("general","version",int)

param["Auteur"]=loader.get_value("general","author",str)

param["size_x"] = loader.get_value("general", "size_x", int)

param["size_y"] = loader.get_value("general", "size_y", int)

tilesize = loader.get_value("general", "tilesize", int)

level = loader.get_value("map", "level")

array_pos_alien = loader.get_value("aliens", "array_pos_alien",tuple,tuple_delimiter=":",value_delimiter=",")

array_pos_item = loader.get_value("items", "array_pos_item",tuple,tuple_delimiter=":",value_delimiter=",")

ground_color=loader.get_value("color","ground_color",str)
grid_color=loader.get_value("color","grid_color",str)
head_color=loader.get_value("color","head_color",str)
body_color=loader.get_value("color","body_color",str)
wall_color=loader.get_value("color","wall_color",str)
cross_color=loader.get_value("color","cross_color",str)
item_color=loader.get_value("color","item_color",str)
alien_color=loader.get_value("color","alien_color",str)

items = []
aliens = []
running = True
dt = 0
show_grid = True
show_pos = False
paused = False
direction = "UP"
itemFound = False
DisplayMessage = False
score=0
affiche_score=False
arret = False

#constantes
#tilesize = tile # taille d'une tuile IG
size = (param["size_x"], param["size_y"]) # taille du monde
fps = 30 # fps du jeu
player_speed = 150 # vitesse du joueur
next_move = 0 #tic avant déplacement
filename='color.ini'

laby = Labyrinthe(size[0], size[1])
laby.load_from_file(level)
laby.set_color(wall_color)

grid = Grid(size[0], size[1],tilesize)
grid.set_color(grid_color)

screen = pygame.display.set_mode((size[0]*tilesize, size[1]*tilesize))


clock = pygame.time.Clock() 





player_pos=(5,9)
player_pos2=(4,9)
snake=[player_pos,player_pos2]
# Utilisation de la classe dans le programme principal
input_handler = InputHandler()

#création items
for i in range(len(array_pos_item)):
    if not laby.hit_box(array_pos_item[i][0],array_pos_item[i][1]):
        items.append(Item(screen,tilesize,item_color,array_pos_item[i][0],array_pos_item[i][1]))





#tour de boucle, pour chaque FPS
while running:    
    #
    #   Gestion des I/O  clavier / souris
    #
    direction, running,show_grid, show_pos,paused,affiche_score,arret = input_handler.event_Polling(direction, running, show_grid, show_pos, paused,affiche_score,arret)
    
    #
    # gestion des déplacements
    #
    if not paused:
        
        next_move += dt
        if next_move>0:
            new_x, new_y = player_pos[0], player_pos[1]
            if direction == 'UP':
                new_y -=1
            elif direction == 'DOWN':
                new_y += 1
            elif direction == 'LEFT':
                new_x -=1
            elif direction == 'RIGHT':
                new_x += 1
            

            # vérification du déplacement du joueur                                    
            if not laby.hit_box(new_x, new_y):
                player_pos = new_x, new_y
                next_move -= player_speed            

            for j in range (len(items)):
                if new_x == items[j].x and new_y == items[j].y:
                    snake.insert(0,player_pos)                        
                    del items[j]
                    items.append(Item(screen,tilesize,item_color,random.randint(0,param["size_x"]-1),random.randint(0,param["size_y"]-1)))
                    score+=1

            if affiche_score:
                print(score)
                affiche_score=False
                        
            if arret:
                print("Votre score est de "+str(score))
                sys.exit()
                        
            if score == 5:
                print("Félicitations, vous avez atteint un score de 5 !")
                sys.exit()

            # Vérification si le joueur est hors du cadre
            if new_x<0 : 
                player_pos=param["size_x"],new_y
            if new_x >param["size_x"]-1:
                player_pos=0,new_y
            if new_y<0 :
                player_pos=new_x,param["size_y"]-1
            if new_y >param["size_y"]-1:
                player_pos=new_x,0

            # Agrandissement snake       
            snake.insert(0,player_pos)

            if len(snake) > 2:
                snake.pop()

            if itemFound :
                
                itemFound=False

        
    #
    # affichage des différents composants graphique
    #
    screen.fill(ground_color)

    laby.draw(screen, tilesize)

    if show_grid:
        grid.draw(screen)       
    

    for index, tile in enumerate(snake):
        if index == 0:
            pygame.draw.rect(screen,head_color, (tile[0] * tilesize, tile[1] * tilesize, tilesize, tilesize))
        else:
            pygame.draw.rect(screen,body_color, (tile[0] * tilesize, tile[1] * tilesize, tilesize, tilesize))
    
    if show_pos:
        print("pos: ",player_pos)
    
    
    

    
    # test items
    for elt in items:
        elt.pos_item()
    
    #test aliens
    for ali in aliens:
         ali.pos_alien()      
    
    
    # affichage des modification du screen_view
    pygame.display.flip()
    # gestion fps
    dt = clock.tick(fps)

    # Vérifier si le joueur est arrivé à la sortie
pygame.quit()