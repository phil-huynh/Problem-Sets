# Snail Sort
# Given an n x n array, return the array elements arranged from outermost elements to the middle element, traveling clockwise.

# array = [[1,2,3],
#          [4,5,6],
#          [7,8,9]]
# snail(array) #=> [1,2,3,6,9,8,7,4,5]
# For better understanding, please follow the numbers of the next array consecutively:

# array = [[1,2,3],
#          [8,9,4],
#          [7,6,5]]
# snail(array) #=> [1,2,3,4,5,6,7,8,9]
# This image will illustrate things more clearly:

# NOTE: The idea is not sort the elements from the lowest value to the highest; the idea is to traverse the 2-d array in a clockwise snailshell pattern.

# NOTE 2: The 0x0 (empty matrix) is represented as en empty array inside an array [[]].

def snail(snail_map):
    snail_array = []
    top, bottom = 0, len(snail_map)
    left, right = 0, len(snail_map[0])

    while top < bottom and left < right:

        [snail_array.append(snail_map[top][i]) for i in range(left, right)]
        top += 1

        [snail_array.append(snail_map[j][right - 1]) for j in range(top, bottom)]
        right -= 1

        if top < bottom:
            [snail_array.append(snail_map[bottom -1][k]) for k in range(right - 1, left - 1, -1)]
            bottom -= 1

        if left < right:
            [snail_array.append(snail_map[l][left]) for l in range(bottom - 1, top - 1, -1)]
            left += 1

    return snail_array