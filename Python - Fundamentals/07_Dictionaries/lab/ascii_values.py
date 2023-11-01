characters = input().split(", ")
ascii_values = {}

for character in characters:
    ascii_values[character] = ord(character)

print(ascii_values)
