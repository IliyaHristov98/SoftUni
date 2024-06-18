string = input()
final_string = ""
explosion_power = 0

for index in range(len(string)):
    if string[index] == ">":
        explosion_power += int(string[index + 1])
        final_string += string[index]
    else:
        if explosion_power > 0:
            explosion_power -= 1
        else:
            final_string += string[index]

print(final_string)
