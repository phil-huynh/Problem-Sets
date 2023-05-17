/*
https://www.codewars.com/kata/521c2db8ddc89b9b7a0000c1/train/javascript

Snail Sort
Given an n x n array, return the array elements arranged from outermost elements to the middle element, traveling clockwise.

array = [[1,2,3],
         [4,5,6],
         [7,8,9]]
snail(array) #=> [1,2,3,6,9,8,7,4,5]
For better understanding, please follow the numbers of the next array consecutively:

array = [[1,2,3],
         [8,9,4],
         [7,6,5]]
snail(array) #=> [1,2,3,4,5,6,7,8,9]
This image will illustrate things more clearly:

NOTE: The idea is not sort the elements from the lowest value to the highest; the idea is to traverse the 2-d array in a clockwise snailshell pattern.

NOTE 2: The 0x0 (empty matrix) is represented as en empty array inside an array [[]].
*/

snail = function(array) {
  const snailArray = []
  let top = 0
  let bottom = array.length
  let left = 0
  let right = array[0].length

  while (top < bottom && left < right) {

    for (let i = left; i < right; i++) {
      snailArray.push(array[top][i])
    }
    top++

    for (let j = top; j < bottom; j++) {
      snailArray.push(array[j][right - 1])
    }
    right--

    if (top < bottom){
      for (let k = right - 1; k > left - 1; k--){
        snailArray.push(array[bottom -1][k])
      }
      bottom--
    }

    if (left < right){
      for (let l = bottom - 1; l > top - 1; l--) {
        snailArray.push(array[l][left])
      }
      left++
    }

  }
  return snailArray
}