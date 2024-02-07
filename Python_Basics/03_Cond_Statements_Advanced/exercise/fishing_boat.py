budget = int(input())
season = input()
fishermen_count = int(input())

rent = 0

if season == 'Spring':
    if fishermen_count <= 6:
        rent = 3000 * 0.9
    elif fishermen_count > 6 and fishermen_count <= 11:
        rent = 3000 * 0.85
    elif fishermen_count > 11:
        rent = 3000 * 0.75
elif season == 'Summer' or season == 'Autumn':
    if fishermen_count <= 6:
        rent = 4200 * 0.9
    elif fishermen_count > 6 and fishermen_count <= 11:
        rent = 4200 * 0.85
    elif fishermen_count > 11:
        rent = 4200 * 0.75
else:
    if fishermen_count <= 6:
        rent = 2600 * 0.9
    elif fishermen_count > 6 and fishermen_count <= 11:
        rent = 2600 * 0.85
    elif fishermen_count > 11:
        rent = 2600 * 0.75

if fishermen_count % 2 == 0 and season != 'Autumn':
    rent = rent * 0.95

if rent <= budget:
    print(f'Yes! You have {budget - rent:.2f} leva left.')
elif rent > budget:
    print(f'Not enough money! You need {rent - budget:.2f} leva.')