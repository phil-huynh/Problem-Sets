all_digits = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]


def list_to_number(array):
    return int("".join([str(num) for num in array]))


def get_highest(sum_dig, digs):
    top_array = [sum_dig//digs for i in range(digs)]
    left_to_spread = sum_dig % digs
    index = len(top_array) - 1
    while left_to_spread:
        top_array[index] += 1
        index -= 1
        left_to_spread -=1
    return top_array


def search(length, run_sum, final_sum, current, results):
    if run_sum > final_sum:
        return
    if len(current) == length and run_sum == final_sum:
        final_num = list_to_number(current)
        results.insert(0, final_num)
        return
    else:
        if len(current) < length:
            available_nums = all_digits[current[-1]:]
            available_nums.reverse()
            leftover_spaces = length - len(current)
            for num in available_nums:
                if num * leftover_spaces <= final_sum - run_sum:
                    run_sum += num
                    current.append(num)
                    search(length, run_sum, final_sum, current, results)
                    current.pop()
                    run_sum -= num


def find_all(sum_dig, digs):
    if sum_dig/digs > 9:
        return []
    upper = get_highest(sum_dig, digs)
    length =  sum_dig
    start = upper[0]
    results = []
    for num in range(start, 0, -1):
        search(digs, num, length, [num], results)
    if not results:
        return []
    return [len(results), results[0], results[-1]]


