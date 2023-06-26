# https://www.codewars.com/kata/545cedaa9943f7fe7b000048/train/python

# A pangram is a sentence that contains every single letter of the alphabet at least once. For example, the sentence "The quick brown fox jumps over the lazy dog" is a pangram, because it uses the letters A-Z at least once (case is irrelevant).

# Given a string, detect whether or not it is a pangram. Return True if it is, False if not. Ignore numbers and punctuation.

def is_pangram(s):
    alphabet = [letter for letter in "abcdefghijklmnopqrstuvwxyz"]
    cache = {char.lower(): True for char in s}
    for letter in alphabet:
        if not cache.get(letter):
            return False
    return True