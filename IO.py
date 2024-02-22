import pygame

class InputHandler:
    def __init__(self, keys):
        self.keys = keys
        self.mouse_pos = (0, 0)
        self.mouse_clicked = False

    def event_Polling(self, keys, running, show_grid, show_pos):
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

        return keys, running, show_grid, show_pos
