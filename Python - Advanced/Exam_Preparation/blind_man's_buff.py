n, m = [int(x) for x in input().split()]

playground = []
start_position = ()

directions = {
    "up": (-1, 0),
    "down": (1, 0),
    "left": (0, -1),
    "right": (0, 1),
}

moves = 0
touched = 0

for i in range(n):
    playground.append(input().split())
    if "B" in playground[i]:
        start_position = (i, playground[i].index("B"))

command = input()

while command != "Finish":
    row = start_position[0] + directions[command][0]
    col = start_position[1] + directions[command][1]

    if not (0 <= row < n and 0 <= col < m) or playground[row][col] == "O":
        command = input()
        continue

    if playground[row][col] == "P":
        touched += 1
        playground[row][col] = "-"

    moves += 1

    if touched == 3:
        break

    start_position = (row, col)

    command = input()

print(f"Game over!\nTouched opponents: {touched} Moves made: {moves}")
