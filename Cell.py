from pygame import *

CELL_WIDTH = 96
CELL_HEIGHT = 96
CELL = (CELL_WIDTH, CELL_HEIGHT)
CELL_COLOR = "#ffffff"


class Cell(sprite.Sprite):
    def __init__(self, x, y,):
        sprite.Sprite.__init__(self)
        self.image = Surface(CELL)
        self.image.fill(Color(CELL_COLOR))
        self.rect = Rect(x, y, CELL_WIDTH, CELL_HEIGHT)
