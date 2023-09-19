import sys

desired_profit = float(input())
profit = 0
price = 0

for i in range(sys.maxsize):
    cocktail = input()
    if cocktail == 'Party!':
        print(f'We need {desired_profit - profit:.2f} leva more.')
        break
    quantity = int(input())
    price = len(cocktail) * quantity

    if price % 2 != 0:
        price = price * 0.75
    profit += price

    if profit >= desired_profit:
        print(f'Target acquired.')
        break

print(f'Club income - {profit:.2f} leva.')
