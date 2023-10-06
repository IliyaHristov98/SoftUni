given_numbers = input().split()
list_of_rounded_integers = []

for number in given_numbers:
    list_of_rounded_integers.append(round(float(number)))

print(list_of_rounded_integers)
