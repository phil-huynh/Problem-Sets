# Consider a "word" as any sequence of capital letters A-Z (not limited to just "dictionary words"). For any word with at least two different letters, there are other words composed of the same letters but in a different order (for instance, STATIONARILY/ANTIROYALIST, which happen to both be dictionary words; for our purposes "AAIILNORSTTY" is also a "word" composed of the same letters as these two).

# We can then assign a number to every word, based on where it falls in an alphabetically sorted list of all words made up of the same group of letters. One way to do this would be to generate the entire list of words and find the desired one, but this would be slow if the word is long.

# Given a word, return its number. Your function should be able to accept any word 25 letters or less in length (possibly with some letters repeated), and take no more than 500 milliseconds to run. To compare, when the solution code runs the 27 test cases in JS, it takes 101ms.

# For very large words, you'll run into number precision issues in JS (if the word's position is greater than 2^53). For the JS tests with large positions, there's some leeway (.000000001%). If you feel like you're getting it right for the smaller ranks, and only failing by rounding on the larger, submit a couple more times and see if it takes.

# Python, Java and Haskell have arbitrary integer precision, so you must be precise in those languages (unless someone corrects me).

# C# is using a long, which may not have the best precision, but the tests are locked so we can't change it.

# Sample words, with their rank:
# ABAB = 2
# AAAB = 1
# BAAA = 4
# QUESTION = 24572
# BOOKKEEPER = 10743


from math import factorial

def get_factorial(num, ref):
    if num in ref:
        result = ref[num]
    else:
        result = factorial(num)
        ref[num] = result
    return result

def listPosition(word):
    checker = {}
    factorials = {}
    for letter in word:
        if letter not in checker:
            checker[letter] = 1
        else:
            checker[letter] += 1
    order = [key for key in checker]
    order.sort()

    def get_number(word, total):
        if len(word) == 1:
            total += 1
            return total
        numerator = get_factorial(len(word) - 1, factorials)
        ref = checker.copy()
        order = [key for key in ref]
        order.sort()
        current_letter = word[0]
        for letter in order:
            ref[letter] -= 1
            denominator = 1
            if letter == current_letter:
                checker[letter] -= 1
                if checker[letter] == 0:
                    del checker[letter]
                return get_number(word[1:], total)
            else:
                for key in ref:
                    if ref[key] > 0:
                        denominator *= get_factorial(ref[key], factorials)
            combos = numerator//denominator
            total += combos
            ref[letter] += 1

    final_num = get_number(word, 0)
    return final_num

print(listPosition("A"))
print(listPosition("ABAB"))
print(listPosition("AAAB"))
print(listPosition("BAAA"))
print(listPosition("QUESTION"))
print(listPosition("BOOKKEEPER"))

