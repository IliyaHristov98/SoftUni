string = input()
upper_case_index = []
current_index = 0
for character in string:
    if character.isupper():
        upper_case_index.append(current_index)
    current_index += 1
print(upper_case_index)
