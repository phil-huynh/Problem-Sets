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
    if '\n' in strng:
        strng = strng.split('\n')
    else:
        strng = [strng]
    for i, line in enumerate(strng):
        for j, char in enumerate(line):
            if char in markers:
                strng[i] = line[:j].rstrip()
                break
    return "\n".join(strng) if len(strng) > 1 else strng[0]