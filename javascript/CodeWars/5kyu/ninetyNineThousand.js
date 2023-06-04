/*
https://www.codewars.com/kata/5463c8db865001c1710003b2/train/javascript

Write a method that takes a number and returns a string of that number in English.

Your method should be able to handle any number between 0 and 99999. If the given number is outside of that range or not an integer, the method should return an empty string.

Examples
0      -->  "zero"
27     -->  "twenty seven"
100    -->  "one hundred"
7012   -->  "seven thousand twelve"
99205  -->  "ninety nine thousand two hundred five"
*/

const single= {
    0: "zero",
    1: "one",
    2: "two",
    3: "three",
    4: "four",
    5: "five",
    6: "six",
    7: "seven",
    8: "eight",
    9: "nine"
}

const teens= {
    0: "ten",
    1: "eleven",
    2: "twelve",
    3: "thirteen",
    4: "fourteen",
    5: "fifteen",
    6: "sixteen",
    7: "seventeen",
    8: "eighteen",
    9: "nineteen"
}

const tens_place= {
    "2": "twenty",
    "3": "thirty",
    "4": "forty",
    "5": "fifty",
    "6": "sixty",
    "7": "seventy",
    "8": "eighty",
    "9": "ninety"
}

const numberToEnglish = n => {
  if (n < 0 || n >= 100000 || n.toString().split('.').length > 1) return ""

  const handleTwoDigits = (num) => {
    if (num[0] === '0')  words.push(`${single[num[1]]}`)
    else if (num[0] === '1')  words.push(teens[num[1]])
    else {
      words.push(tens_place[num[0]])
      num[1] !== '0' ? words.push(`${single[num[1]]}`) : null
    }
  }

  const words = []
  n = n.toString()

  while (n) {
    if (n.length === 5) {
      handleTwoDigits(n.slice(0,2))
      words.push("thousand")
      n = n.slice(2)
    }
    else if (n.length === 4) {
      words.push(`${single[n[0]]} thousand`)
      n = n[1] === '0' ? n.slice(2) : n.slice(1)
    }
    else if (n.length === 3) {
      n[0] !== '0' ? words.push(`${single[n[0]]} hundred`) : null
      n = !(n[1] === '0' && n[2] === '0') ? n.slice(1) : ''
    }
    else if (n.length === 2) {
      handleTwoDigits(n)
      n = ''
    }
    else if (n.length === 1) {
      words.push(single[n])
      n = ''
    }
  }
  return words.join(' ')
}





