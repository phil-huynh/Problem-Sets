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

