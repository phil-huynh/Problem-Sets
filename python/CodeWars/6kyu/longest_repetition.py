# https://www.codewars.com/kata/586d6cefbcc21eed7a001155/train/python

# For a given string s find the character c (or C) with longest consecutive repetition and return:

# (c, l)
# where l (or L) is the length of the repetition. If there are two or more characters with the same l return the first in order of appearance.

# For empty string return:

# ('', 0)
# Happy coding! :)

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