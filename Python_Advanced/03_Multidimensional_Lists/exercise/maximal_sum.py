rows, cols = [int(x) for x in input().split()]

matrix = [[int(x) for x in input().split()] for _ in range(rows)]

highest_sum = float("-inf")
highest_matrix = []

for row in range(rows - 2):
    for col in range(cols - 2):
        first = matrix[row][col:col + 3]
        second = matrix[row + 1][col:col + 3]
        third = matrix[row + 2][col:col + 3]

        total_sum = sum(first) + sum(second) + sum(third)
        if total_sum > highest_sum:
            highest_sum = total_sum
            highest_matrix = [first, second, third]

print(f"Sum = {highest_sum}")
for highest in highest_matrix:
    print(f'{" ".join(map(str, highest))}')
