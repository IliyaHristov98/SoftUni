from collections import deque

water = int(input())
queue_of_people = deque()
person = input()

while person != "Start":
    queue_of_people.append(person)
    person = input()

command = input().split()
while command[0] != "End":
    if len(command) == 1:
        liters = int(command[0])
        if liters <= water:
            print(f"{queue_of_people.popleft()} got water")
            water -= liters
        else:
            print(f"{queue_of_people.popleft()} must wait")
    else:
        liters = int(command[1])
        water += liters

    command = input().split()

print(f"{water} liters left")
