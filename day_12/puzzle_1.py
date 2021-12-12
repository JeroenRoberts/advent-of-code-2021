def read_file(file):
    with open(file, 'r') as f:
        lines = f.readlines()
    return [line.rstrip() for line in lines]

# a path is a concatonation of connections.
# such that lower case letters(caves) are only in once
# such that each new connection start at the current location
# if you have A-B, can you just visit A, B infinitely often? Yes, luckily this is not in the input...
def caves_visited(path):
    return {i for sub in path for i in sub}


def find_good_connections(small_caves_visited, connections, current_location):
    good_connections = []
    for c in connections:
        if c[0] == current_location:
            if c[1] not in small_caves_visited:
                good_connections.append(c)
    return good_connections

def print_paths(paths):
    for path in paths:
        print(path)
    print('\n')

reverse = lambda tuple: (tuple[1], tuple[0])
if __name__ == "__main__":
    # file = 'tiny_input.txt'
    # file = 'slightly_larger_example.txt'
    # file = 'even_larger_example.txt'
    file = 'input.txt'

    lines =  read_file(file)
    forward_connections = {tuple(line.split('-')) for line in lines}
    reverse_connections = {reverse(c) for c in forward_connections}
    connections = set.union(forward_connections, reverse_connections)
    starting_connections = [c for c in connections if c[0] == 'start']
    paths = []
    for start in starting_connections:
        path = [start]
        paths.append(path)

    step = 0
    print(f'{step = }')
    print_paths(paths)
    finished_paths = []
    max_steps = 1000
    for i in range(max_steps):
        new_paths = []
        for path in paths:
            current_location = path[-1][-1]
            visited = caves_visited(path)
            small_caves_visited = {v for v in visited if v.islower()}
            if current_location == 'end':
                finished_paths.append(path)

            good_connections = find_good_connections(small_caves_visited, connections, current_location)

            for c in good_connections:
                new_paths.append(path + [c])

        paths = new_paths
        step += 1
        print(f'{step = }')
        print_paths(paths)

    print_paths(finished_paths)
    print(f'{len(finished_paths) = }')



