
def correct_passphrases(filename):
    passphrases = []
    counter = 0
    with open(filename, 'r') as f:
        for line in f.readlines():
            passphrases.append(line.strip())
    for i in range(len(passphrases)):
        passphrases[i] = passphrases[i].split()
    for passphrase in passphrases:
        if all(passphrase.count(phrase) == 1 for phrase in passphrase):
            counter += 1
    return counter


print(correct_passphrases('day4_input.txt'))
