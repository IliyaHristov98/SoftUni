n = int(input())

odd_sum = 0
even_sum = 0

for number in range(n):
    a = int(input())
    if number % 2 == 0:
        even_sum += a
    else:
        odd_sum += a

if even_sum == odd_sum:
    print(f'Yes\nSum = {even_sum}')
else:
    difference = abs(even_sum - odd_sum)
    print(f'No\nDiff = {difference}')