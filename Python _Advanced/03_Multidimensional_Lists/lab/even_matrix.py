rows = int(input())

matrix = []

for _ in range(rows):
    sub_list = [int(x) for x in input().split(", ") if int(x) % 2 == 0]
    matrix.append(sub_list)

print(matrix)
