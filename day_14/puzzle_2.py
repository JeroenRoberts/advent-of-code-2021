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

def calculate_N_pairs(polymer):
    pairs = zip(polymer[:-1], polymer[1:])
    counts = Counter(pairs)
    return dict(counts)

def perform_inserts(N_pairs, rules):
    new_N_pairs = N_pairs.copy()
    for k, N in N_pairs.items():
        if k in rules.keys():
            if N >= 1:
                inserted_letter = rules[k]
                new_pair_1 = (k[0], inserted_letter)
                new_pair_2 = (inserted_letter, k[1])
                for new_pair in [new_pair_1, new_pair_2]:
                    if new_pair not in new_N_pairs.keys():
                        new_N_pairs[new_pair] = 0
                    new_N_pairs[new_pair] += N


            new_N_pairs[k] -= N
    # print(new_N_pairs)
    # print(new_N_pairs)
    N_pairs.update(new_N_pairs)
    for k, N in N_pairs.items():
        assert(N >= 0)

def print_occurences(N_pairs):
    counts = {}
    for pair, count in N_pairs.items():
        for letter in pair:
            if letter not in counts:
                counts[letter] = 0
            counts[letter] += count

    boundary_letters = ['N', 'B']
    for l in boundary_letters:
        counts[l] += 1

    for k in counts.keys():
        assert(counts[k] % 2 == 0)
        counts[k] = counts[k]//2

    print(counts)
    length = sum(counts.values())
    print(f'{length=}')
    maximum = max(counts.values())
    minimum = min(counts.values())
    return maximum - minimum



if __name__ == "__main__":
    # file = 'input.txt'
    file = 'small_input.txt'
    polymer_template, rules = read_file(file)
    polymer=polymer_template
    N_pairs = calculate_N_pairs(polymer)
    for step in range(10):
        # print(step, ''.join(polymer))
        perform_inserts(N_pairs, rules)
        print(f'step={step+1}')
        print_occurences(N_pairs)
        print(f'\n')
        # print(N_pairs)
    # print(f'{answer = }')
    # print(4, ''.join(polymer))
