import random
import pygame
from pygame import *

from CellImage import Cell

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
    # generate first two values on the start
    generate_new_value(data_array)
    generate_new_value(data_array)

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
        right = left = up = down = False

        # input handling
        for e in pygame.event.get():
            if e.type == KEYUP and e.key == K_RIGHT:
                right = True
            if e.type == KEYUP and e.key == K_LEFT:
                left = True
            if e.type == KEYUP and e.key == K_UP:
                up = True
            if e.type == KEYUP and e.key == K_DOWN:
                down = True
            if e.type == QUIT:
                raise SystemExit("QUIT")

        # data recalculate/generates and screen is overrides in the main loop to triger it once per key click
        while right or left or up or down:

            movement_done = False  # flag to track was movement done or note
            if left:
                data_array, movement_done = left_turn(data_array)
            if right:
                data_array, movement_done = right_turn(data_array)
            if up:
                data_array, movement_done = up_turn(data_array)
            if down:
                data_array, movement_done = down_turn(data_array)

            if movement_done:  # generate new value only when movement is done
                generate_new_value(data_array)

            x = y = 0
            for i in range(4):
                for j in range(4):
                    print(x, y, data_array[i][j])
                    cell = Cell(x, y, data_array[i][j])
                    entities.add(cell)
                    x += SPACE_FOR_ONE_CELL
                y += SPACE_FOR_ONE_CELL
                x = 0

            right = left = up = down = False

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

    if empty_coordinates:
        result = random.choice(empty_coordinates)
    else:
        result = [5, 5]  # random out or range index
    return result


def generate_new_value(data_array):
    new_value = generate_input_value()  # generate 2 or 4 Int randomly
    x_coor, y_coor = generate_coordinates_for_input(data_array)  # coordinated for new value
    try:
        data_array[x_coor][y_coor] = new_value
    except IndexError:
        pass  # no new value in case there is no empty cell


def left_turn(data_array):
    movement_done = False
    for i in range(4):  # execute for each of 4 lines
        sum_done = False  # only two values may be sum up under one move
        for k in range(3):  # max three-cell offset
            for j in range(3):  # execute for each of three pairs of values
                if not sum_done:
                    if data_array[i][j] == data_array[i][j + 1] and data_array[i][j] != 0:
                        data_array[i][j] *= 2
                        data_array[i][j + 1] = 0
                        sum_done = True
                        movement_done = True
                if data_array[i][j] == 0 and data_array[i][j + 1] != 0:
                    data_array[i][j] = data_array[i][j + 1]
                    data_array[i][j + 1] = 0
                    movement_done = True

    return data_array, movement_done


def right_turn(data_array):
    movement_done = False
    for i in range(4):  # execute for each of 4 lines
        sum_done = False  # only two values may be sum up under one move
        for k in range(3):  # max three-cell offset
            for j in range(3):  # execute for each of three pairs of values
                if not sum_done:
                    if data_array[i][-(j+1)] == data_array[i][-(j + 2)] and data_array[i][-(j+1)] != 0:
                        data_array[i][-(j+1)] *= 2
                        data_array[i][-(j + 2)] = 0
                        sum_done = True
                        movement_done = True
                if data_array[i][-(j+1)] == 0 and data_array[i][-(j + 2)] != 0:
                    data_array[i][-(j+1)] = data_array[i][-(j + 2)]
                    data_array[i][-(j + 2)] = 0
                    movement_done = True

    return data_array, movement_done


def up_turn(data_array):
    movement_done = False
    for j in range(4):  # execute for each of 4 columns
        sum_done = False  # only two values may be sum up under one move
        for k in range(3):  # max three-cell offset
            for i in range(3):  # execute for each of three pairs of values
                if not sum_done:
                    if data_array[i][j] == data_array[i+1][j] and data_array[i][j] != 0:
                        data_array[i][j] *= 2
                        data_array[i+1][j] = 0
                        sum_done = True
                        movement_done = True
                if data_array[i][j] == 0 and data_array[i+1][j] != 0:
                    data_array[i][j] = data_array[i+1][j]
                    data_array[i+1][j] = 0
                    movement_done = True

    return data_array, movement_done


def down_turn(data_array):
    movement_done = False
    for j in range(4):  # execute for each of 4 columns
        sum_done = False  # only two values may be sum up under one move
        for k in range(3):  # max three-cell offset
            for i in range(2, -1, -1):  # execute for each of three pairs of values
                if not sum_done:
                    if data_array[i+1][j] == data_array[i][j] and data_array[i+1][j] != 0:
                        data_array[i+1][j] *= 2
                        data_array[i][j] = 0
                        sum_done = True
                        movement_done = True
                if data_array[i+1][j] == 0 and data_array[i][j] != 0 :
                    data_array[i+1][j] = data_array[i][j]
                    data_array[i][j] = 0
                    movement_done = True

    return data_array, movement_done


if __name__ == "__main__":
    main()
