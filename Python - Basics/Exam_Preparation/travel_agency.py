place = input()
package = input()
vip = input()
days = int(input())

price = 0
error = False

if place == 'Bansko' or place == 'Borovets':
    if package == 'noEquipment':
        price = 80
        if vip == 'yes':
            price = price * 0.95
    elif package == 'withEquipment':
        price = 100
        if vip == 'yes':
            price = price * 0.90
    else:
        error = True
elif place == 'Varna' or place == 'Burgas':
    if package == 'noBreakfast':
        price = 100
        if vip == 'yes':
            price = price * 0.93
    elif package == 'withBreakfast':
        price = 130
        if vip == 'yes':
            price = price * 0.88
    else:
        error = True
else:
    error = True

if days > 7:
    days -= 1

total_price = price * days

if error:
    print(f'Invalid input!')
elif days < 1:
    print(f'Days must be positive number!')
else:
    print(f'The price is {total_price:.2f}lv! Have a nice time!')