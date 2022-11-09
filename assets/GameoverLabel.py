import pygame

from utils.GameObject import GameObject


class GameoverLabel(GameObject):
    def draw(self, screen):
        label = "Game Over!"
        font = pygame.font.get_fonts()
        font = pygame.font.SysFont(font[0], 72)
        score_t = font.render(label, True, pygame.Color("RED"))
        screen.blit(score_t, (230, 230))

        label = "[ Space to restart ]"
        font = pygame.font.get_fonts()
        font = pygame.font.SysFont(font[0], 24)
        score_t = font.render(label, True, pygame.Color("RED"))
        screen.blit(score_t, (320, 300))

    def event(self, event):
        if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            from __main__ import game
            game.__init__()
            game.run()
