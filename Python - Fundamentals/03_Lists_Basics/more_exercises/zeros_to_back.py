list_of_strings = input().split(', ')
list_of_integers = []
number_of_zeros = 0
for integer in list_of_strings:
    list_of_integers.append(int(integer))

while 0 in list_of_integers:
    number_of_zeros += 1
    list_of_integers.remove(0)

for i in range(number_of_zeros):
    list_of_integers.append(0)
print(list_of_integers)
