def main():
    data_array = [[8, 0, 0, 2],
                  [0, 0, 2, 2],
                  [0, 4, 2, 4],
                  [0, 4, 4, 8]]
    for i in range(4):
        print(data_array[i])
    a = down_turn(data_array)
    print('')
    for i in range(4):
        print(a[i])


def down_turn(data_array):
    for j in range(4):  # execute for each of 4 columns
        sum_done = False  # only two values may be sum up under one move
        for k in range(3):  # max three-cell offset
            for i in range(2, -1, -1):  # execute for each of three pairs of values
                if not sum_done:
                    if data_array[i+1][j] == data_array[i][j] and data_array[i+1][j] != 0:
                        data_array[i+1][j] *= 2
                        data_array[i][j] = 0
                        sum_done = True
                if data_array[i+1][j] == 0:
                    data_array[i+1][j] = data_array[i][j]
                    data_array[i][j] = 0

    return data_array


def up_turn(data_array):
    for j in range(4):  # execute for each of 4 columns
        sum_done = False  # only two values may be sum up under one move
        for k in range(3):  # max three-cell offset
            for i in range(3):  # execute for each of three pairs of values
                if not sum_done:
                    if data_array[i][j] == data_array[i+1][j] and data_array[i][j] != 0:
                        data_array[i][j] *= 2
                        data_array[i+1][j] = 0
                        sum_done = True
                if data_array[i][j] == 0:
                    data_array[i][j] = data_array[i+1][j]
                    data_array[i+1][j] = 0

    return data_array


def right_turn(data_array):
    for i in range(4):  # execute for each of 4 lines
        sum_done = False  # only two values may be sum up under one move
        for k in range(3):  # max three-cell offset
            for j in range(3):  # execute for each of three pairs of values
                if not sum_done:
                    if data_array[i][-(j+1)] == data_array[i][-(j + 2)] and data_array[i][-(j+1)] != 0:
                        data_array[i][-(j+1)] = data_array[i][-(j+1)] * 2
                        data_array[i][-(j + 2)] = 0
                        sum_done = True
                if data_array[i][-(j+1)] == 0:
                    data_array[i][-(j+1)] = data_array[i][-(j + 2)]
                    data_array[i][-(j + 2)] = 0

    return data_array


def left_turn(data_array):
    for i in range(4):  # execute for each of 4 lines
        sum_done = False  # only two values may be sum up under one move
        for k in range(3):  # max three-cell offset
            for j in range(3):  # execute for each of three pairs of values
                if not sum_done:
                    if data_array[i][j] == data_array[i][j + 1] and data_array[i][j] != 0:
                        data_array[i][j] = data_array[i][j] * 2
                        data_array[i][j + 1] = 0
                        sum_done = True
                if data_array[i][j] == 0:
                    data_array[i][j] = data_array[i][j + 1]
                    data_array[i][j + 1] = 0

    return data_array


if __name__ == "__main__":
    main()
