# https://www.codewars.com/kata/5463c8db865001c1710003b2/train/python

# Write a method that takes a number and returns a string of that number in English.

# Your method should be able to handle any number between 0 and 99999. If the given number is outside of that range or not an integer, the method should return an empty string.

# Examples
# 0      -->  "zero"
# 27     -->  "twenty seven"
# 100    -->  "one hundred"
# 7012   -->  "seven thousand twelve"
# 99205  -->  "ninety nine thousand two hundred five"

from pprint import pprint

single= {
    "0": "zero",
    "1": "one",
    "2": "two",
    "3": "three",
    "4": "four",
    "5": "five",
    "6": "six",
    "7": "seven",
    "8": "eight",
    "9": "nine"
}

teens= {
    "0": "ten",
    "1": "eleven",
    "2": "twelve",
    "3": "thirteen",
    "4": "fourteen",
    "5": "fifteen",
    "6": "sixteen",
    "7": "seventeen",
    "8": "eighteen",
    "9": "nineteen"
}

tens_place= {
    "2": "twenty",
    "3": "thirty",
    "4": "forty",
    "5": "fifty",
    "6": "sixty",
    "7": "seventy",
    "8": "eighty",
    "9": "ninety"
}

def number_to_english(n):

    def handle_two_digits(n):
        if n[0] == "0":
            words.append(f"{single[n[1]]}")
        elif n[0] == "1":
            words.append(teens[n[1]])
        else:
            words.append(tens_place[n[0]])
            words.append(f"{single[n[1]]}") if n[1] != "0" else ""


    if n < 0 or n >= 100000 or len(str(n).split(".")) > 1:
        return ""
    n, words = str(n), []

    while n:
        if len(n) == 5:
            handle_two_digits(n[:2])
            words.append("thousand")
            n = n[2:]
        elif len(n) == 4:
            words.append(f"{single[n[0]]} thousand")
            n = n[2:] if n[1] == 0 else n[1:]
        elif len(n) == 3:
            words.append(f"{single[n[0]]} hundred") if n[0] != "0" else ""
            n = n[1:] if not (n[1] == "0" and n[2] == "0") else ""
        elif len(n) == 2:
            handle_two_digits(n)
            n = ""
        elif len(n) == 1:
            words.append(single[n])
            n = ""
    return " ".join(words)


print(number_to_english(50))