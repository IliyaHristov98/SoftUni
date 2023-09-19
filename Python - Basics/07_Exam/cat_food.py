cats_count = int(input())
small_cats = 0
big_cats = 0
giant_cats = 0
food_per_day = 0
one_kg_of_food = 12.45
for cat in range(cats_count):
    grams_of_food = float(input())
    food_per_day += grams_of_food
    if 100 <= grams_of_food < 200:
        small_cats += 1
    elif 200 <= grams_of_food < 300:
        big_cats += 1
    elif 300 <= grams_of_food < 400:
        giant_cats += 1

food_price = (food_per_day / 1000) * one_kg_of_food
print(f'Group 1: {small_cats} cats.\n'
      f'Group 2: {big_cats} cats.\n'
      f'Group 3: {giant_cats} cats.\n'
      f'Price for food per day: {food_price:.2f} lv.')
