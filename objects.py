import pygame
from pygame import gfxdraw


class Ball:
    def __init__(self):
        self.radius = 10
        self.color = 'red'
        self.position = pygame.math.Vector2(x, y)
        self.speed = pygame.math.Vector2()
        self.acceleration = pygame.math.Vector2()

    def draw(self, screen):
        gfxdraw.aacircle(screen,
                         int(self.position.x),
                         int(self.position.y),
                         int(self.radius),
                         self.color)

        gfxdraw.filled_circle(screen,
                              int(self.position.x),
                              int(self.position.y),
                              int(self.radius),
                              self.color)

    def update(self, dt):
        self.speed += self.acceleration * dt
        self.position += self.speed * dt
