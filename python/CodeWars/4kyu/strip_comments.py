# https://www.codewars.com/kata/51c8e37cee245da6b40000bd/train/python

# Complete the solution so that it strips all text that follows any of a set of comment markers passed in. Any whitespace at the end of the line should also be stripped out.

# Example:

# Given an input string of:

# apples, pears # and bananas
# grapes
# bananas !apples
# The output expected would be:

# apples, pears
# grapes
# bananas
# The code would be called like so:

# result = solution("apples, pears # and bananas\ngrapes\nbananas !apples", ["#", "!"])
# result should == "apples, pears\ngrapes\nbananas"


def strip_comments(strng, markers):
    strng = strng.split('\n')
    for i, line in enumerate(strng):
        for marker in markers:
            if marker in line:
                line = line[:line.index(marker)]
        strng[i] = line.rstrip()
    return "\n".join(strng)