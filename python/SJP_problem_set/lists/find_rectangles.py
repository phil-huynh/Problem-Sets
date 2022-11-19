def mark_recangles(board, row, col):
    board[row][col] = "O"
    try:
        if board[row][col+1] == "*" and row >= 0 and col+1 >= 0:
            mark_recangles(board, row, col+1)
    except IndexError:
        pass
    try:
        if board[row+1][col] == "*" and row+1 >= 0 and col >= 0:
            mark_recangles(board, row+1, col)
    except IndexError:
        pass


def count_rectangles(drawing):
    count = 0
    for i in range(len(drawing)):
        row = []
        [row.append(char) for char in drawing[i]]
        drawing[i] = row
    for j in range(len(drawing)):
        for k in range(len(drawing[j])):
            if drawing[j][k] == "*":
                count += 1
                mark_recangles(drawing, j, k)
            if drawing[j][k] == ".":
                continue
            if drawing[j][k] == "O":
                continue
    return count