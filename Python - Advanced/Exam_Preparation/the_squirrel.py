collected = 0

size = int(input())
commands = input().split(", ")

field = []

start_position = ()

directions = {
    "up": (-1, 0),
    "down": (1, 0),
    "left": (0, -1),
    "right": (0, 1),
}

for i in range(size):
    field.append(list(input()))
    if "s" in field[i]:
        start_position = (i, field[i].index("s"))

for move in commands:
    row = start_position[0] + directions[move][0]
    col = start_position[1] + directions[move][1]

    if not (0 <= row < size and 0 <= col < size):
        print("The squirrel is out of the field.")
        break

    if field[row][col] == "t":
        print("Unfortunately, the squirrel stepped on a trap...")
        break

    if field[row][col] == "h":
        collected += 1
        field[row][col] = "*"

        if collected == 3:
            print("Good job! You have collected all hazelnuts!")
            break

    start_position = (row, col)

else:
    print("There are more hazelnuts to collect.")

print(f"Hazelnuts collected: {collected}")
