def monty(swaps):
    left = "x"
    middle = "Q"
    right  = "x"

    for swap in swaps:
        if swap == "L":
            left, middle = middle, left
        if swap == "R":
            middle, right = right, middle
        if swap == "O":
            right, left = left, right

    if left == "Q":
        return "left"
    if right == "Q":
        return "right"
    if middle == "Q":
        return "middle"