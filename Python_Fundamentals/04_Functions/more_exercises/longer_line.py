from math import sqrt, floor


def longer_line(a, b, c, d, a1, b1, c1, d1):
    first_line = sqrt(a ** 2 + b ** 2)
    second_line = sqrt(c ** 2 + d ** 2)
    third_line = sqrt(a1 ** 2 + b1 ** 2)
    fourth_line = sqrt(c1 ** 2 + d1 ** 2)

    if first_line + second_line < third_line + fourth_line:
        if third_line <= fourth_line:
            return f"({floor(a1)}, {floor(b1)})({floor(c1)}, {floor(d1)})"
        else:
            return f"({floor(c1)}, {floor(d1)})({floor(a1)}, {floor(b1)})"
    else:
        if first_line <= second_line:
            return f"({floor(a)}, {floor(b)})({floor(c)}, {floor(d)})"
        else:
            return f"({floor(c)}, {floor(d)})({floor(a)}, {floor(b)})"


first = float(input())
second = float(input())
third = float(input())
fourth = float(input())
fifth = float(input())
sixth = float(input())
seventh = float(input())
eighth = float(input())

print(longer_line(first, second, third, fourth, fifth, sixth, seventh, eighth))
