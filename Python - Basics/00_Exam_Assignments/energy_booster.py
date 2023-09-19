fruit = input()
size = input()
quantity = int(input())

price = 0

if fruit == 'Watermelon':
    if size == 'small':
        price = 2 * quantity * 56
    else:
        price = 5 * quantity * 28.7
elif fruit == 'Mango':
    if size == 'small':
        price = 2 * quantity * 36.66
    else:
        price = 5 * quantity * 19.6
elif fruit == 'Pineapple':
    if size == 'small':
        price = 2 * quantity * 42.1
    else:
        price = 5 * quantity * 24.8
else:
    if size == 'small':
        price = 2 * quantity * 20
    else:
        price = 5 * quantity * 15.2

if 400 <= price <= 1000:
    price = price * 0.85
elif price > 1000:
    price = price * 0.5

print(f'{price:.2f} lv.')
