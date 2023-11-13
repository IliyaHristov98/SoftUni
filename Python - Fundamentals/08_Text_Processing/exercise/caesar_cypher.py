string = input()
encrypted_string = ""

for char in string:
    encrypted_char = chr(ord(char) + 3)
    encrypted_string += encrypted_char

print(encrypted_string)
