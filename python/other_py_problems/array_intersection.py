def intersection(nums):
    shortest = (nums[0])
    for group in nums:
        if len(group) < len(shortest):
            shortest = group

    shortest.sort()
    checker = dict.fromkeys(shortest, True)

    for array in nums:
        temp_check = dict.fromkeys(array, True)
        for key in checker:
            shared = temp_check.get(key)
            if not shared:
                checker[key] =False
    result = []
    for key in checker:
        if checker[key] == True:
            result.append(key)

    return result


print(intersection([[3,1,2,4,5],[1,2,3,4],[3,4,5,6]]))
