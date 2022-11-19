def check_for_word(board, full_word, found, row, col, word, used):
    if [row, col] in used:
        return
    used.append([row, col])
    if len(word) == 0:
        found[full_word] = True
        return
    else:
        try:
            if board[row-1][col-1] == word[0]:
                check_for_word(board, full_word, found, row-1, col-1, word[1:], used)
        except IndexError:
            pass
        try:
            if board[row-1][col] == word[0]:
                check_for_word(board, full_word, found, row-1, col, word[1:], used)
        except IndexError:
            pass
        try:
            if board[row-1][col+1] == word[0]:
                check_for_word(board,full_word, found, row-1, col+1, word[1:], used)
        except IndexError:
            pass
        try:
            if board[row][col-1] == word[0]:
                check_for_word(board, full_word, found, row, col-1, word[1:], used)
        except IndexError:
            pass
        try:
            if board[row][col+1] == word[0]:
                check_for_word(board, full_word, found, row, col+1, word[1:], used)
        except IndexError:
            pass
        try:
            if board[row+1][col-1] == word[0]:
                check_for_word(board, full_word, found, row+1, col-1, word[1:], used)
        except IndexError:
            pass
        try:
            if board[row+1][col] == word[0]:
                check_for_word(board, full_word, found, row+1, col, word[1:], used)
        except IndexError:
            pass
        try:
            if board[row+1][col+1] == word[0]:
                check_for_word(board, full_word, found, row+1, col+1, word[1:], used)
        except IndexError:
            pass

def score_boggle(board, words):
    found = {}
    score = 0
    for word in words:
        for i, row in enumerate(board):
            for j, col in enumerate(row):
                if board[i][j] == word[0]:
                    check_for_word(board, word, found, i, j, word[1:], [])
    words_found = list(found.keys())
    for answer in words_found:
        if len(answer) > 2 and len(answer) < 5:
            score += 1
        if len(answer) == 5:
            score += 2
        if len(answer) == 6:
            score += 3
        if len(answer) == 7:
            score += 4
        if len(answer) > 7:
            score += 11
    return score




print(score_boggle(
  [['V', 'R', 'T', 'S'],
  ['R', 'W', 'E', 'I'],
  ['O', 'I', 'J', 'I'],
  ['Y', 'C', 'K', 'T']],
  ['WICK', 'TIER', 'ROY', 'ROCK', 'WOW', 'SEW', 'WE', 'JEW', 'SITE', 'VEST', 'SITE', 'ROW', 'ROWE', 'SETTER', 'ROWER', 'ROWBOAT', 'JET', 'JETS', 'WEST', 'WESTER', 'WET', 'WETS', 'STEW']
  ))

# [['V', 'R', 'T', 'S'], ['R', 'W', 'E', 'I'], ['O', 'I', 'J', 'I'], ['Y', 'C', 'K', 'T']]

# ['WICK', 'TIER', 'ROY', 'ROCK', 'WOW', 'SEW', 'WE', 'JEW', 'SITE', 'VEST', 'SITE', 'ROW', 'ROWE', 'SETTER', 'ROWER', 'ROWBOAT', 'JET', 'JETS', 'WEST', 'WESTER', 'WET', 'WETS', 'STEW']

# [['T', 'D', 'A', 'L'], ['I', 'Y', 'P', 'X'], ['H', 'R', 'U', 'D'], ['Q', 'C', 'T', 'E']]

# ['QCTEDURHIYPXLADT', 'QCTEDURHIYXPLADT', 'LAD', 'PAL', 'LAY', 'LAYUP', 'PUT', 'PAD', 'TUX', 'ED', 'TRUE', 'RUDE', 'HIT', 'HID', 'CHIT', 'CHIRP', 'DIRT', 'YIRT', 'PAX', 'PA', 'PAX', 'CHIRP', 'CHIRPED', 'CRY', 'TRIAD', 'TRIP', 'DUE', 'PRUDE']