import numpy as np
from puzzle import get_local_minimum_matrix

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
    # file = 'small_input.txt'
    file = 'input.txt'
    heights = np.genfromtxt(file, delimiter=1, dtype=int)
    min = get_local_minimum_matrix(heights)
    low_points = np.transpose((heights < min).nonzero())

    basin_sizes = []
    for x in low_points:
        free = []
        checked = []
        free.append(list(x))
        while(free != []):
            determine_local_basin(heights, free, checked)

        basin_sizes.append(len(checked))

    sorted = np.sort(basin_sizes)
    answer = sorted[-3] * sorted[-2] * sorted[-1]
    print(f'{answer = }')
