/*
https://www.codewars.com/kata/63cbe409959401003e09978b/train/javascript

These arrays are too long! Let's reduce them!

Description
Write a function that takes in an array of integers from 0-9, and returns a new array:

Numbers with no identical numbers preceding or following it returns a 1: 2, 4, 9  => 1, 1, 1
Sequential groups of identical numbers return their count: 6, 6, 6, 6 => 4
Example

[0, 4, 6, 8, 8, 8, 5, 5, 7] => [1, 1, 1, 3, 2, 1]

Your function should then repeat the process on the resulting array, and on the resulting array of that, until it returns a single integer:

[0, 4, 6, 8, 8, 8, 5, 5, 7] =>  [1, 1, 1, 3, 2, 1] => [3, 1, 1, 1] => [1, 3] => [1, 1] => [2]

When your function has reduced the array to a single integer following these rules, it should return that integer.

[2] => 2

Rules and assertions
All test arrays will be 2+ in length
All integers in the test arrays will be positive numbers from 0 - 9
You should return an integer, not an array with 1 element
*/

function setReducer(input) {
  while (input.length > 1) {
    let [ cache, next ] = [ [input[0]],[] ]
    input.forEach((item, i) => {
      if (i === input.length - 1) {
        if (item === cache[0]) {
          cache.push(item)
          next.push(cache.length)
        }
        else {
          next.push(cache.length)
          next.push(1)
        }
      }
      else if (i > 0) {
        if (item === cache[0]) {
          cache.push(item)
        }
        else {
          next.push(cache.length)
          cache = [item]
        }
      }
    })
    input = next
  }
  return input[0]
}