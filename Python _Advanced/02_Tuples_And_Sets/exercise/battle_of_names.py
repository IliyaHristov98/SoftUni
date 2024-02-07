n = int(input())

odd = set()
even = set()

for count in range(1, n + 1):
    name = input()
    ascii_total = 0
    for symbol in name:
        ascii_total += ord(symbol)

    if ascii_total // count % 2 == 0:
        even.add(ascii_total // count)
    else:
        odd.add(ascii_total // count)

if sum(odd) == sum(even):
    union = odd.union(even)
    print(*union, sep=", ")
elif sum(odd) > sum(even):
    difference = odd.difference(even)
    print(*difference, sep=", ")
else:
    sym_diff = odd.symmetric_difference(even)
    print(*sym_diff, sep=", ")
