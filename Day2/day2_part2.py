def spreadsheets_divison(filename):
    spreads = []
    to_sum_list = []
    with open(filename, 'r') as f:
        for row in f.readlines():
            spreads.append(row.strip())
    for i in range(len(spreads)):
        spreads[i] = spreads[i].split('\t')
    for i in range(len(spreads)):
        for a in range(len(spreads[i])): # a is an index of elements in spreads[i]
            spreads[i][a] = int(spreads[i][a])
    for spread in spreads:
        for i in range(len(spread)):
            for number in spread:
                if spread[i] % number == 0 and spread[i] != number:
                    to_sum_list.append(int(spread[i] / number))
    return sum(to_sum_list)















print(spreadsheets_divison('spreadsheets.txt'))
