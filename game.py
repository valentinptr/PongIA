from objects import *


class Engine:
    def __init__(self):
        self.score = 0
        self.ball = []
        self.pallets = []

    def update(self, dt):
        a = 0

    def drawBackground(self, screen):
        b = 0

    def drawBall(self, screen): # TODO : voir pour optimiser cette partie étant donné qu'il n'y a qu'une balle
        for ball in self.ball:
            ball.draw(screen)

    def drawPallets(self, screen):
        for pallet in self.pallets:
            pallet.draw(screen)

    def draw(self, screen):
        self.drawBackground(screen)
        self.drawBall(screen)
        self.drawPallets(screen)

    def dropBall(self, screen, x, y):
        new_ball = Ball(x, y)
        self.ball.append(new_ball)
        return new_ball

    def dropPallets(self, screen, x, y):
        new_pallets_j1 = Pallets(x, y)
        new_pallets_j2 = Pallets(x, y + 300)
        self.ball.append(new_pallets_j1)
        self.ball.append(new_pallets_j2)
        return new_pallets_j1, new_pallets_j2
