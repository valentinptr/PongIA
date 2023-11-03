import pygame
from pygame import gfxdraw

LENGTH_PALLETS = 100


class Ball:
    def __init__(self, x, y):
        self.radius = 30
        self.color = (255, 255, 255)
        self.x = x
        self.y = y

    def draw(self, screen):
        gfxdraw.aacircle(screen,
                         int(self.x),
                         int(self.y),
                         int(self.radius),
                         self.color)

        gfxdraw.filled_circle(screen,
                              int(self.x),
                              int(self.y),
                              int(self.radius),
                              self.color)


class Pallets:
    def __init__(self, x, y):
        self.color = (255, 255, 255)
        self.x = x
        self.y = y

    def draw(self, screen):
        pygame.draw.aaline(screen, self.color, (self.x, self.y),
                           (self.x + LENGTH_PALLETS, self.y))
