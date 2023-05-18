from pprint import pprint


def make_board(n):
    return [["." for j in range(n)] for i in range(n)]

def create_cache(n):
    cache = {
        "row": {num: True for num in range(n)},
        "col": {num: True for num in range(n)},
        "fwd_diag": {num: True for num in range(-n, n+1)},
        "bck_diag": {num: True for num in range(0, ((n-1)*2) + 1)}
    }
    return cache

def place_piece(board, cache, row, col):
    cache["row"][row] = False
    cache["col"][col] = False
    cache["fwd_diag"][col - row] = False
    cache["bck_diag"][row + col] = False
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
    if not cache["row"].get(row) or \
        not cache["col"].get(col) or \
        not cache["fwd_diag"].get(col - row) or \
        not cache["bck_diag"].get(row + col):
        return False
    return True


def solve_n_queens(n, fixed_queen):
    print(f"\n Here are the solutions for n-queens if n={n}\n")
    board, safe, results = make_board(n), create_cache(n), []
    place_piece(board, safe, fixed_queen[0], fixed_queen[1])
    def n_queens(board, safe, n, row):
        if row == n:
            string = ""
            for r in board:
                string += f'{"".join(r)}\n'[:]
            results.append(string)
            return string
        else:
            if row_is_safe(safe, row):
                for col in range(len(board[row])):
                    if is_safe(safe, row, col):
                        board, safe = place_piece(board, safe, row, col)
                        n_queens(board, safe.copy(), n, row + 1)
                        board, safe = remove_piece(board, safe, row, col)
            else:
                n_queens(board, safe.copy(), n, row + 1)
    n_queens(board, safe, n, 0)
    if results:
        return results[0]
    else:
        return None


test = solve_n_queens(4, (2,2))
print(test)


# board = make_board(5)
# cache = create_cache(5)

# print("\n")
# pprint(board)
# print("\n")
# pprint(cache)
# place_piece(board, cache, 1, 1)
# print("\n")
# pprint(board)
# print("\n")
# pprint(cache)
# print("\n")
# print(is_safe(cache, 1, 3))
