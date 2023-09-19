length = float(input())
width = float(input()) - 1

places_per_row = width // 0.7
rows = length // 1.2
places = places_per_row * rows

number_of_places_total = places - 3
print(int(number_of_places_total))