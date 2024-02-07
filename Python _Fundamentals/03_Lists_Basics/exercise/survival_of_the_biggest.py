from sys import maxsize
list_as_string = input().split()
number = int(input())
list_as_integer = []
for string in list_as_string:
    list_as_integer.append(int(string))

for n in range(number):
    current_smallest = maxsize
    for integer in list_as_integer:
        if integer < current_smallest:
            current_smallest = integer
    list_as_integer.remove(current_smallest)

print(", ".join(map(str, list_as_integer)))
