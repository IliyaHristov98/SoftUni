def find_cheese(cupboard):
    for a in cupboard:
        if "C" in a:
            return True


r, c = [int(x) for x in input().split(",")]

matrix = []
position = []

directions = {
    "up": (-1, 0),
    "down": (1, 0),
    "left": (0, -1),
    "right": (0, 1),
}

for i in range(r):
    matrix.append(list(input()))
    if "M" in matrix[i]:
        position = [i, matrix[i].index("M")]
        matrix[position[0]][position[1]] = "*"

while True:
    command = input()

    if command == "danger":
        if find_cheese(matrix):
            print("Mouse will come back later!")
        break

    row = position[0] + directions[command][0]
    col = position[1] + directions[command][1]

    if not (0 <= row < r and 0 <= col < c):
        print("No more cheese for tonight!")
        matrix[position[0]][position[1]] = "M"
        break

    if matrix[row][col] == "@":
        continue

    if matrix[row][col] == "T":
        matrix[row][col] = "M"
        print("Mouse is trapped!")
        break

    if matrix[row][col] == "C":
        matrix[row][col] = "*"
        if not find_cheese(matrix):
            print("Happy mouse! All the cheese is eaten, good night!")
            matrix[row][col] = "M"
            break

    position = [row, col]

for y in matrix:
    print("".join(y))
