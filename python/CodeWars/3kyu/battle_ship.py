def check_ships(battleship, cruisers, destroyers, submarines):
    if battleship == 1 and cruisers == 2 and destroyers == 3 and submarines == 4:
        return True
    return False

def near_other_ships(board, i, j):
    if (j-1 >= 0 and board[i][j-1] == 2) or \
      (j-1 >= 0 and i-1>=0 and board[i-1][j-1] == 2) or \
      (i-1 >= 0 and board[i-1][j] == 2 ) or \
      (i-1 >= 0 and j+1 < len(board) and board[i-1][j+1] == 2) or \
      (j+1 < len(board) and board[i][j+1] == 2) or \
      (i+1 < len(board) and j+1 < len(board) and board[i+1][j+1] == 2 ) or \
      (i+1 < len(board) and board[i+1][j] == 2 ) or \
      (i+1 < len(board) and j-1>=0 and board[i+1][j-1] == 2):
        return True
    return False

def boat_check_row(board, i, j):
    count, square = 0, board[i][j]
    while square == 1 and j < 10:
        board[i][j] = 2
        count += 1
        j += 1
        if j < 10:
            square = board[i][j]
    return count

def boat_check_col(board, i, j):
    count, square = 0, board[i][j]
    while square == 1 and i < 10:
        board[i][j] = 2
        count += 1
        i += 1
        if i < 10:
            square = board[i][j]
    return count

def validate_battlefield(field):
    ships = { "bat": 0, "cru": 0, "des": 0, "sub": 0 }
    shipLengths = { 4: "bat", 3: "cru", 2: "des"}
    for i, row in enumerate(field):
        for j, square in enumerate(row):
            if square == 1:
                if near_other_ships(field, i, j):
                    return False
                across = boat_check_row(field, i, j)
                field[i][j] = 1
                down = boat_check_col(field, i, j)
                if across > 4 or down > 4:
                    return False
                if across == 1 and down == 1:
                    ships["sub"] += 1
                if across > down:
                    if down > 1:
                        return False
                    ships[shipLengths[across]] += 1
                if down > across:
                    if across > 1:
                        return False
                    ships[shipLengths[down]] += 1
    return check_ships(ships["bat"], ships["cru"], ships["des"], ships["sub"])