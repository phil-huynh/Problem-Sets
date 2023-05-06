# My friend John and I are members of the "Fat to Fit Club (FFC)". John is worried because each month a list with the weights of members is published and each month he is the last on the list which means he is the heaviest.

# I am the one who establishes the list so I told him: "Don't worry any more, I will modify the order of the list". It was decided to attribute a "weight" to numbers. The weight of a number will be from now on the sum of its digits.

# For example 99 will have "weight" 18, 100 will have "weight" 1 so in the list 100 will come before 99.

# Given a string with the weights of FFC members in normal order can you give this string ordered by "weights" of these numbers?

# Example:
# "56 65 74 100 99 68 86 180 90" ordered by numbers weights becomes:

# "100 180 90 56 65 74 68 86 99"
# When two numbers have the same "weight", let us class them as if they were strings (alphabetical ordering) and not numbers:

# 180 is before 90 since, having the same "weight" (9), it comes before as a string.

# All numbers in the list are positive numbers and the list can be empty.

# Notes
# it may happen that the input string have leading, trailing whitespaces and more than a unique whitespace between two consecutive numbers

from functools import reduce

def get_weight(num_str):
    if num_str:
        return reduce(lambda a, b: a + b, [int(num) for num in num_str])

def get_weight_list(string):
    nums = []
    cache = ""
    for char in string:
        if char != " ":
            cache += char
        else:
            if cache:
                nums.append(cache)
                cache = ""
    nums.append(cache)
    return nums

def create_weight_dict(weights):
    weight_dict = {}
    for weight in weights:
        w = get_weight(weight)
        if not weight_dict.get(w):
            weight_dict[w] = []
        weight_dict[w].append(weight)
    for key in weight_dict:
        weight_dict[key].sort()
        weight_dict[key] = " ".join(weight_dict[key])
    return weight_dict

def order_weight(string):
    weights = get_weight_list(string)
    weight_dict = create_weight_dict(weights)
    keys = list(weight_dict.keys())
    keys.sort()
    result = ""
    for i, key in enumerate(keys):
        if i == 0:
            result += weight_dict[key]
        else:
            result += f" {weight_dict[key]}"
    return result