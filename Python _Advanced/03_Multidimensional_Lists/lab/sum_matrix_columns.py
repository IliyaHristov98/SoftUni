row, col = [int(x) for x in input().split(", ")]

matrix = []

for _ in range(row):
    matrix.append([int(x) for x in input().split()])

for col_index in range(col):
    col_total = 0
    for row_index in range(row):
        col_total += matrix[row_index][col_index]
    print(col_total)
