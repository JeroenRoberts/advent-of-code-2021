import numpy as np

def parse_folds(fold_line):
    folds = {}
    for line in fold_line:
        k, v = (line.split(' ')[-1]).split('=')
        folds[k] = v
    return folds

def parse_input(file):
    coords = []
    with open(file, 'r') as f:
        lines = [line.rstrip() for line in f.readlines()]
        for k, line in enumerate(lines):
            if line == "":
                coord_lines = lines[:k]
                fold_lines = lines[k+1:]
                break
    coords = np.loadtxt(coord_lines, delimiter=',', dtype=int)
    folds = parse_folds(fold_lines)
    return coords, folds

def perform_fold(coords, fold_axis, z):
    for i in range(coords.shape[0]):
        if fold_axis == 'x':
            distance = coords[i, 0] - z
            if distance >= 0:
                print(f'folding {coords[i,0]} about {z} into {z-distance}')
                coords[i, 0] = z - distance

if __name__ == "__main__":
    file = 'small_input.txt'
    coords, folds = parse_input(file)
    print(coords)
    for fold in folds.item():
        perform_fold(coords, 'x', 5)
        print(coords)
