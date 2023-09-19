number = int(input())
for n in range(1, number + 1):
    total = 0
    for digit in str(n):
        total += int(digit)
    if total == 5 or total == 7 or total == 11:
        print(f'{n} -> True')
    else:
        print(f'{n} -> False')
