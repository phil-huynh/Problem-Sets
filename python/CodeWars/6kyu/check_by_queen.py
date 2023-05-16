# https://www.codewars.com/kata/5a1cae0832b8b99e2900000c/train/python

# An opponent's king who can be taken by the queen is said to be in 'check', and would then need to find some way to escape this situation.

# In any normal game of chess, the queen would work with her army on an 8x8 board to threaten the king in this way, and ultimately try to win the game. However, for this kata, the queen will work by herself on a 5x5 board.

# The 5x5 chessboard will be represented as a 2 dimensional array, (ie: an array containing 5 other arrays, each containing 5 single character elements). Empty spaces within each sub-array will be represented by an asterix: "*", while one of these 25 elements will be represented by a "q" (queen) and a "k" (king). Both will be represented in lower case.

# The 2 dimensional chessboard array would look something like this:

# var board = [ [ '*', '*', '*', '*', '*' ],
#               [ '*', '*', '*', '*', 'k' ],
#               [ '*', '*', '*', '*', '*' ],
#               [ '*', 'q', '*', '*', '*' ],
#               [ '*', '*', '*', '*', '*' ] ];
# Your task is to write a function which will return true if the king is in check, and false if he isn't.


def check(board):
    cache = {"k": "empty", "q": "empty"}
    for i, row in enumerate(board):
        for j, square in enumerate(row):
            if cache.get(square):
                cache[square] = {"row": i, "col": j}
    if cache["k"]["row"] == cache["q"]["row"] or \
        cache["k"]["col"] == cache["q"]["col"] or \
        cache["k"]["col"] - cache["k"]["row"] == cache["q"]["col"] - cache["q"]["row"] or \
        cache["k"]["col"] + cache["k"]["row"] == cache["q"]["col"] + cache["q"]["row"]:
        return True
    return False