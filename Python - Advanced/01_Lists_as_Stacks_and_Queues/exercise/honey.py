from collections import deque

bees = deque([int(x) for x in input().split()])
amount_of_nectar = [int(x) for x in input().split()]
symbols = deque(input().split())
total_honey = 0
while bees and amount_of_nectar:
    bee = bees.popleft()
    nectar = amount_of_nectar.pop()

    if nectar < bee:
        bees.appendleft(bee)
    else:
        symbol = symbols.popleft()
        if symbol == "+":
            total_honey += abs(bee + nectar)
        elif symbol == "-":
            total_honey += abs(bee - nectar)
        elif symbol == "*":
            total_honey += abs(bee * nectar)
        elif symbol == "/" and nectar != 0:
            total_honey += abs(bee / nectar)

print(f"Total honey made: {total_honey}")
if bees:
    print(f"Bees left: {', '.join(str(x) for x in bees)}")
if amount_of_nectar:
    print(f"Nectar left: {', '.join(str(x) for x in amount_of_nectar)}")
