import pygame
from pygame.math import Vector2
import pymunk


class RigidBody:
    def __init__(self, frame_size, width, height):
        self.gravity = Vector2(0, 0)
        self.frame_size = frame_size
        self.width = width
        self.height = height
        self.position = Vector2(0, 0)
        self.speed = Vector2(0, 0)

    def set_gravity(self, x):
        self.gravity = x
        return self

    def set_speed(self, x, y):
        self.speed.x = x
        self.speed.y = y

    def set_position(self, x, y):
        self.position.x = x
        self.position.y = y

    def check_collisions(self):
        if self.position.x - self.width / 2 < 0:
            self.speed.x = -self.speed.x
            self.position.x = 0 + self.width / 2
        if self.position.x + self.width / 2 > self.frame_size[0]:
            self.speed.x = -self.speed.x
            self.position.x = self.frame_size[0] - self.width / 2
        if self.position.y - self.height / 2 < 0:
            self.speed.y = -self.speed.y
            self.position.y = 0 + self.height / 2
        if self.position.y + self.height / 2 > self.frame_size[1]:
            self.speed.y = -self.speed.y
            self.position.y = self.frame_size[1] - self.width / 2

    def tick(self):
        self.position += self.speed
        self.check_collisions()
        self.speed += self.gravity
        self.speed *= 0.9999

    def isColliding(self, other):
        ax1, ay1, ax2, ay2 = self.position.x - self.width / 2, self.position.y - self.height / 2, self.position.x + self.width / 2, self.position.y + self.height / 2
        bx1, by1, bx2, by2 = other.position.x - other.width / 2, other.position.y - other.height / 2, other.position.x + other.width / 2, other.position.y + other.height / 2
        # print(bx1, by1, bx2, by2)

        return ax1 < bx2 and ax2 > bx1 and ay1 < by2 and ay2 > by1

    def drawCollider(self, screen):
        from __main__ import game
        if not game.hitbox_rendering: return
        ax1, ay1, ax2, ay2 = self.position.x - self.width / 2, \
                             self.position.y - self.height / 2, \
                             self.position.x + self.width / 2, \
                             self.position.y + self.height / 2

        pygame.draw.rect(screen, (0, 255, 0), (ax1, ay1, ax2 - ax1, ay2 - ay1), 1)
        pygame.draw.circle(screen, (255, 0, 0), (ax1, ay1), 5)
        pygame.draw.circle(screen, (0, 0, 255), (ax2, ay2), 5)

    @property
    def coord(self):
        return [self.position.x, self.position.y]

    @property
    def rectangle(self):
        return [0, 0, 0, 0]
