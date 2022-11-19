from pprint import pprint

def make_board(n):
  board = []
  for i in range(n):
    row = []
    [row.append(".") for j in range(n)]
    board.append(row)
  return board

def place_piece(board, row, col):
    if board[row][col] == ".":
        board[row][col] = "Q"
    return board

def remove_piece(board, row, col):
    if board[row][col] == "Q":
        board[row][col] ="."
    return board

def row_safe(board, row):
    for square in board[row]:
        if square == "Q":
            return False
    return True

def col_safe(board, col):
    for i, row in enumerate(board):
        if board[i][col] == "Q":
            return False
    return True

def back_diag_safe(board, row, col):
    while row >= 0 and col >= 0:
        if board[row][col] == "Q":
            return False
        row -=1
        col -=1
    return True

def front_diag_safe(board, n, row, col):
    while row >= 0 and col < n:
        if board[row][col] == "Q":
            return False
        row -= 1
        col += 1
    return True

def is_safe_from_rooks(board, row, col):
    return row_safe(board, row) and col_safe(board, col)

def diagonals_safe(board, n, row, col):
    return back_diag_safe(board, row, col) and front_diag_safe(board, n, row, col)

def is_safe_from_queens(board, n, row, col):
    return is_safe_from_rooks(board, row, col) and diagonals_safe(board, n, row, col)

def solve_n_queens(n, fixed_queen):
    print(f"\n Here are the solutions for n-queens if n={n}\n")
    board = make_board(n)
    results = []
    def n_queens(board, n, row):
        if row == n:
            if board[fixed_queen[0]][fixed_queen[1]] == "Q":
                string = ""
                for r in board:
                    string += f'{"".join(r)}\n'[:]
                results.append(string)
                return results
        else:
            for col in range(len(board[row])):
                if row <= fixed_queen[0] or \
                (row > fixed_queen[0] and board[fixed_queen[0]][fixed_queen[1]] == "Q"):
                    if is_safe_from_queens(board, n, row, col):
                        board = place_piece(board, row, col)
                        n_queens(board, n, row + 1)
                        board = remove_piece(board, row, col)

    n_queens(board, n, 0)
    if results:
        return results[0]
    else:
        return None


test = solve_n_queens(4, (0,2))

pprint(test)
print("\n")
