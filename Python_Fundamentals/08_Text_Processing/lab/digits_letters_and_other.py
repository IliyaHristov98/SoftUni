string = input()
digits = ""
letters = ""
others = ""
for character in string:
    if character.isdigit():
        digits += character
    elif character.isalpha():
        letters += character
    else:
        others += character
print(digits)
print(letters)
print(others)
