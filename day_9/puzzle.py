import numpy as np

def get_local_minimum_matrix(matrix):
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
            roll[n_data['index'], :] = 99999
        elif n_data['type'] == 'column':
            roll[:, n_data['index']] = 99999
        translations[n] = roll

    local_minimum = 99999 * np.ones(matrix.shape, dtype=int)
    for k, t in translations.items():
        local_minimum = np.minimum(local_minimum, t)
    return local_minimum


if __name__ == "__main__":
    file = 'small_input.txt'
    heights = np.genfromtxt(file, delimiter=1, dtype=int)
    min = get_local_minimum_matrix(heights)
    # print(heights)
    # print(min)
    # print(heights < min)
    risk = (heights+1)[heights < min].sum()
    print(f'{risk = }')

