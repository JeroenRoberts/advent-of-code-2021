import numpy as np

def check_boundary(i: int, bound: int) -> bool:
    if i >= 0 and i < bound:
        return True
    else:
        return False


# if check_boundary(i, data.shape[0]) and check_boundary(j, data.shape[1]):
def increment_neighbours(data: np.array, i: int, j: int) -> None:
    for k in range(i-1, i+2):
        for l in range(j-1, j+2):
            if k == i and l == j: #self
                pass
            else: #neighbour
                try:
                    data[k, l] += 1
                except IndexError as error:
                    # print(error)
                    pass

def perform_step(data: np.array):
    #1. Increment all
    for i in range(data.shape[0]):
        for j in range(data.shape[1]):
            data[i, j] += 1

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


if __name__ == "__main__":
    file = 'smaller_input.txt'
    data = np.genfromtxt(file, delimiter=1, dtype=int)
    print(data)
    for step in range(3):
        perform_step(data)
        print(data)
    # data[0, 0] = 9
    # for i in range(data.shape[0]):
    #     for j in range(data.shape[1]):
    #         data[i, j] += 1

    # flashed = np.zeros(data.shape, dtype=bool)
    # # print(np.where(data > 9))
    # # print(flashed
    # # print(flashed[np.where(data > 9)])
    # # print(np.all(flashed[np.where(data > 9)]))
    # while np.all(flashed[np.where(data > 9)]) == False :
    #     # print(data)
    #     # print(flashed[np.where(data > 9)])
    #     # print(np.all(flashed[np.where(data > 9)]))
    #     for i in range(data.shape[0]):
    #         for j in range(data.shape[1]):
    #             if data[i, j] > 9 and flashed[i, j] == False:
    #                 flashed[i, j] = True
    #                 increment_neighbours(data, i, j)
    # # print(data)
    # # print(flashed[np.where(data > 9)])
    # # print(np.all(flashed[np.where(data > 9)]))

    # data[flashed] = 0
    # print(data)
    # # for i in range(data.shape[0]):
    # #     for j in range(data.shape[1]):



