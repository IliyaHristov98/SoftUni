number = int(input())

for i in range(1, number + 1):
    for j in range(i):
        print("*", end="")
    print()

for k in range(number - 1, 0, -1):
    for l in range(k):
        print("*", end="")
    print()
