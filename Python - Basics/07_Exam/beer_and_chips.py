from math import ceil

name = input()
budget = float(input())
beers = int(input())
chips_packets = int(input())

beer_price = 1.2
chips_price = (beer_price * beers) * 0.45
total_price = beer_price * beers + ceil(chips_price * chips_packets)

if total_price <= budget:
    print(f'{name} bought a snack and has {budget - total_price:.2f} leva left.')
else:
    print(f'{name} needs {total_price - budget:.2f} more leva!')
    