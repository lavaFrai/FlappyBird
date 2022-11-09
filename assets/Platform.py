import pygame
from pygame.math import Vector2

from utils.GameObject import GameObject


class Platform(GameObject):
    def __init__(self):
        super().__init__()

        self.speed = 5

        self.physics = True
        self.rigid_body.width = 100
        self.rigid_body.height = 18
        self.rigid_body.frame_size = [800, 600]
        self.rigid_body.speed = Vector2(0, 0)
        self.rigid_body.position = Vector2(100, self.rigid_body.frame_size[1] - 40)
        self.image = pygame.image.load("media\\platform.bmp")

    def draw(self, screen):
        coord = self.rigid_body.coord
        screen.blit(self.image, self.image.get_rect(center=coord))

        self.rigid_body.drawCollider(screen)

    def event(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                self.rigid_body.speed.x = -self.speed
            if event.key == pygame.K_RIGHT:
                self.rigid_body.speed.x = self.speed
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                self.rigid_body.speed.x = 0
            if event.key == pygame.K_RIGHT:
                self.rigid_body.speed.x = 0
