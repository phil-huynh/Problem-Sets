/*
https://www.codewars.com/kata/525f4206b73515bffb000b21/train/javascript

We need to sum big numbers and we require your help.

Write a function that returns the sum of two numbers. The input numbers are strings and the function must return a string.

Example
add("123", "321"); -> "444"
add("11", "99");   -> "110"
Notes
The input numbers are big.
The input is a string of only digits
The numbers are positives

*/

function add(a, b) {
  a = a.split("").reverse();
  b = b.split("").reverse();
  let carried = 0, result = []
  const [top, bottom] = a.length >= b.length ? [a, b] : [b, a]

  top.forEach((num, i) => {
    let total = carried;
    total += bottom[i] ? Number(num) + Number(bottom[i]) : Number(num);
    carried = total >= 10 ? 1 : 0;
    carried ? result.push(Number(total.toString()[1])) : result.push(total);
    (i === top.length - 1) && carried ? result.push(1) : null;
  })
  return result.reverse().join("");
}