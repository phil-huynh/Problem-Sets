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