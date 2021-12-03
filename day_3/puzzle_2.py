import numpy as np
from matplotlib import pyplot as plt
from scipy.optimize import curve_fit

def calculate_counts(array):
    counts = np.bincount(array, minlength=2)
    equal = False
    if counts[0] == counts[1]:
        equal = True
    return counts, equal


def convert_binary_array_to_int(array):
    return array.dot(2**np.arange(array.size)[::-1])

def find(data, max_or_min, number_to_keep_if_equal):
    for k in range(data.shape[1]):
        if data.shape[0] == 1: #only one word remaining
            return data
        column = data[:, k]
        counts, equal = calculate_counts(column)
        keep = max_or_min(counts)
        if equal == True:
            keep = number_to_keep_if_equal

        filter = [column[j] == keep for j in range(data.shape[0])]
        data = data[filter]

    return data





if __name__ == "__main__":
    # file = "small_input.txt"
    file = "input.txt"
    data = np.genfromtxt(file, delimiter=1, dtype=int)
    data_oxygen = data.copy()
    data_co2 = data.copy()
    gamma = np.zeros(data.shape[1], dtype=int)
    epsilon = np.zeros(data.shape[1], dtype=int)
    oxygen = find(data_oxygen, lambda c: c.argmax(), 1)
    co2 = find(data_co2, lambda c: c.argmin(), 0)

    print(oxygen)
    print(co2)
    print(convert_binary_array_to_int(oxygen) * convert_binary_array_to_int(co2))
