import pygame
import sys

class InputHandler:
    def __init__(self):
        self.mouse_pos = (0, 0)
        self.mouse_clicked = False

    def event_Polling(self, direction, running, show_grid, show_pos, paused, affiche_score,arret):
        for event in pygame.event.get(): 
            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_z or event.key == pygame.K_UP:
                    direction = 'UP'
                if event.key == pygame.K_s or event.key == pygame.K_DOWN:
                    direction = 'DOWN'
                if event.key == pygame.K_q or event.key == pygame.K_LEFT:
                    direction = 'LEFT'
                if event.key == pygame.K_d or event.key == pygame.K_RIGHT:
                    direction = 'RIGHT'
                

                if event.key == pygame.K_ESCAPE:
                    running = False
                if event.key == pygame.K_g:
                    show_grid = not show_grid
                if event.key == pygame.K_p:
                    paused = not paused
                if event.key == pygame.K_e:
                    arret = True
                if event.key == pygame.K_a:
                    affiche_score = True

            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                print("mouse_pos:", pos)

        return direction, running, show_grid, show_pos, paused,affiche_score,arret
