x1 = int(input())
x2 = int(input())
x3 = int(input())


def negative_result(a, b, c):
    list_of_numbers = [a, b, c]
    negative_count = 0
    for i in list_of_numbers:
        if i < 0:
            negative_count += 1

    if a == 0 or b == 0 or c == 0:
        return "zero"
    elif negative_count % 2 == 0:
        return "positive"
    else:
        return "negative"


print(negative_result(x1, x2, x3))
