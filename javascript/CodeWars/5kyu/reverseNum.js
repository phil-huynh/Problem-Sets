/*
https://www.codewars.com/kata/57c786e858da9e5ed20000ea/train/javascript

Given a string representing an integer, return a string with every sequence of ascending or descending digits reversed.

Examples:

123456  --->  654321  // ascending sequence 123456
654321  --->  123456  // descending sequence 654321
135246  --->  531642  // ascending sequence 135, ascending sequence 246
642531  --->  246135  // descending sequence 642, descending sequence 531
Such sequences are not required to be strictly ascending / descending:

12333  ---> 33321     // ascending sequence 12333
66654  ---> 45666     // descending sequence 66654
133555224466  ---> 555331664422   // ascending sequence 133555, ascending sequence 224466
If a digit (or several of the same consecutive digits) is at the junction part of ascending and descending sequence, it should belong to the left part of the junction:

12321  ---> 32112
digit 3 may be part of an ascending order(123)
It can also be a part of a descending order(321)

135642  --->  653124
digit 6 may be part of an ascending order(1356)
It can also be a part of a descending order(642)

13555432  ---> 55531234
consecutive digits 555 may be part of an ascending order(13555)
It can also be a part of a descending order(555432)
If the number is a negative number, the symbol - does not reverse:

-123  ---> -321
-123321  --->  -332112
After reverse, if the digit 0 is in the first place (ignoring the sign), it should be removed:

420135  ---> 024531  ---> 24531
-520025  ---> -002552  --->  -2552
Task
Complete function reverseNumber() that accepts a arguments n(given by string format).

Returns the number that reverse in accordance with the rules(string format).
*/


function reverseNumber(n){
  let negative = n[0] === '-' ? true : false
  n = negative ? n.slice(1) : n

  let dir = null, result = '', temp = [n[0]]
  const reset = () => { dir = null; temp = [] }
  n.split('').forEach((digit, i) => {
    let last = temp[temp.length - 1]
    if (i > 0) {
      if (digit === last) temp.push(digit)
      else if (Number(digit) > Number(last)){
        if (!dir) dir = "up"
        else if (dir === 'down') { result += temp.reverse().join(''); reset() }
        temp.push(digit)
      }
      else {
        if (!dir) dir = "down"
        else if (dir === "up") { result += temp.reverse().join(''); reset() }
        temp.push(digit)
      }
    }
  })
  if (result.length !== n.length) { result += temp.reverse().join('') }
  while (result[0] === '0') { result = result.slice(1) }
  return negative ? `-${result}` : result
}