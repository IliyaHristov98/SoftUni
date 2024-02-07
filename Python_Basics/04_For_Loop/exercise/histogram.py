n = int(input())
p1 = 0
p2 = 0
p3 = 0
p4 = 0
p5 = 0

for numbers in range(n):
    a = int(input())
    if a < 200:
        p1 += 1
    elif a < 400:
        p2 += 1
    elif a < 600:
        p3 += 1
    elif a < 800:
        p4 += 1
    else:
        p5 += 1

print(f'{p1 / n * 100:.2f}%\n'
      f'{p2 / n * 100:.2f}%\n'
      f'{p3 / n * 100:.2f}%\n'
      f'{p4 / n * 100:.2f}%\n'
      f'{p5 / n * 100:.2f}%')
