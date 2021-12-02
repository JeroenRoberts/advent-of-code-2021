import numpy as np
from matplotlib import pyplot as plt
from scipy.optimize import curve_fit
import pandas as pd

if __name__ == "__main__":
    data = pd.read_table('input.txt', header=None, delimiter=" ")

    instructions = data[0]
    movements = set(instructions)
    totals = {}
    for move in movements:
        moves = data.loc[instructions == move]
        total = moves[1].sum(axis=0)
        totals[move] = total

    forward = totals['forward']
    depth = totals['down'] - totals['up']
    print(forward)
    print(depth)
    print(depth * forward)
