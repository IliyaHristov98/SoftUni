period = input()
type_of_plan = input()
internet = input()
months = int(input())

price_per_month = 0

if period == 'one':
    if type_of_plan == "Small":
        price_per_month = 9.98
    elif type_of_plan == "Middle":
        price_per_month = 18.99
    elif type_of_plan == 'Large':
        price_per_month = 25.98
    else:
        price_per_month = 35.99
elif period == 'two':
    if type_of_plan == "Small":
        price_per_month = 8.58
    elif type_of_plan == "Middle":
        price_per_month = 17.09
    elif type_of_plan == 'Large':
        price_per_month = 23.59
    else:
        price_per_month = 31.79

if internet == 'yes':
    if price_per_month <= 10:
        price_per_month += 5.50
    elif price_per_month <= 30:
        price_per_month += 4.35
    else:
        price_per_month += 3.85

if period == 'two':
    price_per_month = price_per_month * 0.9625

final_price = price_per_month * months
print(f'{final_price:.2f} lv.')

