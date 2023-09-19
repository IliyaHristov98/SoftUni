juniors = int(input())
seniors = int(input())
type = input()

junior_price = 0
senior_price = 0

if type == 'trail':
    junior_price = 5.5
    senior_price = 7
elif type == 'cross-country':
    junior_price = 8
    senior_price = 9.5
    if juniors + seniors >= 50:
        junior_price = 8 * 0.75
        senior_price = 9.5 * 0.75
elif type == 'downhill':
    junior_price = 12.25
    senior_price = 13.75
elif type == 'road':
    junior_price = 20
    senior_price = 21.5

total = juniors * junior_price + seniors * senior_price
donated = total * 0.95
print(f'{donated:.2f}')