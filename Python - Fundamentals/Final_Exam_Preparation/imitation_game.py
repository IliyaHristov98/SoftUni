encrypted_message = [x for x in input()]
while True:
    given_input = input()
    if given_input == "Decode":
        break

    command = given_input.split("|")
    if command[0] == "Move":
        letters = int(command[1])
        for i in range(letters):
            popped = encrypted_message.pop(0)
            encrypted_message.append(popped)
    elif command[0] == "Insert":
        index = int(command[1])
        value = command[2]
        firstPart = encrypted_message[:index]
        secondPart = encrypted_message[index:len(encrypted_message)]
        encrypted_message = []
        for letter in firstPart:
            encrypted_message.append(letter)
        for letter in value:
            encrypted_message.append(letter)
        for letter in secondPart:
            encrypted_message.append(letter)
    elif command[0] == "ChangeAll":
        substring = command[1]
        replacement = command[2]
        for i in range(len(encrypted_message)):
            if encrypted_message[i] == substring:
                encrypted_message[i] = replacement

print(f"The decrypted message is: {''.join(encrypted_message)}")
