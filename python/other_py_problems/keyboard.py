def check_word(word, char_dict):
    row = 0
    for i,letter in enumerate(word):
        if i == 0:
            row = char_dict[letter.lower()]
        else:
            if char_dict[letter.lower()] != row:
                return False
    return True

def keyboard_words(words):
    row_one = "qwertyuiop"
    row_two = "asdfghjkl"
    row_three = "zxcvbnm"
    char_dict = {}

    for char in row_one:
        char_dict[char] = 1

    for char in row_two:
        char_dict[char] = 2

    for char in row_three:
        char_dict[char] = 3

    results = []
    for word in words:
        if check_word(word, char_dict):
            results.append(word)

    return results



print(keyboard_words(["Hello","Alaska","Dad","Peace", "adsdf","sfd"]))