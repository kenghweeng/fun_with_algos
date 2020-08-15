def dp_choose(n, k):
    # n + 1 rows, k + 1 columns
    row = [1] * (k + 1)
    table = []

    for i in range(n + 1):
        table.append(row.copy())

    for j in range(1, k + 1):
        table[0][j] = 0

    for i in range(1, n + 1):
        for j in range(1, k + 1):
            table[i][j] = table[i - 1][j] + table[i - 1][j - 1]

    return table[n][k]

print(dp_choose(8,4))
