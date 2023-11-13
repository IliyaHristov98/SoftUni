string = input()
unique = string[0]

for index in range(1, len(string)):
    if string[index] != string[index - 1]:
        unique += string[index]

print(unique)
