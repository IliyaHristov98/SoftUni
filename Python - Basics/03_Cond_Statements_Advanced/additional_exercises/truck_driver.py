season = input()
kilometers = float(input())

pay_per_km = 0

if season == 'Spring' or season == 'Autumn':
    pay_per_km = 0.75
    if 5000 < kilometers <= 10000:
        pay_per_km = 0.95
    elif kilometers > 10000:
        pay_per_km = 1.45
elif season == 'Summer':
    pay_per_km = 0.90
    if 5000 < kilometers <= 10000:
        pay_per_km = 1.1
    elif kilometers > 10000:
        pay_per_km = 1.45
elif season == 'Winter':
    pay_per_km = 1.05
    if 5000 < kilometers <= 10000:
        pay_per_km = 1.25
    elif kilometers > 10000:
        pay_per_km = 1.45

final_pay = (pay_per_km * kilometers) * 4 * 0.90
print(f'{final_pay:.2f}')