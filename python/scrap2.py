from pprint import pprint

array = []

def remove_duplicates(arr):
    result = []
    if arr:
        cache = {}
        for num in arr:
            if num not in cache:
                cache[num] = True
        for num in arr:
            if cache.get(num):
                result.append(num)
                cache[num] = []



print(remove_duplicates(array))