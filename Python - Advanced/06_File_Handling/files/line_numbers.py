from string import punctuation

with open("resources\\text.txt") as file:
    text = file.readlines()

output = open("resources\\output.txt", "w")

for row in range(len(text)):
    letters, marks = 0, 0

    for symbol in text[row]:

        if symbol.isalpha():
            letters += 1
        elif symbol in punctuation:
            marks += 1

    output.write(f"Line {row + 1}: {text[row][:-1]} ({letters})({marks})\n")

output.close()
