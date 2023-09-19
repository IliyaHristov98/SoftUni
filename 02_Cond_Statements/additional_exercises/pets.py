from math import ceil, floor

days = int(input())
kilos_of_food_left = int(input())
dog_food_per_day_needed = float(input())
cat_food_per_day_needed = float(input())
turtle_food_per_day_needed = float(input()) / 1000

food_per_day = dog_food_per_day_needed + cat_food_per_day_needed + turtle_food_per_day_needed
total_food_needed = food_per_day * days

food_left = ceil(total_food_needed - kilos_of_food_left)
food_needed = floor(kilos_of_food_left - total_food_needed)

if total_food_needed >= kilos_of_food_left:
    print(f"{food_left} kilos of food left.")
else:
    print(f'{food_needed} more kilos of food are needed.')