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
from puzzle_1 import get_possible_digits_based_on_length

# 2 and 5 have 3 letters in common: 'a', 'd', 'g'
# 3 and 5 have 4 letters in common: 'a', 'd', 'f', 'g'
# 2 and 3 have 4 letters in common: 'a', 'c', 'd', 'g'

if __name__ == "__main__":
    a = get_possible_digits_based_on_length()
    for word_length in range(2, 7):
        print(f'Digits with letter_length {word_length}: ', a[word_length])
        for digit in a[word_length]:
            for digit_2 in a[word_length]:
                if digit != digit_2:
                    intersection = [letter for letter in letters_used[digit] if letter in letters_used[digit_2]]
                    print(digit, digit_2, intersection)

