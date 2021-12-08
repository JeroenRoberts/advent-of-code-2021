#STRATEGY:
# find 1, 4, 7, 8
#FIND 2, 5, 3:
    # 5 has 4 letters in common with 3, while only 3 letters in common with 2
    # Distuinguish words for 2 and 5:
        # 5 has 3 letters in common with 4 (which is known), while 2 only has 2
    # the remaining word with length 5 is 3

#FIND 0, 6, 9:?TODO
letters_used = {}
letters_used[0] = ['a', 'b', 'c', 'e', 'f', 'g']
letters_used[1] = ['c', 'f']
letters_used[2] = ['a', 'c', 'd', 'e', 'g']
letters_used[3] = ['a', 'c', 'd', 'f', 'g']
letters_used[4] = ['b', 'c', 'd', 'f']
letters_used[5] = ['a', 'b', 'd', 'f', 'g']
letters_used[6] = ['a', 'b', 'd', 'e', 'f', 'g']
letters_used[7] = ['a', 'c', 'f']
letters_used[8] = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
letters_used[9] = ['a', 'b', 'c', 'd', 'f', 'g']


def parse_line(line):
    signal_patterns, output = [x.split(' ') for x in line.rstrip().split(' | ')]
    return signal_patterns, output


def parse(word):
    symbols = [x for x in word]
    return symbols

def calculate_lengths_of_digits():
    lengths_of_digits = {}
    for d in range(0, 10):
        length = len(letters_used[d])
        if length not in lengths_of_digits.keys():
            lengths_of_digits[length] = []
        lengths_of_digits[length].append(d)
    return lengths_of_digits

def find_words_unique_length(words):
    lengths_of_digits = calculate_lengths_of_digits()
    lengths_with_unique_digit = {}
    
    for length, digits in lengths_of_digits.items():
        if(len(digits)) == 1: #unique digit
            lengths_with_unique_digit[length] = digits[0]

    for word in words:
        if len(word) in lengths_with_unique_digit.keys():
            digit = lengths_with_unique_digit[len(word)]
            interpreted_words[digit] = parse(word)
    return interpreted_words

def get_words_of_length_5(words):
    return [w for w in words if len(w) == 5]

def count_intersection_of_pairs(list_1, list_2):
    print(list_1, list_2)
    return(len([x for x in list_1 if x in list_2]) )

def find_2_5_3(words):
    lengths_of_digits = calculate_lengths_of_digits()
    words_of_length_5 = get_words_of_length_5(words)
    for word in words_of_length_5:
        for word_2 in words_of_length_5:
            if word != word_2:
                if count_intersection_of_pairs(parse(word), parse(word_2)) == 3:
                    two_or_five = word
                    two_or_five_ = word_2
                    words_of_length_5.remove(word)
                    words_of_length_5.remove(word_2)
                    three = words_of_length_5[0]
                    return parse(two_or_five), parse(two_or_five_), parse(three)

def distuinguish_two_and_five(interpreted_words, two_or_five, two_or_five_):
    for x in [two_or_five, two_or_five_]:
        if count_intersection_of_pairs(x, interpreted_words[4]) == 3:# 5 and 4 have 3 letters in common
            interpreted_words[5] = x
        else:
            assert count_intersection_of_pairs(x, interpreted_words[4]) == 2, "something went wrong here" # 2 and 4 have 2 letters in common

            interpreted_words[2] = x

def check_if_dictionary_is_consistent(interpreted_words):
    for digit, word in interpreted_words.items():
        assert len(word) == len(letters_used[digit]), f"digit {digit} has word with wrong amount of letters"
    for word in interpreted_words.values():
        assert len(set(word)) == len(word), f"errors: duplicate letters: {word}"

# def sum_output(interpreted_words):
def translate_word(dictionary, word):
    symbols = parse(word)
    translated_symbols=[]
    for s in symbols:
        translated = dictionary[s]
        translated_symbols.append(translated)
    assert len(symbols) == len(translated_symbols), "error"
    return translated_symbols

def find_digit_based_on_translated_symbols(symbols, interpreted_words):
    for i in range(10):
        x = set(symbols) 
        y =set(interpreted_words[i])
        # print(f'{x=}')
        # print(f'{y=}')
        if x == y:
            return i
    print("\n\nno digit found for:\n")
    print(symbols)

if __name__ == "__main__":

    file = 'input.txt'
    sum = 0

    with open(file, 'r') as f:
        for line in f.readlines():
            words, out = parse_line(line)

            interpreted_words = {}
            interpreted_words = find_words_unique_length(words)
            print(interpreted_words)
            two_or_five, two_or_five_, interpreted_words[3] = find_2_5_3(words)
            distuinguish_two_and_five(interpreted_words, two_or_five, two_or_five_)
            dictionary = {}
            dictionary['f'] = [x for x in interpreted_words[5] if x in interpreted_words[1]][0]
            dictionary['c'] = [x for x in interpreted_words[2] if x in interpreted_words[1]][0]
            dictionary['a'] = [x for x in interpreted_words[7] if x not in interpreted_words[1]][0]

            dictionary['d'] = [x for x in interpreted_words[4] if x not in interpreted_words[1] and x in interpreted_words[2]][0]
            dictionary['b'] = [x for x in interpreted_words[4] if x not in interpreted_words[2] + interpreted_words[3]][0]
            dictionary['e'] = [x for x in interpreted_words[2] if x not in interpreted_words[3]][0]
            all_letters= ['a', 'b', 'c', 'd', 'e', 'f', 'g']
            dictionary['g'] = [x for x in all_letters if x not in list(dictionary.values())][0]
            print(f'{dictionary = }')

            for i in [0, 6, 9]:
                interpreted_words[i] = [dictionary[letter] for letter in letters_used[i]]
            # print(interpreted_words)
            check_if_dictionary_is_consistent(interpreted_words)

            digits = []
            for word in out:
                # translated = translate_word(dictionary, word)
                d = find_digit_based_on_translated_symbols(parse(word), interpreted_words)
                digits.append(str(d))
            print(digits)
            number = int(''.join(digits))
            sum += number
    answer = sum
    print(f'{answer = }')
