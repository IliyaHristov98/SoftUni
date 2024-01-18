from collections import deque

chocolates = [int(x) for x in input().split(", ")]
cups_of_milk = deque([int(x) for x in input().split(", ")])
milkshakes = 0

while milkshakes != 5 and cups_of_milk and chocolates:
    choc = chocolates.pop()
    cup = cups_of_milk.popleft()

    if choc <= 0 and cup <= 0:
        continue
    elif choc <= 0:
        cups_of_milk.appendleft(cup)
        continue
    elif cup <= 0:
        chocolates.append(choc)
        continue

    if choc == cup:
        milkshakes += 1
    else:
        cups_of_milk.append(cup)
        chocolates.append(choc - 5)

if milkshakes == 5:
    print(f"Great! You made all the chocolate milkshakes needed!")
else:
    print("Not enough milkshakes.")

print(f"Chocolate: {', '.join(str(x) for x in chocolates) or 'empty'}")
print(f"Milk: {', '.join(str(x) for x in cups_of_milk) or 'empty'}")
