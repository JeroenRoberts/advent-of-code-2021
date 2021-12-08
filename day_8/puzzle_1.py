import pprint
number_of_letters = {}
number_of_letters['0'] = 6
number_of_letters['1'] = 2 #Unique
number_of_letters['2'] = 5
number_of_letters['3'] = 5
number_of_letters['4'] = 4 #Unique   
number_of_letters['5'] = 5
number_of_letters['6'] = 6
number_of_letters['7'] = 3 #Unique
number_of_letters['8'] = 7 #Unique
number_of_letters['9'] = 6

possible_digits_based_on_length = {}

def get_possible_digits_based_on_length(number_of_letters):
    for k, v in number_of_letters.items():
        if v not in possible_digits_based_on_length:
            possible_digits_based_on_length[v] = []
        possible_digits_based_on_length[v].append(k)

unique_digit_based_on_length = {}
def get_unique_digit_based_on_length(possible_digits_based_on_length):
    for k, v in possible_digits_based_on_length.items():
        if len(v) == 1:
            unique_digit_based_on_length[k] = int(v[0])

if __name__ == "__main__":
    file = 'small_input.txt'
    # file = 'input.txt'
    get_possible_digits_based_on_length(number_of_letters)
    get_unique_digit_based_on_length(possible_digits_based_on_length)
    print(possible_digits_based_on_length)
    print(unique_digit_based_on_length)

    
    counts = {}
    for i in range(10):
        counts[i] = 0
    with open(file, 'r') as f:
        for line in f.readlines():
            signal_patterns, output = [x.split(' ') for x in line.rstrip().split(' | ')]
            #ten UNIQUE signal patterns
            #four digit output
            for word in output:
                digit = unique_digit_based_on_length.get(len(word), None) 
                if digit != None:
                    counts[digit] += 1

    total = sum(counts.values())
    print(f'{total = }')

    pprint.pprint(counts)


