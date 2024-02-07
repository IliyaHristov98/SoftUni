n = int(input())

for special_number in range(1111, 10000):
    is_special = True
    for index, digit in enumerate(str(special_number)):
        if int(digit) == 0 or n % int(digit) != 0:
            is_special = False
            break

    if is_special:
        print(f'{special_number}', end = ' ')
