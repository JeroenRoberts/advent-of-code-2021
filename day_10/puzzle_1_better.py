matches = {}
matches['['] = ']'
matches['<'] = '>'
matches['{'] = '}'
matches['('] = ')'
#left symbol: start a chunk
#corresponding match: end a chunk
#only one chunk remaining: symbol must end this chunk
points = {')': 3, ']': 57, '}': 1197, '>': 25137}

def get_points_first_illegal_character(line):
    print(line)
    left_symbols_to_match = []
    # n_chunks = [0]
    for k, x in enumerate(line):
        if x in matches.keys():
            left_symbols_to_match.append({'position': k, 'value': x})
        if x in matches.values():
            most_recent_symbol = left_symbols_to_match[-1]
            y = most_recent_symbol['value']
            j = most_recent_symbol['position']
            if x == matches[y]:
                print(j, y, ' match found with ', k, x)
                left_symbols_to_match = left_symbols_to_match[:-1]
            else:
                print(j, y, 'does NOT match ', k, x)
                return points[x]
    return 0 #no illegal character found


if __name__ == "__main__":
    file = 'small_input.txt'
    with open(file, 'r') as f:
        lines = f.readlines()
    total_points = 0
    for line in lines:
        total_points += get_points_first_illegal_character(line.rstrip())
    print(f'{ total_points = }')



    # line = lines[2].rstrip()
    

    # print(n_chunks)

