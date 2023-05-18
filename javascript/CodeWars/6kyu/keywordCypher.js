/*
https://www.codewars.com/kata/57241cafef90082e270012d8/train/javascript

Third day at your new cryptoanalyst job and you come across your toughest assignment yet. Your job is to implement a simple keyword cipher. A keyword cipher is a type of monoalphabetic substitution where two parameters are provided as such (string, keyword). The string is encrypted by taking the keyword, dropping any letters that appear more than once. The rest of the letters of the alphabet that aren't used are then appended to the end of the keyword.

For example, if your string was "hello" and your keyword was "wednesday", your encryption key would be 'wednsaybcfghijklmopqrtuvxz'.

To encrypt 'hello' you'd substitute as follows,

              abcdefghijklmnopqrstuvwxyz
  hello ==>   |||||||||||||||||||||||||| ==> bshhk
              wednsaybcfghijklmopqrtuvxz
hello encrypts into bshhk with the keyword wednesday. This cipher also uses lower case letters only.

Good Luck.
*/

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