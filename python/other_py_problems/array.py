def find_list_difference(nums1, nums2):
    nums1.sort()
    result = []
    checker = dict.fromkeys(nums2, True)

    for number in nums1:
        num1_in_num2 = checker.get(number)
        if not num1_in_num2:
            result.append(number)

    return result

print(find_list_difference([5, 2, 4, 3, 1], [4, 2]))


