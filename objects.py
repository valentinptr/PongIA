import pygame
from pygame import gfxdraw


class Ball:
    def __init__(self, x, y):
        self.radius = 10
        self.color = 'red'
        self.position = pygame.math.Vector2(x, y)
        self.speed = pygame.math.Vector2()
        self.acceleration = pygame.math.Vector2()

    def drawBall(self, screen):
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
        self.color = 'red'
        self.x = x
        self.y = y

    def drawPallets(self, screen):  # TODO :  ajouter les pallets
        c = 0

    def update(self, dt):
        self.speed += self.acceleration * dt
        self.position += self.speed * dt