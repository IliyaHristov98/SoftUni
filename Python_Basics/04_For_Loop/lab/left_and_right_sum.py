n = int(input())

left_sum = 0
right_sum = 0

for numbers in range(n * 2):
    currect_number = int(input())
    if numbers < n:
        left_sum += currect_number
    else:
        right_sum += currect_number

if left_sum == right_sum:
    print(f'Yes, sum = {left_sum}')
else:
    difference = abs(left_sum - right_sum)
    print(f'No, diff = {difference}')