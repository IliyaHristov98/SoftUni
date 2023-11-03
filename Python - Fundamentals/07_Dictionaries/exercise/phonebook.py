phonebook = {}

while True:
    given_input = input()
    if "-" not in given_input:
        break
    person, number = given_input.split("-")
    phonebook[person] = number

for i in range(int(given_input)):
    name = input()
    if name in phonebook:
        print(f"{name} -> {phonebook[name]}")
    else:
        print(f"Contact {name} does not exist.")
