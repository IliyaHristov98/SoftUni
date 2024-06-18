command = input().split()
final_string = ""

for word in command:
    for i in range(len(word)):
        final_string += word

print(final_string)
