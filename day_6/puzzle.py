import numpy as np
def update(data):
    N_births = (data == 0).sum()

    #one day passed
    data = (data - 1)

    #reset
    data[data == -1] = 6

    #add new guys
    data = np.hstack([data, 8*np.ones(N_births)])
    return data


if __name__ == "__main__":
    # data = np.loadtxt('small_input.txt', delimiter=',', dtype=int)
    data = np.loadtxt('input.txt', delimiter=',', dtype=int)
    print(data)
    N_days = 256
    # N_days = 18
    for day in range(1, N_days+1):
        N_births = (data == 0).sum()

        #one day passed
        data = (data - 1)

        #reset
        data[data == -1] = 6

        #add new guys
        data = np.hstack([data, 8*np.ones(N_births)])
        # print(f'{day = } ,',data)

    answer = data.size
    print(f'{answer = }')

    
