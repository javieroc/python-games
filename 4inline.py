# import pygame
import numpy as np

# pygame.init()

SQUARESIZE
ROWS = 6
COLUMNS = 7

# width = COLUMNS * SQUARESIZE
# heigth = (ROWS+1) * SQUARESIZE
# window = pygame.display.set_mode((width, height))

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


def check_winner(board):
    # Check horizontal
    for r in range(board.shape[0]):
        for c in range(board.shape[1]-3):
            if board[r][c] != 0 and board[r][c] == board[r][c+1] and board[r][c] == board[r][c+2] and board[r][c] == board[r][c+3]:
                return board[r][c]

    # Check vertical
    for c in range(board.shape[1]):
        for r in range(board.shape[0]-3):
            if board[r][c] != 0 and board[r][c] == board[r+1][c] and board[r][c] == board[r+2][c] and board[r][c] == board[r+3][c]:
                return board[r][c]

    # Check positive diagonal /
    for r in range(3, board.shape[0]):
        for c in range(board.shape[1]-3):
            if board[r][c] != 0 and board[r][c] == board[r-1][c+1] and board[r][c] == board[r-2][c+2] and board[r][c] == board[r-3][c+3]:
                return board[r][c]

    # Check negative diagonal \
    for r in range(board.shape[0]-3):
        for c in range(board.shape[1]-3):
            if board[r][c] != 0 and board[r][c] == board[r+1][c+1] and board[r][c] == board[r+2][c+2] and board[r][c] == board[r+3][c+3]:
                return board[r][c]


def draw_board(board):
    pass


def main():
    board = create_board()
    game_over = False
    turn = 0
    while not game_over:
        # for event in pygame.event.get():
        #     if event.type == pygame.QUIT:
        #         pygame.quit()

        #     if event.type == pygame.

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

        winner = check_winner(board)
        if (winner == 1):
            print('Player 1 win')
            game_over = True
        elif (winner == 2):
            print('Player 2 win')
            game_over = True

main()
