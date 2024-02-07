start = int(input())
end = int(input())
string = ''
for character in range(start, end + 1):
    string += f'{chr(character)} '
print(string)
