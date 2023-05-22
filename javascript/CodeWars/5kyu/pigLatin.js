/*
https://www.codewars.com/kata/520b9d2ad5c005041100000f/train/javascript

Move the first letter of each word to the end of it, then add "ay" to the end of the word. Leave punctuation marks untouched.

Examples
pig_it('Pig latin is cool') # igPay atinlay siay oolcay
pig_it('Hello world !')     # elloHay orldway !
*/

function pigIt(str){
  const punctuation = [",", ".", "?", "!"]
  return str.split(' ').map(word =>
    !punctuation.includes(word) ? `${word.slice(1)}${word[0]}ay` : word).join(' ')
}