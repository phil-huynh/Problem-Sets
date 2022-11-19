def mode(numbers):
    checker = {}
    highest = 0
    modes = []
    for num in numbers:
        if checker.get(num):
            checker[num] += 1
            if checker[num] > highest:
                highest = checker[num]
        else:
            checker[num] = 1

    for key in checker:
        if checker[key] == highest:
            modes.append(key)
    return modes