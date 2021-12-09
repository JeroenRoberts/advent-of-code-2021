import sys
path = sys.path[0] + "/../.."
sys.path.insert(1, path)
from puzzle_1 import get_possible_digits_based_on_length
from puzzle_1 import get_unique_digit_based_on_length
from puzzle_1 import number_of_letters
from itertools import permutations

letters_used = {}
letters_used['0'] = ['a', 'b', 'c', 'e', 'f', 'g']
letters_used['1'] = ['c', 'f']
letters_used['2'] = ['a', 'c', 'd', 'e', 'g']
letters_used['3'] = ['a', 'c', 'd', 'f', 'g']
letters_used['4'] = ['b', 'c', 'd', 'f']
letters_used['5'] = ['a', 'b', 'd', 'f', 'g']
letters_used['6'] = ['a', 'b', 'd', 'e', 'f', 'g']
letters_used['7'] = ['a', 'c', 'f']
letters_used['8'] = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
letters_used['9'] = ['a', 'b', 'c', 'd', 'f', 'g']

free_letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g']

def check_if_correct_symbols(letters_used, number_of_letters):
    for digit, v in letters_used.items():
        assert len(v) == number_of_letters[digit], f"wrong: {digit}, {len(v)} neq {number_of_letters[digit]}"


def parse_file(file):
    with open(file, 'r') as f:
        for line in f.readlines():
            signal_patterns, output = [x.split(' ') for x in line.rstrip().split(' | ')]
    return signal_patterns, output

dictionary = {}
dictionary['a'] = 'a'
dictionary['b'] = 'b'
dictionary['c'] = 'c'
dictionary['d'] = 'd'
dictionary['e'] = 'e'
dictionary['f'] = 'f'
dictionary['g'] = 'g'

def swap_two_rules(dictionary, first, second):
    temp = dictionary[first]
    dictionary[first] = dictionary[second]
    dictionary[second] = temp
    return

def print_possible_digits_with_length(length):
    s, out = parse_file(file)
    a = get_possible_digits_based_on_length(number_of_letters)
    print(f'words with {length} letters that could mean: ', a[length])
    words = []
    print(f'length: {length} {a[length]}' )
    for word in s:
        if len(word) == length:
            words.append(word)
    print(words)
    print('\n')
    return words

def find_symbols_missing(list_of_words):
    possible_letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
    for word in words:
        for letter in possible_letters:
            if letter in word:
                possible_letters.remove(letter)
    # print(possible_letters)
    return possible_letters

def parse(word):
    symbols = [x for x in word]
    return symbols
    
def find_letters_that_form_5(words_length_5, words_length_6):
    for word in words_length_5:
        for word_2 in words_length_6:
            # print(word, word_2)
            if all(d in parse(word_2) for d in parse(word)):
                print("inside", word, word_2)

if __name__ == "__main__":
    file = 'smaller_input.txt'
    # print(s)
    possible_words = {}
    for i in range(10):
        possible_words[str(i)] = print_possible_digits_with_length(i)
    # words_length_6 = print_possible_digits_with_length(6)
    find_letters_that_form_5(possible_words['5'], possible_words['6'])
    # check_if_correct_symbols(letters_used, number_of_letters)
    # print(number_of_letters)
    # print(a)

