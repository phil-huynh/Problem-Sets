def breakout_room(code, message):
    count = 0
    index = 0

    for letter in message:
        if letter == code[index]:
            if index == len(code) - 1:
               index = 0
               count += 1
            else:
                index += 1
    return count