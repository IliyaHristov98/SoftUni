coins = [int(x) for x in input().split(", ")]
target = int(input())

coins.sort(reverse=True)
results = {x: 0 for x in coins}

for coin in coins:
    times = target // coin
    results[coin] = times
    target -= times * coin

    if target == 0:
        break

if target != 0:
    print("Error")
    raise SystemExit

print(f"Number of coins to take: {sum(results.values())}")
for key, value in results.items():
    if value > 0:
        print(f"{value} coin(s) with value {key}")
