import pygame
from pygame import *

from Cell import Cell

WIN_WIDTH = 400
WIN_HEIGHT = 400
SPACE_FOR_ONE_CELL = 100
DISPLAY = (WIN_WIDTH, WIN_HEIGHT)
BACKGROUND_COLOR = "#000000"
CELL_BORDER_SIZE = 2


def main():
    pygame.init()
    screen = pygame.display.set_mode(DISPLAY)
    pygame.display.set_caption("2018 on pygame")
    background = Surface(DISPLAY)
    background.fill(Color(BACKGROUND_COLOR))

    screen_array = [[j for j in range(4)] for i in range(4)]

    # draw cells
    entities = pygame.sprite.Group()
    x = y = CELL_BORDER_SIZE
    for i in screen_array:
        for j in i:
            cell = Cell(x, y)
            entities.add(cell)
            x += SPACE_FOR_ONE_CELL
        y += SPACE_FOR_ONE_CELL
        x = CELL_BORDER_SIZE

    while 1:  # main loop

        # input handling
        for e in pygame.event.get():
            if e.type == QUIT:
                raise SystemExit("QUIT")

        screen.blit(background, (0, 0))
        entities.draw(screen)
        pygame.display.update()


if __name__ == "__main__":
    main()
