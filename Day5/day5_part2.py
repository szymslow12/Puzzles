def steps_2(filename):
    input_numbers = []
    with open(filename, 'r') as f:
        for line in f.readlines():
            input_numbers.append(int(line.strip()))
    position = 0
    end_position = len(input_numbers)
    sum_of_steps = 0
    while 0 <= position < len(input_numbers):
            step = position
            position += input_numbers[position]
            if input_numbers[step] >= 3:
                input_numbers[step] -= 1
            else:
                input_numbers[step] += 1
            sum_of_steps += 1
    return sum_of_steps


print(steps_2('day5_input.txt'))
