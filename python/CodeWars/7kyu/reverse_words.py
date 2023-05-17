# Complete the function that accepts a string parameter, and reverses each word in the string. All spaces in the string should be retained.

# Examples
# "This is an example!" ==> "sihT si na !elpmaxe"
# "double  spaces"      ==> "elbuod  secaps"

def reverse_words(text):
    text = [word for word in text.split(' ')]
    for i, word in enumerate(text):
        word = [letter for letter in word]
        word.reverse()
        text[i] = "".join(word)
    return " ".join(text)