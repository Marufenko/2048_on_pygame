import pygame
from pygame import *

WIN_WIDTH = 400
WIN_HEIGHT = 400
SPACE_FOR_ONE_CELL = 100
DISPLAY = (WIN_WIDTH, WIN_HEIGHT)
BACKGROUND_COLOR = "#000000"
CELL_WIDTH = 96
CELL_HEIGHT = 96
CELL = (CELL_WIDTH, CELL_HEIGHT)
CELL_BACKGROUND_COLOR = "#ffffff"
BORDER_SIZE = 2


def main():
    pygame.init()
    screen = pygame.display.set_mode(DISPLAY)
    pygame.display.set_caption("2018 on pygame")
    background = Surface(DISPLAY)
    background.fill(Color(BACKGROUND_COLOR))

    while 1:  # main loop

        # input handling
        for e in pygame.event.get():
            if e.type == QUIT:
                raise SystemExit("QUIT")

        screen.blit(background, (0, 0))

        # draw cells
        x = y = BORDER_SIZE
        for i in range(4):
            for j in range(4):
                cell = Surface(CELL)
                cell.fill(Color(CELL_BACKGROUND_COLOR))
                screen.blit(cell, (x, y))
                x += SPACE_FOR_ONE_CELL
            y += SPACE_FOR_ONE_CELL
            x = BORDER_SIZE

        pygame.display.update()


if __name__ == "__main__":
    main()
