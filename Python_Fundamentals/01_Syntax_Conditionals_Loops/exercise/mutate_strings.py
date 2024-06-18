first = input()
second = input()
last_printed_string = first
for character in range(len(first)):
    left = second[:character + 1]
    right = first[character + 1:]
    new_string = left + right
    if new_string != last_printed_string:
        print(new_string)
        last_printed_string = new_string
