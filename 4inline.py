import numpy as np

ROWS = 6
COLUMNS = 7


def create_board():
    return np.zeros((ROWS, COLUMNS))

def drop_piece(board, row, col, piece):
    board[row][col] = piece

def is_valid_location(board, col):
    return board[0][col] == 0

def get_next_free_row(board, col):
    for r in reversed(range(board.shape[0])):
        if board[r][col] == 0:
            return r

def main():
    board = create_board()
    game_over = False
    turn = 0
    while not game_over:
        if turn == 0:
            col = int(input('Player 1 Make your selection (0-6):'))
            if is_valid_location(board, col):
                row = get_next_free_row(board, col)
                drop_piece(board, row, col, 1)
        else:
            col = int(input('Player 2 Make your selection (0-6):'))
            if is_valid_location(board, col):
                row = get_next_free_row(board, col)
                drop_piece(board, row, col, 2)

        print(board)
        turn += 1
        turn = turn % 2

main()
