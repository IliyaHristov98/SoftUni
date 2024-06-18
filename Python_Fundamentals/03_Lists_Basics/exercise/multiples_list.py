factor = int(input())
count = int(input())
new_factor = factor
list_of_integers = []
while len(list_of_integers) < count:
    list_of_integers.append(new_factor)
    new_factor += factor

print(list_of_integers)
