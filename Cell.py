from pygame import *

CELL_WIDTH = 100
CELL_HEIGHT = 100
CELL = (CELL_WIDTH, CELL_HEIGHT)


class Cell(sprite.Sprite):
    def __init__(self, x, y,):
        sprite.Sprite.__init__(self)
        self.image = Surface(CELL)
        self.image = image.load("images/empty.png")
        self.rect = Rect(x, y, CELL_WIDTH, CELL_HEIGHT)
