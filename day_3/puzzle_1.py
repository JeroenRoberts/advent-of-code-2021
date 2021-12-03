import numpy as np
from matplotlib import pyplot as plt
from scipy.optimize import curve_fit


def most_common_argument(array):
    counts = np.bincount(array)
    return counts.argmax()

def least_common_argument(array):
    counts = np.bincount(array)
    return counts.argmin()
def convert_binary_array_to_int(array):
    return array.dot(2**np.arange(array.size)[::-1])

if __name__ == "__main__":
    # file = "small_input.txt"
    file = "input.txt"
    data = np.genfromtxt(file, delimiter=1, dtype=int)
    gamma = np.zeros(data.shape[1], dtype=int)
    epsilon = np.zeros(data.shape[1], dtype=int)
    for k in range(data.shape[1]):
        column = data[:, k]
        gamma[k] = most_common_argument(column)
        epsilon[k] = least_common_argument(column)

    print(gamma)
    print(convert_binary_array_to_int(gamma))
    print(epsilon)
    print(convert_binary_array_to_int(epsilon))
    print(convert_binary_array_to_int(epsilon) * convert_binary_array_to_int(gamma))
    # print(first_column)

    # print(data)

