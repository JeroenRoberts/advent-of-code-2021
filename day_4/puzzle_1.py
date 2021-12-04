import numpy as np

def load_numbers_to_draw(file):
    numbers = np.loadtxt(file, max_rows=1, delimiter=',', dtype=int)
    return numbers
def load_boards(file):
    # boards = np.loadtxt(file, skiprows=1, delimiter=' ')
    bingo_board_size = 5
    tables = []
    with open(file, 'r') as f:
        lines = [line.rstrip() for line in f.readlines()[1:]]
        table_starts = []
        for k, line in enumerate(lines):
            if line == "":
                table_starts.append(k)

        for k in table_starts:
            table = lines[k:k+bingo_board_size+1]
            table = np.loadtxt(table, dtype=int)
            assert table.shape == (bingo_board_size, bingo_board_size), " Table has incorrect shape"
            tables.append(table)

    return tables

def load_score_card(boards):
    N = len(boards)
    score_cards = []
    for board in boards:
        score_card = np.zeros(board.shape, dtype=bool)
        score_cards.append(score_card)
    return score_cards

def check_if_row_filled(score_card):
    for k in range(score_card.shape[0]):
        row = score_card[k, :] 
        if np.all(row == True):
            return True, k
    return False, None

def check_if_column_filled(score_card):
    for k in range(score_card.shape[1]):
        column = score_card[:, k] 
        if np.all(column == True):
            return True, k
    return False, None

def check_for_bingo(score_card):
    check_column, column = check_if_column_filled(score_card)
    check_row, row = check_if_row_filled(score_card)
    if check_column:
        return check_column, 'column', column
    if check_row:
        return check_row, 'row', row
    return False, None, None

def print_row_or_col(matrix, row_or_col, index):
    if row_or_col == 'row':
        print(matrix[index, :])
    elif row_or_col == 'column':
        print(matrix[:, index].T)

def do_draws(draws, boards, score_cards):
    for draw in draws:
        for board, score_card in zip(boards, score_cards):
            if draw in board:
                location = np.where(board == draw)
                score_card[location] = True

            check, row_or_col, location = check_for_bingo(score_card)
            if check == True:
                print(score_card)
                print(board)
                print_row_or_col(score_card, row_or_col, location)
                print_row_or_col(board, row_or_col, location)
                print("winner after drawing: ", draw)
                return draw, board, score_card, draws, boards, score_cards
    # print(score_cards[-1])
    assert False, "No winner!"

def sum_unmarked_numbers(board, score_card):
    unmarked = board[np.invert(score_card)]
    # print(f'{unmarked=}')
    return np.sum(unmarked)

if __name__ == "__main__":
    file = 'input.txt'
    draws = load_numbers_to_draw(file)
    print(draws)
    load_boards(file)
    boards = load_boards(file)
    # for board in boards:
    #     print(board.shape)
    draw, board, score_card = do_draws(draws, boards)
    sum = sum_unmarked_numbers(board, score_card)
    print(draw, sum)
    answer = int(sum * draw)
    print(f'{answer = }')
