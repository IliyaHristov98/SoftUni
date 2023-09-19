n = int(input())
divided_by_two = 0
divided_by_three = 0
divided_by_four = 0

for i in range(n):
    number = int(input())
    if number % 2 == 0:
        divided_by_two += 1
    if number % 3 == 0:
        divided_by_three += 1
    if number % 4 == 0:
        divided_by_four += 1

print(f'{divided_by_two / n * 100:.2f}%\n'
      f'{divided_by_three / n * 100:.2f}%\n'
      f'{divided_by_four / n * 100:.2f}%')
