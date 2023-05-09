# The principle of spiral permutation consists in concatenating the different characters of a string in a spiral manner starting with the last character (last character, first character, character before last character, second character, etc.).

# This principle is illustrated by the example below, which for a starting string "ABCDE" formed of 5 letters and after 4 spiral permutations, the string "BDECA" is obtained. The 5th spiral permutation allows to find the starting string.

# Task
# Write a function that given a string s return an array of all the distinct possible permutations.

# The elements of the resulting array are ordered and added sequentially, meaning arr[1] is generated from arr[0], arr[2] is generated from arr[1] and so on.

# Examples
# spiralPermutations("ABCDE")
# //=> ["ABCDE","EADBC","CEBAD","DCAEB","BDECA"]
# // given "ABCDE" we can generate fellowing permutation by concatenating the following letters
# // "E" + "A"  (last char + first)
# // "D" + "B"  (4th char + 2nd char)
# // "C"        (middle or 3rd char)
# // ==> "EADBC"
# spiralPermutations("ABABA")
# //=> ["ABABA","AABBA","AABAB","BAAAB","BBAAA"]
# spiralPermutations('HLORRSGXRV')
# //=> ['HLORRSGXRV','VHRLXOGRSR','RVSHRRGLOX','XROVLSGHRR','RXRRHOGVSL','LRSXVRGROH' ]
# spiralPermutations('MAAMAAA')
# //=> ["MAAMAAA","AMAAAAM"]
# spiralPermutations('XXXXX')
# //=> ['XXXXX']


def spiral_permutations(s):
    result, current, complete, checker = [s], s, False, {s:True}
    while not complete:
        string, i, j = "", 0, len(current) - 1
        while i <= j:
            string += current[i] if i == j else f"{current[j]}{current[i]}"
            i += 1
            j -= 1
        if string not in checker:
            checker[string] = True
            result.append(string)
            current = string
        else:
            complete = True
    return result