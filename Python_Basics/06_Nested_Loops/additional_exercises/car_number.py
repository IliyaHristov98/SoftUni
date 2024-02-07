beginning = int(input())
ending = int(input())

for one in range(beginning, ending + 1):
    for two in range(beginning, ending + 1):
        for three in range(beginning, ending + 1):
            for four in range(beginning, ending + 1):

                if (one % 2 == 0 and four % 2 != 0) or (one % 2 != 0 and four % 2 == 0):
                    if one > four:
                        if (two + three) % 2 == 0:
                            special_number = f"{one}{two}{three}{four}"
                            print(special_number, end=" ")
