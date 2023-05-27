/*
https://www.codewars.com/kata/5842df8ccbd22792a4000245/train/javascript

You will be given a number and you will need to return it as a string in Expanded Form. For example:

expandedForm(12); // Should return '10 + 2'
expandedForm(42); // Should return '40 + 2'
expandedForm(70304); // Should return '70000 + 300 + 4'
NOTE: All numbers will be whole numbers greater than 0.

If you liked this kata, check out part 2!!
*/

function expandedForm(num) {
  num = num.toString()
  array = num.split("")
  copy = array.slice()
  final = ""
  array.forEach((digit, i) => {

    if(i === 0) {
      copy.shift()
      final += digit
      copy.forEach((x) => {
        final += "0"
      })
    } else if(digit === "0") {
      copy.shift()
    } else {
      copy.shift()
      final += ` + ${digit}`
      copy.forEach((x) => {
        final += "0"
      })
    }
  })
  return final
}