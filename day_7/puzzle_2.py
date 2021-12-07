import numpy as np
def total_fuel_new(v, position):
    distance = np.abs(v - position)
    fuel = np.array([np.sum(range(d+1)) for d in distance])
    return np.sum(fuel)

if __name__ == "__main__":
    # sample_input = np.array([5, 5, 1, 3, 1], dtype=int)
    # sample_input = np.loadtxt('small_input.txt', dtype=int, delimiter=',')
    sample_input = np.loadtxt('input.txt', dtype=int, delimiter=',')
    min = np.min(sample_input)
    max = np.max(sample_input)
    # print(sample_input.mean())
    sorted = np.sort(sample_input)
    median = sorted[sorted.size//2]
    print(f'{median =}')
    N_median_occurence = (sorted == median).sum()

    first_guess = median
    N_guesses = 300
    min = 1239084901241
    min_index = 0
    for i in range(median - N_guesses, median + N_guesses):
        fuel = total_fuel_new(sorted, i)
        print(i, fuel)
        if fuel < min:
            min = fuel
            min_index = i
    print("MINIMUM ", min_index, min)

