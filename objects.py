import pygame
from pygame import gfxdraw


class Ball:
    def __init__(self, x, y):
        self.radius = 30
        self.color = (255, 255, 255)
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


class Pallets:
    def __init__(self, x, y):
        self.color = (255, 255, 255)
        self.x = x
        self.y = y
        self.position = pygame.math.Vector2(x, y)
        self.speed = pygame.math.Vector2()
        self.acceleration = pygame.math.Vector2()

    def draw(self, screen):  # TODO :  ajouter les pallets
        c = 0
        pygame.draw.aaline(screen, self.color, (self.position.x, self.position.y), (self.position.x + 100, self.position.y))

    def update(self, dt):
        self.speed += self.acceleration * dt
        self.position += self.speed * dt