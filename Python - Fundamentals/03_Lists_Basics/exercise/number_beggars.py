money_as_integers = [int(number) for number in input().split(', ')]
beggars = int(input())
beggars_list = [0] * beggars
count = 0

for coin in money_as_integers:
    beggars_list[count] += coin
    count += 1
    if count >= beggars:
        count = 0

print(beggars_list)
