strings = input().split()
one = strings[0]
two = strings[1]
total_sum = 0
if len(one) == len(two):
    for i in range(len(one)):
        total_sum += ord(one[i]) * ord(two[i])
elif len(one) > len(two):
    for i in range(len(two)):
        total_sum += ord(one[i]) * ord(two[i])

    for x in range(len(two), len(one)):
        total_sum += ord(one[x])
else:
    for i in range(len(one)):
        total_sum += ord(one[i]) * ord(two[i])

    for x in range(len(one), len(two)):
        total_sum += ord(two[x])

print(total_sum)
