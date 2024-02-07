import os
import re

words_path = os.path.join("resources", "words.txt")
text_path = os.path.join("resources", "input.txt")
output_path = os.path.join("resources", "output.txt")

with open(words_path) as file:
    looked_for_words = file.read()
    searched_words = [word.lower() for word in looked_for_words.split()]

with open(text_path) as file:
    content = file.read().lower()

words_count = {}

for searched_word in searched_words:
    pattern = re.compile(rf'\b{searched_word}\b')
    results = re.findall(pattern, content)
    words_count[searched_word] = len(results)

sorted_count = sorted(words_count.items(), key=lambda x: -x[1])

with open(output_path, "a") as file:
    for word, count in sorted_count:
        file.write(f"{word} - {count}\n")
