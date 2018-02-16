def redistibute_banks(filename):
    banks = []
    with open(filename, 'r') as f:
        for bank in f.readlines():
            banks.append(bank.strip().split('\t'))
    for bank in banks:
        for i in range(len(bank)):
            bank[i] = int(bank[i])
    states = [banks[0]]
    cycle = 0
    while True:
        new_state = [block for block in states[-1]]
        cycle += 1
        position = new_state.index(max(new_state))
        blocks = new_state[position]
        new_state[position] = 0
        while blocks > 0:
            position = (position + 1) % len(new_state)
            new_state[position] += 1
            blocks -= 1
        if new_state in states:
            return cycle - states.index(new_state)
        else:
            states.append(new_state)


print(redistibute_banks('day6_input.txt'))
