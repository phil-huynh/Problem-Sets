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

def find_combos(combo, digits, combos):
    if len(digits) == 0:
        combos.append(combo)
        return
    letters = []
    [letters.append(letter) for letter in ref[digits[0]]]
    for letter in letters:
        find_combos(combo + letter, digits[1:], combos)

def translate(words, digits):
    digits = str(digits)
    combos = []
    total = 0
    find_combos("", digits, combos)
    for combination in combos:
        if combination in words:
            total += 1
    return total

print(translate(['TOMO', 'MONO', 'DAK'], 6666))
print(translate(['DOM', 'FON', 'TOM'], 366))
print(translate(['JA', 'LA'], 52))