function countConsonants(str) {
  const consonants = {
    'b': 1,
    'c': 1,
    'd': 1,
    'f': 1,
    'g': 1,
    'h': 1,
    'j': 1,
    'k': 1,
    'l': 1,
    'm': 1,
    'n': 1,
    'p': 1,
    'q': 1,
    'r': 1,
    's': 1,
    't': 1,
    'v': 1,
    'w': 1,
    'x': 1,
    'y': 1,
    'z': 1,
  }
  const checker = {}
  let total = 0
  str.split('').forEach((letter) => {
    letter = letter.toLowerCase()
    if (consonants[letter]) {
      if (!checker[letter]) {
        checker[letter] = true
        total++
      }
    }
  })
  return total
}