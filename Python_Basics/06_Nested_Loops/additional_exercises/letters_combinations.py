start_letter = input()
end_letter = input()
omit_letter = input()

one = 0
two = 0
three = 0
count = 0
for letter1 in range(ord(start_letter), ord(end_letter) + 1):
    if letter1 == ord(omit_letter):
        continue
    else:
        one = chr(letter1)

    for letter2 in range(ord(start_letter), ord(end_letter) + 1):
        if letter2 == ord(omit_letter):
            continue
        else:
            two = chr(letter2)

        for letter3 in range(ord(start_letter), ord(end_letter) + 1):
            if letter3 == ord(omit_letter):
                continue
            else:
                three = chr(letter3)
            print(f'{one}{two}{three}', end=' ')
            count += 1
print(count)
