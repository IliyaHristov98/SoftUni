n = int(input())

matrix = []

for _ in range(n):
    matrix.append(list(input()))

symbol = input()

for row in range(n):
    for col in range(n):
        if matrix[row][col] == symbol:
            print(f"({row}, {col})")
            exit()
else:
    print(f"{symbol} does not occur in the matrix")
