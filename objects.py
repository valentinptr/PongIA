import pygame
from pygame import gfxdraw

LENGTH_PALLETS = 150
RADIUS = 30


class Ball:
    """
    This is the class Ball used to create a ball
    """
    def __init__(self, x, y):
        """
        This is the initialization function of the class Ball
        :param x: initialization of the X axis of the ball
        :param y: initialization of the Y axis of the ball
        """
        self.radius = RADIUS
        self.color = (255, 255, 255)  # white color
        self.x = x
        self.y = y

    def draw(self, screen):
        """
        This function is used to draw the ball
        :param screen: window that have been initialized in main.py
        :return: does not return anything
        """
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
    """
    This is the class Ball used to create a pallet
    """
    def __init__(self, x, y):
        """
        This is the initialization function of the class Pallets
        :param x: initialization of the X axis of the pallet
        :param y: initialization of the Y axis of the pallet
        """
        self.color = (255, 255, 255)  # white color
        self.x = x
        self.y = y

    def draw(self, screen):
        """
        This function is used to draw the pallets
        :param screen: window that have been initialized in main.py
        :return: does not return anything
        """
        pygame.draw.aaline(screen, self.color, (self.x, self.y),
                           (self.x + LENGTH_PALLETS, self.y))
