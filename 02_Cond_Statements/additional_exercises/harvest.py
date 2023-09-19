from math import floor, ceil

area = int(input())
kgs_grapes_per_sq_meter = float(input())
needed_liters_of_wine = int(input())
number_of_workers = int(input())

area_for_grapes = area * 0.4
total_liters_wine = (area_for_grapes * kgs_grapes_per_sq_meter) / 2.5

not_enough_wine = needed_liters_of_wine - total_liters_wine
enough_wine_left = total_liters_wine - needed_liters_of_wine
wine_per_worker = enough_wine_left / number_of_workers

if total_liters_wine < needed_liters_of_wine:
    print(f'It will be a tough winter! More {floor(not_enough_wine)} liters wine needed.')
else:
    print(f'Good harvest this year! Total wine: {floor(total_liters_wine)} liters.')
    print(f'{ceil(enough_wine_left)} liters left -> {ceil(wine_per_worker)} liters per person.')