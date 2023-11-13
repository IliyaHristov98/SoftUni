n = int(input())
keys = {}
composers = {}

for _ in range(n):
    piece, composer, key = input().split("|")
    keys[piece] = key
    composers[piece] = composer

while True:
    command = input().split("|")
    if command[0] == "Stop":
        break

    if command[0] == "Add":
        piece = command[1]
        composer = command[2]
        key = command[3]
        if piece in composers:
            print(f"{piece} is already in the collection!")
        else:
            keys[piece] = key
            composers[piece] = composer
            print(f"{piece} by {composer} in {key} added to the collection!")

    elif command[0] == "Remove":
        piece = command[1]
        if piece in keys:
            del keys[piece]
            del composers[piece]
            print(f"Successfully removed {piece}!")
        else:
            print(f"Invalid operation! {piece} does not exist in the collection.")

    else:
        piece = command[1]
        new_key = command[2]
        if piece in keys:
            keys[piece] = new_key
            print(f"Changed the key of {piece} to {new_key}!")
        else:
            print(f"Invalid operation! {piece} does not exist in the collection.")

for song, value in keys.items():
    print(f"{song} -> Composer: {composers[song]}, Key: {keys[song]}")
