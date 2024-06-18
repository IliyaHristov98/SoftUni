one = ord(input())
two = ord(input())
string = input()
ascii_total = 0

for character in string:
    if one < ord(character) < two:
        ascii_total += ord(character)

print(ascii_total)
