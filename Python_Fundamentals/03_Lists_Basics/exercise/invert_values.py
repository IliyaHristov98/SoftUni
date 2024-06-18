string = input()
list_of_numbers = string.split()
numbers_reversed = []

for i in list_of_numbers:
    integer_element = int(i)
    if integer_element == 0:
        numbers_reversed.append(integer_element)
    else:
        numbers_reversed.append(integer_element * -1)

print(numbers_reversed)
