n = int(input())
for i in range(n):
    string = input()
    for letter in range(len(string)):
        if string[letter] == ',' or string[letter] == '.' or string[letter] == '_':
            print(f'{string} is not pure!')
            break
    else:
        print(f'{string} is pure.')
