CALORIES_PER_MINUTE = 5

minutes_walked = int(input())
number_of_walks = int(input())
daily_calorie_intake = int(input())

total_calories_burned = minutes_walked * CALORIES_PER_MINUTE * number_of_walks

if total_calories_burned >= daily_calorie_intake / 2:
    print(f'Yes, the walk for your cat is enough. Burned calories per day: {total_calories_burned}.')
else:
    print(f'No, the walk for your cat is not enough. Burned calories per day: {total_calories_burned}.')