GASOLINE = 2.22
GASOLINE_DISCOUNTED = 2.22 - 0.18
DIESEL = 2.33
DIESEL_DISCOUNTED = 2.33 - 0.12
GAS = 0.93
GAS_DISCOUNTED = 0.93 - 0.08
MID_DISCOUNT = 0.08
HIGH_DISCOUNT = 0.10

fuel = input()
liters = float(input())
card = input()

total_price = 0

if fuel == "Gasoline":
    if card == "Yes":
        total_price = liters * GASOLINE_DISCOUNTED
    else:
        total_price = liters * GASOLINE
elif fuel == "Diesel":
    if card == "Yes":
        total_price = liters * DIESEL_DISCOUNTED
    else:
        total_price = liters * DIESEL
else:
    if card == "Yes":
        total_price = liters * GAS_DISCOUNTED
    else:
        total_price = liters * GAS

if liters > 25:
    total_price = total_price - (total_price * HIGH_DISCOUNT)
elif liters >= 20:
    total_price = total_price - (total_price * MID_DISCOUNT)
else:
    total_price = total_price

print(f'{total_price:.2f} lv.')