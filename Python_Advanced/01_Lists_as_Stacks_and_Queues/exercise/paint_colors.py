from collections import deque

words = deque(input().split())
colors = {"red", "yellow", "blue", "purple", "orange", "green"}
combinations = {
    "orange": {"red", "yellow"},
    "purple": {"blue", "red"},
    "green": {"yellow", "blue"},
}

result = []

while words:

    first = words.popleft()
    second = words.pop() if words else ""

    for color in (first + second, second + first):
        if color in colors:
            result.append(color)
            break
    else:
        for el in (first[:-1], second[:-1]):
            if el:
                words.insert(len(words) // 2, el)

for color in set(combinations.keys()).intersection(result):
    if not combinations[color].issubset(result):
        result.remove(color)

print(result)
