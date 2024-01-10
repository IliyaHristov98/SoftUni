budget = float(input())
people = int(input())
clothes_price_per_one = float(input())
decor = budget * 0.10
if people > 150:
    clothes_price_per_one = clothes_price_per_one * 0.9

total_cost = decor + people * clothes_price_per_one

if total_cost > budget:
    print(f'Not enough money!\n'
          f'Wingard needs {total_cost - budget:.2f} leva more.')
else:
    print(f'Action!\n'
          f'Wingard starts filming with {budget - total_cost:.2f} leva left.')
