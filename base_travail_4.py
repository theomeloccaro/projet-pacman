# Example file showing a circle moving on screen
import pygame
import random
# pygame setup
pygame.init()

#constantes
tilesize = 32 # taille d'une tuile IG
size = (20, 10) # taille du monde
fps = 30 # fps du jeu
player_speed = 150 # vitesse du joueur
next_move = 0 #tic avant déplacement

# color
ground_color = "#EDDACF"
grid_color = "#7F513D"
player_color = "#9F715D"


screen = pygame.display.set_mode((size[0]*tilesize, size[1]*tilesize))
clock = pygame.time.Clock()
running = True
dt = 0
show_grid = True
show_pos = False

keys= { "UP":0 , "DOWN":0, "LEFT":0, "RIGHT":0 }

player_pos = pygame.Vector2(round(size[0]/8), round(size[1]/2))

#tour de boucle, pour chaque FPS
while running:
    screen.fill(ground_color)

    # lecture clavier / souris
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_z or event.key == pygame.K_UP:
                keys['UP'] = 1
            if event.key == pygame.K_s or event.key == pygame.K_DOWN:
                keys['DOWN'] = 1
            if event.key == pygame.K_q or event.key == pygame.K_LEFT:
                keys['LEFT'] = 1
            if event.key == pygame.K_d or event.key == pygame.K_RIGHT:
                keys['RIGHT'] = 1

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_z or event.key == pygame.K_UP:
                keys['UP'] = 0
            if event.key == pygame.K_s or event.key == pygame.K_DOWN:
                keys['DOWN'] = 0
            if event.key == pygame.K_q or event.key == pygame.K_LEFT:
                keys['LEFT'] = 0
            if event.key == pygame.K_d or event.key == pygame.K_RIGHT:
                keys['RIGHT'] = 0

            if event.key == pygame.K_ESCAPE:
                running = False
            if event.key == pygame.K_g:
                show_grid = not show_grid
            if event.key == pygame.K_p:
                show_pos = not show_pos
        
        if event.type == pygame.MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()
            print("mouse_pos:", pos)
    


    next_move += dt
    # gestion des déplacements
    if next_move>0:
        if keys['UP'] == 1:
            player_pos.y -= 1
            next_move = -player_speed
        elif keys['DOWN'] == 1:
            player_pos.y += 1
            next_move = -player_speed
        elif keys['LEFT'] == 1:
            player_pos.x -= 1
            next_move = -player_speed
        elif keys['RIGHT'] == 1:
            player_pos.x += 1
            next_move = -player_speed

        # vérification du déplacement du joueur
        if player_pos.y < 0:
            player_pos.y = 0
        if player_pos.y >= size[1]:
            player_pos.y = size[1]-1
        if player_pos.x < 0:
            player_pos.x = 0
        if player_pos.x > size[0]-1:
            player_pos.x = size[0]-1

        if show_pos:
            print("pos: ",player_pos)


    # affichage des différents composants
    if show_grid:
        for i in range(1,size[0]):
            pygame.draw.line(screen,grid_color, (tilesize*i, 0), (tilesize*i, tilesize*size[0]) )
        for i in range(0,size[1]):
            pygame.draw.line(screen,grid_color, (0, tilesize*i), (tilesize*size[0], tilesize*i) )

    #affichage du joueur
    pygame.draw.rect(screen, player_color, pygame.Rect(player_pos.x*tilesize, player_pos.y*tilesize, tilesize, tilesize))

    pygame.display.flip()
    dt = clock.tick(fps)

pygame.quit()