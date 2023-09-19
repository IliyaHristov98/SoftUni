first = int(input())
second = int(input())
third = int(input())

first_number = 0
second_number = 0
third_number = 0

for x in range(1, first + 1):
    if x % 2 != 0:
        continue
    else:
        first_number = x

    for y in range(2, second + 1):
        if y == 2 or y == 3 or y == 5 or y == 7:
            second_number = y
        else:
            continue

        for z in range(1, third + 1):
            if z % 2 != 0:
                continue
            else:
                third_number = z
                print(f'{first_number} {second_number} {third_number}')
