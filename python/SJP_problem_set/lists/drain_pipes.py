def pipe_outputs(num_pipes, steps):
    pipes = []
    [pipes.append(8) for i in range(num_pipes)]
    for step in steps:
        if len(step) == 2:
            index = step[0] - 1
            flow = pipes[index]
            left = step[1]
            right = flow - left
            pipes.pop(step[0] - 1)
            pipes.insert(index, right)
            pipes.insert(index, left)
        if len(step) == 1:
            index = step[0] - 1
            left = pipes[index]
            right = pipes[step[0]]
            pipes.pop(step[0])
            pipes.pop(index)
            pipes.insert(index, left + right)
    return pipes

# 1
# [[1, 4], [2, 2], [1, 2]]
# 4
# [[2, 3], [4, 7], [1], [2], [3]]
# 3
# [[2], [1]]