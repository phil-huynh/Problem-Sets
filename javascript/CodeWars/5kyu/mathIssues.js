/*
https://www.codewars.com/kata/5267faf57526ea542e0007fb/train/javascript

Oh no, our Math object was "accidently" reset. Can you re-implement some of those functions? We can assure, that only non-negative numbers are passed as arguments. So you don't have to consider things like undefined, null, NaN, negative numbers, strings and so on.

Here is a list of functions, we need:

Math.round()
Math.ceil()
Math.floor()
*/

Math.round = function(number) {
  console.log(number)
  let numArray = number.toString().split('.')
  if (numArray.length === 1) {return Number(numArray[0])}
  if (Number(numArray[1][0]) >= 5) {
    return Math.ceil(number)
  }
  return Math.floor(number)
};

Math.ceil = function(number) {
  let numArray = number.toString().split('.')
  if (numArray.length === 1) {return Number(numArray[0])}
  return Number(number.toString().split('.')[0]) + 1
};

Math.floor = function(number) {
  return Number(number.toString().split('.')[0])
};