rows, cols = [int(x) for x in input().split(", ")]

matrix = []
max_sum = float("-inf")

for _ in range(rows):
    matrix.append([int(y) for y in input().split(", ")])

sub_matrix = []

for row in range(rows - 1):
    for col in range(cols - 1):
        current = matrix[row][col]
        right = matrix[row][col + 1]
        down = matrix[row + 1][col]
        diagonal = matrix[row + 1][col + 1]

        current_sum = current + right + down + diagonal
        if current_sum > max_sum:
            max_sum = current_sum
            sub_matrix = [[current, right], [down, diagonal]]

print(*sub_matrix[0])
print(*sub_matrix[1])
print(max_sum)
