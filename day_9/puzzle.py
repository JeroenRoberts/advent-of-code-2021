import numpy as np


if __name__ == "__main__":
    file = 'small_input.txt'
    heights = np.genfromtxt(file, delimiter=1, dtype=int)
    min_of_neighbours = np.zeros(heights.shape)

    first_row = heights[0, :]
    first_row_shift_right = np.roll(heights[0, :], 1)
    first_row_shift_right[0] = 99999 #invalid neighbour (no pbc)
    first_row_shift_left = np.roll(heights[0, :], -1)
    first_row_shift_left[-1] = 99999 #invalid neighbour (no pbc)
    print(first_row)
    print(first_row_shift_right)
    print(first_row_shift_left)
    minimum = np.minimum(first_row_shift_left, first_row_shift_right)
    print(first_row < minimum)


    # print(heights.shape)
    # for k in range(heights.shape[0]):
    #     for l in range(heights.shape[1]):
    #     print(k, l)

    # print(heights)
