n = int(input())
for _ in range(n):
    name = ""
    age = ""
    string = input()
    for i in range(len(string)):
        if string[i] == "@":
            for l in range(i + 1, len(string)):
                if string[l] == "|":
                    break
                else:
                    name += string[l]

        if string[i] == "#":
            for m in range(i + 1, len(string)):
                if string[m] == "*":
                    break
                else:
                    age += string[m]

    print(f"{name} is {age} years old.")
