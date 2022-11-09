import random

import pygame
from pygame.math import Vector2

from utils.GameObject import GameObject
from utils.RigidBody import RigidBody


class Background(GameObject):
    def __init__(self):
        super().__init__()

        self.k = 0

        self.image = pygame.image.load("media\\background.png")
        self.image = pygame.transform.scale(self.image, (336, 600))

    def draw(self, screen):
        from __main__ import game

        for i in range(4):
            screen.blit(self.image, (i * 336 + self.k, 0))

    def tick(self):
        self.k -= 1
        if self.k < -336:
            self.k = 0

