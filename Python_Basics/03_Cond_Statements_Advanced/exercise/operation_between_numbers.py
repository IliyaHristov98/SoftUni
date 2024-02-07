n1 = int(input())
n2 = int(input())
operator = input()

total = 0

if operator == '/' and n2 == 0:
    print(f"Cannot divide {n1} by zero")
elif operator == '%' and n2 == 0:
    print(f"Cannot divide {n1} by zero")
elif operator == '+':
    total = n1 + n2
    if total % 2 == 0:
        print(f"{n1} {operator} {n2} = {total} - even")
    else:
        print(f"{n1} {operator} {n2} = {total} - odd")
elif operator == '-':
    total = n1 - n2
    if total % 2 == 0:
        print(f"{n1} {operator} {n2} = {total} - even")
    else:
        print(f"{n1} {operator} {n2} = {total} - odd")
elif operator == '*':
    total = n1 * n2
    if total % 2 == 0:
        print(f"{n1} {operator} {n2} = {total} - even")
    else:
        print(f"{n1} {operator} {n2} = {total} - odd")
elif operator == '/':
    total = n1 / n2
    print(f"{n1} / {n2} = {total:.2f}")
elif operator == '%':
    total = n1 % n2
    print(f'{n1} % {n2} = {total}')