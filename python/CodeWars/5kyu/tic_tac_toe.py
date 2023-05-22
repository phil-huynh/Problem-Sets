# https://www.codewars.com/kata/525caa5c1bf619d28c000335/train/python

# If we were to set up a Tic-Tac-Toe game, we would want to know whether the board's current state is solved, wouldn't we? Our goal is to create a function that will check that for us!

# Assume that the board comes in the form of a 3x3 array, where the value is 0 if a spot is empty, 1 if it is an "X", or 2 if it is an "O", like so:

# [[0, 0, 1],
#  [0, 1, 2],
#  [2, 1, 0]]
# We want our function to return:

# -1 if the board is not yet finished AND no one has won yet (there are empty spots),
# 1 if "X" won,
# 2 if "O" won,
# 0 if it's a cat's game (i.e. a draw).
# You may assume that the board passed in is valid in the context of a game of Tic-Tac-Toe.


def is_solved(board):
    has_empty = False
    if ((board[0][0] == board[1][1] and board[0][0] == board[2][2]) or \
    (board[0][2] == board[1][1] and board[0][2] == board[2][0])) and board[0][0] != 0:
        return board[1][1]
    for row in board:
        if 0 in row:
            has_empty = True
        if row[0] == row[1] and row[0] == row[2] and row[0] != 0 :
            return row[0]
    for col in [0, 1, 2]:
        if board[0][col] == board[1][col] and board[0][col] == board[2][col] and board[0][col] != 0:
            return board[0][col]
    return -1 if has_empty else 0