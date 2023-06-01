# https://www.codewars.com/kata/58ae6ae22c3aaafc58000079/train/python

# Write a function that will check whether ANY permutation of the characters of the input string is a palindrome. Bonus points for a solution that is efficient and/or that uses only built-in language functions. Deem yourself brilliant if you can come up with a version that does not use any function whatsoever.

# Example
# madam -> True
# adamm -> True
# junk -> False

# Hint
# The brute force approach would be to generate all the permutations of the string and check each one of them whether it is a palindrome. However, an optimized approach will not require this at all.

def permute_a_palindrome(input):
    cache, odds = {}, []
    for letter in input:
        if not cache.get(letter.lower()):
            cache[letter.lower()] = 0
        cache[letter.lower()] += 1
    for key in cache:
        if cache[key] % 2 != 0:
            odds.append(key)
    return True if len(odds) <= 1 else False