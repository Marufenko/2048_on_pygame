from pygame import *

CELL_WIDTH = 100
CELL_HEIGHT = 100
CELL = (CELL_WIDTH, CELL_HEIGHT)


class Cell(sprite.Sprite):
    def __init__(self, x, y, value):

        if value == 0:
            image_file = "images/empty.png"
        elif value == 2:
            image_file = "images/2.png"
        elif value == 4:
            image_file = "images/4.png"
        elif value == 8:
            image_file = "images/8.png"
        elif value == 16:
            image_file = "images/16.png"
        elif value == 32:
            image_file = "images/32.png"
        elif value == 64:
            image_file = "images/64.png"
        elif value == 128:
            image_file = "images/128.png"
        elif value == 256:
            image_file = "images/256.png"
        elif value == 512:
            image_file = "images/512.png"
        elif value == 1024:
            image_file = "images/1024.png"
        elif value == 2048:
            image_file = "images/2048.png"
        else:
            pass

        sprite.Sprite.__init__(self)
        self.image = Surface(CELL)
        self.image = image.load(image_file)
        self.rect = Rect(x, y, CELL_WIDTH, CELL_HEIGHT)
