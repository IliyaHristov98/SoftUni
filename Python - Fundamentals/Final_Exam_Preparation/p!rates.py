cities = {}

while True:
    command = input()
    if command == "Sail":
        break

    command = command.split("||")
    city = command[0]
    population = int(command[1])
    gold = int(command[2])
    if city not in cities:
        cities[city] = [population, gold]
    else:
        cities[city][0] += population
        cities[city][1] += gold

while True:
    event = input()
    if event == "End":
        break

    event = event.split("=>")
    action = event[0]
    town = event[1]
    if action == "Plunder":
        people = int(event[2])
        gold = int(event[3])
        wiped_off = False
        if cities[town][0] - people <= 0:
            plundered = gold
            killed = cities[town][0]
            wiped_off = True
        elif cities[town][1] - gold <= 0:
            plundered = cities[town][1]
            killed = people
            wiped_off = True
        else:
            plundered = gold
            killed = people

        print(f"{town} plundered! {plundered} gold stolen, {killed} citizens killed.")
        cities[town][0] -= killed
        cities[town][1] -= plundered
        if wiped_off:
            print(f"{town} has been wiped off the map!")
            del cities[town]
    else:
        gold = int(event[2])
        if gold < 0:
            print(f"Gold added cannot be a negative number!")
        else:
            cities[town][1] += gold
            print(f"{gold} gold added to the city treasury. {town} now has {cities[town][1]} gold.")

if len(cities) == 0:
    print(f"Ahoy, Captain! All targets have been plundered and destroyed!")
else:
    print(f"Ahoy, Captain! There are {len(cities)} wealthy settlements to go to:")
    for key, values in cities.items():
        print(f"{key} -> Population: {values[0]} citizens, Gold: {values[1]} kg")
