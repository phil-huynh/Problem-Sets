ref = {
    "1": ["1", "2", "4"],
    "2": ["1", "2", "3", "5"],
    "3": ["2", "3", "6"],
    "4": ["1", "4", "5", "7"],
    "5": ["2", "4", "5", "6", "8"],
    "6": ["3", "5", "6", "9"],
    "7": ["4", "7", "8"],
    "8": ["0", "5", "7", "8", "9"],
    "9": ["6", "8", "9"],
    "0": ["0", "8"],
}

def get_pins(observed):
    result = []

    def recursive (pin, combo, result):
        if not pin:
            result.append(combo)
            return
        for num in ref[pin[0]]:
            recursive(pin[1:], f"{combo}{num}", result)

    recursive(observed, "", result)
    return result
