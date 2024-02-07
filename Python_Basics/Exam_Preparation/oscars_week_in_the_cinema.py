movie = input()
hall = input()
tickets_bought = int(input())
price = 0
if movie == 'A Star Is Born':
    if hall == 'normal':
        price = 7.50
    elif hall == 'luxury':
        price = 10.5
    else:
        price = 13.5
elif movie == 'Bohemian Rhapsody':
    if hall == 'normal':
        price = 7.35
    elif hall == 'luxury':
        price = 9.45
    else:
        price = 12.75
elif movie == 'Green Book':
    if hall == 'normal':
        price = 8.15
    elif hall == 'luxury':
        price = 10.25
    else:
        price = 13.25
else:
    if hall == 'normal':
        price = 8.75
    elif hall == 'luxury':
        price = 11.55
    else:
        price = 13.95

income = price * tickets_bought
print(f'{movie} -> {income:.2f} lv.')
