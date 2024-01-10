days = int(input())
total_food = float(input())

food_eaten = 0
eaten_dog_food = 0
eaten_cat_food = 0
biscuits_eaten = 0

for day in range(1, days + 1):
    dog_food = int(input())
    cat_food = int(input())
    eaten_dog_food += dog_food
    eaten_cat_food += cat_food
    food_eaten += dog_food + cat_food
    if day % 3 == 0:
        biscuits_eaten += 0.1 * (dog_food + cat_food)

print(f'Total eaten biscuits: {round(biscuits_eaten)}gr.\n'
      f'{food_eaten / total_food * 100:.2f}% of the food has been eaten.\n'
      f'{eaten_dog_food / food_eaten * 100:.2f}% eaten from the dog.\n'
      f'{eaten_cat_food /food_eaten * 100:.2f}% eaten from the cat.')

