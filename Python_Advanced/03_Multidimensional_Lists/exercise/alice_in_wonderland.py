n = int(input())

alice_pos = []
matrix = []
bags_collected = 0

directions = {
    "up": (-1, 0),
    "down": (1, 0),
    "left": (0, -1),
    "right": (0, 1),
}

for i in range(n):
    matrix.append(input().split())

    if "A" in matrix[i]:
        alice_pos = [i, matrix[i].index("A")]
        matrix[i][alice_pos[1]] = "*"

while bags_collected < 10:
    command = input()

    row = alice_pos[0] + directions[command][0]
    col = alice_pos[1] + directions[command][1]

    if not (0 <= row < n and 0 <= col < n):
        break

    alice_pos = [row, col]
    element = matrix[row][col]
    matrix[row][col] = "*"

    if element == "R":
        break

    if element.isdigit():
        bags_collected += int(element)

if bags_collected >= 10:
    print("She did it! She went to the party.")
else:
    print("Alice didn't make it to the tea party.")

[print(*row) for row in matrix]
