budget = float(input())
nights = int(input())
price_per_night = float(input())
additional_costs_percentage = int(input()) / 100

if nights > 7:
    price_per_night = price_per_night * 0.95

total_price = nights * price_per_night + (additional_costs_percentage * budget)

if total_price <= budget:
    print(f'Ivanovi will be left with {budget - total_price:.2f} leva after vacation.')
else:
    print(f'{total_price - budget:.2f} leva needed.')