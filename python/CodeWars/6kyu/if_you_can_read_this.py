NATO = {
  "a": 'Alfa',
  "n": 'November',
  "b": 'Bravo',
  "o": 'Oscar',
  "c": 'Charlie',
  "p": 'Papa',
  "d": 'Delta',
  "q": 'Quebec',
  "e": 'Echo',
  "r": 'Romeo',
  "f": 'Foxtrot',
  "s": 'Sierra',
  "g": 'Golf',
  "t": 'Tango',
  "h": 'Hotel',
  "u": 'Uniform',
  "i": 'India',
  "v": 'Victor',
  "j": 'Juliett',
  "w": 'Whiskey',
  "k": 'Kilo',
  "x": 'Xray',
  "l": 'Lima',
  "y": 'Yankee',
  "m": 'Mike',
  "z": 'Zulu'
}


def to_nato(words):
    result = ""
    for i, letter in enumerate([l for l in words]):
        if NATO.get(letter.upper()):
            result += NATO.get(letter.upper())
        if not letter.isalnum() and letter != " " and not letter.isdigit():
            result += letter
        if i != len(words) - 1 and letter != " ":
            result += " "
    return result