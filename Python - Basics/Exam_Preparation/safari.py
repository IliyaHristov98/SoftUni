budget = float(input())
fuel_liters = float(input())
day = input()

fuel_price = fuel_liters * 2.1
guide_price = 100
total_price = guide_price + fuel_price

if day == 'Saturday':
    total_price = total_price * 0.9
else:
    total_price = total_price * 0.8

if total_price <= budget:
    print(f'Safari time! Money left: {budget - total_price:.2f} lv.')
else:
    print(f'Not enough money! Money needed: {total_price - budget:.2f} lv.')
