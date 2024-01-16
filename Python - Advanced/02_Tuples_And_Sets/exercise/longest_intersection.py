n = int(input())

longest_intersection = []

for _ in range(n):
    first, second = input().split("-")
    first_start, first_end = first.split(",")
    second_start, second_end = second.split(",")

    first_set = set(x for x in range(int(first_start), int(first_end) + 1))
    second_set = set(y for y in range(int(second_start), int(second_end) + 1))
    intersection = first_set & second_set

    if len(intersection) > len(longest_intersection):
        longest_intersection = []
        for digit in intersection:
            longest_intersection.append(digit)

print(f"Longest intersection is {longest_intersection} with length {len(longest_intersection)}")
