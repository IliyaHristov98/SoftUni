list_of_numbers = input().split()
message = input()
new_word = []

for number in list_of_numbers:
    index = 0
    for digit in number:
        index += int(digit)

    index %= len(message)
    new_word.append(message[index])
    message = message.replace(message[index], '', 1)

print(''.join(new_word))
