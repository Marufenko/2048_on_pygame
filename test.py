import random


def main():
    a, b = [0, 1]
    print(a)
    print(b)


#     data_array = [[0, 0, 0, 0],
#              [0, 0, 0, 0],
#              [0, 0, 0, 0],
#              [0, 0, 0, 0]]
#     print(data_array)
#     for i in range(5):
#         a = generate_input_value()
#         print(a)
#         b, c = generate_coordinates_for_input(data_array)
#         print(b, c)
#         data_array[b][c] = a
#         print(data_array)
#
# def generate_input_value():
#     input_values = [2, 4]
#     return random.choice(input_values)
#
# def generate_coordinates_for_input(input_array):
#     empty_coordinates = []
#     for i in range(len(input_array)):
#         for j in range(len(input_array[i])):
#             if input_array[i][j] == 0:
#                 empty_coordinates.append([i, j])
#
#     return random.choice(empty_coordinates)

if __name__ == "__main__":
    main()