
def sum_squares(p_input):
    values = [(0, 0, 1)]
    directions = [(0, 1), (-1, 0), (0, -1), (1, 0)]
    level = 1
    x, y = 0, 0
    while True:
        for direction in range(4):
            dirX, dirY = directions[direction]
            if direction == 0:
                moveN = level - 2
            elif direction in [1, 2]:
                moveN = level - 1
            else:
                moveN = level
            for i in range(moveN):
                x += dirX
                y += dirY
                new = []
                for value in values:
                    if abs(x - value[0]) <= 1 and abs(y - value[1]) <= 1:
                        new.append(value[2])
                values.append((x, y, sum(new)))
                if sum(new) >= p_input:
                    return sum(new)
        level += 2

print(sum_squares(312051))
