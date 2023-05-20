/*
https://www.codewars.com/kata/62013b174c72240016600e60/train/javascript

Wordle is a game where users try to guess a hidden 5 letter word. Feedback is given for each guess, in the form of colored tiles, indicating when letters match or occupy the correct position.

see: https://www.nytimes.com/games/wordle/index.html

The Brief
Make a function that takes in a 5 letter guess and, comparing to a known solution, returns clues for the user to solve the wordle puzzle.

Requirements
The function takes in two strings of 5 letters each, a guess and a solution.
The function returns a string of 5 letters.
The returned string is composed of letters each corresponding to a letter of the guess: 'b' (black) when the letter is not present in the answer; 'y' (yellow) when the letter is present but in a different location; and 'g' (green) when the letter is present and in the right location.
Duplicates
A letter appearing in the correct place is always green, including if it appears elsewhere in the word.
A letter can only be green or yellow as many times as it appears in the correct answer. Extra occurences of that letter are marked as 'b'. Below are some examples, see example tests for more:
letters are evaluated left to right.
Guess: xxxxx
Answer: yxxxx
Expected Output: bgggg
Explanation: extra letters marked as 'b'

guess: xxxxz
answer:aaaax
expected output: ybbbb
first x marked as 'y',  and each one as 'b' after
*/

function resolver(guess, solution){
  const cache = {}
  const ref = {
    0: null,
    1: null,
    2: null,
    3: null,
    4: null
  }
  guess = guess.split('')
  solution.split('').forEach((letter) => {
    if(!cache[letter]) {
      cache[letter] = 0
    }
    cache[letter]++
  })
  guess.forEach((letter, i) => {
    if (letter === solution[i]) {
      cache[letter]--
      ref[i] = 'g'
    }
  })
  guess.forEach((letter, i) => {
    if (cache[letter] > 0 && !ref[i]) {
      cache[letter]--
      ref[i] = 'y'
    }
  })
  for (let key in ref) {
    if (ref[key] == null) {
      ref[key] = 'b'
    }
  }
  const result = []
  for (let key of [0,1,2,3,4]) {
    result.push(ref[key])
  }
  return result.join('')
}