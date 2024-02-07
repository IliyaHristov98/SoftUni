database = {}

while True:
    command = input()
    if command == "Lumpawaroo":
        break

    if "|" in command:
        side, user = command.split(" | ")
        user_in_data = False
        for key, value in database.items():
            if user in value:
                user_in_data = True
                break

        if user_in_data:
            continue
        else:
            if side not in database:
                database[side] = [user]
            else:
                database[side] += [user]

    elif "->" in command:
        user, side = command.split(" -> ")
        user_in_data = False
        user_key = None
        for key, value in database.items():
            if user in value:
                user_key = key
                user_in_data = True
                break

        if user_in_data:
            database[user_key].remove(user)
            if side in database:
                database[side] += [user]
            else:
                database[side] = [user]

        else:
            if side in database:
                database[side] += [user]
            else:
                database[side] = [user]

        print(f"{user} joins the {side} side!")

for key, value in database.items():
    if len(value) == 0:
        continue
    print(f"Side: {key}, Members: {len(value)}")
    for i in value:
        print(f"! {i}")
