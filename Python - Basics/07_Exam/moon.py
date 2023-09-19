from math import ceil

average_speed = float(input())
liters_per_100_km = float(input())
distance = 384400

time = (2 * distance) / average_speed + 3
fuel = ((2 * distance) / 100) * liters_per_100_km

print(ceil(time))
print(round(fuel))
