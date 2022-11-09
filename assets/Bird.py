import pygame
from pygame.math import Vector2

from utils.GameObject import GameObject


class Bird(GameObject):
    def __init__(self):
        super().__init__()

        self.spedUpByKeydown = 8
        self.physics = True
        self.rigid_body.width = 50
        self.rigid_body.height = 40
        self.rigid_body.frame_size = [800, 600]
        self.rigid_body.speed = Vector2(0, -10)
        self.rigid_body.position = Vector2(100, self.rigid_body.frame_size[1] // 2)
        self.rigid_body.set_gravity(Vector2(0, 0.3))
        self.image = pygame.image.load("media\\bird.png ")
        self.image = pygame.transform.scale(self.image, (self.rigid_body.width, self.rigid_body.height))

    def draw(self, screen):
        coord = self.rigid_body.coord
        screen.blit(self.image, self.image.get_rect(center=coord))

        self.rigid_body.drawCollider(screen)

    def tick(self):
        from __main__ import game
        if self.rigid_body.position.y > self.rigid_body.frame_size[1] - self.rigid_body.height + 12:
            self.rigid_body.speed = Vector2(0, -1)
        if self.rigid_body.position.y < 0 + self.rigid_body.height:
            self.rigid_body.speed = Vector2(0, 1)

        for column in game.columns:
            if self.rigid_body.isColliding(column.rigid_body) or self.rigid_body.isColliding(column.top_rigid_body):
                game.game_over()
        super().tick()

    def event(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                self.rigid_body.speed.y -= self.spedUpByKeydown
