n = int(input())
count = 0
total = 0
for i in range(n):
    number = int(input())
    count += 1
    total += number
average = total / count
print(f'{average:.2f}')
