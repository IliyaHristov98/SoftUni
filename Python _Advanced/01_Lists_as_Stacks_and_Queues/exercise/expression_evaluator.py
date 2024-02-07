from collections import deque
from math import floor

expression = deque(input().split())
last = deque()
result = None

for _ in range(len(expression)):
    current = expression.popleft()
    if current not in "-+/*":
        last.append(current)
    else:
        result = int(last.popleft())
        if current == "-":
            while last:
                result -= int(last.popleft())
        elif current == "+":
            while last:
                result += int(last.popleft())
        elif current == "*":
            while last:
                result *= int(last.popleft())
        elif current == "/":
            while last:
                result /= int(last.popleft())

        last.append(result)

print(floor(result))
