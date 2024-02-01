import os

path = os.path.join("resources", "numbers.txt")
file = open(path)

total = 0
for line in file:
    total += int(line)

print(total)
