def calculate_plays(num_quarters):
    slots = [0, 0, 0]
    plays = 0
    i = 0
    quarters = num_quarters

    while quarters:
        slots[i] += 1
        plays += 1
        quarters -= 1
        if i == 0 and slots[i] % 27 == 0:
            quarters += 20
        if i == 1 and slots[i] % 100 == 0:
            quarters += 50
        if i == 2 and slots[i] % 8 == 0:
            quarters += 7
        if i == 2:
            i = 0
        else:
            i += 1
    return plays