
def second_correct_passphrases(filename):
    passphrases = []
    counter = 0
    list_of_letters = []
    with open(filename, 'r') as f:
        for line in f.readlines():
            passphrases.append(line.strip())
    for i in range(len(passphrases)):
        passphrases[i] = passphrases[i].split()
    for n in range(len(passphrases)):
        list_of_letters.append([])
        for i in range(len(passphrases[n])):
            list_of_letters[n].append(tuple(sorted([letter for letter in passphrases[n][i]])))
    for i in range(len(list_of_letters)):
        if len(set(list_of_letters[i])) == len(list_of_letters[i]):
            counter += 1
    return counter


print(second_correct_passphrases('day4_input.txt'))
