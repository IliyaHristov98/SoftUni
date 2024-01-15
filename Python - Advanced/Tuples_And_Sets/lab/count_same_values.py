values = tuple([float(x) for x in input().split()])

same_values = {}

for num in values:
    if num not in same_values:
        same_values[num] = values.count(num)

for key, value in same_values.items():
    print(f"{key} - {value} times")
