rows = int(input())

matrix = [[int(x) for x in input().split()] for _ in range(rows)]

while True:

    command = input()

    if command == "END":
        break

    to_do, row, col, value = command.split()

    if not (0 <= int(row) <= rows - 1 and 0 <= int(col) <= len(matrix[0]) - 1):
        print("Invalid coordinates")
    elif to_do == "Add":
        matrix[int(row)][int(col)] += int(value)
    elif to_do == "Subtract":
        matrix[int(row)][int(col)] -= int(value)

for sub in matrix:
    print(*sub)
