import pygame
from pygame import *

from Cell import Cell

WIN_WIDTH = 400
WIN_HEIGHT = 400
SPACE_FOR_ONE_CELL = 100
DISPLAY = (WIN_WIDTH, WIN_HEIGHT)


def main():
    pygame.init()
    screen = pygame.display.set_mode(DISPLAY)
    pygame.display.set_caption("2018 on pygame")
    background = Surface(DISPLAY)

    # data
    data_array = [[0, 0, 0, 0],
                  [0, 0, 0, 0],
                  [0, 0, 0, 0],
                  [0, 0, 0, 0]]

    # draw cells
    entities = pygame.sprite.Group()
    x = y = 0
    for i in range(4):
        for j in range(4):
            print(x, y, data_array[i][j])
            cell = Cell(x, y, data_array[i][j])
            entities.add(cell)
            x += SPACE_FOR_ONE_CELL
        y += SPACE_FOR_ONE_CELL
        x = 0

    while 1:  # main loop
        action = False

        # input handling
        for e in pygame.event.get():
            if e.type == QUIT:
                raise SystemExit("QUIT")

        while action:

            # draw updated cells here

            action = False

        screen.blit(background, (0, 0))
        entities.draw(screen)
        pygame.display.update()


if __name__ == "__main__":
    main()
