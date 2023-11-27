import re

info = input()
regex = r"(=|\/)([A-Z][A-Za-z][A-Za-z]+)\1"
locations = []
points = 0

for location in re.finditer(regex, info):
    locations.append(location.group(2))
    points += len(location.group(2))

print(f"Destinations: {', '.join(locations)}")
print(f"Travel Points: {points}")
