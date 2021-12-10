matches = {}
matches['['] = ']'
matches['<'] = '>'
matches['{'] = '}'
matches['('] = ')'
#left symbol: start a chunk
#corresponding match: end a chunk
#only one chunk remaining: symbol must end this chunk
points = {')': 1, ']': 2, '}': 3, '>': 4}

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
                # print(j, y, ' match found with ', k, x)
                left_symbols_to_match = left_symbols_to_match[:-1]
            else:
                # print(j, y, 'does NOT match ', k, x)
                return None#illegal line
    #if we get here the line is not illegal
    symbols = [x['value'] for x in left_symbols_to_match]
    symbols.reverse()
    symbols_to_add = [matches[x] for x in symbols]
    
    # print('add:', ''.join(symbols_to_add))
    return symbols_to_add
    # return 0 #no illegal character found


if __name__ == "__main__":
    file = 'small_input.txt'
    # file = 'input.txt'
    with open(file, 'r') as f:
        lines = f.readlines()
    total_points = 0
    for line in lines:
        symbols_to_add = get_points_first_illegal_character(line.rstrip())
        line_points = 0
        if symbols_to_add != None: #line is not corrupt
            for x in symbols_to_add:
                line_points *= 5
                line_points += points[x]
        print(f' {line_points = }')
    print(f'{ total_points = }')



    # line = lines[2].rstrip()
    

    # print(n_chunks)

