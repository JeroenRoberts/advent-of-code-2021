import numpy as np
from matplotlib import pyplot as plt
from scipy.optimize import curve_fit
import pandas as pd

if __name__ == "__main__":
    data = pd.read_table('input.txt', names=["instruction", "value"], delimiter=" ")

    instructions = data.loc[:, 'instruction']
    movements = set(instructions)
    m = {}

    for move in movements:
        filter = instructions == move
        moves = data.loc[instructions == move]

        df = pd.DataFrame(np.zeros(len(instructions)), columns=["value"])
        df.update(moves)
        m[move] = df

    horizontal = m['forward']
    delta_aim = m['down'] - m['up']
    aim = delta_aim.cumsum(axis=0)
    delta_depth = aim.multiply(horizontal)
    depth = delta_depth.sum(axis=0)

    final_horizontal_position = horizontal.sum(axis=0)
    final_depth = depth.iloc[-1]
    print(final_horizontal_position)
    print(final_depth)
    answer = final_horizontal_position * final_depth
    print(f'{answer.value=}')
