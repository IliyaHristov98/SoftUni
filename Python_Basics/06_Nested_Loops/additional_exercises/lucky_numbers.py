n = int(input())

for one in range(1, 10):
    for two in range(1, 10):
        if n % (one + two) == 0:

            for three in range(1, 10):
                for four in range(1, 10):
                    if three + four == one + two:
                        print(f"{one}{two}{three}{four}", end=" ")
