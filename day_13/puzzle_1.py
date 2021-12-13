import numpy as np

def parse_folds(fold_line):
    folds = []
    for line in fold_line:
        k, v = (line.split(' ')[-1]).split('=')
        folds.append({'fold_axis': k, 'z': int(v)})
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
                # print(fold_axis + f' folding {coords[i,0]} about {z} into {z-distance}')
                coords[i, 0] = z - distance
        elif fold_axis == 'y':
            distance = coords[i, 1] - z
            if distance >= 0:
                # print(fold_axis + f' folding {coords[i,1]} about {z} into {z-distance}')
                coords[i, 1] = z - distance

def print_dots(dots):
    shape_x = max([dot[0] for dot in dots])
    shape_y = max([dot[1] for dot in dots])
    print(shape_x, shape_y)
    A = np.zeros((shape_x+1, shape_y+1), dtype=int)
    for s in dots:
        A[tuple(s)] = 1
    k=1
    print(f'{k} th letter')
    convert = lambda x: '#' if x else ' '
    letters = []
    letters.append([])
    for a in A:
        if not np.any(a): 
            letters.append([])
            k +=1
            print("\n\n")
            print(f'{k} th letter')
        else:
            b = ''.join([convert(x) for x in a])
            letters[k-1].append(b)
            print(b)
            # print(a)

    #join letters
    print('\n\n')
    for k,l in enumerate(letters[0]):
        line = ""
        for l in letters:
            line += str(l[k]) + '\t'
            # print(letters[0][k], '\t', letters[1][k])
        print(line)
        # print('\t\t\t'.join(letters[:][k]))
    
    # print('\n\n')
    # print(A.T)

if __name__ == "__main__":
    # file = 'small_input.txt'
    file = 'input.txt'
    coords, folds = parse_input(file)
    # print(coords)
    for fold in folds:
        print(fold)
        perform_fold(coords, **fold)
        dots = set([tuple(coord) for coord in coords])
        # print_dots(dots)
        print(len(dots))
        # dots = set([tuple(coord) for coord in coords])
        # print(dots)
    print_dots(dots)
    dots = set([tuple(coord) for coord in coords])
    print(len(dots))
        # break
