string = input()
current_string = ""
multiplier = ""
final_string = ""

for i in range(len(string)):
    if string[i].isdigit():
        multiplier += string[i]
        if i + 1 < len(string) and string[i + 1].isdigit():
            continue
        else:
            final_string += current_string.upper() * int(multiplier)
            current_string = ""
            multiplier = ""
    else:
        current_string += string[i]

unique = []
for character in final_string:
    if character.upper() not in unique:
        unique.append(character.upper())

print(f"Unique symbols used: {len(unique)}\n{final_string}")
