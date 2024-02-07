import re

sentence = input()
word = input()
word_to_find = fr"(?i)\b{word}\b"

regex = re.findall(word_to_find, sentence)
print(len(regex))
