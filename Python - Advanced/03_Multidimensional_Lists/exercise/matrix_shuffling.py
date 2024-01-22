def are_indices_valid(indices):
    return {indices[0], indices[2]}.issubset(valid_rows) and {indices[1], indices[3]}.issubset(valid_cols)


def perform_swap(command, indices):
    if len(indices) == 4 and are_indices_valid(indices) and command == "swap":
        row1, col1, row2, col2 = indices
        matrix[row1][col1], matrix[row2][col2] = matrix[row2][col2], matrix[row1][col1]

        [print(*row) for row in matrix]
    else:
        print("Invalid input!")


num_rows, num_cols = [int(x) for x in input().split()]
matrix = [input().split() for _ in range(num_rows)]

valid_rows = range(num_rows)
valid_cols = range(num_cols)

while True:
    command_type, *coordinates = [int(x) if x.isdigit() else x for x in input().split()]

    if command_type == "END":
        break

    perform_swap(command_type, coordinates)
