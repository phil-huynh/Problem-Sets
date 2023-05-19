/*
https://www.codewars.com/kata/55c04b4cc56a697bb0000048/train/javascript

Complete the function scramble(str1, str2) that returns true if a portion of str1 characters can be rearranged to match str2, otherwise returns false.

Notes:

Only lower case letters will be used (a-z). No punctuation or digits will be included.
Performance needs to be considered.
Examples
scramble('rkqodlw', 'world') ==> True
scramble('cedewaraaossoqqyt', 'codewars') ==> True
scramble('katas', 'steak') ==> False
*/

function scramble(str1, str2) {
  let [check1, check2] = [{}, {}]
  for (let char of str1) { check1[char] ? check1[char] += 1 : check1[char] = 1 }
  for (let char of str2) { check2[char] ? check2[char] += 1 : check2[char] = 1 }
  for (let key in check2) { if (!check1[key] || check1[key] < check2[key]) { return false } }
  return true
}