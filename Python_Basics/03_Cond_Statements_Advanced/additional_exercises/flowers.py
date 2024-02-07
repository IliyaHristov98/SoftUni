greylishes_count = int(input())
roses_count = int(input())
tulips_count = int(input())
season = input()
holiday = input()

greylish = 0
rose = 0
tulip = 0
arrangement = 2

if season == 'Spring' or season == 'Summer':
    if holiday == 'Y':
        greylish = 2 * 1.15
        rose = 4.1 * 1.15
        tulip = 2.5 * 1.15
    else:
        greylish = 2
        rose = 4.1
        tulip = 2.5
elif season == 'Autumn' or season == 'Winter':
    if holiday == 'Y':
        greylish = 3.75 * 1.15
        rose = 4.5 * 1.15
        tulip = 4.15 * 1.15
    else:
        greylish = 3.75
        rose = 4.5
        tulip = 4.15

total = greylish * greylishes_count + roses_count * rose + tulip * tulips_count

if tulips_count > 7 and season == 'Spring':
    total = total * 0.95
if roses_count >= 10 and season == 'Winter':
    total = total * 0.9
if greylishes_count + roses_count + tulips_count > 20:
    total = total * 0.8

final_price = total + arrangement
print(f'{final_price:.2f}')
