# https://www.codewars.com/kata/55c04b4cc56a697bb0000048/train/javascript

# Complete the function scramble(str1, str2) that returns true if a portion of str1 characters can be rearranged to match str2, otherwise returns false.

# Notes:

# Only lower case letters will be used (a-z). No punctuation or digits will be included.
# Performance needs to be considered.
# Examples
# scramble('rkqodlw', 'world') ==> True
# scramble('cedewaraaossoqqyt', 'codewars') ==> True
# scramble('katas', 'steak') ==> False

def scramble(s1, s2):
    check1, check2 = {}, {}
    for char in s1:
        check1[char] = check1[char] + 1 if char in check1 else 1
    for char in s2:
        check2[char] = check2[char] + 1 if char in check2 else 1
    for key in check2:
        if key not in check1 or check1.get(key) < check2.get(key):
            return False
    return True