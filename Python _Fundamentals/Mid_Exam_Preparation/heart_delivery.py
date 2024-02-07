neighbourhood = [int(x) for x in input().split("@")]
current_index = 0
while True:
    command = input()
    if command == "Love!":
        break
    jump = command.split()
    length = int(jump[1])
    current_index += length
    if current_index >= len(neighbourhood):
        current_index = 0

    neighbourhood[current_index] -= 2
    if neighbourhood[current_index] == 0:
        print(f"Place {current_index} has Valentine's day.")
    elif neighbourhood[current_index] < 0:
        print(f"Place {current_index} already had Valentine's day.")

fails = 0
for i in neighbourhood:
    if i > 0:
        fails += 1
print(f"Cupid's last position was {current_index}.")
if fails == 0:
    print(f"Mission was successful.")
else:
    print(f"Cupid has failed {fails} places.")
