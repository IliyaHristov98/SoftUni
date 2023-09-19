divisor = int(input())
boundary = int(input())
largest_integer = 0
for number in range(boundary + 1):
    if number % divisor == 0:
        largest_integer = number
print(largest_integer)
