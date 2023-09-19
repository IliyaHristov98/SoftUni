team = input()
souvenir = input()
count = int(input())
souvenir_is_invalid = False
team_is_invalid = False
price = 0

if team == 'Argentina':
    if souvenir == 'flags':
        price = 3.25
    elif souvenir == 'caps':
        price = 7.20
    elif souvenir == 'posters':
        price = 5.10
    elif souvenir == 'stickers':
        price = 1.25
    else:
        souvenir_is_invalid = True
elif team == 'Brazil':
    if souvenir == 'flags':
        price = 4.20
    elif souvenir == 'caps':
        price = 8.50
    elif souvenir == 'posters':
        price = 5.35
    elif souvenir == 'stickers':
        price = 1.20
    else:
        souvenir_is_invalid = True
elif team == 'Croatia':
    if souvenir == 'flags':
        price = 2.75
    elif souvenir == 'caps':
        price = 6.90
    elif souvenir == 'posters':
        price = 4.95
    elif souvenir == 'stickers':
        price = 1.10
    else:
        souvenir_is_invalid = True
elif team == 'Denmark':
    if souvenir == 'flags':
        price = 3.10
    elif souvenir == 'caps':
        price = 6.50
    elif souvenir == 'posters':
        price = 4.80
    elif souvenir == 'stickers':
        price = 0.90
    else:
        souvenir_is_invalid = True
else:
    team_is_invalid = True

total_price = price * count
if team_is_invalid:
    print(f'Invalid country!')
elif souvenir_is_invalid:
    print(f'Invalid stock!')
else:
    print(f'Pepi bought {count} {souvenir} of {team} for {total_price:.2f} lv.')
