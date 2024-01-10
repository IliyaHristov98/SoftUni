from collections import deque

quantity = int(input())
orders = deque(int(x) for x in input().split())
print(max(orders))

while orders:
    if orders.popleft() > quantity:
        break
    else:
        quantity -= orders.popleft()

if orders:
    print(f"Orders left: {' '.join(str(orders))}")
else:
    print("Orders complete")
