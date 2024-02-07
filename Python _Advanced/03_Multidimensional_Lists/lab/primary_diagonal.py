n = int(input())

matrix = []
diagonal_total = 0

for _ in range(n):
    matrix.append([int(x) for x in input().split()])

for row in range(n):
    diagonal_total += matrix[row][row]

print(diagonal_total)
