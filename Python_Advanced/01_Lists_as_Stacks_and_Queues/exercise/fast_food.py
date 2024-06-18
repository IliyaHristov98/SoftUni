from collections import deque

quantity = int(input())
orders = deque(int(x) for x in input().split())
print(max(orders))

for order in orders.copy():
    if order <= quantity:
        orders.popleft()
        quantity -= order
    else:
        break

if orders:
    print(f"Orders left:", *orders)
else:
    print("Orders complete")
