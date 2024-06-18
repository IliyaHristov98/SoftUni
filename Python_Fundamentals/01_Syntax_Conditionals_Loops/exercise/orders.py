number_of_orders = int(input())
total_price = 0
for order in range(number_of_orders):
    price_per_capsule = float(input())
    days = int(input())
    capsules_per_day = int(input())

    if price_per_capsule < 0.01 or price_per_capsule > 100.00:
        continue
    elif days < 1 or days > 31:
        continue
    elif capsules_per_day < 1 or capsules_per_day > 2000:
        continue

    price_for_today = price_per_capsule * capsules_per_day * days
    print(f'The price for the coffee is: ${price_for_today:.2f}')
    total_price += price_for_today

print(f'Total: ${total_price:.2f}')
