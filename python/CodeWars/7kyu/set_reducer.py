# These arrays are too long! Let's reduce them!

# Description
# Write a function that takes in an array of integers from 0-9, and returns a new array:

# Numbers with no identical numbers preceding or following it returns a 1: 2, 4, 9  => 1, 1, 1
# Sequential groups of identical numbers return their count: 6, 6, 6, 6 => 4
# Example

# [0, 4, 6, 8, 8, 8, 5, 5, 7] => [1, 1, 1, 3, 2, 1]

# Your function should then repeat the process on the resulting array, and on the resulting array of that, until it returns a single integer:

# [0, 4, 6, 8, 8, 8, 5, 5, 7] =>  [1, 1, 1, 3, 2, 1] => [3, 1, 1, 1] => [1, 3] => [1, 1] => [2]

# When your function has reduced the array to a single integer following these rules, it should return that integer.

# [2] => 2

# Rules and assertions
# All test arrays will be 2+ in length
# All integers in the test arrays will be positive numbers from 0 - 9
# You should return an integer, not an array with 1 element
# Visual example
# Example of the flow of the algorithm



def set_reducer(inp):
    while len(inp) > 1:
        storage, next = [inp[0]], []
        for i, item in enumerate(inp):
            if i == len(inp) - 1:
                if item == storage[0]:
                    storage.append(item)
                    next.append(len(storage))
                else:
                    next.append(len(storage))
                    next.append(1)
            elif i > 0:
                if item == storage[0]:
                    storage.append(item)
                else:
                    next.append(len(storage))
                    storage = [item]
        inp = next
    return inp[0]



print(set_reducer([0, 4, 6, 8, 8, 8, 5, 5, 7]))
# print(set_reducer([8, 1, 6, 1, 2, 7, 7, 7, 7, 6, 5, 3, 2, 1, 8]))
# print(set_reducer([0, 0, 8, 6, 6, 7, 8, 6, 6, 4, 7, 6, 4, 0, 1, 1, 2, 1, 2, 9, 9, 0, 3, 3, 0, 4]))
# print(set_reducer([6, 3, 5, 7, 4, 2, 0, 0, 1, 6, 9, 6, 1, 3, 9, 3, 2]))
# print(set_reducer([1, 4, 0, 1, 2, 6, 6, 0, 8, 4, 7, 9, 9, 4, 3, 7, 2, 6, 7, 5, 0, 9, 8]))
# print(set_reducer([4, 6, 8, 1, 9, 3, 8, 4, 1, 4, 0, 8, 3, 7, 1, 5, 6, 3, 2, 1, 8, 4, 9]))
# print(set_reducer([8, 3, 2, 6, 2, 7, 9, 9, 6, 8, 2, 4, 3, 6, 9, 5, 2, 4, 9]))
# print(set_reducer([7, 2, 0, 6, 5, 7, 3, 9, 1, 8, 4, 5, 5, 5, 8, 9, 8, 1, 9, 1, 2, 7, 2, 6, 0, 8, 0, 2]))
# print(set_reducer([8, 5, 1, 1, 1, 5, 9, 7, 4, 8, 8, 8, 2, 4, 3, 1, 2, 1, 3, 5, 6, 4]))
# print(set_reducer([2, 4, 4, 6, 2, 1, 1, 5, 6, 7, 8, 8, 8, 8, 9, 0, 1, 1, 5, 4, 4]))