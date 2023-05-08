# Greed is a dice game played with five six-sided dice. Your mission, should you choose to accept it, is to score a throw according to these rules. You will always be given an array with five six-sided dice values.

#  Three 1's => 1000 points
#  Three 6's =>  600 points
#  Three 5's =>  500 points
#  Three 4's =>  400 points
#  Three 3's =>  300 points
#  Three 2's =>  200 points
#  One   1   =>  100 points
#  One   5   =>   50 point
# A single die can only be counted once in each roll. For example, a given "5" can only count as part of a triplet (contributing to the 500 points) or as a single 50 points, but not both in the same roll.

# Example scoring

#  Throw       Score
#  ---------   ------------------
#  5 1 3 4 1   250:  50 (for the 5) + 2 * 100 (for the 1s)
#  1 1 1 3 1   1100: 1000 (for three 1s) + 100 (for the other 1)
#  2 4 4 5 4   450:  400 (for three 4s) + 50 (for the 5)
# In some languages, it is possible to mutate the input to the function. This is something that you should never do. If you mutate the input, you will not be able to pass all the tests.


def score(dice):
    points = {
        6: 600,
        4: 400,
        3: 300,
        2: 200,
        5: [50, 500],
        1: [100, 1000]
    }
    checker = {}
    score = 0
    for num in dice:
        if num not in checker:
            checker[num] = 1
        else:
            checker[num] += 1
    for key in checker:
        if key != 1 and key != 5:
            if checker[key] >= 3:
                score += points[key]
        else:
            if checker[key] >= 3:
                leftover = checker[key] % 3
                total = points[key][1]
                total += leftover * points[key][0]
                score += total
            else:
                score += checker[key] * points[key][0]
    return score

