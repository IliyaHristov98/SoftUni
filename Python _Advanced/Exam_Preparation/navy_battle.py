n = int(input())

field = []

position = None

direction = {
    "up": (-1, 0),
    "down": (1, 0),
    "left": (0, -1),
    "right": (0, 1),
}

mines_hit = 3
cruisers_hit = 3

for i in range(n):
    field.append(list(input()))

    if "S" in field[i]:
        position = (i, field[i].index("S"))
        field[position[0]][position[1]] = "-"

while True:
    command = input()

    field[position[0]][position[1]] = "-"

    new_row = position[0] + direction[command][0]
    new_col = position[1] + direction[command][1]

    if field[new_row][new_col] == "*":
        mines_hit -= 1
    elif field[new_row][new_col] == "C":
        cruisers_hit -= 1

    field[new_row][new_col] = "S"
    position = (new_row, new_col)

    if mines_hit == 0:
        print(f"Mission failed, U-9 disappeared! Last known coordinates [{new_row}, {new_col}]!")
        break
    elif cruisers_hit == 0:
        print("Mission accomplished, U-9 has destroyed all battle cruisers of the enemy!")
        break

print("\n".join("".join(row) for row in field))
