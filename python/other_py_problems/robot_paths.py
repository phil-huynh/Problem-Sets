from pprint import pprint

def make_board(n):
    board = []
    for i in range(n):
        board.append([])
        for j in range(n):
            board[i].append(False)
    return board

def toggle_square(board, i, j):
    board[i][j] = not board[i][j]
    return board


def robot_paths(n, board, i, j, count):
    if not board:
        board = make_board(n)

    if not (i >= 0 and i < n and j >= 0 and j < n) or board[i][j] == True:
        return

    if i == n - 1 and j == n - 1:
        count += 1
        return count


    board = toggle_square(board, i, j)
    print("\n")
    pprint(board)
    count = robot_paths(n, board, i, j + 1, count) + robot_paths(n, board, i, j - 1, count) + robot_paths(n, board, i + 1, j, count) + robot_paths(n, board, i - 1, j, count)

    board = toggle_square(board, i, j)
    return count


print(robot_paths(5, None, 0, 0, 0))