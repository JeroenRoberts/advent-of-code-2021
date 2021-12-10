matches = {}
matches['['] = ']'
matches['<'] = '>'
matches['{'] = '}'
matches['('] = ')'
matches_reverse = {matches[k]: k for k in matches.keys()}
def find_matching_brace_reverse(position, symbol, line):
    match = matches_reverse[symbol]
    delay = 0 
    symbols_to_check = [x for x in line[:position-1]]
    symbols_to_check.reverse()
    for k, x in enumerate(symbols_to_check):
        if x == symbol:
            delay +=1
        if x == match:
            if delay == 0:
                return position-1-k, x
            else:
                delay -= 1
    return None


def find_matching_brace(position, symbol, line):
    match = matches[symbol]
    delay = 0 
    for k, x in enumerate(line[position+1:]):
        if x == symbol:
            delay +=1
        if x == match:
            if delay == 0:
                return position+1+k, x
            else:
                delay -= 1
    return None


if __name__ == "__main__": 
    file = 'small_input.txt'
    with open(file, 'r') as f:
        lines = f.readlines()

    line = lines[2].rstrip()

    print(line)
    positions_of_symbols_with_a_match = []
    for k, x in enumerate(line):
        if x in matches.keys(): #if it is a left brace
            match = find_matching_brace(k, x, line)
            if match != None: #a match was found
                j = match[0]
                y = match[1]
                print(k, x, " matches with ", j, y)
                positions_of_symbols_with_a_match.append(k)
                positions_of_symbols_with_a_match.append(j)
            else:
                print(k, x, " no match")
    print(positions_of_symbols_with_a_match)
    unmatched = [line[k] for k in range(len(line)) if k not in positions_of_symbols_with_a_match]
    print(line)
    print(unmatched)
    # for k, x in enumerate(line):
    #     if x in matches_reverse.keys(): #if it is a left brace
    #         match = find_matching_brace_reverse(k, x, line)
    #         if match != None: #a match was found
    #             j = match[0]
    #             y = match[1]
    #             print(k, x, " matches with ", j, y)
    #         else:
    #             print(k, x, " no match")
