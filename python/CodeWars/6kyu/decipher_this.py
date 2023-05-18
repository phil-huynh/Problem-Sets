# https://www.codewars.com/kata/581e014b55f2c52bb00000f8/train/python

# You are given a secret message you need to decipher. Here are the things you need to know to decipher it:

# For each word:

# the second and the last letter is switched (e.g. Hello becomes Holle)
# the first letter is replaced by its character code (e.g. H becomes 72)
# Note: there are no special characters used, only letters and spaces

# Examples

# decipherThis('72olle 103doo 100ya'); // 'Hello good day'
# decipherThis('82yade 115te 103o'); // 'Ready set go'


def arrange(word):
    if len(word) <= 1:
        return word
    word = [letter for letter in word]
    word[0], word[-1] = word[-1], word[0]
    return "".join(word)

def decipher_this(string):
    message, final = string.split(), []
    for word in message:
        first, leftover = '', ''
        for letter in word:
            if letter.isdigit():
                first += letter
            else:
                leftover += letter
        final.append(f"{chr(int(first))}{arrange(leftover)}")
    return " ".join(final)