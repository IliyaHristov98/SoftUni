n = int(input())
guests = set()

for _ in range(n):
    guest = input()
    guests.add(guest)

while True:
    guest_came = input()

    if guest_came == "END":
        break

    if guest_came in guests:
        guests.remove(guest_came)

print(len(guests))

for left in sorted(guests):
    print(left)
