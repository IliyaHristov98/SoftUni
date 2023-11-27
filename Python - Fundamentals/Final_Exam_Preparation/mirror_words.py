import re

text = input()
regex = r"(\@|\#)([A-Za-z]{2}[A-Za-z]+)\1\1([A-Za-z]{2}[A-Za-z]+)\1"

mirror_pairs = {}
valid = 0
mirror = 0

for pairs in re.finditer(regex, text):
    one = pairs.group(2)
    two = pairs.group(3)
    valid += 1

    if one == two[::-1]:
        mirror_pairs[one] = two
        mirror += 1

if valid == 0:
    print(f"No word pairs found!\n"
          f"No mirror words!")
else:
    print(f"{valid} word pairs found!")
    if mirror == 0:
        print(f"No mirror words!")
    else:
        print(f"The mirror words are:")
        match = ", ".join(f"{first} <=> {second}" for first, second in mirror_pairs.items())
        print(match)
