string = input()
while string != 'End':
    if string != 'SoftUni':
        new_string = ''
        for i in string:
            new_string += i * 2
        print(new_string)
    string = input()
