import pygame
from pygame.math import Vector2

from utils.GameObject import GameObject
from main import Game


class Face(GameObject):
    def __init__(self):
        super().__init__()
        self.physics = True

        self.rigid_body.width = 200
        self.rigid_body.height = 200
        self.rigid_body.frame_size = [800, 600]
        self.rigid_body.speed = Vector2(1, -1)
        self.rigid_body.position = Vector2(100, 100)

    def draw(self, screen):
        coord = self.rigid_body.coord
        pygame.draw.circle(screen, Game.Color.green, coord, 70)
        pygame.draw.circle(screen, Game.Color.black, coord, 68)
        pygame.draw.rect(screen, Game.Color.black, [coord[0] - 90, coord[1] - 80, 180, 120])
        pygame.draw.circle(screen, Game.Color.green, coord, 100, 2)
        coord[1] -= 40
        coord[0] -= 40
        pygame.draw.circle(screen, Game.Color.green, coord, 20)
        pygame.draw.circle(screen, Game.Color.black, coord, 18)
        coord[0] += 80
        pygame.draw.circle(screen, Game.Color.green, coord, 20)
        pygame.draw.circle(screen, Game.Color.black, coord, 18)
        coord[0] -= 40
        pygame.draw.rect(screen, Game.Color.green, [coord[0] - 1, coord[1] + 10, 2, 50])

    def event(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                self.physics = not self.physics
