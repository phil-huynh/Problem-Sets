from math import factorial

def get_factorial(num, ref):
    if num in ref:
        result = ref[num]
    else:
        result = factorial(num)
        ref[num] = result
    return result

def listPosition(word):
    checker = {}
    factorials = {}
    for letter in word:
        if letter not in checker:
            checker[letter] = 1
        else:
            checker[letter] += 1
    order = [key for key in checker]
    order.sort()

    def get_number(word, total):
        if len(word) == 1:
            total += 1
            return total
        numerator = get_factorial(len(word) - 1, factorials)
        ref = checker.copy()
        order = [key for key in ref]
        order.sort()
        current_letter = word[0]
        for letter in order:
            ref[letter] -= 1
            denominator = 1
            if letter == current_letter:
                checker[letter] -= 1
                if checker[letter] == 0:
                    del checker[letter]
                return get_number(word[1:], total)
            else:
                for key in ref:
                    if ref[key] > 0:
                        denominator *= get_factorial(ref[key], factorials)
            combos = numerator//denominator
            total += combos
            ref[letter] += 1

    final_num = get_number(word, 0)
    return final_num

print(listPosition("A"))
print(listPosition("ABAB"))
print(listPosition("AAAB"))
print(listPosition("BAAA"))
print(listPosition("QUESTION"))
print(listPosition("BOOKKEEPER"))

