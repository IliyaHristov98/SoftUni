def distribute_presents(presents_left: int, nice_kids_count: int):
    for direction in directions.values():
        r = santa_position[0] + direction[0]
        c = santa_position[1] + direction[1]

        if grid[r][c].isalpha():
            if grid[r][c] == "V":
                nice_kids_count += 1

            grid[r][c] = "-"
            presents_left -= 1

        if not presents_left:
            break

    return presents_left, nice_kids_count


total_presents = int(input())
grid_size = int(input())

grid = []
santa_position = []

total_nice_kids = 0
nice_kids_visited = 0

directions = {
    "up": (-1, 0),
    "down": (1, 0),
    "left": (0, -1),
    "right": (0, 1),
}

for row in range(grid_size):
    line = input().split()
    grid.append(line)

    if "S" in line:
        santa_position = [row, line.index("S")]
        grid[row][santa_position[1]] = "-"

    total_nice_kids += line.count("V")

current_command = input()

while current_command != "Christmas morning":
    santa_position = [
        santa_position[0] + directions[current_command][0],
        santa_position[1] + directions[current_command][1]
    ]

    current_house = grid[santa_position[0]][santa_position[1]]

    if current_house == "V":
        nice_kids_visited += 1
        total_presents -= 1
    elif current_house == "C":
        total_presents, nice_kids_visited = distribute_presents(total_presents, nice_kids_visited)

    grid[santa_position[0]][santa_position[1]] = "-"

    if not total_presents or nice_kids_visited == total_nice_kids:
        break

    current_command = input()

grid[santa_position[0]][santa_position[1]] = "S"

if not total_presents and nice_kids_visited < total_nice_kids:
    print("Santa ran out of presents!")

[print(*row) for row in grid]

if nice_kids_visited == total_nice_kids:
    print(f"Good job, Santa! {total_nice_kids} happy nice kid/s.")
else:
    print(f"No presents for {total_nice_kids - nice_kids_visited} nice kid/s.")
