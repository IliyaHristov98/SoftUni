hundreds_max = int(input())
tens_max = int(input())
ones_max = int(input())

for first in range(1, hundreds_max + 1):
    if first % 2 == 0:

        for second in range(2, tens_max + 1):
            if second == 2 or second == 3 or second == 5 or second == 7:

                for third in range(1, ones_max + 1):
                    if third % 2 == 0:
                        print(f'{first} {second} {third}')
