def num_same_spaces(yesterday, today):
    matches = 0
    for i, space in enumerate(today):
        if space == yesterday[i] and space == "C":
            matches += 1
    return matches