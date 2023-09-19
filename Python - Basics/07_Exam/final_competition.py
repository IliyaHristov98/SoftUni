dancers = int(input())
points = float(input())
season = input()
place = input()

prize = 0

if place == 'Bulgaria':
    prize = points * dancers
    if season == 'summer':
        prize = prize * 0.95
    else:
        prize = prize * 0.92
else:
    prize = (dancers * points) * 1.5
    if season == 'summer':
        prize = prize * 0.9
    else:
        prize = prize * 0.85

money_to_charity = prize * 0.75
money_left = prize - money_to_charity
money_per_dancer = money_left / dancers
print(f'Charity - {money_to_charity:.2f}\n'
      f'Money per dancer - {money_per_dancer:.2f}')
