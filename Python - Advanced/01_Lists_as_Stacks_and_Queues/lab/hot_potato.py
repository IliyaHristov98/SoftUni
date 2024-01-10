from collections import deque

children = deque(input().split())
fired_count = int(input()) - 1

while len(children) > 1:
    children.rotate(-fired_count)
    print(f"Removed {children.popleft()}")

print(f"Last is {children.popleft()}")
