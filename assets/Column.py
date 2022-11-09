import random

import pygame
from pygame.math import Vector2

from utils.GameObject import GameObject
from utils.RigidBody import RigidBody


class Column(GameObject):
    def __init__(self, offset):
        super().__init__()

        self.vertOffset = random.randint(200, 300)
        self.spedUpByKeydown = 8
        self.physics = True

        self.rigid_body.width = 60
        self.rigid_body.height = 300
        self.rigid_body.frame_size = [800, 600]

        self.top_rigid_body = RigidBody(self.rigid_body.frame_size, self.rigid_body.width, self.rigid_body.height)
        self.top_rigid_body.position = Vector2(offset, (self.rigid_body.frame_size[1] // 2) + self.vertOffset - 500)

        self.rigid_body.speed = Vector2(0, 0)
        self.rigid_body.position = Vector2(offset, (self.rigid_body.frame_size[1] // 2) + self.vertOffset)
        self.image = pygame.image.load("media\\column.png")
        self.top_image = pygame.image.load("media\\top_column.png")
        self.image = pygame.transform.scale(self.image, (self.rigid_body.width, self.rigid_body.height))
        self.top_image = pygame.transform.scale(self.top_image, (self.rigid_body.width, self.rigid_body.height))

    def draw(self, screen):
        coord = self.rigid_body.coord
        top_coord = self.top_rigid_body.coord
        screen.blit(self.image, self.image.get_rect(center=coord))
        screen.blit(self.top_image, self.image.get_rect(center=top_coord))

        self.rigid_body.drawCollider(screen)
        self.top_rigid_body.drawCollider(screen)

    def tick(self):
        self.rigid_body.position.x -= 2
        self.top_rigid_body.position.x -= 2
        if self.rigid_body.position.x < -100:
            self.rigid_body.position.x = self.rigid_body.frame_size[0] + 100
            self.top_rigid_body.position.x = self.top_rigid_body.frame_size[0] + 100

            from __main__ import game
            game.score += 1
