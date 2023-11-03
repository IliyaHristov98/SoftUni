strings = input().split()
dictionary = {}
for string in strings:
    for letter in string:
        if letter not in dictionary:
            dictionary[letter] = 0
        dictionary[letter] += 1

for key, value in dictionary.items():
    print(f"{key} -> {value}")
