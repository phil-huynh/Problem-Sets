def snail(snail_map):
    snail_array = []
    top = 0
    bottom = len(snail_map)
    left = 0
    right = len(snail_map[0])

    while top < bottom and left < right:

        [snail_array.append(snail_map[top][i]) for i in range(left, right)]
        top += 1

        [snail_array.append(snail_map[j][right - 1]) for j in range(top, bottom)]
        right -= 1

        if top < bottom:
            [snail_array.append(snail_map[bottom -1][k]) for k in range(right - 1, left - 1, -1)]
            bottom -= 1

        if left < right:
            [snail_array.append(snail_map[l][left]) for l in range(bottom - 1, top - 1, -1)]
            left += 1

    return snail_array










print(snail(
  [[1,2,3],
  [4,5,6],
  [7,8,9]]
  ))

print(snail([[1,2,3,4],[5,6,7,8],[9,10,11,12]]))