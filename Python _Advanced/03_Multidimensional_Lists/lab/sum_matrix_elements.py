row, col = input().split(", ")

matrix = []
total = 0

for _ in range(int(row)):
    sub_list = [int(x) for x in input().split(", ")]
    total += sum(sub_list)
    matrix.append(sub_list)

print(total)
print(matrix)
