from pprint import pprint

def snail(snail_map):

    def move_left(x, y):
        return (x, y-1)

    def move_right(x, y):
        return (x, y+1)

    def move_up(x, y):
        return (x-1, y)

    def move_down(x, y):
        return (x+1, y)

    def in_bounds(x, y):
        return (0 <= x < len(snail_map)) and (0 <= y < len(snail_map))

    position = (0, 0)
    result = []
    moves = [move_right, move_down, move_left, move_up]

    move = 0
    while len(result) != len(snail_map)**2:


        if snail_map[position[0]][position[1]]:
            curr_val = snail_map[position[0]][position[1]]
            result.append(curr_val)
            snail_map[position[0]][position[1]] = None

            next_step = moves[move%4](position[0], position[1])
            if not in_bounds(next_step[0], next_step[1]):
                move += 1
            position = moves[move%4](position[0], position[1])
            next_step = position


        else:
            move += 1

    return result

array = [[1,2,3],
         [4,5,6],
         [7,8,9]]

print(snail(array))