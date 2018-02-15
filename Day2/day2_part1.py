def spreadsheets_checksum(filename):
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
        a = max(spread)
        b = min(spread)
        to_sum_list.append(a - b)
    return sum(to_sum_list)

print(spreadsheets_checksum('spreadsheets.txt'))
