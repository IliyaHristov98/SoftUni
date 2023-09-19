import sys
result = 0
n = sys.maxsize

for numbers in range(n):
    a = float(input())
    result = a * 2
    if a < 0:
        print("Negative number!")
        break
    else:
        print(f'Result: {result:.2f}')