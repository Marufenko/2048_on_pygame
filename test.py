def main():
    data_array = [[2, 0, 0, 2],
                  [0, 2, 2, 2],
                  [0, 4, 2, 4],
                  [0, 8, 0, 8]]
    print(data_array)
    print(left_turn(data_array))



def left_turn(data_array):
    for k in range(3):
        for i in range(4):
            for j in range(3):
                if data_array[i][j] == data_array[i][j + 1]:
                    data_array[i][j] = data_array[i][j] * 2
                    data_array[i][j + 1] = 0
                if data_array[i][j] == 0:
                    data_array[i][j] = data_array[i][j + 1]
                    data_array[i][j + 1] = 0

    return data_array


if __name__ == "__main__":
    main()
