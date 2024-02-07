from math import log

number = int(input())
base = input()

try:
    print(f"{log(number, int(base)):.2f}")
except (TypeError, ValueError):
    print(f"{log(number):.2f}")
