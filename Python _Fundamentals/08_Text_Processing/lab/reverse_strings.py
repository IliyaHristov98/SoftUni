while True:
    string = input()
    if string == "end":
        break

    reversed_string = ""
    for i in reversed(string):
        reversed_string += i

    print(f"{string} = {reversed_string}")
