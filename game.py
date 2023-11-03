from objects import *

BACKGROUND_COLOR = 'black'
BOX_COLOR = 'white'
WINDOW_WIDTH = 600
WINDOW_HEIGHT = 800
CURSOR_SPEED = 200
BALL_SPEED_X = 200
BALL_SPEED_Y = -150
BOX_THICKNESS = 20
BOX_OFFSET_TOP = 0
BOX_OFFSET_HORIZ = 0
BOX_OFFSET_BOTTOM = 100
BOX_POSITION_LEFT = BOX_OFFSET_HORIZ
BOX_POSITION_RIGHT = WINDOW_WIDTH - BOX_THICKNESS
BOX_POSITION_BOTTOM = WINDOW_HEIGHT - BOX_THICKNESS
LENGTH_PALLETS = 100


class Engine:
    def __init__(self):
        self.score = [0, 0]
        self.ball = []
        self.pallets = []

    def update(self, dt):
        global BALL_SPEED_X, BALL_SPEED_Y
        for ball in self.ball:  # TODO : a terme, revoir la gestion des balles
            ball.x -= BALL_SPEED_X * dt
            ball.y -= BALL_SPEED_Y * dt
            if (ball.x - ball.radius) <= (BOX_POSITION_LEFT + BOX_THICKNESS):
                BALL_SPEED_X = -BALL_SPEED_X
            if (ball.x + ball.radius) >= BOX_POSITION_RIGHT:
                BALL_SPEED_X = -BALL_SPEED_X

            if (ball.y <= BOX_OFFSET_TOP) and ((ball.x - ball.radius) >= (WINDOW_WIDTH / 4)) and (
                    (ball.x + ball.radius) <= (3 * WINDOW_WIDTH / 4)):
                self.score[0] += 1
                print(self.score)
                ball.x = WINDOW_WIDTH / 2
                ball.y = WINDOW_HEIGHT / 2
                BALL_SPEED_X = -BALL_SPEED_X
                BALL_SPEED_Y = -BALL_SPEED_Y
            if (ball.y <= (BOX_THICKNESS + ball.radius)) and (ball.x - ball.radius) < (WINDOW_WIDTH / 4):
                BALL_SPEED_Y = -BALL_SPEED_Y
            if (ball.y <= (BOX_THICKNESS + ball.radius)) and (ball.x + ball.radius) > (3 * WINDOW_WIDTH / 4):
                BALL_SPEED_Y = -BALL_SPEED_Y

            if (ball.y >= WINDOW_HEIGHT) and ((ball.x - ball.radius) >= (WINDOW_WIDTH / 4)) and (
                    (ball.x + ball.radius) <= (3 * WINDOW_WIDTH / 4)):
                self.score[1] += 1
                print(self.score)
                ball.x = WINDOW_WIDTH / 2
                ball.y = WINDOW_HEIGHT / 2
                BALL_SPEED_X = -BALL_SPEED_X
                BALL_SPEED_Y = -BALL_SPEED_Y
            if (ball.y + ball.radius >= BOX_POSITION_BOTTOM) and (ball.x - ball.radius) < (WINDOW_WIDTH / 4):
                BALL_SPEED_Y = -BALL_SPEED_Y
            if (ball.y + ball.radius >= BOX_POSITION_BOTTOM) and (ball.x + ball.radius) > (3 * WINDOW_WIDTH / 4):
                BALL_SPEED_Y = -BALL_SPEED_Y

        for pallet in self.pallets:
            keys_pressed = pygame.key.get_pressed()
            if keys_pressed[pygame.K_LEFT]:
                pallet.x -= CURSOR_SPEED * dt
            if keys_pressed[pygame.K_RIGHT]:
                pallet.x += CURSOR_SPEED * dt
            # Détection d'une collision entre le pallet et le mur gauche
            if pallet.x <= (BOX_POSITION_LEFT + BOX_THICKNESS):
                # on fige la position du pallet pour qu'il n'aille pas plus loin
                pallet.x = BOX_POSITION_LEFT + BOX_THICKNESS

            # Détection d'une collision entre le pallet et le mur droit
            if pallet.x + LENGTH_PALLETS >= BOX_POSITION_RIGHT:
                # on fige la position du pallet pour qu'il n'aille pas plus loin
                pallet.x = BOX_POSITION_RIGHT - LENGTH_PALLETS

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
                                             BOX_POSITION_BOTTOM,
                                             (WINDOW_WIDTH / 4) - BOX_THICKNESS,
                                             BOX_THICKNESS))
        # Bottom right wall
        pygame.draw.rect(screen, BOX_COLOR, ((3 * WINDOW_WIDTH / 4),
                                             BOX_POSITION_BOTTOM,
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
        self.pallets.append(new_pallets)
        return new_pallets

    def dropBall(self, x, y):
        new_ball = Ball(x, y)
        self.ball.append(new_ball)
        return new_ball
