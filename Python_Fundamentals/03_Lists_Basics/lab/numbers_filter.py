n = int(input())
numbers_list = []

for x in range(n):
    integer = int(input())
    numbers_list.append(integer)

command = input()

for y in range(len(numbers_list) - 1, -1, -1):
    element = numbers_list[y]
    if command == 'even':
        if element % 2 != 0:
            numbers_list.remove(element)
    elif command == 'odd':
        if element % 2 == 0 or numbers_list[y] == 0:
            numbers_list.remove(element)
    elif command == 'negative':
        if element >= 0:
            numbers_list.remove(element)
    else:
        if element < 0:
            numbers_list.remove(element)

print(numbers_list)
