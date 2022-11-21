def longest_repetition(chars):
    if not chars:
        return ("", 0)
    character, longest, length, index = chars[0], 1, 1, 1
    while index < len(chars):
        if chars[index] == chars[index - 1]:
            length += 1
            if index == len(chars) - 1:
                if length > longest:
                    character, longest = chars[index], length
        else:
            if length > longest:
                character, longest = chars[index - 1], length
            length = 1
        index += 1
    return (character, longest)