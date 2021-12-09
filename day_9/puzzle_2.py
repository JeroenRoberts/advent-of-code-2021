import numpy as np
from puzzle import get_local_minimum_matrix

def get_local_maximum_matrix(matrix):
    directions = [-1, 1]
    axis = np.array([0, 1])
    neighbours = {}
    neighbours['up'] = {'direction': -1, 'axis': 0, 'type': 'row', 'index': -1}
    neighbours['down'] = {'direction': 1, 'axis': 0, 'type': 'row', 'index': 0}
    neighbours['left'] = {'direction': -1, 'axis': 1, 'type': 'column', 'index': -1}
    neighbours['right'] = {'direction': 1, 'axis': 1, 'type': 'column', 'index': 0}
    translations = {}
    for n, n_data in neighbours.items():
        roll = np.roll(matrix, n_data['direction'], axis=n_data['axis'])
        if n_data['type'] == 'row':
            roll[n_data['index'], :] = 0
        elif n_data['type'] == 'column':
            roll[:, n_data['index']] = 0
        translations[n] = roll

    local_minimum = 0 * np.ones(matrix.shape, dtype=int)
    for k, t in translations.items():
        local_minimum = np.maximum(local_minimum, t)
    return local_minimum


def determine_local_basin(heights, free, checked):
    x = free[0]
    for delta in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
        n = np.array(x) + delta
        if np.all(n < heights.shape) and np.all(n >= 0):
            n = list(n)
            if heights[n[0], n[1]] < 9:
                if n not in checked and n not in free:
                    free.append(n)
    free.remove(x)
    checked.append(x)

    

if __name__ == "__main__":
    file = 'small_input.txt'
    heights = np.genfromtxt(file, delimiter=1, dtype=int)
    max = get_local_maximum_matrix(heights)
    min = get_local_minimum_matrix(heights)
    # print(min)
    print(heights)
    low_points = np.transpose((heights < min).nonzero())

    basin_sizes = []
    for x in low_points:
        free = []
        checked = []
        free.append(list(x))
        while(free != []):
            determine_local_basin(heights, free, checked)

        basin_sizes.append(len(checked))
        # print(len(checked))
        # copy = heights.copy()
        # for check in checked:
        #     copy[check[0], check[1]] = 404

        # print(copy)
        # print(heights)
        # break
    sorted = np.sort(basin_sizes)
    answer = sorted[-3] * sorted[-2] * sorted[-1]
    print(f'{answer = }')

        # heights[x[0], x[1]] = 404
    # print(heights)
    # print(np.where(low_points == True))
    # print(max)
    # print(heights[heights < 9])
    # heights[heights == 9] = 404
    # print(heights)
    # basin_inside = max < 9
    # print(basin_inside)
    # print(heights)
    # print(min)
    # print(heights < min)
    # risk = (heights+1)[heights < min].sum()
    # print(f'{risk = }')

