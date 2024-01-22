rows = int(input())

flattened_matrix = []

for _ in range(rows):
    sub_list = [int(x) for x in input().split(", ")]
    flattened_matrix.extend(sub_list)

print(flattened_matrix)
