import numpy as np

def find_intermediate_points(int_1, int_2):
    int_1 = int(int_1)
    int_2 = int(int_2)
    mininum = min(int_1, int_2)
    maximum = max(int_1, int_2)
    return list(range(mininum, maximum+1))

def get_line(start_coord, end_coord):
    if start_coord[0] == end_coord[0]: #line is vertical
        intermediate = find_intermediate_points(start_coord[1], end_coord[1])
        return 'vertical', [(start_coord[0], y) for y in intermediate]
    elif start_coord[1] == end_coord[1]: #line is horizontal
        intermediate = find_intermediate_points(start_coord[0], end_coord[0])
        return 'horizontal', [(x, start_coord[1]) for x in intermediate]
    else: # f'Line from {start_coord=} to {end_coord=} is neither vertical nor horizontal'
        return 'diagonal', [] #TODO


def read_lines(file):
    # read input file.
    start_coords = []
    end_coords = []
    max = 0
    with open(file, 'r') as f:
        for file_line in f.readlines():
            start_coord, end_coord = [np.array(coords.split(','), dtype=int) for coords in file_line.rstrip().split(' -> ')]
            start_coords.append(start_coord)
            end_coords.append(end_coord)
            for number in start_coords + end_coords:
                if int(number[0]) > max:
                    max = int(number[0])
                if int(number[1]) > max:
                    max = int(number[1])

    lines = {'horizontal': [], 'vertical': [], 'diagonal': []}
    for start_coord, end_coord in zip(start_coords, end_coords):
        type_of_line, line = get_line(start_coord, end_coord)
        lines[type_of_line].append(line)
    return lines, max+1

def count_number_of_overlaps(lines, grid_size):
    grid = np.zeros((grid_size, grid_size))
    # print(grid)
    types_of_line = ['horizontal', 'vertical']
    for type_of_line in types_of_line:
        for line in lines[type_of_line]:
            for coord in line:
                # print(coord)
                grid[coord] += 1
    return grid


if __name__ == "__main__":
    # file = 'small_input.txt'
    file = 'input.txt'
    lines, grid_size = read_lines(file)
    grid = count_number_of_overlaps(lines, grid_size)
    answer = (grid >= 2).sum()
    print(grid.T)
    print(f'{answer = }')


