food = float(input())
hay = float(input())
cover = float(input())
weight = float(input())
day = 0
force_stopped = False
while day < 30:
    day += 1
    food -= 0.3
    if day % 2 == 0:
        hay -= food * 0.05

    if day % 3 == 0:
        cover -= (1 / 3) * weight

    if food <= 0 or hay <= 0 or cover <= 0:
        force_stopped = True
        break

if force_stopped:
    print(f"Merry must go to the pet store!")
else:
    print(f"Everything is fine! Puppy is happy! Food: {food:.2f}, Hay: {hay:.2f}, Cover: {cover:.2f}.")
