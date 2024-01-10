drink = input()
sugar = input()
quantity = int(input())
price = 0
if drink == 'Espresso':
    if sugar == 'Without':
        price = 0.9
    elif sugar == 'Normal':
        price = 1
    else:
        price = 1.2
elif drink == 'Cappuccino':
    if sugar == 'Without':
        price = 1
    elif sugar == 'Normal':
        price = 1.2
    else:
        price = 1.6
else:
    if sugar == 'Without':
        price = 0.5
    elif sugar == 'Normal':
        price = 0.6
    else:
        price = 0.7

if sugar == 'Without':
    price = price * 0.65
if drink == 'Espresso' and quantity > 4:
    price = price * 0.75

total_price = price * quantity

if total_price> 15:
    total_price = total_price * 0.8

print(f'You bought {quantity} cups of {drink} for {total_price:.2f} lv.')
