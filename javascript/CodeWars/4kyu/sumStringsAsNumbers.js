/*
https://www.codewars.com/kata/5324945e2ece5e1f32000370/train/javascript

Given the string representations of two integers, return the string representation of the sum of those integers.

For example:

sumStrings('1','2') // => '3'
A string representation of an integer will contain no characters besides the ten numerals "0" to "9".

I have removed the use of BigInteger and BigDecimal in java

Python: your solution need to work with huge numbers (about a milion digits), converting to int will not work.
*/

function removeZeros(array) {
  count = 0
  for (let char of array) {
    if (char === '0') { count += 1 }
    else { break }
  }
  while (count) {
    array.shift()
    count--
  }
  return array
}

function sumStrings(a,b) {
  a = removeZeros(a.split("")).reverse()
  b = removeZeros(b.split("")).reverse()
  let [carried, result] = [0, []]
  let [top, bottom] = a.length >= b.length ? [a, b] : [b, a]
  top.forEach((number, index) => {
    let total = carried == 1 ? 1 : 0
    if (bottom[index]) {
     total += Number(bottom[index])
    }
    total += Number(number)
    if (total >= 10) {
      carried = 1
      total = Number(total.toString()[1])
    } else {
      carried = 0
    }
    result.push(total)
    total = 0
    if (index === top.length - 1){
      if (carried === 1) {
        result.push(1)
      }
    }
  })
  return result.reverse().join("")
}