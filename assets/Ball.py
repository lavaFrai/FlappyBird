import pygame
from pygame.math import Vector2

from utils.GameObject import GameObject


class Ball(GameObject):
    def __init__(self):
        super().__init__()

        self.physics = True
        self.rigid_body.width = 100
        self.rigid_body.height = 100
        self.rigid_body.frame_size = [800, 600]
        self.rigid_body.speed = Vector2(2, -2)
        self.rigid_body.position = Vector2(100, 100)
        self.rigid_body.set_gravity(Vector2(0, 0.3))

        self.image = pygame.image.load("media\\basketball.png")

    def draw(self, screen):
        coord = self.rigid_body.coord
        screen.blit(self.image, self.image.get_rect(center=coord))

        self.rigid_body.drawCollider(screen)

    def tick(self):
        super().tick()

        from __main__ import game
        if self.rigid_body.isColliding(game.platform.rigid_body):
            self.rigid_body.speed.y = -abs(self.rigid_body.speed.y)
