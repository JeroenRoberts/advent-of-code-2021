from collections import Counter
def read_file(file):
    with open(file, 'r') as f:
        lines = [line.rstrip() for line in f.readlines()]
        polymer_template = list(lines[0])
        rules = {}
        for line in lines[2:]:
            pair, insert = line.split(' -> ')
            rules[tuple(pair)] = insert
    return polymer_template, rules

def perform_inserts(polymer, rules):
    pairs = zip(polymer[:-1], polymer[1:])
    n_inserts = 0
    for k, p in enumerate(pairs):
        if p in rules.keys():
            polymer.insert(k+ n_inserts + 1, rules[p])
            n_inserts += 1

def print_occurences(polymer):
    print(f'{len(polymer)}')
    counts = Counter(polymer)
    print(counts)
    maximum = max(counts.values())
    minimum = min(counts.values())
    return maximum - minimum



if __name__ == "__main__":
    file = 'input.txt'
    # file = 'small_input.txt'
    polymer_template, rules = read_file(file)
    polymer=polymer_template
    for step in range(10):
        # print(step, ''.join(polymer))
        print(f'{step+1 =}')
        perform_inserts(polymer, rules)
        answer = print_occurences(polymer)
    print(f'{answer = }')
    # print(4, ''.join(polymer))
