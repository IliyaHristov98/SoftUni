from collections import deque

MAX_CAFFEINE = 300
caffeine = 0
mls_of_caffeine = [int(x) for x in input().split(", ")]
drinks = deque([int(x) for x in input().split(", ")])

while mls_of_caffeine and drinks:
    caff, drink = mls_of_caffeine.pop(), drinks.popleft()
    total_caff = caff * drink

    if caffeine + total_caff <= MAX_CAFFEINE:
        caffeine += total_caff
    else:
        drinks.append(drink)
        if caffeine - 30 < 0:
            caffeine = 0
        else:
            caffeine -= 30

if drinks:
    print(f'Drinks left: {", ".join(map(str, drinks))}')
else:
    print("At least Stamat wasn't exceeding the maximum caffeine.")

print(f"Stamat is going to sleep with {caffeine} mg caffeine.")
