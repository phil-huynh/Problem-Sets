# https://www.codewars.com/kata/645e541f3e6c2c0038a01216/train/python

# Given a train track with some trains on it, then the same train track after some time has passed, return True if the arrangement is valid, otherwise return False.

# For example, this is valid:

# before: ">....."
# after:  ".....>"
# In this example, a train is facing right. In the before time, it is at the beginning of the track. Then by the after time, it has traveled to the end of the track.

# Input format:

# Input shall consist of a string containing 3 characters:
# > indicates a train traveling right
# < indicates a train traveling left
# . indicates a space - a stretch of empty track.
# Requirements:

# trains cannot change direction
# before: "..>.."
# after:  "..<.."
# trains cannot go backward
# before: "..>.."
# after:  ">...."
# train track cannot change length
# before: "..>.."
# after:  "........>"
# trains cannot be created or destroyed
# before: "..>.."
# after:  "..>>.."
# trains cannot enter or leave the given section of train track
# before: "..>.."
# after:  "....."
# trains cannot go past one another
# before: "..><.."
# after:  "<....>"
# Performance expectation:

# Solution should work for strings of upto 30k characters.
# FAQ:

# Can we have longer trains?
# No, not really. Doesn't make a difference for this problem. <<< is just 3 trains, not one long train.

def create_cache(track):
    cache, cars = {}, []
    for i, char in enumerate(track):
        if char != ".":
            cache[char] = [i] if not cache.get(char) else cache[char] + [i]
            cars.append(char)
    return cache, "".join(cars)

def is_valid_train_arrangement(before, after):
    cache1, cars1 = create_cache(before)
    cache2, cars2 = create_cache(after)
    if cars1 != cars2 or len(before) != len(after):
        return False
    for train in cache1:
        if list(cache1.keys()) != list(cache2.keys()) or \
            len(cache1[train]) != len(cache2[train]):
            return False
        for j, car in enumerate(cache1[train]):
            if train == "<" and cache1[train][j] < cache2[train][j] or \
                train == ">" and cache1[train][j] > cache2[train][j]:
                return False
    return True