money = float(input())
gender = input()
age = int(input())
sport = input()

card = 0

if gender == 'm':
    if sport == 'Gym':
        card = 42
    elif sport == 'Boxing':
        card = 41
    elif sport == 'Yoga':
        card = 45
    elif sport == 'Zumba':
        card = 34
    elif sport == 'Dances':
        card = 51
    else:
        card = 39
elif gender == 'f':
    if sport == 'Gym':
        card = 35
    elif sport == 'Boxing':
        card = 37
    elif sport == 'Yoga':
        card = 42
    elif sport == 'Zumba':
        card = 31
    elif sport == 'Dances':
        card = 53
    else:
        card = 37

if age <= 19:
    card = card * 0.8

if card <= money:
    print(f'You purchased a 1 month pass for {sport}.')
else:
    print(f"You don't have enough money! You need ${card - money:.2f} more.")