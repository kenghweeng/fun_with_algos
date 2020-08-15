def faster_pascal(row, col):
    table = []
    for i in range(row):
        row_list = [1] * (i + 1)
        table.append(row_list.copy())

    for i in range(2, row):
        for j in range(1, i):
            table[i][j] = table[i-1][j] + table[i-1][j-1]

    return table[row - 1][col - 1]

print(faster_pascal(800,799))
