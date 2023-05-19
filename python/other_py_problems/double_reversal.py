def reverse_int(num, total):
    if (num < 10):
        total += num
        return total
    else:
        ones_place = num % 10
        total += ones_place
        total *= 10
        new_num = (num - ones_place)//10
        return reverse_int(new_num, total)


def is_double_reversible(num):
    double_rev = reverse_int(reverse_int(num, 0), 0)
    if double_rev == num:
        return True
    return False


print(is_double_reversible(1234))
print(is_double_reversible(2340))



