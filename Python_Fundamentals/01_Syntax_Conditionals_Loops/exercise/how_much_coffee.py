# /1/

command = input()
coffees = 0
while command != 'END':
    if command == 'coding' or command == 'cat' or command == 'dog' or command == 'movie':
        coffees += 1
    elif command == 'CODING' or command == 'CAT' or command == 'DOG' or command == 'MOVIE':
        coffees += 2
    command = input()

if coffees <= 5:
    print(coffees)
else:
    print('You need extra sleep')

# /2/

command = input()
coffees = 0
while command != 'END':
    if command.lower() == 'coding' or command.lower() == 'cat' \
            or command.lower() == 'dog' or command.lower() == 'movie':
        if command.islower():
            coffees += 1
        else:  # if command.isupper()
            coffees += 2
    command = input()
if coffees <= 5:
    print(coffees)
else:
    print('You need extra sleep')