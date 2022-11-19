from functools import reduce

def check(n):
    return reduce(lambda a,b: a + b**2, [int(num) for num in str(n)], 0)

def is_happy(n):
    used = {}
    while True:
        next = check(n)
        if next == 1:
            return True
        if next in used:
          return False
        used[next] = True
        n = next


