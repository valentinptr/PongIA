import random
from objects import *

BACKGROUND_COLOR = 'black'
BOX_COLOR = 'white'
WINDOW_WIDTH = 600
WINDOW_HEIGHT = 800
CURSOR_SPEED = 200
CURSOR_SPEED_IA = 100
BOX_THICKNESS = 20
BOX_OFFSET_TOP = 0
BOX_OFFSET_HORIZ = 0
BOX_OFFSET_BOTTOM = 100
BOX_POSITION_LEFT = BOX_OFFSET_HORIZ
BOX_POSITION_RIGHT = WINDOW_WIDTH - BOX_THICKNESS
BOX_POSITION_BOTTOM = WINDOW_HEIGHT - BOX_THICKNESS
LENGTH_PALLETS = 100
MIN_SPEED = 200
MAX_SPEED = 500


def direction():
    """
    This function is used to determine a random speed
    :return:  with random sign
    """
    speed = random.randint(MIN_SPEED, MAX_SPEED)
    sign = random.randint(0, 100000000)
    if (sign % 2) == 0:
        speed = -speed
    return speed


BALL_SPEED_X = direction()  # we assign an X speed
BALL_SPEED_Y = direction()  # we assign an Y speed


class Engine:
    def __init__(self):
        """
        this is the init function of the class Engine
        """
        self.score = [0, 0]  # [0] : player 1 and [1] for player 2
        self.ball = Ball(WINDOW_WIDTH / 2, WINDOW_HEIGHT / 2)  # initialization of the ball
        self.pallets = []  # initialization of the 2 pallets

    def update(self, dt):
        """
        this function is used to update the behavior of the speed and the pallets
        :param dt: interval of time between 2 frames
        :return: does not return anything
        """
        global BALL_SPEED_X, BALL_SPEED_Y

        print(self.ball.x, self.ball.y, BALL_SPEED_X, BALL_SPEED_Y)

        # initialization of the X and Y speed of the ball
        self.ball.x += int(BALL_SPEED_X * dt)
        self.ball.y += int(BALL_SPEED_Y * dt)

        # used to check if the ball as collided with the left wall
        if (self.ball.x - self.ball.radius) < (BOX_POSITION_LEFT + BOX_THICKNESS):
            self.ball.x = BOX_POSITION_LEFT + BOX_THICKNESS + self.ball.radius
            BALL_SPEED_X = -BALL_SPEED_X  # the X speed is then reversed

        # used to check if the ball as collided with the right wall
        if (self.ball.x + self.ball.radius) > BOX_POSITION_RIGHT:
            self.ball.x = BOX_POSITION_RIGHT - self.ball.radius
            BALL_SPEED_X = -BALL_SPEED_X  # the X speed is then reversed

        # used to check if the ball as entered the upper goal
        if self.ball.y < BOX_OFFSET_TOP:
            self.score[1] += 1  # the score is updated
            self.ball.x = WINDOW_WIDTH / 2  # the ball goes back to the center of the window
            self.ball.y = WINDOW_HEIGHT / 2  # the ball goes back to the center of the window
            BALL_SPEED_X = direction()  # a new X speed is called
            BALL_SPEED_Y = direction()  # a new Y speed is called

        # used to check if the ball as entered the lower goal
        if self.ball.y > WINDOW_HEIGHT:
            self.score[0] += 1
            self.ball.x = WINDOW_WIDTH / 2
            self.ball.y = WINDOW_HEIGHT / 2
            BALL_SPEED_X = direction()
            BALL_SPEED_Y = direction()

        # used to control the pallet 1 with the keyboard
        keys_pressed = pygame.key.get_pressed()
        if keys_pressed[pygame.K_LEFT]:
            self.pallets[0].x -= CURSOR_SPEED * dt
        if keys_pressed[pygame.K_RIGHT]:
            self.pallets[0].x += CURSOR_SPEED * dt

        # The pallet 2 is controlled autonomously
        if self.ball.y > WINDOW_HEIGHT / 2:  # check to see if the ball is coming to pallet 2
            if self.ball.x < WINDOW_WIDTH / 2:  # check to see if the ball is on the left side
                self.pallets[1].x -= CURSOR_SPEED_IA * dt
            elif self.ball.x > WINDOW_WIDTH / 2:  # check to see if the ball is on the right side
                self.pallets[1].x += CURSOR_SPEED_IA * dt
        else:  # used to drive back the pallet 2 after a move
            if self.pallets[1].x < (WINDOW_WIDTH / 2 - 50):
                self.pallets[1].x += CURSOR_SPEED * dt
            elif self.pallets[1].x > (WINDOW_WIDTH / 2 - 50):
                self.pallets[1].x -= CURSOR_SPEED * dt
            else:  # used to maintain pallet 2 in its position
                self.pallets[1].x = WINDOW_WIDTH / 2 - 50

        # used to check if the pallets are not going outside the walls
        for pallet in self.pallets:
            # used to check if the pallet as collided with the left wall
            if pallet.x <= (BOX_POSITION_LEFT + BOX_THICKNESS):
                # used to maintain pallet in its position
                pallet.x = BOX_POSITION_LEFT + BOX_THICKNESS

            # used to check if the pallet as collided with the right wall
            if (pallet.x + LENGTH_PALLETS) >= BOX_POSITION_RIGHT:
                # used to maintain pallet in its position
                pallet.x = BOX_POSITION_RIGHT - LENGTH_PALLETS

        # used to check is there is a collision between the ball and the pallet 1
        if (self.ball.y - self.ball.radius) < self.pallets[0].y and (
                (self.ball.x + self.ball.radius) > self.pallets[0].x) and (
                (self.ball.x - self.ball.radius) < (self.pallets[0].x + LENGTH_PALLETS)):
            self.ball.y = self.pallets[0].y + self.ball.radius
            BALL_SPEED_Y = -BALL_SPEED_Y  # Y speed of the ball is then reversed

        # used to check is there is a collision between the ball and the pallet 2
        if (self.ball.y + self.ball.radius) > self.pallets[1].y and (
                (self.ball.x + self.ball.radius) > self.pallets[1].x) and (
                (self.ball.x - self.ball.radius) < (self.pallets[1].x + LENGTH_PALLETS)):
            self.ball.y = self.pallets[1].y - self.ball.radius
            BALL_SPEED_Y = -BALL_SPEED_Y  # Y speed of the ball is then reversed

    @staticmethod
    def draw_background(screen):
        """
        This static method is used to print the wall on the screen
        :param screen: window that have been initialized in main.py
        :return: does not return anything
        """
        # the background is filled with a specified color, here : black
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

    def draw_ball(self, screen):
        """
        This method is used to draw the ball on the screen
        :param screen: window that have been initialized in main.py
        :return: does not return anything
        """
        self.ball.draw(screen)

    def draw_pallets(self, screen):
        """
        This method is used to draw the pallets on the screen
        :param screen: window that have been initialized in main.py
        :return: does not return anything
        """
        for pallet in self.pallets:
            pallet.draw(screen)

    def drop_pallets(self, x, y):
        """
        This method is used to create and then drop the pallets on the screen
        :param x: initialization of the X axis of the pallet
        :param y: initialization of the Y axis of the pallet
        :return: return a Pallets object
        """
        new_pallets = Pallets(x, y)
        self.pallets.append(new_pallets)
        return new_pallets
