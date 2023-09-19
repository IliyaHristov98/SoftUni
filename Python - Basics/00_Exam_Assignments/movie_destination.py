budget = float(input())
destination = input()
season = input()
days = int(input())
price_per_day = 0

if destination == "Dubai":
    if season == "Winter":
        price_per_day = 45000
    else:
        price_per_day = 40000
elif destination == "Sofia":
    if season == "Winter":
        price_per_day = 17000
    else:
        price_per_day = 12500
elif destination == "London":
    if season == "Winter":
        price_per_day = 24000
    else:
        price_per_day = 20250

total_price = price_per_day * days

if destination == 'Dubai':
    total_price = total_price * 0.7
elif destination == "Sofia":
    total_price = total_price * 1.25


if total_price <= budget:
    print(f'The budget for the movie is enough! We have {budget - total_price:.2f} leva left!')
else:
    print(f'The director needs {total_price - budget:.2f} leva more!')
