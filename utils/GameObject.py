from pygame.math import Vector2

from utils.RigidBody import RigidBody


class GameObject:
    def __init__(self):
        self.visible = True
        self.physics = False
        self.rigid_body: RigidBody = RigidBody([0, 0], 0, 0)

    def draw(self, screen):
        raise NotImplementedError("draw() not implemented")

    def event(self, event):
        pass

    def tick(self):
        if self.physics:
            self.rigid_body.tick()
