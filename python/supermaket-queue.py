def queueTime(customers, n):
    lines = []
    [lines.append(0) for num in range(n)]
    for customer in customers:
        lines[0] += customer
        lines.sort()
    return max(lines)




  # for i, customers in enumerate(customers):

print(queueTime([5,3,4], 1))
print(queueTime([10,2,3,3], 2))
print(queueTime([2,3,10], 2))
print(queueTime([2,2,3,3,4,4], 2))