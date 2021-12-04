import numpy as np
import sys
path = sys.path[0] + "/.."
sys.path.insert(1, path)
from day_4.puzzle_1 import load_numbers_to_draw
from day_4.puzzle_1 import load_boards
from day_4.puzzle_1 import sum_unmarked_numbers
from day_4.puzzle_1 import do_draws
from day_4.puzzle_1 import load_score_card


def remove_array_from_list(L,arr):
    #this is ugly : https://stackoverflow.com/questions/3157374/how-do-you-remove-a-numpy-array-from-a-list-of-numpy-arrays
    ind = 0
    size = len(L)
    while ind != size and not np.array_equal(L[ind],arr):
        ind += 1
    if ind != size:
        L.pop(ind)
    else:
        raise ValueError('array not found in list.')

if __name__ == "__main__":
    file = 'input.txt'
    draws = load_numbers_to_draw(file)
    boards = load_boards(file)
    score_cards = load_score_card(boards)
    while boards != []:
        draw, board, score_card, draws, boards, score_cards = do_draws(draws, boards, score_cards)
        # print(boards)
        remove_array_from_list(boards, board)
        remove_array_from_list(score_cards, score_card)
        # boards.pop(boards.index(board))
        # score_cards.pop(score_cards.index(score_card))

    sum = sum_unmarked_numbers(board, score_card)
    print(draw, sum)
    answer = int(sum * draw)
    print(f'{answer = }')
