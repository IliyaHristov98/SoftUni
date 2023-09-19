# /1/
n = int(input())
all_are_even = True
for i in range(n):
    number = int(input())
    if number % 2 != 0:
        print(f'{number} is odd!')
        all_are_even = False
        break
if all_are_even:
    print(f'All numbers are even.')

# /2/
n = int(input())
for i in range(n):
    number = int(input())
    if number % 2 != 0:
        print(f'{number} is odd!')
        all_are_even = False
        break
else:
    print(f'All numbers are even.')
