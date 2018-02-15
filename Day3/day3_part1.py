
def get_manhattan_distance(value):
    ring_delta = 8
    corner_delta = 2
    for i in range(1):
        input_value = value
        cursor = 1
        ring = 0
        corner = 0
        manhattan_distance = 0
        while cursor < input_value:
            manhattan_distance += 1
            ring += ring_delta
            corner += corner_delta
            cursor += ring
        while cursor > input_value:
            cursor -= corner
        cursor = int(cursor + 0.5 * corner)
        distance = cursor - input_value
        manhattan_distance += distance
        return manhattan_distance

print(get_manhattan_distance(312051))
