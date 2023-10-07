import math


def closest_point(a, b, c, d):
    distance_first = math.sqrt(a ** 2 + b ** 2)
    distance_second = math.sqrt(c ** 2 + d ** 2)
    if distance_first > distance_second:
        return f"({int(c)}, {int(d)})"
    else:
        return f"({int(a)}, {int(b)})"


first = float(input())
second = float(input())
third = float(input())
fourth = float(input())

print(closest_point(first, second, third, fourth))
