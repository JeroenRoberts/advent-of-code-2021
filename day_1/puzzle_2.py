import numpy as np
from matplotlib import pyplot as plt
from scipy.optimize import curve_fit

if __name__ == "__main__":
    data = np.loadtxt("puzzle_1_input.txt")
    print(data[0:10])
    weighted_sum_data = np.convolve(data, np.ones(3))
    print(weighted_sum_data[2:10])
    print(weighted_sum_data[-10:-2])
    difference_from_previous = np.diff(weighted_sum_data[2:-2])
    N_increasing = np.sum(difference_from_previous > 0)
    print(N_increasing)
