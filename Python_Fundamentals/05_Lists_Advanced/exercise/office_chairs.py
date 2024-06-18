rooms = int(input())
all_good = True
excess_chairs = 0

for room in range(rooms):
    chairs = input().split()
    available_chairs = len(chairs[0])
    people = int(chairs[1])
    if available_chairs < people:
        all_good = False
        print(f"{people - available_chairs} more chairs needed in room {room + 1}")
    else:
        excess_chairs += available_chairs - people
if all_good:
    print(f"Game On, {excess_chairs} free chairs left")
