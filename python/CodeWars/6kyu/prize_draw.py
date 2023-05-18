# https://www.codewars.com/kata/5616868c81a0f281e500005c/train/python

# To participate in a prize draw each one gives his/her firstname.

# Each letter of a firstname has a value which is its rank in the English alphabet. A and a have rank 1, B and b rank 2 and so on.

# The length of the firstname is added to the sum of these ranks hence a number som.

# An array of random weights is linked to the firstnames and each som is multiplied by its corresponding weight to get what they call a winning number.

# Example:
# names: "COLIN,AMANDBA,AMANDAB,CAROL,PauL,JOSEPH"
# weights: [1, 4, 4, 5, 2, 1]

# PauL -> som = length of firstname + 16 + 1 + 21 + 12 = 4 + 50 -> 54
# The *weight* associated with PauL is 2 so PauL's *winning number* is 54 * 2 = 108.
# Now one can sort the firstnames in decreasing order of the winning numbers. When two people have the same winning number sort them alphabetically by their firstnames.

# Task:
# parameters: st a string of firstnames, we an array of weights, n a rank

# return: the firstname of the participant whose rank is n (ranks are numbered from 1)

# Example:
# names: "COLIN,AMANDBA,AMANDAB,CAROL,PauL,JOSEPH"
# weights: [1, 4, 4, 5, 2, 1]
# n: 4

# The function should return: "PauL"
# Notes:
# The weight array is at least as long as the number of names, it may be longer.

# If st is empty return "No participants".

# If n is greater than the number of participants then return "Not enough participants".

from functools import reduce

def score_name(name):
    letters = "abcdefghijklmnopqrstuvwxyz"
    ref = {letters[i]: i+1 for i in range(len(letters))}
    return reduce(lambda a,b: a + ref[b.lower()], name, 0)


def rank(st, we, n):
    if not st:
        return "No participants"
    names = st.split(",")
    if n > len(names):
        return "Not enough participants"
    players = zip(names, we)
    scoreboard = {player[0]: (score_name(player[0]) + len(player[0])) * player[1] for player in players}

    ranks = [(player, scoreboard[player]) for player in list(scoreboard.keys())]
    ranks.sort()
    ranks.sort(reverse=True, key=lambda a: a[1])
    return ranks[n-1][0]


# print(score_name("paul"))



# print(rank("Addison,Jayden,Sofia,Michael,Andrew,Lily,Benjamin", [4, 2, 1, 4, 3, 1, 2], 4))   # "Benjamin"
# print(rank("Elijah,Chloe,Elizabeth,Matthew,Natalie,Jayden", [1, 3, 5, 5, 3, 6], 2))          # "Matthew"
# print(rank("Aubrey,Olivai,Abigail,Chloe,Andrew,Elizabeth", [3, 1, 4, 4, 3, 2], 4))           # "Abigail"
# print(rank("Lagon,Lily", [1, 5], 2))                                                         # "Lagon"