import sys

number = input()
max_number = -sys.maxsize
while number != 'Stop':
    if int(number) > max_number:
        max_number = int(number)
    number = input()
print(max_number)