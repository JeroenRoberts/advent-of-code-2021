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



if __name__ == "__main__":
    # file = 'input.txt'
    file = 'small_input.txt'
    polymer_template, rules = read_file(file)
    # print(polymer_template)
    # print(rules)
    polymer=polymer_template
    for step in range(4):
        print(step, ''.join(polymer))
        perform_inserts(polymer, rules)
    print(4, ''.join(polymer))
