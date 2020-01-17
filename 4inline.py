import sys, pygame
import numpy as np
import math
pygame.init()

ROWS = 6
COLUMNS = 7
BLUE = (0,0,255)
# Colors: 0 -> black, 1 -> red, 2 -> yellow
COLORS = [(0,0,0), (255,0,0), (255,255,0)]
SQUARESIZE = 100
HALFSQUARESIZE = SQUARESIZE // 2
RADIUS = HALFSQUARESIZE - 5

width = COLUMNS * SQUARESIZE
height = (ROWS+1) * SQUARESIZE
window = pygame.display.set_mode((width, height))
myfont = pygame.font.SysFont("comicsansms", 75)

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

    return 0


def clear_window():
    window.fill((0, 0, 0))


def draw_board(board):
    for r in range(board.shape[0]):
        for c in range(board.shape[1]):
            pygame.draw.rect(window, BLUE, (c*SQUARESIZE, r*SQUARESIZE+SQUARESIZE, SQUARESIZE, SQUARESIZE))
            pygame.draw.circle(window, COLORS[int(board[r][c])], (c*SQUARESIZE+HALFSQUARESIZE, r*SQUARESIZE+SQUARESIZE+HALFSQUARESIZE), RADIUS)


def main():
    board = create_board()
    game_over = False
    turn = 0
    while not game_over:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

            if event.type == pygame.MOUSEMOTION:
                clear_window()
                posx = event.pos[0]
                pygame.draw.circle(window, COLORS[turn+1], (posx, HALFSQUARESIZE), RADIUS)

            if event.type == pygame.MOUSEBUTTONDOWN:
                clear_window()
                posx = event.pos[0]
                if turn == 0:
                    col = int(math.floor(posx / SQUARESIZE))
                    if is_valid_location(board, col):
                        row = get_next_free_row(board, col)
                        drop_piece(board, row, col, 1)
                else:
                    col = int(math.floor(posx / SQUARESIZE))
                    if is_valid_location(board, col):
                        row = get_next_free_row(board, col)
                        drop_piece(board, row, col, 2)

                print(board)
                turn += 1
                turn = turn % 2

                winner = int(check_winner(board))
                if (winner != 0):
                    label = myfont.render('Player {} wins!!'.format(winner), 1, COLORS[winner])
                    window.blit(label, (70, 10))
                    game_over = True

        draw_board(board)
        pygame.display.update()

        if game_over:
            pygame.time.wait(3000)

main()
