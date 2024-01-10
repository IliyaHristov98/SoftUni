from sys import maxsize
from math import ceil

height = int(input())
width = int(input())
percentage = int(input()) / 100

area = height * width
painted_area = ceil(area - (area * percentage)) * 4
total_paint = 0

for wall in range(maxsize):
    paint = input()
    if paint == 'Tired!':
        print(f'{painted_area - total_paint} quadratic m left.')
        break
    liters = int(paint)
    total_paint += liters

    if total_paint > painted_area:
        print(f'All walls are painted and you have {total_paint - painted_area} l paint left!')
        break
    elif total_paint == painted_area:
        print(f'All walls are painted! Great job, Pesho!')
        break
