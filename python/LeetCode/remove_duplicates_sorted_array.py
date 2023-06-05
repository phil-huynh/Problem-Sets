def removeDuplicates(nums):
    cache, indices = {}
    for num in nums:
        if num not in cache:
            cache[num] = 0
        cache[num] += 1
    for i in range(len(nums)-1, -1, -1):
        if nums[i] in cache and cache[nums[i]] > 1:
            indices.append(i)
            cache[nums[i]] -= 1
    for j in indices:
        nums.pop(j)
    return len(nums)


print(removeDuplicates([1,1,2]))