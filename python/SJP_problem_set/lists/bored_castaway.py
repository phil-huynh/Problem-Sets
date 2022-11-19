def tide_difference(measurements):
    low = min(measurements)
    high = max(measurements)
    i = measurements.index(low)
    j = measurements.index(high)
    if i > j:
        return None
    nums = measurements[i:j]
    for i, num in enumerate(nums):
        if i == len(nums) - 1:
            break
        if num > nums[i + 1]:
            return None
    return high - low