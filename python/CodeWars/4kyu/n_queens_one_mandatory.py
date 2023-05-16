# A standard 8x8 chess board has its rows (aka ranks) labelled 1-8 from bottom to top, and its columns (aka files) labelled a-h from left to right. Any square can be denoted by a combination of letter and number. For example, the top left square is a8. A queen may attack any square on its rank or file. It may also attack any square diagonally.

# In this kata, chessboard may have any size from 1 to 10. Columns are marked with letters a-j, and rows with single digit from 1 to 0 (first row is marked with 1, ninth row is marked with 9, and tenth row is marked with 0, so a1 denotes bottom left field of the chessboard, and j0 - top right field on a 10x10 board).

# You will be given the position of one queen on the board (e.g. 'c3'). Your challenge is to compute the position of the remaining queens and return the full solution (including the original input) as a comma-separated string (e.g. 'd8,a7,e6,h5,b4,g3,c2,f1'). Fields do not have to be sorted in any particular way, but you have to adhere to above format (lowercase letters, no spaces, fields separated with commas).

# Note that there may be multiple valid solutions for a given starting position. Your function only needs to produce (any) one of these. All given starting positions produce valid solutions.

# If you wish to write more tests, the validity of a solution may be checked using preloaded function (see sample tests).

# Hint: check the wiki article for the various algorithms that are applicable to this problem.


def make_board(n):
    return [["." for j in range(n)] for i in range(n)]

def create_cache(n):
    return {
        "row": {num: True for num in range(n)},
        "col": {num: True for num in range(n)},
        "fwd_diag": {num: True for num in range(-n, n+1)},
        "bck_diag": {num: True for num in range(0, ((n-1)*2) + 1)}
    }

def place_piece(board, cache, row, col):
    del cache["row"][row]
    del cache["col"][col]
    del cache["fwd_diag"][col - row]
    del cache["bck_diag"][row + col]
    board[row][col] = "Q"
    return board, cache

def remove_piece(board, cache, row, col):
    cache["row"][row] = True
    cache["col"][col] = True
    cache["fwd_diag"][col - row] = True
    cache["bck_diag"][row + col] = True
    board[row][col] = "."
    return board, cache

def row_is_safe(cache, row):
    return True if cache["row"].get(row) else False

def is_safe(cache, row, col):
    if not cache["fwd_diag"].get(col - row) or not cache["bck_diag"].get(row + col):
        return False
    return True


def queens(position, n):
    col_labels_to_grid = { "a": 0, "b": 1,"c": 2, "d": 3, "e": 4, "f": 5, "g": 6, "h": 7, "i": 8, "j": 9 }
    col_grid_to_labels = {col_labels_to_grid[key]:key for key in col_labels_to_grid.keys()}

    fixed_queen = [char for char in position]
    fixed_queen[0] = col_labels_to_grid[fixed_queen[0]]
    fixed_queen[1] = n - int(fixed_queen[1]) if fixed_queen[1] != "0" else 0

    board, safe, results = make_board(n), create_cache(n), []
    place_piece(board, safe, fixed_queen[1], fixed_queen[0])

    def n_queens(board, safe, n, row):
        if row == n:
            board.reverse()
            string_arr = []
            for i, r in enumerate(board):
                for j, c in enumerate(r):
                    if board[i][j] == "Q":
                        string_arr.append(f"{col_grid_to_labels[j]}{i + 1 if i != 9 else 0}")
            results.append(",".join(string_arr))
            board.reverse()
            return
        else:
            columns = list(safe["col"].keys())
            if row_is_safe(safe, row):
                for col in columns:
                    if is_safe(safe, row, col):
                        board, safe = place_piece(board, safe, row, col)
                        n_queens(board, safe.copy(), n, row + 1)
                        board, safe = remove_piece(board, safe, row, col)
            else:
                n_queens(board, safe.copy(), n, row + 1)
    n_queens(board, safe, n, 0)
    return results[0] if results else None