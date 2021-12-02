import numpy as np
from matplotlib import pyplot as plt
from scipy.optimize import curve_fit

if __name__ == "__main__":
    data = np.loadtxt("puzzle_1_input.txt")
    difference_from_previous = np.diff(data)
    N_increasing = np.sum(difference_from_previous > 0)
    print(N_increasing)
