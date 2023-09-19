first = int(input())
second = int(input())
third = int(input())
largest = 0
if first > second and first > third:
    largest = first
elif second > first and second > third:
    largest = second
elif third > first and third > second:
    largest = third

print(largest)
