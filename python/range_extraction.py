def solution(args):
    index, result, storage = 1, "", [args[0]]
    while index < len(args):
        if args[index] == storage[-1] + 1:
            storage.append(args[index])
        else:
            if len(storage) >= 3:
                result += f"{storage[0]}-{storage[-1]},"
            elif len(storage) == 2:
                result += f"{storage[0]},{storage[1]},"
            else:
                result += f"{storage[0]},"
            storage = [args[index]]
        index += 1
    if len(storage) >= 3:
        result += f"{storage[0]}-{storage[-1]}"
    elif len(storage) == 2:
        result += f"{storage[0]},{storage[1]}"
    else:
        result += f"{storage[0]}"
    return result