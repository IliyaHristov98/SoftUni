import sys

numbers_count = int(input())
max = - sys.maxsize
min = sys.maxsize
for sequence in range(numbers_count):
    a = int(input())
    if a > max:
        max = a
    if a < min:
        min = a

print(f'Max number: {max}\nMin number: {min}')