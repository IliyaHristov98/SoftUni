from math import floor

record = float(input())
distance = float(input())
seconds_per_meter = float(input())

elevation_slow = floor(distance // 50 * 30)
total_time = distance * seconds_per_meter + elevation_slow

if total_time < record:
    print(f'Yes! The new record is {total_time:.2f} seconds.')
else:
    print(f'No! He was {total_time - record:.2f} seconds slower.')