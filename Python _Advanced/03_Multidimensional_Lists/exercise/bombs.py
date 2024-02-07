matrix = [[int(x) for x in input().split()] for _ in range(int(input()))]

bombs = input().split()

directions = {
    (-1, 0),
    (1, 0),
    (0, -1),
    (0, 1),
    (-1, 1),
    (-1, -1),
    (1, -1),
    (1, 1),
    (0, 0),
}

for b in bombs:
    bomb = b.split(",")
    r, c = int(bomb[0]), int(bomb[1])
    damage = matrix[r][c]

    if damage > 0:
        for direction in directions:
            if 0 <= r + direction[0] < len(matrix[0]) \
                    and 0 <= c + direction[1] < len(matrix) \
                    and matrix[r + direction[0]][c + direction[1]] > 0:
                matrix[r + direction[0]][c + direction[1]] -= damage

alive_cells = [num for row in range(len(matrix[0])) for num in matrix[row] if num > 0]
print(f"Alive cells: {len(alive_cells)}")
print(f"Sum: {sum(alive_cells)}")

for row in matrix:
    print(*row, sep=" ")
