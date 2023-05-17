# Third day at your new cryptoanalyst job and you come across your toughest assignment yet. Your job is to implement a simple keyword cipher. A keyword cipher is a type of monoalphabetic substitution where two parameters are provided as such (string, keyword). The string is encrypted by taking the keyword, dropping any letters that appear more than once. The rest of the letters of the alphabet that aren't used are then appended to the end of the keyword.

# For example, if your string was "hello" and your keyword was "wednesday", your encryption key would be 'wednsaybcfghijklmopqrtuvxz'.

# To encrypt 'hello' you'd substitute as follows,

#               abcdefghijklmnopqrstuvwxyz
#   hello ==>   |||||||||||||||||||||||||| ==> bshhk
#               wednsaybcfghijklmopqrtuvxz
# hello encrypts into bshhk with the keyword wednesday. This cipher also uses lower case letters only.

# Good Luck.

def keyword_cipher(msg, keyword):
    alphabet = [letter for letter in "abcdefghijklmnopqrstuvwxyz"]
    letters, key_letters = alphabet[:], []
    keyword = [letter for letter in keyword]
    for letter in keyword:
        letter = letter.lower()
        if letter not in key_letters:
            key_letters.append(letter)
        if letter in letters:
            letters.pop(letters.index(letter))
    cypher_key = key_letters + letters
    return "".join([cypher_key[alphabet.index(letter.lower())] if letter.lower() in cypher_key else letter for letter in msg])