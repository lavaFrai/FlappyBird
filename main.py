import pygame
import pymunk
from pygame.math import Vector2


class Game:
    class Consts:
        gForce = Vector2(0, 0.1)
        displayMode = [800, 600]

    class Color:
        white = (255, 255, 255)
        black = (0, 0, 0)
        blue = (0, 0, 255)
        green = (0, 255, 0)
        red = (255, 0, 0)

    def registrate_game_object(self, game_object):
        self.game_objects.append(game_object)

    def __init__(self):
        self.paused = False
        self.hitbox_rendering = False
        self.score = 0
        self.columns = None
        self.average_fps_list = [0 for _ in range(10)]
        self.screen = pygame.display.set_mode(self.Consts.displayMode)
        self.running = True
        self.clock = pygame.time.Clock()
        self.fps = 60
        self.game_objects = []
        self.space = pymunk.Space()
        self.space.gravity = (0, 981)
        self.create_boundaries()

    def average_fps(self, fps):
        self.average_fps_list.append(fps)
        self.average_fps_list.pop(0)
        return sum(self.average_fps_list) / len(self.average_fps_list)

    def create_boundaries(self):
        width = self.Consts.displayMode[0]
        height = self.Consts.displayMode[1]
        rects = [
            [(width / 4, height - 10), (width, 20)], [(width / 2, 10), (width, 20)], [(10, height / 2), (20, height)],
            [(width - 10, height / 2), (20, height)]

        ]

        for pos, size in rects:
            body = pymunk.Body(body_type=pymunk.Body.STATIC)
            body.position = pos
            shape = pymunk.Poly.create_box(body, size)
            shape.elasticity = 0.8
            shape.friction = 0.5
            self.space.add(body, shape)

    def render_fps(self):
        fps = str(int(self.average_fps(self.clock.get_fps()))) + " fps"
        font = pygame.font.get_fonts()
        font = pygame.font.SysFont(font[0], 12)
        fps_t = font.render(fps, True, pygame.Color("RED"))

        self.screen.blit(fps_t, (770, 2))

    def quit(self):
        self.running = False

    def handle_event(self, event):
        if event.type == pygame.QUIT:
            self.quit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_h:
                self.hitbox_rendering = not self.hitbox_rendering
        for i in self.game_objects:
            i.event(event)

    def clear(self):
        self.screen.fill((255, 255, 255))

    def draw(self):
        for i in self.game_objects:
            if i.visible:
                i.draw(self.screen)

        # self.draw_face(self.face.coord)

    def handle_physics(self):
        for i in self.game_objects:
            i.tick()

    def run(self):
        pygame.init()

        from assets.Background import Background
        self.registrate_game_object(Background())

        from assets.Bird import Bird
        bird = Bird()
        self.registrate_game_object(bird)

        from assets.Column import Column
        self.columns = [Column(i * 330 + 100) for i in range(1, 4)]
        for column in self.columns:
            self.registrate_game_object(column)

        from assets.Score import Score
        self.registrate_game_object(Score())

        while self.running:
            for event in pygame.event.get():
                self.handle_event(event)
            if not self.paused:
                self.handle_physics()
            self.draw()
            self.render_fps()
            self.clock.tick(self.fps)
            pygame.display.flip()
            self.clear()

    def game_over(self):
        self.paused = True
        from assets.GameoverLabel import GameoverLabel
        self.registrate_game_object(GameoverLabel())

    def __del__(self):
        pygame.quit()


if __name__ == "__main__":
    game = Game()
    game.run()
