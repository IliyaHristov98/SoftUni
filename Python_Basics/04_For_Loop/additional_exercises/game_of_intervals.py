moves = int(input())
points = 0

less_than_10 = 0
less_than_20 = 0
less_than_30 = 0
less_than_40 = 0
less_than_50 = 0
invalid_numbers = 0

for move in range(moves):
    number = int(input())
    if number > 50 or number < 0:
        points = points / 2
        invalid_numbers += 1
    elif number >= 40:
        points += 100
        less_than_50 += 1
    elif number >= 30:
        points += 50
        less_than_40 +=1
    elif number >= 20:
        points += number * 0.4
        less_than_30 +=1
    elif number >= 10:
        points += number * 0.3
        less_than_20 +=1
    else:
        points += number * 0.2
        less_than_10 += 1

print(f'{points:.2f}')
print(f'From 0 to 9: {less_than_10 / moves * 100:.2f}%')
print(f'From 10 to 19: {less_than_20 / moves * 100:.2f}%')
print(f'From 20 to 29: {less_than_30 / moves * 100:.2f}%')
print(f'From 30 to 39: {less_than_40 / moves * 100:.2f}%')
print(f'From 40 to 50: {less_than_50 / moves * 100:.2f}%')
print(f'Invalid numbers: {invalid_numbers / moves * 100:.2f}%')
