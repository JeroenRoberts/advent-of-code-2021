import sys
path = sys.path[0] + "/.."
sys.path.insert(1, path)
from day_6.puzzle import update
import numpy as np
def load_current_state():
    data = np.load('current.npy')

    with open('current_day.txt', 'r') as f:
        lines = f.readlines()
        day = int(lines[0].rstrip())

    return data, day

def write_current_state(data, day):
    np.save('current.npy', data)

    with open('current_day.txt', 'w') as f:
       f.write(str(day))

def load_initial_state():
    data = np.loadtxt('input.txt', delimiter=',', dtype=int)
    day = 0
    return data, day

if __name__ == "__main__":
    N_days = 50
    # data, day = load_initial_state()
    data, day = load_current_state()
    N_days = day + N_days
    while day < N_days:
        data = update(data)
        day += 1
        print(day)
    write_current_state(data, day)
        

    
    
