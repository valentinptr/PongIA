import pygame
from game import *
from objects import *

FPS = 60
fpsClock = pygame.time.Clock()

WINDOW_WIDTH = 600
WINDOW_HEIGHT = 800

pygame.init()
screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
clock = pygame.time.Clock()
running = True
dt = 0

engine = Engine()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    dt = clock.tick(FPS) / 1000

pygame.quit()
