string = input()
string = string.lower()

my_list = ["sand", "water", "fish", "sun"]
count = 0

for word in my_list:
    if word in string:
        word_count = string.count(word)
        count += word_count
print(count)
