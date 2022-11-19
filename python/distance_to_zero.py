def closest_to_zero(nums):
    closest = nums[0]
    for num in nums[1:]:
        if num < 0:
            if abs(num) < abs(closest):
                closest = num
        else:
            if num <= abs(closest):
                closest = num
    return closest


# print(closest_to_zero([3, -2]))
# print(closest_to_zero([-4, 3]))
# print(closest_to_zero([2, -2]))
# print(closest_to_zero([4, -2, 1]))