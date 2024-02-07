from math import floor

word = input()
most_powerful_word = ''
strength_of_the_word = 0
while word != 'End of words':
    strength = 0
    for n in range(len(word)):
        strength += ord(word[n])

    if word[0] == 'a' or word[0] == 'e' or word[0] == 'i'\
            or word[0] == 'o' or word[0] == 'u' or word[0] == 'y' or word[0] == 'A'\
        or word[0] == 'E' or word[0] == 'I' or word[0] == 'O' or word[0] == 'U'\
        or word[0] == 'Y':
        strength = strength * len(word)
    else:
        strength = floor(strength / len(word))

    if strength > strength_of_the_word:
        strength_of_the_word = strength
        most_powerful_word = word
    word = input()
print(f'The most powerful word is {most_powerful_word} - {strength_of_the_word}')

