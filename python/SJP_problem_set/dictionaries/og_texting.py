def translate(words, digits):
    ref = {
      "0": '0',
      "1": '1',
      "2": 'ABC',
      "3": 'DEF',
      "4": 'GHI',
      "5": 'JKL',
      "6": 'MNO',
      "7": 'PQRS',
      "8": 'TUV',
      "9": 'WXYZ'
    }
    letter_ref = {}
    for key in ref:
        for char in ref[key]:
            letter_ref[char] = key
    digits = str(digits)
    total = 0
    for word in words:
        word_digits = ""
        for char in word:
            word_digits += letter_ref[char]
        if word_digits == digits:
            total += 1
    return total