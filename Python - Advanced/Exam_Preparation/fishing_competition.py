n = int(input())

matrix = []
position = []

directions = {
    "up": (-1, 0),
    "down": (1, 0),
    "left": (0, -1),
    "right": (0, 1),
}

for i in range(n):
    matrix.append(list(input()))

    if "S" in matrix[i]:
        position = [i, matrix[i].index("S")]
        matrix[i][matrix[i].index("S")] = "-"

tons_of_fish = 0

while True:
    command = input()
    if command == "collect the nets":
        break

    position[0] += directions[command][0]
    position[1] += directions[command][1]

    if position[0] == n:
        position[0] = 0
    elif position[0] == -1:
        position[0] = n - 1
    elif position[1] == n:
        position[1] = 0
    elif position[1] == -1:
        position[1] = n - 1

    if matrix[position[0]][position[1]] == "W":
        print(f"You fell into a whirlpool! The ship sank and you lost the fish you caught. "
              f"Last coordinates of the ship: [{position[0]},{position[1]}]")
        exit()
    elif matrix[position[0]][position[1]].isdigit():
        tons_of_fish += int(matrix[position[0]][position[1]])
        matrix[position[0]][position[1]] = "-"

matrix[position[0]][position[1]] = "S"

if tons_of_fish >= 20:
    print("Success! You managed to reach the quota!")
else:
    print(f"You didn't catch enough fish and didn't reach the quota! "
          f"You need {20 - tons_of_fish} tons of fish more.")

if tons_of_fish > 0:
    print(f"Amount of fish caught: {tons_of_fish} tons.")

for row in matrix:
    print("".join(row))
