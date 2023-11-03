from game import *
from objects import *

FPS = 60
fpsClock = pygame.time.Clock()

WINDOW_WIDTH = 600
WINDOW_HEIGHT = 800

pygame.init()
screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Pong IA")
clock = pygame.time.Clock()
running = True
dt = 0

cursor_x = WINDOW_WIDTH / 2 - 50

engine = Engine()
ball = Ball(WINDOW_WIDTH / 2, WINDOW_HEIGHT / 2) #WINDOW_WIDTH / 2
pallet_j1 = Pallets(cursor_x, 40)
pallet_j2 = Pallets(cursor_x, WINDOW_HEIGHT - 40)
engine.dropPallets(pallet_j1.x, pallet_j1.y)
engine.dropPallets(pallet_j2.x, pallet_j2.y)

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                engine.dropBall(ball.x, ball.y) # TODO : a terme, revoir la gestion d'appartition des balles

    engine.update(dt)
    engine.drawBackground(screen)
    engine.drawBall(screen)
    engine.drawPallets(screen)

    pygame.display.flip()
    dt = clock.tick(FPS) / 1000

pygame.quit()
