budget = float(input())
category = input()
number_of_people = int(input())

transport_price = 0

if number_of_people <= 4:
    transport_price = budget * 0.75
elif number_of_people <= 9:
    transport_price = budget * 0.60
elif number_of_people <= 24:
    transport_price = budget * 0.50
elif number_of_people <= 49:
    transport_price = budget * 0.40
else:
    transport_price = budget * 0.25

budget_left = budget - transport_price

if category == 'VIP':
    tickets_total = number_of_people * 499.99
    if tickets_total >= budget_left:
        print(f'Not enough money! You need {tickets_total - budget_left:.2f} leva.')
    else:
        print(f'Yes! You have {budget_left - tickets_total:.2f} leva left.')
elif category == 'Normal':
    tickets_total = number_of_people * 249.99
    if tickets_total >= budget_left:
        print(f'Not enough money! You need {tickets_total - budget_left:.2f} leva.')
    else:
        print(f'Yes! You have {budget_left - tickets_total:.2f} leva left.')