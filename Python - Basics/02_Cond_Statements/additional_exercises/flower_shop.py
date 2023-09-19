from math import ceil, floor

MAGNOLII = 3.25
ZUMBULI = 4.00
ROZI = 3.50
KAKTUSI = 8.00
TAX = 0.05

magnolii_count = int(input())
zumbuli_count = int(input())
rozi_count = int(input())
kaktusi_count = int(input())
gift_price = float(input())

pre_tax_income = magnolii_count * MAGNOLII + zumbuli_count * ZUMBULI + rozi_count * ROZI\
    + kaktusi_count * KAKTUSI
final_income = pre_tax_income - (pre_tax_income * TAX)

money_left = final_income - gift_price
money_needed = gift_price - final_income

if final_income >= gift_price:
    print(f'She is left with {floor(money_left)} leva.')
else:
    print(f'She will have to borrow {ceil(money_needed)} leva.')