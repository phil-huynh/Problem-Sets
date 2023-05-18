# https://www.codewars.com/kata/52597aa56021e91c93000cb0/train/python

# Write an algorithm that takes an array and moves all of the zeros to the end, preserving the order of the other elements.
# move_zeros([1, 0, 1, 2, 0, 1, 3])  returns [1, 1, 2, 1, 3, 0, 0]


def move_zeros(lst):
    zeros, non_zeros = [], []
    [zeros.append(num) if num == 0 else non_zeros.append(num) for num in lst]
    return non_zeros + zeros

print(move_zeros([1,2,3,4,0,6,0,5,4,5,0,0,9]))































