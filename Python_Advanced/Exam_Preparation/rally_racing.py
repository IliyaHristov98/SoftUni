n = int(input())
car_number = input()

matrix = []
tunnels = []

for i in range(n):
    matrix.append(input().split())

    for t in matrix[i]:
        if t == "T":
            tunnels.append((i, matrix[i].index("T")))

directions = {
    "up": (-1, 0),
    "down": (1, 0),
    "left": (0, -1),
    "right": (0, 1),
}

passed_kms = 0
position = (0, 0)

while True:
    command = input()

    if command == "End":
        print(f"Racing car {car_number} DNF.")
        break

    new_row = position[0] + directions[command][0]
    new_col = position[1] + directions[command][1]
    position = (new_row, new_col)

    if matrix[new_row][new_col] == ".":
        passed_kms += 10
    elif matrix[new_row][new_col] == "F":
        passed_kms += 10
        print(f"Racing car {car_number} finished the stage!")
        break
    elif matrix[new_row][new_col] == "T":
        if new_row == tunnels[0][0] and new_col == tunnels[0][1]:
            new_row, new_col = tunnels[1][0], tunnels[1][1]
        else:
            new_row, new_col = tunnels[0][0], tunnels[0][1]

        position = (new_row, new_col)
        passed_kms += 30
        matrix[tunnels[0][0]][tunnels[0][1]] = "."
        matrix[tunnels[1][0]][tunnels[1][1]] = "."

matrix[position[0]][position[1]] = "C"

print(f"Distance covered {passed_kms} km.")

for row in matrix:
    print("".join(row))
