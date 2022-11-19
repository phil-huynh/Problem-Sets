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