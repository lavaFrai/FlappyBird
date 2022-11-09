import random

import pygame
from pygame.math import Vector2

from utils.GameObject import GameObject
from utils.RigidBody import RigidBody


class Score(GameObject):
    def draw(self, screen):
        from __main__ import game

        score = "Score: " + str(game.score)
        font = pygame.font.get_fonts()
        font = pygame.font.SysFont(font[0], 36)
        score_t = font.render(score, True, pygame.Color("RED"))
        screen.blit(score_t, (2, 2))
