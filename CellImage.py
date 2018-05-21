from pygame import *

CELL_WIDTH = 100
CELL_HEIGHT = 100
CELL = (CELL_WIDTH, CELL_HEIGHT)


class Cell(sprite.Sprite):
    def __init__(self, x, y, value, update_flag):

        if update_flag:
            image_file = "images/" + str(value) + "_update.png"
        else:
            image_file = "images/" + str(value) + ".png"

        sprite.Sprite.__init__(self)
        self.image = Surface(CELL)
        self.image = image.load(image_file)
        self.rect = Rect(x, y, CELL_WIDTH, CELL_HEIGHT)
