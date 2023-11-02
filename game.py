from objects import *

BACKGROUND_COLOR = 'black'
BOX_COLOR = 'white'
WINDOW_WIDTH = 600
WINDOW_HEIGHT = 800
BOX_THICKNESS = 20
BOX_OFFSET_TOP = 0
BOX_OFFSET_HORIZ = 0
BOX_OFFSET_BOTTOM = 100
BOX_POSITION_LEFT = BOX_OFFSET_HORIZ
BOX_POSITION_RIGHT = WINDOW_WIDTH - BOX_THICKNESS
BOX_POSITION_BOTTOM = WINDOW_HEIGHT - BOX_OFFSET_BOTTOM


class Engine:
    def __init__(self):
        self.score = 0
        self.ball = []
        self.pallets = []

    def update(self, dt):
        for ball in self.ball:
            ball.acceleration = pygame.math.Vector2(0, 2)

    def drawBackground(self, screen):
        screen.fill(BACKGROUND_COLOR)

        # Left wall
        pygame.draw.rect(screen, BOX_COLOR, (BOX_POSITION_LEFT,
                                             BOX_OFFSET_TOP,
                                             BOX_THICKNESS,
                                             WINDOW_HEIGHT))
        # Right wall
        pygame.draw.rect(screen, BOX_COLOR, (BOX_POSITION_RIGHT,
                                             BOX_OFFSET_TOP,
                                             BOX_THICKNESS,
                                             WINDOW_HEIGHT))
        # Top left wall
        pygame.draw.rect(screen, BOX_COLOR, (BOX_THICKNESS,
                                             0,
                                             (WINDOW_WIDTH / 4) - BOX_THICKNESS,
                                             BOX_THICKNESS))
        # Top right wall
        pygame.draw.rect(screen, BOX_COLOR, ((3 * WINDOW_WIDTH / 4),
                                             0,
                                             (WINDOW_WIDTH / 4) - BOX_THICKNESS,
                                             BOX_THICKNESS))
        # Bottom left wall
        pygame.draw.rect(screen, BOX_COLOR, (BOX_THICKNESS,
                                             WINDOW_HEIGHT,
                                             (WINDOW_WIDTH / 4) - BOX_THICKNESS,
                                             BOX_THICKNESS))
        # Bottom right wall
        pygame.draw.rect(screen, BOX_COLOR, ((3 * WINDOW_WIDTH / 4),
                                             WINDOW_HEIGHT,
                                             (WINDOW_WIDTH / 4) - BOX_THICKNESS,
                                             BOX_THICKNESS))

    def drawBall(self, screen):  # TODO : voir pour optimiser cette partie étant donné qu'il n'y a qu'une balle
        for ball in self.ball:
            ball.draw(screen)

    def drawPallets(self, screen):
        for pallet in self.pallets:
            pallet.draw(screen)

    def dropPallets(self, x, y):
        new_pallets = Pallets(x, y)
        self.ball.append(new_pallets)
        return new_pallets

    def dropBall(self, x, y):
        new_ball = Ball(x, y)
        self.ball.append(new_ball)
        return new_ball
