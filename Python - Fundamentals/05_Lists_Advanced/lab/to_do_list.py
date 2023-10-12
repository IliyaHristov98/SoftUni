list_of_notes = [0] * 10
while True:
    command = input().split("-")
    if command[0] == "End":
        break
    note = command[1]
    index = int(command[0]) - 1
    list_of_notes.pop(index)
    list_of_notes.insert(index, note)

result = [i for i in list_of_notes if i != 0]
print(result)
