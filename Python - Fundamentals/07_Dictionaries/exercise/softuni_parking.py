n = int(input())
registered = {}

for _ in range(n):
    command = input().split()
    username = command[1]

    if command[0] == "register":
        license_plate = command[2]

        if username in registered and registered[username] == license_plate:
            print(f"ERROR: already registered with plate number {license_plate}")
        else:
            print(f"{username} registered {license_plate} successfully")
            registered[username] = license_plate

    else:

        if username not in registered:
            print(f"ERROR: user {username} not found")
        else:
            print(f"{username} unregistered successfully")
            del registered[username]

for key, value in registered.items():
    print(f"{key} => {value}")
