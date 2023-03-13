function keywordCipher(string, keyword){
  const alphabet = "abcdefghijklmnopqrstuvwxyz".split('');
  const letters = alphabet.slice()
  const keyLetters = [];
  keyword.split('').forEach((letter) => {
    letter = letter.toLowerCase()
    keyLetters.includes(letter) ? null : keyLetters.push(letter)
    letters.includes(letter) ? letters.splice(letters.indexOf(letter), 1) : null
  })
  const cypherKey = [...keyLetters, ...letters]
  return string.split('').map((letter) => (
    cypherKey.includes(letter.toLowerCase()) ? cypherKey[alphabet.indexOf(letter.toLowerCase())] : letter)).join('')
}