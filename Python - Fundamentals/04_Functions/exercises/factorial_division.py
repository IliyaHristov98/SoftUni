def factorial_division(a, b):
    factorial_of_a = a
    factorial_of_b = b
    for x in range(a - 1, 0, -1):
        factorial_of_a = factorial_of_a * x

    for y in range(b - 1, 0, -1):
        factorial_of_b = factorial_of_b * y

    return f"{factorial_of_a / factorial_of_b:.2f}"


first_number = int(input())
second_number = int(input())
print(factorial_division(first_number, second_number))
