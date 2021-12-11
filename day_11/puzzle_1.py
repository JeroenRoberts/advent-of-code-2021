import numpy as np

def increment_neighbours(data: np.array, i: int, j: int) -> None:
    for k in range(max(i-1, 0), i+2):
        for l in range(max(j-1, 0), j+2):
            if k == i and l == j: #self
                pass
            else: #neighbour
                try:
                    data[k, l] += 1
                except IndexError as error:
                    # print(error)
                    pass

def perform_step(data: np.array) -> int:
    #1. Increment all
    data += 1

    #2. flashing
    flashed = np.zeros(data.shape, dtype=bool)
    while np.all(flashed[np.where(data > 9)]) == False :
        for i in range(data.shape[0]):
            for j in range(data.shape[1]):
                if data[i, j] > 9 and flashed[i, j] == False:
                    flashed[i, j] = True
                    increment_neighbours(data, i, j)

    #3. octopus that flashed gets set to 0
    data[flashed] = 0
    return flashed.sum()


if __name__ == "__main__":
    # file = 'smaller_input.txt'
    # file = 'small_input.txt'
    file = 'input.txt'
    data = np.genfromtxt(file, delimiter=1, dtype=int)
    print(data)
    total_flashes = 0
    for step in range(100):
        # print(f'\n\n{step = }')
        # print(data)
        total_flashes += perform_step(data)
    print(total_flashes)
