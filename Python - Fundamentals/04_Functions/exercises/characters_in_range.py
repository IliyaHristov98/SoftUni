def between_characters(a, b):
    result = ""
    for i in range(ord(a) + 1, ord(b)):
        result += chr(i) + " "
    return result


beginning_character = input()
ending_character = input()

print(between_characters(beginning_character, ending_character))
