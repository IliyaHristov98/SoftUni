budget = float(input())
season = input()

destination = ''
accomodation = ''
price = 0

if season == 'summer':
    if budget <= 100:
        destination = 'Bulgaria'
        accomodation = 'Camp'
        price = budget * 0.3
    elif budget <= 1000:
        destination = 'Balkans'
        accomodation = 'Camp'
        price = budget * 0.4
    elif budget > 1000:
        destination = 'Europe'
        accomodation = 'Hotel'
        price = budget * 0.9
elif season == 'winter':
    if budget <= 100:
        destination = 'Bulgaria'
        accomodation = 'Hotel'
        price = budget * 0.7
    elif budget <= 1000:
        destination = 'Balkans'
        accomodation = 'Hotel'
        price = budget * 0.8
    elif budget > 1000:
        destination = 'Europe'
        accomodation = 'Hotel'
        price = budget * 0.9

print(f'Somewhere in {destination}')
print(f"{accomodation} - {price:.2f}")