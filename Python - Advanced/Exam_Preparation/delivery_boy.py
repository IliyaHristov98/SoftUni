r, c = [int(x) for x in input().split()]

matrix = []
starting_position = []

directions = {
    "up": (-1, 0),
    "down": (1, 0),
    "left": (0, -1),
    "right": (0, 1),
}

for i in range(r):
    matrix.append(list(input()))

    if "B" in matrix[i]:
        starting_position = [i, matrix[i].index("B")]

current_position = [starting_position[0], starting_position[1]]

while True:
    command = input()

    current_position[0] += directions[command][0]
    current_position[1] += directions[command][1]

    if not (0 <= current_position[0] < r and 0 <= current_position[1] < c):
        print("The delivery is late. Order is canceled.")
        matrix[starting_position[0]][starting_position[1]] = " "
        break

    if matrix[current_position[0]][current_position[1]] == "*":
        current_position[0] -= directions[command][0]
        current_position[1] -= directions[command][1]
        continue

    if matrix[current_position[0]][current_position[1]] == "-":
        matrix[current_position[0]][current_position[1]] = "."
    elif matrix[current_position[0]][current_position[1]] == "P":
        print("Pizza is collected. 10 minutes for delivery.")
        matrix[current_position[0]][current_position[1]] = "R"
    elif matrix[current_position[0]][current_position[1]] == "A":
        print("Pizza is delivered on time! Next order...")
        matrix[current_position[0]][current_position[1]] = "P"
        break

for row in matrix:
    print("".join(row))
