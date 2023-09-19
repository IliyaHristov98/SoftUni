import sys

n = int(input())
max_sum = -sys.maxsize
sum = 0

for numbers in range(n):
    a = int(input())
    sum += a
    if a > max_sum:
        max_sum = a

if max_sum == sum - max_sum:
    print(f'Yes\nSum = {max_sum}')
else:
    difference = abs(max_sum - (sum - max_sum))
    print(f'No\n Diff = {difference}')
