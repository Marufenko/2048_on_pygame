import random
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
            if e.type == KEYUP and e.key == K_RIGHT:
                action = True

        while action:

            # draw updated cells here
            new_value = generate_input_value()
            x_coor, y_coor = generate_coordinates_for_input(data_array)  # coordinated for new value
            data_array[x_coor][y_coor] = new_value

            x = y = 0
            for i in range(4):
                for j in range(4):
                    print(x, y, data_array[i][j])
                    cell = Cell(x, y, data_array[i][j])
                    entities.add(cell)
                    x += SPACE_FOR_ONE_CELL
                y += SPACE_FOR_ONE_CELL
                x = 0

            action = False

        screen.blit(background, (0, 0))
        entities.draw(screen)
        pygame.display.update()


def generate_input_value():
    input_values = [2, 4]
    return random.choice(input_values)


def generate_coordinates_for_input(input_array):
    empty_coordinates = []
    for i in range(4):
        for j in range(4):
            if input_array[i][j] == 0:
                empty_coordinates.append([i, j])
    return random.choice(empty_coordinates)


if __name__ == "__main__":
    main()
