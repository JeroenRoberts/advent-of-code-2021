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

def find(data, max_or_min, number_to_keep_if_equal, column_):
    column = data[:, column_]
    counts, equal = calculate_counts(column)
    keep = max_or_min(counts)
    if equal == True:
        keep = number_to_keep_if_equal

    filter = [column[j] == keep for j in range(data.shape[0])]
    data = data[filter]
    return data





if __name__ == "__main__":
    file = "small_input.txt"
    # file = "input.txt"
    data = np.genfromtxt(file, delimiter=1, dtype=int)
    data_oxygen = data.copy()
    data_co2 = data.copy()
    gamma = np.zeros(data.shape[1], dtype=int)
    epsilon = np.zeros(data.shape[1], dtype=int)
    column = 0
    for column in range(data.shape[1]):
        data_oxygen = find(data_oxygen, lambda c: c.argmax(), 1, column)
        if data_oxygen.shape[0] == 1: #one number left
            break
        # print(data_oxygen)
    oxygen = data_oxygen[0, :]

    print(data_co2)
    column = 0
    for column in range(data.shape[1]):
        data_co2 = find(data_co2, lambda c: c.argmin(), 0, column)
        if data_co2.shape[0] == 1: #one number left
            break
        # print(data_co2)
    co2 = data_co2[0, :]

    print(oxygen)
    print(co2)


    # for k in range(data.shape[1]):
    #     # print(f'{k=}')
    #     data_oxygen = find(data_oxygen, lambda c: c.argmax(), 1)
    #     data_co2 = find(data_co2, lambda c: c.argmin(), 0)
        # print(data_oxygen)
        # print(data_co2)
        # column = data[:, k]
        # counts, equal = calculate_counts(column)
        # gamma[k] = counts.argmax()
        # epsilon[k] = counts.argmin()
        # keep_oxygen = gamma[k]
        # keep_co2 = epsilon[k]
        # if equal == True:
        #     keep_oxygen = 1
        #     keep_co2 = 0

        # filter_oxygen = [column[j] == keep_oxygen for j in range(data_oxygen.shape[0])]
        # filter_co2  = [column[j] == keep_co2 for j in range(data_co2.shape[0])]
        # # print(bool(gamma[k]))
        # data_oxygen = data_oxygen[filter_oxygen]
        # data_co2 =  data_co2[filter_co2]
        # print(data.shape)
        # print(f'{data_oxygen.shape=}')
        # print(new_data)
        # break

    # print(gamma)
    # print(convert_binary_array_to_int(gamma))
    # print(epsilon)
    # print(convert_binary_array_to_int(epsilon))
    # print(convert_binary_array_to_int(epsilon) * convert_binary_array_to_int(gamma))
    # print(first_column)

    # print(data)

