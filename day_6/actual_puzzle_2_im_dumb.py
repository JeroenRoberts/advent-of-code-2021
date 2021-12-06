import numpy as np

max_days = 9

def update(total_fish_per_day_remaining):
    # for i in range(max_days):
    N_births = total_fish_per_day_remaining[0]
    total_fish_per_day_remaining = np.roll(total_fish_per_day_remaining, -1)
    total_fish_per_day_remaining[6] += total_fish_per_day_remaining[8]
    total_fish_per_day_remaining[8] = N_births
    return total_fish_per_day_remaining

if __name__ == "__main__":
    # data = np.loadtxt('input.txt', delimiter=',', dtype=int)
    data = np.loadtxt('input.txt', delimiter=',', dtype=int)
    total_fish_per_day_remaining = np.zeros(max_days, dtype=int)
    for i in range(max_days):
        total_fish_per_day_remaining[i] = (data == i).sum()

    N_days = 256
    for day in range(1, N_days+1):
        total_fish_per_day_remaining = update(total_fish_per_day_remaining)
        print(total_fish_per_day_remaining)
        print(total_fish_per_day_remaining.sum())

