n = int(input())

for i in range(n):
    number = int(input())
    if number == 88:
        print('Hello')
    elif number == 86:
        print('How are you?')
    elif number < 86 or number == 87:
        print('GREAT!')
    else:
        print('Bye.')
