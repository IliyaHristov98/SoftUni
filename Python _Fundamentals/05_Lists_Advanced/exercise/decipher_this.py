secret_message = input().split()
final_message = []

for word in secret_message:
    code = ''
    list_of_word = list(word)
    for letter in word:
        if letter.isdigit():
            code += letter
            list_of_word.remove(letter)

    list_of_word.insert(0, chr(int(code)))
    list_of_word[1], list_of_word[-1] = list_of_word[-1], list_of_word[1]

    final_word = "".join(list_of_word)
    final_message.append(final_word)

print(" ".join(final_message))
