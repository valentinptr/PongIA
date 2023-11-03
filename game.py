import random
from objects import *

BACKGROUND_COLOR = 'black'
BOX_COLOR = 'white'
WINDOW_WIDTH = 600
WINDOW_HEIGHT = 800
CURSOR_SPEED = 200
CURSOR_SPEED_IA = 10
BOX_THICKNESS = 20
BOX_OFFSET_TOP = 0
BOX_OFFSET_HORIZ = 0
BOX_OFFSET_BOTTOM = 100
BOX_POSITION_LEFT = BOX_OFFSET_HORIZ
BOX_POSITION_RIGHT = WINDOW_WIDTH - BOX_THICKNESS
BOX_POSITION_BOTTOM = WINDOW_HEIGHT - BOX_THICKNESS
LENGTH_PALLETS = 100
MIN_SPEED = 50
MAX_SPEED = 300


def direction():
    speed = random.randint(MIN_SPEED, MAX_SPEED)
    sign = random.randint(0, 100000000)
    if (sign % 2) == 0:
        speed = -speed
    return speed


BALL_SPEED_X = direction()
BALL_SPEED_Y = direction()


class Engine:
    def __init__(self):
        self.score = [0, 0]
        self.ball = Ball(WINDOW_WIDTH / 2, WINDOW_HEIGHT / 2)
        self.pallets = []

    def update(self, dt):
        global BALL_SPEED_X, BALL_SPEED_Y

        self.ball.x -= BALL_SPEED_X * dt
        self.ball.y -= BALL_SPEED_Y * dt

        if (self.ball.x - self.ball.radius) <= (BOX_POSITION_LEFT + BOX_THICKNESS):
            BALL_SPEED_X = -BALL_SPEED_X

        if (self.ball.x + self.ball.radius) >= BOX_POSITION_RIGHT:
            BALL_SPEED_X = -BALL_SPEED_X

        if (self.ball.y <= BOX_OFFSET_TOP) and ((self.ball.x - self.ball.radius) >= (WINDOW_WIDTH / 4)) and (
                (self.ball.x + self.ball.radius) <= (3 * WINDOW_WIDTH / 4)):
            self.score[1] += 1
            self.ball.x = WINDOW_WIDTH / 2
            self.ball.y = WINDOW_HEIGHT / 2
            BALL_SPEED_X = direction()
            BALL_SPEED_Y = direction()

        if (self.ball.y <= (BOX_THICKNESS + self.ball.radius)) and (
                self.ball.x - self.ball.radius) < (WINDOW_WIDTH / 4):
            BALL_SPEED_Y = -BALL_SPEED_Y

        if (self.ball.y <= (BOX_THICKNESS + self.ball.radius)) and (
                self.ball.x + self.ball.radius) > (3 * WINDOW_WIDTH / 4):
            BALL_SPEED_Y = -BALL_SPEED_Y

        if (self.ball.y >= WINDOW_HEIGHT) and ((self.ball.x - self.ball.radius) >= (WINDOW_WIDTH / 4)) and (
                (self.ball.x + self.ball.radius) <= (3 * WINDOW_WIDTH / 4)):
            self.score[0] += 1
            self.ball.x = WINDOW_WIDTH / 2
            self.ball.y = WINDOW_HEIGHT / 2
            BALL_SPEED_X = direction()
            BALL_SPEED_Y = direction()

        if (self.ball.y + self.ball.radius >= BOX_POSITION_BOTTOM) and (
                self.ball.x - self.ball.radius) < (WINDOW_WIDTH / 4):
            BALL_SPEED_Y = -BALL_SPEED_Y

        if (self.ball.y + self.ball.radius >= BOX_POSITION_BOTTOM) and (
                self.ball.x + self.ball.radius) > (3 * WINDOW_WIDTH / 4):
            BALL_SPEED_Y = -BALL_SPEED_Y

        # Controle du pallet 1 via les touches du clavier
        keys_pressed = pygame.key.get_pressed()
        if keys_pressed[pygame.K_LEFT]:
            self.pallets[0].x -= CURSOR_SPEED * dt
        if keys_pressed[pygame.K_RIGHT]:
            self.pallets[0].x += CURSOR_SPEED * dt

        # Gestion autonome du pallet 2
        if self.ball.y > 600:
            if self.ball.x < WINDOW_WIDTH/2:
                self.pallets[1].x -= CURSOR_SPEED_IA * dt
            elif self.ball.x > WINDOW_WIDTH/2:
                self.pallets[1].x += CURSOR_SPEED_IA * dt
        else:
            if self.pallets[1].x < (WINDOW_WIDTH / 2 - 50):
                self.pallets[1].x += CURSOR_SPEED * dt
            elif self.pallets[1].x > (WINDOW_WIDTH / 2 - 50):
                self.pallets[1].x -= CURSOR_SPEED * dt
            else:
                self.pallets[1].x = WINDOW_WIDTH / 2 - 50

        # sécurité pour que les pallets ne sortent pas du cadre
        for pallet in self.pallets:
            # Détection d'une collision entre le pallet et le mur gauche
            if pallet.x <= (BOX_POSITION_LEFT + BOX_THICKNESS):
                # on fige la position du pallet pour qu'il n'aille pas plus loin
                pallet.x = BOX_POSITION_LEFT + BOX_THICKNESS

            # Détection d'une collision entre le pallet et le mur droit
            if (pallet.x + LENGTH_PALLETS) >= BOX_POSITION_RIGHT:
                # on fige la position du pallet pour qu'il n'aille pas plus loin
                pallet.x = BOX_POSITION_RIGHT - LENGTH_PALLETS

        if (self.ball.y - self.ball.radius) <= self.pallets[0].y and (
                (self.ball.x + self.ball.radius) >= self.pallets[0].x) and (
                (self.ball.x - self.ball.radius) <= (self.pallets[0].x + LENGTH_PALLETS)):
            BALL_SPEED_Y = -BALL_SPEED_Y
        if (self.ball.y + self.ball.radius) >= self.pallets[1].y and (
                (self.ball.x + self.ball.radius) >= self.pallets[1].x) and (
                (self.ball.x - self.ball.radius) <= (self.pallets[1].x + LENGTH_PALLETS)):
            BALL_SPEED_Y = -BALL_SPEED_Y

    @staticmethod
    def drawBackground(screen):
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
                                             BOX_POSITION_BOTTOM,
                                             (WINDOW_WIDTH / 4) - BOX_THICKNESS,
                                             BOX_THICKNESS))
        # Bottom right wall
        pygame.draw.rect(screen, BOX_COLOR, ((3 * WINDOW_WIDTH / 4),
                                             BOX_POSITION_BOTTOM,
                                             (WINDOW_WIDTH / 4) - BOX_THICKNESS,
                                             BOX_THICKNESS))

    def drawBall(self, screen):
        self.ball.draw(screen)

    def drawPallets(self, screen):
        for pallet in self.pallets:
            pallet.draw(screen)

    def dropPallets(self, x, y):
        new_pallets = Pallets(x, y)
        self.pallets.append(new_pallets)
        return new_pallets
