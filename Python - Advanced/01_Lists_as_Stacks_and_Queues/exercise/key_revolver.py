from collections import deque

price_per_bullet = int(input())
barrel_size = int(input())
bullets = [int(x) for x in input().split()]
locks = deque([int(y) for y in input().split()])
value = int(input())
used_bullets = 0

while locks:

    if not bullets:
        break

    if used_bullets % barrel_size == 0 and used_bullets != 0:
        print("Reloading!")

    lock_current = locks.popleft()
    bullet_current = bullets.pop()
    used_bullets += 1
    if lock_current < bullet_current:
        print("Ping!")
        locks.appendleft(lock_current)
        continue
    else:
        print("Bang!")
        if used_bullets % barrel_size == 0 and bullets and not locks:
            print("Reloading!")

if locks:
    print(f"Couldn't get through. Locks left: {len(locks)}")
else:
    earned = value - (used_bullets * price_per_bullet)
    print(f"{len(bullets)} bullets left. Earned ${earned}")
