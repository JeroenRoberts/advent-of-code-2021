import numpy as np
def total_fuel(v, position):
    return np.sum(np.abs(v - position))

if __name__ == "__main__":
    # sample_input = np.array([5, 5, 1, 3, 1], dtype=int)
    # sample_input = np.loadtxt('small_input.txt', dtype=int, delimiter=',')
    sample_input = np.loadtxt('input.txt', dtype=int, delimiter=',')
    min = np.min(sample_input)
    max = np.max(sample_input)
    # print(sample_input.mean())
    sorted = np.sort(sample_input)
    median = sorted[sorted.size//2]
    print(median)
    N_median_occurence = (sorted == median).sum()
    print(N_median_occurence)

    first_guess = median
    N_guesses = 20
    min = 1239084901241
    min_index = 0
    for i in range(median - N_guesses, median + N_guesses):
        fuel = total_fuel(sorted, i)
        print(i, fuel)
        if fuel < min:
            min = fuel
            min_index = i
    print("MINIMUM ", min_index, min)

    # cost_first_half = total_fuel(sorted[:sorted.size//2], first_guess)
    # cost_second_half = total_fuel(sorted[sorted.size//2:], first_guess)
    # print(cost_first_half)
    # print(cost_second_half)

    # for i in range(min, max):
    #     print(i, total_fuel(sample_input, i))
