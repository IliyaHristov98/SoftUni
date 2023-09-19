from sys import maxsize

budget = float(input())
items_count = 0
total_price = 0

for i in range(1, maxsize):
    name = input()

    if name == 'Stop':
        print(f'You bought {items_count} products for {total_price:.2f} leva.')
        price = 0
        break

    price = float(input())
    items_count += 1

    if i % 3 == 0:
        price = price * 0.5

    total_price += price

    if total_price > budget:
        print(f"You don't have enough money!\n"
              f"You need {total_price - budget:.2f} leva!")
        break
