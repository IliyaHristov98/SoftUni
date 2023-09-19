count = int(input())
size = input()
delivery = input()

price = 0

if size == '90X130':
    if 30 < count <= 60:
        price = count * 110 * 0.95
    elif count > 60:
        price = count * 110 * 0.92
    else:
        price = count * 110
elif size == '100X150':
    if 40 < count <= 80:
        price = count * 140 * 0.94
    elif count > 80:
        price = count * 140 * 0.9
    else:
        price = count * 140
elif size == '130X180':
    if 20 < count <= 50:
        price = count * 190 * 0.93
    elif count > 50:
        price = count * 190 * 0.88
    else:
        price = count * 190
elif size == '200X300':
    if 25 < count < 50:
        price = count * 250 * 0.91
    elif count > 50:
        price = count * 250 * 0.86
    else:
        price = count * 250

if delivery == 'With delivery':
    price += 60

if count > 99:
    price = price * 0.96

if count < 10:
    print('Invalid order')
else:
    print(f'{price:.2f} BGN')